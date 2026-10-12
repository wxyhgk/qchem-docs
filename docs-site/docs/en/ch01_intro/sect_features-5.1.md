---
title: "1.3.11 New Features in Q-Chem 5.1"
---

## 1.3.11 New Features in **Q-Chem** 5.1

(July 4, 2026)

- Improved OpenMP parallelization for:

- SCF vibrational frequency calculations (Zhengting Gan)
- RIMP2 gradient (Fazle Rob, Joonho Lee, Xintian Feng, Evgeny Epifanovsky)
- Complete active space self-consistent field (CASSCF) and adaptive sampling CI (Daniel Levine, Martin Head-Gordon)
- Tkatchenko-Scheffler van der Waals method (Section [5.7.5](../ch05_dft/sect_TS.md)) and many-body dispersion method (Section [5.7.6](../ch05_dft/sect_MBD.md))
(Denis Barton, Ka Un Lao, & Rob DiStasio)
- Enhancements to the coupled-cluster package:

- Core/valence separation for EOM-CCSD core-level excited and ionized states
(Marta Vidal, Anna Krylov, Xintian Feng, Evgeny Epifanovsky, Sonia Coriani), Section [7.9.9](../ch07_excited/sub_cvs_eom.md).
- NTO analysis of two-photon transitions (Kaushik Nanda, Anna Krylov), Section [7.9.21.6](../ch07_excited/sec_EOMGRAD.md#sec:2PA).
- NTO analysis of the complex-valued EOM wave functions (Anna Krylov, Wojciech Skomorowski), Section [7.9.21](../ch07_excited/sec_EOMGRAD.md).
- Analytic gradients for Cholesky-decomposed and resolution-of-identity CCSD and EOM-CCSD (Xintian Feng, Anna Krylov).
- Improved performance, reduced disk usage by coupled-cluster methods (Evgeny Epifanovsky, Ilya Kaliman, Xintian Feng).
- New features in NTO analysis: Energies of NTOs (Anna Krylov), Section [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md).
- Finite-difference evaluation of non-linear properties (Marc de Wergifosse, Anna Krylov), Section [10.13.3](../ch10_properties/sect_Romberg.md).
- Poisson boundary conditions for SCF calculations (Marc Coons, John Herbert), Section [11.2.11](../ch11_env/sect_PEQS.md).

- Enables quantum chemistry calculations in an arbitrary (anisotropic and
inhomogeneous) dielectric environment.
- Nonequilibrium solvent corrections for vertical ionization energies.
- Energy decomposition analysis (EDA):

- EDA based on symmetry-adapted perturbation theory and constrained DFT (SAPT/cDFT-EDA),
Section [12.11](../ch12_frag/sect_SAPTEDA.md) (Ka Un Lao, Kevin Carter-Fenk, John Herbert)
- ALMO-EDA for CIS and TDDFT/TDA excited states, Section [12.7.5](../ch12_frag/sect_ex_eda.md)
(Qinghui Ge, Yuezhi Mao, Martin Head-Gordon)
- Perturbative ALMO-CTA and COVP analysis in EDA2 (Yuezhi Mao, Martin Head-Gordon)
- Analytic derivative couplings for computing excitation/vibration energy couplings within the
*ab initio* Frenkel-Davydov exciton model (Adrian Morrison, John Herbert), Section [12.14](../ch12_frag/sect_AIFDEM.md).
- Hyperfine and nuclear quadrupole couplings,
Section [10.11.4](../ch10_properties/sec_magnetman.md) (Eric Berquist, Daniel Lambrecht)
- Variational two-electron reduced-density-matrix (v2RDM) and v2RDM-driven complete active space self-consistent field (v2RDM-CASSCF)
method (Gergely Gidofalvi, Lauren Koulias, Wayne Mullinax, Eugene DePrince)
- Frozen and restrained potential energy scans, Section [9.6](../ch09_opt/sec_pes-scan.md) (Yihan Shao)
- Extended ESP charge fitting procedure to the computation of RESP charges (Yihan Shao)
