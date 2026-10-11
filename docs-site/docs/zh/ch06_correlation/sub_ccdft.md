---
title: "6.15.2 相关计算中的非 Hartree-Fock 轨道"
---

## 6.15.2 相关计算中的非 Hartree-Fock 轨道

（2026 年 7 月 4 日）

对于存在问题的开壳层参考情形，*例如* 自旋污染严重的双重态自由基，可以选择使用 DFT 轨道，这往往能显著改善计算结果。[[111]](../bib_references/bib.md#bib97)
 实现方式是先进行一次 DFT 计算，然后读取其轨道并关闭 SCF 过程。注意，必须将 GEN_SCFMAN 设为 false，
这样才能对轨道进行正确的伪正则化（pseudocanonicalization）。

???+ example "示例 6.49: 使用 B3LYP 轨道对三重态卡宾进行 CCSD 计算"
    CCSD calculation of triplet methylene using B3LYP orbitals
