---
title: "4.3.1 Introduction"
---

## 4.3.1 Introduction

(July 4, 2026)

As of version 5.1, **Q-Chem** uses a new SCF package, GEN_SCFMAN,
developed by E. J. Sundstrom, P. R. Horn and many other coworkers. In
addition to supporting the basic features of the previous SCF package (*e.g.*
restricted, unrestricted and restricted open-shell HF/KS-DFT calculations),
many new features are now available in **Q-Chem**, including:

- •

Addition of several useful SCF convergence algorithms and support for
user-specified hybrid algorithm (Section [4.5.12](sub_custom_algorithm.md)).
- •

More general and user-friendly internal stability analysis and
automatic correction for the energy minimum (Section [4.5.17](sub_stability_analysis.md)).

GEN_SCFMAN also supports a wider range of orbital types, including complex
orbitals. A full list of supported orbitals is:

- •

Restricted (R): typically appropriate for closed shell molecules at their
equilibrium geometry, where electrons occupy orbitals in pairs.
- •

Unrestricted (U): appropriate for radicals with an odd number of
electrons, and also for molecules with even numbers of electrons where
not all electrons are paired, *e.g.*, stretched bonds and diradicals.
- •

Restricted open-shell (RO): for open-shell molecules, where the $\alpha$
and $\beta$ orbitals are constrained to be identical.
- •

Canonical restricted open-shell (can. RO or “ROSCF-DODS”):
canonical form of ROSCF, see Section [4.5.18](sub_ROHF-DODS.md) for details.
- •

Open-shell singlet ROSCF (OS_RO): see the “ROKS" method documented in
Section [7.7.4](../ch07_excited/ex_ESROKS.md).
- •

Generalized (G): *i.e.*, each MO is associated with both $\alpha$ and
$\beta$ spin components.
- •

The use of complex orbitals (with Hartree-Fock only): restricted (CR),
unrestricted (CU), and generalized (CG).

Aspects of an SCF calculation such as the SCF guess, the use of efficient
algorithms to construct the Fock matrix like occ-RI-K (see
Section [4.6.8](subsec_occrik.md)), are unaffected by the use of GEN_SCFMAN.
Likewise, using GEN_SCFMAN does not make any difference to the post-SCF
procedures such as correlated methods, excited state calculations and
evaluation of molecular properties.

It should be noted that many special features (*e.g.* dual-basis SCF, CDFT,
*etc.*) based on **Q-Chem**’s old SCF code are not yet supported in GEN_SCFMAN.
They will become available in the future.

Starting Q-Chem v7.0, MPI+OMP-parallel non-RI SCF calculations done with DIIS
(Section [4.5.3](sect_diis.md)), GDM (Section [4.5.7](sect_gdm.md)), and the robust SCF pipelines
(Section [4.5.13](sub_scf_robust_pipelines.md)) are supported for RHF, UHF, and ROHF ansätze.
Q-Chem v7.0 uses the replicated-Fock approach in which each MPI rank allocates
memory for the entire Fock matrix. Since the full Fock matrix is built at the end of
the Fock build during the SCF iteration, the per-rank memory overhead must be
considered while spawning multiple MPI ranks on the same physical node.
