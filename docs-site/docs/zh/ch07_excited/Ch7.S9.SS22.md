---
title: "7.9.22 EOM-CC 优化与性质作业控制"
---

## 7.9.22 EOM-CC 优化与性质作业控制

（2026 年 7 月 4 日）

CC_STATE_TO_OPT

### `CC_STATE_TO_OPT`

> **指定要优化哪个态（或从哪个态计算 EOM-EOM 态间性质）。**
>
> * **类型**: `INTEGER ARRAY`（整型数组）
> * **默认值**: `None`
> * **选项**:
>     * [
>     * $i$
>     * ,
>     * $j$
>     * ]
>     * 优化第
>     * $i$
>     * 个不可约表示（irrep）中的第
>     * $j$
>     * 个态。
> * **建议**: 无

**注意：

态编号应小于或等于相应不可约表示中计算得到的激发态数目。
**

**注意：

若解析梯度不可用，则执行有限差分计算，并且对称性会被关闭。在这种情况下，
CC_STATE_TO_OPT 应在假定 C${}_{1}$ 对称性的前提下指定，*即*，写作 [1,N] 的形式，
其中 N 为要优化的态数（EOM 态从 1 开始编号）。
**

CC_EOM_PROP

### `CC_EOM_PROP`

> **控制是否计算 EOM-CCSD 目标态的非弛豫（期望值）单粒子性质。当前可用的性质包括永久偶极矩、角动量投影、电子密度沿各轴的二次矩（ $\langle x^{2}\rangle$ 、 $\langle y^{2}\rangle$ 和 $\langle z^{2}\rangle$ ）以及 $\langle r^{2}\rangle=\langle x^{2}\rangle+\langle y^{2}\rangle+\langle z^{2}\rangle$ 。该选项与 JOBTYPE = FORCE 、OPT 或 FREQ 不兼容。**
>
> * **类型**: `LOGICAL`（逻辑型）
> * **默认值**: `FALSE (no one-particle properties will be calculated)`（FALSE，不计算单粒子性质）
> * **选项**:
>     * FALSE, TRUE
> * **建议**: 计算性质需要求解额外的方程（用于左本征向量的 EOM-CCSD 方程），这会使每个不可约表示的计算代价约增加一倍。单粒子性质计算本身的代价很低。可通过 CC_STATE_TO_OPT 指定态并请求 NBO = TRUE 以及 = TRUE，使用 NBO 或 libwfa 软件包分析 EOM-CCSD 目标态的单粒子密度。

CC_TRANS_PROP

### `CC_TRANS_PROP`

> **控制是否计算 EOM-CCSD 目标态的跃迁偶极矩（原子单位）、振子强度和旋转强度（原子单位）。默认情况下，跃迁偶极矩、角动量矩阵元及旋转强度在 CCSD 参考态与 EOM-CCSD 目标态之间计算。若要计算一组 EOM-CCSD 态与另一个 EOM-CCSD 态之间的跃迁偶极矩、角动量矩阵元及旋转强度，必须为该态指定 CC_STATE_TO_OPT。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `0 (no transition properties will be calculated)`（0，不计算跃迁性质）
> * **选项**:
>     * 1（计算所有已计算 EOM 态与参考态之间的跃迁性质）
>     * 2（计算所有 EOM 态对之间的跃迁性质）
> * **建议**: 计算跃迁性质需要求解额外的方程（左 EOM-CCSD 本征向量方程，若请求 CCSD 参考态与 EOM-CCSD 目标态之间的跃迁性质，还需加上 lambda CCSD 方程），这会使计算代价约增加一倍。跃迁性质计算本身的代价很低。

**注意：

当输入文件中存在 *$trans_prop* 区段时，它会覆盖 CC_TRANS_PROP *$rem* 变量的设置。
但 *$trans_prop* 要生效，CC_TRANS_PROP *确实* 需要被设置。
**

CC_EOM_ECD

### `CC_EOM_ECD`

> **控制是否计算 ECD（电子圆二色性）跃迁矩。默认情况下，跃迁矩在 CCSD 参考态与 EOM-CCSD 目标态之间计算。若要计算一组 EOM-CCSD 态与另一个 EOM-CCSD 态之间的跃迁矩，必须为该态指定 CC_STATE_TO_OPT。**
>
> * **类型**: `LOGICAL`（逻辑型）
> * **默认值**: `FALSE (do not compute ECD transition moments)`（FALSE，不计算 ECD 跃迁矩）
> * **选项**:
>     * TRUE
>     * 计算 ECD 跃迁矩。
> * **建议**: 仅对手性分子启用。

CC_EOM_2PA

### `CC_EOM_2PA`

> **控制是否计算双光子吸收（2PA）的跃迁矩和截面积。默认情况下，跃迁矩在 CCSD 参考态与 EOM-CCSD 目标态之间计算。若要计算一组 EOM-CCSD 态与另一个 EOM-CCSD 态之间的跃迁矩，必须为该态指定 CC_STATE_TO_OPT。若请求了 2PA NTO 分析，只要取值 $>0$ ，该值便是冗余的。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `0 (do not compute 2PA transition moments)`（0，不计算 2PA 跃迁矩）
> * **选项**:
>     * 1
>     * 使用最快的算法计算 2PA（对正则（canonical）计算使用
>     * $\tilde{\sigma}$
>     * 中间量，对
>     * RI/CD
>     * 响应计算使用
>     * $\sigma$
>     * 中间量）。
>     * 2
>     * 在 2PA 响应方程计算中使用
>     * $\sigma$
>     * 中间量。
>     * 3
>     * 在 2PA 响应方程计算中使用
>     * $\tilde{\sigma}$
>     * 中间量。
> * **建议**: 将求解额外的响应方程（每个目标态 6 个），从而增加计算代价。2PA 矩的计算代价约为能量计算的 10 倍。建议使用默认算法。设置 $>0$ 会同时开启 CC_TRANS_PROP。

