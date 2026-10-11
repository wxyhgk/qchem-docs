#!/usr/bin/env python3
"""
LaTeXML HTML to Markdown Converter for Q-Chem 7.0 User's Manual
"""

import os
import re
import sys
import html
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

def clean_latex(alt):
    if not alt:
        return ""
    # Remove LaTeXML line continuation comments: %\n
    alt = re.sub(r'%\s*\n\s*', '', alt)
    alt = alt.strip()
    return alt

def extract_remblock(rem_div, url_mapper=None, current_doc=""):
    """Format a Q-Chem $rem parameter block into a clean, readable Markdown card."""
    bold_tag = rem_div.find("span", class_="ltx_font_bold")
    var_name = bold_tag.get_text(strip=True) if bold_tag else "VARIABLE"

    # Convert inner content to text/markdown
    # We can inspect the sections inside remblock
    text_lines = []
    
    # Process internal math first
    for m in rem_div.find_all("math"):
        alt = clean_latex(m.get("alttext", ""))
        m.replace_with(f"${alt}$")

    # Process internal links
    if url_mapper and current_doc:
        for a in rem_div.find_all("a"):
            href = a.get("href", "")
            if href and not href.startswith("http"):
                new_href = url_mapper(href, current_doc)
                a["href"] = new_href

    full_text = rem_div.get_text("\n")
    lines = [l.strip() for l in full_text.splitlines() if l.strip()]

    # Parse sections: Description, TYPE, DEFAULT, OPTIONS, RECOMMENDATION
    description = []
    var_type = ""
    default_val = ""
    options = []
    recommendation = []

    current_section = "desc"
    for line in lines:
        if line == var_name:
            continue
        if line.startswith("TYPE:"):
            current_section = "type"
            val = line[5:].strip()
            if val:
                var_type = val
            continue
        elif line.startswith("DEFAULT:"):
            current_section = "default"
            val = line[8:].strip()
            if val:
                default_val = val
            continue
        elif line.startswith("OPTIONS:"):
            current_section = "options"
            continue
        elif line.startswith("RECOMMENDATION:"):
            current_section = "rec"
            continue

        if current_section == "desc":
            description.append(line)
        elif current_section == "type" and not var_type:
            var_type = line
        elif current_section == "default" and not default_val:
            default_val = line
        elif current_section == "options":
            options.append(line)
        elif current_section == "rec":
            recommendation.append(line)

    md_out = [f"### `{var_name}`\n"]
    if description:
        desc_str = " ".join(description)
        md_out.append(f"> **{desc_str}**\n>")
    if var_type:
        md_out.append(f"> * **Type**: `{var_type}`")
    if default_val:
        md_out.append(f"> * **Default**: `{default_val}`")
    if options:
        opt_str = "\n>     * ".join(options)
        md_out.append(f"> * **Options**:\n>     * {opt_str}")
    if recommendation:
        rec_str = " ".join(recommendation)
        md_out.append(f"> * **Recommendation**: {rec_str}")

    md_out.append("\n")
    return "\n".join(md_out)

def convert_table(table_tag, url_mapper=None, current_doc=""):
    """Convert a BeautifulSoup table tag to a GFM Markdown table or clean HTML table."""
    # Check if table has rowspan or colspan
    has_spans = bool(table_tag.find(lambda t: t.has_attr("colspan") or t.has_attr("rowspan")))
    if has_spans:
        # Keep clean HTML table
        return f"\n\n{str(table_tag)}\n\n"

    rows = []
    for tr in table_tag.find_all("tr"):
        cells = []
        for td in tr.find_all(["th", "td"]):
            # Format cell content
            cell_txt = td.get_text(" ", strip=True)
            cell_txt = cell_txt.replace("|", "\\|").replace("\n", " ")
            cells.append(cell_txt)
        if cells:
            rows.append(cells)

    if not rows:
        return ""

    num_cols = max(len(r) for r in rows)
    # Pad rows
    for r in rows:
        while len(r) < num_cols:
            r.append("")

    header = rows[0]
    md_table = []
    md_table.append("| " + " | ".join(header) + " |")
    md_table.append("| " + " | ".join(["---"] * num_cols) + " |")
    for r in rows[1:]:
        md_table.append("| " + " | ".join(r) + " |")

    return "\n\n" + "\n".join(md_table) + "\n\n"

