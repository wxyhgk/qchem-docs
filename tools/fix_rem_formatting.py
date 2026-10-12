#!/usr/bin/env python3
"""
Batch fixer for Q-Chem $rem parameter documentation formatting:
1. Removes stray duplicate variable keyword lines immediately before `### VAR` headers.
2. Unifies fragmented Options bullet lists into clean key-value pairs (e.g. `0`: description).
3. Preserves inline formulas ($...$), code, and handles both Chinese and English documents.
"""

import os
import re
import glob
from bs4 import BeautifulSoup

def build_rem_map():
    rem_map = {}
    for fpath in glob.glob("crawl/html/*.html"):
        slug = os.path.splitext(os.path.basename(fpath))[0]
        with open(fpath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")
        for rem in soup.find_all("div", class_="remblock"):
            p = rem.find("p")
            if not p or "OPTIONS:" not in p.get_text():
                continue
            bold = p.find("span", class_="ltx_font_bold")
            if not bold:
                continue
            vname = bold.get_text(strip=True)
            tabs = rem.find_all("span", class_="ltx_tabular")
            opt_list = []
            for tab in tabs:
                rows = tab.find_all("span", class_="ltx_tr")
                if len(rows) >= 1:
                    temp = []
                    is_opt = False
                    for r in rows:
                        tds = r.find_all("span", class_=lambda c: c and "ltx_td" in c)
                        if len(tds) >= 2:
                            is_opt = True
                            k = tds[0].get_text(" ", strip=True)
                            d = tds[1].get_text(" ", strip=True)
                            temp.append((k, d))
                        elif len(tds) == 1:
                            k = tds[0].get_text(" ", strip=True)
                            temp.append((k, ""))
                    if is_opt and len(temp) > len(opt_list):
                        opt_list = temp
            if opt_list:
                rem_map[(slug, vname)] = [o[0] for o in opt_list]
                rem_map[vname] = [o[0] for o in opt_list]
    return rem_map

def is_cjk(ch):
    return "\u4e00" <= ch <= "\u9fff"

def smart_join(tokens, lang="zh"):
    if lang == "en":
        return " ".join(t.strip() for t in tokens if t.strip())
    res = ""
    for token in tokens:
        token = token.strip()
        if not token:
            continue
        if not res:
            res = token
            continue
        last_char = res[-1]
        first_char = token[0]
        if first_char in "，。！？；：）】》、":
            res += token
        elif last_char in "（【《":
            res += token
        elif is_cjk(last_char) and is_cjk(first_char):
            res += token
        elif is_cjk(last_char) and (first_char.isalnum() or first_char in "$`"):
            res += " " + token
        elif (last_char.isalnum() or last_char in "$`") and is_cjk(first_char):
            res += " " + token
        else:
            res += " " + token
    res = re.sub(r"\s+([，。！？；：）】》])", r"\1", res)
    res = re.sub(r"([（【《])\s+", r"\1", res)
    return res.strip()

def format_opt_key(k):
    k = k.strip()
    if k.startswith("`") or k.startswith("$"):
        return k
    if re.match(r"^[A-Za-z0-9_\-\.\+]+$", k):
        return f"`{k}`"
    m = re.match(r"^(TRUE|FALSE)\s*[（\(](?:或|or)?\s*([0-9]+)[）\)]$", k)
    if m:
        return f"`{m.group(1)}`（或 `{m.group(2)}`）"
    if len(k) < 30 and not any(is_cjk(c) for c in k):
        return f"`{k}`"
    return k

def is_key(item, exp_keys=None):
    clean_item = item.strip()
    if exp_keys:
        if clean_item in exp_keys:
            return True
        for ek in exp_keys:
            if clean_item.startswith(ek) and (len(clean_item) == len(ek) or clean_item[len(ek):].startswith(" ")):
                return True
    if re.match(r"^[0-9]+$", clean_item):
        return True
    if clean_item in ["TRUE", "FALSE", "true", "false", "None", "Symbol", "$n$", "$m$", "n", "m", "STRING", "INTEGER", "User-defined"]:
        return True
    if re.match(r"^(TRUE|FALSE)\s*[（\(](?:或|or)?\s*[0-9]+[）\)]$", clean_item):
        return True
    return False

def group_options(bullets, exp_keys=None, lang="zh"):
    # If all bullets already contain ':' or '：', they might already be formatted
    already_formatted = sum(1 for b in bullets if re.match(r"^[`\$]?[A-Za-z0-9_\-\.\+]+[`\$]?\s*[:：]", b))
    if already_formatted >= len(bullets) * 0.7:
        return [f">     * {b}" for b in bullets]

    groups = []
    current_key = None
    current_desc = []

    for b in bullets:
        if is_key(b, exp_keys):
            if current_key is not None:
                groups.append((current_key, current_desc))
            current_key = b
            current_desc = []
        else:
            if current_key is None:
                current_key = b
            else:
                current_desc.append(b)
    if current_key is not None:
        groups.append((current_key, current_desc))

    res = []
    for k, desc_tokens in groups:
        k_fmt = format_opt_key(k)
        desc = smart_join(desc_tokens, lang=lang)
        if desc:
            res.append(f">     * {k_fmt}: {desc}")
        else:
            res.append(f">     * {k_fmt}")
    return res

def process_file(fpath, rem_map, dry_run=False):
    lang = "zh" if "/zh/" in fpath else "en"
    slug = os.path.splitext(os.path.basename(fpath))[0]
    raw_slug = slug.replace("sec_O_N", "sec_O(N)")

    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    lines = content.split("\n")
    new_lines = []
    i = 0
    modified = False
    opt_headers = ["Options", "取值", "取值选项", "可选值", "可选取值", "可选项", "选项", "选项（Options）"]

    current_var = None

    while i < len(lines):
        line = lines[i]

        # 1. Check for stray duplicate keyword line before `### VAR`
        m_var_heading = re.match(r"^### `([A-Za-z0-9_\-]+)`", line.strip())
        if m_var_heading:
            current_var = m_var_heading.group(1)
            # Check if previous non-blank line in new_lines is exactly current_var
            j = len(new_lines) - 1
            while j >= 0 and new_lines[j].strip() == "":
                j -= 1
            if j >= 0 and new_lines[j].strip() == current_var:
                # Remove the stray keyword line
                new_lines.pop(j)
                # Also remove any empty line right after it if needed
                while j < len(new_lines) and new_lines[j].strip() == "":
                    new_lines.pop(j)
                modified = True

            new_lines.append(line)
            i += 1
            continue

        # 2. Check for Options header inside blockquote
        m_opt = re.match(r"^>\s*\*\s*\*\*([^\*:]+)\*\*:\s*$", line)
        if m_opt and any(m_opt.group(1).strip() == h for h in opt_headers):
            hdr = m_opt.group(1).strip()
            new_lines.append(line)
            i += 1
            # Collect bullet lines
            bullets = []
            while i < len(lines):
                l = lines[i]
                if l.strip().startswith("> * **") or (not l.strip().startswith(">") and l.strip() != ""):
                    break
                if l.strip().startswith(">"):
                    b = re.sub(r"^>\s*\*\s*", "", l).strip()
                    if b:
                        bullets.append(b)
                i += 1

            if bullets:
                exp_keys = rem_map.get((raw_slug, current_var)) or rem_map.get((slug, current_var)) or rem_map.get(current_var)
                grouped = group_options(bullets, exp_keys=exp_keys, lang=lang)
                new_lines.extend(grouped)
                modified = True
            continue

        new_lines.append(line)
        i += 1

    new_content = "\n".join(new_lines)
    if modified and new_content != content:
        if not dry_run:
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
        return True

    return False

def main():
    import sys
    dry_run = "--dry-run" in sys.argv
    rem_map = build_rem_map()
    print(f"Loaded {len(rem_map)} REM variable maps from crawl/html.")

    docs = glob.glob("docs-site/docs/**/*.md", recursive=True)
    count_mod = 0
    for d in sorted(docs):
        if process_file(d, rem_map, dry_run=dry_run):
            count_mod += 1

    print(f"{'Would modify' if dry_run else 'Modified'} {count_mod} / {len(docs)} markdown files.")

if __name__ == "__main__":
    main()