CC_EOM_2PA_XCONV

### `CC_EOM_2PA_XCONV`

> **2PA 和 RIXS 计算中阻尼响应方程 DIIS 求解器响应向量（差值范数）的收敛判据。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `5 Corresponding to`（5，对应于）
> * **选项**:
>     * $n$
>     * 对应于
>     * $10^{-n}$
>     * 收敛判据。
> * **建议**: 双精度计算时使用默认值。单精度计算时可放宽。

DAMPED_DALTON_SOLVER

### `DAMPED_DALTON_SOLVER`

> **布尔开关，控制是否在阻尼响应方程（CCSD 极化率与超极化率，以及 EOM-CCSD 2PA 和 RIXS 截面积）中使用新的类 Davidson 求解器（Dalton）。**
>
> * **类型**: `LOGICAL`（逻辑型）
> * **默认值**: `TRUE (Use the new`（TRUE，使用新求解器）
> * **Options**:
>     * FALSE
>     * 若希望对上述性质使用旧的 DIIS 求解器。
> * **建议**: 使用新求解器，其收敛速度相对 DIIS 更快。

DALTON_XCONV

### `DALTON_XCONV`

> **响应方程 Dalton 求解器残差（平方范数）的收敛判据。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `6 Corresponding to`（6，对应于）
> * **选项**:
>     * $n$
>     * 对应于
>     * $10^{-n}$
>     * 收敛判据。
> * **建议**: 双精度计算时使用默认值。单精度计算时可放宽至 5。

DALTON_MAXITER

### `DALTON_MAXITER`

> **响应方程 Dalton 求解器允许的最大迭代次数。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `100`
> * **选项**:
>     * $n$
>     * 用户自定义的迭代次数。
> * **建议**: 默认值通常已足够。

DALTON_MAXSPACE

### `DALTON_MAXSPACE`

> **指定响应方程 Dalton 求解器子空间中向量的最大数目。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `200`
> * **选项**:
>     * $n$
>     * 在子空间重置之前，每个根最多
>     * $n$
>     * 个向量。
> * **建议**: 较大的值会增加磁盘存储占用，但能加快并稳定收敛。

DALTON_PRECOND_START

### `DALTON_PRECOND_START`

> **指定在响应方程的 Dalton 过程中，从第几次迭代开始对残差应用预处理器。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `1`
> * **选项**:
>     * $n$
>     * 用户自定义的迭代次数。
> * **建议**: 使用默认值。

CALC_SOC

### `CALC_SOC`

> **控制是否计算 CC/EOM/ADC/CIS/TDDFT 电子态之间的自旋-轨道耦合（Spin-Orbit Coupling, SOC）。在 CC/EOM-CC 方法族中，默认在 CCSD 参考态与 EOM-CCSD 目标态之间计算耦合。若要计算 EOM 态之间的耦合，CC_STATE_TO_OPT 必须指定初始 EOM 态。若请求了 NTO 分析，则将对无自旋跃迁密度矩阵进行分析，并打印 NTO 对上的自旋-轨道积分。**
>
> * **类型**: `INTEGER/LOGICAL`（整型/逻辑型）
> * **默认值**: `FALSE (no spin-orbit couplings will be calculated)`（FALSE，不计算自旋-轨道耦合）
> * **选项**:
>     * 0/FALSE
>     * （不计算自旋-轨道耦合）
>     * 1/TRUE
>     * 启用 SOC 计算。仅限 EOM-CC/EOM-MP2：使用带 L+/L- 平均的新代码计算自旋-轨道耦合
>     * 2
>     * 仅限 EOM-CC/EOM-MP2：使用不带 L+/L- 平均的新代码计算自旋-轨道耦合
>     * 3
>     * 仅限 EOM-CC/EOM-MP2：使用旧版代码计算自旋-轨道耦合
>     * 4
>     * 使用有效核电荷计算单电子自旋-轨道耦合（对 EOM-CC/MP2 带 L+/L- 平均）
> * **建议**: CCMAN2 为 EOM-CC/EOM-MP2 方法支持多种 SOC 计算变体。默认计算单电子和平均场双电子 SOC。若要启用完整的双电子 SOC，必须开启双粒子 EOM 性质（参见 CC_EOM_PROP_TE）。

CALC_NAC

### `CALC_NAC`

> **控制是否为 EOM-CC、CIS 和 TDDFT 波函数计算非绝热耦合（Nonadiabatic Couplings, NAC）。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `0 (do not compute NAC)`（0，不计算 NAC）
> * **选项**:
>     * 1
>     * 对 EOM-CC 尚未实现（NYI）
>     * 2
>     * 使用 Szalay 的方法计算 NAC（EOM-CC 需指定此项）。
> * **建议**: 将求解额外的响应方程，并计算所有 EOM 态及求和态的梯度，从而增加计算代价。仅在需要时请求，且不要请求过多的 EOM 态。

CC_POL

### `CC_POL`

> **指定计算 CCSD 波函数极化率的方法。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `0`
> * **选项**:
>     * 1
>     * （解析导数或响应理论的对称-非对称混合方法）
>     * 2
>     * （解析导数或响应理论的非对称方法）
>     * 3
>     * （使用右响应中间量的期望值方法）
>     * 4
>     * （使用左响应中间量的期望值方法）
>     * 13
>     * （使用右响应中间量的阻尼响应期望值方法）
>     * 14
>     * （使用左响应中间量的阻尼响应期望值方法）
>     * 15
>     * （使用一阶响应密度矩阵的阻尼响应期望值方法）
>     * 23
>     * （使用右响应中间量和虚频率的期望值方法）
> * **建议**: CCSD 极化率的计算代价很高，因为需求解三个/六个（静态）或六个/十二个（动态）额外的响应方程。非必要请勿请求该性质。

