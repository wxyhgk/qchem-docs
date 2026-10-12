---
title: "7.7.10 Δ SCF 驱动"
---

## 7.7.10 $\Delta$SCF 驱动

(July 4, 2026)

*$delta_scf* 输入部分可用于更便捷地控制 $\Delta$SCF 单重态、双重态和三重态激发态计算。该部分通过在 *$rem* 输入部分中设置 DELTA_SCF = TRUE 来启用。示例 7.7.10 给出了一个使用默认设置的基本作业。

### `DELTA_SCF`

> **触发一次 $\Delta$ SCF 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `FALSE`: 不执行 $\Delta$ SCF 计算。
>     * `TRUE`: 执行 $\Delta$ SCF 计算。
> * **建议**: 若希望进行 $\Delta$ SCF 计算,请设置为 TRUE。

???+ example "示例 7.61: 默认情况下,针对与 HOMO $\to$ LUMO 跃迁相关的单重态、双重态(阳离子)和三重态,均执行受限开壳层 SCF 计算。"
    ```qchem
    $comment
      Basic DeltaSCF calculation on formamide.
      HOMO (n) -> LUMO (pi*) transition.
    $end
    
    $molecule
      0   1
      C   0.00096902 0.00000000  0.41970774
      O   1.20026422 0.00000000  0.23240832
      N  -0.93604020 0.00000000 -0.56208780
      H  -0.44521491 0.00000000  1.42281135
      H  -0.64165047 0.00000000 -1.52189668
      H  -1.91364957 0.00000000 -0.34413077
    $end
    
    $rem
      METHOD     wB97X-D
      BASIS      STO-3G
      DELTA_SCF  TRUE
    $end
    ```

