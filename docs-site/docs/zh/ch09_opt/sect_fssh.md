---
title: "9.9.7 最少跳跃面跳跃（Fewest-Switches Surface Hopping）"
---

## 9.9.7 最少跳跃面跳跃（Fewest-Switches Surface Hopping, FSSH）

（2026 年 7 月 4 日）

正如第 [9.8](topic_namd.md) 节所讨论的，沿锥形漏斗（conical seam）优化最小能量交叉点（minimum-energy crossing points, MECPs），随后优化将这些 MECPs 与基态和激发态势能面上其他感兴趣的站点连接起来的最小能量路径，可以得到一幅颇具吸引力的一维光化学反应图像，它类似于基态化学中"反应物 $\rightarrow$ 过渡态 $\rightarrow$ 产物"的图像。然而，正如基态反应并不一定*严格*经过过渡态几何一样，激发态反应也未必恰好经过 MECP，核动能的具体情形会导致偏差。对于激发态反应而言，这个问题可以说更为突出，因为多个锥形交叉的存在很容易导致多种可能的反应机理。从头算分子动力学（AIMD）有望提供一种对可用机理进行采样的途径，从而以自动化的方式推断出哪些机理是重要的，但在光化学情形下，必须将其扩展到涉及多个玻恩-奥本海默（Born-Oppenheimer）势能面的反应。

