---
title: "5.5.1 引言"
---

## 5.5.1 引言

(July 4, 2026)

在实际的密度泛函理论（Density Functional Theory, DFT）计算中，所使用的近似交换-关联泛函的形式相当复杂，因此涉及这些泛函的所需积分一般无法解析求解。**Q-Chem** 通过对交换-关联被积函数直接施加数值求积（Numerical Quadrature）来计算这些积分。程序提供了若干标准求积网格（“SG-$n$”，$n=0,1,2,3$），其默认值会根据所涉泛函的复杂度自动设置。

**Q-Chem** 中的求积方法与许多 DFT 程序中的方法大体相似。多中心交换-关联（XC）积分首先利用核权重函数（nuclear weight function）划分为“原子”贡献。**Q-Chem** 采用 Becke 的核划分方案，[[94]](../bib_references/bib.md#bib73)
 但未使用文献 [[94]](../bib_references/bib.md#bib73)
 中的“原子尺寸调整（atomic size adjustments）”。随后通过标准单中心数值技术计算这些原子积分。因此，交换-关联能量可表示为

<a id="eq439"></a>
$$
E_{\mathrm{XC}}=\sum_{A}^{\rm atoms}\sum_{i\in A}^{\rm points}w_{Ai}f(\mathbf{r}_{Ai})\;, \tag{5.15}
$$

其中函数 $f$ 即前述的 XC 被积函数，量 $w_{Ai}$ 为求积权重。对 $i$ 的求和遍历属于原子 $A$ 的网格点，这些点位于位置 $\mathbf{r}_{Ai}=\mathbf{R}_{A}+\mathbf{r}_{i}$，因此该方法只需要选择一个合适的单中心积分网格（以定义 $\mathbf{r}_{i}$），且该网格与核构型无关。**Q-Chem** 对这些网格的实现方式保证了 $E_{\rm XC}$ 具有旋转不变性，*i.e.*，当分子在空间中发生刚性旋转时其值不变。[[648]](../bib_references/bib.md#bib672)

求积网格进一步分为径向部分和角向部分。在 **Q-Chem** 中，径向部分通常采用 Murray *et al.* 提出的 Euler-Maclaurin 方案，[[967]](../bib_references/bib.md#bib1009)
 该方案将半无限区间 $[0,\infty)$ 映射到 $[0,1)$，并对变换后的被积函数应用扩展梯形法则。另一种选择是 Gill 和 Chien 提出的径向方案，其基于区间 $[0,1]$ 上采用不同权重函数的高斯求积。[[240]](../bib_references/bib.md#bib241)
 这种“MultiExp”径向求积对呈指数函数几何级数线性组合的被积函数是精确的，因此非常适合计算原子积分。然而，随着径向点数增加，生成 MultiExp 求积点的问题会变得越来越病态，因此对于 **Q-Chem** 中最大的标准网格，[[953]](../bib_references/bib.md#bib993)

即 SG-2 和 SG-3，[[301]](../bib_references/bib.md#bib305)
 采用了“双指数（double exponential）”径向求积方案。[[953]](../bib_references/bib.md#bib993)

（见第 [5.5.3 节](sect_standard-quad.md)。）