def convert_html_to_md(html_str, url_mapper=None, current_doc="", asset_rel_path="../assets"):
    soup = BeautifulSoup(html_str, "html.parser")

    # Find main content container
    content = soup.find("div", class_="ltx_page_content")
    if not content:
        content = soup.find("article", class_="ltx_document")
    if not content:
        content = soup.find("body")
    if not content:
        return ""

    # Remove unwanted elements
    for el in content.find_all(["header", "footer", "nav", "div.ltx_pagination"]):
        el.decompose()

    # Pre-process display equations: table.ltx_equation or table.ltx_eqn_table
    for eq_table in content.find_all("table", class_=lambda c: c and "ltx_equation" in c):
        math = eq_table.find("math")
        alt = clean_latex(math.get("alttext", "")) if math else ""
        
        # Check equation tag
        eqn_tag = eq_table.find(class_=lambda c: c and "ltx_tag_equation" in c)
        tag_str = ""
        if eqn_tag:
            tag_text = eqn_tag.get_text(strip=True).strip("()")
            if tag_text:
                tag_str = f" \\tag{{{tag_text}}}"

        eq_id = eq_table.get("id", "")
        anchor_str = f'<a id="{eq_id}"></a>\n\n' if eq_id else ""
        eq_md = f"\n\n{anchor_str}$$\n{alt}{tag_str}\n$$\n\n"
        eq_table.replace_with(soup.new_string(eq_md))

    # Pre-process bibliography items
    for li in content.find_all("li", class_=lambda c: c and "ltx_bibitem" in c):
        b_id = li.get("id", "")
        txt = li.get_text(" ", strip=True)
        anchor = f'<a id="{b_id}"></a> ' if b_id else ""
        li.replace_with(soup.new_string(f"\n- {anchor}{txt}\n"))

    # Pre-process inline math
    for math in content.find_all("math"):
        alt = clean_latex(math.get("alttext", ""))
        # Check if block
        if math.get("display") == "block":
            math.replace_with(soup.new_string(f"\n\n$$\n{alt}\n$$\n\n"))
        else:
            math.replace_with(soup.new_string(f"${alt}$"))

    # Pre-process examples: div.qexample
    for qex in content.find_all("div", class_="qexample"):
        cap = qex.find("div", class_="caption")
        cap_title = "Example"
        cap_desc = ""
        if cap:
            bold = cap.find("span", class_="ltx_font_bold")
            if bold:
                cap_title = bold.get_text(strip=True)
                bold.decompose()
            cap_desc = cap.get_text(" ", strip=True)

        qin = qex.find("div", class_=lambda c: c in ["qin", "qinput"] if c else False)
        code_str = ""
        if qin:
            pre = qin.find("pre")
            code_str = pre.get_text() if pre else qin.get_text()
        else:
            pre = qex.find("pre")
            code_str = pre.get_text() if pre else ""

        title_line = f'???+ example "{cap_title}: {cap_desc}"' if cap_desc else f'???+ example "{cap_title}"'
        ex_md = [title_line]
        ex_md.append("    ```qchem")
        for line in code_str.splitlines():
            ex_md.append(f"    {line}")
        ex_md.append("    ```\n")
        qex.replace_with(soup.new_string("\n\n" + "\n".join(ex_md) + "\n\n"))

    # Pre-process input blocks not in qexample: div.qin or div.qinput
    for qin in content.find_all("div", class_=lambda c: c in ["qin", "qinput"] if c else False):
        pre = qin.find("pre")
        code_str = pre.get_text() if pre else qin.get_text()
        md_code = f"\n\n```qchem\n{code_str.strip()}\n```\n\n"
        qin.replace_with(soup.new_string(md_code))

    # Pre-process generic verbatim <pre>
    for pre in content.find_all("pre", class_=lambda c: c and "ltx_verbatim" in c):
        code_str = pre.get_text()
        md_code = f"\n\n```qchem\n{code_str.strip()}\n```\n\n"
        pre.replace_with(soup.new_string(md_code))

    # Pre-process remblock
    for rem in content.find_all("div", class_="remblock"):
        md_rem = extract_remblock(rem, url_mapper=url_mapper, current_doc=current_doc)
        rem.replace_with(soup.new_string(md_rem))

    # Pre-process figures: figure.ltx_figure
    for fig in content.find_all("figure", class_="ltx_figure"):
        img = fig.find("img")
        caption = fig.find("figcaption")
        cap_text = caption.get_text(" ", strip=True) if caption else ""
        if img:
            src = img.get("src", "")
            img_filename = Path(src).name
            img_rel = f"{asset_rel_path}/{img_filename}"
            md_fig = f"\n\n![{cap_text}]({img_rel})\n\n*{cap_text}*\n\n"
            fig.replace_with(soup.new_string(md_fig))

    # Pre-process standalone images
    for img in content.find_all("img"):
        src = img.get("src", "")
        if src.startswith("data:"):
            img.decompose()
            continue
        alt = img.get("alt", "")
        img_filename = Path(src).name
        img_rel = f"{asset_rel_path}/{img_filename}"
        img.replace_with(soup.new_string(f"![{alt}]({img_rel})"))

    # Pre-process citations: cite.ltx_cite
    for cite in content.find_all("cite", class_="ltx_cite"):
        a_tag = cite.find("a")
        if a_tag:
            href = a_tag.get("href", "")
            text = a_tag.get_text(strip=True)
            if url_mapper and current_doc:
                href = url_mapper(href, current_doc)
            cite.replace_with(soup.new_string(f"[[{text}]]({href})"))

    # Pre-process tables
    for tbl in content.find_all("table", class_="ltx_tabular"):
        md_tbl = convert_table(tbl, url_mapper=url_mapper, current_doc=current_doc)
        tbl.replace_with(soup.new_string(md_tbl))

    # Process links: <a>
    if url_mapper and current_doc:
        for a in content.find_all("a"):
            href = a.get("href", "")
            if href and not href.startswith("http") and not href.startswith("mailto:") and not href.startswith("#"):
                new_href = url_mapper(href, current_doc)
                a["href"] = new_href

    # Convert node to Markdown text recursively
    md_text = render_markdown(content)
    
    # Clean up empty lines
    md_text = re.sub(r'\n{3,}', '\n\n', md_text).strip()
    return md_text

