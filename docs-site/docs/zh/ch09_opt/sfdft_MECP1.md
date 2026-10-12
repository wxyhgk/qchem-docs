---
title: "9.8.4 作业控制与示例"
---

## 9.8.4 作业控制与示例

(July 4, 2026)

进行 MECP（最小能量交叉点，Minimum Energy Crossing Point）优化时，在 *$rem* 区段中设置 MECP_OPT = TRUE，并注意本例中不需要第 [9.8.2](subsec_deriv-couple-jobcontrol.md) 节讨论的 *$derivative_coupling* 输入区段。

### `MECP_OPT`

> **决定是否进行 MECP 优化。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `TRUE`: 进行 MECP 优化。
>     * `FALSE`: 不进行 MECP 优化。
> * **建议**: 无。

### `MECP_METHODS`

> **决定使用哪种方法。**
>
> * **类型**: `STRING`
> * **默认值**: `BRANCHING_PLANE`
> * **选项**:
>     * `BRANCHING_PLANE`: 使用分支平面（branching-plane）更新方法。
>     * `MECP_DIRECT`: 使用直接法（direct method）。
>     * `PENALTY_FUNCTION`: 使用罚约束（penalty-constrained）方法。
> * **建议**: 直接法对于小分子或高对称性分子是稳定的。分支平面更新方法对于较大分子更高效，但如果两个态具有不同的对称性则无法使用。若使用分支平面更新方法，必须在 $rem 区段中将 GEOM_OPT_COORDS 设置为 0，因为该算法仅在笛卡尔坐标下可用。罚约束方法收敛缓慢，仅建议在其他方法失败时使用。

### `MECP_STATE1`

> **为 MECP 优化设置第一个 Born-Oppenheimer 态。**
>
> * **类型**: `INTEGER/INTEGER ARRAY`
> * **默认值**: `None`
> * **选项**:
>     * `[`: $i$ , $j$ ] 查找总自旋为 $i$ 的第 $j$ 个激发态； $j=0$ 表示 SCF 基态。
> * **建议**: 在受限（restricted）计算中 $i$ 被忽略；在非受限（unrestricted）计算中，$i$ 只能取 0 或 1。

### `MECP_STATE2`

> **为 MECP 优化设置第二个 Born-Oppenheimer 态。**
>
> * **类型**: `INTEGER/INTEGER ARRAY`
> * **默认值**: `None`
> * **选项**:
>     * `[`: $i$ , $j$ ] 查找总自旋为 $i$ 的第 $j$ 个激发态； $j=0$ 表示 SCF 基态。
> * **建议**: 在受限（restricted）计算中 $i$ 被忽略；在非受限（unrestricted）计算中，$i$ 只能取 0 或 1。

### `CIS_S2_THRESH`

> **决定在非受限计算中某个态是单重态还是三重态。**
>
> * **类型**: `INTEGER`
> * **默认值**: `120`
> * **选项**:
>     * $n$: 将 $\langle\hat{S}^{2}\rangle$ 阈值设置为 $n/100$
> * **建议**: 在默认情况下，$\langle\hat{S}^{2}\rangle>1.2$ 的态被视为三重态，其余态被视为单重态。

### `MECP_PROJ_HESS`

> **决定在使用分支平面更新方法时，是否从 Hessian 中投影掉耦合矢量。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **选项**:
>     * `TRUE`
>     * `FALSE`
> * **建议**: 使用默认值。

???+ example "示例 9.29: 使用直接法在 SOS-CIS(D0) 级别下对 NO ${}_{2}^{-}$ 的 S ${}_{2}$ 与 S ${}_{3}$ 态之间的交叉点进行 MECP 优化。"
    ```qchem
    $molecule
       -1 1
       N1
       O2  N1  RNO
       O3  N1  RNO  O2  AONO
    
       RNO  = 1.50
       AONO = 100
    $end
    
    $rem
       JOBTYPE         = opt
       METHOD          = soscis(d0)
       BASIS           = aug-cc-pVDZ
       AUX_BASIS       = rimp2-aug-cc-pVDZ
       PURECART        = 1111
       CIS_N_ROOTS     = 4
       CIS_TRIPLETS    = false
       CIS_SINGLETS    = true
       MEM_STATIC      = 900
       MEM_TOTAL       = 1950
       MECP_OPT        = true
       MECP_STATE1     = [0,2]
       MECP_STATE2     = [0,3]
       MECP_METHODS    = mecp_direct
    $end
    ```

