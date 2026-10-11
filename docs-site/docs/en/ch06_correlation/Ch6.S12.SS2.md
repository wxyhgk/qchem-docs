---
title: "6.12.2 Coupled Cluster Singles and Doubles (CCSD)"
---

## 6.12.2 Coupled Cluster Singles and Doubles (CCSD)

(July 4, 2026)

The standard approach for treating pair correlations self-consistently are
coupled-cluster methods where the cluster operator contains all single and
double substitutions,[[1138]](../bib_references/bib.md#bib1186)
 abbreviated as CCSD. CCSD yields
results that are only slightly superior to MP2 for structures and frequencies
of stable closed-shell molecules. However, it is far superior for reactive
species, such as transition structures and radicals, for which the performance
of MP2 is quite erratic.

A full textbook presentation of CCSD is beyond the scope of this manual, and
several comprehensive references are available. However, it may be useful to
briefly summarize the main equations. The CCSD wave function is:

<a id="eq518"></a>

$$
\left|{\Psi_{\mathrm{CCSD}}}\right\rangle=\exp\left({\hat{T}_{1}+\hat{T}_{2}}\right)\left|{\Phi_{0}}\right\rangle \tag{6.58}
$$

where the single and double excitation operators may be defined by their
actions on the reference single determinant (which is normally taken as the
Hartree-Fock determinant in CCSD):

<a id="eq519"></a>

$$
\hat{T}_{1}\left|{\Phi_{0}}\right\rangle=\sum_{i}^{\mathrm{occ}}{\sum_{a}^{\mathrm{virt}}{t_{i}^{a}}}\left|{\Phi_{i}^{a}}\right\rangle \tag{6.59}
$$

<a id="eq520"></a>

$$
\hat{T}_{2}\left|{\Phi_{0}}\right\rangle=\frac{1}{4}\sum_{ij}^{\mathrm{occ}}{\sum_{ab}^{\mathrm{virt}}{t_{ij}^{ab}}}\left|{\Phi_{ij}^{ab}}\right\rangle \tag{6.60}
$$

It is not feasible to determine the CCSD energy by variational minimization of
$\langle E\rangle_{\mathrm{CCSD}}$ with respect to the singles and doubles amplitudes
because the expressions terminate at the same level of complexity as full
configuration interaction (!). So, instead, the Schrödinger equation is
satisfied in the subspace spanned by the reference determinant, all single
substitutions, and all double substitutions. Projection with these functions
and integration over all space provides sufficient equations to determine the
energy, the singles and doubles amplitudes as the solutions of sets of
nonlinear equations. These equations may be symbolically written as follows:

<a id="A3.S8.EGx22"></a>

$$
\displaystyle E_{\mathrm{CCSD}} \tag{6.61}
$$

The result is a set of equations which yield an energy that is not necessarily
variational (*i.e.*, may not be above the true energy), although it is strictly
size-consistent. The equations are also exact for a pair of electrons, and, to
the extent that molecules are a collection of interacting electron pairs, this
is the basis for expecting that CCSD results will be of useful accuracy.

The computational effort necessary to solve the CCSD equations can be shown to
scale with the 6th power of the molecular size, for fixed choice of basis
set. Disk storage scales with the 4th power of molecular size, and
involves a number of sets of doubles amplitudes, as well as two-electron
integrals in the molecular orbital basis. Therefore the improved accuracy
relative to MP2 theory comes at a steep computational cost. Given these
scalings it is relatively straightforward to estimate the feasibility (or
non feasibility) of a CCSD calculation on a larger molecule (or with a larger
basis set) given that a smaller trial calculation is first performed.
**Q-Chem** supports both energies and analytic gradients for CCSD for
RHF and UHF references (including frozen core). For ROHF, only energies and
unrelaxed properties are available.
Available properties include dipole moments, angular momentum projections,
$\langle\hat{S}^{2}\rangle$, static polarizabilities,
and g-tensors (see Section [7.9.21](../ch07_excited/sec_EOMGRAD.md) for details).