EOM_POL

### `EOM_POL`

> **指定计算 EOM-CCSD 波函数极化率的方法。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `0`
> * **选项**:
>     * 1
>     * （解析导数或响应理论的对称-非对称混合方法）
>     * 2
>     * （解析导数或响应理论的非对称方法）
>     * 3
>     * （使用右响应中间量的期望值方法）
>     * 4
>     * （使用左响应中间量的期望值方法）
>     * 23
>     * （使用右响应中间量和虚频率的期望值方法）
> * **建议**: EOM-CCSD 极化率的计算代价很高，因为需求解三个/九个（静态）或六个/十八个（动态）额外的响应方程。非必要请勿请求该性质。

CC_1HPOL

### `CC_1HPOL`

> **指定计算 CCSD 波函数一阶超极化率（first hyperpolarizability）的方法。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `0`
> * **选项**:
>     * 1
>     * （仅使用一阶响应波函数的阻尼响应期望值方法）
>     * 3
>     * （使用二阶响应密度矩阵进行波函数与自然轨道分析的阻尼响应期望值方法）
> * **建议**: CCSD 一阶超极化率的计算代价很高，因为需求解大量一阶和二阶响应方程。非必要请勿请求该性质。

CC_EOM_PROP_TE

### `CC_EOM_PROP_TE`

> **请求计算非弛豫双粒子 EOM-CC 性质。双粒子性质目前包括 $\langle\hat{S}^{2}\rangle$ 。单粒子性质也将一并计算，因为与 $\langle\hat{S}^{2}\rangle$ 的代价相比，单粒子性质计算的额外代价可以忽略。变量 CC_EOM_PROP 也必须同时设置为 TRUE。或者，可以使用 CC_CALC_SSQ 来请求计算 $\langle\hat{S}^{2}\rangle$ 。**
>
> * **类型**: `LOGICAL`（逻辑型）
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE, TRUE
> * **建议**: 双粒子性质的计算代价很高，因为需要计算并使用双粒子密度矩阵（代价约等于一次解析梯度计算的代价）。除非确实需要，请勿请求双粒子性质。

CC_FULLRESPONSE

### `CC_FULLRESPONSE`

> **计算完全弛豫的性质（含或不含轨道弛豫项）。变量 CC_EOM_PROP 也必须同时设置为 TRUE。**
>
> * **类型**: `INTEGER`（整型）
> * **默认值**: `0`
> * **选项**:
>     * 1
>     * （同时计算振幅响应和轨道响应）
>     * 2
>     * （仅计算振幅响应）
> * **建议**: 非 UHF/RHF 参考态不可用。仅对拥有解析梯度的 EOM/CI 方法可用。

CC_SYMMETRY

### `CC_SYMMETRY`

> **控制耦合簇计算中对称性的使用**
>
> * **类型**: `LOGICAL`（逻辑型）
> * **默认值**: `TRUE`
> * **选项**:
>     * TRUE
>     * 使用分子的点群对称性
>     * FALSE
>     * 不使用点群对称性（所有态均为
>     * $A$
>     * 对称性）。
> * **建议**: 任何有限差分计算（例如二阶导数）都会自动关闭该选项。

**注意：

仅支持阿贝尔群。对于属于非阿贝尔群的分子，必须将 USE_ABELIAN_SUBGROUP 设置为
TRUE（这目前是 CCMAN 和 CCMAN2 所有作业的默认设置）。
**

STATE_ANALYSIS

### `STATE_ANALYSIS`

> **激活使用 libwfa 进行的激发态分析。**
>
> * **类型**: `LOGICAL`（逻辑型）
> * **默认值**: `FALSE (no excited state analyses)`（FALSE，不进行激发态分析）
> * **选项**:
>     * TRUE, FALSE
> * **建议**: 若需要激发态分析则设置为 TRUE，若需要绘制密度或轨道图也应设置。详见第 10.2.12 节。

G_TENSOR

### `G_TENSOR`

> **激活 g 张量计算。**
>
> * **类型**: `LOGICAL`（逻辑型）
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE（或 0）
>     * 不计算 g 张量
>     * TRUE（或 1）
>     * 计算 g 张量。
> * **建议**: 无。

**注意：

g 张量计算仅对 CCSD 可用。
**

## 7.9.22.1 示例

???+ example "示例 7.127: 使用 EOM-EE-CCSD 对亚甲基（methylene）的激发开壳单重态 ${}^{1}$ B ${}_{2}$ 进行几何优化，随后计算完全弛豫的单电子性质。"
    ```qchem
    $molecule
       0 1
       C
       H  1 rCH
       H  1 rCH 2 aHCH
    
       rCH    = 1.083
       aHCH   = 145.
    $end
    
    $rem
       JOBTYPE                   OPT
       METHOD                    EOM-CCSD
       BASIS                     cc-pVTZ
       SCF_GUESS                 CORE
       SCF_CONVERGENCE           9
       EE_SINGLETS               [0,0,0,1]
       EOM_NGUESS_SINGLES        2
       CC_STATE_TO_OPT           [4,1]
       EOM_DAVIDSON_CONVERGENCE  9    use tighter convergence for EOM amplitudes
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD               EOM-CCSD
       BASIS                cc-pVTZ
       SCF_GUESS            READ
       EE_SINGLETS          [0,0,0,1]
       EOM_NGUESS_SINGLES   2
       CC_EOM_PROP          1  calculate properties for EOM states
       CC_FULLRESPONSE      1  use fully relaxed properties
    $end
    ```

