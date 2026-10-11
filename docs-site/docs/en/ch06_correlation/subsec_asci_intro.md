---
title: "6.22.1 Introduction"
---

## 6.22.1 Introduction

(July 4, 2026)

Selected CI methods seek to approximate full CI (FCI) energy, possibly in an active space,
by including only the most important determinants for a particular problem. There
are many flavors of selected CI going back to the 1970s. **Q-Chem** includes the adaptive
sampling configuration interaction (ASCI) method. In the ASCI method, a trial CI wave
function $\psi^{k}$ is iteratively improved by the inclusion of new determinants that
are deemed important. The selection rule is derived from a consistency relationship
among the coefficients in a CI expansion of the exact FCI wave function.
