---
title: "1.3.14 New Features in Q-Chem 4.3"
---

## 1.3.14 New Features in **Q-Chem** 4.3

(July 4, 2026)

- •

Analytic derivative couplings (*i.e.*, nonadiabatic couplings) between electronic states
computed at the CIS, spin-flip CIS, TDDFT, and spin-flip TDDFT levels
(S. Fatehi, Q. Ou, J. E. Subotnik, X. Zhang, J. M. Herbert); Section [9.8](../ch09_opt/topic_namd.md).
- •

A third-generation (“+D3”) dispersion potential for XSAPT
(K. U. Lao, J. M. Herbert); Section [12.10](../ch12_frag/sect_XSAPT.md).
- •

Non-equilibrium PCM for computing vertical excitation energies (at the TDDFT level) and ionization energies in solution
(Z.-Q. You, J. M. Herbert); Section [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM).
- •

Spin-orbit couplings between electronic states for CC and EOM-CC wave functions
(E. Epifanovsky, J. Gauss, A. I. Krylov); Section [7.9.21.4](../ch07_excited/sec_EOMGRAD.md#sec:EOMSOC).
- •

PARI-K method for evaluation of exact exchange, which affords dramatic speed-ups for triple-$\zeta$ and larger basis sets
in hybrid DFT calculations (S. Manzer, M. Head-Gordon).
- •

Transition moments and cross sections for two-photon absorption using EOM-CC wave functions
(K. Nanda, A. I. Krylov); Section [7.9.21.6](../ch07_excited/sec_EOMGRAD.md#sec:2PA).
- •

New excited-state analysis for ADC and CC/EOM-CC methods (M. Wormit); Section [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md)).
- •

New Dyson orbital code for EOM-IP-CCSD and EOM-EA-CCSD (A. Gunina and A. I. Krylov; Section [7.9.29](../ch07_excited/topic_dyson.md)).
- •

Transition moments, state dipole moments, and Dyson orbitals for CAP-EOM-CCSD (T.-C. Jagau and A. I. Krylov;
Sections [7.9.10](../ch07_excited/sub_cc_cs_cap.md) and [7.9.29](../ch07_excited/topic_dyson.md)).
- •

TAO-DFT: Thermally-assisted-occupation density functional theory (J.-D. Chai; Section [5.12.3](../ch05_dft/ex_ptao.md)).
- •

MP2[V], a dual basis method that approximates the MP2 energy (J. Deng and A. Gilbert).
- •

Iterative Hirshfeld population analysis for charged systems, and CM5 semi-empirical charge scheme
(K. U. Lao and J. M. Herbert; Section [10.2.2](../ch10_properties/subsec_pop_anal.md)).
- •

New DFT functionals: (Section [5.3](../ch05_dft/sect_XCfuncs.md)):

- **–**

Long-range corrected functionals with empirical dispersion-: $\omega$M05-D, $\omega$B97X-D3 and $\omega$M06-D3
(Y.-S. Lin, K. Hui, and J.-D. Chai.
- **–**

PBE0_DH and PBE0_2 double-hybrid functionals (K. Hui and J.-D. Chai; Section [5.9](../ch05_dft/subsec_dhdft.md)).
- **–**

AK13 (K. Hui and J.-D. Chai).
- **–**

LFAs asymptotic correction scheme (P.-T. Fang and J.-D. Chai).
- •

LDA/GGA fundamental gap using a frozen-orbital approximation
(K. Hui and J.-D. Chai; Section [5.12.2](../ch05_dft/sect_foaDD.md)).
