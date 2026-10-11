#!/usr/bin/env python3
"""
Translation pipeline for Q-Chem 7.0 documentation.
Translates Markdown files from docs-site/docs/en/ to docs-site/docs/zh/
Uses pi CLI with opencode-go provider.
"""

import os
import sys
import re
import glob
import subprocess
import argparse
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

ROOT_DIR = Path(__file__).resolve().parent.parent
EN_DIR = ROOT_DIR / "docs-site" / "docs" / "en"
ZH_DIR = ROOT_DIR / "docs-site" / "docs" / "zh"

DEFAULT_MODEL = "qwen3.8-flash"
DEFAULT_PROVIDER = "opencode-go"

TRANSLATE_PROMPT_TEMPLATE = """你是一位精通计算化学与量子化学的专业翻译专家。
请将以下来自 Q-Chem 7.0 官方手册的 Markdown 文档翻译为流畅、规范的简体中文。

翻译要求：
1. 保持严格的 Markdown 语法结构，不要破坏标题级别、列表缩进、表格、Frontmatter 元数据。
2. 专有名词采用中文（英文缩写或原文）形式，例如：密度泛函理论（Density Functional Theory, DFT）、自洽场（SCF）、基组（Basis Set）等。
3. 数学公式（无论是行内 $...$ 还是块级 $$...$$）一律原样保留，严禁修改任何 LaTeX 表达式或公式编号 \\tag{{...}}。
4. 代码块（```qchem ... ``` 或其他代码块）内部的代码、关键字（如 $rem, $molecule, METHOD, BASIS, $end）一律原样保留，不要翻译代码内部内容。
5. 保持所有链接格式不变，包括相对路径 [链接文本](路径#锚点)，仅翻译中括号内的描述文本，不要改变圆括号内的 URL 或路径。
6. 对于 Callout 块（如 ???+ example "Example 4.2: Description"），将标题描述翻译为中文，例如 ???+ example "示例 4.2: 水分子的单点能计算"。
7. 直接输出翻译后的完整 Markdown 内容，不要添加任何额外的问候语、代码围栏包裹说明或对话文本。

待翻译文档：
{content}
"""

def is_already_translated(zh_path):
    """Check if the Chinese file contains significant Chinese characters."""
    if not zh_path.exists():
        return False
    try:
        with open(zh_path, "r", encoding="utf-8") as f:
            text = f.read()
        # Count Chinese characters
        chinese_chars = re.findall(r'[\u4e00-\u9fff]', text)
        return len(chinese_chars) > 20
    except Exception:
        return False

def translate_content_with_pi(content, model=DEFAULT_MODEL, provider=DEFAULT_PROVIDER):
    prompt = TRANSLATE_PROMPT_TEMPLATE.format(content=content)
    cmd = [
        "pi", "-p",
        "--provider", provider,
        "--model", model,
        "--no-session",
        prompt
    ]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=120)
        if result.returncode == 0:
            out = result.stdout.strip()
            # Clean possible markdown wrapping if the model wrapped everything in ```markdown ... ```
            if out.startswith("```markdown") and out.endswith("```"):
                out = out[len("```markdown"): -3].strip()
            elif out.startswith("```md") and out.endswith("```"):
                out = out[len("```md"): -3].strip()
            return True, out
        else:
            return False, f"CLI error: {result.stderr.strip()}"
    except Exception as e:
        return False, str(e)

def translate_file(rel_path, model=DEFAULT_MODEL, provider=DEFAULT_PROVIDER, force=False):
    en_file = EN_DIR / rel_path
    zh_file = ZH_DIR / rel_path

    if not en_file.exists():
        return False, f"File not found: {en_file}"

    if not force and is_already_translated(zh_file):
        return True, "already translated (skipped)"

    with open(en_file, "r", encoding="utf-8") as f:
        en_content = f.read()

    # For home page, provide customized translation
    if rel_path == "index.md":
        zh_content = translate_home_page(en_content)
        zh_file.parent.mkdir(parents=True, exist_ok=True)
        with open(zh_file, "w", encoding="utf-8") as f:
            f.write(zh_content)
        return True, "translated (home)"

    success, res = translate_content_with_pi(en_content, model=model, provider=provider)
    if success:
        zh_file.parent.mkdir(parents=True, exist_ok=True)
        with open(zh_file, "w", encoding="utf-8") as f:
            f.write(res + "\n")
        return True, "translated successfully"
    else:
        return False, res