???+ example "示例 7.128: 使用 EOM-SF-CCSD 对 CH ${}_{2}$ 的最低单重态进行性质与跃迁性质计算。"
    ```qchem
    $molecule
       0 3
       C
       H  1 rch
       H  1 rch 2 ahch
    
       rch  = 1.1167
       ahch = 102.07
    $end
    
    $rem
       METHOD             eom-ccsd
       BASIS              cc-pvtz
       SCF_GUESS          core
       SCF_CONVERGENCE    9
       SF_STATES          [2,0,0,3]   Get three 1^B2 and two 1^A1 SF states
       CC_EOM_PROP        1
       CC_TRANS_PROP      1
       CC_STATE_TO_OPT    [4,1] First EOM state in the 4th irrep
    $end
    ```

???+ example "示例 7.129: 使用长度规范、动量规范和混合规范计算 EOM 跃迁强度。"
    ```qchem
    $comment
    EOM-CC oscillator strength using three gauges
    $end
    
    $molecule
    0 1
    C       1.2509987    -0.0000000     0.0000000
    C      -1.2509987     0.0000000    -0.0000000
    H       2.3262529     1.8903377     0.4190778
    H       2.3262529    -1.8903377    -0.4190778
    H      -2.3262529     1.8903377    -0.4190778
    H      -2.3262529    -1.8903377     0.4190778
    $end
    
    $rem
        method = ccsd
        input_bohr = true
        ee_singlets [0,0,2,2]
        basis = 6-31g
        cc_trans_prop = true
        cc_ref_prop = 1
        cc_eom_prop = 1
    $end
    
    $trans_prop
      state_list
        ref
        ee_singlets 0 0
      end_list
      calc dipole linmom
    $end
    ```

???+ example "示例 7.130: 使用 EOM-CCSD 波函数计算 ECD。"
    ```qchem
    $comment
    Calculation of ECD  using EOM-CC wave-functions
    $end
    
    $molecule
    0 1
    C       1.2509987    -0.0000000     0.0000000
    C      -1.2509987     0.0000000    -0.0000000
    H       2.3262529     1.8903377     0.4190778
    H       2.3262529    -1.8903377    -0.4190778
    H      -2.3262529     1.8903377    -0.4190778
    H      -2.3262529    -1.8903377     0.4190778
    $end
    
    $rem
    method = ccsd
    input_bohr = true
    ee_singlets [0,0,2,2]
    basis = 6-31g
    cc_trans_prop = true
    cc_ref_prop = 1
    cc_eom_prop = 1
    cc_eom_ecd  = 1 ! keyword to activate ECD
    $end
    
    @@@
    $comment
    Calculation of ECD  using EOM-CC wave-functions
    using trans_prop section
    $end
    
    $molecule
    0 1
    C       1.2509987    -0.0000000     0.0000000
    C      -1.2509987     0.0000000    -0.0000000
    H       2.3262529     1.8903377     0.4190778
    H       2.3262529    -1.8903377    -0.4190778
    H      -2.3262529     1.8903377    -0.4190778
    H      -2.3262529    -1.8903377     0.4190778
    $end
    
    $rem
    method = ccsd
    input_bohr = true
    ee_singlets [0,0,2,2]
    basis = 6-31g
    cc_trans_prop = true
    cc_ref_prop = 1
    cc_eom_prop = 1
    $end
    
    $trans_prop
    state_list
        ref
        ee_singlets 0 0
        end_list
        calc ecd
    $end
    ```

???+ example "示例 7.7.131: 对 CH ${}_{2}$ Cl 的 ${}^{2}$ A ${}_{1}$ 激发态进行严格收敛的几何优化，随后计算非弛豫与完全弛豫的永久偶极矩和 $\langle\hat{S}^{2}\rangle$ 。"
    ```qchem
    $molecule
       0 2
       H
       C   1  CH
       CL  2  CCL  1  CCLH
       H   2  CH   3  CCLH  1  DIH
    
       CH   = 1.096247
       CCL  = 2.158212
       CCLH = 122.0
       DIH  = 180.0
    $end
    
    $rem
       JOBTYPE                    OPT
       METHOD                     EOM-CCSD
       BASIS                      6-31G*  Basis Set
       SCF_GUESS                  SAD
       EOM_DAVIDSON_CONVERGENCE   9    EOM amplitude convergence
       CC_T_CONV                  9    CCSD amplitudes convergence
       EE_STATES                  [0,0,0,1]
       CC_STATE_TO_OPT            [4,1]
       EOM_NGUESS_SINGLES         2
       GEOM_OPT_TOL_GRADIENT      2
       GEOM_OPT_TOL_DISPLACEMENT  2
       GEOM_OPT_TOL_ENERGY        2
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD             EOM-CCSD
       BASIS              6-31G*  Basis Set
       SCF_GUESS          READ
       EE_STATES          [0,0,0,1]
       EOM_NGUESS_SINGLES  2
       CC_EOM_PROP        1   calculate one-electron properties
       CC_EOM_PROP_TE     1   and two-electron properties (S^2)
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD              EOM-CCSD
       BASIS               6-31G*  Basis Set
       SCF_GUESS           READ
       EE_STATES           [0,0,0,1]
       EOM_NGUESS_SINGLES  2
       CC_EOM_PROP         1  calculate one-electron properties
       CC_EOM_PROP_TE      1  and two-electron properties (S^2)CC_EXSTATES_PROP 1
       CC_FULLRESPONSE     1  same as above, but do fully relaxed properties
    $end
    ```

