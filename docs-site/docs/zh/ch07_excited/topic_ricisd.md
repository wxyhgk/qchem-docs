---
title: "7.8.3 Resolution of the Identity CIS(D) Methods"
---

## 7.8.3 Resolution of the Identity CIS(D) Methods

(July 4, 2026)

Because of algorithmic similarity with MP2 calculation, the “resolution of the
identity” approximation can also be used in CIS(D). In fact, RI-CIS(D) is
orders of magnitudes more efficient than previously explained CIS(D) algorithms
for effectively all molecules with more than a few atoms. Like in MP2, this is
achieved by reducing the prefactor of the computational load. In fact, the
overall cost still scales with the fifth power of the system size.

Presently in **Q-Chem**, RI approximation is supported for closed-shell
restricted CIS(D) and open-shell unrestricted UCIS(D) energy calculations. The
theta diagnostic is not implemented for RI-CIS(D).
