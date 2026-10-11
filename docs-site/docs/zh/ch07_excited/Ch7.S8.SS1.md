---
title: "7.8.1 引言"
---

## 7.8.1 引言

（2026 年 7 月 4 日）

CIS(D) 是对 CIS 的一种简单且尺寸一致（size-consistent）的双激发（doubles）校正，对于每个激发态，其计算代价随基组规模呈五次方增长。[[544]](../bib_references/bib.md#bib554)
从这个意义上说，CIS(D) 可以视为基态 MP2 方法在激发态上的类比。相对于 CIS，CIS(D) 能够显著提升激发能的精度，并且借助 **Q-Chem** 高效的积分变换程序包，该方法还可应用于相对较大的分子。此外，与 MP2 方法的情况类似，通过使用辅助基组展开（第 [6.6](../ch06_correlation/topic_rimp2.md) 节），其计算效率可以得到大幅提升。[[1162]](../bib_references/bib.md#bib1215)