???+ example "示例 7.132: 对甲醛（formaldehyde）的三个 A ${}_{2}$ 态和一个 B ${}_{2}$ 态进行 CCSD 计算。将在第三个 A ${}_{2}$ 态与所有其他 EOM 态之间计算跃迁性质。"
    ```qchem
    $molecule
       0  1
       O
       C  1  1.4
       H  2  1.0  1  120
       H  2  1.0  1  120  3 180
    $end
    
    $rem
       BASIS             6-31+G
       METHOD            EOM-CCSD
       EE_STATES         [0,3,0,1]
       CC_STATE_TO_OPT   [2,3]
       CC_TRANS_PROP     true
    $end
    ```

???+ example "示例 7.133: 对 $\rm H_{2}O^{+}$ 的 X ${}^{2}$ B ${}_{2}$ 态进行 EOM-IP-CCSD 几何优化。"
    ```qchem
    $molecule
       0 1
       H    0.774767     0.000000     0.458565
       O    0.000000     0.000000    -0.114641
       H   -0.774767     0.000000     0.458565
    $end
    
    $rem
       JOBTYPE           opt
       METHOD            eom-ccsd
       BASIS             6-311G
       IP_STATES         [0,0,0,1]
       CC_STATE_TO_OPT   [4,1]
    $end
    ```

???+ example "示例 7.7.134: 对甲醛的 ${}^{2}B_{1}$ 阴离子共振态进行 CAP-EOM-EA-CCSD 几何优化。所采用的基组为 aug-cc-pVDZ，并在重原子上附加了 3s3p 弥散函数。"
    ```qchem
    $molecule
       0 1
       C       0.0000000000     0.0000000000     0.5721328608
       O       0.0000000000     0.0000000000    -0.7102635035
       H       0.9478180646     0.0000000000     1.1819748108
       H      -0.9478180646     0.0000000000     1.1819748108
    $end
    
    $rem
       JOBTYPE                    opt
       METHOD                     eom-ccsd
       BASIS                      gen
       N_FROZEN_CORE              0
       SCF_CONVERGENCE            9
       CC_CONVERGENCE             9
       EOM_DAVIDSON_CONVERGENCE   9
       EA_STATES                  [0,0,0,2]
       CC_STATE_TO_OPT            [4,1]
       XC_GRID                    000250000974
       COMPLEX_CCMAN              1
    $end
    
    $complex_ccman
       CS_HF 1
       CAP_TYPE 1
       CAP_ETA 60
       CAP_X 3850
       CAP_Y 2950
       CAP_Z 6100
    $end
    
    $basis
     H   0
     S   3  1.00
           13.0100000         0.196850000E-01
           1.96200000         0.137977000
          0.444600000         0.478148000
     S   1  1.00
          0.122000000          1.00000000
     P   1  1.00
          0.727000000          1.00000000
     S   1  1.00
          0.297400000E-01      1.00000000
     P   1  1.00
          0.141000000          1.00000000
     ****
     C   0
     S   8  1.00
           6665.00000         0.692000000E-03
           1000.00000         0.532900000E-02
           228.000000         0.270770000E-01
           64.7100000         0.101718000
           21.0600000         0.274740000
           7.49500000         0.448564000
           2.79700000         0.285074000
          0.521500000         0.152040000E-01
     S   8  1.00
           6665.00000        -0.146000000E-03
           1000.00000        -0.115400000E-02
           228.000000        -0.572500000E-02
           64.7100000        -0.233120000E-01
           21.0600000        -0.639550000E-01
           7.49500000        -0.149981000
           2.79700000        -0.127262000
          0.521500000         0.544529000
     S   1  1.00
          0.159600000          1.00000000
     P   3  1.00
           9.43900000         0.381090000E-01
           2.00200000         0.209480000
          0.545600000         0.508557000
     P   1  1.00
          0.151700000          1.00000000
     D   1  1.00
          0.550000000          1.00000000
     S   1  1.00
          0.469000000E-01     1.00000000
     P   1  1.00
          0.404100000E-01     1.00000000
     D   1  1.00
          0.151000000         1.00000000
     S   1  1.00
          0.234500000E-01      1.00000000
     S   1  1.00
          0.117250000E-01      1.00000000
     S   1  1.00
          0.058625000E-01      1.00000000
     P   1  1.00
          0.202050000E-01      1.00000000
     P   1  1.00
          0.101025000E-01      1.00000000
     P   1  1.00
          0.050512500E-01      1.00000000
     ****
     O   0
     S   8  1.00
           11720.0000         0.710000000E-03
           1759.00000         0.547000000E-02
           400.800000         0.278370000E-01
           113.700000         0.104800000
           37.0300000         0.283062000
           13.2700000         0.448719000
           5.02500000         0.270952000
           1.01300000         0.154580000E-01
     S   8  1.00
           11720.0000        -0.160000000E-03
           1759.00000        -0.126300000E-02
           400.800000        -0.626700000E-02
           113.700000        -0.257160000E-01
           37.0300000        -0.709240000E-01
           13.2700000        -0.165411000
           5.02500000        -0.116955000
           1.01300000         0.557368000
     S   1  1.00
          0.302300000          1.00000000
     P   3  1.00
           17.7000000         0.430180000E-01
           3.85400000         0.228913000
           1.04600000         0.508728000
     P   1  1.00
          0.275300000          1.00000000
     D   1  1.00
           1.18500000          1.00000000
     S   1  1.00
          0.789600000E-01      1.00000000
     P   1  1.00
          0.685600000E-01      1.00000000
     D   1  1.00
          0.332000000          1.00000000
     S   1  1.00
          0.394800000E-01      1.00000000
     S   1  1.00
          0.197400000E-01      1.00000000
     S   1  1.00
          0.098700000E-01      1.00000000
     P   1  1.00
          0.342800000E-01      1.00000000
     P   1  1.00
          0.171400000E-01      1.00000000
     P   1  1.00
          0.085700000E-01      1.00000000
     ****
    $end
    ```

