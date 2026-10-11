---
title: "1.3.13 New Features in Q-Chem 4.4"
---

## 1.3.13 New Features in **Q-Chem** 4.4

(July 4, 2026)

- •

occ-RI-K algorithm for the evaluation of exact exchange in energy and force calculations
(S. Manzer, F. Rob, M. Head-Gordon); Section [4.6.8](../ch04_scf/subsec_occrik.md).
- •

Combinatorially-optimized exchange-correlation functionals
(N. Mardirossian, M. Head-Gordon); Section [5.3](../ch05_dft/sect_XCfuncs.md)):

- **–**

$\omega$B97M-V (range-separated hybrid, meta-GGA functional with VV10 non-local correlation)
- **–**

B97M-V (meta-GGA functional with VV10 non-local correlation)
- **–**

$\omega$B97X-V (range-separated hybrid functional with VV10 non-local correlation)
- •

Implementation of new exchange-correlation functionals from the literature (N. Mardirossian and M. Head-Gordon;
Section [5.3](../ch05_dft/sect_XCfuncs.md)). These include:

- **–**

MGGA_MS0, MGGA_MS1, MGGA_MS2, MGGA_MS2h, MGGA_MVS, MGGA_MVSh, PKZB, revTPSS, revTPSSh, SCAN, SCAN0,
PBEsol, revPBE, revPBE0
- **–**

N12, N12-SX, GAM, MN12-L, MN12-SX, MN15-L, dlDF
- **–**

VV10, LC-VV10
- **–**

B97-K, B97-D3(0), B97-3, $\tau$-HCTH, $\tau$-HCTHh
- **–**

SRC1-R1, SRC1-R2, SRC2-R1, SRC2-R2
- **–**

B1LYP, B1PW91, MPW1K, LRC-BOP, BHH, BB1K, PW6B95, PWB6K, B2PLYP
- •

Hessian-free minimum point verification (S. Sharada, M. Head-Gordon); Section [9.3.3](../ch09_opt/sect_approx_hess.md))
- •

Exciton-based excited-state models:

- **–**

*Ab initio* Frenkel-Davydov model for coupled excitations in multi-chromophore systems
(A. F. Morrison, J. M. Herbert); Section [12.14](../ch12_frag/sect_AIFDEM.md).
- **–**

TDDFT for molecular interactions [TDDFT(MI)], a set of local excitation
approximations for efficient TDDFT calculations in multi-chromophore systems and for single
chromophores in the presence of explicit solvent molecules
(J. Liu, J. M. Herbert); Section [12.15](../ch12_frag/sec_TDDFT_MI.md).
- •

Improvements to many-body and XSAPT methods (K. U. Lao, J. M. Herbert):

- **–**

MPI-parallelized many-body expansion with analytic gradient (Section [12.12](../ch12_frag/sec_MBE.md)).
- **–**

Efficient atomic orbital implementation of XSAPT for both closed- and open-shell systems
(Section [12.10.3](../ch12_frag/subsec_AO-XSAPT_KS_D.md)).
- •

Thermostats for *ab initio* molecular dynamics (R. P. Steele, J. M. Herbert).
- •

Analytic energy gradient for the Ewald summation in QM/MM calculations (Z. C. Holden, J. M. Herbert).
- •

Zeolite QM/MM methods (J. Gomes, M. Head-Gordon).
- •

EOM-MP2 methods for excitation, ionization and electron attachment energies
(A. Kunitsa, K. Bravaya); Section [7.9.5.1](../ch07_excited/Ch7.S9.SS5.md#sec:EOMMP2).
- •

Evaluation of polarizabilities using CCSD and EOM-CCSD wave functions
(K. Nanda, A. I. Krylov); Section [7.9.21.8](../ch07_excited/sec_EOMGRAD.md#sec:EOMpol).
- •

Distributed-memory parallel implementation of CC and EOM-CC methods
and performance improvements in disk-based algorithms (E. Epifanovsky, I. Kaliman, A. I. Krylov).
- •

Improvements to the maximum overlap method (MOM) for SCF calculations (A. T. B. Gilbert); Section [7.7.2](../ch07_excited/ex_OpSing.md).
- •

Non-equilibrium PCM method to describe solvent effects in ADC excited-state calculations
(J.-M. Mewes, A. Dreuw); Section [7.10.11](../ch07_excited/topic_abs-adc.md).
- •

Spin-flip ADC method (D. Lefrancois, A. Dreuw); Section [7.10.8](../ch07_excited/sect_SF-ADC.md).