def translate_home_page(en_content):
    lines = [
        "---",
        "title: Q-Chem 7.0 用户手册",
        "hide:",
        "  - navigation",
        "---",
        "",
        "# Q-Chem 7.0 用户手册",
        "",
        '<div style="text-align:center; margin: 1.5rem 0 2.5rem 0;">',
        '  <img src="assets/logo.svg" alt="Q-Chem Logo" style="max-height: 90px; margin-bottom: 1rem;">',
        '  <p style="font-size: 1.15rem; color: var(--md-default-fg-color--light);">',
        '    Q-Chem 7.0 量子化学计算软件包官方用户手册、理论背景与执行指南（中英双语版）。',
        '  </p>',
        '  <div style="margin-top: 1rem;">',
        '    <a class="md-button md-button--primary" href="ch01_intro/chap_intro.md" style="margin-right: 0.5rem;">📖 快速入门</a>',
        '    <a class="md-button" href="assets/qchem_manual.pdf" target="_blank" download>⬇️ 下载官方 PDF 手册 (5.5 MB)</a>',
        '  </div>',
        '</div>',
        "",
        "## 章节概览",
        "",
        '<div class="grid cards" markdown>',
        "",
        "-   :material-book-open-page-variant: **[第 1 章：简介与概览](ch01_intro/chap_intro.md)**",
        "    ---",
        "    Q-Chem 功能概览、Q-Chem 7.0 最新特性及文献引用规范。",
        "",
        "-   :material-cog-box: **[第 2 章：安装、配置与执行](ch02_install/chap_install.md)**",
        "    ---",
        "    环境部署、环境变量 ($QCAUX)、授权配置、IQmol 可视化集成与作业提交。",
        "",
        "-   :material-file-code-outline: **[第 3 章：Q-Chem 输入文件结构](ch03_inputs/chap_inputs.md)**",
        "    ---",
        "    输入文件通用格式、分子坐标定义 (`$molecule`)、作业控制 (`$rem`) 与批处理执行。",
        "",
        "-   :material-atom-variant: **[第 4 章：自洽场（SCF）基态方法](ch04_scf/chap_scf.md)**",
        "    ---",
        "    哈特里-福克（HF）、DIIS、收敛加速算法、线性标度 O(N) 算法与扩展紧束缚（xTB）。",
        "",
        "-   :material-chart-bell-curve: **[第 5 章：密度泛函理论（DFT）](ch05_dft/chap_DFT.md)**",
        "    ---",
        "    LDA、GGA、杂化泛函、长程校正（RSH）、双杂化泛函与经验色散校正（DFT-D / vdW）。",
        "",
        "-   :material-wave: **[第 6 章：波函数电子相关方法](ch06_correlation/chap_correlation.md)**",
        "    ---",
        "    MP2、RI-MP2、局域相关、耦合簇（CCSD, CCSD(T)）与活性空间方法。",
        "",
        "-   :material-lightning-bolt: **[第 7 章：开壳层与激发态方法](ch07_excited/chap_excited.md)**",
        "    ---",
        "    CIS、TD-DFT、EOM-CC、ADC 家族方法与芯能级激发光谱计算。",
        "",
        "-   :material-blur-radial: **[第 8 章：基组与有效核心势（ECP）](ch08_basis/chap_basis.md)**",
        "    ---",
        "    标准高斯基组库、有效核心势（ECP）以及用户自定义混合基组定义。",
        "",
        "-   :material-map-marker-path: **[第 9 章：势能面搜索与动力学](ch09_opt/chap_opt.md)**",
        "    ---",
        "    几何构型优化、过渡态搜索（Freezing String, NEB）与从头算分子动力学（AIMD）。",
        "",
        "-   :material-flask: **[第 10 章：分子性质与波函数分析](ch10_properties/chap_properties.md)**",
        "    ---",
        "    多极矩、NBO 自然键轨道、NMR 屏蔽常数、极化率、振动光谱与能量分解分析（EDA）。",
        "",
        "-   :material-water-outline: **[第 11 章：复杂环境与溶剂化模型](ch11_env/chap_env.md)**",
        "    ---",
        "    连续介质溶剂模型（PCM, SMD, COSMO）、QM/MM 接口与密度嵌入方法。",
        "",
        "-   :material-puzzle: **[第 12 章：基于片段的计算方法](ch12_frag/chap_frag.md)**",
        "    ---",
        "    ALMO-EDA 能量分解、绝对定域分子轨道与大分子体系片段计算。",
        "",
        "-   :material-creation: **[第 13 章：专门专题与高级特性](ch13_specialized/chap_specialized_topics.md)**",
        "    ---",
        "    非绝热动力学、电子传输以及量子计算接口特性。",
        "",
        "-   :material-format-list-bulleted: **[附录 B：$rem 参数速查手册](app_b_quickref/app_quick_ref.md)**",
        "    ---",
        "    所有 Q-Chem `$rem` 控制变量的完整字母索引、默认值及合法选项速查表。",
        "",
        "</div>",
        ""
    ]
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Translate Q-Chem documentation to Chinese")
    parser.add_argument("--chapter", help="Translate specific chapter (e.g. ch01_intro)")
    parser.add_argument("--file", help="Translate specific file (e.g. ch01_intro/chap_intro.md)")
    parser.add_argument("--home", action="store_true", help="Translate home page")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="Model to use (default: qwen3.8-flash)")
    parser.add_argument("--provider", default=DEFAULT_PROVIDER, help="Provider (default: opencode-go)")
    parser.add_argument("--workers", type=int, default=4, help="Concurrency workers")
    parser.add_argument("--force", action="store_true", help="Force re-translation")
    parser.add_argument("--emit", action="store_true", help="Emit shell commands for manual execution")
    args = parser.parse_args()

    files = []
    if args.home:
        files = ["index.md"]
    elif args.file:
        files = [args.file]
    elif args.chapter:
        chap_dir = EN_DIR / args.chapter
        for p in chap_dir.glob("*.md"):
            files.append(f"{args.chapter}/{p.name}")
    else:
        # All files
        files.append("index.md")
        for p in sorted(EN_DIR.rglob("*.md")):
            rel = str(p.relative_to(EN_DIR))
            if rel != "index.md":
                files.append(rel)

    print(f"[*] Target files to translate: {len(files)}")

    if args.emit:
        for f in files:
            print(f'python3 tools/translate.py --file "{f}" --model {args.model}')
        return

    # Direct parallel translation
    success_count = 0
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(translate_file, f, model=args.model, provider=args.provider, force=args.force): f
            for f in files
        }
        for future in as_completed(futures):
            f = futures[future]
            try:
                ok, msg = future.result()
                if ok:
                    success_count += 1
                    print(f"[+] {f}: {msg}")
                else:
                    print(f"[!] {f} FAILED: {msg}")
            except Exception as e:
                print(f"[!] {f} EXCEPTION: {e}")

    print(f"[✓] Finished translation: {success_count}/{len(files)} files processed.")

if __name__ == "__main__":
    main()
