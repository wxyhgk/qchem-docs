---
title: "7.10.8 自旋翻转 ADC 方法（Spin-Flip ADC Methods）"
---

## 7.10.8 自旋翻转 ADC 方法（Spin-Flip ADC Methods）

（2026 年 7 月 4 日）

自旋翻转（spin-flip, SF）方法[[726]](../bib_references/bib.md#bib757)

适用于少参考（few-reference）波函数的分子体系，例如双自由基（diradicals）、化学键断裂、单键绕转以及锥形交叉（conical intersections）。该方法以三重态（$m_{s}=1$）基态作为参考，引入自旋翻转激发算符 $\{\hat{C}_{J}\}=\{c_{a\beta}^{\dagger}c_{i\alpha};$
$\hskip 2.845276ptc_{a\beta}^{\dagger}c_{b\sigma}^{\dagger}c_{i\alpha}c_{j\sigma},$
$\hskip 7.113189pt\text{a \textless~{} b, i \textless~{} j}\}$，该算符翻转其中一个电子的自旋，从而得到单重态以及（$m_{s}=0$）三重态的激发目标态。自旋翻转方法已在 ADC(2)（严格型 strict 与扩展型 extended）以及 ADC(3)
方法中实现。[[796]](../bib_references/bib.md#bib830)
 需要注意的是，高自旋（$m_{s}=1$）三重态同样可以使用 SF-ADC 方法、以闭壳层单重态参考态进行计算。所需计算的自旋翻转态数目由 *$rem* 变量 SF_STATES 控制。
