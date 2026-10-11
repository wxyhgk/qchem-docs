---
title: "1.3.9 New Features in Q-Chem 5.3"
---

## 1.3.9 New Features in **Q-Chem** 5.3

(July 4, 2026)

- •

**Changes in default settings:**

- **–**

Renamed rem variable ADIABATIC_CTA to VFB_CTA
- **–**

Changed ROHF_DIAG_SPEC default from 0 to 2 for ROHF and set
GEN_SCFMAN as default ROSCF engine
- •

**General improvements:**

- **–**

Added support for the jun-cc-pVDZ basis set (Kevin Carter-Fenk)
- •

**New features and improvements in the DFT suite:**

- **–**

TD-DFT analytic force and frequencies for meta-GGA density functionals
- **–**

Level shifting in DIIS for better SCF convergence in difficult cases (Section [4.5](../ch04_scf/sect_convergence.md))
- **–**

M06-SX density functional (Pierpaolo Morgante, Roberto Peverati)
- **–**

HF-3c method (Bhaskar Rana, John Herbert)
- •

**New features and improvements in the CC/EOM-CC package:**

- **–**

Calculation of RIXS and orbital analysis of RIXS transition moments (Kaushik Nanda, Anna Krylov; Section [7.9.9.1](../ch07_excited/sub_cvs_eom.md#sec:cvs_eom_rixs))
- **–**

New features in the CVS-EOM-CC suite (Marta Vidal, Sonia Coriani)
- **–**

Energies and properties for EOM-DEA-CCSD (Sahil Gulania, Maxim Ivanov, Anna Krylov; Section [7.9.8](../ch07_excited/sec_eomdea.md))
- **–**

Transition properties and $\langle\hat{S}^{2}\rangle$
for EOM-DIP-CCSD (Sahil Gulania, Wojciech Skomorowski, Anna Krylov)
- **–**

New NLO properties (hyperpolarizabilities) in EOM-CC (Kaushik Nanda, Anna Krylov)
- **–**

New tools for strongly correlated and magnetic systems: Extension of FNO to open-shell references
(Pavel Pokhilko, Anna Krylov; Section [7.9.14](../ch07_excited/sec_FNO.md))
- **–**

Construction of effective Hamiltonians from EOM-CC wave functions (Pavel Pokhilko, Anna Krylov; Section [13.6](../ch13_specialized/sec_EffHam.md))
- **–**

NTO analysis of spin-forbidden transitions (Pavel Pokhilko, Anna Krylov; Section [7.9.21.4](../ch07_excited/sec_EOMGRAD.md#sec:EOMSOC))
- **–**

Search for special points of complex PES (minima, MECP, and exceptional points) within CAP-EOM-CCSD (Zsuzsanna Koczor-Benda, Thomas Jagau)
- **–**

Voronoi CAP and projected CAP methods (James Gayvert, Ksenia Bravaya; Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md))
- **–**

Two-body Dyson orbitals for computing Auger decay rates and resonance lifetimes (Wojciech Skomorowski, Anna Krylov)
- **–**

Stability improvements in EOM-CC (Pavel Pokhilko, Anna Krylov)
- •

**New features and improvements in MP2 methods:**

- **–**

Geometry optimization with regularized orbital-optimized second-order Møller-Plesset perturbation theory ($\kappa$-OOMP2)
(Joonho Lee, Martin Head-Gordon; Section [6.6.6](../ch06_correlation/sec_oomp2.md))
- •

**New capabilities for intermolecular interactions:**

- **–**

Implementation of the XSAPT+MBD method (Kevin Carter-Fenk, John Herbert)
- •

**QM/MM improvements:**

- **–**

L-BFGS algorithm for geometry optimization (Bhaskar Rana, John Herbert)
- **–**

Harmonic confining potentials (Saswata Dasgupta, John Herbert)
- •

**New methods and capabilities:**

- **–**

Nuclear-electronic orbital DFT and TD-DFT methods (Fabian Pavosevic, Zhen Tao, Sharon Hammes-Schiffer)
- **–**

New module for RAS-SF methods (Shannon Houck, Nick Mayhall)
- **–**

A family of configuration-interaction methods: non-orthogonal configuration interaction singles (NOCIS), static exchange (STEX),
and one-center NOCIS (Katherine Oosterbaan, Martin Head-Gordon)
- **–**

Integral screening and resolution-of-the-identity capabilities for complex basis functions (Thomas Jagau)
- **–**

RI-MP2 method for complex basis functions (Mario Hernández Vera, Thomas Jagau; Section [6.6.10](../ch06_correlation/sec_cbf_rimp2.md))
- **–**

New method (concentric localization) for truncating the virtual space in projector-based embedding theory (Yuezhi Mao)
- **–**

Square gradient minimization for excited-state orbital optimization (Diptarka Hait, Martin Head-Gordon)
- **–**

Resonance Raman spectroscopy simulation (Saswata Dasgupta, John Herbert)
- **–**

Population analysis of antibonding orbitals (Abdulrahman Aldossary)
- **–**

Fragment-based diabatization schemes (Yuezhi Mao)
- **–**

Enabled ghost atoms without basis functions (Bushra Alam, John Herbert)
- **–**

Electron localization function (Bushra Alam, John Herbert
- **–**

New input options for wave function analysis (Felix Plasser)
- •

**New features in the BrianQC GPU module:**

- **–**

Extended support for GPU accelerated DFT exchange-correlation with support for LDA, GGA, and meta-GGA functionals
- **–**

Partially GPU accelerated DFT frequency calculations
