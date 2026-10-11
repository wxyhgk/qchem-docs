---
title: "6.14.5 用于双激发以上价关联的局域对模型"
---

## 6.14.5 用于双激发以上价关联的局域对模型

（2026 年 7 月 4 日）

John Parkhill 与伯克利分校的 Head-Gordon 教授合作，开发了一类对模型（pair models）的实现，能够对 4 电子和 6 电子体系进行定量耦合。由于这些模型分别将耦合簇（Coupled Cluster, CC）方程截断至四激发（quadruples）和六激发（hextuples），因此被称为"完美四激发（Perfect Quadruples, PQ）"模型和"完美六激发（Perfect Hextuples, PH）"模型。这些模型可以视为完全活性空间自洽场（Complete Active Space Self-Consistent Field, CASSCF）的局域近似。PQ 和 PH 模型通过 **Q-Chem** 耦合簇代码的一个扩展来执行，并且为这些模型定义的若干选项会产生相同的效果，尽管其机制可能有所不同（CC_DIIS_START、CC_DIIS_SIZE、CC_DOV_THRESH、CC_CONV、*等等*）。

在实现过程中，非局域耦合簇模型也被实现至 ${\hat{T}}_{6}$。由于其算法是显式稀疏的，相对于现有 CCSD 实现而言其计算代价要高得多（绝不应用来替代现有的 CCMAN 代码），但这一能力可能对开发用途有价值，且在计算可行的情况下，高于 CCSDTQ 的模型具有极高的精度。若要使用 PQ、PH、它们的含动态关联的"+SD"版本，或这套机器生成的簇代码，请设置 METHOD = MGC。

MGC_AMODEL

### `MGC_AMODEL`

> **近似簇模型的选择。**
>
> * **类型**：`INTEGER`
> * **默认值**：`Determines`
> * **选项**：
>     * 0
>     * 局域活性空间振幅迭代（先用你选择的方法预计算广义价键（Generalized Valence Bond, GVB）轨道（RPP 效果良好））。
>     * 7
>     * 使用 VOD 两步求解器进行轨道优化。
>     * （仅实验性使用，需配合 MGC_AMPS = 2、24、246）
>     * 8
>     * 传统耦合簇，直至 CCSDTQPH。
>     * 9
>     * 对模型的多参考组态耦合簇（Multi-Reference Coupled Cluster, MR-CC）版本。（实验性）
> * **建议**：无

MGC_NLPAIRS

### `MGC_NLPAIRS`

> **振幅上的局域对数目。**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **选项**：
>     * 必须大于 1，其对应 PP 模型。
>     * PQ 取 2，PH 取 3。
> * **建议**：无

MGC_AMPS

### `MGC_AMPS`

> **振幅截断方式的选择**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **选项**：
>     * 2
>     * $\leq$
>     * n
>     * $\leq$
>     * 123456，一个已排序的整数列表，对应每一个将被迭代的振幅。PQ 选择 1234，PH 选择 123456
> * **建议**：无

MGC_LOCALINTS

### `MGC_LOCALINTS`

> **对积分施加的对过滤。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * 对双电子积分施加对过滤，可显著降低计算代价。对于大于 1 的对局域性通常很有用。
> * **建议**：无

MGC_LOCALINTER

### `MGC_LOCALINTER`

> **对中间量施加的对过滤。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * 任何非零值都会对中间量（intermediates）施加对约束，可显著降低计算代价。对于 $\leq$ 2 的对局域性不推荐使用
> * **建议**：无
