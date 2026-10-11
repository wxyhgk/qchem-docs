---
title: "5.5.2 Angular Grids"
---

## 5.5.2 Angular Grids

(July 4, 2026)

For a fixed value of the radial spherical-polar coordinate $r$, a function
$f(\mathbf{r})\equiv f(r,\theta,\phi)$ has an exact expansion in spherical
harmonic functions,

<a id="Ch5.E16"></a>
$$
f(r,\theta,\phi)=\sum_{\ell=0}^{\infty}\sum_{m=-\ell}^{\ell}c_{\ell m}\mbox{Y}_{\ell m}(\theta,\phi)\;. \tag{5.16}
$$

Angular quadrature grids are designed to integrate $f(r,\theta,\phi)$ for fixed
$r$, and are often characterized by their degree, meaning the maximum value of
$\ell$ for which the quadrature is exact, as well as by their efficiency,
meaning the number of spherical harmonics exactly integrated per degree of
freedom in the formula. **Q-Chem** supports the following two types of angular
grids.

- •

**Lebedev grids.**
These are specially-constructed grids for quadrature on the surface of a
sphere,[[776]](../bib_references/bib.md#bib808)
 based on the
octahedral point group. Lebedev grids available in **Q-Chem** are listed in
Table [5.2](#table:Lebedev). These grids typically have near-unit efficiencies,
with efficiencies exceeding unity in some cases. A Lebedev grid is selected by
specifying the number of grid points (from Table [5.2](#table:Lebedev)) using the
*$rem* keyword XC_GRID, as discussed below.

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<thead class="ltx_thead">
<tr class="ltx_tr">
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_th_row ltx_border_tt" rowspan="2">No. Points</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_r ltx_border_tt">Degree</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_th_row ltx_border_tt" rowspan="2">No. Points</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_r ltx_border_tt">Degree</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_th_row ltx_border_tt" rowspan="2">No. Points</th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt">Degree</th>
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

Table 5.2: 
Lebedev angular quadrature grids available in **Q-Chem**.
- •

**Gauss-Legendre grids.**
These are spherical direct-product grids in the two spherical-polar angles,
$\theta$ and $\phi$. Integration in over $\theta$ is performed using a Gaussian
quadrature derived from the Legendre polynomials,
while integration over $\phi$ is performed using equally-spaced points. A
Gauss-Legendre grid is selected by specifying the total number of points,
$2N^{2}$, to be used for the integration, which specifies a grid consisting of
$2N_{\phi}$ points in $\phi$ and $N_{\theta}$ in $\theta$, for a degree of
$2N-1$. Gauss-Legendre grids exhibit efficiencies of only 2/3, and are thus
lower in quality than Lebedev grids for the same number of grid points, but
have the advantage that they are defined for arbitrary (and arbitrarily-large)
numbers of grid points. This offers a mechanism to achieve arbitrary accuracy
in the angular integration, if desired.

Combining these radial and angular schemes yields an intimidating selection of
quadratures, so it is useful to standardize the grids. This is done for the
convenience of the user, to facilitate comparisons in the literature, and also
for developers wishing to compared detailed results between different software
programs, because the total electronic energy is sensitive to the details of
the grid, just as it is sensitive to details of the basis set. Standard
quadrature grids are discussed next.
