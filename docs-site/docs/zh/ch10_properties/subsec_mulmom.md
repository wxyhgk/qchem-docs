---
title: "10.2.3 Multipole Moments"
---

## 10.2.3 多极矩（Multipole Moments）

（2026 年 7 月 4 日）

本节讨论如何计算整个分子的任意阶静电多极矩，包括基态与激发态的电子密度。不过在有些情况下，将多极矩的电子部分按各个分子轨道（MO）的贡献进行分解会很有用。对于含有未成对电子的体系[[1471]](../bib_references/bib.md#bib1534)，这种分解尤其有用：其一阶矩 $\langle x\rangle$、$\langle y\rangle$ 和 $\langle z\rangle$ 描述了半占据 MO 的质心（平均位置），而二阶矩则确定其回转半径（radius of gyration）$R_{g}$，用以刻画该 MO 的尺寸。设置 PRINT_RADII_GYRE = TRUE 后，**Q-Chem** 会为每个占据 MO 以及 Hartree-Fock 或 Kohn-Sham 参考行列式的总体电子密度打印出质心和回转半径。如果请求了 CIS 或 TDDFT 激发态，该关键字还会为每个激发态电子密度打印质心和回转半径。

**注意：**

这些关键字仅适用于 SCF、DFT、CIS 和 TDDFT 计算。若要为关联波函数计算这些量，请使用相应方法中用于指定性质计算的关键词，如第 [6](../ch06_correlation/chap_correlation.md) 章和第 [7](../ch07_excited/chap_excited.md) 章所述。例如，要计算 CCSD 或 EOM-CCSD 的多极矩及其他性质，请使用 CC_REF_PROP = TRUE 和 CC_EOM_PROP = TRUE。

PRINT_RADII_GYRE

### `PRINT_RADII_GYRE`

> **控制分子轨道质心与回转半径的打印输出。**
>
> * **类型**: `LOGICAL/INTEGER`
> * **默认值**: `FALSE`
> * **可选值**:
>     * TRUE（或 1）
>     * 为每个占据 MO 及每种密度打印质心和回转半径。
>     * 2
>     * 同时打印虚 MO 的质心和回转半径。
>     * FALSE（或 0）
>     * 不计算这些量。
> * **建议**: 无

**Q-Chem** 能够以任意阶数计算电荷密度的笛卡尔（Cartesian）多极矩，既适用于基态，也适用于用 CIS 或 TDDFT 方法计算的激发态。

MULTIPOLE_ORDER

### `MULTIPOLE_ORDER`

> **在请求波函数分析时，决定打印的多极矩最高阶数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `4`
> * **可选值**:
>     * $n$
>     * 计算至 $n$ 阶的矩。
> * **建议**: 除非需要更高阶的多极矩，否则使用默认值。

CIS_MOMENTS

### `CIS_MOMENTS`

> **控制激发态（CIS 或 TDDFT）多极矩的计算**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * FALSE
>     * 不计算激发态的矩。
>     * TRUE
>     * 为每个激发态计算矩。
> * **建议**: 若需要激发态的多极矩，请设置为 TRUE。（这是一项几乎不增加开销的附加计算。）打印哪些多极矩由 MULTIPOLE_ORDER 控制。
