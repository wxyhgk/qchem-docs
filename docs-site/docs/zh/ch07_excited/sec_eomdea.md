---
title: "7.9.8 EOM-DEA-CCSD"
---

## 7.9.8 EOM-DEA-CCSD

（2026 年 7 月 4 日）

在 EOM-DEA（逐出电子耦合簇）方法中，目标态由作用于 $N-2$ 电子参考态[[1077]](../bib_references/bib.md#bib1122)上的 $2p$ 与 $1h3p$ 算符来描述：

<a id="DEA:WF"></a>

$$
\Psi_{k}=\hat{R}_{N+2}\Psi_{0}(N-2), \tag{7.102}
$$

其中激发算符 $R$ 具有如下形式：

<a id="eq:R-DEA"></a>

$$
\hat{R}=\frac{1}{2}\sum_{ab}r_{ab}a^{\dagger}b^{\dagger}+\frac{1}{6}\sum_{iabc}r_{i}^{abc}a^{\dagger}b^{\dagger}c^{\dagger}i. \tag{7.103}
$$

EOM-DEA 适用于计算双自由基态，包括自旋翻转（SF）流形之外的激发态。在计算中性双自由基时，EOM-DEA 应使用带 +2 电荷的参考态。EOM-DEA 同样适合描述某些类型的双重激发态，例如乙烯中的 $\ldots(\pi)^{0}(\pi^{*})^{2}$ 态。通过设置 `DEA_STATES`，或 `DEA_SINGLETS` 与 `DEA_TRIPLETS` 关键字即可调用 EOM-DEA 计算。在一些更为特殊的计算中，例如针对开壳层参考态的 EOM-DEA，`DEA_AA_STATES`、`DEA_BB_STATES` 与 `DEA_AB_STATES` 关键字可能会有用。EOM-CCSD 和 EOM-MP2 两种变体均可使用。

**注意：**

在某些 EOM-DEA-CCSD 的应用中，仅包含了 $2p$ 算符。
