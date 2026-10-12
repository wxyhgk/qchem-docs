---
title: "4.1.1 Overview"
---

## 4.1.1 Overview

(July 4, 2026)

Theoretical “model chemistries"

 involve two principle
approximations. One must specify, first of all, the type of atomic orbital
(AO) basis set that will be used to construct molecular orbitals (MOs), via
the “linear combination of atomic orbitals” (LCAO) *ansatz*, available
options for which are discussed in Chapter [8](../ch08_basis/chap_basis.md).
Second, one must specify the manner in which the instantaneous
interactions between electrons (“electron correlation”) are to be treated.
Self-consistent field (SCF) methods, in which electron correlation is described
in a mean-field way, represent the simplest, most affordable, and most
widely-used electronic structure methods. The SCF category of methods includes
both Hartree-Fock (HF) theory as well as Kohn-Sham (KS) density functional
theory (DFT). This Chapter summarizes **Q-Chem**’s SCF capabilities, while
Chapter [5](../ch05_dft/chap_DFT.md) provides further details specific to DFT calculations.
Chapter [6](../ch06_correlation/chap_correlation.md) describes the more sophisticated (but also more
computationally expensive!) post-HF, wave function-based methods for describing
electron correlation. If you are new to quantum chemistry, we recommend an
introductory textbook such as Refs. 

,

, or 

.

Section [4.2](sec_SCF_theory.md) provides the theoretical background behind SCF
methods, including both HF and KS-DFT. In some sense, the former may be
considered as a special case of the latter, and job-control *$rem* variables
are much the same in both cases. Basic SCF job control is described in
Section [4.3](sec_SCF_job-control.md). Later sections introduce more specialized
options that can be consulted as needed. Of particular note are the following:

- Initial guesses for SCF calculations (Section [4.4](sect_initialguess.md)).
Modification of the guess is recommended in cases where the SCF
calculation fails to converge.
- Changing the SCF convergence algorithm (Section [4.5](sect_convergence.md))
is also a good strategy when the SCF calculation fails to converge.
- Linear-scaling, “${\cal{O}}({N})$”, and other reduced-cost methods are
available for large systems (see Section [4.6](sec_O_N.md)).
- Unconventional SCF calculations. Some non-standard SCF methods
with novel physical and mathematical features are available. These include:

- Dual-basis SCF calculations (Section [4.7](sect_dualbasis.md)) and DFT
perturbation theory (Section [4.8](sect_HFPC.md)), which facilitate
large-basis quality results but require self-consistent iterations
only in a smaller basis set.
- SCF meta-dynamics (Section [4.9.2](sec_SCF-meta-dyn.md)), which can be
used to locate multiple solutions to the SCF equations and to help
check that the solution obtained is actually the lowest minimum.

Some of these unconventional SCF methods are available exclusively in **Q-Chem**.
