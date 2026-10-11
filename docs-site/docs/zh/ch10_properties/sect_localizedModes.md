---
title: "10.8.5 定域模式振动分析"
---

## 10.8.5 定域模式振动分析

（2026 年 7 月 4 日）

谐振频率（harmonic frequencies）的计算会得到由通常高度离域（de-localized）的坐标所描述的分子振动。对于较大的分子，许多振动模式可能共同贡献于单个观测到的谱带，因而关于定域化学单元之间相互作用的信息会变得不那么容易获取。在某些情况下，采用与本手册前文讨论的定域轨道方案（localized orbital schemes）相似的流程对振动模式进行定域化，从而可以提供一种更符合化学直觉的方式来分析光谱数据，[[620]](../bib_references/bib.md#bib640)
 解释二维振动光谱，[[524]](../bib_references/bib.md#bib537)
 或改进超越谐振近似的计算。[[239]](../bib_references/bib.md#bib240)
 此外，还可以通过调用 LOCALFREQ_SELECT rem 变量，在定域化计算中仅包含法正模式（normal modes）的一个子集。这对于改善较大分子的收敛性，或者探索特定振动模式之间的耦合可能很有用。这些模式在 *$alist* 块中定义。另外，也可以使用 LOCALFREQ_GROUPS 及相关输入，在单次计算中分别对高频模式和低频模式进行定域化。

LOCALFREQ

### `LOCALFREQ`

> **控制是否执行振动模式定域化计算。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 1
>     * 使用类似 Pipek-Mezey 的判据进行定域模式计算。
>     * 2
>     * 使用类似 Boys 的判据进行定域模式计算。
> * **建议**：无

LOCALFREQ_THRESH

### `LOCALFREQ_THRESH`

> **当定域化判据的变化小于 $10^{\mathrm{-LOCALFREQ\_THRESH}}$ 时，认为模式定域化已收敛。**
>
> * **类型**：`INTEGER`
> * **默认值**：`6`
> * **选项**：
>     * $n$
>     * 用户指定的整数。
> * **建议**：无

LOCALFREQ_MAX_ITER

### `LOCALFREQ_MAX_ITER`

> **控制允许的模式定域化扫描（sweeps）的最大次数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`200`
> * **选项**：
>     * $n$
>     * 用户指定的整数。
> * **建议**：无

LOCALFREQ_SELECT

### `LOCALFREQ_SELECT`

> **选取一个法正模式子集，用于后续的非谐（anharmonic）频率分析。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 选取法正模式的一个子集。
> * **建议**：无

LOCALFREQ_GROUPS

### `LOCALFREQ_GROUPS`

> **在定域模式计算中，选取需要分别定域化的频率组数。各组的大小随后通过 LOCALFREQ_GROUP1 、 LOCALFREQ_GROUP2 和 LOCALFREQ_GROUP3 关键字控制。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 1
>     * 定义一个独立定域化的模式子集。
>     * 2
>     * 定义两个独立定域化的模式子集。
>     * 3
>     * 定义三个独立定域化的模式子集。
> * **建议**：无

LOCALFREQ_GROUP1

### `LOCALFREQ_GROUP1`

> **当关键字 LOCALFREQ_GROUPS > 0 时，选取包含在第一个独立定域化模式子集中的模式数量。**
>
> * **类型**：`INTEGER`
> * **默认值**：`NONE`
> * **选项**：
>     * $n$
>     * 用户指定的整数。
> * **建议**：模式的纳入从最低频率模式开始，随后按能量递增顺序，直至所定义的值。

LOCALFREQ_GROUP2 和 LOCALFREQ_GROUP3 的定义类似。
