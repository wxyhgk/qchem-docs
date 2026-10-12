---
title: "5.12.3 热助占据密度泛函理论 (TAO-DFT)"
---

## 5.12.3 热助占据密度泛函理论 (TAO-DFT)

（2026 年 7 月 4 日）

为了以最小的计算复杂度研究大型强关联体系的基态性质，Jeng-Da Chai 教授最近提出了热助占据密度泛函理论（thermally-assisted-occupation density functional theory, TAO-DFT）。[[227]](../bib_references/bib.md#bib222)
 与传统的多参考方法不同，TAO-DFT 的计算复杂度随活性空间大小的增长极为缓慢（*即*，TAO-DFT 计算不需要限制活性空间），因此 TAO-DFT 在大型多自由基体系的研究中非常有前景。TAO-DFT 是一种通过费米-狄拉克（Fermi-Dirac）分布产生分数轨道占据的 DFT 方案，该分布由一个虚拟温度 $\theta$ 控制，并且现有的 XC 泛函（*e.g.*，LDA[[227]](../bib_references/bib.md#bib222)
、
GGA[[228]](../bib_references/bib.md#bib228)
、全局杂化 GGA[[229]](../bib_references/bib.md#bib229)
 或 range-separated 杂化 GGA [[229]](../bib_references/bib.md#bib229)
）均可用于 TAO-DFT。
该方法在单点能计算和解析核梯度方面的计算代价与 Kohn-Sham DFT 相当，并且在不存在强静态关联效应时，其代价退化为 Kohn-Sham DFT 的代价。

有几个 *$rem* 变量用于 TAO-DFT。

### `TAO_DFT`

> **控制是否使用 TAO-DFT。**
>
> * **类型**: `Boolean`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不使用 TAO-DFT
>     * `TRUE`: 使用 TAO-DFT
> * **建议**: 无

### `TAO_DFT_THETA`

> **TAO-DFT 中虚拟温度取值 $\theta=m\times 10^{-n}\ E_{h}$ 的参数 $m$（尾数）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `7`
> * **选项**:
>     * $m$: 自定义虚拟温度的尾数。
> * **建议**: 无

### `TAO_DFT_THETA_NDP`

> **TAO-DFT 中虚拟温度取值 $\theta=m\times 10^{-n}\ E_{h}$ 的参数 $n$（指数）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `3`
> * **选项**:
>     * $n$: 自定义虚拟温度的指数幂。
> * **建议**: 无

### `PTAO`

> **控制是否执行 pTAO/TDA 方法。**
>
> * **类型**: `Boolean`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不执行 pTAO/TDA 方法
>     * `TRUE`: 执行 pTAO/TDA 方法
> * **建议**: 无

请注意，将 TAO_DFT_THETA 设为 0 即可恢复普通的 Kohn-Sham DFT。[[227]](../bib_references/bib.md#bib222)
 除 XC 泛函外，TAO-DFT 还需要一个泛函
$E_{\theta}[\rho]$。目前 **Q-Chem** 中可用的有
一个 LDA 版本[[227]](../bib_references/bib.md#bib222)
（ETheta_LDA 泛函）以及一个基于
梯度展开近似（gradient expansion approximation, GEA）的版本[[228]](../bib_references/bib.md#bib228)
（ETheta_GEA 泛函），在下面的示例作业中，后者可以替换前者。
此外，对于全局杂化（global hybrid, GH）GGA，TAO-DFT 还需要一个泛函 $E_{x,\theta}[\rho]$。
目前 Q-CHEM 中可用的是一个 LDA 版本（EThetaX_LDA 泛函）[[229]](../bib_references/bib.md#bib229)
。
另外，对于 range-separated 杂化（RSH）GGA，TAO-DFT 还需要两个泛函 $E^{\text{SR}}_{x,\theta}[\rho]$ 和 $E^{\text{LR}}_{x,\theta}[\rho]$，其 LDA 版本（SR_ETHETAX_LDA 和 LR_ETHETAX_LDA 泛函）现已在 Q-CHEM 中提供 [[815]](../bib_references/bib.md#bib858)
。请注意，$E^{\text{SR}}_{x,\theta}[\rho]$ 和 $E^{\text{LR}}_{x,\theta}[\rho]$ 都依赖于 range-separation 参数 $\omega$，并且当 $\omega=0$ 时，$E^{\text{SR}}_{x,\theta}[\rho]$ 退化为 $E_{x,\theta}[\rho]$。因此，取 $\omega=0$ 的 SR_ETHETAX_LDA 泛函是 $E_{x,\theta}[\rho]$ 的另一个 LDA 版本，记作 ETHETAX19_LDA。

为了提升 TAO-DFT 泛函的性能，采用基于 D4 模型的半经验色散校正的 B97 型泛函在 TAO-DFT 框架下使用与体系无关的虚拟温度进行了优化，得到了 TAO-B97-D4、TAO-B97X-D4 和 TAO-$\omega$B97X-D4 [[815]](../bib_references/bib.md#bib858)
。在约束 $\theta=0$ 下，B97 型 RSH 泛函也在 KS-DFT 中进行了优化，得到了 KS-$\omega$B97X-D4 [[815]](../bib_references/bib.md#bib858)
（用法参见示例 [5.6.3](ex_ks-wb97xd4.md)）。

当 $\theta>0$ 时，使用绝热 xc 核的 TAO-DFT 含时推广（TDTAO-DFT）中可能出现虚假激发（spurious excitations）[[1523]](../bib_references/bib.md#bib1587)
，这与采用绝热近似的含时密度矩阵泛函理论（TDDMFT）类似 [[442]](../bib_references/bib.md#bib453)
。为解决这一问题，人们提出了一种 post-TAO/TDA 方法（pTAO/TDA）[[815]](../bib_references/bib.md#bib858)
。在 pTAO/TDA 方法中，态 X 相对于基态的能量（即态 X 的激发能）由文献 [[815]](../bib_references/bib.md#bib858)
 中的公式 (85) 给出：

<a id="eq:excitationX"></a>

$$
\omega_{\text{pTAO/TDA}}[\text{X}]=(\omega[\text{X}]-\omega[\text{A}_{1}])+(E_{\text{A}_{1}}-E_{\text{GS}}). \tag{5.76}
$$

其中，$\omega[\text{X}]$ 是 X 相对于 pTAO 参考态的能量，可通过在 Q-CHEM 中设置 PTAO = TRUE 获得（参见示例 5.12.3）。此外，$E_{\text{GS}}$ 和 $E_{\text{A}_{1}}$ 分别是通过 TAO-DFT 得到的体系基态能量和不同自旋态之间的最低激发能。请注意，采用 $(\omega[\text{X}]-\omega[\text{A}_{1}])$ 是为了抑制参考态（例如 pTAO 参考态）选择所带来的影响。

???+ example "示例 5.30: Be 原子的 TAO-LDA 计算"
    ```qchem
    $molecule
       0 1
       Be
    $end
    
    $rem
       BASIS               6-31G*
       EXCHANGE            gen
       TAO_DFT             true
       TAO_DFT_THETA       7    ! default, theta=7 mhartree
       TAO_DFT_THETA_NDP   3    ! default
    $end
    
    $xc_functional
       X   S             1.0
       C   PW92          1.0
       X   ETheta_LDA    1.0
    $end
    ```

???+ example "示例 5.31: 拉伸 N ${}_{2}$ 的 TAO-PBE 自旋限制计算"
    ```qchem
    $molecule
       0 1
       N1
       N2 N1 4.5
    $end
    
    $rem
       BASIS               6-31G*
       EXCHANGE            gen
       TAO_DFT             true
       TAO_DFT_THETA       40  ! theta = 40 mhartree
       TAO_DFT_THETA_NDP   3
    $end
    
    $xc_functional
       X PBE         1.0
       C PBE         1.0
       X ETheta_LDA  1.0
    $end
    ```

???+ example "示例 5.32: 拉伸 N ${}_{2}$ 的 TAO-PBE 自旋非限制计算"
    ```qchem
    $molecule
       0 1
       N1
       N2 N1 5.0
    $end
    
    $rem
       JOBTYPE             opt
       UNRESTRICTED        true
       BASIS               6-31G*
       EXCHANGE            gen
       TAO_DFT             true
       TAO_DFT_THETA       40  ! theta = 40 mhartrees
       TAO_DFT_THETA_NDP   3   ! can omit this line
       SCF_GUESS           gwh
       SCF_GUESS_MIX       3   ! mix in 30% LUMO in alpha to break symmetry
    $end
    
    $xc_functional
       X PBE         1.0
       C PBE         1.0
       X ETheta_LDA  1.0
    $end
    ```

???+ example "示例 5.33: H ${}_{2}$ 分子的 TAO-PBE0 计算"
    ```qchem
    $molecule
       0 1
       H1
       H2 H1 1.00
    $end
    
    $rem
       JOBTYPE             opt
       UNRESTRICTED        true
       BASIS               6-31G*
       EXCHANGE            gen
       TAO_DFT             true
       TAO_DFT_THETA       20  ! theta = 20 mhartrees
       TAO_DFT_THETA_NDP   3   ! can omit this line
       SCF_GUESS           gwh
       SCF_GUESS_MIX       3   ! mix in 30% LUMO in alpha to break symmetry
    $end
    
    $xc_functional
       X ETheta_LDA    1.00
       X EThetaX_LDA   0.25
       X HF            0.25
       X PBE           0.75
       C PBE           1.00
    $end
    ```

???+ example "示例 5.34: H ${}_{2}$ 分子的 TAO-B3LYP 计算"
    ```qchem
    $molecule
       0 1
       H1
       H2 H1 1.00
    $end
    
    $rem
       JOBTYPE             opt
       UNRESTRICTED        true
       BASIS               6-31G*
       EXCHANGE            gen
       TAO_DFT             true
       TAO_DFT_THETA       174 ! theta = 17.4 mhartrees
       TAO_DFT_THETA_NDP   4
       SCF_GUESS           gwh
       SCF_GUESS_MIX       3   ! mix in 30% LUMO in alpha to break symmetry
    $end
    
    $xc_functional
       X ETheta_LDA    1.00
       X EThetaX_LDA   0.20
       X HF            0.20
       X Slater        0.08
       X Becke88       0.72
       C LYP           0.81
       C VWN1RPA       0.19
    $end
    ```

???+ example "示例 5.35: H ${}_{2}$ 分子的 TAO-B97-D4 计算"
    ```qchem
    $molecule
    0 1
    H 0.00 0.00 0.00
    H 1.00 0.00 0.00
    $end
    
    $rem
    JOBTYPE              = sp
    unrestricted         = FALSE
    scf_guess            = SAD
    scf_guess_mix        = 0
    scf_algorithm        = diis
    max_scf_cycles       = 300
    GEN_SCFMAN           = FALSE
    xc_grid              = 000075000302
    scf_convergence      = 8
    thresh               = 14
    BASIS                = 6-31G(d)
    TAO_DFT              = true
    TAO_DFT_THETA        = 959717
    TAO_DFT_THETA_NDP    = 8
    EXCHANGE             = gen
    symmetry             = false
    sym_ignore           = true
    basis_lin_dep_thresh = 8
    DFT_D                = D4
    DFT_D4_A1            = 50000000
    DFT_D4_A2            = 350000000
    DFT_D4_S6            = 100000000
    DFT_D4_S8            = 172371500
    DFT_D4_S9            = 100000000
    DFT_D4_S10           = 0
    $end
    
    $XC_functional
    X ETheta_LSDA         1.000000
    X TAO_B97             1.000000
    C TAO_B97             1.000000
    $end
    ```

???+ example "示例 5.36: H ${}_{2}$ 分子的 TAO-B97X-D4 计算"
    ```qchem
    $molecule
    0 1
    H 0.00 0.00 0.00
    H 1.00 0.00 0.00
    $end
    
    $rem
    JOBTYPE              = sp
    unrestricted         = FALSE
    scf_guess            = SAD
    scf_guess_mix        = 0
    scf_algorithm        = diis
    max_scf_cycles       = 300
    GEN_SCFMAN           = FALSE
    xc_grid              = 000075000302
    scf_convergence      = 8
    thresh               = 14
    BASIS                = 6-31G(d)
    TAO_DFT              = true
    TAO_DFT_THETA        = 240964
    TAO_DFT_THETA_NDP    = 7
    EXCHANGE             = gen
    symmetry             = false
    sym_ignore           = true
    basis_lin_dep_thresh = 8
    DFT_D                = D4
    DFT_D4_A1            = 50000000
    DFT_D4_A2            = 400000000
    DFT_D4_S6            = 100000000
    DFT_D4_S8            = 170811200
    DFT_D4_S9            = 100000000
    DFT_D4_S10           = 0
    $end
    
    $XC_functional
    X ETheta_LSDA         1.000000
    X ETHETAX_LSDA19      0.325932
    X HF                  0.325932
    X TAO_B97X            1.000000
    C TAO_B97X            1.000000
    $end
    ```

???+ example "示例 5.37: H ${}_{2}$ 分子的 TAO- $\omega$ B97X-D4 计算"
    ```qchem
    $molecule
    0 1
    H 0.00 0.00 0.00
    H 1.00 0.00 0.00
    $end
    
    $rem
    JOBTYPE              = sp
    unrestricted         = FALSE
    scf_guess            = SAD
    scf_guess_mix        = 0
    scf_algorithm        = diis
    max_scf_cycles       = 300
    GEN_SCFMAN           = FALSE
    xc_grid              = 000075000302
    scf_convergence      = 8
    thresh               = 14
    BASIS                = 6-31G(d)
    TAO_DFT              = true
    TAO_DFT_THETA        = 502796
    TAO_DFT_THETA_NDP    = 7
    EXCHANGE             = gen
    LRC_DFT              = TRUE
    COMBINE_K            = TRUE
    OMEGA                = 300
    symmetry             = false
    sym_ignore           = true
    basis_lin_dep_thresh = 8
    DFT_D                = D4
    DFT_D4_A1            = 65000000
    DFT_D4_A2            = 300000000
    DFT_D4_S6            = 100000000
    DFT_D4_S8            = 131716300
    DFT_D4_S9            = 100000000
    DFT_D4_S10           = 0
    $end
    
    $XC_functional
    X ETheta_LSDA         1.000000
    X LR_ETHETAX_LSDA     1.000000
    X SR_ETHETAX_LSDA     0.179379
    X HF                  0.179379
    X TAO_wB97X           1.000000
    C TAO_wB97X           1.000000
    $end
    ```

???+ example "示例 5.38: 使用 pTAO/TDA 方法与 TAO- $\omega$ B97X-D4 计算 Ar $\cdots$ S ${}_{3}$ 二聚体相对于 pTAO 参考态的相对能量"
    ```qchem
    $comment
     Ar-S3 in the singlet state with intermolecular distance R = 5 angstrom
    $end
    
    $molecule
    0 1
    S   3.1879342892   0.0000000000  0.0000000201
    S   2.1560328618   0.0000000000  1.6334812933
    S   2.1560328490   0.0000000000 -1.6334813134
    Ar -2.5000000000   0.0000000000  0.0000000000
    $end
    
    $rem
    JOBTYPE              = sp
    unrestricted         = FALSE
    scf_guess            = SAD
    scf_guess_mix        = 0
    scf_algorithm        = diis
    max_scf_cycles       = 300
    GEN_SCFMAN           = FALSE
    xc_grid              = 000099000590
    scf_convergence      = 8
    thresh               = 14
    BASIS                = 6-31G(d)
    TAO_DFT              = true
    TAO_DFT_THETA        = 502796
    TAO_DFT_THETA_NDP    = 7
    PTAO                 = true
    EXCHANGE             = gen
    LRC_DFT              = TRUE
    COMBINE_K            = TRUE
    OMEGA                = 300
    symmetry             = false
    sym_ignore           = true
    basis_lin_dep_thresh = 8
    DFT_D                = D4
    DFT_D4_A1            = 65000000
    DFT_D4_A2            = 300000000
    DFT_D4_S6            = 100000000
    DFT_D4_S8            = 131716300
    DFT_D4_S9            = 100000000
    DFT_D4_S10           = 0
    max_cis_cycles       = 100
    CIS_N_ROOTS          = 20
    CIS_SINGLETS         = TRUE
    CIS_TRIPLETS         = TRUE
    $end
    
    $XC_functional
    X ETheta_LSDA         1.000000
    X LR_ETHETAX_LSDA     1.000000
    X SR_ETHETAX_LSDA     0.179379
    X HF                  0.179379
    X TAO_wB97X           1.000000
    C TAO_wB97X           1.000000
    $end
    ```
