---
title: "12.6.3 具有明确基组极限的极化能"
---

## 12.6.3 具有明确基组极限的极化能

(July 4, 2026)

原始 ALMO-EDA 中极化能降低（polarization energy lowering）的定义，使用每个片段（fragment）的完整原子轨道（AO）空间作为变分自由度。这一做法基于如下假设：AO 基函数可以根据其所属的原子中心归属于各个片段。然而，当使用非常大的基组时，尤其是带有弥散函数的基组（*e.g.* def2-QZVPPD），这一假设就不再合适。在这种情况下，给定片段上的基函数往往倾向于去描述其他片段，使得“绝对定域化”（absolute localization）约束变弱，并最终被有效地去除。这正是原始 ALMO-EDA 方案的极化能不具备明确基组极限的原因。

为克服这一问题，Horn 与 Head-Gordon[[593]](../bib_references/bib.md#bib617)
 基于片段电响应函数（fragment electrical response functions, FERFs）为 ALMO-EDA 方法中的 POL 项提出了一种新的定义。给定片段上的 FERFs 是在求得该片段的 SCF 解之后，通过求解耦合微扰自洽场（CPSCF）方程得到的：

<a id="Ch12.E1"></a>
$$
H_{ai,bj}(\Delta_{\mu})_{bj}=2(M_{\mu})_{ai}, \tag{12.1}
$$

其中 $\mathbf{H}$ 是 SCF 轨道 Hessian 矩阵，$\mathbf{M}_{\mu}$ 是某一阶多极矩矩阵的分量（$\mu$）。所得到的片段响应矩阵（$\{\Delta_{\mu}\}$）是一组 $n_{\mathrm{v}}\times n_{\mathrm{o}}$ 矩阵。随后，对 $\Delta_{\mu}$ 进行奇异值分解（SVD）：

<a id="eq:ferf_cpscf"></a>
$$
(\Delta_{\mu})_{ai}=(L_{\mu})_{ab}(d_{\mu})_{bj}(R_{\mu}^{T})_{ji}, \tag{12.2}
$$

并利用左奇异矢量（不包含零矢量）构造一个截断的虚空间，该虚空间用于定义 SCF-MI 问题的变分自由度：

<a id="Ch12.E3"></a>
$$
\mathbf{V}_{\mu}=\mathbf{C}_{\mathrm{vir}}\mathbf{L}_{\mu}, \tag{12.3}
$$

其中 $\mathbf{C}_{\mathrm{vir}}$ 表示给定片段原始的虚轨道。

使用 FERFs 的基本思想是：获取与给定片段电极化最为相关的一部分虚轨道子集，同时排除多余的变分自由度（这些自由度可能带有电荷转移（CT）性质）。结果表明，该方案为依赖于 SCF-MI 计算的极化能给出了明确的基组极限。多极阶数——偶极（D）、四极（Q）与八极（O）——是否包含在式 ([12.2](#eq:ferf_cpscf)) 的右侧，决定了每个片段上 FERFs 的张成空间。数值实验表明，纳入偶极型与四极型响应即可正确处理远程诱导静电作用，并给出明确的基组极限，因此推荐将其作为 SCF-MI 问题的基础（working basis）。于是片段 $A$ 极化子空间的完整张成空间为：

<a id="eq:pol_ss"></a>
$$
\mathbf{O}_{A}\oplus\mathrm{span}\{\mathbf{V}_{\mu x},\mathbf{V}_{\mu y},\mathbf{V}_{\mu z}\}\oplus\mathrm{span}\{\mathbf{V}_{Q2,-2},\mathbf{V}_{Q2,-1},\mathbf{V}_{Q2,0},\mathbf{V}_{Q2,1},\mathbf{V}_{Q2,2}\}. \tag{12.4}
$$

因此，每个占据轨道将与八个虚轨道配对（前提是所用的 AO 基组足够大）。

按式 ([12.4](#eq:pol_ss)) 构造的极化子空间在片段之间是非正交的，因此该模型被称为极化的“nDQ”模型。该方法还有另一个版本，它强制各片段间极化子空间相互正交，相应地称为“oDQ”（或配以其他多极阶数）。正交 FERFs 的构造更为复杂（细节见
Ref. [[593]](../bib_references/bib.md#bib617)
），并且通常给出较不有利的极化能。对于大多数一般情形，我们推荐使用“nDQ”模型。使用 FERFs 的计算是通过第 [12.6.2](sect_gen_scfmi.md) 节介绍的广义 SCF-MI 流程进行的。

然而，求解 CPSCF 方程需要求逆维度为 $ov\times ov$ 的大型轨道 Hessian 矩阵 $\mathbf{H}$，这是求解 FERFs 过程中最耗时的步骤。例如，在 Hartree-Fock 理论中，在正则表示下其矩阵元为

<a id="Ch12.E5"></a>
$$
H_{ai,bj}=2\left[(\epsilon_{a}-\epsilon_{i})\delta_{ij}\delta_{ab}+\langle aj||ib\rangle+\langle ab||ij\rangle\right]. \tag{12.5}
$$

最近，Aldossary 及其合作者

 提出了非耦合 FERFs（uncoupled-FERFs, uFERFs），以改进传统的 FERFs。uFERFs 的思想很简单，即采用非耦合 CPSCF 方程的解，其中轨道 Hessian 被近似为

<a id="Ch12.E6"></a>
$$
H_{ai,bj}=2(\epsilon_{a}-\epsilon_{i})\delta_{ij}\delta_{ab}. \tag{12.6}
$$

在这一近似下，轨道 Hessian 极易求逆，片段响应矩阵简化为

<a id="Ch12.E7"></a>
$$
\left(\Delta_{\mu}^{\text{uFERF}}\right)_{ai}=\frac{(M_{\mu})_{ai}}{\epsilon_{a}-\epsilon_{i}}. \tag{12.7}
$$

在 S22、S66 和 Ionic43 基准数据集上的测试表明，使用 uFERFs 时 POL 能几乎没有变化，而 FERF 的构造获得普遍的 5–10 倍加速，整个 EDA 计算平均加速约 20%。此外，人们认识到单极（monopole）uFERFs（对缩放核电荷的响应）对于分子间相互作用很重要，尤其在强离子-中性相互作用体系中。因此，推荐在 ALMO-EDA 计算中使用 MDQ-uFERFs 来计算 POL 能。

### `CHILD_MP`

> **为片段计算 FERF，并将其作为 SCF-MI 计算的基础。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不计算 FERF（使用每个片段的完整 AO 空间）。
>     * TRUE
>     * 计算片段 FERF。
> * **建议**: 当使用大基组时，使用 FERF 来计算极化能。在 "EDA2" 计算中，该 $rem 变量会根据所给选项自动设置。

### `CHILD_MP_ORDERS`

> **所制备 FERF 中包含的多极矩阶数。最后一位数字指定要计算多少个多极矩，前面的数字指定多极矩的阶数：2：偶极（D）；3：四极（Q）；4：八极（O）。多极矩阶数 1 保留给单极 FERF（monopole FERF），其可用于分离轨道收缩（orbital contraction）的效应。808 Levine D. S., Head-Gordon M. J. Phys. Chem. Lett. (2017) , 8 , pp. 1967 . 链接**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 21
>     * D
>     * 232
>     * DQ
>     * 2343
>     * DQO
> * **建议**: 当需要 FERF 时使用 232（DQ）。

### `FRAG_CPSCF_MAXITER`

> **共轭梯度（conjugate-gradient）求解器在切换到 MINRES 算法之前执行的最大迭代次数。MINRES 的最大迭代次数设为该值的两倍。请注意，该 rem 变量也用于绝热 EDA（第 12.7.3 节）以及力分解分析（第 12.7.4 节）计算中涉及的 CPSCF 方程。**
>
> * **类型**: `INTEGER`
> * **默认值**: `50`
> * **选项**:
>     * 用户自定义
> * **建议**: 使用默认值

### `FRAG_CPSCF_CONV`

> **CPSCF 方程的收敛阈值（使用残差向量的 RMS 误差）**
>
> * **类型**: `INTEGER`
> * **默认值**: `8`
> * **选项**:
>     * $n$
>     * 当 RMS 误差低于
>     * $10^{-n}$
>     * 时即达到收敛
> * **建议**: 使用默认值

### `EDA_UFERF`

> **使用非耦合 FERF（uncoupled-FERF, uFERF）代替 FERF**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `TRUE`
> * **选项**:
>     * TRUE
>     * 使用 uFERF
>     * FALSE
>     * 使用 FERF
> * **建议**: 使用默认的 uFERF，当希望使用 FERF 时设为 FALSE。

???+ example "示例 12.13：使用 nDQ FERF 对水二聚体进行广义 SCF-MI 计算。"
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
       METHOD            wb97x-v
       GEN_SCFMAN        true
       BASIS             6-31+G(d)
       GEN_SCFMAN        true
       SCF_ALGORITHM     diis
       SCF_CONVERGENCE   8
       THRESH            14
       SCF_FINAL_PRINT   1
       EDA_UFERF         false
       FRGM_METHOD       stoll
       SCFMI_MODE        1 !nonortho gen scfmi
       CHILD_MP          true
       CHILD_MP_ORDERS   232 !DQ
       FD_MAT_VEC_PROD   false
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    ```
