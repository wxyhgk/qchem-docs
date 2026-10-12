---
title: "12.5.5 作业控制选项"
---

## 12.5.5 作业控制选项

（2026 年 7 月 4 日）

### `FRGM_METHOD`

> **指定一种局域投影（locally-projected）方法。**
>
> * **类型**：`STRING`
> * **默认值**：`NONE`
> * **可选值**：
>     * STOLL
>     * 求解 Stoll 提出的局域投影自洽场（SCF）方程。
>     * GIA
>     * 求解 Gianinetti 提出的局域投影 SCF 方程。
>     * NOSCF_RS
>     * 对
>     * FRAGMO
>     * 初始猜测施加单步 Roothaan 修正。
>     * NOSCF_ARS
>     * 对
>     * FRAGMO
>     * 初始猜测施加近似的单步 Roothaan 修正。
>     * NOSCF_DRS
>     * 对
>     * FRAGMO
>     * 初始猜测施加双步 Roothaan 修正。
>     * NOSCF_RS_FOCK
>     * 单步 Roothaan 分子轨道（MO）对应的未收敛 SCF 能量。
> * **使用建议**：STOLL 与 GIA 用于对局域化分子轨道（ALMO）进行变分优化；NOSCF 系列选项用于对 FRAGMO 初始猜测进行快速的计算修正。

### `FRGM_LPCORR`

> **指定在局域投影方程收敛之后所执行的修正方法。**
>
> * **类型**：`STRING`
> * **默认值**：`NONE`
> * **可选值**：
>     * ARS
>     * 近似 Roothaan 步微扰修正。
>     * RS
>     * 单步 Roothaan 微扰修正。
>     * EXACT_SCF
>     * 完整的 SCF 变分修正。
>     * ARS_EXACT_SCF
>     * 在同一次作业中同时执行
>     * ARS
>     * 与
>     * EXACT_SCF
>     * 。
>     * RS_EXACT_SCF
>     * 在同一次作业中同时执行
>     * RS
>     * 与
>     * EXACT_SCF
>     * 。
> * **使用建议**：对于大基组建议使用 ARS；若 ARS 失败则改用 RS。

### `SCF_PRINT_FRGM`

> **控制对孤立片段（isolated fragments）运行的 Q-Chem 作业的输出。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **可选值**：
>     * TRUE
>     * 将输出打印到父作业的输出文件中。
>     * FALSE
>     * 不打印输出。
> * **使用建议**：若需要了解孤立片段的详细信息，请设置为 TRUE。

### `EDA_BSSE`

> **在进行能量分解分析（Energy Decomposition Analysis, EDA）时计算基组重叠误差（Basis Set Superposition Error, BSSE）修正。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **可选值**：
>     * TRUE/FALSE
> * **使用建议**：除非使用了非常大的基组，否则应设置为 TRUE。

### `EDA_COVP`

> **在计算 RS 或 ARS 电荷转移修正时执行 COVP 分析。目前 COVP 分析仅支持由两个片段组成的体系。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **可选值**：
>     * TRUE/FALSE
> * **使用建议**：在 EDA 或 SCF-MI(RS) 作业中执行 COVP 分析时设置为 TRUE。

### `EDA_PRINT_COVP`

> **在运行结束时用 COVP 轨道替换最终的分子轨道（MO）。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **可选值**：
>     * TRUE/FALSE
> * **使用建议**：若希望打印 COVP 轨道而非传统 MO，请设置为 TRUE。

### `NVO_LIN_MAX_ITE`

> **单激发振幅方程预条件共轭梯度（preconditioned conjugate gradient）求解器的最大迭代次数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`30`
> * **可选值**：
>     * $n$
>     * 用户自定义的迭代次数。
> * **使用建议**：无。

### `NVO_LIN_CONVERGENCE`

> **单激发振幅方程预条件共轭梯度求解器的目标误差因子。**
>
> * **类型**：`INTEGER`
> * **默认值**：`3`
> * **可选值**：
>     * $n$
>     * 用户自定义的数值。
> * **使用建议**：若最大残差小于 $10^{-n}$ 与当前 DIIS 误差的乘积，则认为单激发振幅方程的解已收敛。对于 ARS 修正，$n$ 会自动设为 1，因为局域投影的 DIIS 误差通常比完整 DIIS 误差小若干个数量级。

### `NVO_METHOD`

> **设置用于使单激发振幅方程解收敛的方法。**
>
> * **类型**：`INTEGER`
> * **默认值**：`9`
> * **可选值**：
>     * $n$
>     * 用户自定义的数值。
> * **使用建议**：这是一个实验性选项。请使用默认值。

### `NVO_UVV_PRECISION`

> **控制由单激发振幅计算 $U_{vv}$ 块时泰勒级数的收敛精度。当某一项的最大元素小于 $10^{-n}$ 时，认为该级数已收敛。**
>
> * **类型**：`INTEGER`
> * **默认值**：`11`
> * **可选值**：
>     * $n$
>     * 用户自定义的数值。
> * **使用建议**：该值必须等于或大于 THRESH。

### `NVO_UVV_MAXPWR`

> **控制由单激发振幅计算 $U_{vv}$ 分块时泰勒级数的收敛性。若级数在第 $n$ 项仍未收敛，则改用代价更高的直接求逆来计算 $U_{vv}$ 分块。**
>
> * **类型**: `INTEGER`
> * **默认值**: `10`
> * **选项**:
>     * $n$: 用户自定义的数值。
> * **建议**: 无。

### `NVO_TRUNCATE_DIST`

> **指定在构造预条件器（preconditioner）时使用 Fock 矩阵的哪些原子分块。**
>
> * **类型**: `INTEGER`
> * **默认值**: `$-$`
> * **选项**:
>     * $n>0$: 若一对原子之间的距离超过
>     * $n$: 埃（Ångstroms），则不包含对应的原子分块。 $-$
>     * `2`: 不使用距离阈值，改为使用 NVO_TRUNCATE_PRECOND。 $-$
>     * `1`: 包含所有分块。
>     * `0`: 仅包含对角分块。
> * **建议**: 该选项不影响最终结果，但会影响 PCG 算法的收敛速度。对于小体系，使用默认值即可。

### `NVO_TRUNCATE_PRECOND`

> **指定在构造预条件器时使用 Fock 矩阵的哪些原子分块。仅当 `NVO_TRUNCATE_DIST` 设置为 $-2$ 时，本变量才会生效。**
>
> * **类型**: `INTEGER`
> * **默认值**: `2`
> * **选项**:
>     * $n$: 若某一原子分块中的最大元素小于 $n$，则不包含该分块。
> * **建议**: 无。
