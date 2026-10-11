---
title: "7.8.1 Introduction"
---

## 7.8.1 Introduction

(July 4, 2026)

CIS(D) is a simple, size-consistent doubles correction to CIS which has a
computational cost scaling as the fifth power of the basis set for each excited
state.[[544]](../bib_references/bib.md#bib554)
 In this sense, CIS(D) can be
considered as an excited state analog of the ground state MP2 method. CIS(D)
yields useful improvements in the accuracy of excitation energies relative to
CIS, and yet can be applied to relatively large molecules using **Q-Chem**’s
efficient integrals transformation package. In addition, as in the case of MP2
method, the efficiency can be significantly improved through the use of the
auxiliary basis expansions (Section [6.6](../ch06_correlation/topic_rimp2.md)).[[1162]](../bib_references/bib.md#bib1215)
