---
title: "7.6.4 作业控制"
---

## 7.6.4 作业控制

(July 4, 2026)

NOCIS、1C-NOCIS 和 STEX 均作为 GEN_SCFMAN 中的子程序运行。因此，对于所有计算，你必须设置 GEN_SCFMAN = TRUE。同时强烈建议你在运行 NOCIS/STEX/1C-NOCIS 计算之前，先执行一次开壳层基态计算，因为这些方法都是受限（restricted）的。

### `NOCIS`

> **请求执行 NOCIS/STEX/1C-NOCIS/EA-TDDFT 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不运行这些方法。
>     * `TRUE`: 运行其中一种方法，相关选项在 $nocis 中控制。
> * **建议**: 无

本行以下的选项在 *$nocis* 段中设置。

### `STEX`

> **运行 STEX 计算 INPUT SECTION: $nocis**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * 出现该关键字即会激活 STEX。
> * **建议**: 无

### `ONE_CENTER`

> **运行 1C-NOCIS 计算 INPUT SECTION: $nocis**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `False`: 运行 NOCIS 计算。
>     * `True`: 运行 1C-NOCIS 计算。
> * **建议**: 无

### `ORB_OFFSET`

> **确定 NOCIS/STEX/1C-NOCIS/EA-TDDFT 计算的起始轨道。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 根据所研究体系中首个受关注的轨道来设置。例如，对于 CO ${}_{2}$ 的 O K 边应设为 0，因为两个 O 1s 轨道位于 C 1s 之下；而对于 C K 边则应设为 2。

### `NUM_REF`

> **设置 NOCIS/STEX/1C-NOCIS/EA-TDDFT 计算中参考轨道的数目。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 根据计算中所关注的连续轨道数目来设置。例如，对于 CO ${}_{2}$ 的氧 K 边，参考数应为 2（两个 O 1s 轨道），而对于碳 K 边则为 1（一个 C 1s）。

本行以下的选项专用于 2eOS 参考的 1C-NOCIS 计算。

### `OS_IS`

> **触发以 M ${}_{S}$ = 0 开壳层初态（IS）进行的 1C-NOCIS 计算。INPUT SECTION: $nocis**
>
> * **类型**: `STRING`
> * **默认值**: `ROKS`
> * **选项**:
>     * `CIS`: 采用变换到 NTO 基下的 CIS 激发态波函数作为 IS
>     * `ROKS`: 采用 ROKS 或 ROHF 优化的波函数（单重态或三重态）作为 IS
>     * `CIS_ROKS`: 使用 CIS NTO 作为对 IS 进行 RO 计算的初猜。
> * **建议**: 当以明确定义的初态为目标时使用 CIS，否则使用 ROSCF。注意，若使用 CIS_ROKS 选项，此前的激发态作业可以改用 TDDFT 而非 CIS，以提供更好的初猜。

### `OS_IS_CIS_STATE`

> **当 OS_IS 使用 CIS 或 CIS_ROKS 时，指定以哪个 CIS 态为目标。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 根据所需的 CIS 态来设置。

### `OS_IS_OCC_VALENCE`

> **当 OS_IS 使用 ROKS 时，指定从哪个占据轨道激发。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `HOMO`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 根据所需的 ROKS 态来设置。这是一个从 0 开始索引的变量（最低的轨道索引为 0）。

### `OS_IS_VIR_VALENCE`

> **当 OS_IS 使用 ROKS 时，指定激发到哪个虚轨道。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `LUMO`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 根据所需的 ROKS 态来设置。这是一个从 0 开始索引的变量（最低的轨道索引为 0）。

### `OS_IS_SCF_ALGORITHM`

> **当 OS_IS 使用 ROKS 时，指定 IS 收敛所用的 SCF 算法。INPUT SECTION: $nocis**
>
> * **类型**: `STRING`
> * **默认值**: `GDM when`
> * **选项**:
>     * `DIIS`: GDM GDM_LS SGM SGM_LS
> * **建议**: 使用默认值。

### `OS_IS_DSCF_ALGORITHM`

