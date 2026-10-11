---
title: "6.11.1 Introduction"
---

## 6.11.1 Introduction

(July 4, 2026)

Joonho Lee working with Martin Head-Gordon developed and added an implementation of
RI-MP3 with only cubic-storage requirement.[[784]](../bib_references/bib.md#bib829)

The resulting code can be applied to larger systems than
what is possible in CCMAN2 ([6.12](topic_ccsd.md)) due to the improved storage scaling.
To use this method, one can set METHOD = RIMP3 along with AUXBASIS.
In essence, it applies the RI approximation in Eq. ([8.4](../ch08_basis/Ch8.S8.SS1.md#eq:riapprox)) to the MP3 correlation energy evaluation.
Interested readers are referred to Section [6.3](topic_mp2.md) for further details on the Møller-Plesset perturbation theory.

In addition to RI-MP3 one can incorporate scaled RI-MP2 and RI-MP3 correlation energy
contributions and alternative reference molecular orbitals (DFT and OOMP2) as seen
in recent works by Bertels *et al.*.[[115]](../bib_references/bib.md#bib102)
 and Rettig *et al.*.[[1159]](../bib_references/bib.md#bib1212)

The use of non-HF orbital references requires a composite job where the first calculation
generates the orbital reference and the second first recomputes the SCF energy and Fock with
HF on the fixed orbital reference and then proceeds with the correlated calculation.