???+ example "示例 7.135: 使用简并光子计算共振 2PA。"
    ```qchem
    $molecule
       0 1
       O
       H  1 0.959
       H  1 0.959 2 104.654
    $end
    
    $rem
       METHOD         eom-ccsd
       BASIS          aug-cc-pvtz
       EE_SINGLETS    [1,0,0,0]   1A_1 state
       CC_TRANS_PROP  1    Compute transition properties
       CC_EOM_2PA     1    Calculate 2PA cross-sections using the fastest algorithm
    $end
    ```

???+ example "示例 7.136: 在非简并的共振 2PA 中，对一定范围的频率对进行扫描。"
    ```qchem
    $molecule
       0 1
       O
       H  1 0.959
       H  1 0.959 2 104.654
    $end
    
    $rem
       METHOD         eom-ccsd
       BASIS          aug-cc-pvdz
       EE_SINGLETS    [2,0,0,0]  !Two A_1 states
       CC_TRANS_PROP  1          !Calculate transition properties
       CC_EOM_2PA     1          !Calculate 2PA cross-sections using the fastest algorithm
    $end
    
    $2pa
       n_2pa_points 11
       omega_1 500000 5000
    $end
    ```

???+ example "示例 7.137: 两个激发态之间使用简并光子的共振 2PA。"
    ```qchem
    $molecule
       0 1
       O
       H  1 0.959
       H  1 0.959 2 104.654
    $end
    
    $rem
       METHOD          eom-ccsd
       BASIS           aug-cc-pvtz
       EE_SINGLETS     [2,0,0,0] Two A_1 states
       CC_STATE_TO_OPT [1,1]     "Reference" state for transition properties is 1A_1 state
       CC_TRANS_PROP   1         Compute transition properties
       CC_EOM_2PA      1         Calculate 2PA cross-sections using the fastest algorithm
    $end
    ```

???+ example "示例 7.138: 基于阻尼响应理论框架和期望值方法，在一定频率范围内计算 LiH 的 CCSD 波函数的一阶超极化率。"
    ```qchem
    $comment
    Calculation of static and dynamical first hyperpolarizability for CCSD wave function
    for LiH with STO-3G basis set using the framework of damped response theory and
    the expectation-value approach.
    The property for the following set of photons is calculated:
    (omega_1, omega_2; omega_3) in cm-1
    (0, 0; 0), (2500, 0; -2500), (5000, 0; -5000), (0, 3500; -3500),
    (0, 7000; -7000), (2500, 3500; -6000), (2500, 7000; -9500),
    (5000, 3500; -8500), (5000, 7000; -12000)
    $end
    
    $molecule
    0 1
    H
    Li 1 1.6
    $end
    
    $rem
    METHOD           ccsd
    BASIS            sto-3g
    CC_REF_PROP      1         ! required for CCSD property calculation
    CC_1HPOL         1         ! computes first hyperpolarizability using first-order response wave functions only
    MEM_STATIC       400
    CC_MEMORY        2000
    THRESH           13
    SCF_CONVERGENCE  10
    CC_CONVERGENCE   9
    $end
    
    $1hpol
    omega_1 0 2500000 3 0.01  ! scans the first photon frequency from 0 cm-1 to 5000 cm-1 in 3-1=2 steps of 2500, corresponding damping is 0.01 hartrees
    omega_2 0 3500000 3 0.01  ! scans the second photon frequency from 0 cm-1 to 7000 cm-1 in 3-1=2 steps of 3500, corresponding damping is 0.01 hartrees
    omega_3 0.01              ! damping for the third photon is 0.01 hartrees
    $end
    
    ```

???+ example "示例 7.139: 乙炔-O 中间体（acetylene-O intermediate）中两个激发三重态之间的平均场自旋-轨道计算。"
    ```qchem
    $molecule
       0 1
       C        -0.0303943366   -0.3149506151   -0.0436827067
       H        -0.1031279784   -1.4353675705   -0.1647400816
       O         1.0178175761    0.2350702146    0.2517598501
       C        -1.3252768442    0.1905302054   -0.4205132671
       H        -2.0767072171    0.1461814657    0.3842573052
    $end
    
    $rem
       BASIS             cc-pvdz
       METHOD            eom-ccsd
    point_group_symmetry False
       SF_STATES         [2]
       CC_STATE_TO_OPT   [1,1]
       THRESH            14
       CALC_SOC          1
       CC_TRANS_PROP     1
    $end
    ```

???+ example "示例 7.140: 乙炔-O 中间体中参考单重态与激发三重态之间的平均场自旋-轨道计算。"
    ```qchem
    $molecule
    0 1
      C        -0.0303943366   -0.3149506151   -0.0436827067
      H        -0.1031279784   -1.4353675705   -0.1647400816
      O         1.0178175761    0.2350702146    0.2517598501
      C        -1.3252768442    0.1905302054   -0.4205132671
      H        -2.0767072171    0.1461814657    0.3842573052
    $end
    
    $rem
       BASIS           cc-pvdz
       METHOD          eom-ccsd
    point_group_symmetry False
       EE_TRIPLETS     [1]
       THRESH          14
       CALC_SOC        1
       CC_TRANS_PROP   1
    $end
    ```

???+ example "示例 7.141: 使用 EOM-SF-CCSD 计算 NH 中闭壳单重态与 $M_{S}=1$ 三重态之间的自旋-轨道耦合。"
    ```qchem
    $molecule
       0 3
       N
       H N 1.0450
    $end
    
    $rem
       METHOD          = eom-ccsd
       BASIS           = 6-31g
       SF_STATES       = [1,2,0,0]
       CC_TRANS_PROP   = true
       CALC_SOC        = 3         ! legacy code
       CC_STATE_TO_OPT = [1,1]
    $end
    ```

