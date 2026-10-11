翻译已完成并写入 `translated_7_3_7_tddft_pcm.md`（4 个代码块、4 个 Callout、所有公式与链接均原样保留）。以下为完整内容：

---
title: "7.3.7 溶液中的激发能与发射能：TDDFT + PCM"
---

## 7.3.7 溶液中的激发能与发射能：TDDFT + PCM

（2026 年 7 月 4 日）

如第 [11.2.3](../ch11_env/topic_pcm-em.md) 节所述，可极化连续介质模型（Polarizable Continuum Model, PCM）是在介电连续介质层次上纳入溶剂化效应的一种简便手段。本节讨论 **Q-Chem** 中用于 TDDFT 激发态 PCM 溶剂化的可用选项。关于相关关键字的更多细节，请参见第 [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM) 节和第 [11.2.4](../ch11_env/subsec_PCM_job_control.md) 节。关于 PCM 溶剂化模型的背景信息，请参见文献 [[569]](../bib_references/bib.md#bib580)。

TDDFT 可以通过两种不同的形式框架与 PCM 相结合：*线性响应*（Linear Response, LR）-PCM 与*态特异*（State-Specific, SS）-PCM。LR-PCM 方法 [[183]](../bib_references/bib.md#bib178) 使用基态与激发态之间的跃迁密度，用于描述溶质上的激发过程与溶剂环境之间的耦合。（更多细节请参见第 [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM) 节。）LR-PCM 只带来很小的额外计算代价。然而，使用跃迁密度限制了其适用范围，使之仅适用于光学允许跃迁；而对于电荷转移态或单重态到三重态的激发，LR-PCM 的贡献会消失。在 **Q-Chem** 中，TDDFT/LR-PCM 可用于计算激发能，也可用于计算激发态能量梯度与 Hessian 矩阵 [[844]](../bib_references/bib.md#bib876)，从而实现如第 [7.3.8](subsec_tddft-hessian.md) 节所描述的几何结构优化与振动频率计算。

态特异 PCM 形式框架 [[182]](../bib_references/bib.md#bib179) 基于差密度（difference-density），并考虑了溶剂对溶质波函数变化的瞬时响应。这一贡献在 LR-PCM 中并未包含，并且即使在光学禁阻跃迁的跃迁密度为零的情况下仍然非零。**Q-Chem** 提供的 SS-PCM 既可以是微扰修正形式 [[1530]](../bib_references/bib.md#bib1593)（ptSS-PCM），也可以采用两种完全迭代式的实现方案。一般而言，TDDFT 的 SS-PCM 实现 [[412]](../bib_references/bib.md#bib421) 紧密遵循第 [7.10.11](topic_abs-adc.md) 节所描述的 ADC($n$) 方法族。ptSS-PCM 方法 [[1530]](../bib_references/bib.md#bib1593)（也被称为修正线性响应方法 cLR-PCM [[190]](../bib_references/bib.md#bib185)）针对每一个所计算的态，基于 TDDFT 激发态密度来求解一个态特异的一阶修正。该一阶修正不包含激发态密度对态特异反应场的响应，因为要纳入这种响应需要一个迭代过程。ptSS-PCM 方法可以与 LR-PCM 的微扰近似 ptLR-PCM 相结合。更多细节请参见第 [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM) 节。

若要超越一阶修正，就必须使用 SS-PCM 的某种迭代实现。此时，通过针对特定态迭代优化反应场，可以自洽地求解一个态特异的薛定谔方程。在 **Q-Chem** 中，迭代式 SS-PCM 的实现 [[412]](../bib_references/bib.md#bib421) 有两种途径：*外迭代*（External Iteration, EI-SS-PCM，有时称为 Improta-Barone-Scalmani-Frisch 方法）[[612]](../bib_references/bib.md#bib635)，或者*内迭代*（Internal Iteration, II-SS-PCM，亦称*垂直激发模型*（Vertical Excitation Model, VEM））[[908]](../bib_references/bib.md#bib944)。ptSS-PCM 只增加可忽略的计算代价，而迭代过程则会使计算代价按所需迭代次数成倍增加。

TDDFT 的激发态溶剂化可在两种机制下进行：*平衡*溶剂化与*非平衡*溶剂化。非平衡溶剂化适用于快速过程（*例如*，垂直激发或发射过程），在这些过程中，溶剂的慢核自由度相对于初始态保持平衡。因此，必须将溶质置于（隐式）溶剂的非平衡状态下来建模，其中只有溶剂的快速电子极化是用终态的电荷密度弛豫得到的。这一快速溶剂响应由高频（无限频率）介电常数即所谓“光学”介电常数（$\varepsilon_{\infty}$）决定，通常取溶剂折射率的平方：$\varepsilon_{\infty}=n_{\text{refr}}^{2}$。[[569]](../bib_references/bib.md#bib580)

另一方面，平衡溶剂化适用于寿命足够长、能够让溶剂完全弛豫的激发态。此时相关的是零频率或静态介电常数（$\varepsilon_{0}$），因为它包含所有极化机制，既包括快速的电子自由度，也包括慢速的振动与取向自由度。

## 7.3.7.1 线性响应 PCM

TDDFT 的 LR-PCM 通过在 *$pcm* 段中设置 TDDFT_LR_PCM = TRUE 来启用。默认执行非平衡计算，其中激发态使用光学介电常数 $\varepsilon_{\infty}$，而所用分子轨道（MO）的基态溶剂化则使用静态介电常数。这对应于文献 [[844]](../bib_references/bib.md#bib876) 中的“完整线性响应理论”。$\varepsilon_{\infty}$ 的数值通过 *$solvent* 输入段中的关键字 **OpticalDielectric** 指定，也可以按照第 [11.2.4.3](../ch11_env/subsec_PCM_job_control.md#subsubsec:PCM-solvent-Elst) 节所述从一组预设值中选取；若要在激发态中请求平衡计算，可将 **OpticalDielectric** 设置为溶剂静态介电常数的数值。

完整 LR-PCM 的微扰近似同样可用；此外还有一些在理论上更为严格的态特异修正方法 [[569]](../bib_references/bib.md#bib580)，这些方法也已在 TDDFT 中实现 [[940]](../bib_references/bib.md#bib979)。相关方法在下面的第 [7.3.7.2](#subsubsec:tddft-PCM-iterSS) 节以及第 [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM) 节中有更详细的描述。若使用 C-PCM 模型，则 TDDFT + LR-PCM 提供解析的激发态能量梯度，并且在为 TDDFT 几何优化激活 LR-PCM 时自动启用。由于激发态几何优化隐含了溶质结构在激发态中已经平衡，因此在几何优化中使用静态介电常数可能是合适的。

LR-PCM 方法考虑的是溶剂对电子跃迁密度的响应，因而只对光学允许跃迁给出非零贡献。光学禁阻跃迁应当用态特异 PCM 来描述。这既包括从单重态基态出发的三重态激发，也包括跃迁密度为零的电荷转移态。

???+ example "示例 7.14：TDDFT/LR-C-PCM 计算低能垂直激发能"
    ```qchem
    $molecule
       0 1
       C    0.0   0.0   0.0
       O    0.0   0.0   1.21
    $end
    
    $rem
       EXCHANGE         B3lyp
       CIS_N_ROOTS      10
       CIS_SINGLETS     true
       CIS_TRIPLETS     true
       RPA              TRUE
       BASIS            6-31+G*
       XC_GRID          1
       SOLVENT_METHOD   pcm
    $end
    
    $pcm
       Theory   CPCM
       Method   SWIG
       Solver   Inversion
       Radii    Bondi
    $end
    
    $solvent
       Dielectric         78.39
       OpticalDielectric  1.777849
    $end
    ```

TDDFT_LR_PCM

### `TDDFT_LR_PCM`

> **控制 TDDFT 的 LR-PCM，即决定是否将 LR-PCM 贡献加入 TDDFT 本征值问题。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **可选值**:
>     * FALSE
>     * 不执行 LR-PCM（仅做 0 阶溶剂修正）。
>     * TRUE
>     * 执行完整的 LR-PCM。
> * **建议**: 假设基态已开启 PCM 溶剂化（即在 $rem 段中设置 SOLVENT_METHOD = PCM），则通过设置 = FALSE 关闭 LR-PCM 将得到一个“0 阶”溶剂化修正，其中使用被溶剂极化了的 MO 与能级，其余部分等价于气相 TDDFT 计算。这是更精细的“非平衡”TDDFT + PCM 方法的第一步，详见第 11.2.3.3 节。LR-PCM 对激发能的修正具有一些特殊性质，例如它对光学禁阻态为零，569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . Link，而第 11.2.3.3 节所讨论的态特异方法通常更可取。

## 7.3.7.2 态特异 PCM

态特异 PCM 任务通过 *$pcm* 块中的 StateSpecific 关键字控制，该关键字可用于激活微扰式 SS-PCM 或某一种迭代式 SS-PCM。

### `StateSpecific`

> **指定使用哪一种态特异 PCM。输入段：$pcm**
>
> * **类型**: `Various`
> * **默认值**: `NONE`
> * **可选值**:
>     * Perturb
>     * 对垂直激发执行 ptSS 与 ptLR。
>     * External
>     * 对激发态执行自洽的 EI-SS-PCM（用于发射）。
>     * Internal
>     * 对激发态执行自洽的 II-SS-PCM（用于发射或激发）。
> * **建议**: 对于垂直激发能，使用 ptSS-PCM，或在极性很强的体系中使用非平衡 II-SS-PCM；对于长寿命激发态的发射能，使用平衡 EI-SS-PCM。

**1. 微扰态特异（ptSS）PCM**

微扰态特异 PCM（ptSS-PCM）[[1530]](../bib_references/bib.md#bib1593) 通过在 *$pcm* 块中设置 **StateSpecific** = **Perturb** 来启用。默认情况下，ptSS 修正在由光学介电常数（*$solvent* 块中的 **OpticalDielectric**）决定的非平衡机制下求解。若要强制执行*平衡*的 ptSS-PCM 计算，必须将 **OpticalDielectric** 设置为静态值 $\varepsilon_{0}$。为了将反应场分离为快速贡献与慢速贡献，使用 **ChargeSeparation** 关键字选择电荷分离方案（默认值为 **Marcus**，更多信息请参见第 [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM) 节以及文献 [[1530]](../bib_references/bib.md#bib1593)。）另外，设置 **NonEquilibrium** = **TRUE** 会执行一次默认的非平衡 ptSS-PCM 计算，采用 **Marcus** 电荷分离并关闭 LR-PCM。ptSS-PCM 的输出针对每个所计算的态同时给出 ptSS 修正与 ptLR 修正。在非平衡情形下，修正后的能量对应于垂直激发能。结果会分别基于非弛豫密度与弛豫密度给出（若后者被推荐）。推荐使用基于弛豫密度的结果。[[1530]](../bib_references/bib.md#bib1593)

### `NonEquilibrium`

> **激活非平衡 ptSS-PCM。输入段：$pcm**
>
> * **类型**: `STRING`
> * **默认值**: `False`
> * **可选值**:
>     * TRUE
>     * 激活非平衡 ptSS-PCM。
>     * FALSE
>     * 停用非平衡 ptSS-PCM。
> * **建议**: 激活一次默认的 ptSS-PCM 计算，采用 Marcus 电荷分离且不附加 LR-PCM。

### `ChargeSeparation`

> **在溶剂平衡态中分离快速电荷与慢速电荷。输入段：$pcm**
>
> * **类型**: `STRING`
> * **默认值**: `NONE`
> * **可选值**:
>     * Marcus
>     * 使用 Marcus 分区进行慢/快电荷分离。
>     * Pekar
>     * 使用 Pekar 分区进行慢/快电荷分离。
> * **建议**: 电荷分离需与 $pcm 中的 StateSpecific 关键字配合使用。

???+ example "示例 7.15：使用 ptSS 与 ptLR 方法研究平面型 DMABN 垂直激发能所受的 PCM 溶剂化效应。"
    ```qchem
    $molecule
       0  1
       C     0.000046   -0.000398    1.904953
       C     1.210027    0.000379    1.186051
       C     1.214640   -0.000065   -0.194515
       C     0.000164   -0.000616   -0.933832
       C    -1.214349   -0.001557   -0.194687
       C    -1.209753   -0.001846    1.185775
       H     2.151949    0.001377    1.722018
       H     2.164371    0.000481   -0.709640
       H    -2.164082   -0.002008   -0.709781
       H    -2.151763   -0.002287    1.721615
       C    -0.000227    0.001061    3.325302
       N    -0.000475    0.002405    4.484321
       N     0.000053   -0.000156   -2.297372
       C    -1.258656    0.001284   -3.036994
       H    -1.041042    0.001615   -4.102376
       H    -1.860897   -0.885647   -2.811117
       H    -1.859247    0.889133   -2.810237
       C     1.258563   -0.000660   -3.037285
       H     1.860651    0.886208   -2.810755
       H     1.859362   -0.888604   -2.811461
       H     1.040664   -0.000097   -4.102609
    $end
    
    $rem
       EXCHANGE              LRC-wPBEPBE
       OMEGA                 260
       BASIS                 6-31G*
       CIS_N_ROOTS           10
       RPA                   2
       CIS_SINGLETS          1
       CIS_TRIPLETS          0
       CIS_RELAXED_DENSITY   TRUE
       SOLVENT_METHOD        PCM
    $end
    
    $pcm
       NonEquilibrium
       Theory                 IEFPCM
       StateSpecific          Perturb
    $end
    
    $solvent
       Dielectric             35.688000       ! Acetonitrile
       OpticalDielectric      1.806874
    $end
    ```

**2. 迭代式态特异 PCM**

文献 [[412]](../bib_references/bib.md#bib421) 中实现的迭代式态特异 PCM 的控制选项，与第 [7.10.11](topic_abs-adc.md) 节所述 ADC($n$) 方法族的设置方式相同。将关键字 **EqSolv** 设置为目标最大迭代次数，即可对 **EqState** 所指明的参考态激活自洽 SS-PCM。迭代一直进行，直到达到最大迭代次数或满足收敛判据为止。这些判据基于激发态能量与表面电荷，通过 **Eqs_Conv** 设置。在反应场的迭代优化过程中，各态可能改变其排序（root-flipping，根翻转）。基于表面静电势、能量变化以及激发态偶极矩三者组合的自动态跟踪（**EqState_Follow** = **true**）可以使用。它对分离良好或性质差异显著的态（*即*电荷转移态与局域激发态）表现良好，但在接近交叉点的相似态上可能失效。

请注意，迭代式态特异 PCM 的激发态能量只对被标记为输出中“EqS-reference”的参考态才具有物理意义。对于所有其他态，只能解释相对于自洽参考态的能量。迭代平衡 SS-PCM 的输出列出向基态的发射能（仅 EI-SS-PCM），以及向其他激发态的跃迁能（EI- 与 II-SS-PCM 均提供），并分别给出 0 阶结果与一阶结果（附加非平衡 ptSS 修正）。对于非平衡 II-SS-PCM，只有到自洽优化激发态的垂直激发能才具有物理意义。在非平衡 II-SS-PCM 与 ptSS-PCM 计算中，同样使用 **ChargeSeparation** 关键字。

### `EqSolv`

> **自洽 SS-PCM 过程的主开关。输入段：$pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * 0
>     * 不做自洽 SS-PCM。
>     * 1
>     * 使用磁盘上已有的溶剂场做一次 SS-PCM 计算（SCF + TDDFT）。
>     * $n>1$
>     * 最多执行
>     * $n$
>     * 次自动溶剂场迭代。
> * **建议**: 我们建议最多使用 15 步。典型收敛需要 3–5 步，困难情形需要 6–12 步。如果溶剂场迭代在 15 步内不收敛，说明存在问题。对于 EI-SS-PCM 任务，务必确认此前的任务已将溶剂场写入磁盘。II-SS-PCM 会自动从建立溶剂场开始。

### `EqState`

> **指定要为其优化溶剂场的态。输入段：$pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **可选值**:
>     * 1
>     * 能量最低的激发态
>     * 2
>     * 第二低的激发态
>     * $\cdots$
> * **建议**: 在只计算一类激发态的前提下，该态将按照输出文件“Exited-State Summary”（激发态摘要）中显示的能量位置来选择。

### `Eqs_Conv`

> **通过设置收敛判据（SCF 能量（EI-SS-PCM）或激发态能量（II-SS-PCM）与电荷向量的混合）来控制溶剂场迭代的收敛。SCF 能量判据按 $10^{-n}$ $E_{h}$ 计算。输入段：$pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `SCF_CONVERGENCE`
> * **可选值**:
>     * 3
>     * 对发射能可能已经足够
>     * 4
>     * 确保总能量收敛（2.7 meV）
>     * 5
>     * 非常严格
> * **建议**: 使用默认值。

### `EqState_Follow`

> **控制基于表面静电势、激发态能量变化以及激发态偶极矩的自动态跟踪。输入段：$pcm**
>
> * **类型**: `NONE`
> * **默认值**: `FALSE`
> * **可选值**:
>     * TRUE
>     * 激活自动态跟踪
>     * FALSE
>     * 停用自动态跟踪。
> * **建议**: 态跟踪对性质不同的分离态效果良好，但对近简并态可能出现问题。当相似态彼此接近时，建议停动态跟踪。

**2. (A) 外迭代 SS-PCM**

EI-SS-PCM（亦称 Improta-Barone-Scalmani-Frisch PCM [[612]](../bib_references/bib.md#bib635)）通过在 *$pcm* 段中设置 **StateSpecific** = **External** 来启用。EI-SS-PCM 同时对 SCF 与 TDDFT 计算进行迭代，其做法是将激发态反应场返回到一个冻结反应场（frozen-Reaction-Field, fRF）SCF 中。在此之前的独立任务中，必须通过设置 **StateSpecific** = External 且不加 **EqSolv** 关键字来预先建立反应场。在随后的迭代任务中，参考态（**EqState**）可以在先前计算得到的各态中自由选取，并且可以用完全相同的方式重启迭代（*例如*，用于手动修正自动态跟踪的结果）。EI-SS-PCM 的收敛判据基于表面电荷向量的变化以及 fRF-SCF 能量，以将所有激发态收敛到同一水平。此外，self-ptSS 项也可以指示收敛情况，但它并非实际使用的收敛判据。

EI-SS-PCM 始终按平衡溶剂化执行，基于静态介电常数（**Dielectric**）使用溶剂的完整介电响应。非平衡的发射能与跃迁能则在 ptSS-PCM 级别上一阶求得。EI-SS-PCM 给出态特异薛定谔方程的正确解，且不受基态 MO 的污染，因此，当需要对激发态与基态同等对待时，应当使用该方法。

???+ example "示例 7.7.16：乙腈中硝酸根离子的 TDDFT 外迭代 SS-PCM 计算。"
    ```qchem
    $molecule
       -1 1
       N    -0.068642000000     -0.600693000000     -0.723424000000
       O     0.349666000000      0.711166000000      1.187490000000
       O    -0.948593000000      0.200668000000     -0.956940000000
       O     0.659040000000     -0.386002000000      0.402650000000
    $end
    
    $rem
       jobtype    ¯¯         sp
       method ¯¯             PBE0
       basis  ¯¯¯           3-21g
    point_group_symmetry False
       cis_n_roots             2           ! Number of excited states
       cis_singlets            true
       cis_triplets            false
       rpa                     false       ! Tamm-Dancoff approximation
       cis_moments             true        ! Excited state multipole moments
       cis_relaxed_density     true        ! Excited state density relaxation
       solvent_method        ¯ pcm
    $end
    
    $pcm
       StateSpecific           External    ! Keyword for External Iteration SS-PCM
       LinearResponse          false       ! Switch of LR-PCM
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       jobtype ¯¯             sp
       method ¯¯             PBE0
       basis ¯¯¯             3-21g
    point_group_symmetry False
       cis_n_roots             2
       cis_singlets            true
       cis_triplets            false
       rpa                     false
       cis_moments             true
       cis_relaxed_density     true
       solvent_method          pcm
    $end
    
    $pcm
       StateSpecific           External
       Eqsolv                  15          ! Max. Number of iterations
       Eqstate                 1           ! Ref. State to be equilibrated
       Eqs_Conv                4           ! Conv. criterion for SCF energy and surface charges
       EqState_Follow          true        ! State Following to remain on the same Ref. State
       LinearResponse          false
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    ```

**2. (B) 内迭代 SS-PCM**

II-SS-PCM（亦称垂直激发模型 VEM [[908]](../bib_references/bib.md#bib944)）通过设置关键字 **StateSpecific** = **Internal** 来启用。II-SS-PCM 在迭代过程中保持相同的基态波函数，但在 TDDFT 计算中交换基态与激发态的反应场。这会导致激发态受到基态 MO 的轻微污染。II-SS-PCM 既可用于平衡情形（绝热激发模型，Adiabatic Excitation Model, AEM），也可用于非平衡情形（VEM），并且既可使用激发态反应场的完整矩阵（f），也可仅使用其对角元（d），如文献 [[908]](../bib_references/bib.md#bib944) 所述。要选择确切的模型，需将关键字 **InternalIteration** 设置为 **VEM(d)**、**VEM(f)**、**AEM(d)** 或 **AEM(f)**。与 EI-SS-PCM 不同，II-SS-PCM 方法会自动先执行一次准备计算，以产生用于迭代的初始激发态反应场，而该迭代无法重启。为了在自动态跟踪之外仍然允许手动态跟踪，可以在 **InternalIteration** 中所选方法之后附加 -state 来列出特定的态序列。该序列以零结束，零之后态跟踪将重新启用。对于 II-SS-PCM，收敛判据基于参考态能量与表面电荷向量。

非平衡 II-SS-PCM 或 VEM 计算相当于垂直激发能的非平衡 ptSS-PCM 的迭代版本。此时还纳入了密度对快速激发态反应场的响应。因此，VEM 对收敛参考态（输出中以“EqS-reference”标示）的结果对应于垂直激发能，而其他各态没有物理意义。

而平衡 II-SS-PCM 或 AEM 则给出激发参考态能量以及向其他激发态的跃迁能。但是，从参考态到基态的发射能是绝热型的，因为基态轨道不受激发态反应场的影响。要获得垂直发射能，必须再执行一次 fRF 基态计算：设置 **RF_ptSS_Save** = **true**，并在随后的任务中通过设置 **RF_ptSS_Read** = **true** 来读取反应场。更多信息请参见第 [7.7.9](sect_ROKS_neq-PCM.md) 节。

### `InternalIteration`

> **控制所使用的内迭代 SS-PCM 模型。此外，在添加 -state 之后可以追加要跟踪的态序列。输入段：$pcm**
>
> * **类型**: `NONE`
> * **默认值**: `NONE`
> * **可选值**:
>     * VEM(f)
>     * 激活使用完整矩阵贡献的非平衡 II-SS-PCM（VEM）。
>     * VEM(d)
>     * 激活仅使用对角矩阵元的非平衡 II-SS-PCM（VEM）。
>     * AEM(f)
>     * 激活使用完整矩阵贡献的平衡 II-SS-PCM（AEM）。
>     * AEM(d)
>     * 激活仅使用对角矩阵元的平衡 II-SS-PCM（AEM）。
>     * …-state x y z … 0
>     * 指定要跟踪的态序列（以 0 结束）。
> * **建议**: 非平衡版本（VEM）给出垂直激发能，而在平衡版本（AEM）中则准备发射能的初始态。通过附加 -state 后缀可以提供显式的待跟踪态序列。以零结束之后，态跟踪将重新启用。

???+ example "示例 7.7.17：TDDFT 内迭代 SS-PCM，并附加基态计算以求乙腈中硝酸根离子的垂直发射能。"
    ```qchem
    $molecule
       -1 1
       N    -0.068642000000     -0.600693000000     -0.723424000000
       O     0.349666000000      0.711166000000      1.187490000000
       O    -0.948593000000      0.200668000000     -0.956940000000
       O     0.659040000000     -0.386002000000      0.402650000000
    $end
    
    $rem
       jobtype ¯¯             sp
       method ¯¯             PBE0
       basis ¯¯¯             3-21g
    point_group_symmetry False
       cis_n_roots             4           ! Number of excited states
       cis_singlets            true
       cis_triplets            false
       rpa                     false       ! Tamm-Dancoff approximation
       cis_moments             true        ! Excited state multipole moments
       cis_relaxed_density     true        ! Excited state density relaxation
       solvent_method          pcm
    $end
    
    $pcm
       StateSpecific           Internal    ! Keyword for Internal Iteration SS-PCM
       ChargeSeparation        MARCUS      ! Keyword for the charge separation
       InternalIteration       AEM(f)      ! Procedure (VEM(f), VEM(d), AEM(f), or AEM(d)) + state sequence (add e.g.: -state 1 3 1 0)
       Eqsolv                  10          ! Max. Number of iterations
       Eqstate                 1           ! Ref. State to be equilibrated
       Eqs_Conv                4           ! Conv. criterion for SCF energy and surface charges
       EqState_Follow          true        ! State Following to remain on the same Ref. State
       theory                  iefpcm      ! PCM Theory (else CPCM)
       rf_ptss_save            true        ! Save the eq. reaction field of Ref. State
       LinearResponse          false       ! Switch of LR-PCM
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       jobtype                 sp
       method ¯¯             PBE0
       basis                   3-21g
    point_group_symmetry False
       solvent_method          pcm
    $end
    
    $pcm
       theory                  iefpcm
       rf_ptss_read            true        ! Flag to read the reaction field and do RF-ptSS calc
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    
    ```
