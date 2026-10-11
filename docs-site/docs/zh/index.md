---
title: Q-Chem 7.0 用户手册
hide:
  - navigation
---

# Q-Chem 7.0 用户手册

<div style="text-align:center; margin: 1.5rem 0 2.5rem 0;">
  <img src="assets/logo.svg" alt="Q-Chem Logo" style="max-height: 90px; margin-bottom: 1rem;">
  <p style="font-size: 1.15rem; color: var(--md-default-fg-color--light);">
    Q-Chem 7.0 量子化学计算软件包官方用户手册、理论背景与执行指南（中英双语版）。
  </p>
  <div style="margin-top: 1rem;">
    <a class="md-button md-button--primary" href="ch01_intro/chap_intro.md" style="margin-right: 0.5rem;">📖 快速入门</a>
    <a class="md-button" href="assets/qchem_manual.pdf" target="_blank" download>⬇️ 下载官方 PDF 手册 (5.5 MB)</a>
  </div>
</div>

## 章节概览

<div class="grid cards" markdown>

-   :material-book-open-page-variant: **[第 1 章：简介与概览](ch01_intro/chap_intro.md)**
    ---
    Q-Chem 功能概览、Q-Chem 7.0 最新特性及文献引用规范。

-   :material-cog-box: **[第 2 章：安装、配置与执行](ch02_install/chap_install.md)**
    ---
    环境部署、环境变量 ($QCAUX)、授权配置、IQmol 可视化集成与作业提交。

-   :material-file-code-outline: **[第 3 章：Q-Chem 输入文件结构](ch03_inputs/chap_inputs.md)**
    ---
    输入文件通用格式、分子坐标定义 (`$molecule`)、作业控制 (`$rem`) 与批处理执行。

-   :material-atom-variant: **[第 4 章：自洽场（SCF）基态方法](ch04_scf/chap_scf.md)**
    ---
    哈特里-福克（HF）、DIIS、收敛加速算法、线性标度 O(N) 算法与扩展紧束缚（xTB）。

-   :material-chart-bell-curve: **[第 5 章：密度泛函理论（DFT）](ch05_dft/chap_DFT.md)**
    ---
    LDA、GGA、杂化泛函、长程校正（RSH）、双杂化泛函与经验色散校正（DFT-D / vdW）。

-   :material-wave: **[第 6 章：波函数电子相关方法](ch06_correlation/chap_correlation.md)**
    ---
    MP2、RI-MP2、局域相关、耦合簇（CCSD, CCSD(T)）与活性空间方法。

-   :material-lightning-bolt: **[第 7 章：开壳层与激发态方法](ch07_excited/chap_excited.md)**
    ---
    CIS、TD-DFT、EOM-CC、ADC 家族方法与芯能级激发光谱计算。

-   :material-blur-radial: **[第 8 章：基组与有效核心势（ECP）](ch08_basis/chap_basis.md)**
    ---
    标准高斯基组库、有效核心势（ECP）以及用户自定义混合基组定义。

-   :material-map-marker-path: **[第 9 章：势能面搜索与动力学](ch09_opt/chap_opt.md)**
    ---
    几何构型优化、过渡态搜索（Freezing String, NEB）与从头算分子动力学（AIMD）。

-   :material-flask: **[第 10 章：分子性质与波函数分析](ch10_properties/chap_properties.md)**
    ---
    多极矩、NBO 自然键轨道、NMR 屏蔽常数、极化率、振动光谱与能量分解分析（EDA）。

-   :material-water-outline: **[第 11 章：复杂环境与溶剂化模型](ch11_env/chap_env.md)**
    ---
    连续介质溶剂模型（PCM, SMD, COSMO）、QM/MM 接口与密度嵌入方法。

-   :material-puzzle: **[第 12 章：基于片段的计算方法](ch12_frag/chap_frag.md)**
    ---
    ALMO-EDA 能量分解、绝对定域分子轨道与大分子体系片段计算。

-   :material-creation: **[第 13 章：专门专题与高级特性](ch13_specialized/chap_specialized_topics.md)**
    ---
    非绝热动力学、电子传输以及量子计算接口特性。

-   :material-format-list-bulleted: **[附录 B：$rem 参数速查手册](app_b_quickref/app_quick_ref.md)**
    ---
    所有 Q-Chem `$rem` 控制变量的完整字母索引、默认值及合法选项速查表。

-   :material-calculator: **[附录 A：AOInts 积分引擎](app_a_aoints/app_AOINTS.md)**
    ---
    Q-Chem 高性能原子轨道双电子与多中心积分计算架构与实现。

-   :material-license: **[附录 C：第三方组件与许可](app_c_thirdparty/app_thirdparty.md)**
    ---
    Armadillo、Libtensor、Libefp、Libecpint 等开源组件的版权与开源协议。

-   :material-bookshelf: **[参考文献与延伸阅读](bib_references/bib.md)**
    ---
    全书 1,580 余篇量子化学经典理论文献与 Q-Chem 算法引用检索表。

</div>

