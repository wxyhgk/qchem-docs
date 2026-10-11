---
title: "7.10.4 Resolution of the Identity ADC Methods"
---

## 7.10.4 Resolution of the Identity ADC Methods

(July 4, 2026)

Similar to MP2 and CIS(D), the ADC equations can be reformulated using the
resolution-of-the-identity (RI) approximation. This significantly reduces
the cost of the integral transformation and the storage requirements.
Although it does not change the overall computational scaling of $O(N^{5})$
for ADC(2)-s or $O(N^{6})$ for ADC(2)-x with the system
size, employing the RI approximation will result in computational speed-up of
calculations of larger systems.

The RI approximation can be used with all available ADC methods.
It is invoked as soon as an auxiliary basis set is specified using AUX_BASIS.
