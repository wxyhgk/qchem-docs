---
title: "11.6.1 引言与理论"
---

## 11.6.1 引言与理论

(July 4, 2026)

由 Manby、Miller 及其合作者发展的形式精确密度嵌入方法（formally exact density embedding method）[[878]](../bib_references/bib.md#bib913)
 在描述化学环境时比静电嵌入（electrostatic embedding）更进了一步。该嵌入方案允许将一个系统划分为两个相互作用的子系统，并分别用两种不同的量子力学（QM）理论层次进行处理，*e.g.*，将耦合簇（coupled cluster）嵌入密度泛函理论（Density Functional Theory, DFT）之中。这种类型的嵌入能够充分考虑极化效应以及量子力学交换作用，这些效应由超分子嵌入密度（super-molecular embedding density）和所使用的交换关联泛函计算得到。该嵌入理论的目标是：在由较低层次 QM 理论所描述的环境中，执行较高层次 QM 计算。

## 11.6.1.1 工作方程

对于一个总密度可表示为 $\boldsymbol{\gamma}=\boldsymbol{\gamma}^{A}+\boldsymbol{\gamma}^{B}$ 的系统，*i.e.*，片段 $A$ 与 $B$ 上的分子轨道（MO）彼此正交，其总能量可表示为

<a id="A3.S8.EGx111"></a>

$$
\displaystyle\begin{aligned} \displaystyle E_{\text{tot}}[\boldsymbol{\gamma}^{A}+\boldsymbol{\gamma}^{B}]&\displaystyle=\underbrace{\mathrm{tr}(\boldsymbol{\gamma}^{A}\mathbf{h})+J[\boldsymbol{\gamma}^{A}]+E_{\text{xc}}[\boldsymbol{\gamma}^{A}]}_{\text{Energy of A}}+\underbrace{\mathrm{tr}(\boldsymbol{\gamma}^{B}\mathbf{h})+J[\boldsymbol{\gamma}^{B}]+E_{\text{xc}}[\boldsymbol{\gamma}^{B}]}_{\text{Energy of B}}\\
&\displaystyle\qquad+\underbrace{J[\boldsymbol{\gamma}^{A},\boldsymbol{\gamma}^{B}]+E_{\text{xc}}[\boldsymbol{\gamma}^{A},\boldsymbol{\gamma}^{B}]}_{\text{Non-additive terms}}\end{aligned} \tag{11.99}
$$

其中 $\mathbf{h}$ 是核心哈密顿（core-Hamiltonian）矩阵，$J$ 和 $E_{\text{xc}}$ 分别是库仑（Coulomb）能与交换关联（XC）能（若采用杂化泛函，精确交换 $K$ 也会存在）。在一次嵌入计算中，$A$ 的电子密度（记为 $\tilde{\gamma}^{A}$）在 $\gamma^{B}$（由低层次理论获得并随后固定不动）存在的条件下，用高层次理论进行优化，此时总能量可表示为

<a id="eq:Etot_dft_in_dft"></a>

$$
E_{\text{tot}}[\tilde{\gamma}^{A},\gamma^{B}]=E^{\text{high}}[\tilde{\gamma}^{A}]+E^{\text{low}}[\tilde{\gamma}^{A}+\gamma^{B}]-E^{\text{low}}[\tilde{\gamma}^{A}]. \tag{11.100}
$$

对式 ([11.100](#eq:Etot_dft_in_dft)) 关于 $\tilde{\gamma}^{A}$ 求变分，即得到嵌入计算的 Fock 矩阵：

<a id="Ch11.E101"></a>

$$
\mathbf{f}^{\text{A-in-B}}=\frac{\delta}{\delta\tilde{\gamma}^{A}}E_{\text{tot}}[\tilde{\gamma}^{A},\gamma^{B}]=\mathbf{F}^{\text{high}}[\tilde{\gamma}^{A}]+\mathbf{v}_{\text{emb}}[\tilde{\gamma}^{A},\gamma^{B}], \tag{11.101}
$$

其中嵌入势（embedding potential）

<a id="A3.S8.EGx112"></a>

$$
\displaystyle\begin{aligned} \displaystyle\mathbf{v}_{\text{emb}}[\tilde{\gamma}^{A},\gamma^{B}]&\displaystyle=\frac{\partial}{\partial\tilde{\gamma}^{A}}\left(E^{\text{low}}[\tilde{\gamma}^{A}+\gamma^{B}]-E^{\text{low}}[\tilde{\gamma}^{A}]\right)\\
&\displaystyle=\mathbf{F}^{\text{low}}[\tilde{\gamma}^{A}+\gamma^{B}]-\mathbf{F}^{\text{low}}[\tilde{\gamma}^{A}]\\
&\displaystyle=(\mathbf{J}[\boldsymbol{\gamma}^{A}+\boldsymbol{\gamma}^{B}]-\mathbf{J}[\boldsymbol{\gamma}^{A}])+(\mathbf{v}^{\text{low}}_{\text{xc}}[\boldsymbol{\gamma}^{A}+\boldsymbol{\gamma}^{B}]-\mathbf{v}^{\text{low}}_{\text{xc}}[\boldsymbol{\gamma}^{A}])+\mu\mathbf{P}^{B},\end{aligned} \tag{11.102}
$$

其中 $\mathbf{P}^{B}=\mathbf{S}\boldsymbol{\gamma}^{B}\mathbf{S}$ 是由 $B$ 的轨道构成的投影算符，$\mu$ 是一个足够大的常数（*e.g.* 10${}^{6}$ a.u.），它有效地抬升 $B$ 轨道的能量，从而强制 $A$ 与 $B$ 上的 MO 之间保持正交。在 **Q-Chem** 的实现中（设置 GEN_SCFMAN_EMBED = TRUE），采用了另一种途径：对一个修正的 Fock 矩阵进行对角化，并从其中投影掉由 $B$ 的轨道所垂张的变分自由度：

<a id="Ch11.E103"></a>

$$
\tilde{\mathbf{f}}^{\text{A-in-B}}=(\mathbf{I}-\mathbf{S}\boldsymbol{\gamma}^{B})\mathbf{f}^{\text{A-in-B}}(\mathbf{I}-\boldsymbol{\gamma}^{B}\mathbf{S}), \tag{11.103}
$$

其中 $\mathbf{S}$ 是原子轨道（AO）重叠矩阵。

使用式 ([11.100](#eq:Etot_dft_in_dft)) 给出的能量表达式有一个缺点：嵌入势[式 ([11.102](#eq:v_emb))]依赖于 $\tilde{\gamma}^{A}$，而后者在嵌入计算的每一次迭代中都需要更新。因此，对于 DFT-in-DFT 计算，该方案并不能节省计算成本。为解决这一局限，人们提出了一种线性化近似[[792]](../bib_references/bib.md#bib827)，
 其基于如下展开（对 $\tilde{\gamma}^{A}-\gamma^{A}$ 取至一阶）：

<a id="eq:linear_expansion"></a>

$$
E^{\text{low}}[\tilde{\gamma}^{A}+\gamma^{B}]-E^{\text{low}}[\tilde{\gamma}^{A}]\approx E^{\text{low}}[\gamma^{A}+\gamma^{B}]-E^{\text{low}}[\gamma^{A}]+\mathrm{Tr}\left((\tilde{\gamma}^{A}-\gamma^{A})\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}]\right), \tag{11.104}
$$

其中

<a id="Ch11.E105"></a>

$$
\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}]=\frac{\delta}{\delta\gamma^{A}}\left(E^{\text{low}}[\gamma^{A}+\gamma^{B}]-E^{\text{low}}[\gamma^{A}]\right)=\mathbf{F}^{\text{low}}[\gamma^{A}+\gamma^{B}]-\mathbf{F}[\gamma^{A}] \tag{11.105}
$$

基于此线性化近似，整个系统的总能量可近似表示为

<a id="eq:Etot_dft_in_dft_approx"></a>

$$
E_{\text{tot}}[\tilde{\gamma}^{A};\gamma^{A},\gamma^{B}]=E^{\text{high}}[\tilde{\gamma}^{A}]+E^{\text{low}}[\gamma^{A}+\gamma^{B}]-E^{\text{low}}[\gamma^{A}]+\mathrm{Tr}\left((\tilde{\gamma}^{A}-\gamma^{A})\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}]\right), \tag{11.106}
$$

