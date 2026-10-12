---
title: "12.6.9 与 ALMO-EDA 相关的可视化工具"
---

## 12.6.9 与 ALMO-EDA 相关的可视化工具

(2026 年 7 月 4 日)

EDA2 中启用了以下可视化工具：

- 互补占据-虚轨道对（complementary occupied-virtual pairs, COVP）的自动生成
- 中间态之间（FRZ$\rightarrow$POL、POL$\rightarrow$Full）的电子密度差（electron density difference, EDD）图
- 化学价自然轨道（Natural Orbitals for Chemical Valence, NOCV）图
- 冻结（frozen）与极化（polarized）ALMO 图

如第 [12.5.4 节](sect_covp.md) 所述，COVP 通过展示化学上最相关的供体-受体轨道，
有助于阐明电荷转移过程的细节。在 EDA2 的实现中，
我们启用了最重要的占据-虚轨道对的自动筛选（基于奇异值的阈值）。随后会为这些筛选出的
COVP 生成分子轨道（MO）cube 文件，因此无需指定要绘制哪些轨道。
该新功能可通过设置 EDA_COVP_PRINT = AUTOMATED 来开启。
此外，EDA2 中的自动 COVP cube 生成同时支持 *$plots* 部分的旧格式和新格式。
旧格式需要 MAKE_CUBE_FILES = TRUE，新格式则需要 PLOTS =
TRUE。所绘制的 COVP 以 `covp_a.N.cube` 和
`covp_b.N.cube` 命名索引，而每一对的能量重要性可以从输出文件中查阅。

