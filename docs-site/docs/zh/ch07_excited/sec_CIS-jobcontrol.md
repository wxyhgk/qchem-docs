---
title: "7.2.4 作业控制选项"
---

## 7.2.4 作业控制选项

（2026 年 7 月 4 日）

用于运行 CIS 及相关方法的基本作业控制变量在第 [7.2.4.1 节](#sec:CIS-jobcontrol:Basic) 中讨论，更高级的选项列于第 [7.2.4.2 节](#sec:CIS-jobcontrol:Advanced)。

## 7.2.4.1 基本作业控制

请求 CIS 类作业的方式是：像基态 Hartree-Fock（HF）计算那样，将 *$rem* 变量设置为 EXCHANGE = HF 且 CORRELATION = NONE，然后再使用 *$rem* 关键字 CIS_N_ROOTS 指定所需的激发态根数。

**注意：

对于 RHF 情形，除非通过 CIS_TRIPLETS 和 CIS_SINGLETS 另行指定，否则将计算 $n$ 个单重态和 $n$ 个三重态。
**

CIS_N_ROOTS

### `CIS_N_ROOTS`

> **设置要求解的 CI 单激发（CIS）激发态根数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * $n>0$
>     * 求解
>     * $n$
>     * 个 CIS 激发态。
> * **建议**: 无

CIS_SINGLETS

### `CIS_SINGLETS`

> **在 RCIS 计算中求解单重态激发态（在 UCIS 中被忽略）。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **选项**:
>     * TRUE
>     * 求解单重态。
>     * FALSE
>     * 不求解单重态。
> * **建议**: 无

CIS_TRIPLETS

### `CIS_TRIPLETS`

> **在 RCIS 计算中求解三重态激发态（在 UCIS 中被忽略）。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **选项**:
>     * TRUE
>     * 求解三重态。
>     * FALSE
>     * 不求解三重态。
> * **建议**: 无

CIS_STATE_DERIV

### `CIS_STATE_DERIV`

> **为激发态优化和振动分析指定 CIS 态。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * 选择第
>     * $n$
>     * 个态。
> * **建议**: 注意检查由于态交叉（state crossings）导致优化过程中各态的顺序是否发生变化。

CIS_STATE_MULTIGRAD

### `CIS_STATE_MULTIGRAD`

> **为梯度计算选择 SCF 态及所有 CIS/TDDFT 态。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 1
>     * 对所有 CIS/TDDFT 态计算梯度。
>     * 2
>     * 对 SCF 态及所有 CIS/TDDFT 态计算梯度。
> * **建议**: 是否需要取决于具体应用。如果只需要一个梯度，请改用 CIS_STATE_DERIV。

RPA

### `RPA`

> **在 CIS 或 TDDFT/TDA 计算之外额外进行 RPA（随机相位近似）计算。**
>
> * **类型**: `LOGICAL/INTEGER`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不进行 RPA 计算。
>     * TRUE
>     * 进行 RPA 计算。
>     * 2
>     * 不进行 CIS 或 TDDFT/TDA 计算，直接进行 RPA 计算。
> * **建议**: RPA = 2 不适用于限制开壳层（restricted open-shell）波函数。

SPIN_FLIP

### `SPIN_FLIP`

> **选择执行标准激发态计算还是自旋翻转（spin-flip）计算。在最常见的用法中，对于电子数为偶数的体系，自旋多重度应设为 3；对于电子数为奇数的体系，应设为 4。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE/FALSE
> * **建议**: 无

SPIN_FLIP_XCIS

### `SPIN_FLIP_XCIS`

> **控制是否进行 SF-XCIS 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不进行 SF-XCIS 计算。
>     * TRUE
>     * 进行 SF-XCIS 计算（需要 ROHF 三重态基态）。
> * **建议**: 无

SFX_AMP_OCC_A

### `SFX_AMP_OCC_A`

> **在 SF-XCIS 方法中定义自定义的振幅初始猜测（guess）向量。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * 构建一个在第
>     * $n$
>     * 个轨道上带有
>     * $\alpha$
>     * 空穴的猜测振幅
>     * （需要 SFX_AMP_VIR_B）。
> * **建议**: 仅在默认猜测不满足要求时使用。

SFX_AMP_VIR_B

### `SFX_AMP_VIR_B`

> **在 SF-XCIS 方法中定义用户指定的振幅初始猜测向量。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * 构建一个在第
>     * $n$
>     * 个轨道上带有
>     * $\beta$
>     * 粒子的猜测振幅
>     * （需要 SFX_AMP_OCC_A）。
> * **建议**: 仅在默认猜测不满足要求时使用。

XCIS

### `XCIS`

> **控制是否在 CIS 计算之外额外进行 XCIS 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不进行 XCIS 计算。
>     * TRUE
>     * 进行 XCIS 计算（需要 ROHF 基态）。
> * **建议**: 无

SASF_CIS

### `SASF_CIS`

> **控制是否进行 SA-SF-CIS/DFT 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不进行 SA-SF-CIS/DFT 计算。
>     * TRUE
>     * 进行 SA-SF-CIS/DFT 计算。
> * **建议**: SA-SF 方法需要限制开壳层基态计算。

DFTCIS

### `DFTCIS`

> **控制是否进行 DFT/CIS 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不进行 DFT/CIS 计算。
>     * TRUE
>     * 进行 DFT/CIS 计算。
> * **建议**: 无

DFTCIS_PARAMS

### `DFTCIS_PARAMS`

> **选择 DFT/CIS 的变体**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 执行 CIS
>     * 1
>     * 执行 B3LYP/CIS
>     * 2
>     * 执行 CAM-B3LYP/CIS
> * **建议**: 需要将 DFTCIS 设置为 1 或 2。

## 7.2.4.2 CIS 附加自定义选项

下面提供了用于精细调节 CIS 及相关计算的附加变量。

N_FROZEN_CORE

### `N_FROZEN_CORE`

> **控制被冻结的核心轨道数目。**
>
> * **类型**: `INTEGER/STRING`
> * **默认值**: `0`
> * **选项**:
>     * FC
>     * 冻结核心近似（Frozen core approximation）。
>     * $n$
>     * 冻结
>     * $n$
>     * 个核心轨道。
> * **建议**: 对 CIS 而言，使用冻结核心并没有计算上的优势，且只有在没有轨道被冻结时才提供解析导数。在计算 CIS(D) 校正时该选项很有帮助（参见第 7.8 节）。

**注意：

在关联计算中，默认设置为 N_FROZEN_CORE=FC。
**

N_FROZEN_VIRTUAL

### `N_FROZEN_VIRTUAL`

> **控制被冻结的虚轨道数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * 冻结
>     * $n$
>     * 个虚轨道。
> * **建议**: 对 CIS 而言，使用冻结虚轨道并没有计算上的优势，且只有在没有轨道被冻结时才提供解析导数。

MAX_CIS_CYCLES

### `MAX_CIS_CYCLES`

> **允许的最大 CIS 迭代循环次数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `30`
> * **选项**:
>     * $n$
>     * 用户自定义的循环次数。
> * **建议**: 默认值通常已经足够。

MAX_CIS_SUBSPACE

### `MAX_CIS_SUBSPACE`

> **CIS 迭代中允许的最大子空间向量数目**
>
> * **类型**: `INTEGER`
> * **默认值**: `以收敛所有根所需的数目为准`
> * **选项**:
>     * $n$
>     * 用户自定义的子空间向量数目
> * **建议**: 默认值通常是合适的，除非为大分子请求大量激发态。存储子空间向量所需的总内存上界为 $2nOV$ ，其中 $O$ 和 $V$ 分别表示占据轨道和虚轨道的数目。可以减少 $n$ 以节省内存，代价是更多的 CIS 迭代次数。如果 $n$ 不比 CIS_N_ROOTS 大很多，收敛可能会受到影响。

CIS_CONVERGENCE

### `CIS_CONVERGENCE`

> **当误差小于 $10^{-\mathrm{CIS\_CONVERGENCE}}$ 时，认为 CIS 已收敛**
>
> * **类型**: `INTEGER`
> * **默认值**: `6`
> * **选项**:
>     * $n$
>     * 对应于
>     * $10^{-n}$
> * **建议**: 该变量同时控制 CPSCF 方程的收敛。

CIS_DYNAMIC_MEM

### `CIS_DYNAMIC_MEM`

> **控制 CIS 和 TDDFT 计算中使用静态内存还是动态内存。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 部分使用静态内存
>     * TRUE
>     * 完全使用动态内存
> * **建议**: 默认控制方式需要足够的静态内存（MEM_STATIC），以存放一个在每次 CIS 迭代中以 $2\times OV\times N_{\text{roots}}$ 规模增长的数组，其中 $N_{\text{roots}}$ 为未收敛根的数目（$\leq$ CIS_N_ROOTS）。对于大规模计算，必须为 MEM_STATIC 指定很大的值，这并不推荐（参见第 2 章）。因此，推荐对大规模计算使用动态内存。

CIS_RELAXED_DENSITY

### `CIS_RELAXED_DENSITY`

> **在附着/脱离密度分析（attachment/detachment density analysis）以及第 10.2.12 节所述的一般激发态分析中使用弛豫 CIS 密度（relaxed CIS density）。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 分析中不使用弛豫 CIS 密度。
>     * TRUE
>     * 分析中使用弛豫 CIS 密度。
> * **建议**: 无

CIS_GUESS_DISK

### `CIS_GUESS_DISK`

> **从磁盘读取 CIS 初始猜测（来自之前的计算）。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 生成新的猜测。
>     * TRUE
>     * 从磁盘读取猜测。
> * **建议**: 需要来自之前计算的猜测。

CIS_GUESS_DISK_TYPE

### `CIS_GUESS_DISK_TYPE`

> **确定从磁盘读取的猜测类型**
>
> * **类型**: `INTEGER`
> * **默认值**: `Nil`
> * **选项**:
>     * 0
>     * 仅读取三重态
>     * 1
>     * 读取三重态和单重态
>     * 2
>     * 仅读取单重态
> * **建议**: 若 CIS_GUESS_DISK 为 TRUE，则必须指定该选项。

STS_MOM

### `STS_MOM`

> **控制在 CIS 和 TDDFT 计算（包括自旋翻转变体）中计算态与态之间的跃迁矩。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不计算态间跃迁矩。
>     * TRUE
>     * 计算态间跃迁矩。
> * **建议**: 设置为 true 时，请求计算所有激发态两两之间以及各激发态与基态之间的态间偶极跃迁矩。该选项不适用于限制开壳层波函数。

CIS_MOMENTS

### `CIS_MOMENTS`

> **控制激发态（CIS 或 TDDFT）多极矩的计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不计算激发态矩。
>     * TRUE
>     * 为每个激发态计算多极矩。
> * **建议**: 若需要激发态矩，请设置为 TRUE（这是一项附加的、计算量很小的任务）。MULTIPOLE_ORDER 控制打印多少阶多极矩。该选项不适用于自旋翻转方法。
