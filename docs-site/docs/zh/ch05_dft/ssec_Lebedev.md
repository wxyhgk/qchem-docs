---
title: "5.5.2 角向网格"
---

## 5.5.2 角向网格

(July 4, 2026)

对于球极坐标（spherical-polar coordinate）的径向分量 $r$ 取固定值的情形，函数
$f(\mathbf{r})\equiv f(r,\theta,\phi)$ 可以按球谐函数（spherical harmonic function）精确展开，

<a id="Ch5.E16"></a>
$$
f(r,\theta,\phi)=\sum_{\ell=0}^{\infty}\sum_{m=-\ell}^{\ell}c_{\ell m}\mbox{Y}_{\ell m}(\theta,\phi)\;. \tag{5.16}
$$

角向求积网格（angular quadrature grid）用于在 $r$ 固定的情况下对 $f(r,\theta,\phi)$ 进行积分，通常以两个指标来刻画：其一是“阶”（degree），即求积能够精确积分的 $\ell$ 的最大值；其二是“效率”（efficiency），即公式中每个自由度所能精确积分的球谐函数数目。**Q-Chem** 支持以下两类角向网格。

- •

**Lebedev 网格（Lebedev grids）。**
这类网格是专门为球面求积构造的网格，[[776]](../bib_references/bib.md#bib808)
基于八面体点群（octahedral point group）构造。**Q-Chem** 中可用的 Lebedev 网格列于表
[5.2](#table:Lebedev)。这类网格的效率通常接近 1，在某些情况下甚至超过 1。通过
*$rem* 关键字 XC_GRID 指定网格点数（取自表 [5.2](#table:Lebedev)）即可选择某个 Lebedev 网格，详见下文讨论。

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_th_row ltx_border_tt" rowspan="2">点数</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_r ltx_border_tt">阶</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_th_row ltx_border_tt" rowspan="2">点数</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_r ltx_border_tt">阶</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_th_row ltx_border_tt" rowspan="2">点数</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">阶</th>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_r">(${\ell}_{\mathrm{max}}$)</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_r">(${\ell}_{\mathrm{max}}$)</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column">(${\ell}_{\mathrm{max}}$)</th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_t">6</th>
<td class="ltx_td ltx_align_center ltx_border_r ltx_border_t">3</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_t">230</th>
<td class="ltx_td ltx_align_center ltx_border_r ltx_border_t">25</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_t">1730</th>
<td class="ltx_td ltx_align_center ltx_border_t">71</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">18</th>
<td class="ltx_td ltx_align_center ltx_border_r">5</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">266</th>
<td class="ltx_td ltx_align_center ltx_border_r">27</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">2030</th>
<td class="ltx_td ltx_align_center">77</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">26</th>
<td class="ltx_td ltx_align_center ltx_border_r">7</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">302</th>
<td class="ltx_td ltx_align_center ltx_border_r">29</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">2354</th>
<td class="ltx_td ltx_align_center">83</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">38</th>
<td class="ltx_td ltx_align_center ltx_border_r">9</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">350</th>
<td class="ltx_td ltx_align_center ltx_border_r">31</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">2702</th>
<td class="ltx_td ltx_align_center">89</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">50</th>
<td class="ltx_td ltx_align_center ltx_border_r">11</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">434</th>
<td class="ltx_td ltx_align_center ltx_border_r">35</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">3074</th>
<td class="ltx_td ltx_align_center">95</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">74</th>
<td class="ltx_td ltx_align_center ltx_border_r">13</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">590</th>
<td class="ltx_td ltx_align_center ltx_border_r">41</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">3470</th>
<td class="ltx_td ltx_align_center">101</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">86</th>
<td class="ltx_td ltx_align_center ltx_border_r">15</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">770</th>
<td class="ltx_td ltx_align_center ltx_border_r">47</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">3890</th>
<td class="ltx_td ltx_align_center">107</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">110</th>
<td class="ltx_td ltx_align_center ltx_border_r">17</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">974</th>
<td class="ltx_td ltx_align_center ltx_border_r">53</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">4334</th>
<td class="ltx_td ltx_align_center">113</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">146</th>
<td class="ltx_td ltx_align_center ltx_border_r">19</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">1202</th>
<td class="ltx_td ltx_align_center ltx_border_r">59</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">4802</th>
<td class="ltx_td ltx_align_center">119</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">170</th>
<td class="ltx_td ltx_align_center ltx_border_r">21</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">1454</th>
<td class="ltx_td ltx_align_center ltx_border_r">65</td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_row">5294</th>
<td class="ltx_td ltx_align_center">125</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_row ltx_border_bb">194</th>
<td class="ltx_td ltx_align_center ltx_border_bb ltx_border_r">23</td>
<th class="ltx_td ltx_th ltx_th_row ltx_border_bb"></th>
<td class="ltx_td ltx_border_bb ltx_border_r"></td>
<th class="ltx_td ltx_th ltx_th_row ltx_border_bb"></th>
<td class="ltx_td ltx_border_bb"></td>
</tr>
</tbody>
</table>

表 5.2： 
**Q-Chem** 中可用的 Lebedev 角向求积网格。
- •

**Gauss-Legendre 网格（Gauss-Legendre grids）。**
这类网格是在两个球极角 $\theta$ 和 $\phi$ 上构造的球面直积网格（spherical direct-product grid）。
对 $\theta$ 的积分采用由 Legendre 多项式导出的 Gauss 求积（Gaussian quadrature）来完成，
而对 $\phi$ 的积分则采用等间距分布的网格点。选择 Gauss-Legendre 网格时，需指定用于积分的总点数
$2N^{2}$，它对应于一个在 $\phi$ 方向有 $2N_{\phi}$ 个点、在 $\theta$ 方向有 $N_{\theta}$ 个点的网格，其阶为
$2N-1$。Gauss-Legendre 网格的效率仅为 2/3，因此在相同网格点数下其质量低于 Lebedev 网格；但其优点在于可以针对任意（乃至任意巨大）的网格点数来定义。如有需要，这为实现角向积分的任意精度提供了一种机制。

将上述径向方案与角向方案组合起来，会产生数量庞大、令人望而生畏的求积方案选择，因此对网格进行标准化是非常有用的。标准化的目的既是为了方便用户、便于与文献结果进行比较，也是为了让开发者能够在不同软件程序之间对比详细结果——因为总电子能量对网格的细节同样敏感，正如它对基组（basis set）的细节敏感一样。下面将讨论标准的求积网格。
