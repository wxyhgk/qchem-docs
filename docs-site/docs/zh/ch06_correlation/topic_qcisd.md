---
title: "6.12.7 二次组态相互作用（QCISD）"
---

## 6.12.7 二次组态相互作用（QCISD）

（2026 年 7 月 4 日）

包含单激发和双激发的二次组态相互作用（Quadratic Configuration Interaction with Singles and Doubles, QCISD）是 CCSD 的一种广泛使用的替代方法，[[1113]](../bib_references/bib.md#bib1162) 它具备 CCSD 的主要优良性质：具有尺寸一致性、对双电子体系是精确的，同时也是非变分的。它的计算量随分子大小和基组的标度关系与 CCSD 相同，尽管比例常数略小。虽然最初它是独立于 CCSD 提出的（基于修正组态相互作用方程以使其满足尺寸一致性），但 QCISD 最好被视为 CCSD 的一种近似。定义方程如下所示（假设采用 Hartree-Fock 轨道，在 QCISD 中应始终使用 HF 轨道）。QCISD 方程显然可以看作是忽略了大量项的 CCSD 方程，而这些被忽略的项在数值上显然不太显著：

<a id="Ch6.E74"></a>
$$
\displaystyle E_{\text{QCISD}} \tag{6.74a}
$$

**Q-Chem** 支持计算 QCISD 能量，可通过关键字 QCISD 请求。如第 [6.13](topic_ccni.md) 节所讨论的，对 QCISD 解的非迭代 QCISD(T) 修正同样可用，以近似计入更高阶激发替换的效应。