用于非绝热模拟的最广泛使用的基于轨迹的方法是 Tully 的"最少跳跃"面跳跃（fewest-switches surface-hopping, FSSH）算法。[[1379]](../bib_references/bib.md#bib1440)

在该方法中，经典轨迹在单一势能面上演化，但可以在各势能面接近简并的区域发生"跳跃（hops）"到另一个势能面。这些随机跳跃的概率由非绝热耦合的大小决定 [式 ([9.50](subsec_NACMEs_and_CIs.md#eq:hJK))]。进而，对一族轨迹的系综平均可以提供例如光化学反应分支比等信息。

基于 AIMD 代码的 FSSH 算法在 **Q-Chem** 中可用于任何具备解析导数耦合（analytic derivative couplings）的电子结构方法，目前这意味着 CIS、TDDFT 以及它们的自旋翻转（spin-flip）类似方法（见第 [9.8.1](subsec_NACMEs_and_CIs.md) 节）。模拟中的核动力学部分与 AIMD 计算中的设定方式完全相同。可以按照增广 FSSH（augmented FSSH, AFSSH）方法[[1321]](../bib_references/bib.md#bib1382)，以额外的计算代价在计算中加入人工退相位（artificial decoherence），该方法以与活跃势能面上的轨迹同在其他势能上传播的位置矩/动量矩之间的力之差成比例的速率，强制实现随机的波函数坍缩。在每个时间步，波函数在各活跃势能面上的分量都会被打印到输出文件中。这些振幅以及位置矩和动量矩（如果请求了 AFSSH）还会被打印到一个名为 `SurfaceHopper` 的文本文件中，该文件位于作业临时目录的 `$QC/AIMD` 子目录下。

要请求 FSSH 计算，只需在激发态 AIMD 模拟所需的变量之外再添加少数几个 *$rem* 变量。目前，FSSH 计算只能使用玻恩-奥本海默分子动力学（BOMD）方法进行。此外，FSSH 计算不支持优化速度 Verlet（optimized velocity Verlet, OVV）积分方法。

FSSH_LOWESTSURFACE

### `FSSH_LOWESTSURFACE`

> **指定面跳跃计算中所考虑的最低能量态。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * $n$
>     * 在 FSSH 计算中仅考虑
>     * $n$
>     * 及以上的状态。
> * **建议**: 无

FSSH_NSURFACES

### `FSSH_NSURFACES`

> **指定面跳跃计算中所考虑的状态数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * $n$
>     * 在面跳跃计算中考虑
>     * $n$
>     * 个状态。
> * **建议**: 任何可能与活跃势能面在能量上接近的状态都应包含在面跳跃计算中。

FSSH_INITIALSURFACE

### `FSSH_INITIALSURFACE`

> **指定面跳跃计算的初始状态。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * $n$
>     * 一个介于
>     * FSSH_LOWESTSURFACE
>     * 与
>     * FSSH_LOWESTSURFACE
>     * $+$
>     * FSSH_NSURFACES
>     * $-1$
>     * 之间的整数。
> * **建议**: 无

AFSSH

### `AFSSH`

> **在面跳跃计算中加入退相位近似。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 传统面跳跃，无退相位。
>     * 1
>     * 使用增广最少跳跃面跳跃（AFSSH）。
> * **建议**: AFSSH 会增加计算成本，但可能提高某些体系的精度。更多细节参见文献 1321 Subotnik J. E., Shenvi N. J. Chem. Phys. (2011) , 134 , pp. 024105 . Link , 1324 Subotnik J. E. J. Phys. Chem. A (2011) , 114 , pp. 12083 . Link , 749 Landry B. R., Subotnik J. E. J. Chem. Phys. (2012) , 137 , pp. 22A513 . Link。

AIMD_SHORT_TIME_STEP

### `AIMD_SHORT_TIME_STEP`

> **为 FSSH 计算指定更短的电子时间步。**
>
> * **类型**: `INTEGER`
> * **默认值**: `TIME_STEP`
> * **选项**:
>     * $n$
>     * 指定电子时间步时长为
>     * $n$
>     * /
>     * AIMD_TIME_STEP_CONVERSION
>     * a.u. 如果
>     * $n$
>     * 小于核时间步变量
>     * TIME_STEP
>     * ，则电子波函数将在每个核时间步内被多次积分，
>     * 并对能量梯度、导数耦合等核量使用线性插值。注意
>     * $n$
>     * 必须能整除
>     * TIME_STEP
>     * 。
> * **建议**: 在长时间模拟中保持密度矩阵的迹接近于 1 的前提下，尽量取较大的值。注意，虽然为电子时间步指定合适的时长对于维持准确的波函数时间演化至关重要，但纯电子时间步采用线性插值来估计重要物理量。因此，较短的电子时间步并不能替代合理的核时间步。

FSSH_CONTINUE

### `FSSH_CONTINUE`

> **从上一次运行的结果重启 FSSH 计算，使用文件 396.0。启用此项时，面跳跃计算的初始条件将被设定，包括正确的波函数振幅、初始跳跃面以及位置/动量矩（若使用 AFSSH），这些均取自先前某次计算的最后一步。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **Options**:
> * **选项**:
>     * $0$
>     * 从头开始新计算。
>     * $1$
>     * 从上一次运行重启。
> * **建议**: 无

???+ example "示例 9.44: FSSH 模拟。注意必须通过 CALC_NAC 请求解析导数耦合，但无需包含 $derivative_coupling 段。CIS_STATE_DERIV  likewise 也是如此，它会被自动设置为初始活跃面。最后，对于在能量上可以到达导数耦合较大区域的体系，必须谨慎选择足够小的时间步，因此这里选择了 AIMD_TIME_STEP_CONVERSION 和 TIME_STEP 。"
    ```qchem
    $molecule
       0 1
       C   -1.620294    0.348677   -0.008838
       C   -0.399206   -0.437493   -0.012535
       C   -0.105193   -1.296810   -1.081340
       H   -0.789110   -1.374693   -1.905080
       C    1.069016   -2.045054   -1.072304
       H    1.292495   -2.701157   -1.889686
       C    1.956240   -1.940324    0.002842
       H    2.859680   -2.517019    0.008420
       C    1.666259   -1.084065    1.071007
       H    2.348104   -1.005765    1.894140
       C    0.495542   -0.335701    1.065497
       H    0.253287    0.325843    1.871866
       O   -1.931045    1.124872    0.911738
       H   -2.269528    0.227813   -0.865645
    $end
    
    $rem
       JOBTYPE                    aimd
       EXCHANGE                   hf
       BASIS                      3-21g
       CIS_N_ROOTS                3
       CIS_SINGLETS               false
       CIS_TRIPLETS               true
       PROJ_TRANSROT              true
       FSSH_LOWESTSURFACE         1
       FSSH_NSURFACES             3   ! hop between T1 and T2
       FSSH_INITIALSURFACE        1   ! start on T1
       AFSSH                      0   ! no decoherence
       CALC_NAC                   true
       AIMD_STEPS                 50  ! Typically more would be used
       TIME_STEP                  14
       AIMD_SHORT_TIME_STEP       2
       AIMD_TIME_STEP_CONVERSION  1   ! Do not alter time_step duration
       AIMD_PRINT                 1
       AIMD_INIT_VELOC            thermal
       AIMD_TEMP                  300 # K
       AIMD_INTEGRATION           vverlet
       FOCK_EXTRAP_ORDER          6
       FOCK_EXTRAP_POINTS         12
       INTEGRAL_SYMMETRY          off
       POINT_GROUP_SYMMETRY       false
    $end
    ```
