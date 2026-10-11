---
title: "6.11.1 引言"
---

## 6.11.1 引言

（2026 年 7 月 4 日）

Joonho Lee 与 Martin Head-Gordon 合作开发并加入了一种仅需立方存储需求（cubic-storage requirement）的 RI-MP3 实现。[[784]](../bib_references/bib.md#bib829)

得益于改进的存储标度，所得程序可应用于比 CCMAN2（[6.12](topic_ccsd.md)）所能处理的更大的体系。
若要使用该方法，可设置 METHOD = RIMP3 并配合 AUXBASIS。
本质上，它将式 ([8.4](../ch08_basis/Ch8.S8.SS1.md#eq:riapprox)) 中的 RI 近似应用于 MP3 关联能的计算。
感兴趣的读者请参阅第 [6.3](topic_ccsd.md) 节。
