---
title: "7.3.6 TDDFT 的任务控制"
---

## 7.3.6 TDDFT 的任务控制

(July 4, 2026)

## 7.3.6.1 基本设置

含时密度泛函理论（time-dependent density functional theory, TDDFT）计算的输入格式与前一节中描述的非关联激发态方法（uncorrelated excited state methods）的输入格式基本一致（特别是参见第 [7.2.4](sec_CIS-jobcontrol.md) 节）。有以下几点需要注意：

- 交换与关联泛函的指定方式与基态 DFT 计算完全相同，即通过 EXCHANGE 和 CORRELATION 来设置。要启用 TDDFT，需将 CIS_N_ROOTS 设为 $\geq 1$ 的值，以指定要计算的激发态数目。
- 若将 RPA 设为 TRUE，则执行"完整"的 TDDFT 计算；不过默认值为 RPA = FALSE，此时调用 TDA[[580]](../bib_references/bib.md#bib602)，即在式 ([7.15](sect_tddftintro.md#eq:TDDFT)) 中忽略去激发振幅 $\mathbf{y}$。对于激发能而言，这通常是一个很好的近似，尽管在 TDA 下振子强度不再形式上满足 Thomas-Reiche-Kuhn 求和规则。

   对于 RPA = TRUE，会先执行一次 TDA 计算，并将其作为完整 TDDFT 计算的初始猜测。可以通过 RPA = 2 完全跳过 TDA 计算。RPA 未在限制开壳层（restricted open-shell）计算中实现，此类计算仅支持 TDA。
- 若在执行 TDDFT 计算时将 SPIN_FLIP 设为 1（或 TRUE）或 2，则将执行 SF-TDDFT（自旋翻转 TDDFT）计算。目前，SF-TDDFT 仅在 TDA 框架内实现，因此 RPA 必须设为 FALSE。请记得将自旋多重度设为 3（对于电子数为偶数的体系，*e.g.*，双自由基），设为 4（对于电子数为奇数的体系，*e.g.*，三自由基）。MR-SFTDDFT（通过 SPIN_FLIP=2 调用）仅对三重态参考实现。
- 若在执行 TDDFT 计算时将 MGGA_GINV 设为 1，则会为 meta-GGA 泛函添加规范不变性修正（gauge invariance correction）。[[84]](../bib_references/bib.md#bib69)

下面介绍一些基本的任务控制变量（需添加到 *$rem* 段中）。另外还有用于 X 射线光谱学的其他选项，参见第 [7.12.2](subsec_TDDFT-Xray.md) 节。

### `CIS_SINGLETS`

> **控制是否计算单重态激发态。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **选项**:
>     * `FALSE`: 不计算单重态激发。
>     * `TRUE`: 计算单重态激发。
> * **建议**: 该选项仅对单重态基态有意义，因为使用开壳层基态无法得到自旋纯（spin-pure）的激发态。

### `CIS_TRIPLETS`

> **控制是否计算三重态激发态。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **选项**:
>     * `FALSE`: 不计算三重态激发。
>     * `TRUE`: 计算三重态激发。
> * **建议**: 该选项仅对单重态基态有意义，因为使用开壳层基态无法得到自旋纯（spin-pure）的激发态。

### `SPIN_FLIP`

> **选择执行标准激发态计算还是自旋翻转（spin-flip）计算。对于电子数为偶数的体系，自旋多重度应设为 3；对于电子数为奇数的体系，应设为 4。**
>
> * **类型**: `INEGER`
> * **默认值**: `0`
> * **选项**:
>     * `1`: 执行原始 SF-TDDFT。
>     * `2`: 执行 MRSF-TDDFT。
> * **建议**: 无

### `MGGA_GINV`

> **控制是否为 meta-GGA 泛函添加规范不变性修正。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 不做修正。
>     * `1`: 为 meta-GGA 泛函添加规范不变性修正。
> * **建议**: 使用 TDA 时不推荐启用，因为 TDA 会破坏规范不变性。

### `WANG_ZIEGLER_KERNEL`

> **控制在 SF-TDDFT 计算中是否使用 Wang-Ziegler 非共线（non-collinear）交换-关联核。若使用 5.0 之前版本的 Q-Chem，请设置 NEW_DFT = TRUE。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不使用非共线核。
>     * `TRUE`: 使用非共线核。
> * **建议**: 无

### `CIS_GUESS_TYPE`

> **控制如何在 CIS/TDA/RPA 计算中生成初始猜测激发向量。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 按轨道能量差从低到高的顺序，生成 $N$ 个（所请求的根数）占据 $\to$ 虚轨道的单轨道跃迁。这是常见的做法。
>     * `1`: 按轨道能量差从低到高的顺序生成 $N-1$ 个占据 $\to$ 虚轨道的单轨道跃迁，并额外生成一个猜测激发向量，由占据 $\to$ 虚跃迁空间中所有其余的单轨道跃迁以等权重组合而成。
>     * `2`: 按轨道能量差从低到高的顺序生成 $N$ 个占据/虚轨道的单轨道跃迁，并额外生成一个猜测激发向量，由占据 $\to$ 虚跃迁空间中所有其余的单轨道跃迁以等权重组合而成。
> * **建议**: 默认设置适用于大多数情况。然而，当请求的根数较少时，某些 CIS/TDA/RPA 计算可能会遗漏低能激发态。选项 = 1 或 2 可以通过在跃迁空间中采样更多向量来弥补这一漏根问题。设置 = 1 或 2 可能会使 Davidson 迭代需要更多周期才能收敛，但预期结果更为可靠。目前，SF-XCIS 计算不支持 = 1 或 2。设置 TRNSS = TRUE 也会禁用 的该设置。

## 7.3.6.2 电荷分离度量（Charge-Separation Metrics）的选项

通过设置 CIS_CT_METRICS = TRUE，可以（对每个 TDDFT 激发态）在正则（canonical）表示和 NTO 表示中计算电荷分离度量 $\Lambda$、$\Delta r$、$\Delta\sigma$ 和 $\Gamma$。下面介绍一些额外的选项。关于 **libwfa** 的任务控制（*e.g.*，计算推荐的度量 $d_{\text{e-h}}$、$d_{\text{exc}}$ 和 $d_{\text{CD1}}$），参见第 [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) 节。

### `CIS_CT_METRICS`

> **控制是否计算电荷分离度量 $\Lambda$ 、 $\Delta r$ 、 $\Delta\sigma$ 和 $\Gamma$（第 7.3.2 节）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不计算这些度量。
>     * `TRUE`: 计算全部四个度量（对每个激发态），并在正则表示和 NTO 表示中同时计算。
> * **建议**: 如有需要可请求计算。（计算 $\Lambda$ 会带来一些额外开销，但应当很小。）

### `SPATIAL_OVERLAP_METRIC`

> **控制在使用式 ( 7.16 ) 计算 $\Lambda$ 时采用 $O_{ia}$ 还是 $\tilde{O}_{ia}$ 。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * `1`: 使用 $O_{ia}$ 计算 $\Lambda$。
>     * `2`: 使用 $\tilde{O}_{ia}$ 计算 $\Lambda$。
> * **建议**: 选项 1 表示 Tozer 及其合作者在文献 1057 Peach M. J. G. et al. J. Chem. Phys. (2008) , 128 , pp. 044118 . Link . 中提出的原始度量。

### `SPATIAL_OVERLAP_GRID`

> **控制在式 ( 7.17 ) 中计算 $O_{ia}$ 或 $\tilde{O}_{ia}$ 时所使用的网格。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * `1`: 使用 $N_{r}=300$ 且 $N_{\Omega}=302$ 的 EML 网格。
>     * `2`: 使用 $N_{r}=400$ 且 $N_{\Omega}=434$ 的 EML 网格。
> * **建议**: 无。

### `SPATIAL_OVERLAP_PRINT`

> **控制是否打印空间重叠 $O_{ia}$ 或 $\tilde{O}_{ia}$ 。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 不打印 $O_{ia}$。
>     * `1`: 仅打印前沿（frontier）重叠（5 个占据轨道和 5 个虚轨道）。
>     * `2`: 打印所有 $O_{ia}$。
> * **建议**: 这些信息对于事后分析各分子轨道（MO）之间的空间邻近性可能有用；然而对于大分子，选项 2 会产生大量打印输出。打印的是 $O_{ia}$ [式 ( 7.17 )] 还是 $\tilde{O}_{ia}$ [式 ( 7.18 )]，取决于 SPATIAL_OVERLAP_ANAL 的设置。

## 7.3.6.3 截断子空间（Truncated Subspace）的选项

以下选项可用于实现第 [7.3.3](subsec_TRNSS.md) 节中所述的约化激发空间（reduced excitation space）。

### `CISTR_PRINT`

> **控制输出级别。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `TRUE`: 提高输出级别。
> * **建议**: 无

### `CUTOCC`

> **指定占据轨道截断值（cutoff）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `50`
> * **选项**:
>     * `0-200`: 使用的截断值为 /100
> * **建议**: 无

### `CUTVIR`

> **指定虚轨道截断值（cutoff）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0-100`: CUTOFF = CUTVIR/100
> * **建议**: 无

### `N_SOL`

> **指定 $solute 或 $alist 段中的原子数或轨道数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值。`
> * **选项**:
>     * 用户自定义。
> * **建议**: 从 $solute 或 $alist 输入段读取。

### `TRNSS`

> **控制是否使用约化单激发空间。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `TRUE`: 使用约化激发空间。
> * **建议**: 无

### `TRTYPE`

> **控制如何指定约化子空间。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * `1`: 选择定域在一组原子上的轨道。
>     * `2`: 指定一组轨道。
>     * `3`: 指定一组占据轨道，包含向所有虚轨道的激发。
> * **建议**: 无

## 7.3.6.4 EA-TDDFT 的任务控制

与 NOCIS/STEX/1C-NOCIS 类似，EA-TDDFT/EA-CIS 方法的选项通过在 *$rem* 中将 NOCIS 设为 TRUE 后，在 *$nocis* 段中进行控制。

### `NOCIS`

> **请求执行 NOCIS/STEX/1C-NOCIS/EA-TDDFT 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不运行这些方法。
>     * `TRUE`: 运行这些方法之一，选项在 $nocis 中控制。
> * **建议**: 无

以下选项在 *$nocis* 段内设置。

### `NUM_REF`

> **设置 NOCIS/STEX/1C-NOCIS/EA-TDDFT 计算中参考轨道的数目。输入段：$nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 根据计算中所需关注的连续轨道数目来设置。例如，对于 CO ${}_{\text{2}}$ 的氧 K 边，参考数应为 2（两个氧 1s 轨道），而对于碳 K 边则为 1（一个碳 1s）。

### `ORB_OFFSET`

> **确定 NOCIS/STEX/1C-NOCIS/EA-TDDFT 计算的起始轨道。输入段：$nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 根据所研究体系中第一个需要关注的轨道来设置。例如，对于 CO ${}_{\text{2}}$ 的氧 K 边应设为 0，因为两个 O(1s) 轨道位于 C(1s) 之下；因此对于碳 K 边应设为 2。

### `LOCALIZE_ORBITALS`

> **选择用 Boys 目标函数对哪些核心轨道进行定域化。输入段：$nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `$-1$`
> * **选项**:
>     * $n$: 整数，通常为正。
> * **建议**: 设为 $-1$ 可完全跳过 Boys 定域化；或设为大于 NUM_REF 的值，以便在预定域化中包含更多轨道；否则使用默认值。

### `SUBSYSTEM_ATOMS`

> **选择 EA-TDDFT 计算中需要考虑的原子。输入段：$nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * 以空格分隔的整数列表：: $i\ j\ k$ …
> * **建议**: 仅当关注从特定原子子集出发的激发、且 ORB_OFFSET 和 NUM_REF 的定义较复杂时才使用。这是一个专家选项，只应在特定情形下使用，例如分离空气/水界面处所有水分子的氧 K 边。

### `DSCF_ALGORITHM`

> **设置用于优化核心电离（core-ionized）参考行列式的 $\Delta$ SCF 算法。输入段：$nocis**
>
> * **类型**: `STRING`
> * **默认值**: `MOM`
> * **选项**:
>     * MOM、IMOM、STEP 或 STEP_MOM
> * **建议**: 除非出现收敛问题，否则使用 MOM。IMOM 有时能改善收敛，但 STEP_MOM 选项所采用的 STEP 与 MOM 组合尤其稳健。极少数情况下可能需要 STEP，但不推荐，因为所需的 SCF 循环数目相当大。若请求 STEP_MOM，还必须设置选项 STEP_MOM_START。

### `STEP_MOM_START`

> **设置 STEP 算法停止、MOM 算法开始的 SCF 循环数。输入段：$nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `5`
> * **选项**:
>     * $n$: 正整数。
> * **建议**: 为获得最佳效果，应设置在 STEP 达到至少 $10^{-4}$ a.u. 的收敛阈值之后再切换到 MOM；但如果 MOM 持续坍缩或振荡，则应等待更严格的收敛后再切换算法。

### `REF_SCF_ALGORITHM`

> **设置核心电离（core-ion）参考计算的 SCF 算法。输入段：$nocis**
>
> * **类型**: `STRING`
> * **默认值**: `DIIS`
> * **选项**:
>     * DIIS、GDM、GDM_LS、SGM 或 SGM_LS
> * **建议**: 对于 MOM、IMOM、STEP 或 STEP_MOM 计算使用 DIIS；但如果这些算法无法令人满意地收敛到目标 core-ion 态，可将其设为 SGM 或 SGM_LS。

### `REF_SCF_CONVERGENCE`

> **设置核心电离（core-ion）参考计算的 SCF 收敛阈值。输入段：$nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `Same as`
> * **选项**:
>     * $n$: 正整数
> * **建议**: 无

### `REF_SCF_GUESS`

> **核心电离（core-ion）参考计算的初始猜测。输入段：$nocis**
>
> * **类型**: `STRING`
> * **默认值**: `Koopman`
> * **选项**:
>     * Read（若未指定选项，则自动使用 Koopmans 猜测）
> * **建议**: 默认的 core-ion 猜测通过利用基态 MO 系数从核心轨道移除一个电子来生成（Koopmans 猜测）。或者，当出现收敛问题时，可以先用不同的泛函（*i.e.*，LDA 或 GGA）运行一次 EA-TDDFT 计算，然后将收敛的 core-ion 轨道读入后续使用目标泛函（*i.e.*，范围分离杂化泛函）的 EA-TDDFT 计算中。

### `EA_TDA`

> **在 Tamm-Dancoff 近似（TDA）下调用 EA-TDDFT。输入段：$nocis**
>
> * **类型**: `NONE`
> * **默认值**: `NONE`
> * **选项**:
>     * 出现此关键字即会激活: 。
> * **建议**: 这是 EA-TDDFT 方程最具成本效益的形式，对 K 边 XAS 的结果几乎没有任何影响。

### `EA_RPA`

> **求解完整的 EA-TDDFT 方程。输入段：$nocis**
>
> * **类型**: `NONE`
> * **默认值**: `NONE`
> * **选项**:
>     * 出现此关键字即会激活: 。
> * **建议**: 无建议。

### `SINGLETS`

> **仅计算单重态。输入段：$nocis**
>
> * **类型**: `NONE`
> * **默认值**: `NONE`
> * **选项**:
>     * 出现此关键字且未出现: Triplets 关键字时， 将计算单重态而不计算三重态。
> * **建议**: 无建议。

### `TRIPLETS`

> **仅计算三重态。输入段：$nocis**
>
> * **类型**: `NONE`
> * **默认值**: `NONE`
> * **选项**:
>     * 出现此关键字且未出现: Singlets 关键字时， 将计算三重态而不计算单重态。
> * **建议**: 无建议。

### `N_ROOTS`

> **设置要打印的根数。输入段：$nocis**
>
> * **类型**: `INTEGER`
> * **默认值**: `All`
> * **选项**:
>     * $n$: 其中 $n<m_{\rm{roots}}$
> * **建议**: 无建议。请注意，与 CIS/TDDFT 作业不同，此关键字仅减少打印的根数，但仍会通过直接对角化对整个哈密顿量进行完全对角化。

### `PRINT_NTOS`

> **为通过 N_ROOTS 关键字打印的每个根，将自然跃迁轨道（NTO）输出到 cube 文件。输入段：$nocis**
>
> * **类型**: `NONE`
> * **默认值**: `NONE`
> * **选项**:
>     * 出现此关键字即自动生成: 全部 NTO（默认），或 N_ROOTS 个 NTO。
> * **建议**: 无建议，但务必同时提供一个包含适当细节的 $plots 段，以便生成 cube 文件。

???+ example "示例 7.12: 采用 Tamm-Dancoff 近似的 NH ${}_{3}$ K 边 EA-TDDFT。
本作业将打印的（单重态）根数截断为 10。
core-ion SCF 将使用 SGM 算法。"
    ```qchem
    $rem
    method          rCAM-B3LYP
    rel_x2c         true
    basis           aug-cc-pCVDZ
    nocis           true
    scf_convergence 8
    thresh          14
    integral_symmetry    false
    point_group_symmetry false
    $end
    
    $nocis
    n_roots         10
    orb_offset      0
    num_ref         1
    singlets
    ea_tda
    ref_scf_algorithm sgm
    $end
    
    $molecule
    0 1
    N   0.0000   0.0000   0.1163
    H   0.0000   0.9399  -0.2713
    H   0.8140  -0.4700  -0.2713
    H  -0.8140  -0.4700  -0.2713
    $end
    ```

???+ example "示例 7.13: NH ${}_{3}$ K 边的完整 EA-TDDFT。core-ion SCF 将使用默认的 MOM 算法。"
    ```qchem
    $rem
    method          rCAM-B3LYP
    rel_x2c         true
    scf_convergence 8
    basis           aug-cc-pCVDZ
    nocis           true
    thresh          14
    integral_symmetry    false
    point_group_symmetry false
    $end
    
    $nocis
    n_roots         10
    orb_offset      0
    num_ref         1
    singlets
    ea_rpa
    $end
    
    $molecule
    0 1
    N   0.0000   0.0000   0.1163
    H   0.0000   0.9399  -0.2713
    H   0.8140  -0.4700  -0.2713
    H  -0.8140  -0.4700  -0.2713
    $end
    ```
