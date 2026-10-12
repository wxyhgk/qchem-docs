---
title: "1.3.18 New Features in Q-Chem 4.0"
---

## 1.3.18 New Features in **Q-Chem** 4.0

(July 4, 2026)

- New exchange-correlation functionals (Section [5.3](../ch05_dft/sect_XCfuncs.md)):

- Density-functional dispersion using Becke and Johnson’s XDM
model in an efficient, analytic form (Z. Gan, E. I. Proynov, and J. Kong; Section [5.7.4](../ch05_dft/sect_XDM.md)).
- Van der Waals density functionals vdW-DF-04 and vdW-DF-10
of Langreth and coworkers (O. Vydrov; Section [5.7.2](../ch05_dft/sect_VV10.md)).
- VV09 and VV10, new analytic dispersion functionals (O. Vydrov, T. Van Voorhis; Section [5.7.2](../ch05_dft/sect_VV10.md))
- DFT-D3 empirical dispersion methods for non-covalent interactions (S.-P. Mao and J.-D. Chai; Section [5.7.3](../ch05_dft/subsec_DFT-D.md)).
- $\omega$B97X-2, a double-hybrid functional based on the long-range corrected B97
functional, with improved accounting for medium- and long-range interactions
(J.-D. Chai and M. Head-Gordon; Section [5.9](../ch05_dft/subsec_dhdft.md)).
- XYGJ-OS, a double-hybrid functional for predictions of non-bonded
interactions and thermochemistry at nearly chemical accuracy (X. Xu, W. A. Goddard, and Y. Jung; Section [5.9](../ch05_dft/subsec_dhdft.md)).
- Short-range corrected functional for calculation of
near-edge x-ray absorption spectra (N. A. Besley; Section [7.12.2](../ch07_excited/subsec_TDDFT-Xray.md)).
- LB94 asymptotically-corrected exchange-correlation functional for TDDFT
(Y.-C. Su and J.-D. Chai; Section [5.10.2](../ch05_dft/sect_LB94.md)).
- Non-dynamical correlation in DFT with an efficient RI implementation of the Becke05 model in a fully analytic formulation
(E. I. Proynov, Y. Shao, F. Liu, and J. Kong; Section [5.3](../ch05_dft/sect_XCfuncs.md)).
- TPSS and its hybrid version TPSSh, and rPW86 (F. Liu and O. Vydrov).
- Double-hybrid functional B2PLYP-D (J.-D. Chai).
- Hyper-GGA functional MCY2 from Mori-Sánchez, Cohen, and Yang (F. Liu).
- SOGGA, SOGGA11 and SOGGA11-X family of GGA functionals (R. Peverati, Y. Zhao, and D. G. Truhlar).
- M08-HX and M08-SO suites of high HF exchange meta-GGA functionals (Y. Zhao and D. G. Truhlar).
- M11-L and M11 suites of meta-GGA functionals (R. Peverati, Y. Zhao, D. G. Truhlar).
- Improved DFT algorithms:

- Multi-resolution exchange-correlation (mrXC) for fast calculation of grid-based XC quadrature
(S. T. Brown, C.-M. Chang, and J. Kong; Section [5.5.5](../ch05_dft/sect_mrXC.md)).
- Efficient computation of the XC part of the dual basis DFT (Z. Gan and J. Kong; Section [4.4.5](../ch04_scf/sect_projection.md)).
- Fast DFT calculation with “triple jumps” between different sizes of basis
set and grid, and different levels of functional (J. Deng, A. T. B. Gilbert, and P. M. W. Gill; Section [4.8](../ch04_scf/sect_HFPC.md)).
- Faster DFT and HF calculation with an atomic resolution-of-identity
algorithm (A. Sodt and M. Head-Gordon; Section [4.6.6](../ch04_scf/sect_ri-DFT.md)).
- Post-Hartree–Fock methods:

