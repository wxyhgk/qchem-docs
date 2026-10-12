---
title: "7.9.15 EOM-CC 计算中的单精度算术"
---

## 7.9.15 EOM-CC 计算中的单精度算术

（2026 年 7 月 4 日）

与第 [6.18](../ch06_correlation/sec_SP_CC.md) 节中所描述的基态 CCSD 计算类似，
单精度也可用于 EOM-CC、EOM-MP2 以及 EOM-CC2 计算。[[1102]](../bib_references/bib.md#bib1149)

目前支持以下 EOM 变体：EE、SF、IP、EA、DIP、DEA；
标准实现与 RI/CD 实现均支持，可用于能量、梯度及性质计算。
如果您希望使用单精度版本的 EOM，请先阅读第 [6.18](../ch06_correlation/sec_SP_CC.md) 节，了解
单精度耦合簇计算的基本设置。
此处仅描述 EOM 特有的附加关键字。

精度的选择由
EOM_SINGLE_PREC 关键字控制：
$0$ 对应双精度计算，$1$ 对应单精度计算。
EOM 特有的收敛判据所使用的关键字与双精度计算相同，但同样适用适用于 CCSD 的规则：过于严格的阈值可能
导致收敛问题。默认的 Davidson 阈值 $10^{-5}$ 在大多数情况下都能很好地工作。[[1102]](../bib_references/bib.md#bib1149)

关键字 CC_SP_DM 以与 CCSD 相同的方式控制 EOM 计算中中间量、密度矩阵以及 $\hat{S}^{2}$ 的计算，
相关说明详见第 [6.18](../ch06_correlation/sec_SP_CC.md) 节。

解析梯度的计算需要求解振幅响应方程，
这些方程同样可以用单精度求解；只需将
EOM_ARESP_SINGLE_PREC = 1 即可启用该功能。
若要在双光子吸收（2PA）计算中用单精度求解响应方程，请使用
CC_EOM_2PA_SINGLE_PREC 关键字（另见第 [7.9.21.6](sec_EOMGRAD.md#sec:2PA) 节）。

### `EOM_SINGLE_PREC`

> **EOM-CC/MP2 计算的精度选择。仅在 CCMAN2 中可用。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * `1`: 单精度计算
>     * `2`: 在单精度计算之后执行双精度的清理（clean-up）迭代
> * **建议**: 使用单精度时请勿设置过于严格的收敛判据

### `CC_EOM_2PA_SINGLE_PREC`

> **2PA 响应方程的精度选择。仅在 CCMAN2 中可用。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * `1`: 单精度计算
> * **建议**: 无

**注意：

使用单精度时，请记得调整收敛阈值。
**

???+ example "示例 7.92：采用单精度执行并结合 CD 计算甲醛阴离子的 EOM-EA-CCSD 能量"
    ```qchem
    $comment
       Formaldehyde anion, single-precision calculation
    $end
    
    $molecule
       0 1
       C
       H  1  1.127888
       H  1  1.127888  2  100.546614
    $end
    
    $rem
       BASIS                 = cc-pvdz
       METHOD                = ccsd
       CHOLESKY_TOL          = 3
       EA_STATES             = [1,0,0,0]
       CC_REF_PROP           = 1   Compute properties of the CCSD reference
       !SP keywords
       CC_SINGLE_PREC        = 1
       CC_SP_T_CONV          = 4
       CC_SP_E_CONV          = 6
       CC_ERASE_DP_INTEGRALS = 0 ! set 1 to save disk space
       CC_SP_DM              = 1
       !EOM-specific keyword
       EOM_SINGLE_PREC       = 1
    $end
    ```

???+ example "示例 7.93：在单精度设置下对尿嘧啶-水复合物的三重激发态进行几何结构优化"
    ```qchem
    $molecule
       0 1
       N     0.034130    -.986909    0.000000
       N    -1.173397     .981920    0.000000
       C    -1.218805    -.408164    0.000000
       C    -0.007302    1.702153    0.000000
       C     1.196200    1.107045    0.000000
       C     1.289085    -.345905    0.000000
       O     2.310232    -.996874    0.000000
       O    -2.257041   -1.026495    0.000000
       H     0.049329   -1.997961    0.000000
       H    -2.070598    1.437050    0.000000
       H    -0.125651    2.776484    0.000000
       H     2.111671    1.674079    0.000000
       O     1.747914   -1.338382   -3.040233
       H     2.180817   -1.817552   -2.333676
       H     0.813180   -1.472188   -2.883392
    $end
    
    $rem
       JOB_TYPE              = opt
       METHOD                = ccsd
       BASIS                 = cc-pvdz
       CC_STATE_TO_OPT       = [1,1]
       MEM_TOTAL             = 30000
       EE_TRIPLETS           = [1]
       CC_SP_T_CONV          = 4
       CC_SP_E_CONV          = 6
       CC_SINGLE_PREC        = 1
       EOM_SINGLE_PREC       = 1
       CC_SP_DM              = 1
       CC_EOM_PROP           = 1
       EOM_ARESP_SINGLE_PREC = 1
    $end
    
    ```
