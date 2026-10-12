---
title: "5.5.3 Standard Quadrature Grids"
---

## 5.5.3 Standard Quadrature Grids

(July 4, 2026)

Four different “standard grids" are available in **Q-Chem**, designated
SG-$n$, for $n=0,1,2$, or 3; both quality and the computational cost of
these grids increases with $n$. These grids are constructed starting from a
“parent” grid ($N_{r},~{}N_{\Omega}$) consisting of $N_{r}$ radial spheres with
$N_{\Omega}$ angular (Lebedev) grid points on each, then systematically pruning
the number of angular points in regions where sophisticated angular quadrature
is not necessary, such as near the nuclei where the charge density is nearly
spherically symmetric and at long distance from the nuclei where it varies
slowly. A large number of points are retained in the valence region where
angular accuracy is critical. The SG-$n$ grids are summarized in
Table [5.3](#table:SG). While many electronic structure programs use some kind
of procedure to delete unnecessary grid points in the interest of computational
efficiency, **Q-Chem**’s SG-$n$ grids are notable in that the complete grid
specifications are available in the peer-reviewed
literature,[[448]](../bib_references/bib.md#bib460)
 to facilitate reproduction
of **Q-Chem** DFT calculations using other electronic structure programs. Just
as computed energies may vary quite strongly with the choice of basis set, so
too in DFT they may vary strongly with the choice of quadrature grid. In
publications, users should always specify the grid that is used, and it is
suggested to cite the appropriate literature reference from
Table [5.3](#table:SG).

<table class="ltx_tabular ltx_centering ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_tt">Pruned</td>
<td class="ltx_td ltx_align_center ltx_border_tt">Ref.</td>
<td class="ltx_td ltx_align_center ltx_border_tt">Parent Grid</td>
<td class="ltx_td ltx_align_center ltx_border_tt">No. Grid Points</td>
<td class="ltx_td ltx_align_left ltx_border_tt">Default Grid for</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">Grid</td>
<td class="ltx_td"></td>
<td class="ltx_td ltx_align_center">($N_{r},N_{\Omega}$)</td>
<td class="ltx_td ltx_align_center">(C atom)${}^{a}$
</td>
<td class="ltx_td ltx_align_left">Which Functionals?${}^{b}$
</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_t">SG-0</td>
<td class="ltx_td ltx_align_center ltx_border_t">[[241]](../bib_references/bib.md#bib242)
</td>
<td class="ltx_td ltx_align_center ltx_border_t">(23, 170)</td>
<td class="ltx_td ltx_align_right ltx_border_t">1,390 (36%)</td>
<td class="ltx_td ltx_align_left ltx_border_t">None</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">SG-1</td>
<td class="ltx_td ltx_align_center">[[448]](../bib_references/bib.md#bib460)
</td>
<td class="ltx_td ltx_align_center">(50, 194)</td>
<td class="ltx_td ltx_align_right">3,816 (39%)</td>
<td class="ltx_td ltx_align_left">LDA, most GGAs and hybrids</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">SG-2</td>
<td class="ltx_td ltx_align_center">[[301]](../bib_references/bib.md#bib305)
</td>
<td class="ltx_td ltx_align_center">(75, 302)</td>
<td class="ltx_td ltx_align_right">7,790 (34%)</td>
<td class="ltx_td ltx_align_left">Meta-GGAs; B95- and B97-based functionals</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">SG-3</td>
<td class="ltx_td ltx_align_center">[[301]](../bib_references/bib.md#bib305)
</td>
<td class="ltx_td ltx_align_center">(99, 590)</td>
<td class="ltx_td ltx_align_right">17,674 (30%)</td>
<td class="ltx_td ltx_align_left">Minnesota functionals</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_tt" colspan="5">
${}^{a}$Number in parenthesis is the fraction of points retained from the parent grid</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left" colspan="5">
${}^{b}$Reflects <span class="ltx_text ltx_font_smallcaps">Q-Chem</span> versions since v. 4.4.2</td>
</tr>
</tbody>
</table>

Table 5.3: 
Standard quadrature grids available in **Q-Chem**, along with the number of
grid points for a carbon atom, showing the reduction in grid points due to
pruning.

The SG-0 and SG-1 grids are designed for calculations on large
molecules using GGA functionals. SG-1 affords integration errors on the
order of $\sim$0.2 kcal/mol for medium-sized molecules and GGA functionals,
including for demanding test cases such as reaction enthalpies for
isomerizations. (Integration errors in total energies are no more than a few
$\mu$hartree, or $\sim$0.01 kcal/mol.) The SG-0 grid was derived in
similar fashion, and affords a root-mean-square error in atomization energies
of 72 $\mu$hartree with respect to SG-1, while relative energies are
reproduced well.[[241]](../bib_references/bib.md#bib242)
 In either case, errors of this magnitude
are typically considerably smaller than the intrinsic errors in GGA energies,
and hence acceptable. As seen in Table [5.3](#table:SG), SG-1 retains
$<40$% of the grid points of its parent grid, which translates directly into
cost savings.

Both SG-0 and SG-1 were optimized so that the integration error in the
energy falls below a target threshold, but derivatives of the energy (including
such properties as (hyper)polarizabilities[[216]](../bib_references/bib.md#bib212)
) are often more
sensitive to the quality of the integration grid. Special care is required,
for example, when imaginary vibrational frequencies are encountered, as
low-frequency (but real) vibrational frequencies can manifest as imaginary if
the grid is sparse. If imaginary frequencies are found, or if there is some
doubt about the frequencies reported by **Q-Chem**, the recommended procedure is
to perform the geometry optimization and vibrational frequency calculations
again using a higher-quality grid. (The optimization should converge quite
quickly if the previously-optimized geometry is used as an initial guess.)

SG-1 was the default DFT integration grid for all density functionals for
**Q-Chem** versions 3.2–4.4.
Beginning with **Q-Chem** v. 4.4.2, however, the default grid
is functional-dependent, as summarized in Table [5.3](#table:SG). This is a
reflection of the fact that although SG-1 is adequate for energy
calculations using most GGA and hybrid functionals (although care must be taken
for some other properties, as discussed below), it is *not* adequate to
integrate many functionals developed since $\sim$2005. These include
meta-GGAs, which are more complicated due to their dependence on the kinetic
energy density ($\tau_{\sigma}$ in Eq. ([5.10](Ch5.S3.SS1.md#eq:tau))) and/or the Laplacian
of the density ($\nabla^{2}\rho_{\sigma}$). Functionals based on B97, along with
the Minnesota suite of functionals,[[1569]](../bib_references/bib.md#bib1628)
 contain
relatively complicated expressions for the exchange inhomogeneity factor, and
are therefore also more sensitive to the quality of the integration
grid.[[1455]](../bib_references/bib.md#bib1517)
 To integrate these
modern density functionals, the SG-2 and SG-3 grids were
developed,[[301]](../bib_references/bib.md#bib305)
 which are pruned versions of the medium-quality
(75, 302) and high-quality (99, 590) integration grids, respectively. Tests
of properties known to be highly sensitive to the quality of the integration
grid, such as vibrational frequencies, hyper-polarizabilities, and potential
energy curves for non-bonded interactions, demonstrate that SG-2 is usually
adequate for meta-GGAs and B97-based functionals, and in many cases is
essentially converged with respect to an unpruned (250, 974)
grid.[[301]](../bib_references/bib.md#bib305)
 The Minnesota functionals are more sensitive to the
grid, and while SG-3 is often adequate, it is not completely converged in
the case of non-bonded interactions.[[301]](../bib_references/bib.md#bib305)

!!! note "Note"
    1.

    SG-0 was re-optimized for **Q-Chem** v. 3.0, so results may differ
    slightly as compared to older versions of the program.

    2.

    The SG-2 and SG-3 grids use a double-exponential radial
    quadrature,[[301]](../bib_references/bib.md#bib305)
     whereas a general grid (selected by
    setting XC_GRID = $XY$, as described in
    Section [5.4](sect_DFT_METHOD.md)) uses an Euler-MacLaurin radial quadrature.
    As such, *absolute* energies cannot be compared between, *e.g.*,
    SG-2 and XC_GRID = 000075000302, even though
    SG-2 uses a pruned (75, 302) grid. However, energy
    *differences* should be quite similar between the two.

    3.

    As noted in Ref. [[301]](../bib_references/bib.md#bib305)
    , for Minnesota functionals some wiggles in
    potential energy surfaces may persist with the SG-3 grid, especially for longer-range non-bonded interactions.
    Although these are rarely problematic for energy differences, if the user wants to eliminate these oscillations then
    we recommend an unpruned (99, 590) grid, *i.e.*, XC_GRID = 000099000590.

    4.

    Although much has been said in the literature regarding the grid sensitivity of the SCAN functional,[[83]](../bib_references/bib.md#bib68)

    the conventional wisdom that SCAN is extremely sensitive to grid quality is largely based on calculations in condensed-matter
    (periodic DFT) codes. In **Q-Chem**, the SG-2 and SG-3 grids appear to be of sufficient quality for SCAN calculations.[[161]](../bib_references/bib.md#bib154)

    (That said, regularized functionals such as r${}^{\text{2}}$SCAN[[419]](../bib_references/bib.md#bib428)
     do reduce the grid dependence.)

