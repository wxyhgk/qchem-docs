---
title: "1.3.12 New Features in Q-Chem 5.0"
---

## 1.3.12 New Features in **Q-Chem** 5.0

(July 4, 2026)

- •

Enhancements to the coupled-cluster package:

- **–**

Analytic gradients for Cholesky-decomposed CCSD and EOM-CCSD;
efficiency improvement for canonical CCSD and EOM-CCSD gradients (Xintian Feng, Evgeny Epifanovsky).
- **–**

CAP-EOM-CCSD analytic gradients (Zsuzsanna Koczor-Benda, Thomas Jagau) and Dyson orbitals
for metastable states (Thomas Jagau, Anna Krylov),
Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md)).
- **–**

CAP-EOM-MP2 method (Alexander Kunitsa, Ksenia Bravaya).
- **–**

Evaluation of polarizabilities using CCSD and EOM-CCSD (EE and SF)
wave functions using full derivative formulation (Kaushik Nanda and Anna Krylov), Section [7.9.21.8](../ch07_excited/sec_EOMGRAD.md#sec:EOMpol)).
- **–**

Evaluation of $\langle\hat{S}^{2}\rangle$ for EOM-CCSD wave functions (Xintian Feng).
- **–**

Evaluation of NACs for EOM-CCSD wave functions (Shirin Faraji, Anna Krylov, Evgeny Epifanovsky, Xintian Feng), Section [7.9.21.5](../ch07_excited/sec_EOMGRAD.md#sec:EOMNAC)).
- **–**

Efficiency improvement and new multicore-parallel code for (T) correction (Ilya Kaliman).
- **–**

New coupled-cluster based methods for core states (Anna Krylov).
- •

New capabilities for implicit solvation modeling:

- **–**

Equilibrium PCM capabilities for computing vertical excitation, ionization,
and electron attachment energies at EOM-CC and MP2 levels (Section [11.2](../ch11_env/topic_solvation.md)).
- **–**

State-specific equilibrium and nonequilibrium solvation for all
orders and variants of ADC (Jan Mewes, Andreas Dreuw) , Section [7.10.11](../ch07_excited/topic_abs-adc.md).
- **–**

Poisson equation boundary conditions allowing use of an arbitrary, anisotropic dielectric function
$\varepsilon(\mathbf{r})$, with full treatment of volume
polarization (Marc Coons, John Herbert), Section [11.2.11](../ch11_env/sect_PEQS.md).
- **–**

Composite Model for Implicit Representation of Solvent (CMIRS), an accurate model for free energies of solvation
(Zhi-Qiang You, John Herbert), Section [11.2.7](../ch11_env/example_CMIRS-water.md).
- •

New density functionals (Narbe Mardirossian and Martin Head-Gordon), Section [5.3](../ch05_dft/sect_XCfuncs.md)):

- **–**

GGA functionals: BEEF-vdW, HLE16, KT1, KT2, KT3, rVV10
- **–**

Meta-GGA functionals: B97M-rV, BLOC, mBEEF, oTPSS, TM
- **–**

Hybrids: CAM-QTP(00), CAM-QTP(01), HSE-HJS, LC-$\omega$PBE08, MN15, rCAM-B3LYP, WC04, WP04
- **–**

Double hybrids: B2GP-PLYP, DSD-PBEB95-D3, DSD-PBEP86-D3,
DSD-PBEPBE-D3, LS1DH-PBE, PBE-QIDH, PTPSS-D3, PWPB95-D3
- **–**

Grimme’s PBEh-3c “low-cost” composite method
- **–**

rVV10 non-local correlation functional
- •

Additional DFT developments:

- **–**

New forms of DFT-D3 (J. Witte; Section [5.7.3](../ch05_dft/subsec_DFT-D.md)).
- **–**

New standard integration grids, SG-2 and SG-3
(Saswata Dasgupta, John Herbert), Section [5.5.3](../ch05_dft/sect_standard-quad.md).
- **–**

More efficient propagator algorithms for time-dependent
Kohn-Sham calculations, also known as “real-time” TDDFT
(Ying Zhu, John Herbert), Section [7.4](../ch07_excited/sec_TDKS.md)).
- •

New integral package for for computing effective core potential (ECP)
integrals (Simon McKenzie, Evgeny Epifanovsky), Section [8.10.2](../ch08_basis/sub_ECP-fit.md)).

- **–**

More efficient analytic algorithms for energies and first derivatives.
- **–**

Support for arbitrary projector angular momentum.
- **–**

Support up to $h$ angular momentum in the basis set.
- •

Analytic derivative couplings for the *ab initio* Frenkel-Davydov
exciton model (Adrian Morrison, John Herbert); Section [12.14](../ch12_frag/sect_AIFDEM.md)).
- •

New ALMO-based energy decomposition analysis (EDA) methods:

- **–**

The second-generation ALMO-EDA methods for DFT (Paul Horn, Yuezhi Mao, Martin Head-Gordon); Section [12.6](../ch12_frag/sect_eda2.md).
- **–**

The extension of ALMO-EDA to RIMP2 theory (Jonathan Thirman, Martin Head-Gordon); Section [12.7.1](../ch12_frag/sect_mp2_eda.md).
- **–**

The “adiabatic” EDA method for decomposing changes in molecular properties
(Yuezhi Mao, Paul Horn, Martin Head-Gordon); Section [12.7.3](../ch12_frag/sect_adiabatic_eda.md).
- •

Wave function correlation capabilities:

- **–**

Coupled cluster valence bond (CCVB) method for describing open-shell
molecules with strong spin correlations (David Small, Martin Head-Gordon); Section [6.19.3](../ch06_correlation/subsec_CCVB.md).
- **–**

Implementation of coupled-cluster valence bond with singles and
doubles (CCVB-SD) for closed-shell species (Joonho Lee, David Small, Martin Head-Gordon); Section [6.14.4](../ch06_correlation/topic_ccvb.md).

**Note: 

Several important changes in **Q-Chem**’s default settings have occurred since version 4.4.

•

Core electrons are now frozen by default in most post-Hartree-Fock
calculations; see Section [6.2](../ch06_correlation/sec_core.md).

•

The keywords for calculation of SOCs and NACs were renamed for
consistency between different methods.

•

Some newer density functionals now use either the SG-2 or
SG-3 quadrature grid by default, whereas all functionals used
SG-1 by default in v. 4.4. Table [5.3](../ch05_dft/sect_standard-quad.md#table:SG) lists the
default grid for various classes of functionals.

**
