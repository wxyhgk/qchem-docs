---
title: "11.5.6 QM/MM models within EFP umbrella"
---

## 11.5.6 QM/MM models within EFP umbrella

(July 4, 2026)

Interface to **libefp** provides means to perform simple QM/MM calculations and
constrained QM region geometry optimziations. In this case, the fragment potentials
should include MM_CHARGE and MM_LJ sections,
see `https://libefp2.github.io/parameters.html#additional-efp-parameters` for detail.
Keyword EFP_QMMM specifies the type of interactions between the QM and MM regions
and between the MM (EFP) fragments, with options being mechanical and electrostatic embedding
and a mixed model, in which the polarizable QM/EFP calculation is augmented by Lennard-Jones
interactions between the QM and EFP regions.

Geometry optimziation of the QM region is enabled for the electrostatic embedding scheme
(EFP_QMMM = 2). The MM region remains rigid; only the QM atoms are subjected to
optimization in cartesian coordinates.
