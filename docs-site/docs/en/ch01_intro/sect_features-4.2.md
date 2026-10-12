---
title: "1.3.15 New Features in Q-Chem 4.2"
---

## 1.3.15 New Features in **Q-Chem** 4.2

(July 4, 2026)

- Input file changes:

- New keyword METHOD simplifies input in most cases by
replacing the pair of keywords EXCHANGE and
CORRELATION (see Chapter [4](../ch04_scf/chap_scf.md)).
- Keywords for requesting excited-state calculations have been modified and simplified
(see Chapter [7](../ch07_excited/chap_excited.md) for details).
- Keywords for solvation models have been modified and simplified (see Section [11.2](../ch11_env/topic_solvation.md) for details).
- New features for NMR calculations including spin-spin couplings
(J. Kussmann, A. Luenser, and C. Ochsenfeld; Section [10.11.2](../ch10_properties/sec_magnetic_NMR.md)).
- New built-in basis sets (see Chapter [8](../ch08_basis/chap_basis.md)).
- New features and performance improvements in EOM-CC:

- EOM-CC methods extended to treat meta-stable electronic states (resonances)
via complex scaling and complex absorbing potentials (D. Zuev, T.-C. Jagau, Y. Shao, and A. I. Krylov; Section [7.9.10](../ch07_excited/sub_cc_cs_cap.md)).
- New features added to EOM-CC iterative solvers, such as methods for interior eigenvalues and user-specified guesses
(D. Zuev; Section [7.9.16](../ch07_excited/subsec_EOM-CC-diag.md))
- Multi-threaded parallel code for (EOM-)CC gradients and improved CCSD(T) performance.
- New features and performance improvements in ADC methods (M. Wormit, A. Dreuw):

- RI-ADC can tackle much larger systems at reduced cost (Section [7.10.4](../ch07_excited/sec_ADC_RI.md)).
- SOS-ADC methods (Section [7.10.5](../ch07_excited/sect_SOS-ADC.md)).
- State-to-state properties for ADC (Section [7.10.10](../ch07_excited/sect_ADC_prop.md)).
- SM12 implicit solvation model (A. V. Marenich, D. G. Truhlar, and Y. Shao; Section [11.2.9.1](../ch11_env/ex_SMx-User-Solvent.md#subsubsec:SM8)).
- Interface to NBO v. 6 (Section [10.3.1](../ch10_properties/sect_NBO.md)).
- Optimization of MECPs between electronic states at the SOS-CIS(D) and TDDFT levels
(X. Zhang and J. M. Herbert; Section [9.8.3](../ch09_opt/sect_MECP.md)).
- ROKS method for $\Delta$SCF calculations of excited states (T. Kowalczyk and T. Van Voorhis; Section [7.7.4](../ch07_excited/ex_ESROKS.md)).
- Fragment-based initial guess for SCF methods (Section [12.3](../ch12_frag/sect_FRAGMOguess.md)).
- Pseudo-fractional occupation number method for improved SCF convergence
in small-gap systems (D. S. Lambrecht; Section [4.5.6](../ch04_scf/sect_pFNO.md)).
- Density embedding scheme (B. J. Albrecht, E. Berquist, and D. S. Lambrecht; Section [11.6](../ch11_env/sect_den_emb.md)).
- New features and enhancements in fragment-based many-body expansion methods (K. U. Lao and J. M. Herbert):

- XSAPT(KS)+D:
A dispersion corrected version of symmetry-adapted perturbation theory for fast and accurate calculation of
interaction energies in non-covalent clusters (Section [12.10](../ch12_frag/sect_XSAPT.md)).
- Many-body expansion and fragment molecular orbital (FMO) methods for clusters (Section [12.12](../ch12_frag/sec_MBE.md)).
- Periodic boundary conditions with proper Ewald summation, for energies only (Z. C. Holden and J. M. Herbert;
Section [11.3](../ch11_env/sec_QMMM.md)).
