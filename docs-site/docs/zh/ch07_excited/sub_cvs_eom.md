---
title: "7.9.9 核心能级态的 EOM-CC 计算"
---

## 7.9.9 核心能级态的 EOM-CC 计算

（2026 年 7 月 4 日）

芯价层分离（core-valence separation, CVS）方案[[218]](../bib_references/bib.md#bib215)
 使得我们可以将激发态与电离态的标准方法推广至核心能级态。在该方法中，
涉及核心电子的激发与其余组态空间退耦合。这样可以降低计算成本，
并将高度激发的核心态与连续态分离。目前，CVS 已在 EOM-EE/SF/IP-CCSD 中实现，
可用于计算能量和跃迁性质（振子强度、NTO、Dyson 轨道、激子描述符、SOC、ECD 截面）。
CVS-EOM-EE-CCSD 可用于模拟 NEXAFS，而 CVS-EOM-IP-CCSD
可用于模拟 XPS 和 XES。这些方法还可用于计算瞬态吸收光谱，
*e.g.*，泵浦-探测（valence pump/x-ray probe）实验。[[1403]](../bib_references/bib.md#bib1463)

也可以计算非线性光谱，例如 RIXS。L 边光谱（XAS 和 XPS）
可以采用态相互作用（state-interaction）方法来描述，
其中自旋-轨道耦合使用非相对论性 CVS-EOM-EE 态来计算。[[1404]](../bib_references/bib.md#bib1464)
 Auger 光谱可以通过 Feshbach–Fano 方法[[1262]](../bib_references/bib.md#bib1316)
借助 CVS-EOM-EE 计算，既可以结合对连续态的显式处理，也可以使用单中心近似；[[1264]](../bib_references/bib.md#bib1318)

参见第 [7.9.11](sec_Auger.md) 节。

在 **Q-Chem** 中，实现的 CVS-EOM-EE-CCSD 与 Coriani 和 Koch 的原始理论[[269]](../bib_references/bib.md#bib270)
 略有不同：参考耦合簇振幅不包含核心电子。[[1402]](../bib_references/bib.md#bib1462)

为区别于原始方法，[[269]](../bib_references/bib.md#bib270)
 在下文中我们将 **Q-Chem** 的实现称为冻结芯-基态/芯价层分离
EOM（frozen-core-ground-state/core-valence-separated EOM, FC-CVS-EOM）方法。[[1402]](../bib_references/bib.md#bib1462)

在 FC-CVS-EOM 方法中，基态参数（振幅与 Lagrangian 乘子）在冻结芯近似下计算，
而核心激发能和跃迁强度则是通过要求 EOM 激发（及电离）算符中
至少有一个指标对应核心占据轨道来获得。
类似地，在 RIXS 响应态的计算中也强制施加 CVS。[[982]](../bib_references/bib.md#bib1022)

为确保 EOM 方程具有最佳的收敛性，计算是针对能量最高的边
（即最深处的核心轨道）而做“边特定”（*edge-specific*）处理的：
对每一条边分别选择冻结芯空间和 CVS 空间，使得激发态计算中所涉及的核心轨道
在基态计算中被显式冻结，并被专门包含在 EOM 计算中。
下例 [7.9.9.2](#ex:cvsee1) 和 [7.9.9.2](#ex:cvsee1) 说明了这一点。

尽管 FC-CVS-EOM 的收敛性比常规 EOM-CCSD 稳健得多，有时计算仍会坍缩到低能级的
人造态（artificial states）。如果发生这种情况，请使用 CVS_EOM_SHIFT
重新运行计算，以指定边的近似起始能量。

要调用 CVS 方案，请使用 METHOD = CCSD，并用 CVS_EE_STATES
代替 EE_STATES 来指定期望的目标态（类似地，CVS_EE_SINGLETS 和
CVS_EE_TRIPLETS 的用法与常规 EOM 计算完全相同）。对于电离态，
使用 CVS_IP_STATES 或 CVS_IP_ALPHA/CVS_IP_BETA。
自旋翻转（spin-flip）版本可通过 CVS_SF_STATES 启用
（计算 SOC 和 L 边光谱时可能需要）。
可通过 CVS_EOM_PRECONV_SINGLES 调用单激发振幅的预收敛。
跃迁性质和 Dyson 轨道既可以在 CVS 流形内部计算，也可以在 CVS 与价层流形之间计算
（Dyson 轨道的定义见第 [7.9.29](topic_dyson.md) 节）。CVS-EOM-CCSD 仅可在 CCMAN2 下使用。

!!! note "注意"
    (1) 在 CVS-EOM 计算中必须冻结核心电子。核心的精确定义取决于所研究的边，
    因此使用默认值可能并不合适。
    (2) 默认设置（N_FROZEN_CORE = FC）在 QM/MM 计算中不能正确工作。
    应当显式指定冻结核心轨道的数目。


可以为源自特定核心轨道的电离/激发设置自定义的 CVS 计算。为此，首先应使用
*$reorder_mo* 功能对轨道重新排序，使所需的核心轨道出现在列表首位，
然后以 N_FROZEN_CORE = 1 运行 CVS-EOM 计算。

!!! note "注意"
    *$reorder_mo* 仅适用于旧的 SCF 代码（GEN_SCFMAN=FALSE）。


还可以使用关键字 N_FC_CVS_INACTIVE 将冻结芯空间拆分为 CVS 活性与 CVS 非活性子空间，
该关键字将 CVS 活性子空间的大小定义为 N_FROZEN_CORE 减去 N_FC_CVS_INACTIVE。
这些 CVS 活性轨道的排列顺序为：位于价层轨道子空间之前，但排在 CVS 非活性轨道之后
（如有需要，可使用 *$reorder_mo* 节自定义排序）。

### `CVS_EOM_SHIFT`

> **指定 CVS-EOM 计算中的能量平移。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$: 对应 $n\times 10^{-3}$ hartree 的平移量（i.e.，11000 = 11 hartree）；在该值附近求解本征态。
> * **建议**: 可提高计算的稳定性。

### `N_FC_CVS_INACTIVE`

> **冻结芯中 CVS 非活性轨道的数目**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * n, 其中 0: $\leq$
>     * `n`: $\leq$ 冻结芯轨道总数
> * **建议**: 在团簇计算中很有用。

### `CVS_EOM_PRECONV_SINGLES`

> **不为零时，在完整的激发态计算（仅限 CVS 态）之前先收敛单激发向量。设置预收敛过程的最大迭代次数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 不进行预收敛
>     * `1`: 对单激发进行预收敛
> * **建议**: 有时有助于解决收敛困难的问题。

### `CVS_EE_SINGLETS`

> **设置要搜寻的单重态核心激发态根的数目。仅对闭壳层参考有效。**
>
> * **类型**: `INTEGER/INTEGER ARRAY`
> * **默认值**: `0`
> * **选项**:
>     * $[i,j,k\ldots]$: 在第一个不可约表示中搜寻 $i$ 个激发态， 在第二个不可约表示中搜寻 $j$ 个态， 依此类推。
> * **建议**: 无

### `CVS_EE_TRIPLETS`

> **设置要搜寻的三重态核心激发态根的数目。仅对闭壳层参考有效。**
>
> * **类型**: `INTEGER/INTEGER ARRAY`
> * **默认值**: `0`
> * **选项**:
>     * $[i,j,k\ldots]$: 在第一个不可约表示中搜寻 $i$ 个激发态， 在第二个不可约表示中搜寻 $j$ 个态， 依此类推。
> * **建议**: 无

### `CVS_SF_STATES`

> **设置要搜寻的核心能级自旋翻转目标态根的数目。**
>
> * **类型**: `INTEGER/INTEGER ARRAY`
> * **默认值**: `0`
> * **选项**:
>     * $[i,j,k\ldots]$: 在第一个不可约表示中搜寻 $i$ 个 SF 态， 在第二个不可约表示中搜寻 $j$ 个态， 依此类推。
> * **建议**: 无

### `CVS_IP_STATES`

> **设置要搜寻的核心电离态的数目。默认移除 $\beta$ 电子。**
>
> * **类型**: `INTEGER/INTEGER ARRAY`
> * **默认值**: `0`
> * **选项**:
>     * `[i,j,k…]`: 在第一个不可约表示中搜寻 $i$ 个电离态， 在第二个不可约表示中搜寻 $j$ 个态， 依此类推。
> * **建议**: 无

### `CVS_IP_ALPHA`

> **设置通过移除 $\alpha$ 电子（$M_{S}=-\tfrac{1}{2}$）得到的电离目标态的数目。**
>
> * **类型**: `INTEGER/INTEGER ARRAY`
> * **默认值**: `0`
> * **选项**:
>     * $[i,j,k\ldots]$: 在第一个不可约表示中搜寻 $i$ 个电离态， 在第二个不可约表示中搜寻 $j$ 个态， 依此类推。
> * **建议**: 无

### `CVS_IP_BETA`

> **设置通过移除 $\beta$ 电子（$M_{S}=\tfrac{1}{2}$，CVS-IP 的默认选项）得到的电离目标态的数目。**
>
> * **类型**: `INTEGER/INTEGER ARRAY`
> * **默认值**: `0`
> * **选项**:
>     * $[i,j,k\ldots]$: 在第一个不可约表示中搜寻 $i$ 个电离态， 在第二个不可约表示中搜寻 $j$ 个态， 依此类推。
> * **建议**: 无

## 7.9.9.1 RIXS 的 EOM-CC 计算

RIXS 是涉及核心能级态的相干双光子过程。[[982]](../bib_references/bib.md#bib1022)

RIXS 截面的计算需要求解响应方程，其方式与 2PA 截面的计算相同
（见第 [7.9.21.6](sec_EOMGRAD.md#sec:2PA) 节）。
目前，仅能计算 CCSD 参考态与 EOM-CCSD 目标态之间的 RIXS 截面。
由于 RIXS 具有共振特性，需采用阻尼响应理论（damped response theory）
来处理预解算子（resolvent）中的奇点。
此外，对响应向量强制施加 CVS，以消除其与电离连续态的耦合。
要设置 RIXS 计算，需要设定 METHOD = EOM-CCSD，
并使用 EE_STATES 指定要包含的激发态数目（注意只需包含 2PA 亮态），
并通过 CVS_EE_STATES（请求零个态）来激活 CVS。
通过激活 CC_EOM_RIXS 来执行 RIXS 计算。
也可以选择对复 RIXS 单粒子跃迁密度矩阵进行波函数分析（*e.g.*，NTO 分析）。
概念性细节可参见文献 [[980]](../bib_references/bib.md#bib1023)。
最后，可以通过 CC_REF_PROP = 1 请求计算 REXS（“弹性”峰截面）
（默认情况下不计算 REXS）。
此功能仅在 fc-CVS-EOM-EE-CCSD 中可用。

### `CC_EOM_RIXS`

> **是否计算 RIXS 散射矩和截面。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `1`: 在 fc-CVS-EOM-EE-CCSD 中执行 RIXS，仅使用 CCSD 参考态的响应波函数
>     * `2`: 在 fc-CVS-EOM-EE-CCSD 响应理论中执行 RIXS，并对 RIXS 跃迁密度矩阵进行波函数分析
>     * `11`: 在标准 EOM-EE-CCSD 中执行 RIXS，仅使用 CCSD 参考态的响应波函数
>     * `12`: 在标准 EOM-EE-CCSD 的 RIXS 响应计算中使用 $\sigma$ 中间量
> * **建议**: 使用 1 以启用具有稳健收敛性的 fc-CVS-EOM-EE-CCSD

!!! note "注意"
    由于 EOM-EE-CCSD 中的 RIXS 响应解经常无法收敛，推荐使用 CC_EOM_RIXS = 1
    的 fc-CVS-EOM-EE-CCSD RIXS 计算以获得顺畅的收敛。其他所有选项均为实验性质。


要指定泵浦频率和阻尼因子 $\epsilon$，请使用 *$rixs* 节：

> ```qchem
> $rixs
> damped_epsilon 0.005       Damping factor in hartree.
> omega_1 2306503 500 10 0   Pumping frequencies: starting w (cm-1), increment (cm-1),
>                            number of frequency points, algo (always 0 for now)
> omega_2 2200000 600 20 0   Emitted frequencies:  starting w (cm-1), increment (cm-1),
>                            number of frequency points, algo (always 0 for now)
> $end
> ```

阻尼因子（DAMPED_EPSILON）以原子单位指定（0.005 是不错的选择）。
OMEGA_1 指定起始泵浦频率（单位 cm${}^{-1}$）、频率扫描的增量（单位 cm${}^{-1}$）、
频率点数目以及响应方程的算法（目前一律使用零）。
OMEGA_2 仅应在生成二维 RIXS 扫描时指定。
例 [7.9.9.2](#ex:cvsee1) 说明了 RIXS 计算的设置方式。

默认情况下，阻尼 RIXS 响应波函数采用一种新的、类似 Davidson 的迭代子空间方法
来计算，即 **Dalton** 求解器。[[248]](../bib_references/bib.md#bib251)

它由 DALTON_XCONV、DALTON_PRECOND_START、
DALTON_MAXITER 和 DALTON_MAXSPACE 关键字控制。
阻尼 RIXS 响应波函数也可以使用较旧的 DIIS 流程计算，
方法是设置 DAMPED_DALTON_SOLVER = FALSE。
DIIS 求解器由 CC_MAX_ITER、CC_DIIS_START、
CC_DIIS_SIZE、CC_EOM_2PA_ECONV 和
CC_EOM_2PA_XCONV 控制。

!!! note "注意"
    - 为获得 DIIS 求解器下响应方程更好的收敛性，
    请增大 CC_DIIS_SIZE（推荐 25）并考虑使用更大的阻尼因子。

    - **Dalton** 求解器在估计收敛时使用残差范数的平方（与 Davidson 求解器相同），
    而 DIIS 求解器使用的是相邻迭代之间响应向量之差的范数。


## 7.9.9.2 示例

以下示例说明如何执行这些计算。

- 例 [7.9.9.2](#ex:cvsee1)：在 CCSD 计算中冻结氧原子上的 $1s$ 轨道
（N_FROZEN_CORE = FC）。在 EOM 计算中调用 CVS 近似（CVS_EE_SINGLETS），
从而将核心激发能作为最低激发获得。通过选择 CC_TRANS_PROP = 1
激活振子强度和旋转强度的计算，并通过 STATE_ANALYSIS = TRUE
调用 **libwfa** 分析（见第 [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) 节）。
注意，对于非手性体系，旋转强度为零。
- 例 [7.9.9.2](#ex:cvsee1)：在双边分子（一氧化碳）中进行 CVS-EOM-EE-CCSD 计算。
在当前实现中，应针对每一条边分别进行计算。第一个作业计算碳边态。
由于碳的 $1s$ 轨道在能量上最高（在该分子的核心 $1s$ 轨道中），
C 边的输入与例 [7.9.9.2](#ex:cvsee1) 类似。在参考 CCSD 计算中，
氧和碳的 $1s$ 轨道均被冻结。在 EOM 部分，碳核心激发态被自动选取。
在这种情况下，使用默认冻结芯设置（N_FROZEN_CORE = FC）
等价于指定 N_FROZEN_CORE = 2。在第二个输入中，计算氧边。
由于氧的核心轨道位置更深，冻结芯与 CVS 的选择通过采用更小的芯来
专门针对氧边。氧原子的 1$s$ 轨道通过 N_FROZEN_CORE = 1 选取。
若分子还有其他边，则应通过适当的 N_FROZEN_CORE 值，
选取最深的核心轨道，直至并包括所研究边的轨道。
- 例 [7.9.9.2](#ex:cvsee1)：利用放置在氮原子上的附加 Rydberg 函数组计算氨的 XAS 光谱；
Rydberg 函数的指数按 Kaufmann 的配方[[672]](../bib_references/bib.md#bib696)
生成。
注意，使用虚原子（ghost atoms）时对称性会被关闭。可通过 FORCE_SYMMETRY_ON
关键字强制开启对称性。
 alternatively，此计算也可以通过向所有（或所选）原子添加采用偶数 tempered 指数的
附加弥散函数来设置。用户必须确保虚原子不会降低对称性。
- 例 [7.9.9.2](#ex:cvsee1)：计算苯的 XES 光谱。
- 例 [7.9.9.2](#ex:cvsee1) 和 [7.9.9.2](#ex:cvsee1)：分别计算核心激发态与核心电离态之间、
以及核心激发态与价电离态之间的 Dyson 轨道。
- 例 [7.9.9.2](#ex:cvsee1)：RIXS 计算的设置。

采用态相互作用方法[[1404]](../bib_references/bib.md#bib1464)
计算 L 边光谱需要两步流程。首先，**Q-Chem** 计算所需的 CVS-EOM 态和 SOC。
在第二步中，由后处理脚本计算受自旋-轨道微扰的光谱。脚本、详细说明和
示例参见其他资料。

???+ example "例 7.70: 在水的氧边用 FC-CVS-EOM-EE-CCSD 计算前六个允许的电偶极核心激发能及其强度。同时执行波函数分析。"
    ```qchem
    $molecule
       0 1
       O    0.0000   0.0000   0.1173
       H    0.0000   0.7572  -0.4692
       H    0.0000  -0.7572  -0.4692
    $end
    
    $rem
       METHOD              = eom-ccsd
       BASIS               = aug-cc-pVDZ
       CVS_EE_SINGLETS     = [3,0,2,1]
       N_FROZEN_CORE       = fc
       CC_TRANS_PROP       = true
       EOM_PRECONV_SINGLES = true
       STATE_ANALYSIS      = true !invoke libwa to compute NTOs and exciton descriptors
       MOLDEN_FORMAT       = true
       NTO_PAIRS           = 3
       POP_MULLIKEN        = true
    $end
    ```

???+ example "例 7.71: 在一氧化碳的 (1) 碳边和 (2) 氧边，用 FC-CVS-EOM-EE-CCSD 计算每个不可约表示中前两个允许的电偶极核心激发能及其强度。"
    ```qchem
    $molecule
       0 1
       O    0.0000   0.0000    0.913973
       C    0.0000   0.0000   -1.218243
    $end
    
    $rem
       METHOD               =  eom-ccsd
       BASIS                =  aug-cc-pVDZ
       INPUT_BOHR           =  true
       CVS_EE_SINGLETS      =  [2,0,2,2]
       N_FROZEN_CORE        =  fc            !For C K-edge
       EOM_PRECONV_SINGLES  =  true
       CC_TRANS_PROP        =  true
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD               =  eom-ccsd
       BASIS                =  aug-cc-pVDZ
       CVS_EE_SINGLETS      =  [2,0,2,2]
       N_FROZEN_CORE        =  1             !For O K-edge
       EOM_PRECONV_SINGLES  =  true
       CC_TRANS_PROP        =  true
    $end
    ```

???+ example "例 7.7.72: 利用放置在虚原子上的附加 Rydberg 函数计算氨的 XAS 光谱。"
    ```qchem
    $comment
    NEXAFS AMMONIA / 6-311++G**+Rydberg functions
    Optimized geometry: NH3_opt_coord.out
    $end
    
    $molecule
    0 1
    N      -0.0002568808    -0.2210075702    -0.0000000021
    H       0.8838383819     0.5154343604     1.5287018716
    H      -1.7658867303     0.5161842661     0.0000000000
    H       0.8838383819     0.5154343604    -1.5287018716
    Gh      0.0000000000     0.0000000000     0.0000000000
    $end
    
    $rem
        input_bohr = true
        jobtype = sp
        method = eom-ccsd
        cvs_ee_singlets    [5,5]
        basis = general    !User-defined basis to add extra Rydberg functions
        n_frozen_core = fc
        cc_trans_prop = true
        eom_preconv_singles = true
        eom_davidson_convergence = 4
        eom_shift = 14760
        FORCE_SYMMETRY_ON = true   Forces symmetry to be turned on
        MEM_TOTAL 30000   30GB of total memory
    $end
    
    $basis
    N    0
    6-311++G*
    ****
    H    0
    6-311++G*
    ****
    Gh   0
    S   1   1.00
            0.0112533427        1.0000000000
    S   1   1.00
            0.0058583805        1.0000000000
    S   1   1.00
            0.0033459739        1.0000000000
    S   1   1.00
            0.0020484225        1.0000000000
    S   1   1.00
            0.0013236424        1.0000000000
    P   1   1.00
            0.0192542060        1.0000000000
    P   1   1.00
            0.0099882106        1.0000000000
    P   1   1.00
            0.0056893607        1.0000000000
    P   1   1.00
            0.0034756797        1.0000000000
    P   1   1.00
            0.0022420590        1.0000000000
    D   1   1.00
            0.0274456919        1.0000000000
    D   1   1.00
            0.0142043987        1.0000000000
    D   1   1.00
            0.0080765930        1.0000000000
    D   1   1.00
            0.0049271863        1.0000000000
    D   1   1.00
            0.0031748110        1.0000000000
    ****
    $end
    
    ```

???+ example "例 7.73: 计算苯的 XES 光谱"
    ```qchem
    $comment
    RI-MP2/cc-pVTZ optimized geometry. XES calculation.
    $end
    
    $molecule
    0 1
        H         2.4750347531    0.0000000000    0.0000000000
        C         1.3935929418    0.0000000000    0.0000000000
        C         0.6967964709    1.2068868901    0.0000000000
        H         1.2375173766    2.1434429715    0.0000000000
        C        -0.6967964709    1.2068868901    0.0000000000
        H        -1.2375173766    2.1434429715    0.0000000000
        C        -1.3935929418    0.0000000000    0.0000000000
        H        -2.4750347531    0.0000000000    0.0000000000
        C        -0.6967964709   -1.2068868901    0.0000000000
        H        -1.2375173766   -2.1434429715    0.0000000000
        C         0.6967964709   -1.2068868901    0.0000000000
        H         1.2375173766   -2.1434429715    0.0000000000
    $end
    
    $rem
       BASIS         =  6-31G*
       METHOD        =  eom-ccsd
       IP_STATES     = [3,2,1,1,0,1,2,2] !All valence Koompans-like ionized states
                                         !except for 3 lowest ones
       CVS_IP_STATES = [2,1,0,0,0,0,1,2] !All core-ionized states
       CC_TRANS_PROP = 2 !Compute transitions between all pairs of EOM states
       CC_MEMORY     = 8000  !8 GB
    $end
    ```

???+ example "例 7.74: 计算 FC-CVS-EOM-EE-CCSD 与 FC-CVS-EOM-IP-CCSD 流形之间的 Dyson 轨道。"
    ```qchem
    $comment
       CVS-IP/CVS-EE Dyson orbitals, formaldehyde
    $end
    
    $molecule
       0 1
       C
       H   1  1.096135
       H   1  1.096135  2  116.191164
       O   1  1.207459  2  121.904418  3  -180.000000  0
    $end
    
    $rem
       METHOD           =  eom-ccsd
       BASIS            =  cc-pVDZ   ! Please do not use BASIS2
       SCF_CONVERGENCE  =  8
       CVS_IP_STATES    =  [1,0,0,0]
       CVS_EE_STATES    =  [1,0,1,0]
       CC_DO_DYSON      =  true
       CC_TRANS_PROP    =  2 !Compute all EOM-to-EOM transitions
    $end
    ```

???+ example "例 7.75: 计算 FC-CVS-EOM-EE-CCSD 与 EOM-IP-CCSD 流形之间的 Dyson 轨道。"
    ```qchem
    $comment
       IP/CVS-EE Dyson orbitals, formaldehyde
    $end
    
    $molecule
       0 1
       C
       H  1  1.096135
       H  1  1.096135  2  116.191164
       O  1  1.207459  2  121.904418  3  -180.000000  0
    $end
    
    $rem
       METHOD           =  eom-ccsd
       BASIS            =  cc-pVDZ
       SCF_CONVERGENCE  =  8
       IP_STATES        =  [1,0,0,0]   ! Valence a1 hole
       CVS_EE_STATES    =  [1,0,0,0]
       CC_DO_DYSON      =  true
       CC_TRANS_PROP    =  2 !Compute all EOM-to-EOM transitions
    $end
    ```

???+ example "例 7.76: 计算 FC-CVS-EOM-EE-CCSD 与 FC-CVS-EOM-IP-CCSD 流形之间的 Dyson 轨道。"
    ```qchem
    $comment
    CVS-IP/CVS-EE Dyson orbitals, formaldehyde
    $end
    
    $molecule
       0 1
       C
       H  1  1.096135
       H  1  1.096135  2  116.191164
       O  1  1.207459  2  121.904418  3  -180.000000  0
    $end
    
    $rem
       BASIS           =  cc-pVDZ
       SCF_CONVERGENCE = 8
       METHOD          = eom-ccsd
       IP_STATES       = [1,0,0,0]   ! Valence a1 hole
       CVS_EE_STATES   = [1,0,0,0]
       CC_DO_DYSON     = true
       CC_TRANS_PROP   = true        ! required to activate a Dyson orbitals job
    $end
    ```

???+ example "例 7.77: 计算苯的 RIXS/REXS（每个 2PA 活性不可约表示 10 个激发态）"
    ```qchem
    $comment
    RI-MP2/cc-pVTZ optimized geometry.
    Pump XAS transition peak A at 285.97 eV, only one frequency point.
    $end
    
    $molecule
       0 1
       H      2.4750347531    0.0000000000    0.0000000000
       C      1.3935929418    0.0000000000    0.0000000000
       C      0.6967964709    1.2068868901    0.0000000000
       H      1.2375173766    2.1434429715    0.0000000000
       C     -0.6967964709    1.2068868901    0.0000000000
       H     -1.2375173766    2.1434429715    0.0000000000
       C     -1.3935929418    0.0000000000    0.0000000000
       H     -2.4750347531    0.0000000000    0.0000000000
       C     -0.6967964709   -1.2068868901    0.0000000000
       H     -1.2375173766   -2.1434429715    0.0000000000
       C      0.6967964709   -1.2068868901    0.0000000000
       H      1.2375173766   -2.1434429715    0.0000000000
    $end
    
    $rem
       BASIS         = 6-31(+,+)G**
       METHOD        = eom-ccsd
       CVS_EE_STATES = [0,0,0,0,0,0,0,0]       just to invoke CVS
       EE_STATES     = [10,10,10,10,0,0,0,0]   10 states in each 2PA active irrep
       CC_REF_PROP   = 1     ! Calculate REXS in addition to RIXS
       CC_EOM_RIXS   = 1     ! Activate RIXS calculation using fc-CVS-EOM-EE-CCSD
       CC_DIIS_SIZE  = 25    ! Use for better convergence of response equations
       CC_MEMORY     = 8000  !8 GB
       mem_total = 8500
    $end
    
    $rixs
       omega_1         2306503 500 1 0
       damped_epsilon  0.005
    $end
    ```

???+ example "例 7.78: 对一个水二聚体进行 FC-CVS-EOM-EE-CCSD 和 FC-CVS-EOM-IP-CCSD 计算，核心激发与电离源自能量最低的核心轨道，另一个核心轨道保持为 CVS 非活性。第一个输入对分子轨道重新排序。第二个输入在计算核心能级态和性质之前定义 CVS 活性与非活性轨道。"
    ```qchem
    $molecule
    0 1
              O      -4.9920582819    -0.1246131900     2.2067549109
              H      -5.5873205924    -0.9397949066     2.3252790559
              H      -4.9827539950     0.0559440223     1.1016406903
              O      -6.5474306925    -1.1803213469    -1.0374284134
              H      -5.7367207770    -0.6839235793    -0.7295169422
              H      -6.2716956294    -2.1185636950    -1.1190969125
    $end
    
    $rem
       GEN_SCFMAN = false
       use_libqints = true
       CC_MEMORY = 4000
       MEM_STATIC = 600
       BASIS  =  6-31g
       METHOD  =  hf
       n_frozen_core = 0
       thresh =  14          Does not converge with defaults
       scf_algorithm gdm     Does not converge with defaults
    $end
    
    $reorder_mo
    2 1 3
    2 1 3
    $end
    
    @@@
    
    $molecule
    0 1
              O      -4.9920582819    -0.1246131900     2.2067549109
              H      -5.5873205924    -0.9397949066     2.3252790559
              H      -4.9827539950     0.0559440223     1.1016406903
              O      -6.5474306925    -1.1803213469    -1.0374284134
              H      -5.7367207770    -0.6839235793    -0.7295169422
              H      -6.2716956294    -2.1185636950    -1.1190969125
    $end
    
    $rem
       CC_MEMORY = 4000
       MEM_STATIC = 600
       BASIS  =  6-31g
       METHOD  =  hf
       n_frozen_core = 0
       thresh =  14          Does not converge with defaults
       scf_algorithm gdm     Does not converge with defaults
    $end
    ```