EDA2 还启用了电子密度差（EDD）图，用于展示极化（$\Delta\mathbf{P}_{\mathrm{pol}}=\mathbf{P}_{\mathrm{pol}}-\mathbf{P}_{\mathrm{frz}}$）和电荷转移（$\Delta\mathbf{P}_{\mathrm{ct}}=\mathbf{P}_{\mathrm{full}}-\mathbf{P}_{\mathrm{pol}}$）过程中电子密度的重新分布。对于非限制（unrestricted）ALMO-EDA 计算，FRZ、POL 以及完全弛豫状态下的自旋密度会一起绘制。
另一个可供可视化的相关量是所谓的化学价自然轨道（NOCV），
[[954]](../bib_references/bib.md#bib995)
其定义为 $\Delta\mathbf{P}=\mathbf{P}_{\mathrm{full}}-\mathbf{P}_{\mathrm{frz}}$ 的本征向量。NOCV 以 $\psi_{k}$ 和 $\psi_{-k}$ 成对出现，其对应的本征值分别为 $n_{k}$ 和
$-n_{k}$。每一对 NOCV 相关的能量降低可以使用扩展过渡态（extended transition state, ETS）方法计算（详见
参考文献 [[954]](../bib_references/bib.md#bib995)
）。NOCV 是阐明化学键中 underlying 轨道相互作用（包括极化与
电荷转移）的有用工具。

在 EDA2 中，当 EDA_PLOT_DIFF_DEN = TRUE 时绘制 EDD 图。
当 EDA_NOCV $>0$ 时执行 NOCV 的计算。
最重要的 NOCV 基于本征值 $\{n_{k}\}$ 的阈值自动筛选。当 EDA_NOCV = 1 时，**Q-Chem** 将仅绘制
每个重要 NOCV 对 ($\psi_{-k}$, $\psi_{k}$) 对密度形变 ($\Delta\rho_{k}$) 的贡献：

<a id="Ch12.E24"></a>

$$
\Delta\rho_{k}(\mathbf{r})=-n_{k}|\psi_{-k}(\mathbf{r})|^{2}+n_{k}|\psi_{k}(\mathbf{r})|^{2} \tag{12.24}
$$

当 EDA_NOCV = 2 时，**Q-Chem** 不仅绘制 NOCV 对对密度形变的贡献，
还会绘制 NOCV 本身。注意，这些可视化需要使用 *$plots* 部分的新格式
（详见第 [10.5.4.1 节](../ch10_properties/sect_plot.mo.md#sec:new-plots)）。

最后，**Q-Chem** 5.2.2 启用了冻结与极化 ALMO 的可视化，
由 *$rem* 变量 PLOT_ALMO_FRZ 和 PLOT_ALMO_POL 控制。
用户需要通过 *$almo_print* 部分为每个片段指定要绘制的轨道：

> ```qchem
> $almo_print
>    frgm_idx1   orb1  orb2 ... (spin)
>    frgm_idx2   orb1  orb2 ... (spin)
>    . . .
> $end
> ```

可以使用“orb1:orb2”格式为每个片段指定要绘制的轨道范围。
对于非限制情况，可以在每行末尾书写“a”或“b”以指定绘制 alpha 还是 beta 轨道
（若未作指定，默认绘制 alpha 轨道）。如上所述，ALMO 的可视化需要采用新格式的 *$plots*
部分。

在下表中，我们总结了每种图所生成的 cube 文件名称。注意，对于 EDD 图，“0”表示 POL 与 FRZ 状态之间的 EDD，
而“1”表示完全 SCF 与 POL 状态之间的 EDD；对于自旋密度图，“0”、”1” 和 ”2” 分别对应 FRZ、POL 和完全弛豫状态。

表 12.1：EDA2 中可视化工具生成的 cube 文件名称

| 图类型 | 轨道类型 | Cube 文件名称 |
| --- | --- | --- |
| COVP | R | covp_a.N.cube |
|  | U | covp_a.N.cube , covp_b.N.cube |
| EDD | R | dens.0.cube , dens.1.cube |
|  | U | dens_alpha.0.cube , dens_alpha.1.cube |
|  |  | dens_beta.0.cube , dens_beta.1.cube |
|  |  | dens_spin.0.cube , dens_spin.1.cube , dens_spin.2.cube |
| NOCV | R | nocv_diffden_a.N.cube , nocv_a.N.cube |
|  | U | nocv_diffden_a.N.cube , nocv_a.N.cube |
|  |  | nocv_diffden_b.N.cube , nocv_b.N.cube |
| ALMO | R | almo_frz_a.N.cube , almo_pol_a.N.cube |
|  | U | almo_frz_a.N.cube , almo_frz_b.N.cube |
|  |  | almo_pol_a.N.cube , almo_pol_b.N.cube |

### `EDA_PLOT_DIFF_DEN`

> **绘制由于 POL（极化）和 CT（电荷转移）引起的电子密度变化图**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不生成 EDD（电子密度差）图
>     * `TRUE`: 生成 EDD（电子密度差）图
> * **建议**: 无

### `EDA_NOCV`

> **执行 NOCV 分析并绘制重要的 NOCV（自然轨道对化学键, Natural Orbitals for Chemical Valence）**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 不执行 NOCV 分析
>     * `1`: 绘制 NOCV 对密度形变（density deformation）的贡献
>     * `2`: 同时绘制 NOCV 对密度形变的贡献及 NOCV 轨道
> * **建议**: 无

### `PLOT_ALMO_FRZ`

> **在 EDA2（能量分解分析第二版, Energy Decomposition Analysis 2）计算的冻结（frozen）阶段绘制 ALMO（定域分子轨道, Absolutely Localized Molecular Orbitals）**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不绘制冻结态 ALMO
>     * `TRUE`: 绘制冻结态 ALMO
> * **建议**: 无

### `PLOT_ALMO_POL`

> **在极化（polarization）计算之后绘制 ALMO**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不绘制极化态 ALMO
>     * `TRUE`: 绘制极化态 ALMO
> * **建议**: 无

???+ example "示例 12.24: 通过 EDA2 执行微扰 CTA（约束轨道对, Constrained Transition-amplitude）计算（使用默认设置）。通过设置 EDA_PRINT_COVP = AUTOMATED 来启用自动 COVP（正则化轨道对, Canonical Orbital-Pair）生成，可自动绘制最重要的 COVP。通过设置 PLOTS = TRUE 使用新版 $plots 区块格式，无需指定要绘制的轨道数目。"
    ```qchem
    $molecule
       0 1
       --
       0 1
       O      -1.521720     0.129941     0.000000
       H      -1.924536    -0.737533     0.000000
       H      -0.571766    -0.039961     0.000000
       --
       0 1
       O       1.362840    -0.099704     0.000000
       H       1.727645     0.357101    -0.759281
       H       1.727645     0.357101     0.759281
    $end
    
    $rem
       JOBTYPE               EDA
       METHOD                B3LYP
       BASIS                 6-31+G(d)
       MEM_TOTAL             8000
       MEM_STATIC            2000
       BASIS_LIN_DEP_THRESH  6
       THRESH                14
       SCF_CONVERGENCE       8
       MAXSCF                200
       EDA_COVP              TRUE
       EDA_PRINT_COVP        AUTOMATED !auto-generation of covp cube files
       MAKE_CUBE_FILES       TRUE
       PLOTS                 TRUE      !new format for the plot section
       INTEGRAL_SYMMETRY     FALSE
       POINT_GROUP_SYMMETRY  TRUE
    $end
    
    $plots
       GRID_POINTS           100 100 100
    $end
    ```

???+ example "示例 12.25: NH ${}_{3}\cdots$ BH ${}_{3}$ 复合物的电子密度差（EDD）图及 NOCV 分析。同时绘制了重要的 NOCV 对，以及每一对轨道相互作用（极化与电荷转移）对密度形变的贡献。"
    ```qchem
    $molecule
    0 1
    --
    0 1
    N         0.0000001517    0.7279666667    0.0000000000
    H         0.9488005016    1.0881357449    0.0000000000
    H        -0.4743994984    1.0881371276   -0.8216800000
    H        -0.4743994984    1.0881371276    0.8216800000
    --
    0 1
    B        -0.0000014567   -0.9275533333    0.0000000000
    H        -1.1719117610   -1.2408021948    0.0000000000
    H         0.5859582390   -1.2408039026   -1.0149100000
    H         0.5859582390   -1.2408039026    1.0149100000
    $end
    
    $rem
       JOBTYPE                 eda
       EDA2                    2   !ALMO-POL
       METHOD                  b3lyp
       BASIS                   6-31g(d)
       SCF_ALGORITHM           diis
       XC_GRID                 1
       SCF_CONVERGENCE         8
       MAX_SCF_CYCLES          200
       THRESH                  14
       EDA_PLOT_DIFF_DEN TRUE  !plot EDD maps
       EDA_NOCV  2             !NOCV analysis
       INTEGRAL_SYMMETRY       false
       POINT_GROUP_SYMMETRY    false
    $end
    
    $plots
    grid_points 100 100 100
    $end
    ```

???+ example "示例 12.26: 在 EDA2 计算中绘制每个片段的 HOMO（最高占据分子轨道）和 LUMO（最低未占分子轨道）（冻结态与极化态 ALMO）"
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
       JOBTYPE          eda
       METHOD           b3lyp
       BASIS            6-31g
       EDA2             2   !ALMO-POL
       UNRESTRICTED     false
       SCF_ALGORITHM    diis
       SCF_CONVERGENCE  8
       MAX_SCF_CYCLES   200
       THRESH           14
       PLOT_ALMO_FRZ    true
       PLOT_ALMO_POL    true
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $almo_print
    1 5:6
    2 5:6
    $end
    
    $plots
    grid_points 60 60 60
    $end
    ```