一旦在 *$rem* 部分中将 DELTA_SCF 设置为 TRUE,即可在 *$delta_scf* 输入部分使用下文即将介绍的关键字。通过关键字 **SOMO_1** 和 **SOMO_2**(对应单占据分子轨道, singly-occupied molecular orbitals)分别指定想要从中激发的轨道(空穴态)以及激发进入的轨道(粒子态)。通过将 **doublet** 或 **triplet** 设置为 **restricted** 或 **unrestricted**,可以用 ROSCF 或 USCF 计算双重态(阳离子, $m_{s}=1/2$)或三重态($m_{s}=1$)态。将 **singlet** 设置为 **unrestricted** 可请求非受限的自旋对称性破缺态($m_{s}=0$,参见第 [7.7.3](sect_OpSing.md) 节),而将 **singlet** 设置为 **restricted** 则触发自旋纯的 ROKS 计算(第 [7.7.4](ex_ESROKS.md) 节)。
如果在请求自旋对称性破缺态之外还请求了三重态(受限或非受限),程序将使用近似自旋投影方法计算自旋纯单重态的近似能量,详见第 [7.7.3](sect_OpSing.md) 节。[[1511]](../bib_references/bib.md#bib1574)

### `Singlet`

> **执行自旋对称性破缺或受限开壳层的单重态计算。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `Restricted`
> * **可选值**:
>     * `Restricted`: 执行受限开壳层单重态(ROKS) SCF 计算。
>     * `Unrestricted`: 执行非受限的自旋对称性破缺 SCF 计算。
> * **建议**: 请查阅相关文献。

### `Doublet`

> **执行 $m_{s}=1/2$ 的双重态计算(相对于闭壳层参考的阳离子)。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `Restricted`
> * **可选值**:
>     * `Restricted`: 执行受限开壳层双重态 SCF 计算。
>     * `Unrestricted`: 执行非受限双重态 SCF 计算。
> * **建议**: 尽可能使用受限方式。

### `Triplet`

> **执行 $m_{s}=1$ 的三重态计算。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `Restricted`
> * **可选值**:
>     * `Restricted`: 执行受限开壳层三重态 SCF 计算。
>     * `Unrestricted`: 执行非受限三重态 SCF 计算。
> * **建议**: 尽可能使用受限方式。

### `SOMO_1`

> **指定激发所源自的占据轨道。输入部分: $delta_scf**
>
> * **类型**: `INTEGER`
> * **默认值**: `HOMO`
> * **可选值**:
>     * $0<n<$: LUMO 任意整数 $n\in$ [1, HOMO] 均允许
> * **建议**: 根据此前对基态轨道的检查以及所要瞄准的目标态,选择期望的激发源轨道。

### `SOMO_2`

> **指定激发进入的虚轨道。输入部分: $delta_scf**
>
> * **类型**: `INTEGER`
> * **默认值**: `LUMO`
> * **可选值**:
>     * `HOMO`: $<n$ 大于或等于 LUMO 的任意整数。
> * **建议**: 根据此前对基态轨道的检查以及所要瞄准的目标态,选择期望的激发目标轨道。

???+ example "示例 7.62: 一次非受限三重态与自旋对称性破缺 SCF 计算。所期望的核心激发通过 SOMO_1 和 SOMO_2 关键字来瞄准"
    ```qchem
    $comment
      DeltaSCF calculation on the 1s -> 3s (LUMO + 3) core excited state of Ne.
    $end
    
    $molecule
      0  1
      Ne
    $end
    
    $rem
      METHOD            SCAN
      BASIS             cc-pCVDZ
      INTEGRAL_SYMMETRY FALSE
      DELTA_SCF         TRUE
    $end
    
    $delta_scf
      SOMO_1   1
      SOMO_2   9
      singlet  unrestricted
      triplet  unrestricted
    $end
    ```

???+ example "示例 7.63: 一次受限开壳层单重态 SCF 计算。注意,当仅设置 singlet 或 triplet 时,只会执行所请求的计算(与默认同时执行两者不同)。这里再次使用 SOMO_1 和 SOMO_2 来瞄准氟化氢的特定核心激发态 ( $1s\to 3s$ )。请将此例与示例 7.7.5 对比"
    ```qchem
    $comment
      DeltaSCF calculation on the 1s -> 3s (LUMO + 1) core excited
      state of HF. Only a restricted open-shell singlet calculation
      is requested.
    $end
    
    $molecule
      0  1
      F       0.0000  0.0000  0.0000
      H       0.0000  0.0000  0.9168
    $end
    
    $rem
      METHOD            SCAN
      BASIS             aug-cc-pCVTZ
      INTEGRAL_SYMMETRY FALSE
      DELTA_SCF         TRUE
    $end
    
    $delta_scf
      SOMO_1                1
      SOMO_2                7
      singlet               restricted
      singlet_SCF_algorithm SGM
      singlet_SGM_gradient  50
      singlet_SOMO_mixing   false
    $end
    ```

程序会自动测量三个有用的量:

- 作为初猜的基态 SOMO、单重态(或混合态)SOMO 以及三重态 SOMO 之间的重叠;这可作为一种度量,以确保 $\Delta$SCF 轨道优化确实收敛到期望的激发态。
- 基态与单重态激发态之间的跃迁偶极矩。
- 闭壳层基态与单重态激发态行列式之间的非正交重叠(参见第 [7.7.4](ex_ESROKS.md) 节关于 ROKS 计算中 SOMO 混合的内容)。

当初猜的 SOMO 重叠较差(显著小于 1)时, $\Delta$SCF 计算很可能收敛到与初猜性质不同的解。有两个 SCF 参数可以修改以帮助计算收敛到期望的解: 初猜(初始猜测)与 SCF 算法。除了标准初猜(收敛的闭壳层分子轨道, MO)之外,双重态阳离子 MO 也可用作单重态或三重态计算的初猜。这些初猜有时更容易收敛,并能为 SCF 过程提供更好的起点。对于单重态计算,三重态轨道本身也可作为初猜。最后,TDDFT 计算(第 [7.13.3](sect_NTOs.md) 节)的自然跃迁轨道(natural transition orbitals, NTO)也可以用作初猜。注意在这种情况下,必须先在前一个(顺序执行的)输入中进行一次 TDDFT 计算以保存振幅,并设置 MAX_SCF_CYCLES 为 0 且 GEN_SCFMAN 为 TRUE,从而保持正则轨道不变并将其正确变换到 NTO 基中。变量 **TDDFT_state_guess** 控制使用哪个 TDDFT 态作为初猜。

### `Singlet_SCF_Guess`

> **指定单重态(或对称性破缺)SCF 计算所使用的初猜。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `closed_shell`
> * **可选值**:
>     * closed_shell, doublet, triplet, tddft_nto
> * **建议**: 对于某些存在显著轨道弛豫的激发,例如核心激发,双重态核心电离态可能更容易收敛,并可作为有用的起点。

### `Doublet_SCF_Guess`

> **指定双重态计算所使用的初猜。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `closed_shell`
> * **可选值**:
>     * `closed_shell, tddft_nto`
> * **建议**: 对于 TDDFT NTO 初猜,正则 MO 会被旋转至 NTO 基,并从空穴能级移去一个电子。

### `Triplet_SCF_Guess`

> **指定三重态 SCF 计算所使用的初猜。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `closed_shell`
> * **可选值**:
>     * closed_shell, doublet, tddft_nto
> * **建议**: 对于某些存在显著轨道弛豫的激发,例如核心激发,双重态核心电离态可能更容易收敛,并可作为有用的起点。

### `TDDFT_state_guess`

> **指定用作初猜的 TDDFT 态。输入部分: $delta_scf**
>
> * **类型**: `INT`
> * **默认值**: `1, if the TDDFT NTOs were requested as the guess for any calculation`
> * **可选值**:
>     * $n>0$: 大于 1 的任意整数
> * **建议**: 根据你感兴趣的目标 TDDFT 态进行选择。

除初猜之外,所采用的 SCF 算法对于高效收敛到期望的 SCF 解也至关重要。$\Delta$SCF 驱动会根据所需的目标态设置合理的默认值: 若寻求 HOMO $\rightarrow{}$ LUMO 跃迁则使用 GDM(第 [4.5.7](../ch04_scf/sect_gdm.md) 节),若请求更高激发态则使用 MOM(第 [7.7.2](ex_OpSing.md) 节)算法。然而在某些情况下,GDM 对于收敛更高激发态可能非常有用(这些态因对称性而避免了变分坍缩);反之,如果 HOMO $\rightarrow{}$ LUMO 跃迁并非最低激发态,GDM 可能会坍缩到不同的解。此外,MOM 算法也可能无法收敛。请查阅关于不同 SCF 算法在激发态计算中优缺点的文献,并从 **Q-Chem** 提供的众多求解器中进行选择(第 [4.5](../ch04_scf/sect_convergence.md)、[7.7.2](ex_OpSing.md)、[7.7.5](ex_BEDSCF.md) 和 [7.7.8](ex_ROSTEP.md) 节)。

### `Singlet_SCF_Algorithm`

> **指定用于收敛单重态(或对称性破缺)SCF 计算的算法。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `GDM if`
> * **可选值**:
>     * DIIS, GDM, GDM_LS, MOM, IMOM, STEP, STEP_MOM, SGM, SGM_LS
> * **建议**: DIIS、GDM 和 GDM_LS 适用于 HOMO $\rightarrow$ LUMO 跃迁。若需要更高激发态,请使用 MOM、STEP、SGM 或其某种变体。当使用 ROKS 且与基态的重叠较大时,尝试使用 GDM 或 SGM 并结合设置 Singlet_SOMO_Mixing = false 。

### `Doublet_SCF_Algorithm`

> **指定用于收敛双重态 SCF 计算的算法。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `GDM if`
> * **可选值**:
>     * DIIS, GDM, GDM_LS, MOM, IMOM, STEP, STEP_MOM, SGM, SGM_LS
> * **建议**: DIIS、GDM 和 GDM_LS 适用于 HOMO 电离。若需要从更深的轨道电离,请使用 MOM、STEP、SGM 或其某种变体。

### `Triplet_SCF_Algorithm`

> **指定用于收敛三重态 SCF 计算的算法。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `GDM if`
> * **可选值**:
>     * DIIS, GDM, GDM_LS, MOM, IMOM, STEP, STEP_MOM, SGM, SGM_LS
> * **建议**: DIIS、GDM 和 GDM_LS 适用于 HOMO $\to$ LUMO 跃迁。若需要更高激发态,请使用 MOM、STEP、SGM 或其某种变体。

当然,收敛阈值也可以调整。$\Delta$SCF 驱动会根据 SCF 求解器的性质设置实用的阈值。

### `Singet_SCF_Convergence`

> **指定单重态(或对称性破缺)SCF 计算的能量收敛阈值。输入部分: $delta_scf**
>
> * **类型**: `INTEGER`
> * **默认值**: `5 if`
> * **可选值**:
>     * $n$: 任意正整数。
> * **建议**: 遵循默认值。

### `Doublet_SCF_Convergence`

> **指定双重态 SCF 计算的能量收敛阈值。输入部分: $delta_scf**
>
> * **类型**: `INTEGER`
> * **默认值**: `5 if`
> * **可选值**:
>     * $n$: 任意正整数。
> * **建议**: 遵循默认值。

### `Triplet_SCF_Convergence`

> **指定三重态 SCF 计算的能量收敛阈值。输入部分: $delta_scf**
>
> * **类型**: `INTEGER`
> * **默认值**: `5 if`
> * **可选值**:
>     * $n$: 任意正整数。
> * **建议**: 遵循默认值。

当采用 SGM 作为 SCF 求解器时,可以调整轨道梯度(平方项)的比例因子。

### `Singlet_SGM_Gradient`

> **仅当 Singlet_SCF_Algorithm 设置为 SGM 时相关。参见第 7.7.5 节中的 DELTA_GRADIENT_SCALE。输入部分: $delta_scf**
>
> * **类型**: `INTEGER`
> * **默认值**: `75`
> * **可选值**:
>     * $n$: 任意整数 $n\in[1,100]$。
> * **建议**: 参见关于 DELTA_GRADIENT_SCALE 的文档。

### `Doublet_SGM_Gradient`

> **仅当 Doublet_SCF_Algorithm 设置为 SGM 时相关。参见第 7.7.5 节中的 DELTA_GRADIENT_SCALE。输入部分: $delta_scf**
>
> * **类型**: `INTEGER`
> * **默认值**: `75`
> * **可选值**:
>     * $n$: 介于以下范围内的任意整数 $[1,100]$。
> * **建议**: 参见关于 DELTA_GRADIENT_SCALE 的文档。

### `Triplet_SGM_Gradient`

> **仅当 Triplet_SCF_Algorithm 设置为 SGM 时相关。参见第 7.7.5 节中的 DELTA_GRADIENT_SCALE。输入部分: $delta_scf**
>
> * **类型**: `INTEGER`
> * **默认值**: `75`
> * **可选值**:
>     * $n$: 介于以下范围内的任意整数 $[1,100]$。
> * **建议**: 参见关于 DELTA_GRADIENT_SCALE 的文档。

仅针对单重态的 ROKS 计算,SOMO 之间的混合可以被允许或被抑制。

### `Singlet_SOMO_Mixing`

> **仅当 singlet 设置为 true 时相关。参见第 7.7.4 节中的 ROKS_SS_MIXING。输入部分: $delta_scf**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `FALSE`: 抑制 SOMO 之间的混合。
>     * `TRUE`: 允许 SOMO 之间的混合。
> * **建议**: 参见关于 ROKS_SS_MIXING 的文档。

$\Delta$SCF 驱动允许你生成 SOMO 的 cube 图;这对于目视检查所找到的 SCF 解的性质($n\to\pi^{\ast}$、$\pi\to$ 里德堡(Rydberg)、$1s\to\sigma^{\ast}$ 等)至关重要,并且除输出中打印的 SOMO 轨道重叠之外,还能帮助你确认 SCF 计算是否正在收敛到你所寻求的态。

### `Singlet_SOMO_Print`

> **绘制单重态(或自旋对称性破缺)态的 SOMO。请确保在输入文件中激活 $plots 部分。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `Both`
> * **可选值**:
>     * `Alpha`: 绘制 alpha 轨道的 SOMO
>     * `Beta`: 绘制 beta 轨道的 SOMO
>     * `Both`: 绘制 alpha 和 beta 两者轨道的 SOMO
> * **建议**: 当对 SCF 解存有疑虑时,检查这些轨道。

### `Doublet_SOMO_Print`

> **绘制双重态的 SOMO。请确保在输入文件中激活 $plots 部分。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `Both`
> * **可选值**:
>     * Alpha 绘制 alpha 轨道的 SOMO: Beta 绘制 beta 轨道的 SOMO Both 绘制 alpha 和 beta 两者轨道的 SOMO
> * **建议**: 当对 SCF 解存有疑虑时,检查这些轨道。

### `Triplet_SOMO_Print`

> **绘制三重态的 SOMO。请确保在输入文件中激活 $plots 部分。输入部分: $delta_scf**
>
> * **类型**: `STRING`
> * **默认值**: `Both`
> * **可选值**:
>     * Alpha 绘制 alpha 轨道的 SOMO: Beta 绘制 beta 轨道的 SOMO Both 绘制 alpha 和 beta 两者轨道的 SOMO
> * **建议**: 当对 SCF 解存有疑虑时,检查这些轨道。

最后,在描述高度对称分子(*e.g.*, 乙烯、N${}_{2}$ 或苯)的核心激发时,由于核心轨道离域在整个分子上,需要用 $\Delta$SCF 定域化核心轨道以获得准确的激发能。[[168]](../bib_references/bib.md#bib162)

这可以通过以下关键字实现:

### `Localize`

> **使用 Boys 方法定域化给定数目的轨道(参见第 10.3.2 节)。输入部分: $delta_scf**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **可选值**:
>     * $n>1$: 任意整数 $n\in[2,N_{\text{occ}}]$
> * **建议**: 将该变量设置为要定域化的核心轨道总数(例如,在 N ${}_{2}$ 中为 2,在苯中为 6)。

### `Localize_Offset`

> **设置开始选取定域化轨道数目的偏移量,轨道数目由 localize 变量指定。输入部分: $delta_scf**
>
> * **类型**: `INTEGER`
> * **默认值**: `$\text{HOMO}-n$`
> * **可选值**:
>     * $x$: 任意整数 $x\in[1,\text{HOMO}-n]$
> * **建议**: 考虑能量低于你所关心轨道的那些原子的轨道数目,并将该变量设置为该数目。例如,当试图达到 CS ${}_{2}$ 的碳 K 边时,由于存在两个硫的 1s 轨道,设置 $x=2$。

如果在尝试了不同的 SCF 初猜和算法之后,依据打印的重叠以及目视检查仍无法收敛到期望的解,建议你改用本节前述的标准输入方式(即使用顺序输入以及 *$reorder_mo* 或 *$occupied* 部分)来进行计算,以便对 SCF 过程实现更精细的控制。
