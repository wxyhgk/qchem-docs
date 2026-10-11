---
title: "4.4.1 Introduction"
---

## 4.4.1 Introduction

(July 4, 2026)

The Roothaan-Hall and Pople-Nesbet equations of SCF theory are non-linear in
the molecular orbital coefficients. Like many mathematical problems involving
non-linear equations, prior to the application of a technique to search for a
numerical solution, an initial guess for the solution must be generated. If the
guess is poor, the iterative procedure applied to determine the numerical
solutions may converge very slowly, requiring a large number of iterations, or
at worst, the procedure may diverge.

Thus, in an *ab initio* SCF procedure, the quality of the initial guess
is of utmost importance for (at least) two main reasons:

- •

To ensure that the SCF converges to an appropriate ground state. Often
SCF calculations can converge to different local minima in wave function
space, depending upon which part of “LCAO space” in which the initial guess lands.
- •

When considering jobs with many basis functions requiring the
recalculation of ERIs at each iteration, using a good initial guess that
is close to the final solution can reduce the total job time
significantly by decreasing the number of SCF iterations.

For these reasons, sooner or later most users will find it helpful to have some
understanding of the different options available for customizing the initial
guess. **Q-Chem** currently offers six options for the initial guess:

- •

Superposition of Atomic Densities (SAD)
- •

Superposition of Atomic Potentials (SAP, only available with GEN_SCFMAN = TRUE)
- •

On-the-fly (automated) Superposition of Atomic Densities (AUTOSAD)
- •

Purified SAD guess (provides molecular orbitals; SADMO)
- •

Core Hamiltonian (CORE)
- •

Generalized Wolfsberg-Helmholtz (GWH)
- •

Reading previously obtained MOs from disk. (READ)
- •

Basis set projection (BASIS2)

The first six of these guesses are built-in, and are briefly described in
Section [4.4.2](sect_guess.md). The option of reading MOs from disk is described in
Section [4.4.3](sect_readmos.md). The initial guess MOs can be modified, either by
mixing, or altering the order of occupation. These options are discussed in
Section [4.4.4](sect_occupied.md). Finally, **Q-Chem**’s novel basis set projection
method is discussed in Section [4.4.5](sect_projection.md).
