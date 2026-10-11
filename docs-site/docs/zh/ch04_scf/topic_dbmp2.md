---
title: "4.7.2 Dual-Basis MP2"
---

## 4.7.2 Dual-Basis MP2

(July 4, 2026)

The dual-basis approximation can also be used for the reference energy of a
correlated second-order Møller-Plesset (MP2)
calculation.[[1300]](../bib_references/bib.md#bib1355)
 When activated, the dual-basis HF
energy is first calculated as described above; subsequently, the MO
coefficients and orbital energies are used to calculate the correlation energy
in the large basis. This technique is particularly effective for RI-MP2
calculations (see Section [6.6](../ch06_correlation/topic_rimp2.md)), in which the cost of the
underlying SCF calculation often dominates.

Furthermore, efficient analytic gradients
of the DB-RI-MP2 energy have been developed[[332]](../bib_references/bib.md#bib335)
 and added to **Q-Chem**.
These gradients allow for the optimization of molecular structures with RI-MP2 near the
basis set limit. Typical computational savings are on the order of 50% (aug-cc-pVDZ) to 71% (aug-cc-pVTZ).
Resulting dual-basis errors are only 0.001 Å in molecular structures and are, again,
significantly less than use of a smaller basis set alone.
