---
title: "8.10.2 有效核势（ECP）拟合"
---

## 8.10.2 有效核势（ECP）拟合

(July 4, 2026)

有效核势（Effective Core Potential, ECP）矩阵元可以说是最难计算的一电子积分之一。事实上，使用当前方法，计算 ECP 积分所花费的时间可能超过计算数量多得多的电子排斥积分（electron repulsion integrals）所花费的时间。**Q-Chem** 5.0 实现了一套最先进的 ECP 实现方案[[933]](../bib_references/bib.md#bib972)

其基础是高效的递推关系（recursion relations）与上界（upper bounds）。
该方法依赖于受限的径向势 $U_{\ell}(r)$，其中径向幂次始终仅为零，*即* $n=0$。虽然这对于某些 ECP（如 Stuttgart-Bonn 基组集合）是成立的，但许多其他 ECP 并不满足这一条件。
