---
title: "9.2.2 Optimize（优化）作业控制"
---

## 9.2.2 **Optimize（优化）**作业控制

（2026 年 7 月 4 日）

GEOM_OPT_HESSIAN

### `GEOM_OPT_HESSIAN`

> **决定初始 Hessian（黑塞矩阵）的状态。**
>
> * **类型**: `STRING/INTEGER`
> * **默认值**: `$-$`
> * **选项**:
>     * $-$
>     * 1
>     * 基于力常数矩阵（force constant matrix）的近似 Hessian（与
>     * Libopt3
>     * 中的 “Model” 选项相同）
>     * READ
>     * 具有精确或初始 Hessian。若为笛卡尔坐标则直接使用，若为内坐标则进行转换。
> * **建议**: 精确的初始 Hessian 可提升优化器的性能，但计算代价可能较高。注意 Libopt3 中提供了更多初始 Hessian 选项，由 $geom_opt 段下的 INITIAL_HESSIAN 控制（见第 9.2.5 节）。

GEOM_OPT_COORDS

### `GEOM_OPT_COORDS`

> **控制优化所用坐标的类型。**
>
> * **类型**: `INTEGER`
> * **默认值**: `$-$`
> * **选项**:
>     * 0
>     * 在笛卡尔坐标（Cartesian coordinates）中进行优化。
>     * 1
>     * 生成内坐标（internal coordinates）并在其中优化，若失败则中止。
>     * $-$
>     * 1
>     * 生成内坐标并在其中优化，若在优化的任何阶段失败，则切换为笛卡尔坐标并继续。
>     * 2
>     * 在 $Z$ 矩阵坐标（$Z$-matrix coordinates）中优化，若失败则中止。
>     * $-$
>     * 2
>     * 在 $Z$ 矩阵坐标中优化，若在优化的任何阶段失败，则切换为笛卡尔坐标并继续。
> * **建议**: 使用默认值，因为离域内坐标（delocalized internals）更高效。注意在 $Z$ 矩阵坐标中优化要求输入以 $Z$ 矩阵格式给出。

GEOM_OPT_TOL_GRADIENT

### `GEOM_OPT_TOL_GRADIENT`

> **基于最大梯度分量的收敛判据。**
>
> * **类型**: `INTEGER`
> * **默认值**: `300`
> * **选项**:
>     * $n$
>     * 整数值（容差 =
>     * $n\times 10^{-6}$
>     * ）。
> * **建议**: 使用默认值。要判定收敛，必须满足 GEOM_OPT_TOL_GRADIENT 以及 GEOM_OPT_TOL_DISPLACEMENT 和 GEOM_OPT_TOL_ENERGY 中的至少一个。

GEOM_OPT_TOL_DISPLACEMENT

### `GEOM_OPT_TOL_DISPLACEMENT`

