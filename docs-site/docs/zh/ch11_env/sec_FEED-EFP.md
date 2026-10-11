---
title: "11.5.4 Pairwise Fragment Energy Decomposition"
---

## 11.5.4 Pairwise Fragment Energy Decomposition

(July 4, 2026)

Decomposition of the interaction energy of the QM and EFP regions in the
energy components and in the contributions of individual solvent molecules is
available for the ground and excited states.[[1273]](../bib_references/bib.md#bib1326)

The ground state QM/EFP energy is decomposed as:

<a id="A3.S8.EGx108"></a>
$$
\displaystyle\begin{aligned} \displaystyle E_{\text{QM--EF, gr}}&\displaystyle=E_{\text{elec}}^{(1)}+E_{\text{pol-solute}}^{(0)}+E_{\text{pol-solute}}^{(1)}+E_{\text{pol-frag}}+E_{\text{QM--EFP}}^{\text{disp}}+E_{\text{QM--EF}}^{\text{ex-rep}}\\
&\displaystyle=\langle\Psi_{\text{gr}}^{0}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{0}\rangle+\Big{[}\langle\Psi_{\text{gr}}^{\text{sol}}|\hat{H}^{\text{QM}}|\Psi_{\text{gr}}^{\text{sol}}\rangle-\langle\Psi_{\text{gr}}^{0}|\hat{H}^{\text{QM}}|\Psi_{\text{gr}}^{0}\rangle\Big{]}\\
&\displaystyle\qquad+\Big{[}\langle\Psi_{\text{gr}}^{\text{sol}}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{\text{sol}}\rangle-\langle\Psi_{\text{gr}}^{0}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{0}\rangle\Big{]}+\Big{[}E_{\text{QM--EF, gr}}^{\text{pol}}+\langle\Psi_{\text{gr}}^{\text{sol}}|\hat{V}^{\text{pol}}|\Psi_{\text{gr}}^{\text{sol}}\rangle\Big{]}\\
&\displaystyle\qquad+E_{\text{QM-EF}}^{\text{disp}}+E_{\text{QM--EF}}^{\text{ex-rep}}\end{aligned} \tag{11.78}
$$

where the terms (from left to right) mean the first-order electrostatic energy, solute polarization energy of the zero- and first orders,
solvent polarization energy, and additive dispersion and exchange-repulsion terms.
Superscripts “sol” and “0” denote QM wave function optimized in a solvent and gas phase, respectively.
Each of the integrals involving $\hat{V}^{\text{Coul}}$ and
$\hat{V}^{\text{pol}}$ operators can be decomposed into individual fragment contributions, *e.g.*,

<a id="eq:feed_elec"></a>
$$
E_{\text{elec}}^{(1)}=\langle\Psi_{\text{gr}}^{0}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{0}\rangle=\sum_{A}^{\text{fragments}}\langle\Psi_{\text{gr}}^{0}|\sum_{k\in A}\hat{V}_{k}^{\text{Coul}}|\Psi_{\text{gr}}^{0}\rangle \tag{11.79}
$$

and similarly for the other terms. Polarization energy can be approximately decomposed into individual fragment contributions as:

<a id="eq:feed_pol"></a>
$$
E_{\text{QM--EF, gr}}^{\text{pol}}=\frac{1}{2}\sum_{A}^{\text{fragments}}\sum_{p\in A}(-\mu^{p}F^{\text{ai,nuc,p}}+{\bar{\mu}^{p}F^{\text{ai,elec},p}}) \tag{11.80}
$$

where $p$ are polarizability expansion points.
Dispersion and exchange-repulsion terms are also pairwise-additive.

The only term that cannot be similarly split into fragment contributions is the zero-order solute polarization energy:

<a id="eq:feed_pol2"></a>
$$
E_{\text{pol-solute}}^{(0)}=\langle\Psi_{\text{gr}}^{\text{sol}}|\hat{H}^{\text{QM}}|\Psi_{\text{gr}}^{\text{sol}}\rangle-\langle\Psi_{\text{gr}}^{0}|\hat{H}^{\text{QM}}|\Psi_{\text{gr}}^{0}\rangle\;. \tag{11.81}
$$

This term is referred to as "non-separable term" in the output printout.
From perturbation theory, this term is expected to be about twice smaller and of the opposite sign than the first-order solute polarization term:

<a id="eq:feed_pol3"></a>
$$
E_{\text{pol-solute}}^{(1)}=\langle\Psi_{\text{gr}}^{\text{sol}}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{\text{sol}}\rangle-\langle\Psi_{\text{gr}}^{0}|\hat{V}^{\text{Coul}}|\Psi_{\text{gr}}^{0}\rangle\;. \tag{11.82}
$$

Application of the energy decomposition analysis to the electronically excited states is described below.
The zero-order total solvatochromic shift can be represented as:

<a id="eq:FEED_exs"></a>
$$
E_{\text{solv}}^{\text{QM/EFP}}=\sum_{A}^{\text{fragments}}\big{(}\Delta E_{\text{ex/gr}}^{\text{elec(1),A}}+\Delta E_{\text{ex/gr}}^{\text{pol-solute(1)},A}+\Delta E_{\text{ex/gr}}^{\text{pol-frag(1)},A}\big{)}+\Delta E_{\text{ex/gr}}^{\text{pol-solute(0)},A}\;. \tag{11.83}
$$

The various terms are defined as

<a id="A3.S8.EGx109"></a>
$$
\displaystyle\Delta E_{\text{ex/gr}}^{\text{elec(1)},A} \tag{11.84}
$$

Fragment contribution of the perturbative polarization correction to the excited states [Eq.  ([11.77](sec_EOM-EFP.md#eq:EOM-EFP-ene2))] can be obtained as follows:

<a id="eq:feed:polcorr"></a>
$$
\Delta E_{\text{pol},A}=\frac{1}{2}\sum_{p\in A}\Bigl{[}-(\mu_{\rm{ex}}^{p}-\mu_{\rm{gr}}^{p})(F^{\text{mult},p}+F^{\text{nuc},p})+(\tilde{\mu}_{\text{ex}}^{p}F_{\text{ex}}^{\text{ai},p}-\tilde{\mu}_{\text{gr}}^{p}F_{\text{gr}}^{\text{ai},p})-(\mu_{\text{ex}}^{p}-\mu_{\text{gr}}^{p}+\tilde{\mu}_{\text{ex}}^{p}-\tilde{\mu}_{\text{gr}}^{p})F_{\text{ex}}^{\text{ai},p}\Bigr{]} \tag{11.88}
$$

where $A$ is a fragment of interest.

The energy is decomposed separately for all computed excited states. The excited state analysis is
implemented for CIS/TD-DFT and EOM-CCSD methods both in ccman and ccman2.
Energy decomposition analysis is activated by keyword EFP_PAIRWISE.
Both ground and excited state energy decompositions are conducted in two steps, controlled by keyword EFP_ORDER.
In the first step (EFP_ORDER = 1), the first-order electrostatic energy and
$\langle\Psi_{\text{gr}}^{0}|\hat{H}^{\text{QM}}|\Psi_{\text{gr}}^{0}\rangle$
(or $\langle\Psi_{\text{ex}}^{0}|\hat{H}^{\text{QM}}|\Psi_{\text{ex}}^{0}\rangle$ for the excited states)
part of the non-separable term are computed and printed.
In the second step (EFP_ORDER = 2), the remaining terms are evaluated. Thus,
for a complete analysis, the user is required to conduct two consequent simulations with EFP_ORDER
set to 1 and 2, respectively. Table [11.9](#tbl:feed) shows notations used in the output to denote various terms
in Eqs.  ([11.78](#eq:FEED_gs))–([11.88](#eq:feed:polcorr)).

Table 11.9: Notation for energy decomposition terms

| EFP_ORDER = 1 |  |
| --- | --- |
| (0) ELEC ENERGY <Psi_0\|Vcoul\|Psi_0> | $\langle\Psi_{\text{gr/ex}}^{0}\|\hat{V}^{\text{Coul},A}\|\Psi_{\text{gr/ex}}^{0}\rangle$ |
| TOTAL QM-EFP ELECTROSTATIC ENERGY | $E_{\text{gr/ex}}^{\text{elec(1)}}=\sum_{A}^{\text{fragments}}\textbf{(0)}_{A}$ |
| NON-SEPARABLE TERM <Psi_0\|H0\|Psi_0> | $\langle\Psi_{\text{gr/ex}}^{0}\|\hat{H}_{\text{QM}}\|\Psi_{\text{gr/ex}}^{0}\rangle$ |
| EFP_ORDER = 2 |  |
| (1) ELEC + SOLUTE POL ENERGY <Psi_sol\|Vcoul\|Psi_sol> | $\langle\Psi_{\text{gr/ex}}^{\text{sol}}\|\hat{V}^{\text{Coul},A}\|\Psi_{\text{gr/ex}}^{\text{sol}}\rangle$ |
| (2) SOLVENT POL ENERGY Epol | $\frac{1}{2}\sum_{p\in A}(-\mu^{p}_{\text{gr}}F^{\text{ai,nuc},p}+{\bar{\mu}^{p}_{\text{gr}}F_{\text{gr}}^{\text{ai,elec}},p})$ |
| (3) SOLVENT POL ENERGY <Psi_sol\|Vpol\|Psi_sol> | $\langle\Psi_{\text{gr/ex}}^{\text{sol}}\|\hat{V}^{\text{pol},A_{\text{gr}}}\|\Psi_{\text{gr/ex}}^{\text{sol}}\rangle$ |
| (4) SOLVENT POL ENERGY Epol_corr | for excited states only, see Eq. ( 11.88 ) |
| (5) SOLVENT POL ENERGY TOTAL | (2)+(3) |
| (6) PAIRWISE TOTAL ENERGY | (1) + (2) + (3) |
| QM-EFP TOTAL ENERGY | $\sum_{A}^{\text{fragments}}\textbf{(6)}_{A}$ |
| NON-SEPARABLE TERM <Psi_sol\|H0\|Psi_sol> | $\langle\Psi_{\text{gr/ex}}^{\text{sol}}\|\hat{H}_{\text{QM}}\|\Psi_{\text{gr/ex}}^{\text{sol}}\rangle$ |

The pairwise analysis is performed as a part of property calculation in excited state
methods, and it is associated with an additional computation cost as the electrostatic
and polarization integrals are reevaluated. In CIS and TDDFT calculations, the user may
opt to request the pairwise
analysis for a subset of excited states via the keyword EFP_PAIRWISE_STATES
and the group *$efp_pairwise_states* that gives a sinlge line of excited states to be included in
the analysis, with the first state having index 1.

> ```qchem
> $efp_pairwise_states
>     i j k
> $end
> ```
