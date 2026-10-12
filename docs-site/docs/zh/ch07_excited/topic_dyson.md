---
title: "7.9.29 EOM-CCSD 框架下电离态或附着态的戴森轨道（Dyson Orbitals）"
---

## 7.9.29 EOM-CCSD 框架下电离态或附着态的戴森轨道（Dyson Orbitals）

(July 4, 2026)

戴森轨道（Dyson orbitals）可用于计算总光脱附/光电离截面（cross-sections），以及光电子的角分布。戴森轨道是 N 电子分子波函数与相应阳离子/阴离子的 $N-1$/$N+1$ 电子波函数之间的重叠：

<a id="A3.S8.EGx60"></a>

$$
\displaystyle\phi^{d}(1) \tag{7.127}
$$

对于 Hartree-Fock 波函数，在 Koopmans 近似（Koopmans’ approximation）下，这些轨道就是正则 HF 轨道。对于关联波函数，戴森轨道是参考分子轨道（molecular orbitals）的线性组合：

<a id="A3.S8.EGx61"></a>

$$
\displaystyle\phi^{d} \tag{7.129}
$$

在 EOM-IP/EA-CCSD 方法中，戴森轨道的计算非常直接，因为阳离子/阴离子态与初始分子态都是基于同一套分子轨道（MO）基组定义的。由于左 CC 向量和右 CC 向量并不相同，相应地可以定义两个戴森轨道（左戴森轨道和右戴森轨道）：

<a id="A3.S8.EGx62"></a>

$$
\displaystyle\begin{aligned} \displaystyle\gamma_{p}^{R}&\displaystyle=\bigl{\langle}\Phi_{0}e^{T_{1}+T_{2}}L^{EE}\bigl{|}p^{\dagger}\bigr{|}R^{IP}e^{T_{1}+T_{2}}\Phi_{0}\bigr{\rangle}\\
\displaystyle\gamma_{p}^{L}&\displaystyle=\bigl{\langle}\Phi_{0}e^{T_{1}+T_{2}}L^{IP}\bigl{|}p\bigr{|}R^{EE}e^{T_{1}+T_{2}}\Phi_{0}\bigr{\rangle}\end{aligned} \tag{7.132}
$$

这些轨道的模长正比于跃迁的单电子特征（one-electron character）。

