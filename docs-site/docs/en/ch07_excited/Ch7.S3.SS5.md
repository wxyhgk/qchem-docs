---
title: "7.3.5 Electron-Affinity (EA-) TDDFT"
---

## 7.3.5 Electron-Affinity (EA-) TDDFT

(July 4, 2026)

X-ray absorption spectra (XAS) pose a significant challenge for TDDFT.
The errors in peak positions for the K-edge XAS
of small gas-phase molecules are routinely in excess of
10 eV, and in condensed phase the errors in peak positions and intensities
cause severe distortions in K-edge spectra.
These errors can be traced to two sources:

1. A lack of orbital relaxation effects that is poorly compensated by
linear-response theory with only single excitations atop
ground state reference orbitals, and
2. a form of excited-state self-interaction error in the TDDFT potential
called particle–hole self-interaction error.

Both can be rectified by choosing a more suitable set of reference orbitals
for the core-excitation problem (*e.g.*, a core-ionized reference determinant)
as done with the static-exchange approximation in Section [7.6.2](subsec_STEX.md).
The generalization of STEX to include density functional theory
correlation is accomplished through two separate linear responses.
First, from an initial set of core-ionized molecular orbitals,
the missing core electron is reattached (response #1),
then a second linear response is done to excite the core electron.
The second linear response occurs atop a non-stationary initial density,
which is problematic due to the adiabatic approximation. Fortunately,
an exact first-order correction to errors associated with the
adiabatic approximation can be derived and is applied automatically in
all EA-TDDFT calculations. This correction happens to take a form
reminiscent of excited-state self-interaction error, so the EA-TDDFT
equations are naturally excited-state self-interaction free. Because of this, EA-TDDFT can
achieve statistical errors of just 0.5 eV root-mean-squared deviation
with standard density functionals.[[193]](../bib_references/bib.md#bib193)

Inclusion of orbital relaxation effects at the level of the reference orbitals in EA-TDDFT also
offers critical improvements to the spectra of solvated molecules
relative to TDDFT.[[194]](../bib_references/bib.md#bib194)

EA-TDDFT is only defined for restricted open-shell orbitals
and produces spin-pure spectra.

The full EA-TDDFT equations take a familiar form,

<a id="Ch7.E34"></a>

$$
\displaystyle A_{ia,ib} \tag{7.34a}
$$

where $E^{+}$ is the self-consistently optimized energy of the
core-ionized determinant, $F_{ab}^{+}$ are elements of the virtual-virtual block
of the core-ion Fock matrix, and all integrals are computed using the core-ion orbitals.
While the full EA-TDDFT equations can be solved at low cost
(by requesting **EA_RPA** in the *$nocis* input section),
it is seldom necessary to solve the whole RPA-like expression for K-edge XAS.
Instead, for K-edge transitions the Tamm-Dancoff approximation can be used
by setting **EA_TDA** in *$nocis* without sacrificing any accuracy.[[194]](../bib_references/bib.md#bib194)

Note only one occupied orbital index is considered in the EA-TDDFT
equations, meaning that the core-valence separation approximation is invoked implicitly.
Additionally, because EA-TDDFT is based on linear-response theory,
there is no construction of non-orthogonal
matrix elements between the ground state
and the singly-excited determinants as is done in STEX or 1C-NOCIS.
This means that EA-CIS (EA-TDDFT with the Hartree-Fock functional)
will produce slightly different results than STEX, but the differences
generally do not exceed 0.1 eV.[[193]](../bib_references/bib.md#bib193)

The presence of $E^{+}$ in the above equation means that
core-ionized reference orbitals must be optimized for each
core orbital from which excitations will be generated.
In the NOCIS and STEX implementations, this has been done exclusively with the
Maximum Overlap Method (MOM) from section [7.7.2](ex_OpSing.md).
However, **Q-Chem** now has several excellent algorithms for
converging non-*Aufbau* solutions to the SCF problem
such as State-Targeted Energy Projection (STEP)[[196]](../bib_references/bib.md#bib189)

and Square Gradient Minimization (SGM);[[511]](../bib_references/bib.md#bib526)

see Sections [7.7.8](ex_ROSTEP.md) and [7.7.5](ex_BEDSCF.md), respectively.
All of these approaches are now available in the EA-TDDFT
code by setting either **DSCF_ALGORITHM**
or **REF_SCF_ALGORITHM** within the *$nocis* input section.
A hybrid algorithm consisting of running STEP in the initial cycles of
an optimization to guide the solution towards a set of well-conditioned guess orbitals
for a subsequent MOM optimization has been used with great success when
other algorithms fail to converge. This can be invoked by setting
**DSCF_ALGORITHM** = **STEP_MOM**
and setting the point at which STEP turns off and MOM turns on with the keyword
**STEP_MOM_START**.

There are two points at which localization can be used to improve the
results or make orbital selection more convenient within EA-TDDFT.
First, when two or more reference orbitals are selected a Boys localization
is automatically performed on the core orbitals of interest to improve
convergence of the core-ion SCF to a proper minimum. This localization
routine may be controlled manually (*e.g.*, localizing several orbitals
but only computing excitations out of one of them, or turning off localization
altogether) with the keyword **LOCALIZE_ORBITALS**.
In large systems with many core orbitals of similar energy (*e.g.*,
water clusters where the response out of a particular O(1s) orbital is desired),
Subsystem Projected AO Decomposition (SPADE) orbitals[[253]](../bib_references/bib.md#bib254)

can be used to localize orbitals onto a particular subset of atoms before
**ORB_OFFSET** is considered. For instance, in the water cluster example given above,
if the first water molecule in the *$molecule* section
is of interest then one would set “**SUBSYSTEM_ATOMS** 1 2 3”
within the *$nocis* section and the variable **ORB_OFFSET**
would be set to 0 for the O(1s) orbital on this subset of atoms.
