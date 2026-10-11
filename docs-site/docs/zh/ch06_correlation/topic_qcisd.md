---
title: "6.12.7 二次组态相互作用（QCISD）"
---

## 6.12.7 二次组态相互作用（QCISD）

（2026 年 7 月 4 日）

包含单、双激发的二次组态相互作用（quadratic configuration interaction with singles and doubles，QCISD）
是耦合簇方法 CCSD[[1113]](../bib_references/bib.md#bib1162) 的一种被广泛使用的替代方案，
它继承了 CCSD 的主要优良性质，即具有尺寸一致性（size-consistent）、对电子对（electron pairs）精确，
同时同样属于非变分（non-variational）方法。其计算代价随分子尺寸和基组（Basis Set）的变化规律
与 CCSD 相同，只是常数因子略小。尽管 QCISD 最初是独立于 CCSD 提出的，其出发点是修正组态
相互作用（Configuration Interaction，CI）方程使其具备尺寸一致性，但 QCISD 最好被理解为 CCSD
的一种近似。其定义方程如下所示（假设在此前提下给出）：