> **当 OS_IS 使用 ROKS 时，指定 IS 收敛所用的 SCF 算法。INPUT SECTION: $nocis**
>
> * **类型**: `STRING`
> * **默认值**: `NONE`
> * **选项**:
>     * `MOM`: IMOM STEP STEP_MOM
> * **建议**: 使用 DIIS 时，可能需要 MOM 或 IMOM 才能以更高价层激发态为目标。

### `OS_IS_SCF_CONVERGENCE`

> **当 OS_IS 使用 ROKS 或 CIS_ROKS 时，指定 IS ROSCF 计算的 SCF 收敛精度。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `7 for SGM- and GDM-based solvers`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 可根据收敛需要修改，但对基于下降法的求解器（GDM、SGM）设置低于 5 的阈值，对其余方法设置低于 7 的阈值，可能导致轨道收敛不充分。

### `OS_IS_SGM_GRADIENT`

> **当 OS_IS_SCF_ALGORITHM 使用 SGM 时，指定 IS ROSCF 计算的 DELTA_GRADIENT_SCALE。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `75 when using SGM as the SCF solver for the initial valence state`
> * **选项**:
>     * $n$: 小于 100 的正整数
> * **建议**: 参见 DELTA_GRADIENT_SCALE $rem 变量。若 ROKS_IS_SS_MIXING 设为 FALSE，可尝试默认值；否则可能需要约 10 左右的值。若收敛到错误的态，可尝试减小该值。

### `OS_IS_SS_MIXING`

