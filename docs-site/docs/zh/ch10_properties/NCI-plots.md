---
title: "10.5.6 非共价相互作用（NCI）图"
---

## 10.5.6 非共价相互作用（NCI）图

（2026 年 7 月 4 日）

Yang Weitao（杨伟涛）及其合作者[[652]](../bib_references/bib.md#bib676) 表明，
约化密度梯度（reduced density gradient），

<a id="Ch10.E62"></a>
$$
s(\mathbf{r})=\left(\frac{1}{2(3\pi^{2})^{1/3}}\right)\frac{\|\hat{\bm{\nabla}}\rho(\mathbf{r})\|}{\rho(\mathbf{r})^{4/3}} \tag{10.62}
$$

为非共价相互作用提供了一个便捷的判据。非共价相互作用的特征是：在电子密度本身很小的空间区域中存在较大的密度梯度，从而导致 $s(\mathbf{r})$ 出现非常大的值。**Q-Chem** 能够在三维空间中生成函数 $s(\mathbf{r})$ 的非共价相互作用（NCI）图。若要生成这些图，请将 *$rem* 变量 PLOT_REDUCED_DENSITY_GRAD 设置为 TRUE。
（参见 `$QC/samples` 目录中的输入示例 `nci-c8h14.in`。）
