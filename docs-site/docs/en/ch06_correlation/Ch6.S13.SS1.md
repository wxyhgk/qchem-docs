---
title: "6.13.1 (T) Triples Corrections"
---

## 6.13.1 (T) Triples Corrections

(July 4, 2026)

To approach chemical accuracy in reaction energies and related properties, it
is necessary to account for electron correlation effects that involve three
electrons simultaneously, as represented by triple substitutions relative to
the mean field single determinant reference, which arise in MP4. The best
standard methods for including triple substitutions are the CCSD(T)[[1141]](../bib_references/bib.md#bib1193)

and QCISD(T) methods.[[1113]](../bib_references/bib.md#bib1162)
 The accuracy of
these methods is well-documented for many cases,

 and in
general is a very significant improvement relative to the starting point
(either CCSD or QCISD). The cost of these corrections scales with the
7th power of molecule size (or the 4th power of the number of
basis functions, for a fixed molecule size), although no additional disk resources
are required relative to the starting coupled-cluster calculation. **Q-Chem**
supports the evaluation of CCSD(T) and QCISD(T) energies, as well as the
corresponding OD(T) correction to the optimized doubles method discussed in the
previous subsection. Gradients and properties are not yet available for
any of these (T) corrections.