???+ example "示例 7.142: EOM-DEA 态之间的 SOC 计算。"
    ```qchem
    $comment
    SOC calculations between EOM-DEA states.
    $end
    
    $molecule
    +2 1
    Si
    H  1 1.530
    F  1 1.605 2 97.000
    $end
    
    $rem
    BASIS = 6-31G*
    jobtype = sp
    method = eom-ccsd
    n_frozen_core  0
    dea_singlets = [1,1]     Ms=0 triplet
    dea_triplets = [0,1]     Ms=-1 triplets
    CALC_SOC = 2             Activates SOC calculation with new code
    CC_EOM_PROP = 1
    CC_TRANS_PROP = true
    $end
    
    ```

???+ example "示例 7.143: 使用赝势和有效核电荷，通过 EOM-EA-MP2 方法计算中性六重态 (tpa)Fe 配合物（去除配体）中的自旋-轨道耦合。"
    ```qchem
    $comment
    Spin-orbit coupling calculation with SBKJC ecp using default effective nuclear
    charges.  Computes SOC in neutral hextet (tpa)Fe geometry (stripped ligands)
    by EOM-EA-MP2 method and high-spin reference.
    $end
    
    $molecule
    0 6
      N   -0.0330663   -0.2576466    1.3744726
      N    2.0052862   -0.4826730   -0.5758819
      N   -1.9801232   -0.6573608   -0.6407513
      N   -0.0634263    1.4157074   -0.9056826
     Fe    0.0133915   -0.5560750   -0.6002859
      H   -0.0630940   -1.1802863    1.8620650
      H   -0.8780689    0.2958440    1.6401738
      H    2.3459249   -0.6439674   -1.5498484
      H    2.3506743   -1.2708551    0.0162081
      H   -2.2816187   -0.8324531   -1.6252623
      H   -2.3957415    0.2480261   -0.3283621
      H    0.0565056    1.5985967   -1.9267087
      H    0.7257691    1.8766147   -0.3993792
      H    0.8165651    0.2643868    1.6852415
    $end
    
    $rem
       METHOD                = EOM-MP2
       EOM_EA_BETA           = [5]
       MAX_SCF_CYCLES        = 300
       SCF_ALGORITHM         = gdm
       SCF_GUESS             = autosad
       EOM_PRECONV_SINGLES   = 1
       CALC_SOC              = 4
       CC_TRANS_PROP         = 2
       BASIS  =   SBKJC           [  use effective charges of ecps in soc calculation]
       ECP = fit-SBKJC
    $end
    
    ```

???+ example "示例 7.144: 使用全电子基组、用户提供的有效核电荷以及 EOM-IP 波函数计算 ClO 中的自旋-轨道耦合。"
    ```qchem
    $comment
    Spin-orbit coupling calculation using all-electron basis set
    and user-provided effective nuclear charges by
    using EOM-IP wave-functions.
    $end
    
    $molecule
    -1 1
      Cl   -0.9937913   -0.6696391   -1.9087016
      O    0.3415336   -0.1593825   -1.2619353
    $end
    
    $rem
    jobtype             = sp
    method              = eom-ccsd
    basis               = 6-31G
    print_general_basis = 1
    scf_convergence     = 12
    cc_convergence      = 10
    eom_davidson_conv   = 8
    eom_ip_alpha        = [0,0,1,1]
    cc_eom_prop         = 1
    cc_ref_prop         = 1
    cc_trans_prop       = 1
    cc_state_to_opt     = [3,1]
    calc_soc            = 4
    $end
    
    $soc_eff_charges
    8.0 6.0
    17.0 11.0
    $end
    ```

???+ example "示例 7.145: 计算三重态（第一个作业）和单重态（第二个作业）流形内部 EOM-EE 态之间的非绝热耦合。"
    ```qchem
    $molecule
       +1 1
       H          0.00000        0.00000        0.0
       He         0.00000        0.00000        3.0
    $end
    
    $rem
       JOBTYPE                  = FORCE
       METHOD                   = EOM-CCSD
       BASIS                    = cc-pVDZ
       INPUT_BOHR               = true
       EE_TRIPLETS              = [2]
       CC_EOM_PROP              = true
       POINT_GROUP_SYMMETRY     = false Do not reorient molecule and turn off YYYYYYYYYYYY
       CALC_NAC                 = 2     Invoke Szalay NAC
       EOM_DAVIDSON_CONVERGENCE = 9     tight davidson convergence
       SCF_CONVERGENCE          = 9     Hartree-Fock convergence threshold 1e-9
       CC_CONVERGENCE           = 9
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE                  = FORCE
       METHOD                   = EOM-CCSD
       BASIS                    = cc-pVDZ
       INPUT_BOHR               = true
       EE_STATES                = [2]   singlets
       POINT_GROUP_SYMMETRY     = false Do not reorient molecule and turn off YYYYYYYYYYYY
       CALC_NAC                 = 2     Invoke Szalay NAC
       EOM_DAVIDSON_CONVERGENCE = 9     tight davidson convergence
       SCF_CONVERGENCE          = 9     Hartree-Fock convergence threshold 1e-9
       CC_CONVERGENCE           = 9
    $end
    ```

???+ example "示例 7.146: 计算氦（Helium）的 CCSD 波函数的静态偶极极化率。"
    ```qchem
    $molecule
       0 1
       He
    $end
    
    $rem
       METHOD            ccsd
       BASIS             cc-pvdz
       CC_REF_PROP       1
       CC_POL            2
       CC_DIIS_SIZE      15
       CC_FULLRESPONSE   1
    $end
    ```

