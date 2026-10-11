# Q-Chem 7.0 文档工程 (Q-Chem Documentation Site)

基于官方最新 [Q-Chem 7.0 User's Manual](https://manual.q-chem.com/latest/index.html)（2026年7月版）抓取解析并制作的中英双语 Markdown 知识库与 MkDocs Material 现代化文档站点。

---

## 🌟 项目亮点

1. **LaTeXML 无损公式解析**：直接从官方 LaTeXML 源中提取原始 LaTeX 表达式（`alttext`），100% 保持数学公式精度与编号（`\tag{...}`），杜绝 OCR 误识别。
2. **结构化参数卡片**：`$rem` 参数与 `$molecule` 等控制段被转换为清晰的 Markdown 结构卡片与类型/默认值/选项说明。
3. **输入用例原生高亮**：Q-Chem 计算用例转换为优雅的可折叠 Callout（`???+ example`）及 `qchem` 代码块。
4. **完整目录与交叉链接无损映射**：13 个主体章节、3 个附录与参考文献（共 759 个页面）全部建立拓扑索引与相对链接映射，跨页面链接均可精准定位。
5. **中英双语架构**：采用 `mkdocs-static-i18n` 规范布局（`docs/en` 与 `docs/zh`），支持一键切换语言。

---

## 📁 目录结构

```text
QChem/
├── crawl/                  # 官方站点原始镜像缓存 (不入库，可重跑)
│   ├── html/               # 759 个原始 HTML 页面
│   └── assets/             # 官方图片、矢量 Logo、Figures 及离线 PDF 手册 (5.5 MB)
├── tools/                  # 自动化流水线工具
│   ├── crawler.py          # 多线程断点续传爬虫
│   ├── latexml_to_md.py    # LaTeXML HTML → Markdown 解析器 (公式/参数/用例)
│   └── build_site.py       # 拓扑导航生成与全站转换器
├── docs-site/              # MkDocs Material 文档工程
│   ├── mkdocs.yml          # 站点配置 (主题、插件、MathJax、多语言)
│   └── docs/
│       ├── en/             # 英文全量文档 (759 篇)
│       ├── zh/             # 中文全量文档 (已对齐目录与基底)
│       └── assets/         # 共享静态资源 (图片、Logo、MathJax 脚本)
├── .gitignore
└── README.md
```

---

## 🚀 本地预览

进入文档工程目录并启动本地服务：

```bash
cd docs-site

# 启动本地实时预览服务器
mkdocs serve
```

打开浏览器访问：
* **英文主页**：[http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **中文主页**：[http://127.0.0.1:8000/zh/](http://127.0.0.1:8000/zh/)

---

## 📦 重新抓取与全站构建

如果需要重新同步官方手册或重新生成 Markdown：

```bash
# 1. 爬取最新页面与静态资产
python3 tools/crawler.py 10

# 2. 解析 HTML 并生成双语 Markdown 树与 mkdocs.yml
python3 tools/build_site.py

# 3. 编译静态 HTML 站点
cd docs-site && mkdocs build
```
编译产物位于 `docs-site/site/`。
