---
title: "11.2.1 引言"
---

## 11.2.1 引言

（2026 年 7 月 4 日）

*从头算*（*ab initio*）量子化学使得从第一性原理出发研究气相分子性质成为可能。然而，在溶液中，这些性质可能发生显著变化，在极性溶剂中尤其如此。虽然可以通过在量子化学计算中显式加入溶剂分子来模拟溶剂化效应（*例如*，超分子团簇计算，并对第一溶剂化层中分子的不同构型取平均），但此类计算对算力的要求非常高。此外，团簇计算通常无法给出准确的溶剂化能，这是由于长程静电相互作用十分重要。（包含*部分*显式溶剂的离散/连续介质混合模型则可以相当有效。[[1101]](../bib_references/bib.md#bib1147)）
准确预测溶剂化自由能不仅对模拟化学反应至关重要，对获得溶液中的相对构象能也是如此。

**Q-Chem** 包含多种不同的隐式溶剂模型，它们的复杂程度差异很大。这些模型通常被称为自洽反应场（Self-Consistent Reaction Field, SCRF）模型，因为连续介质溶剂会建立一个依赖于溶质电子密度的“反应场”（溶质哈密顿量中的附加项），因此在波函数迭代收敛的过程中必须对其进行自洽更新。**Q-Chem** 中最简单、历史最悠久的一类模型是多极展开方法（也称为 Kirkwood-Onsager 模型），[[569]](../bib_references/bib.md#bib580)

其做法是将溶质分子置于球形空腔内，并用单中心多极展开来表示其静电势。（这不应与使用偶极近似的 *Onsager 模型* 相混淆；为避免混淆，*多极展开方法*是更好的术语。）更复杂的模型采用分子形状的空腔和完整的分子静电势，包括
导体状 PCM（C-PCM）、[[79]](../bib_references/bib.md#bib61)

导体状屏蔽模型（COSMO）、

“用于静电学的表面与体积极化模拟” [SS(V)PE] 模型，[[245]](../bib_references/bib.md#bib245)
以及与之紧密相关的“积分方程形式”（IEF-PCM）。[[187]](../bib_references/bib.md#bib181)

关于这些方法及其相互联系的综述，可参见 Herbert 的综述文章。[[569]](../bib_references/bib.md#bib580)

C-PCM、IEF-PCM 和 SS(V)PE 都属于所谓的“表观表面电荷”SCRF 模型，而由 Tomasi 及其同事推广的术语*极化连续介质模型*（Polarizable Continuum Models, PCMs）[[1363]](../bib_references/bib.md#bib1425)
如今已几乎普遍用于指代这类溶剂化模型。**Q-Chem** 采用这些 PCM 的 Switching/Gaussian（“SwiG”）实现方式，[[753]](../bib_references/bib.md#bib786)
从而解决了标准 PCM 中一个长期存在（却鲜为人知）的问题，即用于离散化溶质/连续介质界面的边界元方法可能导致溶质分子势能面上的不连续性。这些不连续性会阻碍几何优化收敛，在振动频率计算中引入严重的假象，并使得*从头算*分子动力学计算几乎无法进行。[[753]](../bib_references/bib.md#bib786)

相比之下，**Q-Chem** 的 SwiG-PCM 给出的势能面是严格连续且光滑的。与早期获得光滑 PCM 的尝试不同，SwiG 方法在很大程度上保留了底层积分方程溶剂模型的性质，因此溶剂化能和分子表面积几乎不受平滑处理的影响。

**Q-Chem** 中提供的其他溶剂模型还包括“朗之万偶极子”（Langevin dipoles）模型；[[394]](../bib_references/bib.md#bib402)
以及
SM8、[[912]](../bib_references/bib.md#bib942)
SM12、[[910]](../bib_references/bib.md#bib946)
和 SMD 模型。[[909]](../bib_references/bib.md#bib943)

SM8 和 SM12 基于广义 Born 静电方法，并辅以用于描述非静电效应（空腔化作用、色散作用、交换排斥以及溶剂结构变化）的原子表面张力。这些模型经过了细致的参数化，能够重现实验溶剂化自由能。[[281]](../bib_references/bib.md#bib286)

SMD 模型（其中“D”代表“density”，即密度）将 IEF-PCM 与类似的非静电校正相结合。从统计意义上讲，SMD 并不比其他 SM$x$ 模型更准确或更不准确，[[569]](../bib_references/bib.md#bib580)
但其优点是基于由溶质精确的 SCF 密度导出的严格静电学。SM12 和 SMD 模型都可在任意基组下使用。SM8 模型使用基于“CM4”电荷的广义 Born 静电方法，[[678]](../bib_references/bib.md#bib702)

CM4 电荷本身基于 Löwdin 原子电荷，因此该模型应仅在其经过参数化的基组中使用：6-31G*、6-31+G* 或 6-31+G**。（如果请求使用其他基组，将采用 6-31G* 的参数，但不推荐这样做。）SM12 模型同样使用广义 Born 静电方法，但用 Hirshfeld 电荷替代 CM4 电荷；后者对基组变化更为稳定，因此 SM12 可在任意基组下使用。其代价是：SM8 提供解析梯度而 SM12 不提供；另见表 11.2。对于 SMD，解析一阶导数和二阶导数（频率）均可使用。

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt"><span class="ltx_text ltx_font_bold">模型</span></th>
<td class="ltx_td ltx_align_center ltx_border_tt" colspan="2"><span class="ltx_text ltx_font_bold">空腔</span></td>
<td class="ltx_td ltx_align_center ltx_border_tt"><span class="ltx_text ltx_font_bold">非静电项</span></td>
<td class="ltx_td ltx_align_center ltx_border_tt"><span class="ltx_text ltx_font_bold">支持基组</span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_row"></th>
<td class="ltx_td ltx_align_center ltx_border_t">构建方式</td>
<td class="ltx_td ltx_align_center ltx_border_t">离散化方式</td>
<td class="ltx_td ltx_align_center"><span class="ltx_text ltx_font_bold">是否包含？</span></td>
<td class="ltx_td ltx_align_center"><span class="ltx_text ltx_font_bold"></span></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_row"></th>
<td class="ltx_td"></td>
<td class="ltx_td"></td>
<td class="ltx_td ltx_align_center"></td>
<td class="ltx_td ltx_align_center"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">Kirkwood-Onsager</th>
<td class="ltx_td ltx_align_center ltx_border_t">球面</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷</td>
<td class="ltx_td ltx_align_center ltx_border_t">否</td>
<td class="ltx_td ltx_align_center ltx_border_t">全部</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">朗之万偶极子</th>
<td class="ltx_td ltx_align_center ltx_border_t">原子球</td>
<td class="ltx_td ltx_align_center ltx_border_t">三维空间中的</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">否</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">（用户可定义）</td>
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
<td class="ltx_td ltx_align_center">（用户可定义）</td>
<td class="ltx_td ltx_align_center">网格</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">C-PCM</th>
<td class="ltx_td ltx_align_center ltx_border_t">原子球</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷或</td>
<td class="ltx_td ltx_align_center ltx_border_t">用户指定</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">（用户可定义）</td>
<td class="ltx_td ltx_align_center">光滑高斯函数</td>
<td class="ltx_td ltx_align_center"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">SS(V)PE/</th>
<td class="ltx_td ltx_align_center ltx_border_t">原子球</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷或</td>
<td class="ltx_td ltx_align_center ltx_border_t">用户指定</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">IEF-PCM</th>
<td class="ltx_td ltx_align_center">（用户可定义）</td>
<td class="ltx_td ltx_align_center">光滑高斯函数</td>
<td class="ltx_td ltx_align_center"></td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="2">COSMO</th>
<td class="ltx_td ltx_align_center ltx_border_t">预定义</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">点电荷</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">无</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">原子球</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">等密度面 SS(V)PE</th>
<td class="ltx_td ltx_align_center ltx_border_t">等密度面轮廓</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷</td>
<td class="ltx_td ltx_align_center ltx_border_t">无</td>
<td class="ltx_td ltx_align_center ltx_border_t">全部</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t">CMIRS</th>
<td class="ltx_td ltx_align_center ltx_border_t">等密度面轮廓</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷</td>
<td class="ltx_td ltx_align_center ltx_border_t">自动</td>
<td class="ltx_td ltx_align_center ltx_border_t">全部</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t" rowspan="3">SM8</th>
<td class="ltx_td ltx_align_center ltx_border_t">预定义</td>
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
<td class="ltx_td ltx_align_center ltx_border_t">预定义</td>
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
<td class="ltx_td ltx_align_center ltx_border_t">预定义</td>
<td class="ltx_td ltx_align_center ltx_border_t">点电荷</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">自动</td>
<td class="ltx_td ltx_align_center ltx_border_t" rowspan="2">全部</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_center">原子球</td>
<td class="ltx_td ltx_align_center"></td>
</tr>
</tbody>
<tfoot class="ltx_tfoot">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_tt" colspan="5">
${}^{a}$<span class="ltx_text" style="font-size:80%;">广义 Born 静电模型；无需空腔构建。</span>
</th>
</tr>
</tfoot>
</table>

表 11.1：
**Q-Chem** 中可用的隐式溶剂模型汇总，说明了溶质空腔的构建与离散化方式、是否（或能否）包含非静电项，以及每种模型可用的基组。

表 11.1 汇总了 **Q-Chem** 中可用的隐式溶剂模型。溶剂模型通过 SOLVENT_METHOD 关键字调用，如下所示。有关每种具体溶剂模型的更多细节，请参见后续章节。一般而言，这些方法适用于任意 SCF 层级的电子结构理论，但 SM8 存在 aforementioned 中提到的关于基组的限制。后 Hartree–Fock 计算（例如 MP2 或 EOM-CC）可以先运行 SCF + PCM 计算后再进行，此时 correlated 波函数将使用被溶剂极化的 MO 和 Hartree-Fock 能级。这是在相关能理论水平上对溶剂效应的“零阶”处理，但由于高阶校正通常很小，这种处理对许多应用而言是完全足够的。[[939]](../bib_references/bib.md#bib982)

表 11.2 还汇总了各隐式溶剂模型解析能量梯度的可用性。（对于解析导数不可用的计算，将自动采用有限差分方法求取梯度和 Hessian。）

**注意：

自 **Q-Chem** v. 4.2.1 起，隐式溶剂模型的指定格式发生了显著变化。做出这一更改的目的在于简化和统一大量不同模型的输入记法。
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
<td class="ltx_td ltx_align_center ltx_border_t">朗之万</td>
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
<th class="ltx_td ltx_align_left ltx_th ltx_th_row">MP2 &amp; 双杂化${}^{d}$
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

${}^{a}$梯度仅支持 vdW 空腔和 SAS 空腔表面。
- •

${}^{b}$COSMO 带外点电荷校正（outlying charge correction）的 Hessian 不受支持。
- •

${}^{c}$半数值 Hessian，步长可通过 FDIFF_STEPSIZE 控制。
- •

${}^{d}$不支持梯度，但可使用经溶剂极化的 MO 进行单点能计算。

表 11.2：
隐式溶剂模型解析能量梯度和 Hessian 能力的汇总。

### `SOLVENT_METHOD`

> **设定所使用的溶剂化方法。**
>
> * **类型**: `STRING`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 不使用溶剂化模型。
>     * `KIRKWOOD`: 使用 Kirkwood-Onsager 模型（第 11.2.2 节）。
>     * `PCM`: 使用表观表面电荷可极化连续介质模型（Polarizable Continuum Model）（第 11.2.3 节）。
>     * `ISOSVP`: 使用 SS(V)PE 模型的等密度实现（第 11.2.6 节）。
>     * `COSMO`: 使用 COSMO（第 11.2.8 节）。
>     * `SM8`: 使用 Cramer-Truhlar SM $x$ 模型的第 8 版（第 11.2.9.1 节）。
>     * `SM12`: 使用 SM $x$ 模型的第 12 版（第 11.2.9.2 节）。
>     * `SMD`: 使用 SMD（第 11.2.9.3 节）。
>     * `CHEM_SOL`: 使用 Langevin 偶极子模型（第 11.2.10 节）。
>     * `PEQS`: 使用泊松方程求解器（Poisson Equation Solver）（第 11.2.11 节）。
> * **建议**: 请查阅相关文献（例如，文献 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021), 11, pp. e1519. Link）。PCM 是一个模型家族的统称，在这种情况下可能需要额外的输入选项才能完整地指定模型；参见第 11.2.3 节。此外，SM12 也有多个可用版本，详见第 11.2.9.2 节的讨论。

在详细讨论这些模型之前，先就命名法方面几个容易引起混淆的问题作一些说明。首先，“PCM”一词常被（有时是不太严格地）用来指代一个模型家族，其中包括 COSMO、C-PCM、SS(V)PE 和 IEF-PCM。后两种模型在积分方程层面是形式上等价的，[[188]](../bib_references/bib.md#bib183) 但在数值实现上存在一些差异。[[756]](../bib_references/bib.md#bib789)

可以通过在 *$pcm* 输入段中设置额外的作业控制变量来选择上述模型之一，详见第 [11.2.3](topic_pcm-em.md) 节。COSMO 与 C-PCM 非常相似，但它对溶质电子密度穿透到空腔之外的部分（即所谓的“外溢电荷”，outlying charge）加入了修正，[[692]](../bib_references/bib.md#bib721)

不过后来的研究对这一修正以及其他 *ad hoc*（ 特设的）电荷重整化程序的理论依据提出了质疑。[[244]](../bib_references/bib.md#bib244)

[IEF-PCM 和 SS(V)PE 方法本身已经包含对外溢电荷的 *隐式* 修正，作为这两种模型近似而导出的 C-PCM 方法也是如此，[[244]](../bib_references/bib.md#bib244)

尽管在 COSMO 最初提出时尚未认识到这一点。关于这些发展的历史讨论，可参见文献 [[569]](../bib_references/bib.md#bib580) 。]
无论如何，COSMO 在第 [11.2.8](subsec_COSMO-Klamt.md) 节中有专门描述。

SS(V)PE 模型有两种实现方式。PCM 实现（通过设置 SOLVENT_METHOD = PCM 并配合 *$pcm* 输入段中相应的作业控制变量来调用）与其他 PCM 一样，使用由原子中心球面构造的溶质空腔。另一方面，设置 SOLVENT_METHOD = ISOSVP 则进行这样一种 SS(V)PE 计算：溶质空腔由溶质自身电子密度的等值面定义。[[242]](../bib_references/bib.md#bib247)

这是一种颇具吸引力的单参数空腔构造方法，可以避免由原子中心球面构造的“范德华”空腔表面中出现的许多尖点（cusp）问题，而且 SS(V)PE 的等密度实现构成了一种基于物理的连续介质溶剂化模型的基础，该模型称为 CMIRS，将在第 [11.2.7](example_CMIRS-water.md) 节中介绍。[[1108]](../bib_references/bib.md#bib1155)

在溶剂化自由能方面，CMIRS 的精度（在统计意义上）足以与现有最优的 SM$x$ 溶剂化模型相媲美，[[569]](../bib_references/bib.md#bib580)

尽管它使用的拟合参数要少得多。然而，等密度空腔构造无法提供解析能量梯度，因此 CMIRS 也不提供解析梯度；而当空腔表面由原子中心球面构造时，解析梯度则是可用的。

关于这些模型在溶剂化自由能（$\Delta G_{298}$）方面的精度，SM$x$ 模型对于中性分子通常可达到亚千卡/摩尔（sub-kcal/mol）的精度（这是通过与大型实验值数据库的比较得出的），但对于离子的平均误差更接近 4 kcal/mol。[[281]](../bib_references/bib.md#bib286)

（请注意，SM12 和 SMD 模型在任何统计意义上通常都不会比 SM8 有太大改进，[[909]](../bib_references/bib.md#bib943) 但它们将这些模型扩展到了任意基组，而 SM8 则仅限于少数几个小基组。此外，SMD 同时提供解析梯度和振动频率。

）
要在 PCM 类溶剂模型中达到与 SM$x$ 模型相当的精度，必须加入非静电项。[[569]](../bib_references/bib.md#bib580)

在上述各种 PCM 中，唯一构成溶剂化能量“黑箱”模型的是 CMIRS，它在统计意义上略微优于 SM$x$ 模型，[[1527]](../bib_references/bib.md#bib1594) 尽管它仅适用于少数几种溶剂。

以下各节将提供更多关于 **Q-Chem** 中可用的各种隐式溶剂模型的理论和作业控制方面的详细信息。文献 [[569]](../bib_references/bib.md#bib580) 既包含这些模型之间的形式化比较，也包含溶剂化自由能精度的并列对比。
