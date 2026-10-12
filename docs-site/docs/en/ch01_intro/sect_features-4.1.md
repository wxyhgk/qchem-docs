---
title: "1.3.16 New Features in Q-Chem 4.1"
---

## 1.3.16 New Features in **Q-Chem** 4.1

(July 4, 2026)

- Fundamental algorithms:

- Improved parallel performance at all levels including new OpenMP capabilities for Hartree-Fock, DFT, MP2,
and coupled cluster theory (Z. Gan, E. Epifanovsky, M. Goldey, and Y. Shao; Section [2.2.1.1](../ch02_install/ssect_general-usage.md#sec:parallel)).
- Significantly enhanced ECP capabilities, including gradients and frequencies in all basis sets for which the energy can be evaluated
(Y. Shao and M. Head-Gordon; Section [8.10.7](../ch08_basis/sect_ECP_derivs.md)).
- SCF and DFT capabilities:

- TDDFT energy with the M06, M08, and M11 series of functionals.
- XYGJ-OS analytical energy gradient.
- TDDFT/C-PCM excitation energies, gradient, and Hessian (J. Liu and W. Liang; Section [7.3.7](../ch07_excited/subsec_tddft-cPCM.md)).
- Additional features in the maximum overlap method (MOM) approach for converging difficult SCF calculations
(N. A. Besley; Section [4.5.14](../ch04_scf/topic_mom.md)).
- Wave function correlation capabilities:

- RI and Cholesky decomposition implementation of all CC and EOM-CC methods enabling
applications to larger systems with reduced disk and memory requirements and
improved performance (E. Epifanovsky, X. Feng, D. Zuev, Y. Shao, and A. I. Krylov; Sections [6.12.10](../ch06_correlation/topic_ricc.md) and [6.12.11](../ch06_correlation/topic_cdcc.md)).
- Attenuated MP2 theory in the aug-cc-pVDZ and aug-cc-pVTZ basis sets, which truncates two-electron integrals to cancel basis set superposition
error, yielding results for intermolecular interactions that are much more accurate than standard MP2 in the same basis set
(M. Goldey and M. Head-Gordon; Section [6.7](../ch06_correlation/topic_attmp2.md)).
- Extended RAS-$n$SF methodology for ground and excited states involving strong non-dynamical correlation
(P. M. Zimmerman, D. Casanova, and M. Head-Gordon; Section [7.11](../ch07_excited/topic_rasi.md)).
- Coupled cluster valence bond (CCVB) method for describing molecules with strong spin correlations (D. W. Small and M. Head-Gordon;
Section [6.19.3](../ch06_correlation/subsec_CCVB.md)).
- Searching and scanning potential energy surfaces:

- Potential energy surface scans (Y. Shao; Section [9.6](../ch09_opt/sec_pes-scan.md)).
- Improvements in automatic transition structure searching via the “freezing string” method,
including the ability to perform such calculations without a Hessian calculation (S. M. Sharada and M. Head-Gordon;
Section [9.3.3](../ch09_opt/sect_approx_hess.md)).
- Enhancements to partial Hessian vibrational analysis (N. A. Besley; Section [10.8.4](../ch10_properties/partial-hess.md)).
- Calculating and characterizing inter- and intramolecular interactions

- Extension of EFP to macromolecules: fEFP approach (A. Laurent, D. Ghosh, A. I. Krylov, and L. V. Slipchenko; Section [11.5.5](../ch11_env/sec_fefp.md)).
- Symmetry-adapted perturbation theory level at the “SAPT0” level,
for intermolecular interaction energy decomposition analysis into
physically-meaningful components such as electrostatics, induction, dispersion,
and exchange. An RI version is also available (L. D. Jacobson, J. M. Herbert; Section [12.9](../ch12_frag/topic_sapt.md)).
- The “explicit polarization” (XPol) monomer-based SCF calculations to
compute many-body polarization
effects in linear-scaling time via charge embedding (Section [12.8](../ch12_frag/sect_xpol.md)), which
can be combined either with empirical potentials (*e.g.*, Lennard-Jones) for
the non-polarization parts of the intermolecular interactions, or better yet, with
SAPT for an *ab initio* approach called XSAPT that extends SAPT to systems containing more that two monomers
(L. D. Jacobson and J. M. Herbert; Section [12.10](../ch12_frag/sect_XSAPT.md)).
- Extension of the absolutely-localized molecular orbital (ALMO)-based energy
decomposition analysis to unrestricted cases (P. R. Horn and M. Head-Gordon; Section [12.5.3](../ch12_frag/sect_eda1.md)).
- Calculation of the populations of “effectively unpaired electrons” in low-spin state using DFT,
a new method of evaluating localized atomic magnetic moments within Kohn-Sham without symmetry breaking,
and Mayer-type bond order analysis with inclusion of static correlation effects (E. I. Proynov; Section [10.2.4](../ch10_properties/sect_odd_electron.md)).
- Quantum transport calculations including electron transmission
functions and electron tunneling currents under applied bias voltage (B. D. Dunietz and N. Sergueev; Section [13.4](../ch13_specialized/sect_transport.md)).
- Searchable online version of the **Q-Chem** PDF manual (J. M. Herbert and E. Epifanovsky).