而嵌入计算的 Fock 矩阵为：

<a id="Ch11.E107"></a>

$$
\mathbf{f}^{\text{A-in-B}}=\frac{\delta}{\delta\tilde{\gamma}^{A}}E_{\text{tot}}[\tilde{\gamma}^{A};\gamma^{A},\gamma^{B}]=\mathbf{F}^{\text{high}}[\tilde{\gamma}^{A}]+\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}] \tag{11.107}
$$

其中嵌入势在整个嵌入计算过程中保持不变。在 **Q-Chem** 5.4.1 及其后续版本中，基于投影的嵌入计算默认使用这一线性化近似。

对于波函数-in-DFT（wave function-in-DFT）计算，可以将嵌入势 $\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}]$ 吸收到用于关联波函数计算的哈密顿量中，从而将式 ([11.106](#eq:Etot_dft_in_dft_approx)) 改写为

<a id="eq:Etot_wft_in_dft_approx"></a>

$$
E[\Psi^{A};\gamma^{A},\gamma^{B}]=\langle\Psi^{A}|\hat{H}^{\text{A-in-B}}|\Psi^{A}\rangle+E^{\text{low}}[\gamma^{A}+\gamma^{B}]-E^{\text{low}}[\gamma^{A}]-\mathrm{Tr}\left(\gamma^{A}\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}]\right)\;. \tag{11.108}
$$

