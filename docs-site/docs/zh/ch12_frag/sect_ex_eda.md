---
title: "12.7.5 激发态的 ALMO-EDA"
---

## 12.7.5 激发态的 ALMO-EDA

（2026 年 7 月 4 日）

## 12.7.5.1 理论

到目前为止，我们仅介绍了针对处于基态的分子之间分子间相互作用的能量分解分析（EDA）方法。由于电子激发态通常伴随着束缚较弱的电子、因电子跃迁而改变的多极矩（静电多极矩），以及往往更大的极化率，其他分子对激发态体系的影响可能比对基态的影响更大，也更缺乏化学直觉上的可解释性。此外，还存在一些体系在基态下仅以弱相互作用结合，但在电子激发态下却结合得强得多（*例如* He${}_{2}$ 与 He${}_{2}^{\ast}$）。因此，非常需要开发一种解释工具，用于研究与激发态分子间的分子间相互作用相关的这些重要现象。

Ge *et al.*  recently 将 ALMO-EDA 推广，用于处理在 CIS 或 TDDFT/TDA 理论水平上计算的*激发复合物*（exciplex，其激发可归属于复合物中的单一分子）[[435]](../bib_references/bib.md#bib446)

以及*激发二聚体*（excimer，其激发由多个片段共同贡献）[[434]](../bib_references/bib.md#bib447)

。这里我们简要概述其分解方案。对于激发复合物的 EDA，首先将激发态下的相互作用能（$\Delta E_{\mathrm{INT}}^{\ast}$）定义为

<a id="Ch12.E34"></a>

$$
\Delta E_{\mathrm{INT}}^{\ast}=E^{\ast}-E_{\mathrm{frag}}^{\ast} \tag{12.34}
$$

其中 $E^{\ast}=E+\omega$ 是激发态超体系（supersystem）的能量，而 $E_{\mathrm{frag}}^{\ast}$ 可表示为各基态片段能量之和加上其中一个片段的激发能（不失一般性，将该激发片段记为片段"1"）：

<a id="eq:ex_e_frag"></a>

$$
E_{\mathrm{frag}}^{\ast}=\sum_{F}E_{F}+\omega_{1} \tag{12.35}
$$

因此，我们可以将激发态相互作用能改写为

<a id="eq:ex_int"></a>

$$
\Delta E_{\mathrm{INT}}^{\ast}=\Delta E_{\mathrm{INT}}+\Delta\omega_{\mathrm{INT}} \tag{12.36}
$$

它包含基态相互作用能（$\Delta E=E-\sum_{F}E_{F}$）与激发能之差（$\Delta\omega_{\mathrm{INT}}=\omega-\omega_{1}$）的贡献。然后，类似于第一代基态 ALMO-EDA[[682]](../bib_references/bib.md#bib706)

，激发态相互作用能可以被分离为冻结相互作用（FRZ）、极化（POL）和电荷转移（CT）三项贡献：

<a id="eq:ex_eda"></a>

$$
\Delta E_{\mathrm{INT}}^{\ast}=\Delta E_{\mathrm{FRZ}}^{\ast}+\Delta E_{\mathrm{POL}}^{\ast}+\Delta E_{\mathrm{CT}}^{\ast} \tag{12.37}
$$

式 ([12.37](#eq:ex_eda)) 右端的每一项都可以写成类似于式 ([12.36](#eq:ex_int)) 的形式：

<a id="A3.S8.EGx124"></a>

$$
\displaystyle\begin{aligned} \displaystyle\Delta E_{\mathrm{FRZ}}^{\ast}&\displaystyle=\Delta E_{\mathrm{FRZ}}+\omega_{\mathrm{FRZ}}-\omega_{1}\\
&\displaystyle=\Delta E_{\mathrm{FRZ}}+\Delta\omega_{\mathrm{FRZ}}\\
\displaystyle\Delta E_{\mathrm{POL}}^{\ast}&\displaystyle=\Delta E_{\mathrm{POL}}+\omega_{\mathrm{POL}}-\omega_{\mathrm{FRZ}}\\
&\displaystyle=\Delta E_{\mathrm{POL}}+\Delta\omega_{\mathrm{POL}}\\
\displaystyle\Delta E_{\mathrm{CT}}^{\ast}&\displaystyle=\Delta E_{\mathrm{CT}}+\omega-\omega_{\mathrm{POL}}\\
&\displaystyle=\Delta E_{\mathrm{CT}}+\Delta\omega_{\mathrm{CT}}\end{aligned} \tag{12.38}
$$

其中的 $\Delta E_{\mathrm{FRZ}}$、$\Delta E_{\mathrm{POL}}$ 和 $\Delta E_{\mathrm{CT}}$ 可通过对超体系执行基态 ALMO-EDA 获得。而要计算 $\Delta\omega_{\mathrm{FRZ}}$、$\Delta\omega_{\mathrm{POL}}$ 和 $\Delta\omega_{\mathrm{CT}}$，就需要定义 $\omega_{\mathrm{FRZ}}$ 和 $\omega_{\mathrm{POL}}$，*即* 分别与冻结超体系和极化超体系相关联的激发能。冻结中间态可视为一个激发片段嵌入由其他处于基态的片段所构成的环境中，环境对激发片段的作用仅通过超体系的 Fock 矩阵体现。极化中间态的定义利用了 ALMO-CIS 模型（见第 [12.16](sect_ALMO-CIS.md) 节），其中分子轨道（MO）和激发振幅均被定域在各个片段上。我们还指出，激发态相互作用能中的冻结贡献 $\Delta E_{\mathrm{FRZ}}^{\ast}$ 可以进一步细分为经典静电项（孤立片段电荷分布之间的库仑相互作用）和非静电项（若使用如 CIS 这类未做色散校正的模型，则主要为泡利排斥）：

<a id="eq:ex_eda_frz_decomp"></a>

$$
\Delta E_{\mathrm{FRZ}}^{\ast}=\Delta E_{\textrm{CLS-ELEC}}^{\ast}+\Delta E_{\textrm{NON-ELEC}}^{\ast} \tag{12.39}
$$

若要将此方法推广到激发二聚体（excimer），即不同片段处于简并或近简并激发态的情形，则需要做一些修改。在这种情况下，我们选取 $M$ 个参考片段态作为初始基。将片段 $I$ 上的第 $s$ 个激发态记为第 $\kappa$ 个参考态（$\kappa=1,2,\dots,M$）。
类似于式 ([12.35](#eq:ex_e_frag))，我们有

<a id="eq:ex_e_frag_mult"></a>

$$
E_{\mathrm{frag}}^{\kappa}=\sum_{F}E_{F}+\omega_{I}^{s} \tag{12.40}
$$

相应的冻结激发态波函数通过将这一激发片段嵌入由其他处于基态的片段所构成的环境来构造：

<a id="Ch12.E41"></a>

$$
\left|\Phi_{\mathrm{FRZ}}^{\kappa}\right\rangle=\left|\Psi_{1}\Psi_{2}\cdots\Psi_{I}^{s}\cdots\Psi_{N}\right\rangle \tag{12.41}
$$

激发态冻结相互作用能为

<a id="Ch12.E42"></a>

$$
\Delta E_{\mathrm{FRZ}}^{\kappa}=\Delta E_{\mathrm{FRZ}}+\Delta\omega_{\mathrm{FRZ}}^{\kappa}=\Delta E_{\mathrm{FRZ}}+(\omega_{\mathrm{FRZ}}^{\kappa}-\omega_{I}^{s}) \tag{12.42}
$$

基于这 $M$ 个简并或近简并的冻结激发态，引入一个新的中间态，用于捕捉激发二聚体形成过程中纯的激子分裂（EXSP）效应，其可表示为各冻结态的线性组合：

<a id="eq:ex_eda_exsp"></a>

$$
\left|\Phi^{\kappa}_{\mathrm{EXSP}}\right\rangle=\sum_{\kappa^{\prime}}^{M}c^{\kappa\kappa^{\prime}}\left|\Psi_{1}\Psi_{2}\cdots\Psi_{I}^{s}\cdots\Psi_{N}\right\rangle \tag{12.43}
$$

相应的激发能 $\omega^{\kappa}_{\mathrm{EXSP}}$ 及其线性组合系数可通过在冻结态基组下求解久期方程（secular equation）获得。由于激子分裂 purely 是一种激发态现象，我们有

<a id="Ch12.E44"></a>

$$
\Delta E^{\kappa}_{\mathrm{EXSP}}=\Delta\omega^{\kappa}_{\mathrm{EXSP}}=\omega^{\kappa}_{\mathrm{EXSP}}-\omega^{\kappa}_{\mathrm{FRZ}} \tag{12.44}
$$

随后，极化和电荷转移的处理方式与激发二聚体（exciplex，即激发复合物）情形类似：

<a id="A3.S8.EGx125"></a>

$$
\displaystyle\begin{aligned} \displaystyle\Delta E^{\kappa}_{\mathrm{POL}}&\displaystyle=\Delta E_{\mathrm{POL}}+\Delta\omega^{\kappa}_{\mathrm{POL}}=\Delta E_{\mathrm{POL}}+(\omega^{\kappa}_{\mathrm{POL}}-\omega^{\kappa}_{\mathrm{EXSP}})\\
\displaystyle\Delta E^{\kappa}_{\mathrm{CT}}&\displaystyle=\Delta E_{\mathrm{CT}}+\Delta\omega^{\kappa}_{\mathrm{CT}}=\Delta E_{\mathrm{CT}}+(\omega^{\kappa}-\omega^{\kappa}_{\mathrm{POL}})\end{aligned} \tag{12.45}
$$

与激发复合物的 EDA 方案相比，还有一份额外的复杂性：由于考虑了多个（$M$ 个）态，在不同阶段（EXSP、POL 和 CT）需要格外注意态的排序问题。为了在整个 EDA 流程中正确定位所关心的态（这些态在 EXSP 阶段最容易被明确无误地识别），采用了一种基于最大重叠判据的态追踪（state-tracking）算法。更多细节请参见文献 [[434]](../bib_references/bib.md#bib447)。

## 12.7.5.2 作业控制（Job Control）

**Q-Chem** 5.1 中实现的、涉及激发态分子的分子间相互作用的 ALMO-EDA，支持闭壳层体系在 Tamm-Dancoff 近似（TDA）下的 CIS 与 TDDFT，*亦即*，由 TDDFT 计算的激发态以及非限制（unrestricted）体系目前*尚不*支持。EDA 流程通过将 EX_EDA = TRUE 来触发。程序首先经由 “EDA2” 驱动执行一次定制化的基态计算（使用基于 AO 的 ALMO）。在该 EDA 的孤立片段计算过程中，片段激发态会在其基态 SCF 收敛之后一并计算，这由新的输入段 *$frgm_cis_n_roots* 控制。
该输入段的格式如下：

> ```qchem
> $frgm_cis_n_roots
> ¯frgm_idx1¯¯nstates_to_calc¯¯nstates_as_exciton_basis
> ¯frgm_idx2¯¯nstates_to_calc¯¯nstates_as_exciton_basis
> ¯.  .  .
> $end
> ```

其中 “nstates_to_calc” 指定为每个片段计算的态数目（即各片段计算中 CIS_N_ROOTS 的取值），而 “nstates_as_exciton_basis” 指用于构造 EXSP 态的计算所得片段态数目（其求和给出公式 ([12.43](#eq:ex_eda_exsp)) 中的 $M$）。当把超体系（supersystem）视为激发态被指定到某一特定片段的激基复合物（exciplex）时，本段只需要一行即可，且无需指定用作 EXSP 态基底的态数目。

其余相关的 rem 变量包括 CIS_N_ROOTS，它指定在 ALMO-CIS/TDA 以及完整 CIS/TDA 计算中要计算的根（roots）数目；以及 EIGSLV_METH（见第 [12.16](sect_ALMO-CIS.md) 节），其默认值为 1（使用 Davidson 迭代求解器）。需要注意的是，EDA 所关注的态数目由孤立片段的态数目（激基复合物情形）或由发生激子耦合的态的总数（激基缔合物/excimer 情形）来控制。在后一种情形下，通常将 CIS_N_ROOTS 设置为大于 $M$ 的值，以确保所有感兴趣的态都被包含在 ALMO-CIS/TDA 与完整 CIS/TDA 计算之中，因为可能会出现态排序（state-ordering）的变化。

EX_EDA

### `EX_EDA`

> **执行一个含有一个或多个激发片段的 ALMO-EDA 计算。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 执行 EDA，并考虑激发态分子。
>     * FALSE
> * **建议**: 无

???+ example "示例 12.35: 在 CIS/6-31+G(d)
理论水平下对甲酰胺-水复合物的最低两个激发态执行 EDA。两个激发态均归属于甲酰胺分子，
体系被视为激基复合物（exciplex）。"
    ```qchem
    $molecule
    0 1
    --
    0 1
    C         1.1508059365    0.2982718924    0.0240277739
    O         0.3545181649    1.2334803420   -0.0015882208
    N         0.8104369587   -1.0072797234    0.0043506838
    H         2.2327270535    0.4686363261    0.0666232655
    H        -0.1675092286   -1.2596328526   -0.0352400180
    H         1.5210524537   -1.7122494331    0.0139809901
    --
    0 1
    O        -1.9693273428   -0.2999882700   -0.2293071572
    H        -1.3827632725    0.4697313642   -0.1375254289
    H        -2.7470364523   -0.0962178118    0.2907490329
    $end
    
    $rem
       JOBTYPE           eda
       METHOD            hf
       BASIS             6-31+g(d)
       EX_EDA            true
       SCF_CONVERGENCE   8
       CIS_N_ROOTS       2
       CIS_TRIPLETS      false
       THRESH            12
       POINT_GROUP_SYMMETRY false
       INTEGRAL_SYMMETRY    false
    $end
    
    $frgm_cis_n_roots
    1  2
    $end
    
    ```

???+ example "示例 12.36: 在 CIS/6-311(2+,2+)G（自定义）理论水平下计算 He ${}_{2}^{\ast}$ 激基缔合物（excimer）的最低两个态 (1s->2s) 的 EDA。
对每个 He 计算八个激发态，且仅使用最低的一个来构造 EXSP 态，从而得到两个超体系态。"
    ```qchem
    $molecule
    0 1
    --
    0 1
    He    0.0   0.0  0.0
    --
    0 1
    He    3.0   0.0  0.0
    $end
    
    $rem
       JOBTYPE        eda
       EX_EDA         true
       METHOD         hf
       BASIS          gen   !6-311(2+,2+)G
       CIS_N_ROOTS    8
       CIS_TRIPLETS   false
       THRESH         12
       EIGSLV_METH    0   !direct
       POINT_GROUP_SYMMETRY false
       INTEGRAL_SYMMETRY    false
    $end
    
    $frgm_cis_n_roots
    1  8  1
    2  8  1
    $end
    
    $basis
    He   0
    S    3    1.000000
    9.81243000E+01    2.87452000E-02
    1.47689000E+01    2.08061000E-01
    3.31883000E+00    8.37635000E-01
    S    1    1.000000
    8.74047000E-01    1.00000000E+00
    S    1    1.000000
    2.44564000E-01    1.00000000E+00
    SP   1    1.000000
    4.80000000E-02    1.00000000E+00   1.00000000E+00
    SP   1    1.000000
    1.44578313E-02    1.00000000E+00   1.00000000E+00
    ****
    $end
    ```