???+ example "示例 9.29: 使用分支平面更新方法在 SF-TDDFT 级别下优化 S ${}_{0}$ 与 S ${}_{1}$ 之间的亚乙基（ethylidene）MECP。"
    ```qchem
    $molecule
       0 3
       C   0.044626  -0.2419240   0.357157
       C   0.008905   0.6727548   1.460500
       H   0.928425  -0.1459163  -0.272095
       H  -0.831032  -0.1926895  -0.288529
       H  -0.009238   0.9611331   2.479936
       H   0.068314  -1.2533580   0.778847
    $end
    
    $rem
       JOBTYPE           opt
       METHOD            bhhlyp
       BASIS             6-31G(d,p)
       MECP_OPT          true
       MECP_METHODS      branching_plane
       MECP_PROJ_HESS    true  ! project out y vector from the hessian
       GEOM_OPT_COORDS   0     ! currently only works for Cartesian coordinate
       GEOM_OPT_DRIVER   optimize
       SPIN_FLIP         true
       UNRESTRICTED      true
       CIS_N_ROOTS       4
       MECP_STATE1       [0,1]
       MECP_STATE2       [0,2]
       CIS_S2_THRESH     120
    $end
    ```

???+ example "示例 9.31: 使用罚约束更新方法在 SF-TDDFT 级别下优化 S ${}_{0}$ 与 S ${}_{1}$ 之间的扭曲-金字塔化（twisted-pyramidalized）乙烯 MECP。"
    ```qchem
    $molecule
       0 3
       C  -0.015889   0.073532  -0.059559
       C   0.012427  -0.002468   1.315694
       H   0.857876   0.147014  -0.710529
       H  -0.936470  -0.011696  -0.626761
       H   0.764557   0.663381   1.762573
       H   0.740773  -0.869764   1.328583
    $end
    
    $rem
       JOBTYPE         opt
       MECP_OPT        true
       MECP_METHODS    penalty_function
       METHOD          bhhlyp
       SPIN_FLIP       true
       UNRESTRICTED    true
       BASIS           6-31G(d,p)
       CIS_N_ROOTS     4
       MECP_STATE1     [0,1]
       MECP_STATE2     [0,2]
       CIS_S2_THRESH   120
       GEOM_OPT_DRIVER optimize
    $end
    ```

???+ example "示例 9.32: 使用直接法在 EOM-EE-CCSD 级别下优化 N ${}_{3}^{+}$ 的 $\tilde{B}^{1}A_{2}$ 与 $\tilde{A}^{1}B_{2}$ 态。关于使用耦合簇方法进行 MECP 优化的具体细节，请参见第 7.9.28 节。"
    ```qchem
    $molecule
       1 1
       N1
       N2 N1 rNN
       N3 N2 rNN N1 aNNN
    
       rNN  =  1.54
       aNNN = 50.0
    $end
    
    $rem
       JOBTYPE                opt
       MECP_OPT               true
       MECP_METHODS           mecp_direct
       METHOD                 eom-ccsd
       BASIS                  6-31g
       EE_SINGLETS            [0,2,0,2]
       XOPT_STATE_1           [0,2,2]
       XOPT_STATE_2           [0,4,1]
       CCMAN2                 false
       GEOM_OPT_TOL_GRADIENT  30
       GEOM_OPT_DRIVER        optimize
    $end
    ```

???+ example "示例 9.33: 使用解析导数耦合在 SF-TDDFT 级别下优化 S ${}_{0}$ 与 S ${}_{1}$ 之间的亚乙基（ethylidene）MECP。"
    ```qchem
    $molecule
       0 3
       C   0.044626  -0.241924   0.357157
       C   0.008905   0.672754   1.460500
       H   0.928425  -0.145916  -0.272095
       H  -0.831032  -0.192689  -0.288529
       H  -0.009238   0.961133   2.479936
       H   0.068314  -1.253358   0.778847
    $end
    
    $rem
       JOBTYPE            opt
       MECP_OPT           true
       MECP_METHODS       branching_plane
       MECP_PROJ_HESS     true
       GEOM_OPT_COORDS    0
       MECP_STATE1        [0,1]
       MECP_STATE2        [0,2]
       UNRESTRICTED       true
       SPIN_FLIP          true
       CIS_N_ROOTS        4
       CALC_NAC           true
       CIS_DER_NUMSTATE   2
       MAX_CIS_CYCLES     50
       EXCHANGE           bhhlyp
       BASIS              6-31G(d,p)
       INTEGRAL_SYMMETRY  true
    $end
    ```
