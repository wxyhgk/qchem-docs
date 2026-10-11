---
title: "4.5.5 能级偏移（Level-Shifting）"
---

## 4.5.5 能级偏移（Level-Shifting）

(July 4, 2026)

能级偏移（level-shifting）是一种历史悠久的技术，可帮助 HOMO/LUMO 间隙较小的体系实现自洽场（SCF）收敛[[578]](../bib_references/bib.md#bib599)。
当间隙较小时，简单的 Fock 矩阵对角化（Roothaan 步骤）可能会改变分子轨道的能量排序，导致按照构造原理（*aufbau* principle）重新填充电子后，整体效果表现为电子组态的不连续切换，从而使 SCF 过程无法收敛。为了解决这种不稳定的 SCF 行为，可以在对角化之前偏移 Fock 矩阵虚块（virtual block）的对角元素（即"能级偏移"），以增大计算得到的 HOMO/LUMO 间隙。通过适当的能级偏移，分子轨道的能量排序在对角化过程中得以保持，从而在每个 SCF 循环中轨道的形状以连续的方式发生变化，形成稳定的迭代过程。利用微扰理论可以证明，恰当的能级偏移能够保证 Fock 矩阵对角化后总能量降低[[578]](../bib_references/bib.md#bib599)。
但需要注意的是，通过能级偏移获得的 SCF 解未必是稳定的基态。为检验收敛后电子态的稳定性，我们建议使用关键字 STABILITY_ANALYSIS 或 INTERNAL_STABILITY（参见第 [4.3.3](sub_SCF_addOps.md) 节和第 [4.5.17](sub_stability_analysis.md) 节）。

在 DIIS 或其他某些 SCF 算法能够快速收敛的情况下，施加能级偏移通常会减慢收敛速度。此外，经验表明，能级偏移可以将困难的 SCF 案例收敛到中等阈值（如 $10^{-5}$），但当收敛阈值收紧（例如收紧到 $10^{-8}$）时，其效率会下降。为获得高精度收敛的解，应将能级偏移与 DIIS 或其他收敛算法结合使用。对于困难的 SCF 案例，常见的最佳策略是在 SCF 迭代早期启用能级偏移，随后再将其关闭（转而使用 DIIS）。因此，**Q-Chem** 提供了一种将能级偏移与 DIIS 相结合的混合 SCF 算法，通过将 SCF_ALGORITHM = LS_DIIS 即可调用。此外，通过以下 *$rem* 变量，也可以单独使用能级偏移（不与 DIIS 联用）。

LEVEL_SHIFT

### `LEVEL_SHIFT`

> **确定是否在与 DIIS 联用时启用能级偏移。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 应用能级偏移。
>     * FALSE
>     * 不应用能级偏移。
> * **建议**: 如果需要能级偏移来加速 SCF 收敛，则使用 TRUE。

GAP_TOL

### `GAP_TOL`

> **HOMO/LUMO 间隙阈值，用于控制是否偏移 Fock 矩阵虚块的对角元素。如果在某次 SCF 迭代中 HOMO/LUMO 间隙小于该阈值，则对 Fock 矩阵虚块的对角元素进行偏移；否则不施加能级偏移。**
>
> * **类型**: `INTEGER`
> * **默认值**: `300`
> * **选项**:
>     * 用户自定义
> * **建议**: 输入数值必须是 0 到 9999 之间的整数。实际应用的阈值为 /1000 Eh。默认值的设置只是为了让能级偏移计算能够运行，不应视为任何特定问题的最优值。可能需要通过反复试验来寻找最优阈值。较大的值通常会导致在 SCF 收敛过程中更频繁地使用能级偏移。

LSHIFT

### `LSHIFT`

> **对 Fock 矩阵虚块所有对角元素施加的恒定偏移量。**
>
> * **类型**: `INTEGER`
> * **默认值**: `200`
> * **选项**:
>     * 用户自定义
> * **建议**: 输入数值必须是 0 到 9999 之间的整数。实际偏移量等于 /1000 Eh。默认值的设置只是为了让能级偏移计算能够运行，不应视为任何特定问题的最优值。可能需要通过反复试验来寻找最优阈值。较大的偏移量使 SCF 过程更稳定，但同时也会减慢收敛速度，从而需要更多的 SCF 循环。

**注意：

如果显式指定了 GAP_TOL 或 LSHIFT 或两者皆指定，则 LEVEL_SHIFT 会自动设置为 TRUE。
设置 LEVEL_SHIFT = FALSE 会使 GAP_TOL 和 LSHIFT 的任何取值失效。
调用 LS_DIIS 算法同样会使 LEVEL_SHIFT 的任何设置失效。**

MAX_LS_CYCLES

### `MAX_LS_CYCLES`

> **当 SCF_ALGORITHM = LS_DIIS 时，带能级偏移的 DIIS 迭代的最大次数。另见 THRESH_LS_SWITCH。**
>
> * **类型**: `INTEGER`
> * **默认值**: `MAX_SCF_CYCLES`
> * **选项**:
>     * 1
>     * 仅执行单步带能级偏移的 DIIS，其余 DIIS 步骤不施加能级偏移。
>     * $n$
>     * $n$
>     * 在关闭能级偏移之前进行 $n$ 次带能级偏移的 DIIS 迭代。
> * **建议**: 无

THRESH_LS_SWITCH

### `THRESH_LS_SWITCH`

> **当 SCF_ALGORITHM 设置为 LS_DIIS 时，关闭 DIIS 中能级偏移的阈值为 $10^{-\mbox{{\small THRESH\_LS\_SWITCH}}}$。另见 MAX_LS_CYCLES。**
>
> * **类型**: `INTEGER`
> * **默认值**: `4`
> * **选项**:
>     * 用户自定义。
> * **建议**: 无

???+ example "示例 4.9：在铀配合物上使用带能级偏移的 DIIS 进行 RKS 计算的输入。"
    ```qchem
    $molecule
    0 1
      U   -0.7734808   -0.8815596   -0.8853446
      O   -1.3090665   -2.1863261   -2.7399692
      O   -1.6134743    1.0032462   -1.9673881
      O   -0.2537507    0.4215612    0.9749395
      O    0.0643962   -2.7662217    0.1985884
      O   -2.4384926   -1.2003830   -0.1700214
      O    0.8915310   -0.5627363   -1.6006679
      H   -0.5266214   -2.1731728   -3.3131242
      H   -2.5519330    1.0551966   -1.7276040
      H    0.6520521    0.7395638    0.8360306
      H   -0.6807322   -3.1486006    0.6879451
    $end
    
    $rem
       METHOD          = B3LYP
       BASIS           = LANL2DZ
       ECP             = fit-LANL2DZ
       MAX_SCF_CYCLES  = 200
       THRESH          = 10
       LEVEL_SHIFT     = TRUE
       GAP_TOL         = 200
       LSHIFT          = 200
       SCF_CONVERGENCE = 5
    $end
    ```

???+ example "示例 4.10：在钴配合物上使用 LS_DIIS 进行 UKS 计算的输入。"
    ```qchem
    $molecule
       6 2
       O    0.7515076    1.2954050    1.0605230
       O    0.7506760   -1.2982554    1.0594277
       Co   0.0016554   -0.0007951    0.0017848
       O   -1.4949030   -0.0008880    1.0616115
       O    1.4981395   -0.0006773   -1.0578583
       O   -0.7482665   -1.2970503   -1.0566523
       O   -0.7473745    1.2963844   -1.0559284
    $end
    
    $rem
       METHOD             = B3LYP
       BASIS              = 6-31G
       SCF_ALGORITHM      = LS_DIIS
       MAX_SCF_CYCLES     = 200
       GUI                = 2
       GAP_TOL            = 100
       LSHIFT             = 200
       SCF_CONVERGENCE    = 8
       STABILITY_ANALYSIS = TRUE
    $end
    ```