戴森轨道还可以通过可视化分子态与电离态/附着态之间的差异，提供定性的洞察。在电离/光脱附过程中，这些轨道也可以被解释为逸出电子的波函数。更多细节参见参考文献 [[1002]](../bib_references/bib.md#bib1043)
 和 [[1003]](../bib_references/bib.md#bib1044)
。利用独立的 **ezDyson** 代码 [[478]](../bib_references/bib.md#bib490)
 或 **Q-Chem** 内置功能（见第 [7.9.21.10](sec_EOMGRAD.md#sec:freeEl) 节），可以使用戴森轨道计算总光电子截面和微分光电子截面。

戴森轨道既可以针对价层态（valence states）计算，也可以针对核心能级态（core-level states）计算；[[1403]](../bib_references/bib.md#bib1463)

关于在 FC-CVS-EOM 框架下计算戴森轨道，参见第 [7.9.9](sub_cvs_eom.md) 节。

ezSpectra 套件：一个易于使用的光谱学建模工具包 —— 由佐治亚州立大学（Georgia State University）Samer Gozem 教授呈现

**Q-Chem** 还可以利用 DYSON_PW_COUPLING 关键字计算戴森轨道与平面波的重叠 $\langle\phi^{d}|e^{i{\mathbf{k}r}}\rangle$。
用户可以请求计算多个 $|{\mathbf{k}}|$ 值下的重叠，并可以选择对 ${\mathbf{k}}$ 方向进行平均，或者针对 ${\mathbf{k}}$ 的固定方向进行计算。
该功能通过示例 [7.9.29.2](#ex:DYSONPW) 和 [7.9.29.2](#ex:DYSONPW)
 加以说明，并在第 [7.9.21.10](sec_EOMGRAD.md#sec:freeEl) 节中详细解释。

## 7.9.29.1 戴森轨道的作业控制（Job Control）

戴森轨道的计算已实现，适用于从基态（参考态）和激发态出发的电离/电子附着。要获得基态戴森轨道，需要运行一次 EOM-IP/EA-CCSD 计算，并通过设置 CC_TRANS_PROP =
TRUE 和 CC_DO_DYSON = TRUE 来请求跃迁性质（transition properties）的计算。戴森轨道在 MO 基组下的分解会打印在输出文件中，涵盖参考态与所有 IP/EA 态之间的全部跃迁。在文件末尾，还可以获得戴森轨道在 AO 基组下的系数。

目前有两种戴森轨道的实现方式：(i) CCMAN 中的原始实现；(ii) CCMAN2 中的新实现。CCMAN
实现使用弥散轨道技巧（diffuse orbital trick）（*i.e.*，在这些计算中 EOM_FAKE_IPEA 将被自动设置为
TRUE）。注意：该实现存在一个影响戴森轨道模长数值的 bug（轨道的形状是正确的）；因此强烈不建议使用该代码。CCMAN2
实现支持所有类型的初始态：来自基态 CC、激发态 EOM-EE 以及自旋翻转（spin-flip）EOM-SF 态的戴森轨道；它与 EOM 计算的所有辅助功能完全兼容，例如 FNO、RI、Cholesky 分解。CCMAN2
实现可以使用用户指定的 EOM 初猜（通过 EOM_USER_GUESS 关键字和
*$eom_user_guess* 节），对于高度激发态（例如核心电离态）推荐使用此功能。此外，CCMAN2 还能计算涉及亚稳态（meta-stable states，见第 [7.9.10](sub_cc_cs_cap.md) 节）和核心能级态（见第 [7.9.9](sub_cvs_eom.md) 节）的戴森轨道。

若要计算从参考组态以及激发态或自旋翻转态到 IP/EA 态的戴森轨道，需要在常规的 EOM-IP/EA-CCSD 与 EOM-EE-CCSD 或 EOM-SF-CCSD
计算组合的基础上，添加相同的 CC_TRANS_PROP =
TRUE 和 CC_DO_DYSON = TRUE 关键字。（不过，请注意 CCMAN 有关键字 CC_DO_DYSON_EE =
TRUE。）IP_STATES 关键字用于指定目标电离态。附着态由
EA_STATES 指定。EA-SF 态由 EOM_EA_BETA 指定。
激发态（或自旋翻转态）由 EE_STATES 和 SF_STATES 指定。每个 EE/SF-IP/EA
态对的戴森轨道在 MO 和 AO 基组下的分解会先针对参考态打印，然后按以下顺序针对所有激发态打印：CC-IP/EA1, CC-IP/EA2,$\ldots$,
EE/SF1 - IP/EA1, EE/SF1 - IP/EA2,$\ldots$, EE/SF2
- IP/EA1, EE/SF2 - IP/EA2,$\ldots$，依此类推。CCMAN
实现会将参考态跃迁单独保留，以与相应关键字的划分保持一致。

### `CC_DO_DYSON`

> **CCMAN2: 启动所有类型的戴森轨道计算。期望的类型通过请求相应的 EOM-XX 跃迁来确定。 CCMAN: 对于 EOM-IP/EA-CCSD 计算，是否计算参考态的戴森轨道。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE （必须指定该选项才能运行此计算）`
> * **选项**:
>     * `TRUE/FALSE`
> * **建议**: 无

### `CC_DO_DYSON_EE`

> **对于使用 CCMAN 的 EOM-IP/EA-CCSD 计算，是否计算激发态或自旋翻转态的戴森轨道。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE （必须指定该选项才能运行此计算）`
> * **选项**:
>     * `TRUE/FALSE`
> * **建议**: 无

设置 IQMOL_FCHK =
TRUE（等价地，GUI = 2）并将生成的检查点文件（checkpoint file）读入 **IQmol**，是最简便的戴森轨道可视化方式。除了正则轨道之外，戴森轨道会出现在模型视图（Model View）的 Surfaces 项下。分步操作说明参见 **ezDyson** 手册。

或者，也可以使用 IANLTY = 200 和
*$plots* 工具绘制戴森轨道。只需指定网格盒（box）的尺寸，然后跟一行零即可：

> ```qchem
> $plots
>    comment
>    10   -2   2
>    10   -2   2
>    10   -2   2
>    0     0   0    0
> $plots
> ```

笛卡尔网格上的所有戴森轨道将写入生成的
`plot.mo` 文件（仅 CCMAN）。对于 RHF(UHF) 参考，`plot.mo`
中的列顺序为：
$\phi^{lr}_{1}\alpha\ (\phi^{lr}_{1}\beta)\ \phi^{rl}_{1}\alpha\ (\phi^{rl}_{1}\beta)\ \phi^{lr}_{2}\alpha\ (\phi^{lr}_{2}\beta)\ \ldots$

此外，将 MAKE_CUBE_FILES 关键字设置为 TRUE 会为戴森轨道创建 cube 文件，可用
Visual Molecular Dynamics (VMD)[[W. Humphrey, A. Dalke, and K. Schulten (1996)]](../bib_references/bib.md#bib627)
或其他程序查看；详情参见第 [10.5.5](../ch10_properties/sec_cubefiles.md) 节。该选项对 CCMAN 和 CCMAN2
均可用。戴森轨道将按 $\phi^{lr}_{1}\ \phi^{rl}_{1}\ \ \phi^{lr}_{2}\ \phi^{rl}_{2}\ldots$ 的顺序写入文件 `mo.1.cube`、
`mo.2.cube`、$\ldots$。对于亚稳态，戴森轨道的实部和虚部按以下顺序分别写入不同的文件
$\text{Re}(\phi^{lr}_{1})\ \text{Re}(\phi^{rl}_{1})\ \ \text{Re}(\phi^{lr}_{2})\ \text{Re}(\phi^{rl}_{2})\ldots\text{Im}(\phi^{lr}_{1})\ \text{Im}(\phi^{rl}_{1})\ \ \text{Im}(\phi^{lr}_{2})\ \text{Im}(\phi^{rl}_{2})\ldots$

!!! note "注意"
    通过 **MolDen** 格式进行可视化不可用。


## 7.9.29.2 示例

???+ example "示例 7.166: 绘制氧分子电离过程中 grd-ex 与 ex-grd 态之间的戴森轨道。阳离子的目标态为 ${}^{2}$ A ${}_{g}$ 和 ${}^{2}$ B ${}_{2u}$ 。仅适用于 CCMAN。"
    ```qchem
    $molecule
       0 3
       O    0.000  0.000  0.000
       O    1.222  0.000  0.000
    $end
    
    $rem
       BASIS          6-31G*
       METHOD         eom-ccsd
       IP_STATES      [1,0,0,0,0,0,1,0] Target EOM-IP states
       CC_TRANS_PROP  true  request transition OPDMs to be calculated
       CC_DO_DYSON    true  calculate Dyson orbitals
       IANLTY         200
    $end
    
    $plots
    plots excited states densities and trans densities
       10   -2   2
       10   -2   2
       10   -2   2
       0     0   0    0
    $plots
    ```

???+ example "示例 7.167: 绘制 HO 自由基第 1 个 ${}^{2}A_{1}$ 激发态与 HO ${}^{-}$ 的第 1 个 A ${}_{1}$ 和 A ${}_{2}$ 激发态之间的 ex-ex 态戴森轨道。仅适用于 CCMAN。"
    ```qchem
    $molecule
       -1 1
       H    0.000   0.000  0.000
       O    1.000   0.000  0.000
    $end
    
    $rem
       METHOD             eom-ccsd
       BASIS              6-31G*
       IP_STATES          [1,0,0,0]  states of HO radical
       EE_STATES          [1,1,0,0]  excited states of HO-
       CC_TRANS_PROP      2          calculate transition properties
       CC_DO_DYSON        true       calculate Dyson orbitals for ionization from ex. states
       IANLTY             200
    $end
    
    $plots
    plot excited states densities and trans densities
       10   -2   2
       10   -2   2
       10   -2   2
       0     0   0    0
    $plots
    ```

???+ example "示例 7.168: CO 分子电离的戴森轨道；请求 A ${}_{1}$ 和 B ${}_{1}$ 电离态。"
    ```qchem
    $molecule
       0 1
       O
       C  O  1.131
    $end
    
    $rem
       CORRELATION           CCSD
       BASIS                 cc-pVDZ
       PURECART              111        5d, will be required for ezDyson
       IP_STATES             [1,0,1,0]  (A1,A2,B1,B2)
       CCMAN2                true
       CC_DO_DYSON           true
       CC_TRANS_PROP         true       necessary for Dyson orbitals job
       PRINT_GENERAL_BASIS   true       will be required for ezDyson
    $end
    ```

???+ example "示例 7.169: H ${}_{2}$ O 电离的戴森轨道；请求核心（A ${}_{1}$ ）态 — 从 O(1s) 电离。"
    ```qchem
    $molecule
       0 1
       O
       H1  O  0.955
       H2  O  0.955  H1  104.5
    $end
    
    $rem
       CORRELATION           CCSD
       BASIS                 cc-pVTZ
       PURECART              111        5d, will be required for ezDyson
       IP_STATES             [1,0,0,0]  (A1,A2,B1,B2)
       EOM_USER_GUESS        1          on, further defined in $eom_user_guess
       CCMAN2                true
       CC_DO_DYSON           true
       CC_TRANS_PROP         true       necessary for Dyson orbitals job
       PRINT_GENERAL_BASIS   true       will be required for ezDyson
       N_FROZEN_CORE         false
    $end
    
    $eom_user_guess
       1
    $end
    ```

???+ example "示例 7.170: 使用 EOM-EA 和闭壳层阳离子参考计算 NO 分子电离的戴森轨道；请求 A ${}_{1}$ 和 B ${}_{2}$ 态。"
    ```qchem
    $molecule
       +1 1
       N   0.00000  0.00000  0.00000
       O   0.00000  0.00000  1.02286
    $end
    
    $rem
       CORRELATION            CCSD
       BASIS                  aug-cc-pVTZ
       PURECART               111       5d, will be required for ezDyson
       EA_STATES              [1,0,0,1] (A1,A2,B1,B2)
       CCMAN2                 true
       CC_DO_DYSON            true
       CC_TRANS_PROP          true      necessary for Dyson orbitals job
       PRINT_GENERAL_BASIS    true      will be required for ezDyson
    $end
    ```

???+ example "示例 7.7.171: 从 N ${}_{2}^{-}$ 的亚稳态 ${}^{2}\Pi_{g}$ 脱附的戴森轨道。"
    ```qchem
    $molecule
       0 1
       N   0.0   0.0    0.55
       N   0.0   0.0   -0.55
       GH  0.0   0.0    0.0
    $end
    
    $rem
       METHOD            EOM-CCSD
       EA_STATES         [0,0,2,0,0,0,0,0]
       CC_MEMORY         5000
       MEM_STATIC        1000
       BASIS             GEN
       COMPLEX_CCMAN     TRUE
       CC_TRANS_PROP     TRUE
       CC_DO_DYSON       TRUE
       MAKE_CUBE_FILES   TRUE
       IANLTY            200
       FORCE_SYMMETRY_ON TRUE
    $end
    
    $complex_ccman
       CS_HF             1
       CAP_TYPE          1
       CAP_X             2760
       CAP_Y             2760
       CAP_Z             4880
       CAP_ETA           400
    $end
    
    $plots
    plot Dyson orbitals
       50 -10.0 10.0
       50 -10.0 10.0
       50 -10.0 10.0
       0 0 0 0
    $end
    
    $basis
    N    0
    S    8    1.000000
       1.14200000E+04    5.23000000E-04
       1.71200000E+03    4.04500000E-03
       3.89300000E+02    2.07750000E-02
       1.10000000E+02    8.07270000E-02
       3.55700000E+01    2.33074000E-01
       1.25400000E+01    4.33501000E-01
       4.64400000E+00    3.47472000E-01
       5.11800000E-01   -8.50800000E-03
    S    8    1.000000
       1.14200000E+04   -1.15000000E-04
       1.71200000E+03   -8.95000000E-04
       3.89300000E+02   -4.62400000E-03
       1.10000000E+02   -1.85280000E-02
       3.55700000E+01   -5.73390000E-02
       1.25400000E+01   -1.32076000E-01
       4.64400000E+00   -1.72510000E-01
       5.11800000E-01    5.99944000E-01
    S    1    1.000000
       1.29300000E+00    1.00000000E+00
    S    1    1.000000
       1.78700000E-01    1.00000000E+00
    P    3    1.000000
       2.66300000E+01    1.46700000E-02
       5.94800000E+00    9.17640000E-02
       1.74200000E+00    2.98683000E-01
    P    1    1.000000
       5.55000000E-01    1.00000000E+00
    P    1    1.000000
       1.72500000E-01    1.00000000E+00
    D    1    1.000000
       1.65400000E+00    1.00000000E+00
    D    1    1.000000
       4.69000000E-01    1.00000000E+00
    F    1    1.000000
       1.09300000E+00    1.00000000E+00
    S    1    1.000000
       5.76000000E-02    1.00000000E+00
    P    1    1.000000
       4.91000000E-02    1.00000000E+00
    D    1    1.000000
       1.51000000E-01    1.00000000E+00
    F    1    1.000000
       3.64000000E-01    1.00000000E+00
    ****
    GH   0
    S    1    1.000000
       2.88000000E-02    1.00000000E+00
    S    1    1.000000
       1.44000000E-02    1.00000000E+00
    S    1    1.000000
       0.72000000E-02    1.00000000E+00
    S    1    1.000000
       0.36000000E-02    1.00000000E+00
    S    1    1.000000
       0.18000000E-02    1.00000000E+00
    S    1    1.000000
       0.09000000E-02    1.00000000E+00
    P    1    1.000000
       2.45000000E-02    1.00000000E+00
    P    1    1.000000
       1.22000000E-02    1.00000000E+00
    P    1    1.000000
       0.61000000E-02    1.00000000E+00
    P    1    1.000000
       0.305000000E-02    1.00000000E+00
    P    1    1.000000
       0.152500000E-02    1.00000000E+00
    P    1    1.000000
       0.076250000E-02    1.00000000E+00
    D    1    1.000000
       0.755000000E-01    1.00000000E+00
    D    1    1.000000
       0.377500000E-01    1.00000000E+00
    D    1    1.000000
       0.188750000E-01    1.00000000E+00
    D    1    1.000000
       0.094375000E-01    1.00000000E+00
    D    1    1.000000
       0.047187500E-01    1.00000000E+00
    D    1    1.000000
       0.023593750E-01    1.00000000E+00
    ****
    $end
    ```

???+ example "示例 7.172: 在相对于平衡 O ${}_{2}$ 几何略有拉伸的结构下，三重态 O ${}_{2}$ 和 O ${}_{2}^{-}$ 电离的戴森轨道；请求 B ${}_{3g}$ 态。"
    ```qchem
    $comment
       EOM-IP-CCSD/6-311+G* and EOM-EA-CCSD/6-311+G* levels of theory,
       UHF reference.  Start from O2:
        1) detach electron - ionization of neutral (alpha IP).
        2) attach electron, use EOM-EA w.f. as initial state
           - ionization of anion (beta EA).
    $end
    
    $molecule
       0 3
       O   0.00000  0.00000  0.00000
       O   0.00000  0.00000  1.30000
    $end
    
    $rem
       CORRELATION           CCSD
       BASIS                 6-311(3+)G*
       PURECART              2222          6d, will be required for ezDyson
       EOM_IP_ALPHA          [0,0,0,1,0,0,0,0]  (Ag,B1g,B2g,B3g,Au,B1u,B2u,B3u)
       EOM_EA_BETA           [0,0,0,1,0,0,0,0]  (Ag,B1g,B2g,B3g,Au,B1u,B2u,B3u)
       CCMAN2                true
       CC_DO_DYSON           true
       CC_TRANS_PROP         true          necessary for Dyson orbitals job
       PRINT_GENERAL_BASIS   true          will be required for ezDyson
    $end
    ```

???+ example "示例 7.173: 甲醛（formaldehyde）从第一激发态以及从基态电离的戴森轨道。"
    ```qchem
    $molecule
       0 1
       O     1.535338855      0.000000000     -0.438858006
       C     1.535331598     -0.000007025      0.767790994
       H     1.535342484      0.937663512      1.362651452
       H     1.535342484     -0.937656488      1.362672535
    $end
    
    $rem
       CORRELATION           CCSD
       BASIS                 6-31G*
       PURECART              2222    6d, will be required for ezDyson
       CCMAN2                true    new Dyson code
       EE_STATES             [1]
       EOM_IP_ALPHA          [1]
       EOM_IP_BETA           [1]
       CC_TRANS_PROP         true    necessary for Dyson orbitals job
       CC_DO_DYSON           true
       PRINT_GENERAL_BASIS   true    will be required for ezDyson
    $end
    ```

???+ example "示例 7.174: Li 原子核心电离的戴森轨道：使用 Li ${}^{+}$ 作为参考，通过 EOM-EA 得到中性原子，通过 EOM-EE 得到阳离子的第 1 个激发态；总计：Li 原子的核心电离以及第 1 次电离。"
    ```qchem
    $molecule
       +1 1
       Li   0.00000  0.00000  0.00000
    $end
    
    $rem
       CORRELATION            CCSD
       BASIS                  6-311+G*
       PURECART               2222          6d, will be required for ezDyson
       CCMAN2                 true          new Dyson code
       EE_STATES              [1,0,0,0,0,0,0,0]
       EA_STATES              [1,0,0,0,0,0,0,0]
       EOM_NGUESS_SINGLES     5             to converge to the lowest EA state
       CC_TRANS_PROP          true          necessary for Dyson orbitals job
       CC_DO_DYSON            true
       PRINT_GENERAL_BASIS    true          will be required for ezDyson
    $end
    ```

???+ example "示例 7.175: CH ${}_{2}$ 从高自旋三重态参考以及从最低 SF 态电离的戴森轨道。"
    ```qchem
    $molecule
       0 3
       C
       H  1 rCH
       H  1 rCH 2 aHCH
    
       rCH    = 1.1167
       aHCH   = 102.07
    $end
    
    $rem
       CORRELATION           CCSD
       BASIS                 6-31G*
       SCF_GUESS             core
       CCMAN2                true    new Dyson code
       CC_SYMMETRY           false
       SF_STATES             [1]
       EOM_IP_ALPHA          [2]     one should be careful to request
       EOM_EA_BETA           [2]     meaningful spin for EA/IP state(s)
       CC_TRANS_PROP         true    necessary for Dyson orbitals job
       CC_DO_DYSON           true
       IQMOL_FCHK            true    generate formatted checkpoint file for IQMol
    $end
    ```

???+ example "示例 7.176: SO ${}^{-}$ 电离的戴森轨道：使用 EOM-EA 描述阴离子态，使用 EOM-SF 描述中性态；两组 EOM 态均使用中性三重态参考生成。"
    ```qchem
    $comment
    SO-, calculating Dyson orbitals using EOM-EA to describe
    the anion states and EOM-SF to describe the neutral;
    both sets of EOM states are generated using triplet reference.
    $end
    
    $molecule
    0 3
    S    0.0000000    0.0000000   -0.5241891
    O    0.0000000    0.0000000    1.0676951
    $end
    
    $rem
    JOBTYPE¯¯¯SP
    METHOD¯          ¯EOM-CCSD
    BASIS                  ¯6-31G*
    PURECART¯¯111 needed for ezDyson
    EA_BETA¯¯        [0,0,0,1]  anion state
    SF_STATES               [2,2,0,0]  neutral states
    CC_DO_DYSON¯¯true
    CC_TRANS_PROP¯¯true
    PRINT_GENERAL_BASIS¯true  needed for ezDyson
    $end
    
    $trans_prop
    state_list
    ea_beta   4 1      !state 1
    sf_states 1 1    !state 2
    sf_states 1 2    !state 3
    sf_states 2 1
    sf_states 2 2
    end_list
    state_pair_list
    1 2   ! transition 1 <-> 2
    1 3
    1 4
    1 5
    end_pairs
    calc dyson
    $end
    
    ```

???+ example "示例 7.177: 计算用 EOM-EA 求得的 HCl- 戴森轨道与平面波在 k 固定方向下的重叠。"
    ```qchem
    $comment
    Computes coupling between a Dyson orbital and a plane wave for HCl-
    for fixed direction of k-vector: k = [1,1,1] (no averaging) and
    for 6 values of |k|.
    $end
    
    $molecule
    0 1
    H 0 0 0
    Cl 0 0 1.60
    $end
    
    $rem
    basis 6-31+G*
    method eom-ccsd
    ea_states = [1,0,0,0]
    CC_DO_DYSON true
    DYSON_PW_COUPLING true
    $end
    
    $free_electron
    k_x  100  ! the value of kx is  1
    k_y  100  ! the value of ky is  1
    k_z  100  ! the value of kz is  1
    k_grid_points 6  !Coupling will be calculated for 6 |k|-values
    $end
    
    ```

???+ example "示例 7.178: 计算用 EOM-EA 求得的 N2- 戴森轨道与平面波的重叠，并对 k 取向进行平均。"
    ```qchem
    $comment
    Computes coupling betwee a Dyson orbital of N2- and a plane wave with
    averaging over k-directions
    $end
    
    
    $molecule
    0 1
    N 0 0 0
    N 0 0 1.42
    $end
    
    $rem
    basis 6-31+G*
    method eom-ccsd
    CC_DO_DYSON true
    EA_STATES = [0,0,1,0,0,0,0,0]
    DYSON_PW_COUPLING true
    $end
    
    
    $free_electron
    k_avg  1        !perform averaging over k-orientations using default grid
    k_grid_points 6  !Coupling will be calculated for |k|-values  from 0.0 eV to 0.1x(k_grid_points -1)
    $end
    
    ```