> **控制在 ROKS 过程中是否允许单占据轨道之间发生混合。INPUT SECTION: $nocis**
>
> * **类型**: `BOOL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 抑制耦合。
>     * `TRUE`: 允许耦合。
> * **建议**: 参见 ROKS_SS_MIXING $rem 变量。当所得态难以收敛和/或与基态显著重叠时，抑制耦合非常有用，而在其他情况下似乎无害。某些 $\pi\longrightarrow{}\pi^{*}$ 激发态对此尤其敏感（示例 7.7.4 ）。仅适用于基于下降法的求解器（GDM 或 SGM）。

### `OS_FS_REFERENCE_ORB`

> **终态（FS）参考轨道的选择 INPUT SECTION: $nocis**
>
> * **类型**: `STRING`
> * **默认值**: `ROKS_2EOS for singlet valence excited states`
> * **选项**:
>     * `OC_NOCIS`: 使用 ROSCF 双重态核心电离轨道，并旋转至闭壳层 1C-NOCIS NTO 基
>     * `QUARTET_ION`: 使用 ROSCF 四重态核心电离轨道
>     * `ROKS_2EOS`: 使用经 $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS 优化的轨道。
> * **建议**: 使用默认值。

### `OS_FS_NS_REFERENCE`

> **当 NUM_REF > 1 时，指定所有核心轨道共用的单一参考。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$: 非负整数
> * **建议**: 实验性功能。例如在模拟铁化合物的 M ${}_{2,\;3}$ 边时，3s 核心空穴参考可能有用——虽然它不会逐个优化每个 3p 核心空穴，但能部分描述核心空穴轨道弛豫，并为三个 3p 轨道整体提供无偏的参考。注意目前这些计算尚未实现自旋-轨道耦合。

### `OS_FS_D_ION_SCF_ALGORITHM`

> **指定双重态核心电离 ROSCF 计算收敛所用的 SCF 算法。INPUT SECTION: $nocis**
>
> * **类型**: `STRING`
> * **默认值**: `DIIS`
> * **选项**:
>     * `DIIS`: SGM SGM_LS
> * **建议**: 使用默认值。若无法收敛，尝试 SGM。

### `OS_FS_D_ION_DSCF_ALGORITHM`

> **指定双重态核心电离 ROSCF 计算收敛所用的 SCF 算法。INPUT SECTION: $nocis**
>
> * **类型**: `STRING`
> * **默认值**: `MOM when`
> * **选项**:
>     * `MOM`: IMOM STEP STEP_MOM
> * **建议**: 无。

### `OS_FS_D_ION_SCF_CONVERGENCE`

> **指定双重态核心电离 ROSCF 计算的 SCF 收敛精度。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $ijk...$: 正整数。i, j, k, … 分别对应参考 1、2、3、…
> * **建议**: 将此 $rem 变量设为 0 会跳过双重态核心电离计算，转而在四重态核心电离 ROHF 计算或 $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS 计算中，使用价层激发态轨道作为初猜。当该方式无法收敛参考轨道时，再尝试使用双重态核心电离轨道作为初猜。对基于 SGM 的求解器设置低于 5 的阈值，或对 DIIS / MOM 设置低于 7 的阈值，可能导致轨道收敛不充分。若仅将其作为后续计算的初猜，这一点可能不那么关键（甚至未必必要）。注意 DFT 轨道可能提供更好的初猜——通过 ENV_METHOD $rem 变量指定期望的泛函。当在 1C-NOCIS 2eOS 计算中使用闭壳层 1C-NOCIS 参考轨道时，必须使用恰当的收敛设置而非 DFT。

### `OS_FS_D_ION_SGM_GRADIENT`

> **当 OS_FS_D_ION_SCF_ALGORITHM 使用 SGM 时，指定双重态核心电离 ROSCF 计算的 DELTA_GRADIENT_SCALE。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 根据经验，1 - 10 的值对核心电离似乎效果良好。若 ROSCF 计算不收敛，可尝试增大该值。

### `OS_FS_Q_ION_SCF_ALGORITHM`

> **指定四重态核心电离 ROSCF 计算收敛所用的 SCF 算法。INPUT SECTION: $nocis**
>
> * **类型**: `STRING`
> * **默认值**: `DIIS`
> * **选项**:
>     * `DIIS`: SGM SGM_LS
> * **建议**: 尽可能使用 DIIS。对于棘手的情况，使用 SGM。

### `OS_FS_Q_ION_DSCF_ALGORITHM`

> **指定四重态核心电离 ROSCF 计算收敛所用的 SCF 算法。INPUT SECTION: $nocis**
>
> * **类型**: `STRING`
> * **默认值**: `MOM when`
> * **选项**:
>     * `MOM`: IMOM STEP STEP_MOM
> * **建议**: 为提升效率，优先尝试使用 MOM、IMOM、STEP 或 STEP_MOM（要求 OS_FS_Q_ION_SCF_ALGORITHM 使用 DIIS ）。若 SCF 过程无法收敛或收敛到错误的态，则不要设置该 rem 变量，并尝试在 OS_FS_Q_ION_SCF_ALGORITHM 中使用 SGM。

### `OS_FS_Q_ION_SCF_CONVERGENCE`

> **指定四重态核心电离 ROSCF 计算的 SCF 收敛精度。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `6 (for each reference) for SGM-based solvers`
> * **选项**:
>     * $ijk...$: 正整数。i, j, k, … 分别对应参考 1、2、3、…
> * **建议**: 可根据收敛需要修改，但对基于 SGM 的方法设置低于 5 的阈值、对其余方法设置低于 7 的阈值，可能导致轨道收敛不充分。

### `OS_FS_Q_ION_SGM_GRADIENT`

> **当 OS_FS_Q_ION_SCF_ALGORITHM 使用 SGM 时，指定四重态核心电离 ROSCF 计算的 DELTA_GRADIENT_SCALE。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 根据经验，1 - 10 的值对核心电离似乎效果良好。若 ROSCF 计算不收敛，可尝试增大该值。

### `OS_FS_2EOS_SCF_ALGORITHM`

> **指定 $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS 计算收敛所用的 SCF 算法。INPUT SECTION: $nocis**
>
> * **类型**: `STRING`
> * **默认值**: `SGM`
> * **选项**:
>     * `DIIS`: SGM SGM_LS
> * **建议**: 对非常简单（小）的分子和低能价层激发态使用 DIIS，否则使用 SGM。

### `OS_FS_2EOS_DSCF_ALGORITHM`

> **指定 $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS 计算收敛所用的 SCF 算法。INPUT SECTION: $nocis**
>
> * **类型**: `STRING`
> * **默认值**: `MOM when`
> * **选项**:
>     * `MOM`: IMOM STEP STEP_MOM
> * **建议**: 使用默认值。

### `OS_FS_2EOS_SCF_CONVERGENCE`

> **指定 $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS 计算的 SCF 收敛精度。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `6 (for each reference) for SGM-based solvers`
> * **选项**:
>     * $ijk...$: 正整数。i, j, k, … 分别对应参考 1、2、3、…
> * **建议**: 可根据收敛需要修改，但对基于 SGM 的方法设置低于 5 的阈值、对其余方法设置低于 7 的阈值，可能导致轨道收敛不充分。

### `OS_FS_2EOS_SGM_GRADIENT`

> **当 OS_FS_2EOS_SCF_ALGORITHM 使用 SGM 时，指定 $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ 核心激发 ROKS 计算的 DELTA_GRADIENT_SCALE。INPUT SECTION: $nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `75 when`
> * **选项**:
>     * $n$: 小于 100 的正整数
> * **建议**: 参见 DELTA_GRADIENT_SCALE $rem 变量。若 ROKS_FS_2EOS_SS_MIXING 设为 FALSE，可尝试默认值；否则可能需要约 1 - 10 的值。若收敛到错误的态，可尝试减小该值。

### `OS_FS_2EOS_SS_MIXING`

> **控制在 ROKS 过程中是否允许单占据轨道之间发生混合。INPUT SECTION: $nocis**
>
> * **类型**: `BOOL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 抑制耦合。
>     * `TRUE`: 允许耦合。
> * **建议**: 参见 ROKS_SS_MIXING $rem 变量。当所得态难以收敛和/或与基态显著重叠时，抑制耦合非常有用，而在其他情况下似乎无害。例如 1s $\longrightarrow{}$ 3s 激发态对此现象尤其敏感。仅适用于基于下降法的求解器（GDM 或 SGM）。

