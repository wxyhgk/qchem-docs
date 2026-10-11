---
title: "7.11.8 Direct RAS-nSF-IP/EA (librassf)"
---

## 7.11.8 Direct RAS-nSF-IP/EA (**librassf**)

(July 4, 2026)

The **librassf** module enables the use of Fock-space CI RAS-$n$SF-IP/EA calculations.
The CAS-$n$SF-IP/EA approach combines non-particle-number-conserving and
non-spin-conserving operators to model systems with spin and spatial degeneracies.
For example, the CAS-1SF-IP operator is defined as follows:

<a id="Ch7.E171"></a>
$$
|\Psi\rangle=\sum_{ij\bar{a}}c_{ij}^{\bar{a}}\hat{a}_{ij}^{\bar{a}}|\Psi^{\text{Ref}}\rangle \tag{7.171}
$$

The **librassf** module can also perform traditional spin-flip and IP/EA calculations.
External hole and particle excitations (RAS(h) and RAS(p), respectively) can also be
added; this orbital relaxation is particularly important for IP/EA calculations
due to the change in electron count.

Our implementation uses explicit expressions for unique changes in alpha and
beta electron counts. These methods have been efficiently implemented using
direct tensor contractions rather than alpha and beta strings. The code also
allows the user to select the appropriate number of spin-flips, limiting the
number of determinants considered in cases with large active spaces.

Currently, the following schemes are implemented: CAS-1SF, RAS(h)-1SF,
RAS(p)-1SF, RAS(h,p)-1SF, CAS-2SF, CAS-IP, RAS(h)-IP, CAS-EA, RAS(p)-EA,
CAS-1SF-IP, RAS(h)-1SF-IP, CAS-1SF-EA, and RAS(p)-1SF-EA.
