---
title: "5.10.1 Introduction"
---

## 5.10.1 Introduction

(July 4, 2026)

No GGA exchange functional can simultaneously produce the correct contribution
to the exchange energy density and exchange potential in the asymptotic region
of molecular systems,[[1386]](../bib_references/bib.md#bib1445)
 and existing GGA
exchange-correlation (XC) potentials decay much faster than the correct $-1/r$
XC potential in the asymptotic region.[[214]](../bib_references/bib.md#bib211)
 High-lying occupied
orbitals and low-lying virtual orbitals are therefore too loosely bound, and
$-\varepsilon_{\rm HOMO}$ becomes far smaller than the ionization energy,
despite the exact condition that these should be the same for the exact
functional.[[1385]](../bib_references/bib.md#bib1444)
 Moreover, response properties may
be poorly predicted from TDDFT calculations with GGA
functionals.[[1385]](../bib_references/bib.md#bib1444)
 Long-range corrected hybrid DFT (LRC-DFT),
described in Section [5.6](sect_LRC-DFT.md), has greatly remedied this situation,
but is more expensive that KS-DFT with GGA functionals due to the use of
Hatree-Fock exchange. The asymptotic corrections described in this section are
designed to remedy the same problems but within the GGA framework.
