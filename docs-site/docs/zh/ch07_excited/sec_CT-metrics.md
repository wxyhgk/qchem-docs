---
title: "7.3.2 电荷转移度量"
---

## 7.3.2 电荷转移度量

（2026 年 7 月 4 日）

由于自相互作用（self-interaction）问题，标准密度泛函无法给出具有正确长程库仑尾（long-range Coulomb tail）的势。因此，对于采样该尾部区域的状态（*例如*，弥散的里德堡（Rydberg）态以及某些电荷转移（charge transfer）激发态），其激发能无法被准确计算。[[213]](../bib_references/bib.md#bib210)

可以借助一个空间重叠度量 $\Lambda$ 来评估某个特定激发态的电荷转移特征程度，其定义为[[1057]](../bib_references/bib.md#bib1102)

<a id="eq:Tozer-metric"></a>

$$
\Lambda=\frac{\sum_{ia}(x_{ia}+y_{ia})^{2}O_{ia}}{\sum_{jb}(x_{jb}+y_{jb})^{2}} \tag{7.16}
$$

其中 $O_{ia}$ 是占据分子轨道（MO）$\psi_{i}$ 与虚分子轨道 $\psi_{a}$ 的空间重叠：

<a id="eq:Tozer-overlaps"></a>

$$
O_{ia}=\int|\psi_{i}(\mathbf{r})|\cdot|\psi_{a}(\mathbf{r})|\;d\mathbf{r}\;. \tag{7.17}
$$

由于占据 MO 与虚 MO 是正交的，$\langle\psi_{i}|\psi_{a}\rangle$，因此必须使用绝对值符号；不过 **Q-Chem** 提供了改用 MO 平方 instead 的选项：

<a id="eq:Tozer-overlaps2"></a>

$$
\tilde{O}_{ia}=\int|\psi_{i}(\mathbf{r})|^{2}|\psi_{a}(\mathbf{r})|^{2}\;d\mathbf{r}\;. \tag{7.18}
$$

在这种情况下，式 ([7.16](#eq:Tozer-metric)) 中的 $O_{ia}$ 将被 $\tilde{O}_{ia}$ 取代。对于该度量的原始版本（使用 $O_{ia}$，且 $\psi_{i}$ 与 $\psi_{a}$ 为正则 MO），Tozer 及其合作者发现局域价层（valence）激发的 $0.45\leq\Lambda\leq 0.89$，而里德堡激发则落在 $0.08\leq\Lambda\leq 0.27$ 区间内。[[1057]](../bib_references/bib.md#bib1102)

此外，他们建议采用依赖于具体泛函的截断值，用以判断某个激发是否具有过多的电荷转移特征，以至于 TDDFT（含时密度泛函理论）结果不可信。注意，尽管 **Q-Chem** 实现的是文献 [[1057]](../bib_references/bib.md#bib1102) 中提出的式 ([7.16](#eq:Tozer-metric)) 定义，但该表达式中用于归一化的分母对于完整的 TDDFT 计算（*即*，未使用 TDA（绝热近似，Tamm–Dancoff Approximation）的计算）是不一致的，[[563]](../bib_references/bib.md#bib587) 因为此时 $\mathbf{x}$ 与 $\mathbf{y}$ 的归一化条件是 $\sum_{ia}(x_{ia}^{2}-y_{ia}^{2})=1$，而非 $\sum_{ia}(x_{ia}^{2}+y_{ia}^{2})=1$。

经验上，$\Lambda$ 度量与 TDDFT 误差之间存在非常好的相关性，[[1057]](../bib_references/bib.md#bib1102)

但其数值难以用物理上的电荷分离来解释。因此，有人提出了一个与之类似的度量

<a id="eq:Delta-r"></a>

$$
\Delta r=\frac{\sum_{ia}(x_{ia}+y_{ia})^{2}\|\mathbf{R}_{ia}\|}{\sum_{jb}(x_{jb}+y_{jb})^{2}} \tag{7.19}
$$

其中

<a id="Ch7.E20"></a>

$$
\mathbf{R}_{ia}=\langle\psi_{i}|\hat{\mathbf{r}}|\psi_{i}\rangle-\langle\psi_{a}|\hat{\mathbf{r}}|\psi_{i}\rangle \tag{7.20}
$$

是轨道 $\psi_{i}$ 与 $\psi_{a}$ 质心之间的矢量位移，而式 ([7.19](#eq:Delta-r)) 中的 $\|\mathbf{R}_{ia}\|$ 是二者质心之间的距离。这使得 $\Delta r$ 成为电子位移（$\psi_{i}\to\psi_{a}$）的非相干（incoherent）平均值，而当位移的相干叠加（coherent superposition）在定性上起重要作用时，这就会带来问题。[[563]](../bib_references/bib.md#bib587) 由于对任何中心对称（centrosymmetric）分子 $\Delta r$ 都为零，后来人们用一个量对其进行了补充

<a id="eq:Delta-sigma"></a>

$$
\Delta\sigma=\frac{\sum_{ia}(x_{ia}+y_{ia})^{2}\sigma_{ia}}{\sum_{jb}(x_{jb}+y_{jb})^{2}} \tag{7.21}
$$

其中

<a id="Ch7.E22"></a>

$$
\sigma_{ia}=\bigl{|}\langle\psi_{i}|\hat{r}^{2}|\psi_{i}\rangle-\langle\psi_{a}|\hat{r}^{2}|\psi_{a}\rangle\big{|}^{1/2}\;, \tag{7.22}
$$

其中 $\langle\psi_{r}|\hat{r}^{2}|\psi_{r}\rangle$ 是轨道 $\psi_{r}$ 的二阶矩。量 $\sigma_{ia}$ 给出了给体（$\psi_{i}$）与受体（$\psi_{a}$）MO 之间轨道尺寸变化的度量；并且有人提出度量

<a id="Ch7.E23"></a>

$$
\Gamma=\Delta r+\Delta\sigma \tag{7.23}
$$

用以衡量 TDDFT 激发的电荷转移特征。[[502]](../bib_references/bib.md#bib516)

人们建议，使用基于 $\Gamma$ 的“可信半径（trust radius）”（其量纲为长度）来替代 Tozer 针对 $\Lambda$ 的临界值，作为问题电荷转移跃迁的判据。[[502]](../bib_references/bib.md#bib516)

然而，一个主要的缺陷在于，这些度量（$\Lambda$、$\Delta r$、$\Delta\sigma$ 或 $\Gamma$）均对 MO 的幺正变换（unitary transformation）不具不变性。[[563]](../bib_references/bib.md#bib587) 因此，它们的数值可能相当强烈地依赖于所使用的轨道 $\{\psi_{i}\}$ 与 $\{\psi_{a}\}$。在其原始表述中，假设使用的是正则 MO；不过随后人们注意到，里德堡跃迁的 $\Gamma$ 值 somewhat 不稳定，而当改用自然跃迁轨道（Natural Transition Orbitals, NTOs，第 [7.13.3](sect_NTOs.md) 节）时则更为稳定（尤其是相对于基组变化而言）。[[502]](../bib_references/bib.md#bib516)

后来对此给出了解释。[[563]](../bib_references/bib.md#bib587) 当所讨论的跃迁由单一的一对占据/虚 NTO 主导时（这种情况很常见，但反例也容易找到），[[572]](../bib_references/bib.md#bib586) 那么 $\Delta r$ 与 $\Gamma$ 近似为关于激子（excitonic）波函数的期望值，而任何 Proper 期望值必须分别对占据 MO 的幺正变换以及虚 MO 的幺正变换保持不变。[[563]](../bib_references/bib.md#bib587) 因此，若要用这些度量，建议它们在 NTO 基下计算，而非在正则 MO 基下计算；**Q-Chem** 可以同时给出 $\Lambda$、$\Delta r$、$\Delta\sigma$ 与 $\Gamma$ 各自在这两种表示下的数值。

尽管 NTO 表示在基组变化（尤其是加入弥散函数）方面具有更好的稳定性，[[563]](../bib_references/bib.md#bib587) 但这些度量中的每一个仍然被表述为 $\psi_{i}\to\psi_{a}$ 激发的非相干、按振幅加权平均值。在 Proper 期望值中，激发振幅具有确定的相位关系，如式 ([7.10](subsec_CIS.md#eq:CIS-wavefn)) 中的 CIS 波函数所示。可以找到一些例子，其中 $\Gamma$ 度量对电荷分离给出了极具误导性的度量结果：多个单独的 $\psi_{i}\to\psi_{a}$ 激发各自对应较大的 $\|\mathbf{R}_{ia}\|$ 值，但它们相干相消（interfere destructively），导致净结果几乎没有任何电荷位移。[[563]](../bib_references/bib.md#bib587)

因此，尽管本程序包含了度量 $\Lambda$、$\Delta r$ 与 $\Gamma$（正则表示与 NTO 表示皆有），以帮助用户与现有文献对接，但仍建议电荷转移分析应基于对跃迁密度矩阵（transition density matrices）的 Proper 期望值。这些量可以使用 **libwfa** 模块计算，该模块在第 [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) 节中描述。如该节表 [10.1](../ch10_properties/ex_StateAnal_MolDen.md#table:TDM-analysis) 所示，**libwfa** 可以计算如下期望值

<a id="Ch7.E24"></a>

$$
d_{\text{e-h}}=\|\langle\mathbf{r}_{\text{elec}}-\mathbf{r}_{\text{hole}}\rangle\|\;, \tag{7.24}
$$

*换言之*，即激发电子质心与空穴（hole）质心之间距离的期望值。这构成了对电子–空穴分离程度的 Proper 度量。[[563]](../bib_references/bib.md#bib587) 激子尺寸可通过下式度量

<a id="Ch7.E25"></a>

$$
d_{\text{exc}}=\langle\|\mathbf{r}_{\text{elec}}-\mathbf{r}_{\text{hole}}\|^{2}\rangle^{1/2}\;, \tag{7.25}
$$

该量同样可由 **libwfa** 给出。电荷位移（charge-displacement）度量[[572]](../bib_references/bib.md#bib586)

也可用 **libwfa** 计算，其中包括

<a id="Ch7.E26"></a>

$$
\displaystyle d_{\text{CD1}} \tag{7.26a}
$$

其中 $\sigma_{\text{elec}}$ 与 $\sigma_{\text{hole}}$ 分别是激发电子与空穴的均方根尺寸。关于 **libwfa** 所计算的其他度量，请参见第 [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) 节的讨论。
