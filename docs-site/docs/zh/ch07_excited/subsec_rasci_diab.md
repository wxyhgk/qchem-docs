---
title: "7.11.6 Diabatization of RAS-CI Eigenstates"
---

## 7.11.6 Diabatization of RAS-CI Eigenstates

(July 4, 2026)

Characterization of RAS-CI electronic states can be alternatively performed by
diabatization of multiple eigenstates of the RAS-CI Hamiltonian.
Diabatic states can be obtained following a Boys,[[1323]](../bib_references/bib.md#bib1379)

Edmiston-Ruedenberg[[1319]](../bib_references/bib.md#bib1380)
 or dipole-quadrupole (DQ) localization schemes.[[598]](../bib_references/bib.md#bib621)

See Section [10.15.1.3](../ch10_properties/Ch10.S15.SS1.md#subsec:diabatic) for details.
To activate the diabatization analysis of excited states in RAS-CI method it is necessary to
define a section block (see *$localized_diabatization* keyword) that defines the list of excited states to be included in the diabatization
(by increasing order). This is equivalent to the one used for the diabatization of CIS/TDDFT states.