???+ example "示例 7.40: N ${}_{2}$ 氮 K 边的 NOCIS"
    ```qchem
    $molecule
       0 1
       N     0.000000     0.000000     0.564990
       N     0.000000     0.000000    -0.564990
    $end
    
    $rem
       METHOD           hf
       BASIS            sto-3g
       UNRESTRICTED     false
       GEN_SCFMAN       true
       NOCIS            true
       THRESH           14
       MAX_SCF_CYCLES   500
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    ! the default behavior is NOCIS
    $nocis
       ORB_OFFSET       0
       NUM_REF          2
    $end
    ```

???+ example "示例 7.41: CN 碳 K 边的 STEX"
    ```qchem
    $molecule
       0 2
       C  0.0000000   0.0000000  -0.6258140
       N  0.0000000   0.0000000   0.5364120
    $end
    
    $rem
       METHOD            hf
       BASIS             sto-3g
       SCF_GUESS         core
       SCF_ALGORITHM     diis_gdm
       MAX_SCF_CYCLES    5000
       THRESH            14
       SCF_CONVERGENCE   10
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
       METHOD            hf
       BASIS             sto-3g
       SCF_GUESS         read
       UNRESTRICTED      false
       SCF_ALGORITHM     diis_gdm
       GEN_SCFMAN        true
       NOCIS             true
       MAX_SCF_CYCLES    5000
       THRESH            14
       SCF_CONVERGENCE   10
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    $nocis
       STEX
       ORB_OFFSET        1
       NUM_REF           1
    $end
    ```

???+ example "示例 7.42: O ${}_{2}$ 氧 K 边的 1C-NOCIS"
    ```qchem
    $molecule
       0 3
       O    0.0000000   0.0000000    0.6021380
       O    0.0000000   0.0000000   -0.6021380
    $end
    
    $rem
       METHOD           hf
       BASIS            sto-3g
       GEN_SCFMAN       true
       THRESH           14
       MAX_SCF_CYCLES   500
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
       UNRESTRICTED     false
       SCF_GUESS        read
       METHOD           hf
       BASIS            sto-3g
       GEN_SCFMAN       true
       NOCIS            true
       THRESH           14
       MAX_SCF_CYCLES   500
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $nocis
       ONE_CENTER
       ORB_OFFSET       0
       NUM_REF          2
    $end
    ```

