---
title: "7.13.1 Introduction"
---

## 7.13.1 Introduction

(July 4, 2026)

As methods for *ab initio* calculations of excited states are becoming
increasingly more routine, questions arise concerning how best to extract
chemical meaning from such calculations. There are several approaches for
analyzing molecular excited states; they are based on reduced one-particle
density matrices (OPDMs). The two objects exploited in this analysis are: (i)
the difference between the ground- and excited-state OPDMs and (ii) the
transition OPDM connecting the ground and excited state. In the case of CIS and
TDDFT/TDA wave functions, both quantities are identical and can be directly
mapped into the CIS amplitudes;[[572]](../bib_references/bib.md#bib586)

however, for correlated wave functions the two
objects are not the same. The most basic analysis includes calculation of
attachment and detachment densities[[538]](../bib_references/bib.md#bib555)

(equivalent within TDDFT to particle and hole densities, respectively),[[572]](../bib_references/bib.md#bib586)

and natural transition orbitals (NTOs).[[913]](../bib_references/bib.md#bib947)

These quantities allow one to arrive to
a most compact description of an excited state. More detailed analysis allows
one to derive additional insight about the nature of the excited state.
Detailed description and illustrative examples can be found
elsewhere,[[1099]](../bib_references/bib.md#bib1142)

including a review of visualization tools for TDDFT/TDA calculations.[[572]](../bib_references/bib.md#bib586)

This section describes the theoretical background behind attachment/detachment analysis and natural transition orbitals, while details of the input
for creating data suitable for plotting these quantities is described
separately in Chapter [10](../ch10_properties/chap_properties.md), which also describes additional
excited-state analysis tools. For historical reasons, there are duplicate
implementations of some features. For example, CIS and TDDFT wave functions can
be analyzed using an original built-in code and by using a more recent module, **libwfa**.
