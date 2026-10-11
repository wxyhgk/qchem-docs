#!/usr/bin/env python3
"""
Full site builder for Q-Chem 7.0 User's Manual MkDocs Material Site.
"""

import os
import re
import sys
import shutil
from pathlib import Path
from bs4 import BeautifulSoup
import yaml

from latexml_to_md import convert_html_to_md, clean_latex

ROOT_DIR = Path(__file__).resolve().parent.parent
CRAWL_DIR = ROOT_DIR / "crawl"
HTML_DIR = CRAWL_DIR / "html"
ASSETS_DIR = CRAWL_DIR / "assets"
DOCS_SITE_DIR = ROOT_DIR / "docs-site"
DOCS_DIR = DOCS_SITE_DIR / "docs"
EN_DIR = DOCS_DIR / "en"
ZH_DIR = DOCS_DIR / "zh"
SITE_ASSETS_DIR = DOCS_DIR / "assets"

CHAPTER_META = {
    "chap_intro.html": ("ch01_intro", "Chapter 1: Introduction"),
    "chap_install.html": ("ch02_install", "Chapter 2: Installation, Customization, and Execution"),
    "chap_inputs.html": ("ch03_inputs", "Chapter 3: Q-Chem Inputs"),
    "chap_scf.html": ("ch04_scf", "Chapter 4: Self-Consistent Field Ground-State Methods"),
    "chap_DFT.html": ("ch05_dft", "Chapter 5: Density Functional Theory"),
    "chap_correlation.html": ("ch06_correlation", "Chapter 6: Wave Function-Based Correlation Methods"),
    "chap_excited.html": ("ch07_excited", "Chapter 7: Open-Shell and Excited-State Methods"),
    "chap_basis.html": ("ch08_basis", "Chapter 8: Basis Sets and Effective Core Potentials"),
    "chap_opt.html": ("ch09_opt", "Chapter 9: Exploring Potential Energy Surfaces"),
    "chap_properties.html": ("ch10_properties", "Chapter 10: Molecular Properties and Analysis"),
    "chap_env.html": ("ch11_env", "Chapter 11: Molecules in Complex Environments"),
    "chap_frag.html": ("ch12_frag", "Chapter 12: Fragment-Based Methods"),
    "chap_specialized_topics.html": ("ch13_specialized", "Chapter 13: Specialized Topics"),
    "app_AOINTS.html": ("app_a_aoints", "Appendix A: AOInts: Q-Chem’s Integrals Engine"),
    "app_quick_ref.html": ("app_b_quickref", "Appendix B: Q-Chem Quick Reference"),
    "app_thirdparty.html": ("app_c_thirdparty", "Appendix C: Third-party Components"),
    "bib.html": ("bib_references", "References and Further Reading")
}

def clean_title(raw_title):
    t = re.sub(r'\s*‣.*$', '', raw_title).strip()
    t = re.sub(r'\s+', ' ', t)
    return t

