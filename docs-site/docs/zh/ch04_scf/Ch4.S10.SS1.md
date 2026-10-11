---
title: "4.10.1 引言"
---

## 4.10.1 引言

(July 4, 2026)

xTB 系列半经验紧束缚（semiempirical tight-binding）方法为大分子体系提供了一种高效的低成本电子结构计算途径。当前的 **Q-Chem** 实现基于 Bannwarth、Ehlert 和 Grimme 提出的 GFN2-xTB 哈密顿量[[73]](../bib_references/bib.md#bib58)，
 该哈密顿量将类扩展 Hückel（extended Hückel-like）零级哈密顿量与自洽的各向同性及各向异性静电与交换-关联贡献相结合。
对于开壳层体系，**Q-Chem** 还支持一种非限制自旋极化（unrestricted spin-polarized）变体，其思路源自
Refs. [[986]](../bib_references/bib.md#bib1030)、[[959]](../bib_references/bib.md#bib999) 和
[[958]](../bib_references/bib.md#bib1000) 中描述的 spGFN2-xTB 发展。

## 4.10.1.1 理论背景

GFN2-xTB 属于密度泛函紧束缚（density-functional tight-binding, DFTB）家族，

 其中 Kohn–Sham DFT 能量围绕中性原子参考密度叠加进行展开，

<a id="Ch4.E77"></a>

$$
\rho_{0}(\mathbf{r})=\sum_{A}\rho_{A}^{0}(\mathbf{r}), \tag{4.77}
$$

密度涨落定义为 $\delta\rho=\rho-\rho_{0}$。以示意形式书写，能量展开为

<a id="Ch4.E78"></a>

$$
E[\rho]=E^{(0)}[\rho_{0}]+E^{(1)}[\rho_{0},\delta\rho]+E^{(2)}[\rho_{0},(\delta\rho)^{2}]+E^{(3)}[\rho_{0},(\delta\rho)^{3}]+\cdots. \tag{4.78}
$$

零级项定义了参考原子能量以及一个短程排斥模型，一级项给出类扩展 Hückel 的价层哈密顿量，高阶项则描述对电荷密度涨落的自洽响应。[[73]](../bib_references/bib.md#bib58)

在 GFN2-xTB 中，高阶响应包括各向同性的壳层电荷项以及各向异性的多极修正。

GFN2-xTB 的实用能量表达式为[[73]](../bib_references/bib.md#bib58)

<a id="Ch4.E79"></a>

$$
E_{\mathrm{GFN2-xTB}}=E_{\mathrm{rep}}+E_{\mathrm{disp}}+E_{\mathrm{EHT}}+E_{\mathrm{IES}}+E_{\mathrm{IXC}}+E_{\mathrm{AES}}+E_{\mathrm{AXC}}+G_{\mathrm{Fermi}}. \tag{4.79}
$$

其中，$E_{\mathrm{rep}}$ 是经典的短程排斥项，
$E_{\mathrm{EHT}}$ 是扩展 Hückel 共价键贡献，
$E_{\mathrm{IES}}$ 和 $E_{\mathrm{IXC}}$ 是各向同性静电项与交换-关联项，$E_{\mathrm{AES}}$ 和 $E_{\mathrm{AXC}}$ 是各向异性多极静电与交换-关联修正，而
$G_{\mathrm{Fermi}}$ 是允许分数占据的有限温度熵项。在原始的独立 GFN2-xTB 模型中，
$E_{\mathrm{disp}}$ 是自洽的 D4 色散贡献。
对于开壳层体系，自旋极化扩展基于 Mulliken 自旋布居数和原子自旋常数增加了逐壳层的自旋极化能。[[986]](../bib_references/bib.md#bib1030)

该实现旨在用于快速筛选、结构精修和廉价的单点计算。在实际应用中，它最适合作为在更高精度级别计算之前进行的快速预优化或探索性工具。

**注意：**

当前的 **Q-Chem** 实现*不*包含原始独立 GFN2-xTB 模型中的 D4
色散贡献。因此，总能量和优化结构可能与使用参考程序 `xtb`
得到的结果不同，对于色散相互作用重要的体系尤其如此。
**
