---
title: "4.7.2 双基组 MP2"
---

## 4.7.2 双基组 MP2

（2026 年 7 月 4 日）

双基组近似（dual-basis approximation）也可用于关联微扰二阶（second-order Møller-Plesset, MP2）计算的参考能[[1300]](../bib_references/bib.md#bib1355)。
 启用该近似后，首先按照上文所述计算双基组 HF 能量；随后利用分子轨道（MO）系数和轨道能量，在大基组下计算关联能。该技术对于 RI-MP2 计算尤为有效（见第 [6.6](../ch06_correlation/topic_rimp2.md) 节），在这类计算中，底层自洽场（SCF）计算的开销往往占主导地位。

此外，DB-RI-MP2 的解析梯度（analytic gradients）计算也很高效。
