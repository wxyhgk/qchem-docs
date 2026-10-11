---
title: "7.10.1 Introduction"
---

## 7.10.1 Introduction

(July 4, 2026)

The ADC($n$) family of correlated excited state methods is a series of
size-extensive excited state methods based on perturbation theory. Each order
$n$ of ADC presents the excited state equivalent to the well-known $n$th order
Møller-Plesset perturbation theory for the ground state. Currently, the ADC
variants ADC(0), ADC(1), ADC(2)-s, ADC(2)-x and ADC(3) are implemented in
**Q-Chem**.[[1494]](../bib_references/bib.md#bib1555)
 The resolution-of-the-identity
approximation can be used with any ADC variant. Additionally, there are
spin-opposite scaling versions of both ADC(2) variants
available.[[717]](../bib_references/bib.md#bib749)
 Core-excited states for the
simulation of x-ray absorption spectra can be computed exploiting the
core-valence separation (CVS) approximation. Currently, the CVS-ADC(1),
CVS-ADC(2)-s, CVS-ADC(2)-x and CVS-ADC(3) methods are
available.[[1494]](../bib_references/bib.md#bib1555)

Ionized and electron-attached states can be computed using the non-Dyson IP-
and EA-ADC methods. Currently, the IP-ADC(2), IP-ADC(3), EA-ADC(2) and EA-ADC(3) methods are
implemented.[[317]](../bib_references/bib.md#bib317)

In addition to Møller-Pesset based (MP-)ADC, regular schemes based on a
size-consistent Brillouin-Wigner (BWs) partitioning are available for excited states
(see also [6.8](../ch06_correlation/topic_bws2.md)).
Currently, BWs-ADC(0), BWs-ADC(2)-s, BWs-ADC(2)-x and
BWs-ADC(3) are implemented in combination with the resolution-of-identity
approximation.