???+ example "示例 7.43: 水分子第一单重激发态氧 K 边的 1C-NOCIS 2eOS。使用 CIS 计算为 target 价层态的 ROKS 优化提供初猜。"
    ```qchem
    $comment
      CIS calculation on water to generate the target initial state.
    $end
    
    $molecule
      0   1
      O   0.0000      0.0000      0.1173
      H   0.0000      0.7572     -0.4692
      H   0.0000     -0.7572     -0.4692
    $end
    
    $rem
      METHOD               HF
      UNRESTRICTED         FALSE
      BASIS                DEF2-SVP
      SYMMETRY             FALSE
      SYM_IGNORE           TRUE
      GEN_SCFMAN           TRUE
      SCF_ALGORITHM        DIIS_GDM
      CIS_N_ROOTS          3
      CIS_SINGLETS         TRUE
      CIS_TRIPLETS         FALSE
      REL_X2C              TRUE
      THRESH               14
      MEM_TOTAL            1000
      MEM_STATIC           100
      NTO_PAIRS            3
    $end
    
    @@@
    
    $comment
      1C-NOCIS 2eOS singlet calculation.
    $end
    
    $molecule
      read
    $end
    
    $rem
      METHOD               HF
      UNRESTRICTED         FALSE
      BASIS                DEF2-SVP
      SYMMETRY             FALSE
      SYM_IGNORE           TRUE
      GEN_SCFMAN           TRUE
      SCF_GUESS            READ
      MAX_SCF_CYCLES       0
      REL_X2C              TRUE
      NOCIS                1
      THRESH               14
      MEM_TOTAL            1000
      MEM_STATIC           100
    $end
    
    $nocis
      SINGLETS
      ONE_CENTER
      OS_IS                CIS ! Use CIS NTOs for the valence excited state (IS)
    $end
    ```

???+ example "示例 7.44: 吡嗪第一单重激发态氮 K 边的 1C-NOCIS 2eOS。使用正则轨道作为目标价层态 ROKS 优化的初猜。"
    ```qchem
    $comment
      1C-NOCIS 2eOS singlet calculation on pyrazine for the lowest excited state.
    $end
    
    $molecule
      0   1
      N   0.0000      0.0000      1.3814
      N   0.0000      0.0000     -1.3814
      C   0.0000      1.1192      0.6914
      C   0.0000     -1.1192      0.6914
      C   0.0000     -1.1192     -0.6914
      C   0.0000      1.1192     -0.6914
      H   0.0000      2.0412      1.2411
      H   0.0000     -2.0412      1.2411
      H   0.0000     -2.0412     -1.2411
      H   0.0000      2.0412     -1.2411
    $end
    
    $rem
      METHOD               HF
      UNRESTRICTED         FALSE
      BASIS                STO-3G
      SYMMETRY             FALSE
      SYM_IGNORE           TRUE
      GEN_SCFMAN           TRUE
      REL_X2C              TRUE
      NOCIS                1
      THRESH               14
      MEM_TOTAL            1000
      MEM_STATIC           100
    $end
    
    $nocis
      SINGLETS
      ONE_CENTER
      LOCALIZE_ORBITALS              2         ! Localize the two nitrogen 1s orbitals
      NUM_REF                        2         ! Two nitrogen atoms
      OS_IS                          ROKS      ! Use ROKS for the valence excited state (IS)
    $end
    ```

???+ example "示例 7.45: 分子氧三重态基态氧 K 边的 1C-NOCIS 2eOS。三重态的默认参考轨道是四重态核心电离轨道。注意该作业从闭壳层计算开始。"
    ```qchem
    $comment
      1C-NOCIS 2eOS triplet calculation. Note we begin from a closed-shell reference.
    $end
    
    $molecule
      0   1
      O   0.0000      0.0000      0.60375
      O   0.0000      0.0000     -0.60375
    $end
    
    $rem
      METHOD               HF
      UNRESTRICTED         FALSE
      BASIS                STO-3G
      SYMMETRY             FALSE
      SYM_IGNORE           TRUE
      GEN_SCFMAN           TRUE
      SCF_ALGORITHM        DIIS_GDM
      REL_X2C              TRUE
      NOCIS                1
      THRESH               14
      MEM_TOTAL            1000
      MEM_STATIC           100
    $end
    
    $nocis
      TRIPLETS                            ! Activate a triplet 2eOS reference
      ONE_CENTER                          ! One-center approximation
      LOCALIZE_ORBITALS              2    ! Localize 2 orbitals
      NUM_REF                        2    ! Two oxygen atoms
      OS_IS                          ROKS ! Use ROHF to converge the valence excited state (IS)
      OS_FS_Q_ION_SCF_CONVERGENCE    88   ! Convergence of the quartet core ion orbitals
    $end
    ```
