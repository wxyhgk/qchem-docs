---
title: "7.6.1 Non-Orthogonal CIS (NOCIS)"
---

## 7.6.1 Non-Orthogonal CIS (NOCIS)

(July 4, 2026)

The motivation for the NOCIS method[[1024]](../bib_references/bib.md#bib1066)

is the desire to improve on CIS while still maintaining a reasonably low computational scaling.
It does so by including orbital relaxation, which CIS neglects altogether, and the non-orthogonal
interaction between multiple core-hole references, such as the O($1s$) orbitals in O${}_{2}$.

A brief overview of the NOCIS algorithm is as follows: following a ground-state orbital optimization, an SCF calculation
is performed using the maximum overlap method (MOM, see Section [4.5.14](../ch04_scf/topic_mom.md))
to compute an ionization from each localized core orbital of interest.
This introduces orbital relaxation, and also renders the excited states non-orthogonal to the ground state.
The Hamiltonian, overlap, and total spin squared matrices are constructed using the Slater-Condon rules for matrix elements between determinants which share a common set of orbitals and NOCI for the remaining matrix elements.[[1356]](../bib_references/bib.md#bib1417)

Finally, the generalized eigenvalue problem is solved.

A key feature in open-shell NOCIS is a separate optimization of any open-shell references, which are states in which a core-electron is excited to a singly-occupied ground-state orbital. These separate optimizations render these states non-orthogonal to the other excited states.

NOCIS is spin-pure, size consistent, and maintains spatial symmetry. Like CIS, NOCIS produces excited states with the same $m_{s}$ as the reference but potentially with larger total spin. For example, performing NOCIS on a molecule with a singlet ground state will produce both singlet and triplet excited states.