???+ example "示例 7.147: 水分子：在对分子取向进行平均的情况下计算光电离截面与光电子角分布。"
    ```qchem
    $comment
    Calculating photoionization cross-section and photoelectron angular distribution
    with averaging over molecular orientations.
    $end
    
    $molecule
     0 1
     O     0.000000000000     0.000000000000    -0.004762594898
     H     0.000000000000     0.801842648150    -0.560344690289
     H     0.000000000000    -0.801842648150    -0.560344690289
    $end
    
    $rem
        JOB_TYPE = SP
        METHOD = EOM-CCSD
        BASIS = 6-31G*
        EOM_IP_ALPHA = [1,0,0,1]
        CC_DO_DYSON = TRUE
        CC_FREE_ELECTRON = 1
        MEM_TOTAL = 4000
    $end
    
    $free_electron
        N_ENERGY_POINTS 10
        N_THETA 25
        N_PHI 10
        SPIN_DEG 2
        ORB_DEG 1
        DO_AVERAGE 1
        KE_MIN 10
        KE_MAX 1010
    $end
    
    ```

???+ example "示例 7.148: 水分子：使用 Z 方向偏振光计算光电离截面、不对称参数与光电子角分布。"
    ```qchem
    $comment
    Calculating photoionization cross-section, asymmetry parameter, and PAD
    with a Z-polarized light.
    $end
    
    $molecule
     0 1
     O     0.000000000000     0.000000000000    -0.004762594898
     H     0.000000000000     0.801842648150    -0.560344690289
     H     0.000000000000    -0.801842648150    -0.560344690289
    $end
    
    $rem
        JOB_TYPE = SP
        METHOD = EOM-CCSD
        BASIS = 3-21G
        purecart = 1111
        EOM_IP_ALPHA = [1,0,0,1]
        CC_DO_DYSON = TRUE
        CC_FREE_ELECTRON = 1
        MEM_TOTAL = 4000
    $end
    
    $free_electron
        N_ENERGY_POINTS 10
        N_THETA 25
        N_PHI 10
        SPIN_DEG 2
        ORB_DEG 1
        POL_X 0
        POL_Y 0
        POL_Z 100
        KE_MIN 10
        KE_MAX 1010
    $end
    
    ```

???+ example "示例 7.149: 水分子：在对分子取向进行平均的情况下计算光电离截面与光电子角分布。"
    ```qchem
    $comment
    Calculating photoionization cross-section and PAD
    with averaging over molecular orientations.
    $end
    
    $molecule
     0 1
     O     0.000000000000     0.000000000000    -0.004762594898
     H     0.000000000000     0.801842648150    -0.560344690289
     H     0.000000000000    -0.801842648150    -0.560344690289
    $end
    
    $rem
        JOB_TYPE = SP
        METHOD = EOM-CCSD
        BASIS = 6-31G*
        EOM_IP_ALPHA = [1,0,0,1]
        CC_DO_DYSON = TRUE
        CC_FREE_ELECTRON = 1
        MEM_TOTAL = 4000
    $end
    
    $free_electron
        N_ENERGY_POINTS 10
        N_THETA 25
        N_PHI 10
        SPIN_DEG 2
        ORB_DEG 1
        DO_AVERAGE 1
        KE_MIN 10
        KE_MAX 1010
    $end
    
    ```

???+ example "示例 7.150: 使用 Z 方向偏振光计算水中氧 1s（内层）电子电离的光电离截面。"
    ```qchem
    $comment
    Calculating photoionization cross-sections for the ionization of oxygen 1s (core)
    of water with Z-polarized light.
    $end
    
    $molecule
     0 1
     O     0.000000000000     0.000000000000    -0.004762594898
     H     0.000000000000     0.801842648150    -0.560344690289
     H     0.000000000000    -0.801842648150    -0.560344690289
    $end
    
    $rem
        JOB_TYPE = SP
        METHOD = EOM-CCSD
        BASIS = 3-21G
        purecart = 1111
        CVS_IP_STATES = [1,0,0,0]
        N_FROZEN_CORE = FC
        CC_DO_DYSON = TRUE
        CC_FREE_ELECTRON = 1
        MEM_TOTAL = 4000
    $end
    
    $free_electron
        N_ENERGY_POINTS 10
        N_THETA 25
        N_PHI 10
        SPIN_DEG 2
        ORB_DEG 1
        POL_X 0
        POL_Y 0
        POL_Z 100
        KE_MIN 10
        KE_MAX 1010
    $end
    ```

???+ example "示例 7.151: 使用圆偏振光计算光电离截面、不对称参数与光电子角分布（PAD）。"
    ```qchem
    $comment
    Calculating photoionization cross-section, asymmetry parameter, and
    PAD with a circularly polarized light.
    $end
    
    $molecule
     0 1
    C -0.28956361 0.08176958 0.92701577
    C 1.93885200 -1.15600766 -0.10800484
    C -2.79852375 -0.19094696 -0.27656907
    O 1.53613696 1.47730615 -0.46998636
    H 1.71860882 -2.32670888 -1.80795335
    H 3.52273536 -1.64526642 1.13875511
    H -0.27744501 0.50560530 2.96417187
    H -2.56905279 -0.59002862 -2.30639911
    H -3.89960425 1.56511541 -0.07933409
    H -3.88892566 -1.73605572 0.59599929
    $end
    
    $rem
        JOB_TYPE = SP
        METHOD = EOM-CCSD
        BASIS = 3-21G
        INPUT_BOHR = TRUE
        EOM_IP_ALPHA = [2]
        CC_DO_DYSON = TRUE
        CC_FREE_ELECTRON = 1
        MEM_TOTAL = 4000
    $end
    
    $free_electron
        N_ENERGY_POINTS 10
        N_THETA 15
        N_PHI 10
        SPIN_DEG 2
        ORB_DEG 1
        CIRC_POL 1
        DO_AVERAGE 0
        KE_MIN 10
        KE_MAX 1010
    $end
    ```
