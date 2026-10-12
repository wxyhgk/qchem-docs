---
title: "12.6.2 广义 SCF-MI 计算及附加功能"
---

## 12.6.2 广义 SCF-MI 计算及附加功能

（2026 年 7 月 4 日）

SCF-MI 计算中所使用的绝对局域分子轨道（Absolutely Localized Molecular Orbitals, ALMOs）的原始定义基于原子轨道到分子轨道（AO-to-MO）变换矩阵的分片分块（fragment-blocking）结构，*即*，对于给定的片段（fragment），其对应的分子轨道（MO）只能用归属于同一片段上的原子为中心的原子轨道（AO）基函数展开。此处我们针对 SCF-MI 计算提出一种广义定义：给定一组基向量（$\mathbf{G}$），其中每个基向量都被标记归属于某个片段，但允许由任意 AO 基函数展开，则该组基向量定义了 SCF-MI 问题的_working basis（工作基组）_。随后，在此基组内可以用类似的方式求解局域投影（locally projected）SCF 方程，其约束是分子轨道系数矩阵在工作基组（$\mathbf{G}$）中呈分片分块对角（fragment-block-diagonal）形式，而其在 AO 基组中的系数矩阵则不必一定保留分块结构。$\mathbf{G}$ 中的基向量在片段之间可以是非正交的，也可以是正交的。有关广义 SCF-MI 方程的更多细节可参见文献 Ref. [[593]](../bib_references/bib.md#bib617)。

这一广义 SCF-MI 方案在 GEN_SCFMAN 中得以实现（原始的基于 AO 分块（AO-block）的方案同样可在 GEN_SCFMAN 中使用）。它用于“EDA2”（能量分解分析，Energy Decomposition Analysis）中极化（但禁止电荷转移，CT-forbidden）中间态的变分优化（参见第 [12.6.3](sect_ferf.md) 节）。该广义方案的另一个优点是，$\mathbf{G}$ 中片段间的线性相关性（interfragment linear dependency）能够得到妥善处理。因此，该方案可以用来替代原始的基于 AO 分块的 SCF-MI，且在出现片段间线性相关时不会变得定义不良（ill-defined）。相比之下，采用 AO 分块方法的原始 ALMO-EDA 方法，当各片段轨道数之和不等于超系统（super-system）的轨道数时（后者由 AO 基函数总数与 BASIS_LIN_DEP_THRESH 共同决定）便会失效，而这种情况在使用相当大的基组或超系统包含大量片段时经常发生。

基于 GEN_SCFMAN 实现的 SCF-MI 计算通过设置 GEN_SCFMAN = TRUE 以及 FRGM_METHOD = STOLL 或 GIA 来触发（FRGM_METHOD 的其他选项不被允许）。GEN_SCFMAN 所支持算法的一个子集可用于受限（restricted, R）和非受限（unrestricted, U）SCF-MI，包括 DIIS、GDM、GDM_LS 和 NEWTON_CG。DIIS 算法通过迭代求解局域投影 SCF 方程，而后两种方法则利用能量对片段内轨道旋转（on-fragment orbital rotations）的导数来最小化能量，直至梯度趋近于零。与使用 GEN_SCFMAN 的标准计算一样，R- 和 U-SCF-MI 也支持内部稳定性分析（internal stability analysis），并且当所采用的密度泛函无法获得解析 Hessian 时，可以将 FD_MAT_VEC_PROD 设为 TRUE（注意：对于包含非局域相关（non-local correlation）的泛函，始终可以使用 FD_MAT_VEC_PROD = FALSE）。

与原始实现一样，可以在 SCF-MI 解的基础上施加微扰修正（perturbative corrections）以逼近完整 SCF 结果，这仍然由 FRGM_LPCORR 控制。注意，在第 [12.5.5](sect_old_almo_job.md) 节引入的各选项中，此处仅允许 ARS 和 RS，因为精确的 SCF 计算实际上超出了 SCF-MI 的适用范围。

此外，借助这一更通用的实现，用户可以指定某些片段在 SCF-MI 计算过程中保持冻结（frozen），*即*，这些片段上不发生片段内弛豫（intrafragment relaxation）。这通过设置 *$rem* 变量 SCFMI_FREEZE_SS 来实现。这样的计算可以被理解为：活性片段（active fragment）嵌入在一个冻结环境中，且二者之间的相互作用以量子力学方式处理。

### `SCFMI_MODE`

> **确定是否使用广义 SCF-MI，并指定工作基组的性质。**
>
> * **类型（Type）**: `INTEGER`
> * **默认值（Default）**: `0（基本“EDA2”计算使用“1”）。`
> * **选项（Options）**:
>     * `0`: 基于 AO 分块的 SCF-MI（ALMO 的原始定义）。
>     * `1`: 广义 SCF-MI，其基向量在片段之间非正交。
>     * `2`: 广义 SCF-MI，其基向量在片段之间正交。
> * **建议（Recommendation）**: 无

### `SCFMI_FREEZE_SS`

> **在 SCFMI 计算中保持前若干个片段不发生弛豫。**
>
> * **类型（Type）**: `INTEGER`
> * **默认值（Default）**: `0（所有片段均为活性片段）`
> * **选项（Options）**:
>     * $n$: 冻结前
>     * $n$: 个片段。
> * **建议（Recommendation）**: 无

???+ example "示例 12.12: 水二聚体的广义 SCF-MI 计算，采用单步 Roothaan 步骤（Roothaan step）微扰修正。就这一具体情形而言，
结果与基于 AO 分块的 SCF-MI（SCFMI_MODE = 0）给出的结果相同。"
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
       METHOD           b3lyp
       GEN_SCFMAN       true
       BASIS            6-31+G(d)
       GEN_SCFMAN       true
       SCF_CONVERGENCE  8
       THRESH           14
       FRGM_METHOD      stoll
       FRGM_LPCORR      rs
       SCFMI_MODE       1 !gen scfmi (non-orthogonal)
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
