#!/usr/bin/env python3
"""
Fix MathJax display formula rendering across all documentation files.
Ensures display math blocks ($$...$$) have blank lines before the opening $$
and after the closing $$, allowing pymdownx.arithmatex's BlockProcessor to parse
them cleanly into <div class="arithmatex">\[...\]</div> without colliding with
HTML anchors (<a id="..."></a>) or adjacent text.
"""

import os
import sys

def fix_math_in_file(fpath):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    if "$$" not in content:
        return False, 0

    lines = content.split("\n")
    new_lines = []
    in_math = False
    in_code = False
    fixed_count = 0

    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            new_lines.append(line)
            continue
        if in_code:
            new_lines.append(line)
            continue

        if s == "$$":
            if not in_math:
                # Opening $$
                in_math = True
                if new_lines and new_lines[-1].strip() != "":
                    new_lines.append("")
                    fixed_count += 1
                new_lines.append(line)
            else:
                # Closing $$
                in_math = False
                new_lines.append(line)
                if i + 1 < len(lines) and lines[i + 1].strip() != "":
                    new_lines.append("")
                    fixed_count += 1
        else:
            new_lines.append(line)

    new_content = "\n".join(new_lines)
    if new_content != content:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True, fixed_count

    return False, 0

def main():
    docs_dir = os.path.join(os.path.dirname(__file__), "..", "docs-site", "docs")
    total_files = 0
    modified_files = 0
    total_fixes = 0

    for root, _, files in os.walk(docs_dir):
        for f in sorted(files):
            if f.endswith(".md"):
                total_files += 1
                fpath = os.path.join(root, f)
                mod, cnt = fix_math_in_file(fpath)
                if mod:
                    modified_files += 1
                    total_fixes += cnt

    print(f"Scanned {total_files} markdown files.")
    print(f"Modified {modified_files} files with {total_fixes} math block spacing adjustments.")

if __name__ == "__main__":
    main()
