---
title: "6.6.9 Dual-Basis MP2"
---

## 6.6.9 Dual-Basis MP2

(July 4, 2026)

The successful computational cost speedups of the previous sections often leave
the cost of the underlying SCF calculation dominant. The dual-basis method
provides a means of accelerating the SCF by roughly an order of magnitude, with
minimal associated error (see Section [4.7](../ch04_scf/sect_dualbasis.md)). This dual-basis
reference energy may be combined with RI-MP2 calculations for both
energies[[1300]](../bib_references/bib.md#bib1355)
 and analytic first
derivatives.[[332]](../bib_references/bib.md#bib335)
 In the latter case, further savings (beyond
the SCF alone) are demonstrated in the gradient due to the ability to solve the
response ($Z$-vector) equations in the smaller basis set. Refer to
Section [4.7](../ch04_scf/sect_dualbasis.md) for details and job control options.
