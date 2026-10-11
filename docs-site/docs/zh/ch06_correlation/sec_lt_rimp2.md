---
title: "6.6.11 采用拉普拉斯变换的 RI-MP2 方法"
---

## 6.6.11 采用拉普拉斯变换的 RI-MP2 方法

（2026 年 7 月 4 日）

Joonho Lee 与 Martin Head-Gordon 合作，在 libgmbpt 基础上实现了一种采用拉普拉斯变换的 RI-MP2（分辨恒等式二阶 Møller-Plesset 微扰理论，RI-MP2）方法，可同时处理同自旋（same-spin）与异自旋（opposite-spin）关联能[[784]](../bib_references/bib.md#bib829)。若要使用此功能，只需在 *$rem* 块中添加 LAPLACE_TRANSFORM TRUE 即可。
