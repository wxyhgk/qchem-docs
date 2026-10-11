---
title: "5.3.1 引言"
---

## 5.3.1 引言

（2026 年 7 月 4 日）

**Q-Chem** 目前拥有超过 30 种交换泛函以及超过 30 种相关泛函，此外还有 150 多种交换-相关（XC）泛函，后者指那些不划分为交换部分和相关部分的泛函，其原因或者是由于其参数化方式使得这种划分失去意义（*e.g.*，B97-D[[494]](../bib_references/bib.md#bib502) 或
$\omega$B97X[[223]](../bib_references/bib.md#bib218)
），或者因为它们本身就是交换与相关的标准线性组合（*e.g.*，PBE[[1062]](../bib_references/bib.md#bib1112) 或
B3LYP[[96]](../bib_references/bib.md#bib78)
）。用户可以按照指定的线性组合方式，将任意 30 多种交换泛函和/或 30 多种相关泛函组合，创建自定义的 XC 泛函。

KS-DFT 泛函可以按照 John Perdew 于 2001 年提出的分类方案（“雅各布天梯”，Jacob's Ladder）组织到一个拥有五级横档的阶梯上。[[1070]](../bib_references/bib.md#bib1116)

第一级横档包含仅依赖于（自旋）密度 $\rho_{\sigma}$ 的泛函，即局域自旋密度近似（local spin-density approximation, LSDA）。这类泛函对无限均匀电子气（uniform electron gas, UEG）是精确的，但对于密度呈现显著非均匀性的分子性质则精度很差。为了克服 LSDA 的弱点，必须引入能够描述密度非均匀性的要素：密度梯度
$\hat{\bm{\nabla}}\rho_{\sigma}$。
这些广义梯度近似（generalized gradient approximation, GGA）泛函构成了雅各布天梯的第二级横档，通常能较 LSDA 有显著提升。可用于进一步改善 GGA 泛函性能的另外两种要素是密度的拉普拉斯算符
$\hat{\nabla}^{2}\rho_{\sigma}$，和/或动能密度，

<a id="eq:tau"></a>

$$
\tau_{\sigma}=\sum_{i}^{n_{\sigma}}\big{\|}\hat{\bm{\nabla}}\psi_{i,\sigma}\big{\|}^{2}\;. \tag{5.10}
$$

虽然同时采用这两种要素的泛函在 **Q-Chem** 中均可用，但动能密度无疑是更常用的要素，并已被许多现代泛函用来增加泛函形式的灵活性，以兼顾约束满足（非经验泛函）与最小二乘拟合（半经验参数化）。依赖于这两种要素之一的泛函属于雅各布天梯的第三级横档，称为 meta-GGA。这些 meta-GGA 泛函在热化学、动力学（反应势垒高度）甚至非共价相互作用等方面往往比 GGA 进一步提升。

雅各布天梯第四级横档上的泛函称为杂化密度泛函（hybrid density functionals）。这一级横档包含了可以说当今最流行的密度泛函 B3LYP——第一个在化学中获得广泛应用的泛函。“全局”杂化（global hybrid, GH）泛函如 B3LYP（与下文介绍的“ range-separated hybrids, RSH”相区别）是在前三级横档的任一泛函基础上加入恒定比例的“精确”（Hartree-Fock）交换。因此，可以构造杂化 LSDA、杂化 GGA 和杂化 meta-GGA 泛函，尽管后两种类型更为常见。作为示例，**Q-Chem** 中实现的 B3LYP 泛函公式为[[484]](../bib_references/bib.md#bib496)

<a id="eq:GHGGA"></a>

$$
E_{\text{xc}}^{\textrm{B3LYP}}=c_{\text{x}}E_{\text{x}}^{\text{HF}}+(1-c_{\text{x}}-a_{\text{x}})E_{\text{x}}^{\text{Slater}}+a_{\text{x}}E_{\text{x}}^{\text{B88}}+(1-a_{\text{c}})E_{\text{c}}^{\text{VWN1RPA}}+a_{\text{c}}E_{\text{c}}^{\text{LYP}} \tag{5.11}
$$

其中 $c_{\text{x}}=0.20$，$a_{\text{x}}=0.72$，$a_{\text{c}}=0.81$。

在泛函形式中引入精确交换的更近一些的方法是通过作用域分离（range separation）。作用域分离杂化（range-separated hybrid, RSH）泛函将精确交换贡献拆分为短程（SR）分量和长程（LR）分量，通常借助误差函数（erf）及互补误差函数（$\rm erfc\equiv 1-erf$）实现：

<a id="eq:erf_partition"></a>

$$
\frac{1}{r_{12}}=\underbrace{\frac{\mbox{erfc}(\omega r_{12})}{r_{12}}}_{\text{SR}}+\underbrace{\frac{\mbox{erf}(\omega r_{12})}{r_{12}}}_{\text{LR}}\; \tag{5.12}
$$

式 ([5.12](#eq:erf_partition)) 右端第一项是奇异的但属于短程项，并在 $\sim 1/\omega$ 的长度尺度上衰减为零，而第二项构成一个非奇异的长程背景。RSH XC 泛函一般可表示为

<a id="eq:RSHGGA"></a>

$$
E_{\text{xc}}^{\text{RSH}}=c_{\text{x}}E_{\text{x,SR}}^{\text{HF}}+c_{\text{x,LR}}E_{\text{x,LR}}^{\text{HF}}+(1-c_{\text{x,SR}})E_{\text{x,SR}}^{\text{DFT}}+(1-c_{\text{x,LR}})E_{\text{x,LR}}^{\text{DFT}}+E_{\text{c}}^{\text{DFT}}\;, \tag{5.13}
$$

其中分别使用库仑算符的 SR 和 LR 部分来计算 HF 交换能 $E_{\text{x,SR}}^{\text{HF}}$ 和 $E_{\text{x,LR}}^{\text{HF}}$。
相应的 DFT 交换泛函以同样的方式拆分，但相关能 $E_{\text{c}}^{\text{DFT}}$ 是使用完整库仑算符 $r_{12}^{-1}$ 计算的。式 ([5.13](#eq:RSHGGA)) 中的两个线性参数里，$c_{\text{x,LR}}$ 通常要么设为 1，以定义长程校正（long-range corrected, LRC）RSH 泛函（见第 [5.6](sect_LRC-DFT.md) 节），要么设为零，从而定义屏蔽交换（screened-exchange, SE）RSH 泛函。另一方面，短程精确交换的比例（$c_{\text{x,SR}}$）既可通过最小二乘拟合确定，也可借助绝热连接（adiabatic connection）从理论上加以论证，或者直接设为零。与全局杂化泛函一样，RSH 泛函可以使用前三级横档的所有要素来构造。局域 DFT 交换关闭、非局域精确交换开启的速率由参数 $\omega$ 控制。较大的 $\omega$ 值往往导致衰减函数（attenuator）不够平滑（除非短程精确交换比例非常大），而较小的值（*e.g.*，$\omega=0.2$–0.4 bohr${}^{-1}$）在半经验 RSH 泛函中最常见。

雅各布天梯的最后一级横档包含不仅使用占据轨道（通过精确交换），还使用虚轨道（通过 MP2 或无规相位近似（random phase approximation, RPA）等方法）的泛函。这些双重杂化（double hybrid, DH）泛函是 **Q-Chem** 中计算代价最高的密度泛函，但也可以非常精确。DH 泛函最基本的形式为

<a id="eq:DHGGA"></a>

$$
E_{\text{xc}}^{\text{DH}}=c_{\text{x}}E_{\text{x}}^{\text{HF}}+(1-c_{\text{x}})E_{\text{x}}^{\text{DFT}}+c_{\text{c}}E_{c}^{\text{MP2}}+(1-c_{\text{c}})E_{\text{c}}^{\text{DFT}}\;. \tag{5.14}
$$

与杂化泛函一样，这些系数可以具有理论依据，也可以通过经验确定。此外，双重杂化泛函既可以全局使用精确交换，也可以通过作用域分离方式使用，其组分既可以像 LSDA 一样简单，也可以像 meta-GGA 泛函那样先进。关于双重杂化泛函的更多信息见第 [5.9](subsec_dhdft.md) 节。

最后，近年来 KS-DFT 的最后一项重大进展是发展了能够准确描述非共价相互作用（尤其是色散）的方法。从原理上讲，雅各布天梯上的所有泛函都可以与这些色散校正组合使用，尽管在某些情况下这种组合反而有害，特别是对于那些部分使用非共价相互作用数据集进行参数化的半经验泛函，它们本身已倾向于高估非共价相互作用能。**Q-Chem** 中最常用的此类方法有：

- •

非局域相关（non-local correlation, NLC）泛函（第 [5.7.2](sect_VV10.md) 节），包括 Vydrov 和 Van Voorhis 提出的
[[1414]](../bib_references/bib.md#bib1475)
（VV09 和 VV10）以及 Lundqvist 和 Langreth 提出的[[327]](../bib_references/bib.md#bib331)

（vdW-DF-04 和 vdW-DF-10）。Sabatini 及其合作者改进的 VV10 NLC 泛函（rVV10）同样可用[[1192]](../bib_references/bib.md#bib1247)
。
- •

来自 Grimme 及其他作者的、经阻尼处理的原子间成对经验色散势[[494]](../bib_references/bib.md#bib502)

[DFT-D2, DFT-CHG, DFT-D3(0), DFT-D3(BJ), DFT-D3(CSO), DFT-D3M(0), DFT-D3M(BJ), and DFT-D3(op)]；
见第 [5.7.3](subsec_DFT-D.md) 节。
- •

Johnson 和 Becke 提出的交换偶极模型（exchange-dipole models, XDM）（XDM6 和 XDM10）；见第 [5.7.4](sect_XDM.md) 节。
- •

Tkatchenko-Scheffler (TS) 色散相互作用方法；[[1361]](../bib_references/bib.md#bib1421)
见第 [5.7.5](sect_TS.md) 节。
- •

用于 van der Waals 相互作用的多体色散（Many-Body Dispersion, MBD）方法[[1360]](../bib_references/bib.md#bib1422)
；
见第 [5.7.6](sect_MBD.md) 节。

下文我们将对 **Q-Chem** 中可用的泛函进行分类，包括交换泛函（第 [5.3.3](sect_DFTexchange.md) 节）、相关泛函
（第 [5.3.4](sect_DFTcorrelation.md) 节）以及交换-相关泛函（第 [5.3.5](sect_DFTexchangecorrelation.md) 节）。
在每个类别中，泛函将按雅各布天梯进行分类。交换泛函和相关泛函可以通过 *$rem* 变量
EXCHANGE 和 CORRELATION 来调用，而交换-相关泛函既可以通过设置 *$rem* 变量
METHOD 来调用，也可以（在大多数情况下，出于与早期 **Q-Chem** 版本向后兼容的考虑）通过 *$rem* 变量
EXCHANGE 来调用。这里需要谨慎对待。例如，将 METHOD 设为
PBE 请求的是 Perdew-Burke-Ernzerhof (PBE) 交换-相关泛函[[1062]](../bib_references/bib.md#bib1112)

它同时包含 PBE 交换和 PBE 相关；而设置 EXCHANGE = PBE 仅请求交换分量，设置
CORRELATION = PBE 仅请求相关分量。同时设置这两个值等价于指定
METHOD = PBE。

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<td class="ltx_td ltx_border_tt"></td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">单点计算</span></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">几何优化</span></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">频率计算</span></th>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_t" rowspan="8"><span class="ltx_text ltx_font_bold">基态</span></td>
<td class="ltx_td ltx_align_left ltx_border_t">LSDA</td>
<td class="ltx_td ltx_align_left ltx_border_t">LSDA</td>
<td class="ltx_td ltx_align_left ltx_border_t">LSDA</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">GGA</td>
<td class="ltx_td ltx_align_left">GGA</td>
<td class="ltx_td ltx_align_left">GGA</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">meta-GGA</td>
<td class="ltx_td ltx_align_left">meta-GGA</td>
<td class="ltx_td ltx_align_left">meta-GGA</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">GH</td>
<td class="ltx_td ltx_align_left">GH</td>
<td class="ltx_td ltx_align_left">GH</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">RSH</td>
<td class="ltx_td ltx_align_left">RSH</td>
<td class="ltx_td ltx_align_left">RSH</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">NLC</td>
<td class="ltx_td ltx_align_left">NLC</td>
<td class="ltx_td ltx_align_left">VV10</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">DFT-D</td>
<td class="ltx_td ltx_align_left">DFT-D</td>
<td class="ltx_td ltx_align_left">DFT-D</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">SRC</td>
<td class="ltx_td ltx_align_left">—</td>
<td class="ltx_td ltx_align_left">—</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td"></td>
<td class="ltx_td ltx_align_left">XDM</td>
<td class="ltx_td ltx_align_left">—</td>
<td class="ltx_td ltx_align_left">—</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_t" rowspan="8"><span class="ltx_text ltx_font_bold">TDDFT</span></td>
<td class="ltx_td ltx_align_left ltx_border_t">LSDA</td>
<td class="ltx_td ltx_align_left ltx_border_t">LSDA</td>
<td class="ltx_td ltx_align_left ltx_border_t">LSDA</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">GGA</td>
<td class="ltx_td ltx_align_left">GGA</td>
<td class="ltx_td ltx_align_left">GGA</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">meta-GGA</td>
<td class="ltx_td ltx_align_left">meta-GGA</td>
<td class="ltx_td ltx_align_left">meta-GGA</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">GH</td>
<td class="ltx_td ltx_align_left">GH</td>
<td class="ltx_td ltx_align_left">GH</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">RSH</td>
<td class="ltx_td ltx_align_left">RSH</td>
<td class="ltx_td ltx_align_left">RSH</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">NLC</td>
<td class="ltx_td ltx_align_left">—</td>
<td class="ltx_td ltx_align_left">—</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">DFT-D</td>
<td class="ltx_td ltx_align_left">DFT-D</td>
<td class="ltx_td ltx_align_left">DFT-D</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">SRC</td>
<td class="ltx_td ltx_align_left">—</td>
<td class="ltx_td ltx_align_left">—</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_border_bb"></td>
<td class="ltx_td ltx_align_left ltx_border_bb">—</td>
<td class="ltx_td ltx_align_left ltx_border_bb">—</td>
<td class="ltx_td ltx_align_left ltx_border_bb">—</td>
</tr>
</tbody>
</table>

表 5.1: 
SCF 计算中可用的解析性质。
泛函按雅各布天梯排列。

最后，表 [5.1](#table:DFT_grads_and_parallel) 汇总了哪些类别的泛函可用解析一阶导数（用于几何优化）或二阶导数（用于振动频率计算）。如果所请求任务类型的解析导数不可用，**Q-Chem** 将自动通过有限差分生成它们。
自 **Q-Chem** 6.3 版起，有限差分过程可以进行 MPI 并行化。
对有限差分过程的测试表明，有限差分频率的精度可达 $<1$ cm${}^{-1}$，除了那些本身就无法用谐频良好描述的极低频非键模式之外。[[847]](../bib_references/bib.md#bib880)

如第 [7.3](../ch07_excited/sect_tddft.md) 节所述，激发态的含时 DFT（time-dependent DFT, TDDFT）计算需要导数 $\partial^{2}E_{\text{xc}}/\partial\rho^{2}$。
表 [5.1](#table:DFT_grads_and_parallel) 同样给出了哪些泛函可用于 TDDFT。
