---
title: "7.9.6 Spin-Flip Methods for Di- and Triradicals"
---

## 7.9.6 Spin-Flip Methods for Di- and Triradicals

(July 4, 2026)

The spin-flip method[[726]](../bib_references/bib.md#bib757)

addresses problems due to small HOMO-LUMO gaps, associated with a single-determinant
description of the wave function. Both closed- and open-shell singlet states are
described within a single reference as spin-flipping, (*e.g.*, $\alpha\rightarrow\beta$) excitations from the triplet reference state, for which both dynamical
and non-dynamical correlation effects are smaller than for the corresponding
singlet state. This is because the exchange hole, which arises from the Pauli
exclusion between same-spin electrons, partially compensates for the poor
description of the coulomb hole by the mean-field Hartree–Fock model.
Furthermore, because two $\alpha$ electrons cannot form a bond, no bond
breaking occurs as the internuclear distance is stretched, and the triplet wave
function remains essentially single-reference in character. The spin-flip
approach has also proved useful in the description of di- and tri-radicals as
well as some problematic doublet states.

The spin-flip method is available for the CIS, CIS(D), CC2, CISD, CISDT, OD, CCSD,
EOM-(2,3), and CCSDT levels of theory and the spin complete SF-XCIS (see
Section [7.2.3.2](Ch7.S2.SS3.md#topic:sf)). An ${\cal{O}}({N^{7}})$ non-iterative triples corrections are
also available—*e.g.*, (dT) and (fT).
For the OD and CCSD models, the following non-relaxed
properties are also available: dipoles, transition dipoles, SOCs, eigenvalues of the
spin-squared operator ($\langle\hat{S}^{2}\rangle$), and densities. Analytic
gradients are also for SF-CIS and EOM-SF-CCSD methods.
Construction of effective Hamiltonians in Heisenberg and Hubbard spaces from
EOM-SF wave functions is described in the Section [13.6](../ch13_specialized/sec_EffHam.md).
To invoke a spin-flip
calculation the SF_STATES *$rem* should be used, along with the
associated *$rem* settings for the chosen level of correlation by using
METHOD (recommended) or using older keywords (CORRELATION,
and, optionally, EOM_CORR). Note that the high multiplicity triplet
or quartet reference states should be used.

Several double SF methods have also been implemented.[[207]](../bib_references/bib.md#bib200)

To invoke these methods, use DSF_STATES.
