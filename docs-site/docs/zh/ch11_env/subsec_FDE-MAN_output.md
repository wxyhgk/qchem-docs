---
title: "11.7.7 FDE-Man 输出"
---

## 11.7.7 FDE-Man 输出

(July 4, 2026)

总体而言，FDE-Man 的输出会显示嵌入（embedding）计算的所有重要阶段，即：

1. 1.

$\rho_{A}^{\mathrm{ref}}(\mathbf{r})$ 的生成，
2. 2.

$\rho_{B}(\mathbf{r})$ 的生成，
3. 3.

嵌入势（embedding potential）的构造，
4. 4.

FDE-Man 嵌入计算的启动，以及
5. 5.

FDE-Man 最终总结。

下表汇总了输出中所打印各项术语的定义。这些量会对每一个态（state）*即* 每一个 $\rho_{A}^{I}(\mathbf{r})$ 分别打印。此外，相对于参考密度 $\rho_{A}^{\mathrm{ref}}(\mathbf{r})$ 的非静电相互作用会打印在 FDE-Man 总结的顶部。

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_th_row ltx_border_tt" colspan="2">子系统能量（Subsystem Energies）</th>
</tr>
</thead>
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t"><span class="ltx_text ltx_font_typewriter">Embedded system (A)</span></th>
<td class="ltx_td ltx_align_left ltx_border_t">$\langle\Psi_{A}^{I}|\hat{H}_{A}+v_{\mathrm{emb}}^{\mathrm{lin}}|\Psi_{A}^{I}\rangle$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row"><span class="ltx_text ltx_font_typewriter">Environment (B)</span></th>
<td class="ltx_td ltx_align_left">$E_{B}=E_{v_{B}}^{\mathrm{HK}}[\rho_{B}]\;\text{or}\;E_{\mathrm{HF}}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_th_row ltx_border_t" colspan="2">静电相互作用（Electrostatic Interactions）</th>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t"><span class="ltx_text ltx_font_typewriter">rho_A &lt;-&gt; rho_B</span></th>
<td class="ltx_td ltx_align_left ltx_border_t">$J_{\mathrm{int}}[\rho_{A},\rho_{B}]=\int\int\frac{\rho_{A}(\mathbf{r})\rho_{B}(\mathbf{r}^{\prime})}{|\mathbf{r}-\mathbf{r}^{\prime}|}\mathrm{d}\mathbf{r}\mathrm{d}\mathbf{r}^{\prime}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row"><span class="ltx_text ltx_font_typewriter">rho_A &lt;-&gt; Nuc_B</span></th>
<td class="ltx_td ltx_align_left">$V_{B}^{\mathrm{nuc}}[\rho_{A}]=\int\rho_{A}(\mathbf{r})v_{B}(\mathbf{r})\mathrm{d}\mathbf{r}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row"><span class="ltx_text ltx_font_typewriter">rho_B &lt;-&gt; Nuc_A</span></th>
<td class="ltx_td ltx_align_left">$V_{A}^{\mathrm{nuc}}[\rho_{B}]=\int\rho_{B}(\mathbf{r})v_{A}(\mathbf{r})\mathrm{d}\mathbf{r}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row"><span class="ltx_text ltx_font_typewriter">Nuc_A &lt;-&gt; Nuc_B</span></th>
<td class="ltx_td ltx_align_left">$V_{N_{A}N_{B}}=\sum_{i}\sum_{j}\frac{Z_{i}Z_{j}}{|R_{i}-R_{j}|}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_th_row ltx_border_t" colspan="2">非静电相互作用（Non-Electrostatic Interactions）</th>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t"><span class="ltx_text ltx_font_typewriter">non-additive E_xc</span></th>
<td class="ltx_td ltx_align_left ltx_border_t">$E_{xc}^{\mathrm{nad}}[\rho_{A}^{I},\rho_{B}]$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row"><span class="ltx_text ltx_font_typewriter">non-additive T_s</span></th>
<td class="ltx_td ltx_align_left">$T_{s}^{\mathrm{nad}}[\rho_{A}^{I},\rho_{B}]$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row"><span class="ltx_text ltx_font_typewriter">integrated v_xc nad</span></th>
<td class="ltx_td ltx_align_left">$\int\rho_{A}^{I}(\mathbf{r})v_{xc}^{\mathrm{nad}}(\mathbf{r})\mathrm{d}\mathbf{r}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row"><span class="ltx_text ltx_font_typewriter">integrated v_T nad</span></th>
<td class="ltx_td ltx_align_left">$\int\rho_{A}^{I}(\mathbf{r})v_{T}^{\mathrm{nad}}(\mathbf{r})\mathrm{d}\mathbf{r}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_th_row ltx_border_t" colspan="2">最终 FDET 能量（Final FDET energies）</th>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_t"><span class="ltx_text ltx_font_typewriter">Delta_Lin</span></th>
<td class="ltx_td ltx_align_left ltx_border_t">$\int(\rho_{A}^{I}(\mathbf{r})-\rho_{A}^{\mathrm{ref}}(\mathbf{r}))v_{xc,T}^{\mathrm{nad}}(\mathbf{r})\mathrm{d}\mathbf{r}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row"><span class="ltx_text ltx_font_typewriter">Final Energy (A)</span></th>
<td class="ltx_td ltx_align_left">$E_{A}^{\mathrm{emb}}[\Psi_{A}^{I},\rho_{B}]=\langle\Psi_{A}^{I}|\hat{H}_{A}|\Psi_{A}^{I}\rangle+J_{\mathrm{int}}[\rho_{A}^{I},\rho_{B}]+V_{B}^{\mathrm{nuc}}[\rho_{A}^{I}]$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_th ltx_th_row"></th>
<td class="ltx_td ltx_align_left">$+E_{xc,T}^{\mathrm{nad}}[\rho_{A}^{\mathrm{ref}},\rho_{B}]+\Delta^{\mathrm{lin}}[\rho_{A}^{I},\rho_{A}^{\mathrm{ref}},\rho_{B}]+V_{A}^{\mathrm{nuc}}[\rho_{B}]+V_{N_{A}N_{B}}$</td>
</tr>
<tr class="ltx_tr">
<th class="ltx_td ltx_align_left ltx_th ltx_th_row ltx_border_bb"><span class="ltx_text ltx_font_typewriter">Final Energy (A+B)</span></th>
<td class="ltx_td ltx_align_left ltx_border_bb">$E_{A}^{\mathrm{emb}}[\Psi_{A}^{I},\rho_{B}]+E_{B}$</td>
</tr>
</tbody>
</table>

表 11.11：输出项的定义。
