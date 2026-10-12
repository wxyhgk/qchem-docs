---
title: "5.11.2 电子计数方式"
---

## 5.11.2 电子计数方式

（2026 年 7 月 4 日）

## Becke 划分方案：

在密度泛函理论（Density Functional Theory, DFT）计算中，对总密度的积分是在分子网格上求值的，该网格被系统性地切分为相互嵌套的多中心原子求积网格。[[94]](../bib_references/bib.md#bib73)
 这一原子求积方案基于原子胞元函数 $P_{a}(\textbf{r})$ 的定义，
它们确立了以每个原子为中心的光滑 Voronoi 多面体。这些胞元函数
是开关函数（switching function）的乘积，用以定义原子 $a$ 的原子胞元，其值在 $a$ 的原子核附近约为 $\approx 1$，
并迅速衰减到在其他原子核附近约为 $\approx 0$。
该方案所提供的积分权重在任何实际的 DFT 计算中都会与 Lebedev 求积权重相乘：

<a id="eq:_becke_cell"></a>

$$
w_{n}(\mathbf{r})=\frac{P_{n}(\mathbf{r})}{\sum\limits_{m}P_{m}(\mathbf{r})} \tag{5.72}
$$

在某些情况下，打印由这些原子胞元函数定义的原子 Becke 布居数可能很有用。可以通过在输入文件中将 POP_BECKE 设置为 TRUE 来请求进行 Becke 布居分析。

### `POP_BECKE`

> **控制原子 Becke 布居数的打印输出。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `TRUE`: 打印原子 Becke 布居数。
>     * `FALSE`: 不打印原子 Becke 布居数。
> * **建议**: 无

默认的求积方案使用在键中点处精确相交的原子胞元函数。因此，默认的原子胞元函数会给出在物理上无意义的原子布居数。不过，可以利用原子半径判据来平移原子胞元函数的交点。[[94]](../bib_references/bib.md#bib73)
 在平移相邻原子胞元函数的交点时，Becke 权重从
$\approx 1$ 开始下降到 $\approx 0$ 的位置会随每个原子的原子半径而变化。
虽然原子半径的选择是任意的，但这些原子胞元平移为底层原子求积的划分引入了物理依据。**Q-Chem** 中提供了两种用于 Becke 权重的原子半径选择，即 Bragg 和 Slater 提出的经验半径[[1268]](../bib_references/bib.md#bib1321)
 以及 Pacios 提出的
*ab initio*（从头算）导出的权重[[1034]](../bib_references/bib.md#bib1077)。

### `BECKE_SHIFT`

> **控制在确定 Becke 权重时的原子胞元平移。**
>
> * **类型**: `STRING`
> * **默认值**: `BRAGG_SLATER`
> * **可选值**:
>     * `UNSHIFTED`: 使用不含原子尺寸修正的 Becke 权重， 即基于键中点的划分。
>     * `BRAGG_SLATER`: 使用 Bragg 和 Slater 提出的经验半径。
>     * `UNIVERSAL_DENSITY`: 使用 ab initio 方法导出的、由 Pacios 提出的半径。
> * **建议**: 如果关注的是默认原子求积的划分，请使用 UNSHIFTED。如果用于物理诠释，请选择 BRAGG_SLATER 或 UNIVERSAL_DENSITY。所有 cDFT 计算以及 POP_BECKE = TRUE 的计算将默认使用 BRAGG_SLATER 半径，否则默认网格为 UNSHIFTED。

## 基于片段的 Hirshfeld 划分方案：

一种远没有那么任意的电子计数方法来自于基于片段的 Hirshfeld 划分。[[1160]](../bib_references/bib.md#bib1214)

基于片段的 Hirshfeld（Fragment-Based Hirshfeld, FBH）划分使用由孤立片段密度构造的权重，其形式为

<a id="Ch5.E73"></a>

$$
w_{n}(\text{{r}})=\frac{\rho_{n}(\text{{r}})}{\sum\limits_{m}\rho_{m}(\text{{r}})}~{}, \tag{5.73}
$$

其中 $\rho_{n}(\text{{r}})$ 是孤立片段 $n$ 的密度。
需要注意的是，与原子 Becke 划分不同，FBH 划分并非由原子权重的线性组合构造而成，而是直接由完整片段的密度构建而来。
FBH 划分直接来自孤立片段的密度，这些密度不像 Becke 划分中有效原子半径的选择那样具有任意性。
为了应用 FBH 划分，必须在 *$molecule* 区块中定义片段以承载约束条件，但 *$cdft* 区块的输入保持不变，仍按逐原子的方式施加约束。

### `CDFT_POP`

> **设置 cDFT 或 cDFT-CI 作业的电荷划分方案。**
>
> * **类型**: `STRING`
> * **默认值**: `BECKE`
> * **可选值**:
>     * `BECKE`: 原子 Becke 函数的线性组合
>     * `FBH`: 基于片段的 Hirshfeld 划分
> * **建议**: 无
