---
title: "8.1.1 Overview"
---

## 8.1.1 Overview

(July 4, 2026)

A basis set is a set of functions combined linearly to model molecular
orbitals. Basis functions can be considered as representing the atomic orbitals
of the atoms and are introduced in quantum chemical calculations because the
equations defining the molecular orbitals are otherwise very difficult to solve.

Many standard basis sets have been carefully optimized and tested over the
years. In principle, a user would employ the largest basis set available in
order to model molecular orbitals as accurately as possible. In practice, the
computational cost grows rapidly with the size of the basis set so a compromise
must be sought between accuracy and cost. If this is systematically pursued, it
leads to a “theoretical model chemistry”,

 that is, a
well-defined energy procedure (*e.g.*, Hartree-Fock) in combination with a
well-defined basis set.

Basis sets have been constructed from Slater, Gaussian, plane wave and delta
functions. Slater functions were initially employed because they are considered
“natural” and have the correct behavior at the origin and in the asymptotic
regions. However, the two-electron repulsion integrals (ERIs) encountered when
using Slater basis functions are expensive and difficult to evaluate. Delta
functions are used in several quantum chemistry programs. However, while codes
incorporating delta functions are simple, thousands of functions are required
to achieve accurate results, even for small molecules. Plane waves are widely
used and highly efficient for calculations on periodic systems, but are not so
convenient or natural for molecular calculations.

The most important basis sets are contracted sets of atom-centered Gaussian
functions. The number of basis functions used depends on the number of core and
valence atomic orbitals, and whether the atom is light (H or He) or heavy
(everything else). Contracted basis sets have been shown to be computationally
efficient and to have the ability to yield chemical accuracy (see Appendix [A](../app_a_aoints/app_AOINTS.md)).
The **Q-Chem** program has been optimized to exploit basis sets of
the contracted Gaussian function type and has a large number of built-in
standard basis sets (developed by Dunning and Pople, among others) which the
user can access quickly and easily.

The selection of a basis set for quantum chemical calculations is very
important. It is sometimes possible to use small basis sets to obtain good
chemical accuracy, but calculations can often be significantly improved by the
addition of diffuse and polarization functions. Consult the literature,
including pertinent review
articles,[[608]](../bib_references/bib.md#bib631)

in order to aid your selection. See also the “Further Reading” section at
the end of this chapter.
