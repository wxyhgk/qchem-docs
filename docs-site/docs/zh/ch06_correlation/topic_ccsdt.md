---
title: "6.12.3 耦合簇单激发、双激发与三激发方法（CCSDT）"
---

## 6.12.3 耦合簇单激发、双激发与三激发方法（CCSDT）

（2026 年 7 月 4 日）

包含单激发、双激发和三激发的耦合簇（Coupled-Cluster）方法，简称为 CCSDT [[996]](../bib_references/bib.md#bib66)，在指数 ansatz 中包含了单激发、双激发和三激发算符。该方法的理论与 CCSD 非常相似——只不过完整包含了三激发。我们在此仅给出基本方程。读者可将这些方程与前一节给出的 CCSD 方程进行对比，以了解 CCSD 与 CCSDT 之间的异同。
由下式定义的 CCSDT 波函数为

<a id="eq_ccsdt_psi"></a>

$$
\left|{\Psi_{\mathrm{CCSD}}}\right\rangle=\exp\left({\hat{T}_{1}+\hat{T}_{2}+\hat{T}_{3}}\right)\left|{\Phi_{0}}\right\rangle \tag{6.64}
$$

其中，算符 $\hat{T}_{1}$ 和 $\hat{T}_{2}$ 由公式 [6.59](Ch6.S12.SS2.md#eq519) 和 [6.60](Ch6.S12.SS2.md#eq520) 定义。
算符 $\hat{T}_{3}$ 定义为

<a id="eq_ccsdt_t3"></a>

$$
\hat{T}_{3}\left|{\Phi_{0}}\right\rangle=\frac{1}{36}\sum_{ijk}^{\mathrm{occ}}{\sum_{abc}^{\mathrm{virt}}{t_{ijk}^{abc}}}\left|{\Phi_{ijk}^{abc}}\right\rangle \tag{6.65}
$$

CCSDT 方程是张量 $\hat{T}_{1}$、$\hat{T}_{2}$ 和 $\hat{T}_{3}$ 的耦合非线性联立方程组。然而，相关能仅取决于 $\hat{T}_{1}$ 和 $\hat{T}_{2}$ 振幅（能量方程与公式 [6.61](Ch6.S12.SS2.md#eq521) 相同）。三激发的影响源于单激发、双激发和三激发之间的相互耦合：

<a id="A3.S8.EGx23"></a>

$$
\displaystyle E_{\mathrm{CCSDT}} \tag{6.66}
$$

目前，CCSDT 功能仅可用于计算相关能。
