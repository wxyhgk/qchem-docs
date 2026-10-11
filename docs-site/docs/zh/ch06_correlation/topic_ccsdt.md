---
title: "6.12.3 耦合簇单激发、双激发与三激发方法（CCSDT）"
---

## 6.12.3 耦合簇单激发、双激发与三激发方法（CCSDT）

(July 4, 2026)

包含单激发、双激发和三激发的耦合簇（Coupled-Cluster）方法，简称为 CCSDT [[996]](../bib_references/bib.md#bib66)

其在指数形式的波函数 Ansatz 中纳入了单激发、双激发和三激发算符。该方法的理论与 CCSD 方法非常相似——只是完整地包含了三激发项。我们此处仅给出基本方程。这些方程可以与上一节给出的 CCSD 方程进行对比，以便理解 CCSD 与 CCSDT 之间的异同。
由下式定义的 CCSDT 波函数为

<a id="eq_ccsdt_psi"></a>
$$
\left|{\Psi_{\mathrm{CCSD}}}\right\rangle=\exp\left({\hat{T}_{1}+\hat{T}_{2}+\hat{T}_{3}}\right)\left|{\Phi_{0}}\right\rangle \tag{6.64}
$$

其中，算符 $\hat{T}_{1}$ 和 $\hat{T}_{2}$ 由方程 [6.59](Ch6.S12.SS2.md#eq519) 和 [6.60](Ch6.S12.SS2.md#eq520) 定义。
算符 $\hat{T}_{3}$ 定义为

<a id="eq_ccsdt_t3"></a>
$$
\hat{T}_{3}\left|{\Phi_{0}}\right\rangle=\frac{1}{36}\sum_{ijk}^{\mathrm{occ}}{\sum_{abc}^{\mathrm{virt}}{t_{ijk}^{abc}}}\left|{\Phi_{ijk}^{abc}}\right\rangle \tag{6.65}
$$

CCSDT 方程是一组相互耦合的非线性联立方程。
