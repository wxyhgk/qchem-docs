---
title: "10.2.12 通用激发态分析"
---

## 10.2.12 通用激发态分析

（2026 年 7 月 4 日）

**Q-Chem** 具备一个通过波函数分析库 **libwfa** 进行扩展激发态分析的模块。[[1096]](../bib_references/bib.md#bib1146)
**libwfa** 已与 ADC、CC/EOM-CC、CIS 以及 TDDFT/SF-TDDFT
方法对接。这些分析基于激发态的态密度矩阵、跃迁密度矩阵和差密度矩阵。此类分析的理论背景见第 [7.13](../ch07_excited/sec_ES_visual.md) 章。
关于不同激发态分析方法与分类方案的更详细讨论，以及 TDDFT 计算中可视化工具与电荷转移度量的综述，可参阅文献。[[572]](../bib_references/bib.md#bib586)

| 描述符 | 说明 |
| --- | --- |
| 主要奇值（Leading singular values） | 最大的 NTO 占据数 |
| 奇值之和（Omega） | $\Omega=\\|\bm{\gamma}^{\text{IF}}\\|^{2}$ ，NTO 占据数之和 |
| E(h) | 空穴（hole）NTO 的能量，$E_{I}(\text{h})=\sum_{pq}\alpha_{pI}F_{pq}\alpha_{qI}$ |
| E(p) | 粒子（particle）NTO 的能量，$E_{I}(\text{p})=\sum_{pq}\beta_{pI}F_{pq}\beta_{qI}$ |
| PR_NTO | NTO 参与比 $\mbox{PR}_{\text{NTO}}$ |
| 纠缠熵（S_HE） | $S_{H\|E}=-\sum_{i}\lambda_{i}\log_{2}\lambda_{i}$ |
| 纠缠态数目（Z_HE） | $Z_{HE}=2^{S_{H\|E}}$ |
| 重正化的 S_HE/Z_HE | 将上述两个公式中的 $\lambda_{i}\rightarrow\lambda_{i}/\Omega$ 替换 |
| <Phe> | 粒子-空穴置换算符的期望值，用于度量退激发 |
|  | （de-excitations）[[686]](../bib_references/bib.md#bib711) |
| <r_h> [Ang] | 空穴的平均位置 $\langle\vec{x}_{\text{h}}\rangle_{\text{exc}}$ |
| <r_e> [Ang] | 电子的平均位置 $\langle\vec{x}_{\text{e}}\rangle_{\text{exc}}$ |
| \|<r_e - r_h>\| [Ang] | 电子–空穴距离，$\vec{d}_{\text{e-h}}=\\|\langle\vec{x}_{\text{e}}-\vec{x}_{\text{h}}\rangle\\|$ |
| 空穴尺寸 [Ang] | 空穴的均方根（RMS）尺寸：$\sigma_{\text{h}}=(\langle\vec{x}_{\text{h}}^{\,2}\rangle_{\text{exc}}-\langle\vec{x}_{\text{h}}\rangle_{\text{exc}}^{2})^{1/2}$ |
| 电子尺寸 [Ang] | 电子的均方根尺寸：$\sigma_{\text{e}}=(\langle\vec{x}_{\text{e}}^{\,2}\rangle_{\text{exc}}-\langle\vec{x}_{\text{e}}\rangle_{\text{exc}}^{2})^{1/2}$ |
| 电子-空穴均方根间距 [Ang] | $d_{\text{exc}}=\big{(}\big{\langle}\\|\vec{x}_{\text{e}}-\vec{x}_{\text{h}}\\|^{2}\big{\rangle}_{\text{exc}}\big{)}^{1/2}$ |
| 电荷位移度量 1 | $d_{\text{CD1}}=d_{\text{e-h}}+\|\sigma_{\text{h}}-\sigma_{\text{e}}\|$ |
| 电荷位移度量 2 | $d_{\text{CD2}}=d_{\text{e-h}}-\tfrac{1}{2}\big{(}\sigma_{\text{h}}+\sigma_{\text{e}}\big{)}$ |
| 电荷位移度量 3 | $d_{\text{CD3}}=d_{\text{e-h}}+d_{\text{exc}}$ |
| 协方差(r_h, r_e) [Ang^2] | $\mbox{COV}\left(\vec{x}_{\text{h}},\vec{x}_{\text{e}}\right)=\langle\vec{x}_{\text{h}}\bm{\cdot}\vec{x}_{\text{e}}\rangle_{\text{exc}}-\langle\vec{x}_{\text{h}}\rangle_{\text{exc}}\bm{\cdot}\langle\vec{x}_{\text{e}}\rangle_{\text{exc}}$ |
| 相关系数 | $R_{\text{eh}}=\mbox{COV}\left(\vec{x}_{\text{h}},\vec{x}_{\text{e}}\right)/\sigma_{\text{h}}\bm{\cdot}\sigma_{\text{e}}$ |
| 质心尺寸 | $\tfrac{1}{2}\big{(}\big{\langle}\\|\vec{x}_{\text{e}}+\vec{x}_{\text{h}}\\|^{2}\big{\rangle}_{\text{exc}}-\langle\vec{x}_{\text{e}}+\vec{x}_{\text{h}}\rangle_{\text{exc}}^{2}\big{)}^{1/2}$ |

表 10.1：
**Q-Chem** 针对跃迁密度矩阵分析输出的描述符。注意，打印的是奇值的平方，
其对应于各 NTO 对的权重。$\Omega$ 等于单电子跃迁密度矩阵（1TDM）范数的平方。
电荷位移度量 $d_{\text{CD}n}$ 的定义见文献 [[563]](../bib_references/bib.md#bib587)。

基于单电子跃迁密度矩阵（1TDM）的分析包括：自然跃迁轨道（NTO）[[913]](../bib_references/bib.md#bib947)

的构造与导出、电子密度和空穴密度 [[1099]](../bib_references/bib.md#bib1142)

、电荷转移数（charge transfer numbers）的评估 [[1097]](../bib_references/bib.md#bib1141)

、激子多极矩（exciton multipole moments）分析 [[74]](../bib_references/bib.md#bib43)

以及电子–空穴纠缠程度的量化 [[1100]](../bib_references/bib.md#bib1145)。

NTO 是通过对 1TDM 进行奇异值分解（SVD）获得的：[[572]](../bib_references/bib.md#bib586)

<a id="A3.S8.EGx77"></a>

$$
\displaystyle\gamma^{\text{IF}}_{pq} \tag{10.34}
$$

其中 $\bm{\sigma}$ 是包含奇值的对角矩阵，酉矩阵 $\bm{\alpha}$ 和 $\bm{\beta}$ 分别包含相应的粒子 NTO 和空穴 NTO。注意：

<a id="Ch10.E36"></a>

$$
\|\bm{\gamma}\|^{2}=\sum_{pq}\gamma_{pq}^{2}=\sum_{K}\sigma_{K}^{2}\equiv\Omega \tag{10.36}
$$

此外，还实现了态平均（state-averaged）NTO 的生成与导出，以及将激发态分解为态平均 NTO 之间的跃迁。[[1099]](../bib_references/bib.md#bib1142)
 差密度和/或态密度本身既可以导出，也可用于构造并导出自然轨道（natural orbitals）、自然差轨道（natural difference orbitals）以及附着（attachment）与剥离（detachment）密度。[[572]](../bib_references/bib.md#bib586)
 另外，还会计算两种未成对电子的度量。[[546]](../bib_references/bib.md#bib560)
 此外，还可以基于差密度/态密度进行 Mulliken 或 Löwdin 布居分析以及激子分析。[[572]](../bib_references/bib.md#bib586)
 针对每个激发态打印的各项分析的主要描述符见表 [10.1](#table:TDM-analysis) 和表 [10.2](#table:density-analysis)。
详细说明及示例可参阅文献。[[1099]](../bib_references/bib.md#bib1142)

注意，这些描述符对轨道旋转是不变的，这与第 [7.3.2](../ch07_excited/sec_CT-metrics.md) 节所讨论的某些标准电荷转移度量不同。[[563]](../bib_references/bib.md#bib587)

| 描述符 | 说明 |
| --- | --- |
| n_u | 未成对电子数 $n_{\text{u}}=\sum_{i}\mbox{min}(n_{i},2-n_{i})$ |
| n_u,nl | 未成对电子数 $n_{\text{u,nl}}=\sum_{i}n_{i}^{2}(2-n_{i})^{2}$ |
| PR_NO | 自然轨道（NO）参与比 $\mbox{PR}_{\text{NO}}$ |
| p_D 和 p_A | 激发数（promotion number）$p_{\text{D}}$ 和 $p_{\text{A}}$ |
| PR_D 和 PR_A | 给体/受体（D/A）参与比 $\mbox{PR}_{\text{D}}$ 和 $\mbox{PR}_{\text{A}}$ |
| <r_h> [Ang] | 剥离密度的平均位置 $\vec{d}_{\text{D}}$ |
| <r_e> [Ang] | 附着密度的平均位置 $\vec{d}_{\text{A}}$ |
| \|<r_e - r_h>\| [Ang] | 线性给体/受体距离 $\vec{d}_{\text{D}\to\text{A}}=\vec{d}_{\text{A}}-\vec{d}_{\text{D}}$ |
| 空穴尺寸 [Ang] | 剥离密度的均方根尺寸 $\sigma_{\text{D}}$ |
| 电子尺寸 [Ang] | 附着密度的均方根尺寸 $\sigma_{\text{A}}$ |

表 10.2：
**Q-Chem** 针对差密度/态密度矩阵分析输出的描述符。

**libwfa** 还计算用于区分双自由基（diradical）激发态与离子型（ionic）激发态的描述符，其定义基于价键（valence-bond）理论。
这些描述符记为 `LOC`、`LOCa`、`QT` 和 `QTa`，对于理想的双自由基态其值为零，并随态的离子性增强而增大。[[341]](../bib_references/bib.md#bib355)

要启用任何激发态分析，必须将 STATE_ANALYSIS 设置为 TRUE。对于各项单独的分析，目前仅提供了有限的细粒度控制。任意类型轨道的构造与导出由 MOLDEN_FORMAT 控制（将轨道导出为 **MolDen** 文件），以及由 NTO_PAIRS 指定要打印的重要轨道数目（注意，同一关键字同时控制自然轨道、自然差轨道以及 NTO 的打印数目）。将 MAKE_CUBE_FILES 设置为 TRUE
会触发以“cube 文件”格式构造并导出密度，

 这需要在 *$plots* 区段中以旧格式或新格式进行指定（详见第 [10.5.4](sect_plot.mo.md) 节和第 [10.5.5](sec_cubefiles.md) 节）。
设置 IQMOL_FCHK = TRUE（等价于 GUI = 2）会将数据导出到“`.fchk`”格式检查点（formatted checkpoint）文件，并关闭 cube 文件的生成。布居分析由 POP_MULLIKEN 和 LOWDIN_POPULATION 控制。将后者设置为 TRUE
会对常规布居以及电荷转移（CT）数强制采用 Löwdin 布居分析，而默认使用 Mulliken 布居分析。

由激发态分析生成的任何 **MolDen** 或 cube 文件均位于作业临时（scratch）目录下的 `plots` 目录中。其文件名总是以激发态的唯一标识符开头（该可读标识符的确切形式随激发态方法而异）。**MolDen** 文件的名称随后根据其所含轨道类型分别以 `_no.mo`、`_ndo.mo` 或 `_nto.mo` 结尾。对于 cube 文件，态标识符之后依次为 `_dens`、`_diff`、`_trans`、`_attach`、`_detach`、`_elec` 或 `_hole`，分别对应态密度、差密度、跃迁密度、附着密度、剥离密度、电子密度或空穴密度。所有 cube 文件的后缀均为 `.cube`。在非限制性（unrestricted）计算中，文件名在 `.cube` 之前还会附加一部分以指示 $\alpha$（`_a`）或 $\beta$（`_b`）自旋。唯一的例外是态密度，其文件名附加 `_tot` 或 `_sd` 以指示态密度的总密度部分或自旋密度部分。对松弛（relaxed）CIS 或 TDDFT 密度的分析可通过 CIS_RELAXED_DENSITY = TRUE 触发。
相应的输出文件以 `_rlx` 标记。对态密度、跃迁密度以及电子/空穴密度计算静电势（ESP）（见文献 [[686]](../bib_references/bib.md#bib711)）可通过
设置 ESP_GRID = $-3$ 触发。
这些文件以文件名中包含 `_esp` 来标识。

主目录下生成的 `ctnum_*.om` 文件用作电荷转移数分析的输入，具体说明可参见文献，*e.g.*，[[1097]](../bib_references/bib.md#bib1141)。
使用外部程序 `TheoDORE`（`theodore-qc.sourceforge.net`）可以创建电子/空穴关联图并计算基于片段（fragment）的描述符。

**注意：

•

当从开壳层（open-shell）参考态进行激发态计算时，**libwfa** 会同时对 $\alpha\alpha$ 和 $\beta\beta$ 跃迁密度执行分析。请务必查看正确的部分。判断方法是记住：在开壳层参考态中 $N_{\alpha}>N_{\beta}$，*e.g.*，在双重态（doublet）参考态中，未成对电子为 $\alpha$ 自旋，空穴为 $\beta$ 自旋。因此，对于未成对电子跃迁到未占据轨道的跃迁，需要查看 $\alpha\alpha$ 块；而对于从双占据轨道跃迁到 singly unoccupied 轨道（即空穴）的跃迁，需要查看 $\beta\beta$ 块。

•

要在 CCMAN2 作业中启用所有类型的分析，必须激活 CC_REF_PROP、CC_EOM_PROP 和 CC_TRANS_PROP。
示例 [7.9.30](../ch07_excited/ex_eomip-wfa.md) 展示了这一点。

•

在厄米（Hermitian）形式体系中，$\gamma^{\text{IF}}$ 是 $\gamma^{\text{FI}}$ 的厄米共轭；但在非厄米方法（如耦合簇理论）中，两者略有不同。虽然对于定量的态间性质会同时计算 $\gamma^{\text{IF}}$ 和 $\gamma^{\text{FI}}$，但由 $(\gamma^{\text{IF}})^{\dagger}$ 与 $\gamma^{\text{FI}}$ 导出的激子性质定性趋势非常相似。对于 EOM-CC，仅分析一个 1TDM。

•

在限制性（spin-restricted）计算中，**libwfa** 模块仅对跃迁密度的 $\alpha\alpha$ 块计算 NTO。因此，在计算开壳层 EOM-IP/EA 态之间跃迁的 NTO 时，请务必指定正确的自旋态。例如，使用 EOM_EA_ALPHA 来可视化涉及额外电子的跃迁。

**

### `STATE_ANALYSIS`

> **通过 libwfa 触发通用态分析。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不运行激发态分析。
>     * `TRUE`: 激活激发态分析。
> * **建议**: 该分析仅产生极小的计算开销（在不生成 cube 文件的情况下），当需要有关激发态的额外信息时即可启用。

### `WFA_LEVEL`

> **控制 libwfa 输出量的主控变量。**
>
> * **类型**: `INTEGER`
> * **默认值**: `3`
> * **选项**:
>     * `1`: 仅执行部分布居分析。
>     * `2`: 同时执行激子分析并计算自然（跃迁/差）轨道。
>     * `3`: 同时执行电荷转移数分析。
>     * `4`: 最大输出，包括 NTO 的 cube 文件（复现文献
>     * `686`: Kimber P., Plasser F. Phys. Chem. Chem. Phys. (2020) ,
>     * `22`: , pp. 6058 链接时需要此级别）
> * **建议**: 若希望减少打印输出，请降低该值。

### `NTO_PAIRS`

> **控制在标准输出中打印多少对空穴/粒子 NTO、前线自然轨道对以及自然差轨道对。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $N$: 为每个激发态写出 $N$ 对 NTO/NO/NDO。
> * **建议**: 该关键字控制标准输出的打印内容。若想修改导出的轨道数目，请使用 WFA_ORB_THRESH。

### `WFA_ORB_THRESH`

> **控制导出到 Molden 文件中的空穴/粒子 NTO 对、前线自然轨道对以及自然差轨道对的数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `3`
> * **选项**:
>     * $N$: 导出所有权重大于 $10^{-N}$ 的 NTO/NO/NDO 对。
### `WFA_REF_STATE`

> **控制 libwfa 所使用的跃迁密度矩阵和差密度矩阵的参考态。该关键字适用于 CIS/TDDFT/SF-TDDFT 计算。EOM-CC 请使用 CC_STATE_TO_OPT。**
>
> * **类型**: `INTEGER`
> * **默认值**: `-1`
> * **选项**:
>     * `-1`: 使用默认值：标准 CIS/TDDFT 计算使用基态， SF-TDDFT 使用第一个响应态。
>     * `0`: 参考态
>     * `N`: 第 $N$ 个激发态/响应态。
> * **建议**: 无

???+ example "示例 10.7: 甲醛在 ADC(2)/def2-SV(P) 水平下的基本激发态分析示例：计算各种描述符，并以 MolDen 格式输出 NO、NTO 和 NDO。libwfa 在此基本模式下通常不会增加明显的计算成本。"
    ```qchem
    $molecule
       0 1
       C     0.000000   0.000000    0.523383
       O    -0.000000   0.000000   -0.671856
       H     0.931138   0.000000    1.11728
       H    -0.931138   0.000000    1.11728
    $end
    
    $rem
       METHOD           adc(2)
       BASIS            def2-sv(p)
       N_FROZEN_CORE    fc
       EE_SINGLETS      [0,1,1,0]
       STATE_ANALYSIS   true
       MOLDEN_FORMAT    true
    $end
    ```

???+ example "示例 10.8: 使用 libwfa 分析甲醛的两个 TDDFT 激发态，包括 cube 文件输出。
本例使用新版 $plots 格式（见第 10.5.4.1 节），并指定了网格点。
HOMO 和 LUMO 的 cube 文件也会生成。"
    ```qchem
    $molecule
    0 1
      C    0.0000000   -0.0000000   -0.6133791
      O   -0.0000000    0.0000000    0.6060734
      H    0.0000000    0.9391300   -1.1555819
      H    0.0000000   -0.9391300   -1.1555819
    $end
    
    $rem
       METHOD           PBE0
       BASIS            6-31+G(d)
       CIS_N_ROOTS      2
       CIS_TRIPLETS     false
       MAKE_CUBE_FILES  true
       PLOTS            true
       STATE_ANALYSIS   true
    $end
    
    $plots
       grid_points                    50 50 50
       alpha_molecular_orbital        8-9
    $end
    ```

**注意：

对于轨道和密度的输出，可以使用 MOLDEN_FORMAT = TRUE
（见示例 10.2.12）、
MAKE_CUBE_FILES = TRUE
（见示例 10.2.12）
或 GUI = 2 选项。
当 STATE_ANALYSIS 被激活时，这些选项互斥。
**

???+ example "示例 10.9: 尿嘧啶（Uracil）在 PBE0/def2-SV(P) 水平下的计算。启用 libwfa 的扩展功能，包括以 cube 格式导出 NTO 和密度，并计算这些密度的 ESP。
libwfa 的这种扩展模式会显著增加计算成本，尤其是在选择精细网格时。"
    ```qchem
    $molecule
       0 1
       C    1.194380    1.102510    0.000000
       C   -0.008366    1.692430    0.000000
       N   -1.169600    0.978035    0.000000
       C   -1.212060   -0.402293    0.000000
       N    0.034691   -0.979140    0.000000
       C    1.281590   -0.348737    0.000000
       O   -2.243420   -1.023750    0.000000
       O    2.299180   -0.995854    0.000000
       H   -0.123160    2.767140    0.000000
       H   -2.061440    1.444100    0.000000
       H    0.044818   -1.989990    0.000000
       H    2.104720    1.679840    0.000000
    $end
    
    $rem
       METHOD            pbe0
       BASIS             def2-sv(p)
       CIS_N_ROOTS       4
       CIS_SINGLETS      true
       CIS_TRIPLETS      true
       RPA               false
       STATE_ANALYSIS    true
       NTO_PAIRS         3
       MAKE_CUBE_FILES   true
       ESP_GRID          -3
       WFA_LEVEL         4
       WFA_ORB_THRESH    3
    $end
    
    $plots
    Write cube files for all 4 states
    35  -3.5  3.5
    35  -3.5  3.5
    15  -1.5  1.5
    0  4  0  0
    1 2 3 4
    $end
    ```

**libwfa** 应用的其他示例：

- •

示例 [7.3.4.2](../ch07_excited/sect_sftddft.md#ex:MRSFDFT) 展示了对位苯双自由基（para-benzyne）中 SF-DFT 态的波函数分析；
- •

示例 [7.9.9.2](../ch07_excited/sub_cvs_eom.md#ex:cvsee1) 展示了 CVS-EOM-EE 中 XAS 跃迁的波函数分析；
- •

示例 [7.9.30](../ch07_excited/ex_eomip-wfa.md) 展示了 EOM-IP 态之间跃迁的波函数分析；
- •

示例 [7.9.19](../ch07_excited/ex_CAPlibwfa.md) 展示了 CAP-EOM-CCSD 中复值密度的波函数分析。
