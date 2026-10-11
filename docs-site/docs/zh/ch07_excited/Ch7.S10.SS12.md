---
title: "7.10.12 冻结密度嵌入：FDE-ADC 方法"
---

## 7.10.12 冻结密度嵌入：FDE-ADC 方法

（2026 年 7 月 4 日）

FDE-ADC[[1121]](../bib_references/bib.md#bib1168)
 是一种基于冻结密度嵌入理论（Frozen Density Embedding Theory, FDET）[[1453]](../bib_references/bib.md#bib1515)，
将嵌入物种与其环境之间的相互作用纳入 ADC($n$) 计算的方法。

FDE-ADC 支持 2s、2x 和 3 阶的 ADC 及 CVS-ADC 方法，常规的 ADC
作业控制关键字同样适用。

FDE-ADC 方法首先生成嵌入势（embedding potential），其中嵌入体系 (A)
采用 MP($n$) 密度。对于常规 ADC，本征值问题中通过以下方式定义修正后的轨道能量