def render_markdown(element):
    """Recursively converts remaining HTML DOM into Markdown text."""
    if isinstance(element, NavigableString):
        return str(element)

    tag_name = element.name.lower() if element.name else ""

    # Headings
    if tag_name in ["h1", "h2", "h3", "h4", "h5", "h6"]:
        level = int(tag_name[1])
        # Check classes
        cls = element.get("class", [])
        if "ltx_title_subsection" in cls:
            level = 2
        elif "ltx_title_section" in cls:
            level = 1
        elif "ltx_title_chapter" in cls:
            level = 1
        
        inner = "".join(render_markdown(child) for child in element.children).strip()
        prefix = "#" * level
        return f"\n\n{prefix} {inner}\n\n"

    elif tag_name == "p":
        inner = "".join(render_markdown(child) for child in element.children).strip()
        if not inner:
            return ""
        return f"\n\n{inner}\n\n"

    elif tag_name in ["strong", "b"] or ("ltx_font_bold" in element.get("class", [])):
        inner = "".join(render_markdown(child) for child in element.children)
        return f"**{inner}**"

    elif tag_name in ["em", "i"] or ("ltx_font_italic" in element.get("class", [])):
        inner = "".join(render_markdown(child) for child in element.children)
        return f"*{inner}*"

    elif tag_name in ["code", "tt"] or ("ltx_font_typewriter" in element.get("class", [])):
        inner = "".join(render_markdown(child) for child in element.children)
        return f"`{inner}`"

    elif tag_name == "span" and "ltx_font_smallcaps" in element.get("class", []):
        inner = "".join(render_markdown(child) for child in element.children)
        return f"**{inner}**"

    elif tag_name == "a":
        href = element.get("href", "")
        inner = "".join(render_markdown(child) for child in element.children).strip()
        if not inner:
            return ""
        if not href:
            return inner
        return f"[{inner}]({href})"

    elif tag_name == "ul":
        items = []
        for child in element.children:
            if child.name == "li":
                item_txt = "".join(render_markdown(c) for c in child.children).strip()
                items.append(f"- {item_txt}")
        return "\n\n" + "\n".join(items) + "\n\n"

    elif tag_name == "ol":
        items = []
        idx = 1
        for child in element.children:
            if child.name == "li":
                item_txt = "".join(render_markdown(c) for c in child.children).strip()
                items.append(f"{idx}. {item_txt}")
                idx += 1
        return "\n\n" + "\n".join(items) + "\n\n"

    elif tag_name == "blockquote":
        inner = "".join(render_markdown(child) for child in element.children).strip()
        quoted = "\n".join(f"> {line}" for line in inner.splitlines())
        return f"\n\n{quoted}\n\n"

    elif tag_name in ["div", "section", "article", "span"]:
        return "".join(render_markdown(child) for child in element.children)

    elif tag_name == "br":
        return "\n"

    else:
        return "".join(render_markdown(child) for child in element.children)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        test_file = sys.argv[1]
        with open(test_file, "r", encoding="utf-8") as f:
            raw_html = f.read()
        res = convert_html_to_md(raw_html)
        print(res[:2000])