- Significantly enhanced coupled-cluster code rewritten for better performance on multi-core architectures,
including energy and gradient calculations with CCSD and energy calculations with
EOM-EE/SF/IP/EA-CCSD, and CCSD(T) energy calculations
(E. Epifanovsky, M. Wormit, T. Kús, A. Landau, D. Zuev, K. Khistyaev, I. Kaliman, A. I. Krylov, and A. Dreuw;
Chaps. [6](../ch06_correlation/chap_correlation.md) and [7](../ch07_excited/chap_excited.md)).
- Fast and accurate coupled-cluster calculations with frozen natural orbitals
(A. Landau, D. Zuev, and A. I. Krylov; Section [6.15.1](../ch06_correlation/sec_FNOCC.md)).
- Correlated excited states with the perturbation-theory based, size-consistent ADC scheme
(M. Wormit and A. Dreuw; Section [7.10](../ch07_excited/sect_exadc.md)).
- Restricted active space, spin-flip method for multi-configurational ground states
and multi-electron excited states (P. M. Zimmerman, F. Bell, D. Casanova, and M. Head-Gordon; Section [7.2.3.2](../ch07_excited/Ch7.S2.SS3.md#topic:sf)).
- Post-Hartree–Fock methods for describing strong correlation:

- “Perfect quadruples” and “perfect hextuples” methods for strong
correlation problems (J. A. Parkhill and M. Head-Gordon; Section [6.14.5](../ch06_correlation/topic_lpcc.md)).
- Coupled-cluster valence bond (CCVB) methods for multiple-bond
breaking (D. W. Small, K. V. Lawler, and M. Head-Gordon; Section [6.19](../ch06_correlation/sect_pairing.md)).
- TDDFT for excited states:

- Nuclear gradients for TDDFT (Z. Gan, C.-P. Hsu, A. Dreuw, M. Head-Gordon, and J. Kong; Section [7.3.1](../ch07_excited/sect_tddftintro.md)).
- Direct coupling of charged states for study of charge transfer
reactions (Z.-Q. You and C.-P. Hsu; Section [10.15.2](../ch10_properties/topic_dc.md)).
- Analytical excited-state Hessian for TDDFT within the Tamm-Dancoff approximation
(J. Liu and W. Liang; Section [7.3.8](../ch07_excited/subsec_tddft-hessian.md)).
- Self-consistent excited-states with the maximum overlap method
(A. T. B. Gilbert, N. A. Besley, and P. M. W. Gill; Section [7.7.2](../ch07_excited/ex_OpSing.md)).
- Calculation of reactions via configuration interactions of charge-constrained states computed with constrained DFT
(Q. Wu, B. Kaduk and T. Van Voorhis; Section [5.11](../ch05_dft/topic_cdft.md)).
- Overlap analysis of the charge transfer in a TDDFT excited state
(N. A. Besley; Section [7.3.3](../ch07_excited/subsec_TRNSS.md)).
- Localizing diabatic states with Boys or Edmiston-Ruedenberg localization, for charge or energy transfer
(J. E Subotnik, R. P. Steele, N. Shenvi, and A. Sodt; Section [10.15.1.3](../ch10_properties/Ch10.S15.SS1.md#subsec:diabatic)).
- Non-collinear formalism for spin-flip TDDFT (Y. Shao, Y. A. Bernard, and A. I. Krylov; Section [7.3](../ch07_excited/sect_tddft.md))
- Solvation and condensed-phase modeling

- Smooth free energy surface for solvated molecules via SWIG-PCMs,
for QM and QM/MM calculations, including a linear-scaling QM/MM/PCM algorithm
(A. W. Lange and J. M. Herbert; Sections [11.2.3](../ch11_env/topic_pcm-em.md) and [11.2.5](../ch11_env/subsec_linear-PCM.md)).
- Klamt’s COSMO solvation model with DFT energy and gradient (Y. Shao; Section [11.2.8](../ch11_env/subsec_COSMO-Klamt.md)).
- Polarizable explicit solvent via EFP, for ground- and excited-state calculations at the
DFT/TDDFT and CCSD/EOM-CCSD levels, as well as CIS and CIS(D). A library of
effective fragments for common solvents is also available, along with energy and gradient for EFP–EFP calculations
(V. Vanovschi, D. Ghosh, I. Kaliman, D. Kosenkov, C. F. Williams, J. M. Herbert, M. S. Gordon, M. W. Schmidt, Y. Shao,
L. V. Slipchenko, and A. I. Krylov; Section [11.5](../ch11_env/sect_efp.md)).
- Optimizations, vibrations, and dynamics:

- “Freezing” and “growing” string methods for efficient automated reaction-path finding
(A. Behn, P. M. Zimmerman, A. T. Bell, and M. Head-Gordon; Section [9.3.2](../ch09_opt/sect_fstring.md)).
- Improved robustness of the intrinsic reaction coordinate (IRC)-following code (M. Head-Gordon).
- Quantum-mechanical treatment of nuclear motion at equilibrium via path integrals
(R. P. Steele; Section [9.10](../ch09_opt/sec_PIMC.md)).
- Calculation of local vibrational modes of interest with partial Hessian
vibrational analysis (N. A. Besley; Section [10.8.4](../ch10_properties/partial-hess.md)).
- Accelerated *ab initio* molecular dynamics MP2 and/or dual-basis methods, based on $Z$-vector extrapolation
(R. P. Steele; Section [4.7.3](../ch04_scf/subsec_dual-dyn.md)).
- Quasi-classical *ab initio* molecular dynamics
(D. S. Lambrecht and M. Head-Gordon; Section [9.9.6](../ch09_opt/subsec_QCT.md)).
- Fragment-based methods:

- Symmetry-adapted perturbation theory (SAPT) for computing and analyzing dimer interaction energies
(L. D. Jacobson, M. A. Rohrdanz, and J. M. Herbert; Section [12.9](../ch12_frag/topic_sapt.md)).
- Many-body generalization of SAPT (“XSAPT”), with empirical dispersion corrections for high accuracy and low
cost in large clusters (L. D. Jacobson, K. U. Lao, and J. M. Herbert; Section [12.10](../ch12_frag/sect_XSAPT.md)).
- Methods based on a truncated many-body expansion, including the fragment molecular orbital (FMO)
method (K. U. Lao and J. M. Herbert; Section [12.12](../ch12_frag/sec_MBE.md)).
- Properties and wave function analysis:

- Analysis of metal oxidation states via localized orbital bonding analysis
(A. J. W. Thom, E. J. Sundstrom, and M. Head-Gordon; Section [10.2.6](../ch10_properties/sect_LOBA.md)).
- Hirshfeld population analysis (S. Yeganeh; Section [10.2.2](../ch10_properties/subsec_pop_anal.md)).
- Visualization of non-covalent bonding using Johnson and Yang’s NCI algorithm (Y. Shao; Section [10.5.6](../ch10_properties/NCI-plots.md)).
- Electrostatic potential on a grid for transition densities (Y. Shao; Section [10.5.8](../ch10_properties/sec_ESP.md)).
- Support for modern computing platforms

- Efficient multi-threaded parallel performance for CC, EOM, and ADC methods.
- Better performance for multi-core systems with shared-memory parallel DFT and Hartree-Fock
(Z. Gan, Y. Shao, and J. Kong) and RI-MP2 (M. Goldey and M. Head-Gordon; Section [6.17](../ch06_correlation/CCparallel.md)).
- Accelerated RI-MP2 calculation on GPUs
(R. Olivares-Amaya, M. Watson, R. Edgar, L. Vogt, Y. Shao, and A. Aspuru-Guzik; Section [6.6.4](../ch06_correlation/sect_gpu-rimp2.md)).
- Graphical user interfaces (GUIs):

- Input file generation, **Q-Chem** job submission, and visualization
is supported by **IQmol**, a fully integrated GUI developed by
Andrew Gilbert. **IQmol** is a free software and does not require
purchasing a **Q-Chem** license. See
`http://www.iqmol.org` for details and installation instructions.
- Other graphical interfaces are also available, including
**MolDen**, **MacMolPlt**, and **Avogadro**
(Chapter [10](../ch10_properties/chap_properties.md) and elsewhere).
