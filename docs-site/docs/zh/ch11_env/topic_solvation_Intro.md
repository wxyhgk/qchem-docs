---
title: "11.2.1 引言"
---

## 11.2.1 引言

（2026 年 7 月 4 日）

*从头算（ab initio）*量子化学使得从第一性原理出发研究气相分子性质成为可能。然而在液相溶液中，这些性质可能会发生显著变化，在极性溶剂中尤为如此。尽管可以通过在量子化学计算中显式地包含溶剂分子来模拟溶剂化效应（*例如*，超分子团簇计算，并对第一溶剂化层中分子的不同构型进行平均），但这类计算对计算资源的要求极高。此外，由于长程静电相互作用的重要性，团簇计算通常无法给出准确的溶剂化能。（不过，包含*部分*显式溶剂的离散/连续杂化模型可以非常有效。[[1101]](../bib_references/bib.md#bib1147)）
准确预测溶剂化自由能对于化学反应建模至关重要，对溶液中相对构象能的预测同样如此。

**Q-Chem** 包含若干不同的隐式溶剂模型，它们在精细程度上差异很大。这些模型通常被称为自洽反应场（Self-Consistent Reaction Field, SCRF）模型，因为连续介质溶剂会建立一个依赖于溶质电子密度的“反应场”（溶质哈密顿量中的附加项），因此在波函数迭代收敛过程中必须以自洽的方式对其进行更新。**Q-Chem** 中可用的最简单、最古老的模型是 multipole expansion method（多极展开方法），也称为 Kirkwood-Onsager 模型，[[569]](../bib_references/bib.md#bib580)

在该模型中，溶质分子被置于一个球形空腔内，其静电势用单中心多极展开来表示。
（这不应与 *Onsager 模型*混淆——后者使用的是偶极近似；为避免混淆，使用 *多极展开方法* 这一术语更为恰当。）更复杂的模型使用分子形状的空腔和完整的分子静电势，包括类导体 PCM（Conductor-like PCM, C-PCM）、[[79]](../bib_references/bib.md#bib61)

类导体屏蔽模型（Conductor-like Screening Model, COSMO）、

“静电表面与体积极化模拟”[SS(V)PE] 模型，[[245]](../bib_references/bib.md#bib245)
 以及与之密切相关的
“积分方程形式体系”（Integral Equation Formalism, IEF-PCM）。[[187]](../bib_references/bib.md#bib181)

关于所有这些方法及其相互关系的综述，请参见 Herbert 的综述文章。[[569]](../bib_references/bib.md#bib580)

C-PCM、IEF-PCM 和 SS(V)PE 都是所谓“表观面电荷（apparent surface charge）”SCRF 模型的例子，而由 Tomasi 及其合作者推广开的 *可极化连续介质模型（Polarizable Continuum Models, PCM）* 这一术语，如今几乎被普遍用于指代这一类溶剂化模型。
**Q-Chem** 采用的是这些 PCM 的 Switching/Gaussian（“SwiG”）实现方式，[[753]](../bib_references/bib.md#bib786)
它解决了标准 PCM 中一个长期存在（却鲜为人知）的问题，即：用于离散化溶质/连续介质界面的边界元方法可能导致溶质分子势能面出现不连续性。这些不连续性会阻碍几何优化的收敛，在振动频率计算中引入严重的人为假象，并使 *从头算*分子动力学计算几乎无法进行。[[753]](../bib_references/bib.md#bib786)

相比之下，**Q-Chem** 的 SwiG-PCM 提供了严格连续且光滑的势能面。与早期获得光滑 PCM 的尝试不同，SwiG 方法在很大程度上保留了底层积分方程溶剂模型的性质，因此溶剂化能和分子表面积几乎不受平滑处理的影响。

**Q-Chem** 中可用的其他溶剂模型包括“Langevin 偶极子（Langevin dipoles）”模型；[[394]](../bib_references/bib.md#bib402)
 以及
SM8、[[912]](../bib_references/bib.md#bib942)
 SM12、[[910]](../bib_references/bib.md#bib946)
 和 SMD 模型。[[909]](../bib_references/bib.md#bib943)

SM8 和 SM12 基于广义 Born（generalized Born）静电方法，并辅以原子表面张力项以捕获非静电效应（空穴形成、色散、交换排斥以及溶剂结构的变化）。
这些模型经过精心参数化，以重现实验测得的溶剂化自由能。[[281]](../bib_references/bib.md#bib286)

SMD 模型中的“D”代表“density（密度）”，
它将 IEF-PCM 与类似的非静电校正相结合。从统计学上讲，
SMD 的准确性并不高于或低于其他 SM$x$ 模型，[[569]](../bib_references/bib.md#bib580)
 但其优势在于基于严格静电学，由溶质精确的 SCF 密度导出。
SM12 和 SMD 模型均可在任意基组中使用。SM8 模型
使用基于“CM4”电荷的广义 Born 静电学，[[678]](../bib_references/bib.md#bib702)

而 CM4 电荷本身又基于 Löwdin 原子电荷，因此该模型只能在其参数化所使用的基组中使用：6-31G*、6-31+G* 或 6-31+G**。（若请求其他基组，将使用 6-31G* 的参数，但不建议这样做。）SM12 模型同样使用广义 Born 静电学，但以 Hirshfeld 电荷替代 CM4 电荷；后者对基组变化更加稳定，因此 SM12 可在任意基组中使用。其代价是 SM8 有解析梯度而 SM12 没有；见表 [11.2](#table:solvent_model_derivatives)。
对于 SMD，一阶和二阶解析导数（频率）均可用。

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt"><span class="ltx_text ltx_font_bold">模型</span></th>
<td class="ltx_td ltx_align_center ltx_border_tt" colspan="2"><span class="ltx_text ltx_font_bold">空腔</span></td>
<td class="ltx_td ltx_align_center ltx_border_tt"><span class="ltx_text ltx_font_bold">非静电</span></td>
<td class="ltx_td ltx_align_center ltx_border_tt"><span class="ltx_text ltx_font_bold">基组</span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_row"></th>
<td class="ltx_td ltx_align_center ltx_border_t">构造方式</td>
<td class="ltx_td ltx_align_center ltx_border_t">离散化方式</td>
<td class="ltx_td ltx_align_center"><span class="ltx_text ltx_font_bold">项？</span></td>
<td class="ltx_td ltx_align_center"><span class="ltx_text ltx_font_bold">支持情况</span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_row"></th>
<td class="ltx_td"></td>
<td class="ltx_td"></td>
<td class="ltx_td ltx_align_center"><span class="ltx_text ltx_font_bold"></span></td>
<td class="ltx_td ltx_align_center"><span class="ltx_text ltx_font_bold"></span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">Kirkwood-Onsager</th>
<td class="ltx_td ltx_align_center ltx_border_t">球形</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷</td>
<td class="ltx_td ltx_align_center ltx_border_t">否</td>
<td class="ltx_td ltx_align_center ltx_border_t">全部</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">Langevin 偶极子</th>
<td class="ltx_td ltx_align_center ltx_border_t">原子球</td>
<td class="ltx_td ltx_align_center ltx_border_t">三维空间中的</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">否</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">（用户可自定义）</td>
<td class="ltx_td ltx_align_center">偶极子</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">泊松方程</th>
<td class="ltx_td ltx_align_center ltx_border_t">原子球</td>
<td class="ltx_td ltx_align_center ltx_border_t">三维空间中的</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">否</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">求解器</th>
<td class="ltx_td ltx_align_center">（用户可自定义）</td>
<td class="ltx_td ltx_align_center">网格</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">C-PCM</th>
<td class="ltx_td ltx_align_center ltx_border_t">原子球</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷或</td>
<td class="ltx_td ltx_align_center ltx_border_t">用户</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">（用户可自定义）</td>
<td class="ltx_td ltx_align_center">平滑高斯函数</td>
<td class="ltx_td ltx_align_center">指定</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">SS(V)PE/</th>
<td class="ltx_td ltx_align_center ltx_border_t">原子球</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷或</td>
<td class="ltx_td ltx_align_center ltx_border_t">用户</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">IEF-PCM</th>
<td class="ltx_td ltx_align_center">（用户可自定义）</td>
<td class="ltx_td ltx_align_center">平滑高斯函数</td>
<td class="ltx_td ltx_align_center">指定</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">COSMO</th>
<td class="ltx_td ltx_align_center ltx_border_t">预定义的</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">点电荷</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">无</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">原子球</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">等密度 SS(V)PE</th>
<td class="ltx_td ltx_align_center ltx_border_t">等密度轮廓</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷</td>
<td class="ltx_td ltx_align_center ltx_border_t">无</td>
<td class="ltx_td ltx_align_center ltx_border_t">全部</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">CMIRS</th>
<td class="ltx_td ltx_align_center ltx_border_t">等密度轮廓</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷</td>
<td class="ltx_td ltx_align_center ltx_border_t">自动</td>
<td class="ltx_td ltx_align_center ltx_border_t">全部</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="3">SM8</th>
<td class="ltx_td ltx_align_center ltx_border_t">预定义的</td>
<td class="ltx_td ltx_border_t"></td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="3">自动</td>
<td class="ltx_td ltx_align_center ltx_border_t">6-31G*</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">原子球</td>
<td class="ltx_td ltx_align_center">不适用${}^{a}$
</td>
<td class="ltx_td ltx_align_center">6-31+G*</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td"></td>
<td class="ltx_td"></td>
<td class="ltx_td ltx_align_center">6-31+G**</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">SM12</th>
<td class="ltx_td ltx_align_center ltx_border_t">预定义的</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">不适用${}^{a}$
</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">自动</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">原子球</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">SMD</th>
<td class="ltx_td ltx_align_center ltx_border_t">预定义的</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">自动</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">原子球</td>
<td class="ltx_td"></td>
</tr>
</tbody>
<tfoot class="ltx_tfoot">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt" colspan="5">
${}^{a}$<span class="ltx_text" style="font-size:80%;">广义 Born 静电模型；不需要构造空腔。</span>
</th>
</tr>
</tfoot>
</table>

表 11.1: 
**Q-Chem** 中可用隐式溶剂模型的汇总，
展示了溶质空腔的构造与离散化方式、是否（或能否）包含非静电项，以及各模型
可用的基组。

表 [11.1](#table:solvent_models) 汇总了 **Q-Chem** 中可用的隐式溶剂模型。溶剂模型通过
SOLVENT_METHOD 关键字调用，如下所示。有关各个特定溶剂模型的更多细节可以在后续章节中找到。
一般而言，这些方法可用于任意 SCF 级别的电子结构理论，但需注意前文关于 SM8 基组的限制。
后 Hartree–Fock 计算（如 MP2 或 EOM-CC）可以通过先运行 SCF + PCM 计算来实现，此时关联波函数将采用被溶剂极化了的分子轨道（MO）和 Hartree-Fock 能级。这代表在关联理论级别上对溶剂效应的“零阶”包含，但由于高阶修正通常很小，对于许多应用而言这已经完全足够。[[939]](../bib_references/bib.md#bib982)

表 [11.2](#table:solvent_model_derivatives) 还汇总了隐式溶剂模型解析能量梯度的可用性。（对于无法提供所需解析导数的计算，会自动请求有限差分梯度和 Hessian。）

**注意：

从 **Q-Chem** v. 4.2.1 开始，隐式溶剂模型的指定方式发生了重大
变化。做出这一改动是为了简化和统一大量不同模型的输入表示法。
**

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt" rowspan="3"><span class="ltx_text ltx_font_bold">能量导数</span></th>
<td class="ltx_td ltx_align_center ltx_border_tt" colspan="9"><span class="ltx_text ltx_font_bold">溶剂模型</span></td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">C-PCM</td>
<td class="ltx_td ltx_align_center ltx_border_t">SS(V)PE/</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">CMIRS</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">COSMO</td>
<td class="ltx_td ltx_align_center ltx_border_t" colspan="3">SM$x$
</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">PEqS</td>
<td class="ltx_td ltx_align_center ltx_border_t">Langevin</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">IEF-PCM</td>
<td class="ltx_td ltx_align_center ltx_border_t">SM8</td>
<td class="ltx_td ltx_align_center ltx_border_t">SM12</td>
<td class="ltx_td ltx_align_center ltx_border_t">SMD</td>
<td class="ltx_td ltx_align_center">偶极子</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">SCF 能量梯度</th>
<td class="ltx_td ltx_align_center ltx_border_t">是${}^{a}$
</td>
<td class="ltx_td ltx_align_center ltx_border_t">是${}^{a}$
</td>
<td class="ltx_td ltx_align_center ltx_border_t">否</td>
<td class="ltx_td ltx_align_center ltx_border_t">是</td>
<td class="ltx_td ltx_align_center ltx_border_t">是</td>
<td class="ltx_td ltx_align_center ltx_border_t">否</td>
<td class="ltx_td ltx_align_center ltx_border_t">是</td>
<td class="ltx_td ltx_align_center ltx_border_t">否</td>
<td class="ltx_td ltx_align_center ltx_border_t">是</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">SCF 能量 Hessian</th>
<td class="ltx_td ltx_align_center">是${}^{a}$
</td>
<td class="ltx_td ltx_align_center">否</td>
<td class="ltx_td ltx_align_center">否</td>
<td class="ltx_td ltx_align_center">是${}^{b}$
</td>
<td class="ltx_td ltx_align_center">否</td>
<td class="ltx_td ltx_align_center">否</td>
<td class="ltx_td ltx_align_center">是${}^{c}$
</td>
<td class="ltx_td ltx_align_center">否</td>
<td class="ltx_td ltx_align_center">否</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">CIS/TDDFT 能量梯度</th>
<td class="ltx_td ltx_align_center">是${}^{a}$
</td>
<td class="ltx_td ltx_align_center">否</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center" colspan="3">— 不支持 —</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">CIS/TDDFT 能量 Hessian</th>
<td class="ltx_td ltx_align_center">是${}^{a}$
</td>
<td class="ltx_td ltx_align_center">否</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center" colspan="3">— 不支持 —</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">MP2 与双杂化${}^{d}$
</th>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center" colspan="3">— 不支持 —</td>
<td class="ltx_td ltx_align_center">—</td>
<td class="ltx_td ltx_align_center">—</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb">耦合簇方法${}^{d}$
</th>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
<td class="ltx_td ltx_align_center ltx_border_bb" colspan="3">— 不支持 —</td>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
<td class="ltx_td ltx_align_center ltx_border_bb">—</td>
</tr>
</tbody>
</table>

- •

${}^{a}$仅对 vdW 空腔和 SAS 空腔表面提供梯度。
- •

${}^{b}$带外围电荷校正的 COSMO 不支持 Hessian。
- •

${}^{c}$半数值 Hessian，步长可通过 FDIFF_STEPSIZE 控制。
- •

${}^{d}$不支持梯度，但可以使用溶剂极化的 MO 进行单点计算。

表 11.2: 
隐式溶剂模型下解析能量梯度与 Hessian 功能的汇总。

SOLVENT_METHOD

### `SOLVENT_METHOD`

> **设置所选用的溶剂方法。**
>
> * **类型**: `STRING`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 不使用溶剂化模型。
>     * KIRKWOOD
>     * 使用 Kirkwood-Onsager 模型（第
>     * 11.2.2
>     * 节）。
>     * PCM
>     * 使用表观面电荷可极化连续介质模型（第
>     * 11.2.3
>     * 节）。
>     * ISOSVP
>     * 使用 SS(V)PE 模型的等密度实现方式（第
>     * 11.2.6
>     * 节）。
>     * COSMO
>     * 使用 COSMO（第
>     * 11.2.8
>     * 节）。
>     * SM8
>     * 使用 Cramer-Truhlar SM
>     * $x$
>     * 模型的第 8 版（第
>     * 11.2.9.1
>     * 节）。
>     * SM12
>     * 使用 SM
>     * $x$
>     * 模型的第 12 版（第
>     * 11.2.9.2
>     * 节）。
>     * SMD
>     * 使用 SMD（第
>     * 11.2.9.3
>     * 节）。
>     * CHEM_SOL
>     * 使用 Langevin 偶极子模型（第
>     * 11.2.10
>     * 节）。
>     * PEQS
>     * 使用泊松方程求解器（Poisson Equation Solver）（第
>     * 11.2.11
>     * 节）。
> * **建议**: 参阅文献（*例如*，参考文献 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021), 11, pp. e1519. Link）。PCM 是一族模型的统称，在这种情况下可能需要额外的输入选项才能完整指定该模型；见第 11.2.3 节。SM12 也有若干版本可用，详见第 11.2.9.2 节。

在详细介绍各个模型之前，就命名法而言，有几个容易引起混淆之处值得一提。首先，“PCM”一词被频繁（有时含混地）用于指代包括 COSMO、C-PCM、SS(V)PE 和 IEF-PCM 在内的一族模型。后两种模型在积分方程层面是形式等价的，[[188]](../bib_references/bib.md#bib183)
 但在数值实现上存在一些
差异。[[756]](../bib_references/bib.md#bib789)

可以在 *$pcm* 输入段中通过额外的作业控制变量选择这两种模型之一，如第 [11.2.3](topic_pcm-em.md) 节所述。COSMO 与 C-PCM 非常相似，但包含了对溶质电子密度穿透空腔之外部分（所谓“外围电荷（outlying charge）”）的校正，[[692]](../bib_references/bib.md#bib721)
尽管后来的工作对该校正以及其他 *ad hoc*
电荷重归一化 procedures 的理论依据提出了质疑。[[244]](../bib_references/bib.md#bib244)

[IEF-PCM 和 SS(V)PE 方法本身已经包含了对
外围电荷的*隐式*校正，作为这些模型近似而导出的 C-PCM 方法同样如此，[[244]](../bib_references/bib.md#bib244)
尽管这一点在 COSMO 被提出时并未被认识到。
关于这些发展的历史讨论，参见文献 [[569]](../bib_references/bib.md#bib580)。]
无论如何，COSMO 在第 [11.2.8](subsec_COSMO-Klamt.md) 节中介绍。

SS(V)PE 模型也有两种实现方式可用。PCM
实现方式（通过在 *$pcm* 输入段中配合相应的作业控制变量设置 SOLVENT_METHOD = PCM
来请求）使用由原子中心球构造的溶质空腔，与其他 PCM 保持一致。
另一方面，设置 SOLVENT_METHOD =
ISOSVP 则请求一种 SS(V)PE 计算，其中溶质空腔由溶质自身电子密度的等值线（isocontour）定义。[[242]](../bib_references/bib.md#bib247)

这是一种颇具吸引力的单参数空腔构造方式，避免了由原子中心球构造的“van der Waals”空腔表面上的尖点所带来的诸多问题，而 SS(V)PE 的等密度实现方式构成了一种名为 CMIRS 的物理连续介质溶剂化模型的基础，详见第 [11.2.7](example_CMIRS-water.md) 节。[[1108]](../bib_references/bib.md#bib1155)

尽管使用的拟合参数少得多，CMIRS 在（溶剂化自由能的）准确性上可与最先进的 SM$x$ 溶剂化模型
相媲美。[[569]](../bib_references/bib.md#bib580)

然而，等密度空腔构造没有解析能量梯度，因此 CMIRS 也没有解析梯度；而当空腔表面由原子中心球构造时，这些梯度是可用的。

关于这些模型在溶剂化自由能（$\Delta G_{298}$）方面的准确性，
与大规模实验值数据库的比较表明，SM$x$ 模型对中性分子通常能达到亚 kcal/mol 级别的精度，而离子的平均误差则在 4 kcal/mol 左右。[[281]](../bib_references/bib.md#bib286)

（注意，从统计意义上讲，SM12 和 SMD 模型总体上并没有比 SM8 改进太多，[[909]](../bib_references/bib.md#bib943)
 但确实将这些模型扩展到了任意基组，而
SM8 仅限于少数几个小基组。此外，SMD 同时包含梯度和频率。

）
若要在 PCM 类溶剂模型中达到与 SM$x$ 模型相当的精度，必须添加非静电项。[[569]](../bib_references/bib.md#bib580)

在上述各种 PCM 中，唯一构成溶剂化能“黑箱（black box）”模型的是 CMIRS，它在统计意义上略优于 SM$x$ 模型，[[1527]](../bib_references/bib.md#bib1594)
尽管它仅适用于少数几种溶剂。

以下各节将就 **Q-Chem** 中可用的各种隐式溶剂模型的理论细节与作业控制给出更多说明。
参考文献 [[569]](../bib_references/bib.md#bib580)
 既包含这些模型之间的形式比较，也包含溶剂化自由能准确性的并列对比。
