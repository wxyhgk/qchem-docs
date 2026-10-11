---
title: "6.12.8 Optimized Orbital Coupled Cluster Doubles (OD)"
---

## 6.12.8 Optimized Orbital Coupled Cluster Doubles (OD)

(July 4, 2026)

It is possible to greatly simplify the CCSD equations by omitting the single
substitutions (*i.e.*, setting the $T_{1}$ operator to zero). If the same single
determinant reference is used (specifically the Hartree-Fock determinant),
then this defines the coupled-cluster doubles (CCD) method, as specified by the following equations:

<a id="eq527"></a>
$$
\displaystyle E_{\text{CCD}} \tag{6.75a}
$$

The CCD method cannot itself usually be recommended because while pair
correlations are all correctly included, the neglect of single substitutions
causes calculated energies and properties to be significantly less reliable
than for CCSD. Single substitutions play a role very similar to orbital
optimization, in that they effectively alter the reference determinant to be
more appropriate for the description of electron correlation (the Hartree-Fock
determinant is optimized in the absence of electron correlation).

This suggests an alternative to CCSD and QCISD that has some additional
advantages. This is the optimized orbital CCD method (OO-CCD), which we
normally refer to as simply optimized doubles (OD).[[1251]](../bib_references/bib.md#bib1304)
 The
OD method is defined by the CCD equations above, plus the additional set of
conditions that the cluster energy is minimized with respect to orbital
variations. This may be mathematically expressed by

<a id="eq529"></a>
$$
\frac{\partial E_{\mathrm{CCD}}}{\partial\theta_{i}^{a}}=0 \tag{6.76}
$$

where the rotation angle $\theta_{i}^{a}$ mixes the $i$th occupied orbital
with the $a$th virtual (empty) orbital. Thus the orbitals that define
the single determinant reference are optimized to minimize the coupled-cluster
energy, and are variationally best for this purpose. The resulting orbitals are
approximate Brueckner orbitals.

The OD method has the advantage of formal simplicity (orbital variations and
single substitutions are essentially redundant variables). In cases where
Hartree-Fock theory performs poorly (for example artificial symmetry
breaking, or non-convergence), it is also practically advantageous to use the OD
method, where the HF orbitals are not required, rather than CCSD or QCISD.
**Q-Chem** supports both energies and analytical gradients using the OD method.
The computational cost for the OD energy is more than twice that of the CCSD or
QCISD method, but the total cost of energy plus gradient is roughly similar,
although OD remains more expensive. An additional advantage of the OD method is
that it can be performed in an active space, as discussed later, in
Section [6.14](sect_ccactive.md).
