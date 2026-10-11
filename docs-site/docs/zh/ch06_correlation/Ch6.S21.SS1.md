---
title: "6.21.1 Introduction"
---

## 6.21.1 Introduction

(July 4, 2026)

Treating all possible electronic configurations within a wave function via full
configuration interaction (FCI) provides the exact solution to the electronic
Schrödinger equation. Exponential growth in the number of electronic
configurations with system size makes this approach infeasible for all but the
smallest systems. The method of increments, however, can be used to
systematically capture electron correlation at polynomial cost while
maintaining size extensivity. This approach, called incremental FCI (iFCI), utilizes a
many-body expansion of the correlation energy, separating it into $n$-body
terms. Higher-orders of $n$ converge toward the FCI solution and often do so
without $n$ growing too large to be computationally burdensome. This method is
highly parallelizable and features versatile truncation
schemes.[[1585]](../bib_references/bib.md#bib1648)