def parse_navigation_and_maps():
    """Parse index.html navbar to extract hierarchy tree and URL -> doc mappings."""
    index_path = HTML_DIR / "index.html"
    with open(index_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    nav = soup.find("nav", class_="ltx_page_navbar")
    url_to_doc = {}
    doc_titles = {}

    # Map bib and index
    url_to_doc["index.html"] = "index.md"
    url_to_doc["bib.html"] = "bib_references/bib.md"
    doc_titles["index.html"] = "Home"
    doc_titles["bib.html"] = "References and Further Reading"

    def scan_node(li, current_chapter_dir):
        btn_or_a = li.find(["button", "a"], recursive=False)
        if not btn_or_a:
            return None
        href = btn_or_a.get("href", "")
        title = btn_or_a.get("title", btn_or_a.get_text(" ", strip=True))
        title = clean_title(title)
        
        clean_h = href.split("#")[0] if href else ""
        if clean_h and clean_h not in ["index.html", "#"]:
            stem = Path(clean_h).stem
            doc_rel = f"{current_chapter_dir}/{stem}.md"
            url_to_doc[clean_h] = doc_rel
            doc_titles[clean_h] = title

        children = []
        sub_div = li.find("div", class_="content0", recursive=False)
        if sub_div:
            sub_ul = sub_div.find("ul", recursive=False)
            if sub_ul:
                for sub_li in sub_ul.find_all("li", recursive=False):
                    child = scan_node(sub_li, current_chapter_dir)
                    if child:
                        children.append(child)
        return {"href": clean_h, "title": title, "children": children}

    root_ul = nav.find("ul", class_="ltx_toclist")
    chapters_tree = []

    for li in root_ul.find_all("li", recursive=False):
        btn_or_a = li.find(["button", "a"], recursive=False)
        if not btn_or_a:
            continue
        href = btn_or_a.get("href", "")
        clean_h = href.split("#")[0] if href else ""
        if clean_h in ["index.html", "#"] or not clean_h:
            continue

        chap_dir, chap_name = CHAPTER_META.get(clean_h, (f"ch_{clean_h}", clean_h))
        stem = Path(clean_h).stem
        doc_rel = f"{chap_dir}/{stem}.md"
        url_to_doc[clean_h] = doc_rel
        doc_titles[clean_h] = chap_name

        # Parse subsections
        chap_node = scan_node(li, chap_dir)
        if chap_node:
            chap_node["dir"] = chap_dir
            chap_node["title"] = chap_name
            chapters_tree.append(chap_node)

    # Any remaining unmapped html files in HTML_DIR
    for p in HTML_DIR.glob("*.html"):
        name = p.name
        if name not in url_to_doc:
            url_to_doc[name] = f"ch01_intro/{p.stem}.md"

    return chapters_tree, url_to_doc, doc_titles

def create_url_mapper(url_to_doc):
    def mapper(href, current_doc):
        if not href or href.startswith("http") or href.startswith("mailto:"):
            return href
        parts = href.split("#", 1)
        target_file = parts[0]
        anchor = f"#{parts[1]}" if len(parts) > 1 else ""

        if not target_file:
            return anchor

        if target_file in url_to_doc:
            target_doc = url_to_doc[target_file]
            curr_dir = os.path.dirname(current_doc)
            rel_path = os.path.relpath(target_doc, start=curr_dir)
            return rel_path + anchor
        return href
    return mapper

def build_mkdocs_nav(chapters_tree, url_to_doc):
    """Build nav YAML data structure for MkDocs."""
    nav = [{"Home": "index.md"}]

    def node_to_nav(node):
        title = node["title"]
        href = node["href"]
        children = node.get("children", [])
        doc_rel = url_to_doc.get(href, "")

        if not children:
            return {title: doc_rel}

        child_navs = []
        # If node itself has a doc, include it as first entry
        if doc_rel:
            child_navs.append({title: doc_rel})

        for c in children:
            child_navs.append(node_to_nav(c))

        return {title: child_navs}

    for chap in chapters_tree:
        chap_title = chap["title"]
        chap_href = chap["href"]
        chap_doc = url_to_doc.get(chap_href, "")
        children = chap.get("children", [])

        if not children:
            nav.append({chap_title: chap_doc})
        else:
            chap_entries = []
            if chap_doc:
                chap_entries.append({"Overview": chap_doc})
            for c in children:
                chap_entries.append(node_to_nav(c))
            nav.append({chap_title: chap_entries})

    # Add bibliography
    nav.append({"References": "bib_references/bib.md"})
    return nav

def generate_home_page():
    """Generate modern, attractive landing index.md."""
    lines = [
        "---",
        "title: Q-Chem 7.0 User's Manual",
        "hide:",
        "  - navigation",
        "---",
        "",
        "# Q-Chem 7.0 User's Manual",
        "",
        '<div style="text-align:center; margin: 1.5rem 0 2.5rem 0;">',
        '  <img src="assets/logo.svg" alt="Q-Chem Logo" style="max-height: 90px; margin-bottom: 1rem;">',
        '  <p style="font-size: 1.15rem; color: var(--md-default-fg-color--light);">',
        '    Comprehensive documentation, theoretical background, and execution guide for Q-Chem 7.0 quantum chemistry software package.',
        '  </p>',
        '  <div style="margin-top: 1rem;">',
        '    <a class="md-button md-button--primary" href="ch01_intro/chap_intro.md" style="margin-right: 0.5rem;">📖 Get Started</a>',
        '    <a class="md-button" href="assets/qchem_manual.pdf" target="_blank" download>⬇️ Download PDF Manual (5.5 MB)</a>',
        '  </div>',
        '</div>',
        "",
        "## Chapters Overview",
        "",
        '<div class="grid cards" markdown>',
        "",
        "-   :material-book-open-page-variant: **[Chapter 1: Introduction](ch01_intro/chap_intro.md)**",
        "    ---",
        "    Overview of Q-Chem features, new capabilities in Q-Chem 7.0, and citation guidelines.",
        "",
        "-   :material-cog-box: **[Chapter 2: Installation & Execution](ch02_install/chap_install.md)**",
        "    ---",
        "    Setup, environment variables ($QCAUX), license configuration, IQmol integration, and job execution.",
        "",
        "-   :material-file-code-outline: **[Chapter 3: Q-Chem Inputs](ch03_inputs/chap_inputs.md)**",
        "    ---",
        "    Input structure, molecular coordinates (`$molecule`), `$rem` job controls, and batch execution.",
        "",
        "-   :material-atom-variant: **[Chapter 4: SCF Methods](ch04_scf/chap_scf.md)**",
        "    ---",
        "    Hartree-Fock, DIIS, convergence acceleration algorithms, linear-scaling O(N) methods, and xTB.",
        "",
        "-   :material-chart-bell-curve: **[Chapter 5: Density Functional Theory](ch05_dft/chap_DFT.md)**",
        "    ---",
        "    LDA, GGA, hybrid, range-separated (RSH), double-hybrid functionals, and empirical dispersion (DFT-D/vdW).",
        "",
        "-   :material-wave: **[Chapter 6: Wave Function Correlation](ch06_correlation/chap_correlation.md)**",
        "    ---",
        "    MP2, RI-MP2, local correlation, coupled cluster (CCSD, CCSD(T)), and active space methods.",
        "",
        "-   :material-lightning-bolt: **[Chapter 7: Excited States](ch07_excited/chap_excited.md)**",
        "    ---",
        "    CIS, TD-DFT, EOM-CC, ADC family, open-shell methods, and core-excited spectroscopy.",
        "",
        "-   :material-blur-radial: **[Chapter 8: Basis Sets & ECP](ch08_basis/chap_basis.md)**",
        "    ---",
        "    Standard Gaussian basis sets, effective core potentials, and user-defined mixed bases.",
        "",
        "-   :material-map-marker-path: **[Chapter 9: PES & Dynamics](ch09_opt/chap_opt.md)**",
        "    ---",
        "    Geometry optimization, transition state search (Freezing String, NEB), and ab initio molecular dynamics (AIMD).",
        "",
        "-   :material-flask: **[Chapter 10: Molecular Properties](ch10_properties/chap_properties.md)**",
        "    ---",
        "    Multipole moments, NBO, NMR shielding, polarizabilities, vibrational spectra, and energy decomposition (EDA).",
        "",
        "-   :material-water-outline: **[Chapter 11: Solvation & Environment](ch11_env/chap_env.md)**",
        "    ---",
        "    Continuum solvation models (PCM, SMD, COSMO), QM/MM interfaces, and embedding schemes.",
        "",
        "-   :material-puzzle: **[Chapter 12: Fragment-Based Methods](ch12_frag/chap_frag.md)**",
        "    ---",
        "    ALMO-EDA, absolutely localized molecular orbitals, and large-scale fragment calculations.",
        "",
        "-   :material-creation: **[Chapter 13: Specialized Topics](ch13_specialized/chap_specialized_topics.md)**",
        "    ---",
        "    Non-adiabatic dynamics, electron transport, and quantum computing interfaces.",
        "",
        "-   :material-format-list-bulleted: **[Appendix B: Quick Reference](app_b_quickref/app_quick_ref.md)**",
        "    ---",
        "    Complete alphabetical listing of all `$rem` keywords, default values, and valid options.",
        "",
        "</div>",
        ""
    ]
    return "\n".join(lines)

def build_all():
    print("[*] Starting site conversion...")

    # 1. Parse tree and mappings
    chapters_tree, url_to_doc, doc_titles = parse_navigation_and_maps()
    print(f"[*] Parsed {len(chapters_tree)} chapters and {len(url_to_doc)} document mappings.")

    # 2. Setup directories
    if DOCS_DIR.exists():
        shutil.rmtree(DOCS_DIR)
    EN_DIR.mkdir(parents=True, exist_ok=True)
    ZH_DIR.mkdir(parents=True, exist_ok=True)
    SITE_ASSETS_DIR.mkdir(parents=True, exist_ok=True)

    # 3. Copy assets
    print("[*] Copying assets (images, figures, pdf)...")
    for item in ASSETS_DIR.iterdir():
        if item.is_file():
            shutil.copy2(item, SITE_ASSETS_DIR / item.name)
        elif item.is_dir():
            target_sub = SITE_ASSETS_DIR / item.name
            if target_sub.exists():
                shutil.rmtree(target_sub)
            shutil.copytree(item, target_sub)

    # Also make assets available directly inside en/assets and zh/assets
    # And copy any subfolder files (like Figures/*) to assets root
    figs_dir = ASSETS_DIR / "Figures"
    if figs_dir.exists():
        for f in figs_dir.iterdir():
            if f.is_file():
                shutil.copy2(f, SITE_ASSETS_DIR / f.name)

    shutil.copytree(SITE_ASSETS_DIR, EN_DIR / "assets", dirs_exist_ok=True)
    shutil.copytree(SITE_ASSETS_DIR, ZH_DIR / "assets", dirs_exist_ok=True)

    # 4. Convert all HTML pages to Markdown for English
    print(f"[*] Converting {len(url_to_doc)} pages to Markdown...")
    url_mapper = create_url_mapper(url_to_doc)

    converted_count = 0
    for html_name, doc_rel in url_to_doc.items():
        if html_name == "index.html":
            # Generate custom landing page
            en_md = generate_home_page()
        else:
            html_file = HTML_DIR / html_name
            if not html_file.exists():
                continue
            with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
                raw_html = f.read()

            title = doc_titles.get(html_name, Path(html_name).stem)
            curr_doc_path = doc_rel
            depth = len(Path(doc_rel).parts) - 1
            asset_rel = "../" * depth + "assets"

            body_md = convert_html_to_md(
                raw_html,
                url_mapper=url_mapper,
                current_doc=curr_doc_path,
                asset_rel_path=asset_rel
            )
            en_md = f"---\ntitle: \"{title}\"\n---\n\n{body_md}\n"

        target_en_file = EN_DIR / doc_rel
        target_en_file.parent.mkdir(parents=True, exist_ok=True)
        with open(target_en_file, "w", encoding="utf-8") as f:
            f.write(en_md)

        # Mirror to zh (ready for translation)
        target_zh_file = ZH_DIR / doc_rel
        target_zh_file.parent.mkdir(parents=True, exist_ok=True)
        with open(target_zh_file, "w", encoding="utf-8") as f:
            f.write(en_md)

        converted_count += 1
        if converted_count % 100 == 0:
            print(f"    Progress: {converted_count}/{len(url_to_doc)} documents converted...")

    print(f"[+] All {converted_count} documents converted into docs/en and mirrored to docs/zh.")

    # 5. Build mkdocs.yml
    print("[*] Generating mkdocs.yml...")
    nav_data = build_mkdocs_nav(chapters_tree, url_to_doc)

    mkdocs_config = {
        "site_name": "Q-Chem 7.0 User's Manual",
        "site_description": "Q-Chem 7.0 量子化学软件用户手册与理论指南",
        "site_author": "Q-Chem, Inc.",
        "site_url": "",
        "use_directory_urls": True,
        "docs_dir": "docs",
        "site_dir": "site",
        "theme": {
            "name": "material",
            "language": "en",
            "palette": [
                {
                    "media": "(prefers-color-scheme: light)",
                    "scheme": "default",
                    "primary": "indigo",
                    "accent": "indigo",
                    "toggle": {
                        "icon": "material/weather-night",
                        "name": "Switch to dark mode"
                    }
                },
                {
                    "media": "(prefers-color-scheme: dark)",
                    "scheme": "slate",
                    "primary": "indigo",
                    "accent": "indigo",
                    "toggle": {
                        "icon": "material/weather-sunny",
                        "name": "Switch to light mode"
                    }
                }
            ],
            "features": [
                "navigation.tracking",
                "navigation.tabs",
                "navigation.sections",
                "navigation.top",
                "navigation.footer",
                "search.suggest",
                "search.highlight",
                "content.code.copy",
                "content.tabs.link",
                "toc.follow"
            ],
            "logo": "assets/logo.svg",
            "favicon": "assets/1.png"
        },
        "plugins": [
            "search",
            {
                "i18n": {
                    "docs_structure": "folder",
                    "languages": [
                        {
                            "locale": "en",
                            "default": True,
                            "name": "English",
                            "build": True
                        },
                        {
                            "locale": "zh",
                            "name": "中文",
                            "build": True
                        }
                    ]
                }
            }
        ],
        "markdown_extensions": [
            "admonition",
            "pymdownx.details",
            "pymdownx.superfences",
            "pymdownx.highlight",
            "pymdownx.inlinehilite",
            "pymdownx.tabbed",
            "tables",
            "footnotes",
            "attr_list",
            "md_in_html",
            {
                "pymdownx.arithmatex": {
                    "generic": True
                }
            }
        ],
        "extra_javascript": [
            "https://polyfill.io/v3/polyfill.min.js?features=es6",
            "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js",
            "assets/mathjax.js"
        ],
        "nav": nav_data
    }

    # MathJax configuration script
    mathjax_js_content = """window.MathJax = {
  tex: {
    inlineMath: [["\\$", "\\$"], ["\\\\(", "\\\\)"]],
    displayMath: [["\\$\\$", "\\$\\$"], ["\\\\[", "\\\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  }
};
"""
    with open(SITE_ASSETS_DIR / "mathjax.js", "w", encoding="utf-8") as f:
        f.write(mathjax_js_content)

    mkdocs_file = DOCS_SITE_DIR / "mkdocs.yml"
    with open(mkdocs_file, "w", encoding="utf-8") as f:
        yaml.dump(mkdocs_config, f, allow_unicode=True, sort_keys=False, width=120)

    print(f"[✓] mkdocs.yml generated successfully at {mkdocs_file}")

if __name__ == "__main__":
    build_all()
