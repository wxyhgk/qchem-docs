---
title: "11.5.4 成对片段能量分解"
---

## 11.5.4 成对片段能量分解（Pairwise Fragment Energy Decomposition）

（2026 年 7 月 4 日）

针对基态和激发态，均可将 QM 区域与 EFP（Effective Fragment Potential，有效片段势）区域之间的相互作用能分解为各个能量分量以及单个溶剂分子的贡献。[[1273]](../bib_references/bib.md#bib1326)

基态 QM/EFP 能量的分解形式为：

<a id="A3.S8.EGx108"></a>
$$
\displaystyle\begin{aligned} \displaystyle E_{\text{QM--EF, gr}}&\displaystyle=E_{\text{elec}}^{(1)}+E_{\text{pol-solute}}^{(0)}+E_{\text{pol-solute}}^{(1)}+E_{\text{pol-frag}}+E_{\text{QM--EFP}}^{\text{disp}}+E_{\text{QM--EF}}^{\text{ex-rep}}\\
&\displaystyle=\langle\Psi_{\text{gr}}^{0}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{0}\rangle+\Big{[}\langle\Psi_{\text{gr}}^{\text{sol}}|\hat{H}^{\text{QM}}|\Psi_{\text{gr}}^{\text{sol}}\rangle-\langle\Psi_{\text{gr}}^{0}|\hat{H}^{\text{QM}}|\Psi_{\text{gr}}^{0}\rangle\Big{]}\\
&\displaystyle\qquad+\Big{[}\langle\Psi_{\text{gr}}^{\text{sol}}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{\text{sol}}\rangle-\langle\Psi_{\text{gr}}^{0}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{0}\rangle\Big{]}+\Big{[}E_{\text{QM--EF, gr}}^{\text{pol}}+\langle\Psi_{\text{gr}}^{\text{sol}}|\hat{V}^{\text{pol}}|\Psi_{\text{gr}}^{\text{sol}}\rangle\Big{]}\\
&\displaystyle\qquad+E_{\text{QM-EF}}^{\text{disp}}+E_{\text{QM--EF}}^{\text{ex-rep}}\end{aligned} \tag{11.78}
$$

其中各项（从左至右）依次表示：一阶静电能、零阶与一阶溶质极化能、溶剂极化能，以及加和形式的色散（dispersion）项与交换排斥（exchange-repulsion）项。上标 "sol" 和 "0" 分别表示在溶剂中和气相中优化的 QM 波函数。涉及 $\hat{V}^{\text{Coul}}$ 和
$\hat{V}^{\text{pol}}$ 算符的每个积分都可以分解为各个片段的贡献，*例如*，

<a id="eq:feed_elec"></a>
$$
E_{\text{elec}}^{(1)}=\langle\Psi_{\text{gr}}^{0}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{0}\rangle=\sum_{A}^{\text{fragments}}\langle\Psi_{\text{gr}}^{0}|\sum_{k\in A}\hat{V}_{k}^{\text{Coul}}|\Psi_{\text{gr}}^{0}\rangle \tag{11.79}
$$

其余各项的分解方式类似。极化能可以近似地分解为各个片段的贡献：

<a id="eq:feed_pol"></a>
$$
E_{\text{QM--EF, gr}}^{\text{pol}}=\frac{1}{2}\sum_{A}^{\text{fragments}}\sum_{p\in A}(-\mu^{p}F^{\text{ai,nuc,p}}+{\bar{\mu}^{p}F^{\text{ai,elec},p}}) \tag{11.80}
$$

其中 $p$ 为极化率展开点（polarizability expansion points）。
色散项和交换排斥项同样具有成对加和（pairwise-additive）性质。

唯一无法类似地拆分为片段贡献的项是零阶溶质极化能：

<a id="eq:feed_pol2"></a>
$$
E_{\text{pol-solute}}^{(0)}=\langle\Psi_{\text{gr}}^{\text{sol}}|\hat{H}^{\text{QM}}|\Psi_{\text{gr}}^{\text{sol}}\rangle-\langle\Psi_{\text{gr}}^{0}|\hat{H}^{\text{QM}}|\Psi_{\text{gr}}^{0}\rangle\;. \tag{11.81}
$$

该项在输出信息中被称为"不可分离项（non-separable term）"。
根据微扰理论，该项的绝对值预期约为一阶溶质极化项的一半，且符号相反：

<a id="eq:feed_pol3"></a>
$$
E_{\text{pol-solute}}^{(1)}=\langle\Psi_{\text{gr}}^{\text{sol}}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{\text{sol}}\rangle-\langle\Psi_{\text{gr}}^{0}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{0}\rangle\;. \tag{11.82}
$$

能量分解分析在电子激发态中的应用描述如下。零阶总溶剂致色变位移（solvatochromic shift）可表示为：

<a id="eq:FEED_exs"></a>
$$
E_{\text{solv}}^{\text{QM/EFP}}=\sum_{A}^{\text{fragments}}\big{(}\Delta E_{\text{ex/gr}}^{\text{elec(1),A}}+\Delta E_{\text{ex/gr}}^{\text{pol-solute(1)},A}+\Delta E_{\text{ex/gr}}^{\text{pol-frag(1)},A}\big{)}+\Delta E_{\text{ex/gr}}^{\text{pol-solute(0)},A}\;. \tag{11.83}
$$

各项定义如下

<a id="A3.S8.EGx109"></a>
$$
\displaystyle\Delta E_{\text{ex/gr}}^{\text{elec(1)},A} \tag{11.84}
$$

激发态的微扰极化校正[[式 (11.77)](sec_EOM-EFP.md#eq:EOM-EFP-ene2)]的片段贡献可按如下方式获得：

<a id="eq:feed:polcorr"></a>
$$
\Delta E_{\text{pol},A}=\frac{1}{2}\sum_{p\in A}\Bigl{[}-(\mu_{\rm{ex}}^{p}-\mu_{\rm{gr}}^{p})(F^{\text{mult},p}+F^{\text{nuc},p})+(\tilde{\mu}_{\text{ex}}^{p}F_{\text{ex}}^{\text{ai},p}-\tilde{\mu}_{\text{gr}}^{p}F_{\text{gr}}^{\text{ai},p})-(\mu_{\text{ex}}^{p}-\mu_{\text{gr}}^{p}+\tilde{\mu}_{\text{ex}}^{p}-\tilde{\mu}_{\text{gr}}^{p})F_{\text{ex}}^{\text{ai},p}\Bigr{]} \tag{11.88}
$$

其中 $A$ 为目标片段。

能量分解对每个计算所得的激发态分别进行。激发态分析已在 ccman 和 ccman2 中针对 CIS/TD-DFT 及 EOM-CCSD 方法实现。
能量分解分析通过关键字 EFP_PAIRWISE 激活。
基态与激发态的能量分解均分两步进行，由关键字 EFP_ORDER 控制。
在第一步中（EFP_ORDER = 1），计算并输出一阶静电能以及
$\langle\Psi_{\text{gr}}^{0}|\hat{H}^{\text{QM}}|\Psi_{\text{gr}}^{0}\rangle$
（激发态则为 $\langle\Psi_{\text{ex}}^{0}|\hat{H}^{\text{QM}}|\Psi_{\text{ex}}^{0}\rangle$）
这部分不可分离项。
在第二步中（EFP_ORDER = 2），计算其余各项。因此，
若要进行完整分析，用户需要依次运行两次模拟，分别将 EFP_ORDER
设为 1 和 2。表 [11.9](#tbl:feed) 列出了输出信息中用于表示式 ([11.78](#eq:FEED_gs))–([11.88](#eq:feed:polcorr)) 中各项的记号。

表 11.9：能量分解各项的记号

| EFP_ORDER = 1 |  |
| --- | --- |
| (0) ELEC ENERGY <Psi_0\|Vcoul\|Psi_0> | $\langle\Psi_{\text{gr/ex}}^{0}\|\hat{V}^{\text{Coul},A}\|\Psi_{\text{gr/ex}}^{0}\rangle$ |
| TOTAL QM-EFP ELECTROSTATIC ENERGY | $E_{\text{gr/ex}}^{\text{elec(1)}}=\sum_{A}^{\text{fragments}}\textbf{(0)}_{A}$ |
| NON-SEPARABLE TERM <Psi_0\|H0\|Psi_0> | $\langle\Psi_{\text{gr/ex}}^{0}\|\hat{H}_{\text{QM}}\|\Psi_{\text{gr/ex}}^{0}\rangle$ |
| EFP_ORDER = 2 |  |
| (1) ELEC + SOLUTE POL ENERGY <Psi_sol\|Vcoul\|Psi_sol> | $\langle\Psi_{\text{gr/ex}}^{\text{sol}}\|\hat{V}^{\text{Coul},A}\|\Psi_{\text{gr/ex}}^{\text{sol}}\rangle$ |
| (2) SOLVENT POL ENERGY Epol | $\frac{1}{2}\sum_{p\in A}(-\mu^{p}_{\text{gr}}F^{\text{ai,nuc},p}+{\bar{\mu}^{p}_{\text{gr}}F_{\text{gr}}^{\text{ai,elec}},p})$ |
| (3) SOLVENT POL ENERGY <Psi_sol\|Vpol\|Psi_sol> | $\langle\Psi_{\text{gr/ex}}^{\text{sol}}\|\hat{V}^{\text{pol},A_{\text{gr}}}\|\Psi_{\text{gr/ex}}^{\text{sol}}\rangle$ |
| (4) SOLVENT POL ENERGY Epol_corr | 仅适用于激发态，见式 ( 11.88 ) |
| (5) SOLVENT POL ENERGY TOTAL | (2)+(3) |
| (6) PAIRWISE TOTAL ENERGY | (1) + (2) + (3) |
| QM-EFP TOTAL ENERGY | $\sum_{A}^{\text{fragments}}\textbf{(6)}_{A}$ |
| NON-SEPARABLE TERM <Psi_sol\|H0\|Psi_sol> | $\langle\Psi_{\text{gr/ex}}^{\text{sol}}\|\hat{H}_{\text{QM}}\|\Psi_{\text{gr/ex}}^{\text{sol}}\rangle$ |

成对分析作为激发态方法中性质计算的一部分执行，由于需要重新计算静电积分和极化积分，会带来额外的计算开销。在 CIS 和 TDDFT 计算中，用户可通过关键字 EFP_PAIRWISE_STATES 以及分组 *$efp_pairwise_states*，选择仅对部分激发态进行成对分析；该分组用一行给出需要纳入分析的激发态编号，其中第一个激发态的索引为 1。

> ```qchem
> $efp_pairwise_states
>     i j k
> $end
> ```
