"""
MkDocs hook: turn $molecule code blocks and fenced ```mol blocks into
interactive 3D | input panels powered by fast-mol.

Features:
1. Automatically detects code blocks containing $molecule ... $end with Cartesian coordinates.
2. Converts coordinates into standard XYZ format for the 3D viewer.
3. Preserves the full original Q-Chem input in the 'input' tab.
4. Supports explicit ```mol fence blocks as well.
"""

from __future__ import annotations

import html
import re
from bs4 import BeautifulSoup

ELEMENTS = {
    "h", "he", "li", "be", "b", "c", "n", "o", "f", "ne",
    "na", "mg", "al", "si", "p", "s", "cl", "ar", "k", "ca",
    "sc", "ti", "v", "cr", "mn", "fe", "co", "ni", "cu", "zn",
    "ga", "ge", "as", "se", "br", "kr", "rb", "sr", "y", "zr",
    "nb", "mo", "tc", "ru", "rh", "pd", "ag", "cd", "in", "sn",
    "sb", "te", "i", "xe", "cs", "ba", "la", "ce", "pr", "nd",
    "pm", "sm", "eu", "gd", "tb", "dy", "ho", "er", "tm", "yb",
    "lu", "hf", "ta", "w", "re", "os", "ir", "pt", "au", "hg",
    "tl", "pb", "bi", "po", "at", "rn", "fr", "ra", "ac", "th",
    "pa", "u", "np", "pu", "am", "cm", "bk", "cf", "es", "fm"
}

FENCE = re.compile(
    r"^(?P<indent>[ \t]*)```mol[ \t]*\n(?P<body>.*?)(?:\n(?P=indent)```)[ \t]*$",
    re.M | re.S,
)


def _split_body(source: str) -> tuple[dict[str, str], str, str]:
    meta: dict[str, str] = {}
    xyz_lines: list[str] = []
    inp_lines: list[str] = []
    section = "meta"
    for line in source.splitlines():
        s = line.strip()
        if s in ("--- xyz ---", "---xyz---", "### xyz"):
            section = "xyz"
            continue
        if s in ("--- input ---", "---input---", "--- qchem ---", "### input"):
            section = "input"
            continue
        if section == "meta" and re.match(r"^[A-Za-z_][\w-]*\s*:\s*\S", s):
            k, _, v = s.partition(":")
            meta[k.strip().lower()] = v.strip()
            continue
        if section == "meta":
            section = "xyz"
            xyz_lines.append(line)
            continue
        if section == "xyz":
            xyz_lines.append(line)
        else:
            inp_lines.append(line)
    return meta, "\n".join(xyz_lines).strip("\n"), "\n".join(inp_lines).strip("\n")


def render_mol_panel(xyz: str, inp: str, title: str = "", theme: str = "chem311", height: str = "360px", repr_style: str = "ball-stick", fmt: str = "xyz") -> str:
    # Normalize xyz: count atoms and ensure 2-line header
    if xyz:
        raw = [l.rstrip() for l in xyz.splitlines() if l.strip()]
        if raw and re.match(r"^\s*\d+\s*$", raw[0]):
            comment = raw[1] if len(raw) > 1 and not re.match(r"^\s*[A-Za-z]{1,3}\s+[-+]?\d", raw[1]) else "structure"
            coords = [l for l in raw if re.match(r"^\s*[A-Za-z]{1,3}\s+[-+]?\d", l)]
            if coords:
                xyz = f"{len(coords)}\n{comment or 'structure'}\n" + "\n".join(coords)
            else:
                xyz = ""

    if not xyz:
        if inp:
            return f'<pre class="highlight"><code class="language-qchem">{html.escape(inp)}</code></pre>'
        return ""

    attrs = [
        'class="mol-panel"',
        f'data-mol-theme="{html.escape(theme, True)}"',
        f'data-mol-height="{html.escape(height, True)}"',
        f'data-mol-repr="{html.escape(repr_style, True)}"',
    ]
    if title:
        attrs.append(f'data-mol-title="{html.escape(title, True)}"')

    xyz_out = html.escape(xyz)
    inp_out = html.escape(inp)
    return (
        f'<div {" ".join(attrs)}>\n'
        f'<pre class="mol-xyz" data-format="{html.escape(fmt, True)}">{xyz_out}</pre>\n'
        f'<pre class="mol-input">{inp_out}</pre>\n'
        f"</div>"
    )


