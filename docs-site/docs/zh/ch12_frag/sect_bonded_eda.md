---
title: "12.7.2 用于成键相互作用的 ALMO-EDA"
---

## 12.7.2 用于成键相互作用的 ALMO-EDA

（2026 年 7 月 4 日）

能量分解分析（Energy Decomposition Analysis, EDA）方案在阐明非共价相互作用本质方面取得了巨大成功。然而，这些方法用于分析共价键时往往力不从心。在基于片段的方案中，关键困难在于需要以自旋纯（spin-pure）的方式将两个开壳层自由基片段正确地自旋耦合为一个闭壳层化学键。Levine 将 ALMO-EDA 方法学进行了扩展，从而在 HF 和 KS DFT 框架内实现了这一目标[[810]](../bib_references/bib.md#bib841)。若使用 HF，则被分解相互作用能所对应的最终波函数为 CAS(2,2)/单对完全配对（perfect-pairing）/TCSCF 波函数。目前，这些方案只能分析单个化学键。

该方法从两个双重态（doublet）自由基片段出发，每个片段均由一个受限开壳层（restricted open-shell, RO）Hartree-Fock（HF）或 Kohn-Sham DFT 单行列式描述。在成键 EDA 方案中，由于轨道重杂化（re-hybridization）在能量中可能扮演如此重要的角色，$\Delta E_{\text{PREP}}$ 既包含将每个自由基片段扭曲至其在成键态中所采用几何构型所需的能量 $\Delta E_{\text{GEOM}}$，也包含源于轨道重杂化的电子制备能 $\Delta E_{\text{HYBRID}}$。例如，F 原子的未成对电子位于一个 $p$ 轨道中，而处于化学键中的 F 原子则为 $sp$ 杂化。胺自由基 NH${}_{2}$ 为 $sp^{2}$ 杂化，未成对电子位于 $p$ 轨道中；而分子中的胺基通常为 $sp^{3}$ 或 $sp^{2}$ 杂化，$p$ 轨道中容纳一对孤对电子。于是，

<a id="Ch12.E25"></a>

$$
\Delta E_{\text{PREP}}=\Delta E_{\text{GEOM}}+\Delta E_{\text{HYBRID}} \tag{12.25}
$$

这一重杂化态通过对由片段构成的 ALMO 超体系（supersystem）进行弛豫而获得，仅允许片段内的双占据–单占据轨道旋转（由于片段的 RO 特性，这类旋转是良定义的）。如此优化后的片段再次分离，电子受扰片段与基态片段之间的能量差即为 $\Delta E_{\text{HYBRID}}$。这相当于固定 $\alpha$ 密度、并允许 $\beta$ 空穴（$\beta$-hole）在该 $\alpha$ 密度张成的空间内重新优化。这是一种极化，尽管我们将其与成键和非成键 ALMO 方案中后续出现的电子极化步骤区分开来。将重杂化能量置于此处的另一个合理性在于：由于自由基片段的几何构型被固定为相互作用片段的构型，该项能量已经在一定程度上被计入。例如，游离的甲基自由基是 $sp^{2}$ 杂化的平面分子，而化学键中的甲基则是锥形化的 $sp^{3}$ 片段；重杂化代价已经由几何扭曲支付了。

成键方案中的 FRZ（冻结）能量对应于将各 RO 片段组合而成、但不允许轨道进一步弛豫的自旋纯三重态单行列式波函数所构成的 ALMO 超体系。这一项完全是非成键相互作用，并且由于泡利（Pauli）排斥，对化学键而言通常呈排斥性。它包含片段间静电作用、泡利排斥、交换-关联和色散的贡献。自旋投影形式体系下可将 EDA2 冻结分解方案应用于该项（*即*，BONDED_EDA = 2）。

成键 EDA 方案引入了一个新项：自旋耦合（spin-coupling）能量 $\Delta E_{\text{SC}}$。这一能量差由电子配对引起，粗略地对应于共价性的概念。与 FRZ 类似，SC 也采用冻结轨道来计算；但 FRZ 通常呈强排斥性（由泡利排斥主导），而 SC 在与共价键形成相关的重叠区域中通常呈强吸引性。基于这一原因，并且因为我们主要关心的是单重态势能面（而非初始超体系的三重态势能面），FRZ 和 SC 可以合并为一个总冻结轨道项（FRZ + SC）。

在 KS DFT 方案中[[809]](../bib_references/bib.md#bib843)
，该自旋耦合波函数由对称性破缺 DFT 行列式构造，并通过自旋投影剔除三重态污染组分而得到。由于波函数由 RO 片段构建，自旋污染只能发生在半占据空间内，因而三重态是唯一可能出现的污染。于是我们得到一个精确的单重态波函数。对于 HF，只要片段之间仅有两个未成对自旋（*即*超体系为闭壳层），该方案就与基于非正交组态相互作用（CI）的[[810]](../bib_references/bib.md#bib841)
方案完全等价。这通常是成立的情形，因此既然两种方案等价，我们主张只使用自旋投影形式体系，因其效率要高得多。

POL（极化）项和 CT（电荷转移）项的定义与非成键 ALMO 方案中的类似。可使用冻结电子排斥泛函（Frozen Electron Repulsion Functional, FERF）来定义极化，但应纳入单极（monopole）FERF，其描述轨道的膨胀或收缩（在某些情况下，这一过程在成键时会发生）。[[808]](../bib_references/bib.md#bib842)

CT 项给出了键中离子性程度的指示。综合各项共同构成所研究化学键的"指纹"。有关如何分析结果的更多细节可参阅相关文献。

使用成键 ALMO-EDA 的注意事项：

- 必须设置 SCFMI_MODE = 1。
- 必须设置 ROSCF = TRUE。
- 成键 ALMO-EDA 没有预设（presets）。因此请设置 EDA2 = 10。
- SCF_ALGORITHM 不得使用 DIIS。当 BONDED_EDA = 2 时使用 GDM_LS，当 BONDED_EDA = 1 时使用 L_BFGS。

### `BONDED_EDA`

> **使用键合 ALMO-EDA。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * `0`: 不执行键合 ALMO-EDA。
>     * `1`: 使用非正交组态相互作用（non-orthogonal CI）执行 ALMO-EDA。
>     * `2`: 使用自旋投影形式体系（spin-projected formalism）执行 ALMO-EDA。
> * **建议**: 当超体系（supersystem）为闭壳层（closed shell）时，所有情况均设置为 2；仅当各碎片（fragment）各自拥有多于一个未配对电子时才使用 1。

### `EDA_CONTRACTION_ANAL`

> **执行将轨道收缩（orbital contraction）与 POL（极化，Polarization）中其余部分分离的分析。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `0`
> * **可选值**:
>     * `FALSE`: 不执行收缩分析。
>     * `TRUE`: 执行收缩分析。
> * **建议**: 无特别建议

???+ example "示例 12.28: 使用 MDQ FERF 对 F ${}_2$ 进行键合 EDA，在自旋投影形式体系下进行冻结分析"
    ```qchem
    $molecule
       0 3
       --
       0 2
       F 0.0 0.0 0.0
       --
       0 2
       F 0.0 0.0 1.382
    $end
    
    $rem
       JOBTYPE              eda
       EXCHANGE             wb97x-d
       BASIS                aug-cc-pvdz
       EDA2                 10
       BONDED_EDA           2
       SCF_CONVERGENCE      6
       MAX_SCF_CYCLES       200
       ROSCF                true
       SCF_GUESS            fragmo
       SCF_ALGORITHM        gdm_ls
       SCFMI_MODE           1
       SCF_PRINT_FRGM       true
       CHILD_MP             true
       CHILD_MP_ORDERS      1233
       FRZ_RELAX            true
       FRZ_RELAX_METHOD     2
       FRZ_ORTHO_DECOMP     false
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
       EDA_CLS_ELEC         true
    $end
    
    $rem_frgm
       scf_convergence   7
       scf_algorithm     gdm_ls
       scf_guess         sad
    $end
    ```

???+ example "示例 12.29: 使用 MDQ FERF 对 CH 进行键合 EDA，在非正交 CI 形式体系下进行收缩分析。"
    ```qchem
    $molecule
       0 4
       --
       0 3
       C         0.0000000000    0.0000000000   -0.0525358999
       --
       0 2
       H         0.0000000000    0.0000000000    1.0525358999
    $end
    
    $rem
       JOBTYPE                eda
       EXCHANGE               hf
       BASIS                  aug-cc-pvdz
       EDA2                   10
       BONDED_EDA             1
       SCF_CONVERGENCE        6
       MAX_SCF_CYCLES         2000
       ROSCF                  true
       SCF_GUESS              fragmo
       SCF_ALGORITHM          l_bfgs
       SCFMI_MODE             1
       SCF_PRINT_FRGM         true
       CHILD_MP               true
       CHILD_MP_ORDERS        1233
       FRZ_RELAX              true
       FRZ_RELAX_METHOD       2
       EDA_CONTRACTION_ANAL   true
       INTEGRAL_SYMMETRY      false
       POINT_GROUP_SYMMETRY   false
    $end
    
    $rem_frgm
       scf_convergence   7
       scf_algorithm     gdm_ls
       scf_guess         sad
    $end
    ```

（已同步保存至 `QChem/BONDED_EDA.md`）
