---
title: "6.11.1 引言"
---

## 6.11.1 引言

（2026 年 7 月 4 日）

Joonho Lee 与 Martin Head-Gordon 合作开发并添加了一种仅需三次方存储量（cubic-storage）的 RI-MP3 实现。[[784]](../bib_references/bib.md#bib829)

得益于改进的存储标度，所生成的代码可应用于比 CCMAN2（[6.12](topic_ccsd.md)）中处理的更大体系。若要使用该方法，可以设置 METHOD = RIMP3 以及 AUXBASIS。本质上，它是将公式 ([8.4](../ch08_basis/Ch8.S8.SS1.md#eq:riapprox)) 中的 RI 近似应用于 MP3 相关能的计算。感兴趣的读者可参阅第 [6.3](topic_mp2.md) 节以获取关于 Møller-Plesset 微扰理论的更多详细信息。

除 RI-MP3 外，还可以像 Bertels 等人[[115]](../bib_references/bib.md#bib102) 以及 Rettig 等人[[1159]](../bib_references/bib.md#bib1212) 最近的工作那样，结合缩放的 RI-MP2 和 RI-MP3 相关能贡献以及替代的参考分子轨道（DFT 和 OOMP2）。

使用非 HF 轨道参考需要复合作业：第一个计算生成轨道参考，第二个计算首先在固定的轨道参考上使用 HF 重新计算 SCF 能量和 Fock 矩阵，然后继续进行相关计算。
