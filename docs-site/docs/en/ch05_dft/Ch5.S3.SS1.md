---
title: "5.3.1 Introduction"
---

## 5.3.1 Introduction

(July 4, 2026)

**Q-Chem** currently has more than 30 exchange functionals as well as more than
30 correlation functionals, and in addition over 150 exchange-correlation (XC)
functionals, which refer to functionals that are not separated into exchange
and correlation parts, either because the way in which they were parameterized
renders such a separation meaningless (*e.g.*, B97-D[[494]](../bib_references/bib.md#bib502)
 or
$\omega$B97X[[223]](../bib_references/bib.md#bib218)
) or because they are a standard linear
combination of exchange and correlation (*e.g.*, PBE[[1062]](../bib_references/bib.md#bib1112)
 or
B3LYP[[96]](../bib_references/bib.md#bib78)
). User-defined XC functionals can be
created as specified linear combinations of any of the 30+ exchange functionals
and/or the 30+ correlation functionals.

KS-DFT functionals can be organized onto a ladder with five rungs, in a
classification scheme (“Jacob’s Ladder”) proposed by John Perdew in
2001.[[1070]](../bib_references/bib.md#bib1116)

The first rung contains a functional that
only depends on the (spin-) density $\rho_{\sigma}$, namely, the local
spin-density approximation (LSDA). These functionals are exact for the infinite
uniform electron gas (UEG), but are highly inaccurate for molecular properties
whose densities exhibit significant inhomogeneity. To improve upon the
weaknesses of the LSDA, it is necessary to introduce an ingredient that can
account for inhomogeneities in the density: the density gradient,
$\hat{\bm{\nabla}}\rho_{\sigma}$. These generalized gradient approximation (GGA)
functionals define the second rung of Jacob’s Ladder and tend to improve
significantly upon the LSDA. Two additional ingredients that can be used to
further improve the performance of GGA functionals are either the Laplacian of
the density $\hat{\nabla}^{2}\rho_{\sigma}$, and/or the kinetic energy density,

<a id="eq:tau"></a>

$$
\tau_{\sigma}=\sum_{i}^{n_{\sigma}}\big{\|}\hat{\bm{\nabla}}\psi_{i,\sigma}\big{\|}^{2}\;. \tag{5.10}
$$

While functionals that employ both of these options are available in **Q-Chem**,
the kinetic energy density is by far the more popular ingredient and has been
used in many modern functionals to add flexibility to the functional form with
respect to both constraint satisfaction (non-empirical functionals) and
least-squares fitting (semi-empirical parameterization). Functionals that
depend on either of these two ingredients belong to the third rung of the
Jacob’s Ladder and are called meta-GGAs. These meta-GGAs often further improve
upon GGAs in areas such as thermochemistry, kinetics (reaction barrier
heights), and even non-covalent interactions.

Functionals on the fourth rung of Jacob’s Ladder are called hybrid density
functionals. This rung contains arguably the most popular density functional of
our time, B3LYP, the first functional to see widespread application in
chemistry. “Global” hybrid (GH) functionals such as B3LYP (as distinguished
from the “range-separated hybrids" introduced below) add a constant fraction
of “exact” (Hartree-Fock) exchange to any of the functionals from the first
three rungs. Thus, hybrid LSDA, hybrid GGA, and hybrid meta-GGA functionals can
be constructed, although the latter two types are much more common. As an
example, the formula for the B3LYP functional, as implemented in **Q-Chem**,
is[[484]](../bib_references/bib.md#bib496)

<a id="eq:GHGGA"></a>

$$
E_{\text{xc}}^{\textrm{B3LYP}}=c_{\text{x}}E_{\text{x}}^{\text{HF}}+(1-c_{\text{x}}-a_{\text{x}})E_{\text{x}}^{\text{Slater}}+a_{\text{x}}E_{\text{x}}^{\text{B88}}+(1-a_{\text{c}})E_{\text{c}}^{\text{VWN1RPA}}+a_{\text{c}}E_{\text{c}}^{\text{LYP}} \tag{5.11}
$$

where $c_{\text{x}}=0.20$, $a_{\text{x}}=0.72$, and $a_{\text{c}}=0.81$.

A more recent approach to introducing exact exchange into the functional form
is via range separation. Range-separated hybrid (RSH) functionals split the
exact exchange contribution into a short-range (SR) component and a long-range
(LR) component, often by means of the error function (erf) and complementary
error function ($\rm erfc\equiv 1-erf$):

<a id="eq:erf_partition"></a>

$$
\frac{1}{r_{12}}=\underbrace{\frac{\mbox{erfc}(\omega r_{12})}{r_{12}}}_{\text{SR}}+\underbrace{\frac{\mbox{erf}(\omega r_{12})}{r_{12}}}_{\text{LR}}\; \tag{5.12}
$$

The first term on the right in Eq. ([5.12](#eq:erf_partition)) is singular but
short-range, and decays to zero on a length scale of $\sim 1/\omega$, while the
second term constitutes a non-singular, long-range background. An RSH XC
functional can be expressed generically as

<a id="eq:RSHGGA"></a>

$$
E_{\text{xc}}^{\text{RSH}}=c_{\text{x}}E_{\text{x,SR}}^{\text{HF}}+c_{\text{x,LR}}E_{\text{x,LR}}^{\text{HF}}+(1-c_{\text{x,SR}})E_{\text{x,SR}}^{\text{DFT}}+(1-c_{\text{x,LR}})E_{\text{x,LR}}^{\text{DFT}}+E_{\text{c}}^{\text{DFT}}\;, \tag{5.13}
$$

where the SR and LR parts of the Coulomb operator are used, respectively, to
evaluate the HF exchange energies $E_{\text{x,SR}}^{\text{HF}}$ and $E_{\text{x,LR}}^{\text{HF}}$.
The corresponding DFT exchange functional is partitioned
in the same manner, but the correlation energy $E_{\text{c}}^{\text{DFT}}$ is
evaluated using the full Coulomb operator, $r_{12}^{-1}$. Of the two linear
parameters in Eq. ([5.13](#eq:RSHGGA)), $c_{\text{x,LR}}$ is usually either set to
1 to define long-range corrected (LRC) RSH functionals (see
Section [5.6](sect_LRC-DFT.md)) or else set to zero, which defines screened-exchange
(SE) RSH functionals. On the other hand, the fraction of short-range exact
exchange ($c_{\text{x,SR}}$) can either be determined via least-squares
fitting, theoretically justified using the adiabatic connection, or simply set
to zero. As with the global hybrids, RSH functionals can be fashioned using
all of the ingredients from the lower three rungs. The rate at which the local
DFT exchange is turned off and the non-local exact exchange is turned on is
controlled by the parameter $\omega$. Large values of $\omega$ tend to lead to
attenuators that are less smooth (unless the fraction of short-range exact
exchange is very large), while small values of (*e.g.*,
$\omega=0.2$–0.4 bohr${}^{-1}$) are the most common in semi-empirical RSH functionals.

The final rung on Jacob’s Ladder contains functionals that use not only
occupied orbitals (via exact exchange), but virtual orbitals as well (via
methods such as MP2 or the random phase approximation, RPA). These double
hybrids (DH) are the most expensive density functionals available in **Q-Chem**,
but can also be very accurate. The most basic form of a DH functional is

<a id="eq:DHGGA"></a>

$$
E_{\text{xc}}^{\text{DH}}=c_{\text{x}}E_{\text{x}}^{\text{HF}}+(1-c_{\text{x}})E_{\text{x}}^{\text{DFT}}+c_{\text{c}}E_{c}^{\text{MP2}}+(1-c_{\text{c}})E_{\text{c}}^{\text{DFT}}\;. \tag{5.14}
$$

As with hybrids, the coefficients can either be theoretically motivated or
empirically determined. In addition, double hybrids can use exact exchange
both globally or via range-separation, and their components can be as primitive
as LSDA or as advanced as in meta-GGA functionals. More information on double
hybrids can be found in Section [5.9](subsec_dhdft.md).

Finally, the last major advance in KS-DFT in recent years has been the
development of methods that are capable of accurately describing non-covalent
interactions, particularly dispersion. All of the functionals from Jacob’s
Ladder can technically be combined with these dispersion corrections, although
in some cases the combination is detrimental, particularly for semi-empirical
functionals that were parameterized in part using data sets of non-covalent
interactions, and already tend to overestimate non-covalent interaction
energies. The most popular such methods available in **Q-Chem** are:

- •

Non-local correlation (NLC) functionals (Section [5.7.2](sect_VV10.md)), including those of
Vydrov and Van Voorhis[[1414]](../bib_references/bib.md#bib1475)
 (VV09 and VV10) and of Lundqvist and Langreth[[327]](../bib_references/bib.md#bib331)

(vdW-DF-04 and vdW-DF-10). The revised VV10 NLC functional of Sabatini and coworkers (rVV10) is also available[[1192]](../bib_references/bib.md#bib1247)
.
- •

Damped, atom–atom pairwise empirical dispersion potentials from Grimme and
others[[494]](../bib_references/bib.md#bib502)

[DFT-D2, DFT-CHG, DFT-D3(0), DFT-D3(BJ), DFT-D3(CSO), DFT-D3M(0), DFT-D3M(BJ), and DFT-D3(op)];
see Section [5.7.3](subsec_DFT-D.md).
- •

The exchange-dipole models (XDM) of Johnson and Becke (XDM6 and XDM10); see Section [5.7.4](sect_XDM.md).
- •

The Tkatchenko-Scheffler (TS) method for dispersion interactions;[[1361]](../bib_references/bib.md#bib1421)
 see Section [5.7.5](sect_TS.md).
- •

The Many-Body Dispersion (MBD) method for van der Waals interactions[[1360]](../bib_references/bib.md#bib1422)
;
see Section [5.7.6](sect_MBD.md).

Below, we categorize the functionals that are available in **Q-Chem**, including
exchange functionals (Section [5.3.3](sect_DFTexchange.md)), correlation functionals
(Section [5.3.4](sect_DFTcorrelation.md)), and exchange-correlation functionals
(Section  [5.3.5](sect_DFTexchangecorrelation.md)). Within each category the
functionals will be categorized according to Jacob’s Ladder. Exchange and
correlation functionals can be invoked using the *$rem* variables
EXCHANGE and CORRELATION, while the exchange-correlation
functionals can be invoked either by setting the *$rem* variable
METHOD or alternatively (in most cases, and for backwards
compatibility with earlier versions of **Q-Chem**) by using the *$rem* variable
EXCHANGE. Some caution is warranted here. While setting
METHOD to PBE, for example, requests the
Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional,[[1062]](../bib_references/bib.md#bib1112)

which includes both PBE exchange and PBE correlation, setting
EXCHANGE = PBE requests only the exchange component and setting
CORRELATION = PBE requests only the correlation component.
Setting both of these values is equivalent to specifying
METHOD = PBE.

<table class="ltx_tabular ltx_centering ltx_guessed_headers ltx_align_middle">
<tbody class="ltx_tbody">
<tr class="ltx_tr">
<td class="ltx_td ltx_border_tt"></td>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">Single-Point</span></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">Optimization</span></th>
<th class="ltx_td ltx_align_center ltx_th ltx_th_column ltx_border_tt"><span class="ltx_text ltx_font_bold">Frequency</span></th>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_t" rowspan="8"><span class="ltx_text ltx_font_bold">Ground State</span></td>
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

Table 5.1: 
Available analytic properties for SCF calculations.
Functionals are arranged according to Jacob’s Ladder.

Finally, Table [5.1](#table:DFT_grads_and_parallel) provides a summary
of which categories of functionals are available
with analytic first derivatives (for geometry optimizations) or second
derivatives (for vibrational frequency calculations). If analytic derivatives
are not available for the requested job type, then **Q-Chem** will automatically
generate them via finite difference.
Since **Q-Chem** v. 6.3, the finite-difference procedure can be MPI parallelized.
Tests of the finite-difference procedure suggest that
finite-difference frequencies are accurate to $<1$ cm${}^{-1}$ except for very
low-frequency non-bonded modes that are not well-described by harmonic frequencies
anyway.[[847]](../bib_references/bib.md#bib880)

Time-dependent DFT (TDDFT) calculations of excited states, as described in
Section [7.3](../ch07_excited/sect_tddft.md), require derivatives $\partial^{2}E_{\text{xc}}/\partial\rho^{2}$.
Table [5.1](#table:DFT_grads_and_parallel) also indicates which functionals are available for TDDFT.
