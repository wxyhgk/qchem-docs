---
title: "4.5.12 用户自定义混合 SCF 算法"
---

## 4.5.12 用户自定义混合 SCF 算法

（2026 年 7 月 4 日）

通常情况下，单一算法无法保证自洽场（SCF）的收敛。同时，某些 SCF 算法（*例如*，ADIIS）可以在 SCF 计算的初始阶段加速收敛，但接近收敛时效率会下降。虽然在 **Q-Chem** 原始的 SCF 实现中已经启用了几种混合算法（DIIS_GDM、RCA_DIIS），但在 GEN_SCFMAN 中，我们寻求更灵活的设置来使用多种 SCF 算法，从而让用户对 SCF 过程拥有更精确的控制。在当前的实现下，基于 GEN_SCFMAN 的一次 SCF 计算中最多可以使用四种不同的算法（通常已经足够），基本的作业控制如下：

### `GEN_SCFMAN_HYBRID_ALGO`

> **在基于 GEN_SCFMAN 的 SCF 计算中使用多种算法。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 使用单一 SCF 算法（由 SCF_ALGORITHM 指定）。
>     * `TRUE`: 使用多种 SCF 算法（由用户指定）。
> * **建议**: 当希望使用一种以上算法时，将其设置为 TRUE。

### `GEN_SCFMAN_ALGO_1`

> **混合算法计算中使用的第一个算法。**
>
> * **类型**: `STRING`
> * **默认值**: `0`
> * **选项**:
>     * 所有可用的: SCF_ALGORITHM 选项，包括 GEN_SCFMAN 新增的选项（第 4.3 节）。
> * **建议**: 无

### `GEN_SCFMAN_ITER_1`

> **分配给第一个算法的最大迭代次数。若用尽，则切换到下一个算法。**
>
> * **类型**: `INTEGER`
> * **默认值**: `50`
> * **选项**:
>     * 用户自定义
> * **建议**: 无

### `GEN_SCFMAN_CONV_1`

> **分配给第一个算法的收敛判据。若达到，则切换到下一个算法。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * `10`: ${}^{-n}$
> * **建议**: 无

**注意：

*$rem* 变量 GEN_SCFMAN_ALGO_X、GEN_SCFMAN_ITER_X、
GEN_SCFMAN_CONV_X（X = 2, 3, 4）的定义和使用方式类似。
**

???+ example "示例 4.16: 使用 ADIIS + DIIS 算法对镉-咪唑配合物进行 B3LYP/3-21G 计算
（示例取自文献 601 Hu X., Yang W. J. Chem. Phys. (2010) , 132 , pp. 054109 . 链接 ）。由于 CORE 初始猜测质量较差，使用单一算法（如 DIIS 或 GDM）无法收敛。"
    ```qchem
    $molecule
       2 1
       Cd     0.000000     0.000000     0.000000
       N      0.000000     0.000000    -2.260001
       N     -0.685444     0.000000    -4.348035
       C      0.676053     0.000000    -4.385069
       C      1.085240     0.000000    -3.091231
       C     -1.044752     0.000000    -3.060220
       H      1.231530     0.000000    -5.300759
       H      2.088641     0.000000    -2.711077
       H     -2.068750     0.000000    -2.726515
       H     -1.313170     0.000000    -5.174718
    $end
    
    $rem
       EXCHANGE                 B3LYP
       BASIS                    3-21g
       UNRESTRICTED             FALSE
       THRESH                   14
       SCF_GUESS                CORE
       GEN_SCFMAN_HYBRID_ALGO   TRUE
       GEN_SCFMAN_ALGO_1        ADIIS
       GEN_SCFMAN_CONV_1        3  ! switch to DIIS when error < 1E-3
       GEN_SCFMAN_ITER_1        50
       GEN_SCFMAN_ALGO_2        DIIS
       GEN_SCFMAN_CONV_2        8
       GEN_SCFMAN_ITER_2        50
       INTEGRAL_SYMMETRY        FALSE
       POINT_GROUP_SYMMETRY     FALSE
    $end
    ```
