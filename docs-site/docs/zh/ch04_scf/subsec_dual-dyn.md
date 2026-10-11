---
title: "4.7.3 Dual-Basis Dynamics"
---

## 4.7.3 Dual-Basis Dynamics

(July 4, 2026)

The ability to compute SCF and MP2 energies and forces at reduced cost makes dual-basis calculations
attractive for *ab initio* molecular dynamics simulations, which are described in Section [9.9](../ch09_opt/topic_aimd.md).
Dual-basis BOMD has demonstrated[[1301]](../bib_references/bib.md#bib1359)

savings of 58%, even relative to state-of-the-art, Fock-extrapolated BOMD. Savings are further
increased to 71% for dual-basis RI-MP2 dynamics. Notably, these timings outperform estimates
of extended Lagrangian (“Car-Parrinello”) dynamics, without detrimental energy conservation
artifacts that are sometimes observed in the latter.[[558]](../bib_references/bib.md#bib572)

Two algorithm improvements make modest but worthwhile improvements to dual-basis dynamics. First,
the iterative, small-basis calculation can benefit from Fock matrix extrapolation.[[558]](../bib_references/bib.md#bib572)

Second, extrapolation of the response equations (“$Z$-vector” equations) for
nuclear forces further increases efficiency.[[1304]](../bib_references/bib.md#bib1360)
 (See Section [9.9](../ch09_opt/topic_aimd.md).)
**Q-Chem** automatically
adjusts to extrapolate in the proper basis set when DUAL_BASIS_ENERGY is activated.
