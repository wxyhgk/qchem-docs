---
title: "10.15.3 用于电子耦合的基于片段的方法（Fragment-Based Methods for Electronic Coupling）"
---

## 10.15.3 用于电子耦合的基于片段的方法（Fragment-Based Methods for Electronic Coupling）

（2026 年 7 月 4 日）

## 10.15.3.1 基于完全局域分子轨道的方法（Approach based on absolutely localized molecular orbitals）

可以利用完全局域分子轨道（absolutely localized molecular orbitals, ALMOs，参见第 [12](../ch12_frag/chap_frag.md) 章）直接从密度泛函理论（Density Functional Theory, DFT）计算中构造电荷局域的非绝热态（diabatic states）。每个片段上的 ALMO 仅由属于该片段的原子轨道（atomic orbital, AO）基函数展开，因此其对应的分子轨道（MO）系数矩阵在片段上呈分块对角形式。[[683]](../bib_references/bib.md#bib705)

在能量分解分析（energy decomposition analysis）方法中，[[682]](../bib_references/bib.md#bib706)
ALMO 被用于分离分子间结合中的极化（polarization）与电荷转移（charge transfer）效应，因为 ALMO 具有一个有用的性质：按照 Mulliken 电荷布居的定义，它们不允许片段之间发生电荷转移。利用这一性质，可以针对空穴转移和电子转移构造电荷局域的非绝热态势（diabats）。例如，考虑空穴转移过程的初态与末态 $|D^{+}A\rangle$ 和 $|DA^{+}\rangle$，这两个非绝热态势可以表示为如下形式：

<a id="Ch10.E202"></a>

$$
\displaystyle|{\psi_{a}}\rangle \tag{10.202a}
$$

对于给体（donor）与受体（acceptor）部分分离得较好的体系，可以直接将孤立片段计算所得的轨道拼接起来构造基于 ALMO 的非绝热态势：一个态势使用 $D^{+}$ 和 $A$，另一个态势使用 $D$ 和 $A^{+}$。随后每个 ALMO 态势的能量可以在片段内的轨道旋转下作变分优化，此处使用 SCFMI 技术（自洽场于多体积分解，see
Section [12.5.1](../ch12_frag/sect_lp_scf.md)）。[[1314]](../bib_references/bib.md#bib1371)
这些基于 ALMO 的非绝热态经过变分优化，因而与之相关的核力可以方便地计算出来。[[894]](../bib_references/bib.md#bib928)
给体与受体部分在彼此存在时的相互极化也同样被考虑在内。

要计算两个 ALMO 非绝热态势之间的电子耦合（electronic coupling），首先应在 ALMO 态基下构造非绝热哈密顿量

<a id="Ch10.E203"></a>

$$
\mathbf{H}^{\prime}=\begin{pmatrix}H^{\prime}_{aa}&H^{\prime}_{ab}\\
H^{\prime}_{ba}&H^{\prime}_{bb}\end{pmatrix} \tag{10.203}
$$

然后将其变换到 Löwdin 正交化基下

<a id="eq:sym_ortho_H"></a>

$$
\mathbf{H}=\mathbf{S}^{-1/2}\mathbf{H}^{\prime}\mathbf{S}^{-1/2} \tag{10.204}
$$

其非对角元 $H_{ab}$ 即对应于待求的非绝热耦合。在两态情形下，我们有

<a id="eq:almo_coupling"></a>

$$
H_{ab}=\frac{1}{1-S_{ab}^{2}}\left|H^{\prime}_{ab}-\frac{H^{\prime}_{aa}+H^{\prime}_{bb}}{2}S_{ab}\right| \tag{10.205}
$$

该式需要两个 ALMO 非绝热态势之间的重叠，以及 $\mathbf{H}^{\prime}$ 的对角元和非对角元。态间重叠由下式给出

<a id="eq:state_overlap"></a>

$$
S_{ab}=\langle\psi_{a}|\psi_{b}\rangle=\mathrm{det}\big{[}(\mathbf{C}^{(a)}_{\mathrm{o}})^{\dagger}\mathbf{S}\mathbf{C}^{(b)}_{\mathrm{o}}\big{]}\;. \tag{10.206}
$$

其中 $\mathbf{C}^{(a)}_{\mathrm{o}}$ 和 $\mathbf{C}^{(b)}_{\mathrm{o}}$ 分别是非绝热态势 $|\psi_{a}\rangle$ 和 $|\psi_{b}\rangle$ 中占据轨道的 MO 系数，$\mathbf{S}$ 是 AO 重叠矩阵。

非绝热哈密顿量矩阵的各个元素可以利用多态 DFT（multi-state DFT, MSDFT）方法来求值。[[220]](../bib_references/bib.md#bib216)
对于对角元，直接采用两个非绝热态势的 Kohn-Sham（KS）能量即可：

<a id="Ch10.E207"></a>

$$
H^{\prime}_{aa}=E_{a}^{\mathrm{KS}}[\mathbf{P}^{(a)}],\quad H^{\prime}_{bb}=E_{b}^{\mathrm{KS}}[\mathbf{P}^{(b)}] \tag{10.207}
$$

其中 $\mathbf{P}^{(a)}$ 和 $\mathbf{P}^{(b)}$ 分别是与两个 ALMO 态 $|\psi_{a}\rangle$ 和 $|\psi_{b}\rangle$ 相关联的一电子密度矩阵。非对角元的近似在理论上更具挑战性。在最初的 MSDFT 格式中，[[220]](../bib_references/bib.md#bib216)

<a id="eq:msdft1"></a>

$$
H^{\prime}_{ab}=S_{ab}\left[V_{\mathrm{nn}}+\mathbf{P}_{ab}\cdot\mathbf{h}+\frac{1}{2}\mathbf{P}_{ab}\cdot\mathbf{II}\cdot\mathbf{P}_{ab}+\frac{1}{2}(\Delta E_{a}^{\mathrm{c}}+\Delta E_{b}^{\mathrm{c}})\right] \tag{10.208}
$$

其中 $\mathbf{P}_{ab}$ 是两个 ALMO 态之间的一粒子跃迁密度矩阵

<a id="eq:trans_den"></a>

$$
\mathbf{P}_{ab}=\mathbf{C}_{\mathrm{o}}^{(a)}\left[(\mathbf{C}_{\mathrm{o}}^{(b)})^{\dagger}\mathbf{S}\mathbf{C}_{\mathrm{o}}^{(a)}\right]^{-1}(\mathbf{C}_{\mathrm{o}}^{(b)})^{\dagger} \tag{10.209}
$$

式（[10.208](#eq:msdft1)）右端的前三项分别对应于核排斥、单电子哈密顿量（动能与核-电子吸引）以及完整双电子积分（库仑积分与全部 HF 交换）的贡献，这些项可以像非正交组态相互作用（non-orthogonal CI）中那样推导出来。[[1356]](../bib_references/bib.md#bib1417)

最后一项计入交换-关联（exchange-correlation, XC）泛函的贡献，作为对 HF 耦合的修正，其数值由每个非绝热态势下用同一张一电子密度矩阵计算的 KS 能量与 HF 能量之差取平均得到：

<a id="Ch10.E210"></a>

$$
\displaystyle\Delta E_{a}^{\mathrm{c}} \tag{10.210a}
$$

该方法在文献 [[898]](../bib_references/bib.md#bib929)
 中被记作 ALMO(MSDFT)，结果发现它会高估所测试的空穴转移与电子转移体系的电子耦合。文献 [[898]](../bib_references/bib.md#bib929)
 提出了一种改进方法，记作 ALMO(MSDFT2)，它使用对称化跃迁密度矩阵的 XC 能量来求值 XC 贡献

<a id="eq:msdft2"></a>

$$
H_{ab}^{\prime}=S_{ab}\left(V_{\mathrm{nn}}+\mathbf{P}_{ab}\cdot\mathbf{h}+\tfrac{1}{2}\mathbf{P}_{ab}\cdot\mathbf{II}\cdot\mathbf{P}_{ab}+E_{\mathrm{xc}}[\tilde{\mathbf{P}}_{ab}]\right) \tag{10.211}
$$

其中

<a id="Ch10.E212"></a>

$$
\tilde{\mathbf{P}}_{ab}=\frac{1}{2}(\mathbf{P}_{ab}+\mathbf{P}_{ba})\;. \tag{10.212}
$$

需要注意的是，在式（[10.211](#eq:msdft2)）中，若采用杂化泛函，$\mathbf{II}$
只包含库仑积分以及一部分精确交换。

根据文献 [[898]](../bib_references/bib.md#bib929)
 中的基准测试结果，ALMO(MSDFT2) 在空穴转移和电子转移方面比原始的 MSDFT 方法精度更好，因此在 **Q-Chem** 中被实现为计算 ALMO 非绝热态势之间电子耦合的默认方法。我们指出，当两个态之间的重叠接近奇异时，式（[10.211](#eq:msdft2)）给出的结果可能变得不准确，因为在构造跃迁密度矩阵时需要对式（[10.209](#eq:trans_den)）中的

<a id="Ch10.E213"></a>

$$
\boldsymbol{\sigma}_{ba}=(\mathbf{C}_{\mathrm{o}}^{(b)})^{\dagger}\mathbf{S}\mathbf{C}_{\mathrm{o}}^{(a)} \tag{10.213}
$$

求逆。为规避这一数值问题，可以用 Penrose 伪逆替换式（[10.209](#eq:trans_den)）中的逆矩阵，文献 [[1049]](../bib_references/bib.md#bib1094)
 出于类似目的曾提出过这一做法。

利用原始 MSDFT 或 MSDFT2 格式计算基于 ALMO 的态之间电子耦合的方法，已被推广到由基于 ALMO 的 $\Delta$SCF 计算所制备的非 aufbau 电子态。[[899]](../bib_references/bib.md#bib931)
该方法可称为 $\Delta$-ALMO(MSDFT) 或 $\Delta$-ALMO(MSDFT2)，能够计算局域激发（locally excited, LE）态与电荷转移（charge-transfer, CT）态之间的耦合。关于任务控制的更多细节见第 [10.15.3.4](#subsubsec:frag_diab_job_control) 节。

## 10.15.3.2 投影算符非绝热化方法（Projection operator Diabatization, POD）

除基于 ALMO 的非绝热化方法之外，**Q-Chem** 还提供了其他基于片段的非绝热化方法。投影算符非绝热化（projection operator diabatization, POD）方法 [[705]](../bib_references/bib.md#bib737)
从体系的标准 KS-DFT 计算出发，对收敛后的 Fock 矩阵进行后处理。它首先将 Fock 矩阵变换到 Löwdin 正交化的 AO 基下，然后将其划分为给体块与受体块，并假定这些正交化后的 AO 基函数仍保留其原有的片段标记：

<a id="eq:pod_fock"></a>

$$
\tilde{\mathbf{F}}=\mathbf{S}^{-1/2}\mathbf{F}\mathbf{S}^{-1/2}=\begin{pmatrix}\tilde{\mathbf{F}}_{dd}&\tilde{\mathbf{F}}_{da}\\
\tilde{\mathbf{F}}_{ad}&\tilde{\mathbf{F}}_{aa}\end{pmatrix} \tag{10.214}
$$

随后分别对 $\tilde{\mathbf{F}}_{dd}$ 和 $\tilde{\mathbf{F}}_{aa}$ 对角化

<a id="Ch10.E215"></a>

$$
\boldsymbol{\epsilon}_{d}=\mathbf{D}_{d}^{\dagger}\tilde{\mathbf{F}}_{dd}\mathbf{D}_{d},\ \boldsymbol{\epsilon}_{a}=\mathbf{D}_{a}^{\dagger}\tilde{\mathbf{F}}_{aa}\mathbf{D}_{a}, \tag{10.215}
$$

其中本征矢量 $\mathbf{D}_{d}$ 和 $\mathbf{D}_{a}$ 定义了单粒子"非绝热态"：

<a id="A3.S8.EGx101"></a>

$$
\displaystyle\begin{aligned} \displaystyle\big{|}\bar{\varphi}^{(d)}_{p}\big{\rangle}&\displaystyle=\sum_{\mu}\big{|}\tilde{\chi}^{(d)}_{\mu}\big{\rangle}(D_{d})^{\mu}_{\ p}\\
\displaystyle\big{|}\bar{\varphi}^{(a)}_{p}\big{\rangle}&\displaystyle=\sum_{\mu}\big{|}\tilde{\chi}^{(a)}_{\mu}\big{\rangle}(D_{a})^{\mu}_{\ p},\\
\end{aligned} \tag{10.216}
$$

并把 Fock 矩阵的非对角块变换到这一非绝热基下

<a id="Ch10.E217"></a>

$$
\bar{\mathbf{F}}_{da}=\mathbf{D}_{d}^{\dagger}\tilde{\mathbf{F}}_{da}\mathbf{D}_{a} \tag{10.217}
$$

于是得到

<a id="Ch10.E218"></a>

$$
\bar{\mathbf{F}}=\begin{pmatrix}\boldsymbol{\epsilon}_{d}&\bar{\mathbf{F}}_{da}\\
\bar{\mathbf{F}}_{ad}&\boldsymbol{\epsilon}_{a}\end{pmatrix} \tag{10.218}
$$

这些单粒子非绝热轨道之间的耦合可以直接从 $\bar{\mathbf{F}}_{da}$ 的矩阵元素中读出。

**Q-Chem** 对 POD 方法的实现遵循文献 [[705]](../bib_references/bib.md#bib737)
 与 [[1513]](../bib_references/bib.md#bib1582)
 的描述，其中使用闭壳层参考体系来生成待处理的 Fock 矩阵，*即* 式（[10.214](#eq:pod_fock)）中的 $\mathbf{F}$。默认情况下，对空穴转移情形只计算 $D$(HOMO)–$A$(HOMO) 耦合，对电子转移情形只计算 $D$(LUMO)–$A$(LUMO) 耦合。若要计算多对给体与受体轨道之间的耦合，用户可将 *$rem* 变量设为 POD_MULTI_PAIRS = TRUE，并通过 POD_WINDOW 控制轨道对的数量。具体说明见第 [10.15.3.4](#subsubsec:frag_diab_job_control) 节。

由于式（[10.214](#eq:pod_fock)）中使用了全局 Löwdin 正交化轨道，POD 所创建的非绝热轨道无法严格局域在片段上。这使得 POD 结果随所用 AO 基组的改变而不稳定：当使用更大的基组时，不同片段上的 AO 基函数之间的混合变得更强，所得的 $H_{ab}$ 也随之减小。为缓解这一问题，Ghan *et al.* 提出了改进的 POD 方法，命名为 "POD2"。[[437]](../bib_references/bib.md#bib449)

该方法避免了对 AO 基做全局 Löwdin 正交化；取而代之的是，分别对（原始 AO 基下）Fock 矩阵的给体块与受体块进行对角化：

<a id="Ch10.E219"></a>

$$
\mathbf{F}_{dd}\mathbf{C}_{d}=\mathbf{S}_{dd}\mathbf{C}_{d}\boldsymbol{\epsilon}_{d},\quad\mathbf{F}_{aa}\mathbf{C}_{a}=\mathbf{S}_{aa}\mathbf{C}_{a}\boldsymbol{\epsilon}_{a} \tag{10.219}
$$

所得的非绝热 MO 系数矩阵在 AO 基下呈片段分块对角形式：

<a id="Ch10.E220"></a>

$$
\mathbf{C}_{\text{diab}}=\begin{pmatrix}\mathbf{C}_{d}&\mathbf{0}\\
\mathbf{0}&\mathbf{C}_{a}\\
\end{pmatrix} \tag{10.220}
$$

将 AO Fock 矩阵变换到这一非绝热 MO 基下，所得矩阵的 D–D 块与 A–A 块均为对角矩阵：

<a id="Ch10.E221"></a>

$$
\bar{\mathbf{F}}_{\text{diab}}=\mathbf{C}_{\text{diab}}^{T}\mathbf{F}\mathbf{C}_{\text{diab}}=\begin{pmatrix}\boldsymbol{\epsilon}_{d}&\bar{\mathbf{F}}_{da}\\
\bar{\mathbf{F}}_{ad}&\boldsymbol{\epsilon}_{a}\\
\end{pmatrix} \tag{10.221}
$$

直接使用非对角块（$\bar{\mathbf{F}}_{da}$）中的矩阵元素会高估耦合，因为非绝热 MO $\mathbf{C}_{d}$ 与 $\mathbf{C}_{a}$ 彼此不正交。因此需要最后一步正交化，以得到分别位于给体和受体上的某一对轨道之间的非绝热耦合。将这一对轨道记作 $\phi_{d}$ 和 $\phi_{a}$，可以构造 $2\times 2$ 的哈密顿量矩阵和重叠矩阵：

<a id="Ch10.E222"></a>

$$
\mathbf{H}=\begin{pmatrix}\epsilon_{d}&\bar{F}_{da}\\
\bar{F}_{ad}&\epsilon_{a}\\
\end{pmatrix},\quad\mathbf{S}=\begin{pmatrix}1&S_{da}\\
S_{ad}&1\\
\end{pmatrix} \tag{10.222}
$$

Ghan *et al.* 研究了两种正交化格式。[[437]](../bib_references/bib.md#bib449)

第一种方法对 $\phi_{d}$ 和 $\phi_{a}$ 做 Löwdin 正交化，记为 POD2L。正交化后的非绝热轨道之间的耦合为

<a id="Ch10.E223"></a>

$$
H_{da}^{\text{eff}}=\frac{1}{1-S_{da}^{2}}\left|\bar{F}_{da}-\frac{1}{2}(\epsilon_{d}+\epsilon_{a})S_{da}\right| \tag{10.223}
$$

第二种方法采用 Gram-Schmidt 正交化，它保持两个轨道中的某一个（$\phi_{d}$ 或 $\phi_{a}$）不变，同时确保另一个与其严格正交。该格式记为 POD2GS，对于不对称情形（*例如* 表面与吸附质），可以选择保留较小片段上的轨道，此时 POD2GS 可能是更好的选择。这两种 POD2 变体相比原始 POD 方法显著提高了精度，尤其是在使用较大基组时的稳健性方面。

## 10.15.3.3 片段轨道 DFT（Fragment Orbital DFT, FODFT）

片段轨道 DFT（fragment orbital DFT, FODFT）[[1006]](../bib_references/bib.md#bib1047)
是一种计算片段之间空穴转移与电子转移的非绝热耦合的方法。文献中已发展出若干不同变体的 FODFT 方法，此处我们介绍由 Schober *et al.* 提出的最新变体。[[1217]](../bib_references/bib.md#bib1271)

考虑空穴转移过程 $\text{D}^{+}+\text{A}\to\text{D}+\text{A}^{+}$，或者等价的电子转移过程 $\text{D}^{-}+\text{A}\to\text{D}+\text{A}^{-}$，其中给体（D）与受体（A）片段分别具有 $n_{\text{D}}$ 和 $n_{\text{A}}$ 个电子，具体步骤如下。

- •

对孤立的给体片段和受体片段分别进行 KS-DFT 计算；收集收敛的片段轨道：

$\{\phi_{\text{D1}},\phi_{\text{D2}},\dots,\phi_{\text{D}n_{\text{D}}\pm 1}\}$ 和
$\{\phi_{\text{A1}},\phi_{\text{A2}},\dots,\phi_{\text{A}n_{\text{A}}}\}$
- •

对两个片段上的占据轨道做 Löwdin 正交化。反应物非绝热态势（$\text{D}^{+}\text{A}$ 或 $\text{D}^{-}\text{A}$）可表示为

<a id="Ch10.E224"></a>

$$
|\bar{\psi}_{a}\rangle=\frac{1}{\sqrt{(N-1)!}}\;\mathrm{det}\left\{\bar{\phi}_{\text{D1}},\bar{\phi}_{\text{D2}},\dots,\bar{\phi}_{\text{D}n_{\text{D}}\pm 1}\bar{\phi}_{\text{A1}},\bar{\phi}_{\text{A2}},\dots,\bar{\phi}_{\text{A}n_{\text{A}}}\right\} \tag{10.224}
$$

其中 "$\bar{\phi}$" 表示 Löwdin 正交化后的轨道，$N=n_{\text{D}}+n_{\text{A}}$。需要注意，电子将要跃入的最低未占轨道（空穴转移情形下为 $\phi_{\text{D}n_{\text{D}}}$，电子转移情形下为 $\phi_{\text{A}n_{\text{A}}+1}$）也必须与所有占据轨道所张成的空间正交。
- •

构造产物非绝热态势（$\text{DA}^{+}$ 或 $\text{DA}^{-}$），方法很简单：把空穴从 $\bar{\phi}_{\text{D}n_{\text{D}}}$ 移动到 $\bar{\phi}_{\text{A}n_{\text{A}}}$（空穴转移），或把多余电子从 $\bar{\phi}_{\text{D}n_{\text{D}}+1}$ 移动到 $\bar{\phi}_{\text{A}n_{\text{A}}+1}$（电子转移）

<a id="Ch10.E225"></a>

$$
|\bar{\psi}_{b}\rangle=\frac{1}{\sqrt{(N-1)!}}\;\mathrm{det}\left\{\bar{\phi}_{\text{D1}},\bar{\phi}_{\text{D2}},\dots,\bar{\phi}_{\text{D}n_{\text{D}}}\bar{\phi}_{\text{A1}},\bar{\phi}_{\text{A2}},\dots,\bar{\phi}_{\text{A}n_{\text{A}}\pm 1}\right\} \tag{10.225}
$$

- •

计算 $|\bar{\psi}_{a}\rangle$ 与 $|\bar{\psi}_{b}\rangle$ 之间的电子耦合，该耦合近似为由反应物非绝热态势构造的 Kohn-Sham Fock 算符在正交化片段轨道之间的矩阵元：

<a id="A3.S8.EGx102"></a>

$$
\displaystyle\langle\bar{\psi}_{a}|\hat{H}|\bar{\psi}_{b}\rangle\approx\begin{cases}\langle\phi_{\text{D}n_{\text{D}}}|\hat{f}_{\text{KS}}|\phi_{\text{A}n_{\text{A}}}\rangle&\text{HT}\\
\langle\phi_{\text{D}n_{\text{D}}+1}|\hat{f}_{\text{KS}}|\phi_{\text{A}n_{\text{A}}+1}\rangle&\text{ET}\end{cases} \tag{10.226}
$$

上述方法记作 FODFT($2n-1$)@$\text{D}^{+}\text{A}$（空穴转移）/FODFT($2n+1$)@$\text{D}^{-}\text{A}$（电子转移），[[1217]](../bib_references/bib.md#bib1271)
因为在制备片段轨道时显式考虑了带电片段，并且 KS Fock 矩阵由 $2n\mp 1$ 个占据轨道构造。除此之外，FODFT 还有另外两种变体：

1. 1.

FODFT($2n$)@DA：[[1232]](../bib_references/bib.md#bib1287)
 D 与 A 均以闭壳层制备片段轨道；KS Fock 算符由 $2n$ 个占据轨道构造。
2. 2.

FODFT($\mathrm{2n-1}$)@DA（空穴转移）/
FODFT($2n+1$)@$\text{D}^{-}\text{A}^{-}$（电子转移）：[[1006]](../bib_references/bib.md#bib1047)
 片段轨道在体系带有一个多余电子的情况下制备（空穴转移用 DA，电子转移用 $\text{D}^{-}\text{A}^{-}$），
而在构造 KS Fock 算符时移除一个占据轨道。

根据基准测试结果，[[1217]](../bib_references/bib.md#bib1271)
FODFT($2n-1$)@$\text{D}^{+}\text{A}$（空穴转移）/FODFT($2n+1$)@$\text{D}^{-}\text{A}$（电子转移）
是表现最好的方法，原因可能在于它显式考虑了带电片段，并且在片段轨道制备与 Fock 矩阵构造中保持了电子数的一致性。

FODFT 方法存在的一个问题是，对于不对称体系，结果取决于人们如何为一个电子或空穴转移过程选择初态与末态（*例如* $\text{D}^{+}\text{A}$ 与 $\text{DA}^{+}$ 之别），对以 $2n\pm 1$ 个占据轨道构造 Fock 矩阵的那两种变体尤其如此。[[898]](../bib_references/bib.md#bib929)
**Q-Chem** 对 FODFT($\mathrm{2n-1}$)@DA/FODFT($2n+1$)@$\text{D}^{-}\text{A}^{-}$
的实现会自动以两种方式计算 $H_{ab}$ 并报告其平均值，因为这只需要额外构造一次 Fock 矩阵。然而，对于
FODFT($2n-1$)@$\text{D}^{+}\text{A}$/FODFT($2n+1$)@$\text{D}^{-}\text{A}$
并不自动执行这一处理。

## 10.15.3.4 基于片段的非绝热化方法的任务控制（Job control for fragment-based diabatization methods）

在 **Q-Chem** 中进行 POD、FODFT 和 ALMO(MSDFT) 计算时，需要在 *$molecule* 部分指定片段（参见第 [12.2](../ch12_frag/sect_FRAGinput.md) 节）。对于 ALMO(MSDFT) 计算，还需要在 *$almo_coupling* 部分指定每个非绝热态中各片段的电荷与自旋多重度，其中用两个连字符表示不同非绝热态势之间的分隔：

> ```qchem
> $almo_coupling
>    charge_frag_1     mult_frag_1        !diabat 1
>    charge_frag_2     mult_frag_2
>    --
>    charge_frag_1     mult_frag_1        !diabat 2
>    charge_frag_2     mult_frag_2
> $end
> ```

计算非绝热耦合所使用的方法通过 FRAG_DIABAT_METHOD 指定。需要注意的是，FODFT 的当前实现仅限于 (i) 两个片段 HOMO 之间的空穴转移，或 (ii) 两个片段 LUMO 之间的电子转移。

ALMO(MSDFT)/ALMO(MSDFT2) 方法可用于计算基态电子转移或空穴转移过程中涉及的非绝热耦合。结合基于 ALMO 的 $\Delta$SCF（由 **Q-Chem** 6.2.1 及之后版本支持），该方法还可进一步用于计算光诱导电子或空穴转移过程中 LE 态与 CT 态之间的耦合。此类计算需要设置 EX_ALMO_MSDFT = TRUE。此外，还实现了一种基于 Löwdin 正交化哈密顿量非对角元的简单方法（将式 [10.204](#eq:sym_ortho_H) 推广到多态情形），用于在同时考虑多个（$>2$）态时计算非绝热耦合。

基于 ALMO 的 $\Delta$SCF 态通过 *$scfmi_mom* 部分指定，其语法在第 [12.6.7](../ch12_frag/sect_eda2_non_aufbau.md) 节中有详细说明。不同非绝热态的指定内容之间用 "–" 分隔。对于不涉及片段内激发的非绝热态，只需写 "–" 而无需附加指定。

### `FRAG_DIABAT_METHOD`

> **指定基于片段的非绝热化方法**
>
> * **类型**: `STRING`
> * **默认值**: `NONE`
> * **可选值**:
>     * `ALMO_MSDFT`: 执行 ALMO(MSDFT) 非绝热化
>     * `POD`: 执行投影算符非绝热化（原始方法）
>     * `POD2_L`: 执行采用 Löwdin 正交化的 POD2
>     * `POD2_GS`: 执行采用 Gram-Schmidt 正交化的 POD2
>     * `ESID`: 能量分裂二聚体法（energy-split-in-dimer method），
>     * `1384`: Valeev E. F. et al. J. Am. Chem. Soc. (2006) ,
>     * `128`: , pp. 9882 . 链接（Link） 该选项等价于第 10.15.2.5 节中介绍的 FMO 方法
>     * `FODFT`: 使用片段轨道 DFT 计算电子耦合
> * **建议**: NONE

### `FRAG_DIABAT_DOHT`

> **指定所考虑的是空穴转移还是电子转移**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `TRUE`
> * **可选值**:
>     * `TRUE`: 执行空穴转移（hole transfer）
>     * `FALSE`: 执行电子转移（electron transfer）
> * **建议**: 对于 POD 和 FODFT 计算需要指定

### `FRAG_DIABAT_PRINT`

> **指定基于片段的非绝热化计算的打印级别**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * `0`: 不额外打印任何内容 $\geq 1$ 打印附加细节信息
> * **建议**: 除非需要调试信息，否则使用默认值

### `MSDFT_METHOD`

> **指定 ALMO(MSDFT) 所采用的格式**
>
> * **类型**: `INTEGER`
> * **默认值**: `2`
> * **可选值**:
>     * `1`: 原始 MSDFT 格式 [式 ( 10.208 )]
>     * `2`: ALMO(MSDFT2) 方法 [式 ( 10.211 )]
> * **建议**: 使用默认方法。注意，若请求的是.meta-GGA 泛函，该方法会被自动重置为 1。

### `MSDFT_PINV_THRESH`

> **设置态间重叠伪逆的阈值**
>
> * **类型**: `INTEGER`
> * **默认值**: `4`
> * **可选值**:
>     * $n$: 将阈值设为 10 ${}^{-n}$
> * **建议**: 使用默认值

### `EX_ALMO_MSDFT`

> **启用使用基于 ALMO 的 $\Delta$SCF 态的 MSDFT/MSDFT2 计算**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `TRUE`: 将按 $scfmi_mom 中的指定计算 ALMO- $\Delta$ SCF 态
>     * `FALSE`: 执行基态 ALMO(MSDFT) 计算。
> * **建议**: 无

### `POD_MULTI_PAIRS`

> **在 POD 中计算多对给体与受体轨道之间的耦合**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `TRUE`: 计算多对轨道之间的耦合
>     * `FALSE`: 仅计算 $D$ (HOMO)– $A$ (HOMO) 耦合（空穴转移）或 $D$ (LUMO)– $A$ (LUMO) 耦合（电子转移）
> * **建议**: 无

### `POD_WINDOW`

> **当请求多对轨道之间的耦合时，指定给体和受体轨道的数量**
>
> * **类型**: `INTEGER`
> * **默认值**: `5`
> * **可选值**:
>     * $n$: 对给体和受体均包含
>     * $n$: 个前沿占据轨道（从 $\text{HOMO}-n+1$ 到 HOMO） 以及
>     * $n$: 个前沿虚轨道（从 LUMO 到 $\text{LUMO}+n-1$）
> * **建议**: 无

### `FODFT_METHOD`

> **指定 FODFT 方法的具体变体**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **可选值**:
>     * `1`: FODFT( $\mathrm{2n-1}$ )@ $D^{+}A$ （空穴转移）/ FODFT( $\mathrm{2n+1}$ )@ $D^{-}A$ （电子转移）
>     * `2`: FODFT( $\mathrm{2n}$ )@ $DA$
>     * `3`: FODFT( $\mathrm{2n-1}$ )@ $DA$ （空穴转移）/ FODFT( $\mathrm{2n+1}$ )@ $D^{-}A^{-}$ （电子转移）
> * **建议**: 默认方法的整体表现最佳

### `FODFT_DONOR`

> **指定 FODFT 计算中的给体片段**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **可选值**:
>     * `1`: 以第一个片段作为给体
>     * `2`: 以第二个片段作为给体
> * **建议**: 当 FODFT_METHOD = 1 时，带电片段必须作为给体片段

???+ example "示例 10.77: 乙烯二聚体空穴转移的 ALMO(MSDFT2) 计算"
    ```qchem
    $molecule
    1 2
    --
    1 2
      C      0.000000    0.000000    0.000000
      C      1.332000    0.000000    0.000000
      H     -0.574301    0.000000   -0.928785
      H     -0.574301    0.000000    0.928785
      H      1.906301    0.000000    0.928785
      H      1.906301    0.000000   -0.928785
    --
    0 1
      C     -0.000000    4.000000    0.000000
      C      1.332000    4.000000   -0.000000
      H     -0.574301    4.000000    0.928785
      H     -0.574301    4.000000   -0.928785
      H      1.906301    4.000000   -0.928785
      H      1.906301    4.000000    0.928785
    $end
    
    $rem
       METHOD               PBE0
       BASIS                6-31+G(D)
       UNRESTRICTED         TRUE
       THRESH               14
       SCF_CONVERGENCE      8
       SCFMI_MODE           1
       FRGM_METHOD          STOLL
       FRAG_DIABAT_METHOD   ALMO_MSDFT
       INTEGRAL_SYMMETRY    FALSE
       POINT_GROUP_SYMMETRY FALSE
    $end
    
    $almo_coupling
      1  2
      0  1
      --
      0  1
      1  2
    $end
    ```

???+ example "示例 10.78: 吲哚（Indole）${}^{+\ast}$ 与鸟嘌呤之间空穴转移的 ALMO(MSDFT2) 计算。
吲哚自由基阳离子处于非 aufbau 态，其中一个 $\beta$ 电子从 HOMO 被激发至 HOMO $-$ 1。"
    ```qchem
    $molecule
    1 2
    --
    1 2
    C        2.36540       -2.78410        3.38000
    C        3.73980       -2.83830        3.38000
    C        2.00000       -1.40150        3.38000
    C        3.20860       -0.65020        3.38000
    C        0.77390       -0.70880        3.38000
    C        3.22680        0.75070        3.38000
    C        0.78630        0.67870        3.38000
    C        2.00000        1.40150        3.38000
    N        4.24650       -1.55510        3.38000
    H        4.40550       -3.69200        3.38000
    H        5.22930       -1.31740        3.38300
    H       -0.16770       -1.25470        3.38000
    H        4.16090        1.30910        3.38000
    H       -0.15420        1.22450        3.38000
    H        1.97300        2.48860        3.38000
    H        1.69890       -3.63700        3.38000
    --
    0 1
    C        1.63430       -2.77360        0.00200
    C        1.25300       -0.68190        0.01800
    C        1.32680        0.75830        0.00900
    C       -1.17560        0.58330        0.00600
    C        0.00000       -1.29190        0.00000
    O        2.29090        1.51390       -0.00300
    N        0.26680       -2.63600       -0.00400
    N        2.26910       -1.61180        0.01600
    N        0.00000        1.29190        0.00000
    N       -2.33770        1.33540       -0.07400
    N       -1.24290       -0.72560        0.01500
    H        2.11200       -3.74490       -0.00100
    H       -0.02860        2.30410       -0.09800
    H       -2.35450        2.16800        0.50600
    H       -3.15580        0.75300        0.07300
    H       -0.42990       -3.37190       -0.01800
    $end
    
    $rem
    JOBTYPE  SP
    METHOD   B3LYP
    BASIS    6-31G
    SCF_CONVERGENCE  8
    POINT_GROUP_SYMMETRY  FALSE
    SCFMI_MODE   1
    FRGM_METHOD  STOLL
    FRAG_DIABAT_METHOD ALMO_MSDFT
    MSDFT_METHOD    2
    EX_ALMO_MSDFT   TRUE
    $end
    
    $almo_coupling
    1  2
    0  1
    --
    0  1
    1  2
    $end
    
    $scfmi_mom
    1 0 0 b
    --
    $end
    ```

???+ example "示例 10.79: 乙烯二聚体空穴转移的 POD 非绝热化方法。若使用 POD2 非绝热化方法，可将 FRAG_DIABAT_METHOD 设为 POD2_L 或 POD2_GS。"
    ```qchem
    $molecule
    0 1
    --
    0 1
      C      0.000000    0.000000    0.000000
      C      1.332000    0.000000    0.000000
      H     -0.574301    0.000000   -0.928785
      H     -0.574301    0.000000    0.928785
      H      1.906301    0.000000    0.928785
      H      1.906301    0.000000   -0.928785
    --
    0 1
      C     -0.000000    4.000000    0.000000
      C      1.332000    4.000000   -0.000000
      H     -0.574301    4.000000    0.928785
      H     -0.574301    4.000000   -0.928785
      H      1.906301    4.000000   -0.928785
      H      1.906301    4.000000    0.928785
    $end
    
    $rem
       METHOD               lrc-wpbeh
       BASIS                6-31+g(d)
       FRAG_DIABAT_METHOD   pod
       SCF_CONVERGENCE      8
       THRESH               14
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "示例 10.80: 乙烯二聚体空穴转移的 FODFT( $\mathrm{2n-1}$ )@ $D^{+}A$ 计算"
    ```qchem
    $molecule
    1 2
    --
    1 2
      C      0.000000    0.000000    0.000000
      C      1.332000    0.000000    0.000000
      H     -0.574301    0.000000   -0.928785
      H     -0.574301    0.000000    0.928785
      H      1.906301    0.000000    0.928785
      H      1.906301    0.000000   -0.928785
    --
    0 1
      C     -0.000000    4.000000    0.000000
      C      1.332000    4.000000   -0.000000
      H     -0.574301    4.000000    0.928785
      H     -0.574301    4.000000   -0.928785
      H      1.906301    4.000000   -0.928785
      H      1.906301    4.000000    0.928785
    $end
    
    $rem
       METHOD               wb97x-d
       BASIS                6-31+g(d)
       UNRESTRICTED         true
       SCF_CONVERGENCE      8
       THRESH               14
       FRAG_DIABAT_METHOD   fodft
       FODFT_METHOD         1
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