def extract_xyz_from_qchem(code_text: str) -> str | None:
    """Extract Cartesian coordinates from a Q-Chem input block and format as XYZ."""
    m = re.search(r"\$molecule[^\n]*\n(.*?)\$end", code_text, re.IGNORECASE | re.DOTALL)
    if not m:
        return None

    mol_body = m.group(1)
    lines = mol_body.splitlines()

    atom_lines = []
    for line in lines:
        l = re.sub(r"[!#].*$", "", line).strip()
        if not l or l == "--":
            continue
        parts = l.split()
        # Charge and multiplicity: e.g. "0 1" or "-1 2"
        if len(parts) == 2 and re.match(r"^[-+]?\d+$", parts[0]) and re.match(r"^\d+$", parts[1]):
            continue
        atom_lines.append(parts)

    if not atom_lines:
        return None

    # Z-Matrix or keyword check: if first atom has fewer than 4 tokens (e.g. "O" or "read"), it is not Cartesian
    if len(atom_lines[0]) < 4:
        return None

    atoms = []
    for parts in atom_lines:
        if len(parts) >= 4:
            sym = parts[0].strip("@$")
            clean_sym = re.sub(r"\d+$", "", sym).lower()
            coords = None
            if len(parts) == 4:
                try:
                    coords = [float(p) for p in parts[1:4]]
                except ValueError:
                    coords = None
            elif len(parts) >= 5:
                # sym flag x y z
                if re.match(r"^[-+]?\d+$", parts[1]):
                    try:
                        coords = [float(p) for p in parts[2:5]]
                    except ValueError:
                        coords = None
                else:
                    try:
                        coords = [float(p) for p in parts[1:4]]
                    except ValueError:
                        coords = None

            if coords and (clean_sym in ELEMENTS or sym.isdigit()):
                elem_name = sym if sym.isdigit() else clean_sym.capitalize()
                atoms.append((elem_name, coords[0], coords[1], coords[2]))

    if len(atoms) >= 1:
        xyz_lines = [str(len(atoms)), "structure from Q-Chem input"]
        for elem, x, y, z in atoms:
            xyz_lines.append(f"{elem:<3} {x:14.6f} {y:14.6f} {z:14.6f}")
        return "\n".join(xyz_lines)

    return None


R1_SEP = re.compile(r"^([ \t]*)[-*]\s*•[ \t\u00a0]*\n+[ \t\u00a0]*(?=\S)", re.M)
R1_SAME = re.compile(r"^([ \t]*)[-*]\s*•[ \t\u00a0]+(?=\S)", re.M)
R2_SEP = re.compile(r"^([ \t]*)[-*]\s*\*\*[-–—]\*\*[ \t\u00a0]*\n+[ \t\u00a0]*(?=\S)", re.M)
R2_SAME = re.compile(r"^([ \t]*)[-*]\s*\*\*[-–—]\*\*[ \t\u00a0]+(?=\S)", re.M)
R3_SEP = re.compile(r"^([ \t]*)-\s*\*+[ \t\u00a0]*\n+[ \t\u00a0]*(?=\S)", re.M)
R3_SAME = re.compile(r"^([ \t]*)-\s*\*+[ \t\u00a0]+(?=\S)", re.M)
R4_SEP = re.compile(r"^([ \t]*)(\d+)\.\s*\2\.[ \t\u00a0]*\n+[ \t\u00a0]*(?=\S)", re.M)
R4_SAME = re.compile(r"^([ \t]*)(\d+)\.\s*\2\.[ \t\u00a0]+(?=\S)", re.M)
R5_STRAY = re.compile(r"\n\n[ \t]*\*\*[。.]?[ \t\u00a0]*\n\n")


def on_page_markdown(markdown: str, **kwargs) -> str:
    """Preprocess markdown: clean list artifacts and handle explicit ```mol fences."""
    if "•" in markdown or "**–**" in markdown or "**-**" in markdown:
        markdown = R1_SEP.sub(r"\1- ", markdown)
        markdown = R1_SAME.sub(r"\1- ", markdown)
        markdown = R2_SEP.sub(r"\1- ", markdown)
        markdown = R2_SAME.sub(r"\1- ", markdown)
        markdown = R3_SEP.sub(r"\1- ", markdown)
        markdown = R3_SAME.sub(r"\1- ", markdown)
    if "1. 1." in markdown or "2. 2." in markdown:
        markdown = R4_SEP.sub(r"\1\2. ", markdown)
        markdown = R4_SAME.sub(r"\1\2. ", markdown)

    if "```mol" in markdown:
        def _replace(match):
            meta, xyz, inp = _split_body(match.group("body"))
            return match.group("indent") + render_mol_panel(
                xyz,
                inp,
                title=meta.get("title", ""),
                theme=meta.get("theme", "chem311"),
                height=meta.get("height", "360px"),
                repr_style=meta.get("representation", "ball-stick"),
                fmt=meta.get("format", "xyz"),
            )
        markdown = FENCE.sub(_replace, markdown)

    return markdown


def on_page_content(html: str, **kwargs) -> str:
    """Transform code blocks containing $molecule ... $end into fast-mol panels."""
    if "$molecule" not in html:
        return html

    soup = BeautifulSoup(html, "html.parser")
    modified = False

    for pre in soup.find_all("pre"):
        code_tag = pre.find("code")
        code_text = code_tag.get_text() if code_tag else pre.get_text()

        if "$molecule" in code_text and "$end" in code_text:
            xyz = extract_xyz_from_qchem(code_text)
            if xyz:
                # Find target element to replace
                target = pre
                if pre.parent and "highlight" in pre.parent.get("class", []):
                    target = pre.parent

                panel_html = render_mol_panel(xyz, code_text.strip())
                new_elem = BeautifulSoup(panel_html, "html.parser").find("div", class_="mol-panel")
                if new_elem:
                    target.replace_with(new_elem)
                    modified = True

    if modified:
        return str(soup)
    return html
