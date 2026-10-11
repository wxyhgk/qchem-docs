---
title: "12.6.6 结合隐式溶剂模型的 ALMO-EDA"
---

## 12.6.6 结合隐式溶剂模型的 ALMO-EDA

（2026 年 7 月 4 日）

由于大多数化学过程发生在凝聚相中，因此在溶剂存在的情况下研究分子间相互作用往往是人们所期望的。溶剂环境会以多种方式影响分子间相互作用，使得气相 ALMO-EDA 可能无法正确揭示这些相互作用的物理图像。为了弥补这一不足，Mao *等*提出了 ALMO-EDA(solv) 方法[[897]](../bib_references/bib.md#bib932)，

与许多其他能量分解分析（EDA）方案不同，该方法在计算所有能量组分时都纳入了溶剂化效应。目前，
ALMO-EDA(solv) 支持两种广泛使用的隐式溶剂模型：
PCM 和 SMD（参见第 [11.2](../ch11_env/topic_solvation.md) 节）。未来的 **Q-Chem**
版本还将兼容更多溶剂化模型。

在 ALMO-EDA(solv) 方案中，待分解的相互作用能由溶剂化且完全弛豫的配合物能量与各别溶剂化、无相互作用的片段能量之和的差值给出。[[897]](../bib_references/bib.md#bib932)

与气相 ALMO-EDA 类似，总相互作用能（INT）可以划分为冻结（FRZ）、极化（POL）和电荷转移（CT）三项贡献：

<a id="A3.S8.EGx119"></a>
$$
\displaystyle\begin{aligned} \displaystyle\Delta E_{\mathrm{INT}}^{(\mathrm{s})}&\displaystyle=E_{\mathrm{Full}}^{(\mathrm{s})}-\sum_{A}E_{A}^{(\mathrm{s})}\\
&\displaystyle=\Delta E^{(\mathrm{s})}_{\mathrm{FRZ}}+\Delta E^{(\mathrm{s})}_{\mathrm{POL}}+\Delta E^{(\mathrm{s})}_{\mathrm{CT}}\end{aligned} \tag{12.18}
$$

这里上标“(s)”表示各能量项在计算时均考虑了溶剂的作用。

冻结相互作用能（$\Delta E_{\mathrm{FRZ}}^{(\mathrm{s})}$）定义为：由若干个别溶剂化的无相互作用片段形成一个溶剂化配合物、但*不*弛豫其轨道时的能量变化，该项还可进一步分解为永久静电作用（ELEC）、Pauli 排斥（PAULI）和色散（DISP）三项贡献：

<a id="A3.S8.EGx120"></a>
$$
\displaystyle\begin{aligned} \displaystyle\Delta E_{\mathrm{FRZ}}^{(\mathrm{s})}&\displaystyle=E_{\mathrm{FRZ}}^{(\mathrm{s})}-\sum_{A}E_{A}^{(\mathrm{s})}\\
&\displaystyle=(E_{\mathrm{FRZ}}^{(\mathrm{s})}-E_{\mathrm{FRZ}}^{(\mathrm{0})})-\sum_{A}(E_{A}^{(\mathrm{s})}-E_{A}^{(0)})+E_{\mathrm{FRZ}}^{(0)}-\sum_{A}E_{A}^{(0)}\\
&\displaystyle=\Delta E_{\mathrm{SOL}}+\Delta E^{(0)}_{\mathrm{ELEC}}+\Delta E^{(0)}_{\mathrm{PAULI}}+\Delta E^{(0)}_{\mathrm{DISP}}\end{aligned} \tag{12.19}
$$

这里我们引入了一个新项，

<a id="Ch12.E20"></a>
$$
\Delta E_{\mathrm{SOL}}=(E_{\mathrm{FRZ}}^{(\mathrm{s})}-E_{\mathrm{FRZ}}^{(\mathrm{0})})-\sum_{A}(E_{A}^{(\mathrm{s})}-E_{A}^{(0)}) \tag{12.20}
$$

用于量化形成冻结配合物时溶剂化能的损失/增益。式 [12.19](#eq:frz_decomp_sol) 中的另外三项，$\Delta E^{(0)}_{\mathrm{ELEC}})$、
$\Delta E^{(0)}_{\mathrm{PAULI}}$ 和 $\Delta E^{(0)}_{\mathrm{DISP}}$，其计算方式与真空中的计算完全相同 [[595]](../bib_references/bib.md#bib619)
（由上标“(0)”标示），
但使用的是溶剂化片段的分子轨道（MOs）。

在最一般的情形下，溶剂对冻结相互作用能的贡献（$\Delta E_{\mathrm{SOL}}$）同时包含静电（$\Delta E_{\mathrm{SOL}}^{\mathrm{el}}$）
和非静电（$\Delta E_{\mathrm{SOL}}^{\text{non-el}}$）两部分，它们可分别与“气相”的 ELEC 和 PAULI 项合并。此外，我们忽略溶剂对色散的贡献——这一效应无法被 ALMO-EDA(solv) 所基于的色散校正 DFT 所捕获——因此有 $\Delta E^{(0)}_{\mathrm{DISP}}\approx\Delta E^{(\mathrm{s})}_{\mathrm{DISP}}$。于是溶剂化环境下冻结能的分解式（式 [12.19](#eq:frz_decomp_sol)）可改写为

<a id="A3.S8.EGx121"></a>
$$
\displaystyle\begin{aligned} \displaystyle\Delta E_{\mathrm{FRZ}}^{(\mathrm{s})}&\displaystyle=(\Delta E^{(0)}_{\mathrm{ELEC}}+\Delta E_{\mathrm{SOL}}^{\mathrm{el}})+(\Delta E^{(0)}_{\mathrm{PAULI}}+\Delta E_{\mathrm{SOL}}^{\text{non-el}})+\Delta E^{(0)}_{\mathrm{DISP}}\\
&\displaystyle=\Delta E^{(\mathrm{s})}_{\mathrm{ELEC}}+\Delta E^{(\mathrm{s})}_{\mathrm{PAULI}}+\Delta E^{(\mathrm{s})}_{\mathrm{DISP}}\end{aligned} \tag{12.21}
$$

从溶剂化的冻结配合物出发，可以在溶剂存在下利用 SCF-MI 技术弛豫片段轨道。相应的能量降低被定义为 ALMO-EDA(solv) 中的极化能（$\Delta E_{\mathrm{POL}}^{(\mathrm{s})}$）：

<a id="Ch12.E22"></a>
$$
\Delta E_{\mathrm{POL}}^{(\mathrm{s})}=E_{\mathrm{POL}}^{(\mathrm{s})}-E_{\mathrm{FRZ}}^{(\mathrm{s})} \tag{12.22}
$$

其中 $E_{\mathrm{POL}}^{(\mathrm{s})}$ 是在溶剂存在下收敛的 SCF-MI 能量。类似地，电荷转移项由下式给出

<a id="Ch12.E23"></a>
$$
\Delta E_{\mathrm{CT}}^{(\mathrm{s})}=E_{\mathrm{Full}}^{(\mathrm{s})}-E_{\mathrm{POL}}^{(\mathrm{s})} \tag{12.23}
$$

其中 $E_{\mathrm{Full}}^{(\mathrm{s})}$ 是在溶剂存在下计算的全 SCF 能量。由此，溶剂化效应被隐式地纳入了 ALMO-EDA(solv) 方案所得到的 POL 项和 CT 项之中。

???+ example "示例 12.17：水-Mg ${}^{2+}$ 配合物在 PCM 水溶液中的 EDA 计算。"
    ```qchem
    $molecule
    2 1
    --
    0 1
    H1
    H2 H1 1.55618
    O1 H2 0.97619  H1 37.14891
    --
    2 1
    Mg1 O1 scan    H2 127.14892  H1 180.0
    
    scan = 1.91035
    $end
    
    $rem
       JOBTYPE           eda
       EDA2              2
       METHOD            wb97m-v
       BASIS             6-31+g(d)
       UNRESTRICTED      false
       SCF_ALGORITHM     diis
       SCF_CONVERGENCE   8
       MAX_SCF_CYCLES    200
       THRESH            14
       SOLVENT_METHOD    pcm
       EDA_CLS_DISP      true
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $PCM
       THEORY                     CPCM
       METHOD                     SWIG
       SOLVER                     INVERSION
       HPOINTS                    302
       HEAVYPOINTS                302
    $END
    
    $SOLVENT
       DIELECTRIC                 78.39
    $END
    ```

???+ example "示例 12.18：水-Mg ${}^{2+}$ 配合物在 SMD 水溶液中的 EDA 计算。"
    ```qchem
    $molecule
    2 1
    --
    0 1
    H1
    H2 H1 1.55618
    O1 H2 0.97619  H1 37.14891
    --
    2 1
    Mg1 O1 scan    H2 127.14892  H1 180.0
    
    scan = 1.91035
    $end
    
    $rem
       JOBTYPE           eda
       EDA2              2
       METHOD            wb97m-v
       BASIS             6-31+g(d)
       UNRESTRICTED      false
       SCF_ALGORITHM     diis
       SCF_CONVERGENCE   8
       MAX_SCF_CYCLES    200
       THRESH            14
       SOLVENT_METHOD    smd
       EDA_CLS_DISP      true
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $smx
       solvent water
    $end
    ```
