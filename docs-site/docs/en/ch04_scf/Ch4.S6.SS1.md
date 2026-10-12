---
title: "4.6.1 Introduction"
---

## 4.6.1 Introduction

(July 4, 2026)

Construction of the effective Hamiltonian, or Fock matrix, has traditionally
been the rate-determining step in self-consistent field calculations, due
primarily to the cost of two-electron integral evaluation, even with the
efficient methods available in **Q-Chem** (see Appendix [A](../app_a_aoints/app_AOINTS.md)).
However, for large enough molecules, significant speedups are possible by
employing linear-scaling methods for each of the nonlinear terms that can
arise. Linear scaling means that if the molecule size is doubled, then the
computational effort likewise only doubles. There are three computationally
significant terms:

- Electron-electron Coulomb interactions, for which **Q-Chem** incorporates
the Continuous Fast Multipole Method (CFMM) discussed in section
[4.6.2](sect_cfmm.md)
- Exact exchange interactions, which arise in hybrid DFT calculations and
Hartree-Fock calculations, for which **Q-Chem** incorporates the LinK
method discussed in section [4.6.3](sect_link.md) below.
- Numerical integration of the exchange and correlation functionals in DFT
calculations, which we have already discussed in section [5.5](../ch05_dft/sect_quadrature.md).

**Q-Chem** supports energies and efficient analytical gradients for all three of
these high performance methods to permit structure optimization of large
molecules, as well as relative energy evaluation. Note that analytical second
derivatives of SCF energies do not exploit these methods at present.

For the most part, these methods are switched on automatically by the program
based on whether they offer a significant speedup for the job at hand.
Nevertheless it is useful to have a general idea of the key concepts behind
each of these algorithms, and what input options are necessary to control them.
That is the primary purpose of this section, in addition to briefly describing
two more conventional methods for reducing computer time in large calculations
in Section [4.6.4](sect_incfock.md).

There is one other computationally significant step in SCF calculations, and
that is diagonalization of the Fock matrix, once it has been constructed.
This step scales with the cube of molecular size (or basis set size), with a
small pre-factor. So, for large enough SCF calculations (very roughly in the
vicinity of 2000 basis functions and larger), diagonalization becomes the
rate-determining step. The cost of cubic scaling with a small pre-factor at
this point exceeds the cost of the linear scaling Fock build, which has a
very large pre-factor, and the gap rapidly widens thereafter. This sets an
effective upper limit on the size of SCF calculation for which **Q-Chem** is
useful at several thousand basis functions.
