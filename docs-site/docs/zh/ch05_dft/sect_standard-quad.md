---
title: "5.5.3 标准求积网格"
---

## 5.5.3 标准求积网格

（2026 年 7 月 4 日）

**Q-Chem** 中提供了四种不同的“标准网格”（standard grids），记为 SG-$n$，其中 $n=0,1,2$ 或 3；这些网格的质量与计算开销都随 $n$ 的增大而提高。构造这些网格时，首先从一个“母”网格（parent grid，$(N_{r},~{}N_{\Omega}$）出发，它由 $N_{r}$ 个径向球面以及每个球面上的 $N_{\Omega}$ 个角向（Lebedev）网格点组成；然后系统地“剪枝”（pruning）那些不需要精细角向求积区域的角向点数，例如靠近原子核的区域（此处电荷密度几乎呈球对称）以及远离原子核的远区（此处电荷密度变化缓慢）。在角向精度至关重要的价层区域则保留大量的网格点。SG-$n$ 网格汇总于表 [5.3](#table:SG)。尽管许多电子结构程序都会采用某种流程来删除不必要的网格点以提升计算效率，但 **Q-Chem** 的 SG-$n$ 网格有一个显著特点：其完整的网格定义均可在同行评审文献[[448]](../bib_references/bib.md#bib460)
 中查到，从而便于在其他电子结构程序中复现 **Q-Chem** 的密度泛函理论（Density Functional Theory, DFT）计算结果。正如计算能量会随基组（Basis Set）的选择而发生相当显著的变化，在 DFT 中计算能量同样会随求积网格的选择而大幅变化。在发表论文时，用户应当始终说明所使用的网格，并建议引用表 [5.3](#table:SG) 中相应的文献。

<table class="ltx_tabular ltx_centering ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_tt">剪枝后的</td>
<td class="ltx_td ltx_align_center ltx_border_tt">文献</td>
<td class="ltx_td ltx_align_center ltx_border_tt">母网格</td>
<td class="ltx_td ltx_align_center ltx_border_tt">网格点数</td>
<td class="ltx_td ltx_align_left ltx_border_tt">作为默认网格适用于</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">网格</td>
<td class="ltx_td"></td>
<td class="ltx_td ltx_align_center">($N_{r},N_{\Omega}$)</td>
<td class="ltx_td ltx_align_center">（C 原子）${}^{a}$
</td>
<td class="ltx_td ltx_align_left">哪些泛函？${}^{b}$
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_t">SG-0</td>
<td class="ltx_td ltx_align_center ltx_border_t">[[241]](../bib_references/bib.md#bib242)
</td>
<td class="ltx_td ltx_align_center ltx_border_t">(23, 170)</td>
<td class="ltx_td ltx_align_right ltx_border_t">1,390 (36%)</td>
<td class="ltx_td ltx_align_left ltx_border_t">无</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">SG-1</td>
<td class="ltx_td ltx_align_center">[[448]](../bib_references/bib.md#bib460)
</td>
<td class="ltx_td ltx_align_center">(50, 194)</td>
<td class="ltx_td ltx_align_right">3,816 (39%)</td>
<td class="ltx_td ltx_align_left">LDA、大多数 GGA 及杂化泛函</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">SG-2</td>
<td class="ltx_td ltx_align_center">[[301]](../bib_references/bib.md#bib305)
</td>
<td class="ltx_td ltx_align_center">(75, 302)</td>
<td class="ltx_td ltx_align_right">7,790 (34%)</td>
<td class="ltx_td ltx_align_left">Meta-GGA；基于 B95 与 B97 的泛函</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">SG-3</td>
<td class="ltx_td ltx_align_center">[[301]](../bib_references/bib.md#bib305)
</td>
<td class="ltx_td ltx_align_center">(99, 590)</td>
<td class="ltx_td ltx_align_right">17,674 (30%)</td>
<td class="ltx_td ltx_align_left">明尼苏达（Minnesota）系列泛函</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_tt" colspan="5">
${}^{a}$括号中的数字表示相对母网格所保留的网格点比例</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" colspan="5">
${}^{b}$反映 v. 4.4.2 及之后版本的 <span class="ltx_text ltx_font_smallcaps">Q-Chem</span></td>
</tr>
</tbody>
</table>

表 5.3：
**Q-Chem** 中可用的标准求积网格，同时给出碳原子的网格点数，以显示剪枝所带来的网格点数量减少。

SG-0 与 SG-1 网格专为使用广义梯度近似（Generalized Gradient Approximation, GGA）泛函的大分子计算而设计。对于中等大小的分子和 GGA 泛函，SG-1 带来的积分误差约为 $\sim$0.2 kcal/mol，即使在具有挑战性的测试案例（例如异构化反应的焓）中也是如此。（总能量的积分误差不超过几个 $\mu$hartree，即 $\sim$0.01 kcal/mol。）SG-0 网格以类似方式导出，相对于 SG-1，其原子化能量（atomization energy）的均方根误差为 72 $\mu$hartree，而相对能量则能被很好地复现。[[241]](../bib_references/bib.md#bib242)
 无论使用哪一个网格，这种量级的误差通常都明显小于 GGA 能量本身的固有误差，因此是可以接受的。如表 [5.3](#table:SG) 所示，SG-1 仅保留了其母网格不到 $40$% 的网格点，这直接转化为计算成本的节省。

SG-0 和 SG-1 在优化时都使能量的积分误差低于设定的阈值，但能量对核坐标的导数（包括（超）极化率[[216]](../bib_references/bib.md#bib212)
 等性质）往往对求积网格的质量更为敏感。例如，当出现虚频时需要格外小心，因为若网格过于稀疏，低频（但为实数）的振动频率可能表现为虚频。如果发现虚频，或者对 **Q-Chem** 给出的频率存有疑虑，推荐的流程是使用更高质量的网格重新进行几何优化和振动频率计算。（若将此前已优化的几何结构作为初始猜测，优化应该会很快收敛。）

对于 **Q-Chem** 3.2–4.4 版本，SG-1 是所有密度泛函默认的 DFT 积分网格。但自 **Q-Chem** v. 4.4.2 起，默认网格改为依泛函而定，如表 [5.3](#table:SG) 所总结。这一变化反映出如下事实：尽管 SG-1 对于使用大多数 GGA 和杂化泛函的能量计算已经足够（但对于某些其他性质则需谨慎，如下文所述），它*并不*足以精确积分 2005 年前后（$\sim$2005）之后开发的许多泛函。这些泛函包括 meta-GGA，由于其依赖于动能密度（式 ([5.10](Ch5.S3.SS1.md#eq:tau)) 中的 $\tau_{\sigma}$)和/或密度的拉普拉斯算符（$\nabla^{2}\rho_{\sigma}$），因而更为复杂。基于 B97 的泛函以及明尼苏达系列泛函[[1569]](../bib_references/bib.md#bib1628)
 中描述交换非均匀性因子（exchange inhomogeneity factor）的表达式相对复杂，因此同样对积分网格的质量更加敏感。[[1455]](../bib_references/bib.md#bib1517)
 为了积分这些现代密度泛函，人们发展了 SG-2 与 SG-3 网格，[[301]](../bib_references/bib.md#bib305)
 它们分别是中等质量 (75, 302) 网格与高质量 (99, 590) 积分网格的剪枝版本。对若干已知对积分网格质量高度敏感的性质（如振动频率、超极化率以及非键相互作用的势能曲线）的测试表明，SG-2 对于 meta-GGA 和基于 B97 的泛函通常已经足够，在很多情形下相对于未剪枝的 (250, 974) 网格实质上已经收敛。[[301]](../bib_references/bib.md#bib305)
 明尼苏达泛函对网格更为敏感，虽然 SG-3 通常够用，但在非键相互作用的情况下尚未完全收敛。[[301]](../bib_references/bib.md#bib305)

**注意：**

1.

SG-0 在 **Q-Chem** v. 3.0 中经过重新优化，因此与更早版本的程序相比，结果可能略有差异。

2.

SG-2 和 SG-3 网格采用双指数（double-exponential）径向求积方法，[[301]](../bib_references/bib.md#bib305)
 而一般网格（通过将 XC_GRID 设置为 $XY$ 来选择，如第 [5.4](sect_DFT_METHOD.md) 节所述）采用 Euler-MacLaurin 径向求积方法。因此，*绝对*能量无法在 SG-2 与 XC_GRID = 000075000302 之间进行比较，即使 SG-2 使用的是剪枝后的 (75, 302) 网格。不过，两者之间的能量*差值*应当相当接近。

3.

如文献 [[301]](../bib_references/bib.md#bib305)
 所述，对于明尼苏达泛函，即使使用 SG-3 网格，势能面上仍可能残留一些波动（wiggles），尤其是长程的非键相互作用。虽然这对能量差而言很少造成问题，但如果用户希望消除这些振荡，我们建议使用未剪枝的 (99, 590) 网格，*i.e.*，XC_GRID = 000099000590。

4.

尽管文献中对 SCAN 泛函[[83]](../bib_references/bib.md#bib68)
 的网格敏感性已有大量讨论，

但“SCAN 对网格质量极其敏感”这一普遍认知主要基于凝聚态（周期性 DFT）程序中的计算。在 **Q-Chem** 中，SG-2 和 SG-3 网格对于 SCAN 计算而言质量已经足够。[[161]](../bib_references/bib.md#bib154)

（即便如此，正则化泛函，例如 r${}^{\text{2}}$SCAN[[419]](../bib_references/bib.md#bib428)
 确实能够降低对网格的依赖。）

**
