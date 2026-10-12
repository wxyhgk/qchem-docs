---
title: "1.3.10 New Features in Q-Chem 5.2"
---

## 1.3.10 New Features in **Q-Chem** 5.2

(July 4, 2026)

- **Changes in default settings:**

- Single-node shared-memory parallelism becomes default and recommended for most jobs. New command line key *-mpi* is required to use distributed-memory MPI-parallel features (Section [2.2.1.1](../ch02_install/ssect_general-usage.md#sec:parallel)).
- Pure basis functions are used by default with BASIS = GEN.
- Default number of grid points in Lebedev grids in solvent models changed from 302 to 194 points (non-Hydrogen) and 110 points (Hydrogen) atoms.
- Use of SWIG charges for SM$x$ models.
- Input format for XPol, SAPT and XSAPT, and MBE jobs has changed.
- Use EDA2 as the default driver for ALMO-EDA.
- Frozen core approximation no longer applied by default in RAS-CI calculations.
- **General improvements:**

- Increased availability of basis sets: High angular momentum basis functions (up to k-functions) supported for most SCF, RI-MP2, CC, EOM-CC, ADC calculations.
- Streamlined input format for RI-SCF calculations.
- Added the def2- family of density fitted (RI) basis sets for SCF and post-SCF calculations (courtesy of Dr. Florian Weigend).
- On-the-fly generation for the superposition of atomic densities guess for SCF (Kevin Carter-Fenk, John Herbert).
- Reintroduction of legacy ECPs without fitting.
- Easy specification of basis sets on fragments, reading of basis sets from an external file (Zheng Pei and Yihan Shao).
- **Improvements to the DFT capabilities:**

- Support for analytic frequency calculations using meta-GGA density functionals (available only with shared-memory parallelism).
- Support for analytic frequency calculations using resolution-of-the-identity (density-fitted) Coulomb (available only with shared-memory parallelism).
- Improved performance of analytic partial Hessian calculations using DFT.
- New density functionals: revM06, revM11 (Pierpaolo Morgante and Roberto Peverati).
- **Improvements in implicit solvation models:**

- Revised PCM tessellation grids for improved performance (John Herbert).
- Improved performance of the general SCF program with SM$x$ solvation models (Yuezhi Mao).
- **New MP2 features:**

- Addition of regularized orbital-optimized second-order Møller-Plesset perturbation theory ($\kappa$-OOMP2)
(Joonho Lee, Martin Head-Gordon; Section [6.6.6](../ch06_correlation/sec_oomp2.md)).
- **Enhancements to the coupled-cluster package:**

- Mixed-precision CCSD and EOM-CCSD (Pavel Pokhilko, Evvgeny Epifanovsky, Anna Krylov,
with additional contributions from Ilya Kaliman, Kaushik Nanda, Marta Vidal, and Sonia Coriani; Sections [6.18](../ch06_correlation/sec_SP_CC.md) and [7.9.15](../ch07_excited/sec_SP_EOM_CC.md)).
- Damped response, dynamic polarizabilities for two-electron absorption using EOM-CC (Kaushik Nanda and Anna Krylov).
- Better handling of linear point groups in ADC and CC methods.
- Improved performance of disk-based ADC/CC algorithms.
- Projected and Voronoi CAP for CAP-EOM-CC/CC calculations (Ksenia Bravaya, Alexander Kunitsa; Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md)).
- Dynamic polarizabilities for CCSD and EOM-CCSD (Kaushik Nanda, Anna Krylov; Section [7.9.21.8](../ch07_excited/sec_EOMGRAD.md#sec:EOMpol)).
- Improved evaluation of spin-orbit coupling constants using EOM-CC wave functions (Pavel Pokhilko and Anna Krylov).
- New features for SOC calculation and analysis (Pavel Pokhilko, Anna Krylov; Section [7.9.21.4](../ch07_excited/sec_EOMGRAD.md#sec:EOMSOC)).
- Dyson orbitals for CVS-EOM-CCSD (Marta Vidal, Sonia Coriani, Anna Krylov; Section [7.9.9](../ch07_excited/sub_cvs_eom.md)).
- **Improvements in energy decomposition analysis methods:**

- Added electron density difference (EDD) plots and the ETS-NOCV analysis (Yuezhi Mao).
- Added support for PCM and SMD solvation models in ALMO-EDA (Yuezhi Mao).
- Resolved several issues that caused instabilities in MP2-EDA calculations (Yuezhi Mao).
- **New capabilities for explicit solvation modeling:**

- Polarizable Embedding (PE) Model
for ground-state and ADC calculations (Maximilian Scheurer; Section [11.8](../ch11_env/sect_PE_model.md)).
- **Other new methods and capabilities:**

- Incremental FCI method (Paul Zimmerman).
- Transition potential DFT for core-valence excitations.
- Analytic evaluation of Raman intensities (Zheng Pei and Yihan Shao).
