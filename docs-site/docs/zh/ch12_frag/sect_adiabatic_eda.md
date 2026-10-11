---
title: "12.7.3 绝热 ALMO-EDA 与 VFB 分析"
---

## 12.7.3 绝热 ALMO-EDA 与 VFB 分析

（2026 年 7 月 4 日）

尽管当今最流行的能量分解分析（Energy Decomposition Analysis, EDA）方法取得了巨大成功并被广泛使用，它们在能力上仍存在一些局限。例如，EDA 通常在复杂的几何结构上进行，而这些几何结构来自无约束的电子结构计算（*e.g.*, 优化后的平衡几何结构）。对于强相互作用体系，由极化（POL）特别是电荷转移（CT）驱动的紧密分子间接触，往往导致极度不利的冻结（FRZ）相互作用项，除了表明分子间存在明显的显著重叠之外，几乎无法提供太多物理洞察。另一个局限是，传统的 EDA 方法通常只对给定几何结构处的“单点”相互作用能进行划分。因此，FRZ、POL 和 CT 对分子间复合物结构与振动性质的影响无法被直接表征。

近期 Mao *et al.* 在绝热图像下重新表述了原始的 ALMO-EDA 方法，[[894]](../bib_references/bib.md#bib928)
 其中“绝热（adiabatic）”一词借用于光谱学，表示能量差是在各个势能面的弛豫几何结构上评估的。在该方案中，总结合能（包括单体几何畸变）被重新划分为绝热 FRZ、POL 和 CT 项：

<a id="eq:ad_EDA"></a>
$$
\Delta E_{\mathrm{bind}}=\Delta E^{(\mathrm{ad})}_{\mathrm{frz}}+\Delta E^{(\mathrm{ad})}_{\mathrm{pol}}+\Delta E^{(\mathrm{ad})}_{\mathrm{ct}}. \tag{12.26}
$$

绝热冻结相互作用能由冻结势能面的能量极小值（该面上每一点的能量均使用相应的冻结波函数计算）与完全弛豫、无相互作用的片段能量之和的差值给出：

<a id="eq:ad_FRZ"></a>
$$
\Delta E^{(\mathrm{ad})}_{\mathrm{frz}}=E[\mathbf{P}_{\mathrm{frz}}^{(\mathrm{frz})}]-\sum_{A}E_{A}^{(0)}. \tag{12.27}
$$

类似地，绝热 POL 和 CT 项可以通过分别在极化（SCF-MI）和完全弛豫（无约束 SCF）势能面上进行几何优化来获得：

<a id="A3.S8.EGx122"></a>
$$
\displaystyle\Delta E^{(\mathrm{ad})}_{\mathrm{pol}} \tag{12.28}
$$

利用该方法，可以提供 FRZ、POL 和 CT 引起的单体结构变化、分子间坐标变化以及相应的能量学信息。此外，在每个势能面的能量极小值（或其他驻点）处，还可以计算多极矩点、振动频率及强度等其他性质，因此不同分子间相互作用分量对这些性质的影响也能够被表征。

在冻结势能面上进行几何优化，得益于 **Q-Chem** 中实现的冻结波函数能量解析梯度。至于在极化势能面上的几何优化，若使用原始 ALMO 模型，SCF-MI 能量的核梯度与完整 SCF 能量的梯度形式相同。这些解析梯度还可用于通过设置 IDERIV = 1 来进行谐振频率的有限差分计算。我们注意到，使用费米-迪拉克正则化函数（Fermi-Dirac Regularized Function, FERF）的 SCF-MI 计算的解析梯度尚不可用，并且在冻结和极化势能面上计算力时需要设置 SCFMI_MODE = 0。此外，该方法的当前实现要求用户在三个势能面上分别进行几何优化（见下方示例），然后综合多个 **Q-Chem** 输出（包括单体的几何优化结果）来评估各能量分量，这可能不太方便。我们期待未来扩展该方法的功能并改进其实现。

如第 [12.6.5](sect_eda2_job.md) 节所述，对于包含高度对称几何结构自由基的体系，通过拼接片段分子轨道（MO）得到的冻结波函数可能不是唯一的。在这些情况下，我们建议用户在冻结势能面上进行几何时，设置 EDA_ALIGN_FRGM_SPIN = 1 或 2。这样，计算任务在每个优化循环中都会执行片段自旋对齐流程。

FRZ_GEOM

### `FRZ_GEOM`

> **在冻结势能面上计算力。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **可选值**:
>     * FALSE
>     * 不在冻结势能面上计算力。
>     * TRUE
>     * 在冻结势能面上计算力。
> * **建议**: 当需要在冻结势能面上获得优化几何结构或振动频率时，将其设置为 TRUE。

### `POL_GEOM`

> **在极化（收敛的 SCF-MI）势能面上计算受力。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **可选值**:
>     * FALSE
>     * 不在极化势能面上计算受力。
>     * TRUE
>     * 在极化势能面上计算受力。
> * **建议**: 当需要在极化势能面上进行几何优化或计算振动频率时，将其设置为 TRUE。

???+ example "示例 12.12.30: 依次在全松弛、极化和冻结势能面上对氨-硼烷配合物进行几何优化。"
    ```qchem
    $molecule
    0 1
    --
    0 1
    H       0.000000     0.000000     0.000000
    H       0.000000     0.000000     1.629090
    H       1.417687     0.000000     0.814543
    N       0.473683    -0.370067     0.814542
    --
    0 1
    N       3.494032    -1.531250     0.814538
    H       3.967715    -1.901317    -0.000008
    H       2.550028    -1.901319     0.814537
    H       3.967715    -1.901317     1.629083
    $end
    
    $rem
       JOBTYPE          opt  !optimization on the fully relaxed PES
       GEN_SCFMAN       true
       METHOD           wb97x-d
       BASIS            6-31+g*
       XC_GRID          1
       THRESH           14
       SCF_CONVERGENCE  9
       SCF_GUESS        fragmo
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE          opt
       POL_GEOM         true !optimization on the polarized PES
       GEN_SCFMAN       true
       METHOD           wb97x-d
       BASIS            6-31+g*
       XC_GRID          1
       THRESH           14
       SCF_CONVERGENCE  9
       SCFMI_MODE       0
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE          opt
       FRZ_GEOM         true !optimization on the frozen PES
       GEN_SCFMAN       true
       METHOD           wb97x-d
       BASIS            6-31+g*
       XC_GRID          1
       THRESH           14
       SCF_CONVERGENCE  9
       SCFMI_MODE       0
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "示例 12.31: 先在冻结势能面上对 [Cu(CO)] ${}^{+}$ 配合物进行几何优化，随后通过有限差分法进行频率计算。"
    ```qchem
    $molecule
    1 1
    --
    0 1
    C         0.0000000000    0.0000000000    1.3792049588
    O         0.0000000000    0.0000000000    2.4988670685
    --
    1 1
    Cu        0.0000000000    0.0000000000   -0.9778656750
    $end
    
    $rem
       JOBTYPE            opt
       FRZ_GEOM           true
       METHOD             b3lyp
       BASIS              def2-svp
       UNRESTRICTED       false
       IDERIV             1
       FD_MAT_VEC_PROD    false
       INTEGRAL_SYMMETRY  false
       POINT_GROUP_SYMMETRY true
    $end
    
    
    @@@
    
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE           freq
       FRZ_GEOM          true
       METHOD            b3lyp
       BASIS             def2-svp
       UNRESTRICTED      false
       IDERIV            1
       FD_MAT_VEC_PROD   false
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY true
    $end
    ```

为了进一步理解给予体（dative）配合物中的电荷转移（charge-transfer, CT）效应，在 **Q-Chem** 5.2.2 及之后的版本中，允许使用变分前向-后向（variational forward-backward, VFB）方法[[857]](../bib_references/bib.md#bib891)将总体 CT 分解为前向捐赠（forward donation）与后向捐赠（backward donation）各自的贡献。
该分解通过引入两个额外的受约束中间态来实现，在这两个态中只允许单一方向的 CT。这两个“单向”CT 态以变分方式得到松弛，因而可以方便地求得相应的核受力。这使得该方案能够轻松地嵌入上文介绍的绝热 ALMO-EDA 格式中：

<a id="A3.S8.EGx123"></a>
$$
\displaystyle\Delta E^{(\mathrm{ad})}_{\mathrm{ctf}} \tag{12.30}
$$

由此，前向捐赠与后向捐赠所引发的分子性质变化可以被分别归属。需要注意的是，在 **Q-Chem** 的实现中，VFB 态的求解总是紧随极化（标准 SCF-MI）计算之后。此外，由于 VFB 态的定义基于广义 SCF-MI 技术（第 [12.6.2](sect_gen_scfmi.md) 节），因此必须设置 SCFMI_MODE = 1。

VFB_CTA

### `VFB_CTA`

> **使用变分前向-后向（Variational Forward-Backward, VFB）方法获得“单向”电荷转移（CT）势能面。**
>
> * **类型**：`STRING`
> * **默认值**：`NONE`
> * **可选值**：
>     * FORWARD
>     * 仅允许 1
>     * $\rightarrow$
>     * 2 方向的 CT（1 和 2 为两个片段）。
>     * BACKWARD
>     * 仅允许 2
>     * $\rightarrow$
>     * 1 方向的 CT。
> * **建议设置**：无

???+ example "示例 12.32: 使用变分前向-后向（VFB）方法在单向 CT 势能面（2 $\to$ 1）上进行几何优化"
    ```qchem
    $molecule
       0 1
       --
       0 1
       O  -1.551007  -0.114520   0.000000
       H  -1.934259   0.762503   0.000000
       H  -0.599677   0.040712   0.000000
       --
       0 1
       O   1.350625   0.111469   0.000000
       H   1.680398  -0.373741  -0.758561
       H   1.680398  -0.373741   0.758561
    $end
    
    $rem
       JOBTYPE           opt
       METHOD            wb97x-d
       BASIS             6-31g
       VFB_CTA           backward
       THRESH            14
       SCF_CONVERGENCE   9
       SCF_ALGORITHM     DIIS
       IDERIV            1
       SCFMI_MODE        1
       INTEGRAL_SYMMETRY FALSE
    $end
    ```

在 **Q-Chem** v. 5.4 及更高版本中，已支持在隐式溶剂模型 PCM 与 SMD 下对极化（polarized）VFB “单向” CT 态以及两个 VFB “单向” CT 态求解析梯（解析梯度），从而可以在溶剂化环境中完成绝热 ALMO-EDA 步骤的一部分（POL $\rightarrow$ CTf/CTb $\rightarrow$ Full）。为此，只需将 *$rem* 变量 SOLVENT_METHOD 设置为 PCM 或 SMD，其用法与 ALMO-EDA(solv) 类似（参见第 [12.6.6](sect_eda2_sol.md) 节）。目前在隐式溶剂下计算冻结（frozen）势能面上的解析力尚不可用，我们期待在 **Q-Chem** 的未来版本中实现该功能。

???+ example "示例 12.33: 在极化势能面上使用 SMD 溶剂模型进行几何优化"
    ```qchem
    $molecule
       0 1
       --
       0 1
       H1
       O1 H1 0.95641
       H2 O1 0.96500  H1 104.77306
       --
       0 1
       O2 H2 dist     O1 171.85474 H1 180.000
       H3 O2 0.95822  H2 111.79807 O1 -58.587
       H4 O2 0.95822  H2 111.79807 O1 58.587
    
       dist = 2.0
    $end
    
    $rem
       JOBTYPE           OPT
       METHOD            wB97X-D
       BASIS             cc-pVDZ
       POL_GEOM          TRUE
       THRESH            14
       SCF_CONVERGENCE   9
       MEM_TOTAL         2000
       MEM_STATIC        500
       SCF_GUESS         FRAGMO
       IDERIV            1
       SCFMI_MODE        0
       SOLVENT_METHOD    SMD
       INTEGRAL_SYMMETRY FALSE
       POINT_GROUP_SYMMETRY FALSE
    $end
    
    $smx
       solvent water
    $end
    ```