## 11.6.1.2 占据空间的划分

嵌入计算通常从整个系统在较低理论层次上的自洽场（SCF）计算开始，得到正则分子轨道（canonical MOs）。因此，有必要对占据空间进行划分，并将轨道分配给片段 $A$ 与 $B$（不失一般性地，假设 $A$ 为被嵌入的片段）。在 Manby *et al.* 的原始工作中[[878]](../bib_references/bib.md#bib913)，
 这一划分是通过以下步骤实现的：

- 对正则占据轨道执行 Pipek-Mezey 定域化[[1093]](../bib_references/bib.md#bib1138)
；
- 若某个 PM 定域轨道在 $A$ 上的 Mulliken 布居数大于 0.4，则将其分配给“活性”片段 $A$。

该方法已被 **Q-Chem** 采用为默认的占据空间划分方法。

近来，Claudino 与 Mayhall 提出了一种无参数且更稳健的划分方案，称为子系统投影 AO 分解（Subsystem Projected AO Decomposition, SPADE）程序[[253]](../bib_references/bib.md#bib254)。

在该方法中，首先将占据轨道变换到对称正交化的 AO 基下：

<a id="Ch11.E109"></a>

$$
\bar{\mathbf{C}}_{\text{occ}}=\mathbf{S}^{1/2}\mathbf{C}_{\text{occ}} \tag{11.109}
$$

然后将 $\bar{\mathbf{C}}_{\text{occ}}$ 中对应于片段 $A$ 的行记为 $\bar{\mathbf{C}}_{\text{occ}}^{A}$。接着对 $\bar{\mathbf{C}}_{\text{occ}}^{A}$ 施加奇异值分解（SVD）：$\bar{\mathbf{C}}_{\text{occ}}^{A}=\mathbf{U}^{A}\Sigma^{A}(\mathbf{V}^{A})^{T}$，随后通过旋转原来的 $\mathbf{C}_{\text{occ}}$ 得到 SPADE 轨道：

<a id="Ch11.E110"></a>

$$
\mathbf{C}_{\text{occ}}^{\text{SPADE}}=\mathbf{C}_{\text{occ}}\mathbf{V}^{A}. \tag{11.110}
$$

奇异值谱中的最大间隙决定了在给定 fragmentation 下最合适的占据轨道划分。

## 11.6.1.3 使用同心定域化截断虚空间

波函数-in-DFT 计算不仅需要“活性”片段上的占据轨道，还需要虚轨道。与占据轨道不同，基于投影的嵌入计算所得到的虚轨道并不分配给各片段，而是保持离域状态。若在 post-SCF 计算中使用完整的虚空间，那么计算成本的节省将相当有限，因为被减少的只是占据轨道的数目。因此，进一步截断虚空间是可取的，这样才能显著降低波函数-in-DFT 计算的成本。

Claudino 与 Mayhall 近来提出了一种简单而高效的方法，基于同心定域化（concentric localization, CL）来截断虚空间[[254]](../bib_references/bib.md#bib255)，

其核心思想与占据空间的 SPADE 划分方案一致。第一步，将工作基组（working basis, WB）下表示的原始离域虚轨道集合（$\mathbf{C}_{\text{vir}}$）在用户指定的投影基组（projection basis, PB）下投影到被嵌入片段 $A$ 上：

<a id="Ch11.E111"></a>

$$
{}^{A}\mathbf{C}_{\text{vir}}^{\prime}=(\mathbf{S}_{\text{PB},A}^{-1})(^{A}\mathbf{S}_{\text{PB,WB}})\mathbf{C}_{\text{vir}} \tag{11.111}
$$

其中上标“$A$”表示仅包含对应于片段 $A$ 基函数的行，而 $\mathbf{S}_{\text{PB},A}$ 表示仅含片段 $A$ 上 PB 函数的重叠矩阵。可以选择 PB 与 WB 相同，甚至选用更小的基组（Basis Set）。随后，通过对 ${}^{A}\mathbf{C}_{\text{vir}}^{\prime}$ 与 $\mathbf{C}_{\text{vir}}$ 之间的重叠矩阵执行 SVD，可选出一组记为 $\mathbf{C}_{0}$ 的特定虚轨道：

<a id="eq:cl_step1"></a>

$$
(^{A}\mathbf{C}_{\text{vir}}^{\prime})^{T}(^{A}\mathbf{S}_{\text{PB,WB}})\mathbf{C}_{\text{vir}}=\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{T} \tag{11.112}
$$

其中

<a id="Ch11.E113"></a>

$$
\displaystyle\mathbf{V} \tag{11.113a}
$$

按构造方式，$\mathbf{C}_{0}$ 应当由 WB 的虚价层（virtual valence shell）组成。为了在嵌入的关联方法中获得更高精度，可以从 $\mathbf{C}_{\text{null},0}$ 中逐步选取更多虚轨道。一种推荐的做法[[254]](../bib_references/bib.md#bib255)

是对矩阵 $\mathbf{C}^{T}\mathbf{F}\mathbf{C}_{\text{null},0}$ 进行奇异值分解，*i.e.*，即 $\mathbf{C}_{0}$ 与 $\mathbf{C}_{\text{null},0}$ 之间通过 Fock 算符的耦合：

<a id="eq:cl_step2"></a>

$$
\mathbf{C}_{0}^{T}\mathbf{F}\mathbf{C}_{\text{null},0}=\mathbf{U}_{0}\boldsymbol{\Sigma}_{0}\mathbf{V}_{0}^{T} \tag{11.114}
$$

其中

<a id="Ch11.E115"></a>

$$
\displaystyle\mathbf{V}_{0} \tag{11.115a}
$$

由于 $\mathbf{C}_{1}$ 的规模与 $\mathbf{C}_{0}$ 相同，经过式 ([11.114](#eq:cl_step2)) 给出的流程后，活性虚轨道的数目翻了一倍。该流程可以迭代进行，从而使本方法的精度可调：

<a id="eq:cl_iter"></a>

$$
\mathbf{C}_{n}^{\top}\mathbf{F}\mathbf{C}_{\text{null},n}=\mathbf{U}_{n}\boldsymbol{\Sigma}_{n}\mathbf{V}_{n}^{T} \tag{11.116}
$$

其中

<a id="Ch11.E117"></a>

$$
\displaystyle\mathbf{V}_{n} \tag{11.117a}
$$

垂张零空间的虚轨道 $\mathbf{C}_{\text{null},n+1}$ 在 post-SCF 计算中将保持非活性。实践中，通常只需包含 $\mathbf{C}_{0}$ 与 $\mathbf{C}_{1}$ 即可达到亚 kcal/mol 量级的精度，这被称为“双-$\zeta$”（double-$\zeta$）CL 壳层模型。