> **基于最大原子位移的收敛判据。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1200`
> * **选项**:
>     * $n$
>     * 整数值（容差 =
>     * $n\times 10^{-6}$
>     * ）。
> * **建议**: 使用默认值。要判定收敛，必须满足 GEOM_OPT_TOL_GRADIENT 以及 GEOM_OPT_TOL_DISPLACEMENT 和 GEOM_OPT_TOL_ENERGY 中的至少一个。

GEOM_OPT_TOL_ENERGY

### `GEOM_OPT_TOL_ENERGY`

> **基于相邻优化循环能量变化的收敛判据。**
>
> * **类型**: `INTEGER`
> * **默认值**: `100`
> * **选项**:
>     * $n$
>     * 整数值（容差 = 值
>     * $n\times 10^{-8}$
>     * ）。
> * **建议**: 使用默认值。要判定收敛，必须满足 GEOM_OPT_TOL_GRADIENT 以及 GEOM_OPT_TOL_DISPLACEMENT 和 GEOM_OPT_TOL_ENERGY 中的至少一个。

GEOM_OPT_MAX_CYCLES

### `GEOM_OPT_MAX_CYCLES`

> **最大优化循环次数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `50`
> * **选项**:
>     * $n$
>     * 用户自定义的正整数。
> * **建议**: 默认值对大多数情况已经足够。若初始猜测几何构型较差，或体系势能面较平缓，可适当增大。

GEOM_OPT_PRINT

### `GEOM_OPT_PRINT`

> **控制 Optimize（优化）的输出详细信息量。**
>
> * **类型**: `INTEGER`
> * **默认值**: `3`
> * **选项**:
>     * 0
>     * 仅输出错误信息。
>     * 1
>     * 在级别 0 基础上增加摘要和警告信息输出。
>     * 2
>     * 在级别 1 基础上增加标准信息。
>     * 3
>     * 在级别 2 基础上增加梯度（gradient）输出。
>     * 4
>     * 在级别 3 基础上增加 Hessian 输出。
>     * 5
>     * 在级别 4 基础上增加迭代信息输出。
>     * 6
>     * 在级别 5 基础上增加内坐标生成信息输出。
>     * 7
>     * 调试（Debug）信息输出。
> * **建议**: 使用默认值。

GEOM_OPT_SYMFLAG

### `GEOM_OPT_SYMFLAG`

> **控制在 Optimize（优化）中是否使用对称性。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **选项**:
>     * TRUE
>     * 使用点群对称性（point group symmetry）。
>     * FALSE
>     * 不使用点群对称性。
> * **建议**: 使用默认值。

GEOM_OPT_MODE

### `GEOM_OPT_MODE`

> **决定过渡态搜索（transition state search）过程中遵循的 Hessian 模式。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 关闭模式遵循（mode following）。
>     * $n$
>     * 沿模式
>     * $n$
>     * 求极大值。
> * **建议**: 对于几何优化，使用默认值。

GEOM_OPT_MAX_DIIS

### `GEOM_OPT_MAX_DIIS`

> **控制 GDIIS 子空间的最大规模。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 不使用 GDIIS。
>     * -1
>     * 默认规模 = min(NDEG, NATOMS, 4)，其中 NDEG = 分子自由度数目。
>     * $n$
>     * 由用户指定的规模。
> * **建议**: 使用默认值，或不要将 $n$ 设置得过大。

GEOM_OPT_DMAX

### `GEOM_OPT_DMAX`

> **允许的最大步长。所给数值将乘以 10 ${}^{-3}$ 。**
>
> * **类型**: `INTEGER`
> * **默认值**: `300`
> * **选项**:
>     * $n$
>     * 用户自定义的截断值。
> * **建议**: 使用默认值。

GEOM_OPT_UPDATE

### `GEOM_OPT_UPDATE`

> **控制 Hessian 更新算法。**
>
> * **类型**: `INTEGER`
> * **默认值**: `-1`
> * **选项**:
>     * -1
>     * 使用默认的更新算法。
>     * 0
>     * 不更新 Hessian（不推荐）。
>     * 1
>     * Murtagh-Sargent 更新。
>     * 2
>     * Powell 更新。
>     * 3
>     * Powell/Murtagh-Sargent 更新（TS 默认）。
>     * 4
>     * BFGS 更新（OPT 默认）。
>     * 5
>     * 带保障措施以确保保持正定性的 BFGS 更新（GDIIS 默认）。
> * **建议**: 使用默认值。

GEOM_OPT_LINEAR_ANGLE

### `GEOM_OPT_LINEAR_ANGLE`

> **近线性键角（near linear bond angles）的阈值（单位：度）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `165 degrees.`
> * **选项**:
>     * $n$
>     * 用户自定义的级别。
> * **建议**: 使用默认值。

FINITEDIFFSZ_POWER

### `FINITEDIFFSZ_POWER`

> **控制有限差分法计算导数时所用步长数量级的指数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `5`
> * **选项**:
>     * $n$
>     * 使用指数
>     * $10^{-n}$
>     * 。
> * **建议**: 无。

FDIFF_STEPSIZE

### `FDIFF_STEPSIZE`

> **有限差分法计算导数时所使用的位移量。**
>
> * **类型**: `INTEGER`
> * **默认值**: `100`
> * **选项**:
>     * $n$
>     * 使用步长
>     * $n\times 10^{-m}$
>     * ，其中
>     * $m$
>     * 为
>     * FINITEDIFFSZ_POWER
>     * 的值。
> * **建议**: 使用默认值；但当势能面非常平坦时应使用较大的值。三阶和四阶导数参见 FDIFF_STEPSIZE_QFF。
