---
title: "1.3.2 New Features in Q-Chem 7.0"
---

## 1.3.2 New Features in **Q-Chem** 7.0

(July 4, 2026)

## 1.3.2.1 Features in 7.0.0

- **Default and keyword changes:**

- Keywords for MRSF-TDDFT have been updated to align with SF-TDDFT (Arnab Chakraborty, Anna I. Krylov)

- MR_SPIN_FLIP and MRSF_DUMP have been removed
- SPIN_FLIP = 2 is now used to run an MRSF-TDDFT energy calculation
- STS_MOM = TRUE enables state-to-state transition moment calculations
- Change CC jobs to use Abelian subgroups by default (USE_ABELIAN_SUBGROUP = TRUE) (Tingting Zhao, Anna Krylov)
- Make two-step Cholesky decomposition the default for CC jobs (Tingting Zhao, Anna Krylov)
- Set the default of CD_TS_SPAN_FACTOR to $10^{-2}$ (Tingting Zhao, Anna Krylov)
- Updated the name of the OPSING keyword to SPIN_PROJ for clarity (John Herbert)
- Updated the proton/electron mass ratio in NEO calculations to use the most recent experimental values from NIST CODATA (1836.152673426, rather than 1836.15267389) (Jack Morgenstein, Sharon Hammes-Schiffer)
- Make SIMPLE initial Hessian the default for redundant internal coordinates in geometry optimizer (Kuan-Yu Liu)
- Change default MAX_SCF_CYCLES to 100 for calculations where SCF_CONVERGENCE>=8 (Kaushik Nanda)
- Change default MAX_SCF_CYCLES to 100 for robust SCF workflows (Kaushik Nanda)
- Default for SF-1eX2C has been switched from finite-difference to analytic energy (Xiao Liu, Sahand Adibnia, Martin Head-Gordon)
- **General features and improvements:**

- Unrestricted VCD (Kaushik Nanda)
- MPI improvements (Kaushik Nanda)
- wGDD: Print warning that omega is not reset for subsequent TDDFT job (John Herbert)
- Added improved SIMPLE initial Hessian to geometry optimizer (Kuan-Yu Liu)
- UHF/RHF/ROHF JK, J, K, RS_K, XC contributions to the Fock build with DIIS, GDM, and ROBUST algorithms are now libhpc enabled (Kaushik Nanda)
- **Density functional theory and self-consistent field:**

- Extended tight binding DFT (xtb) energy and gradient (Rebecca Tomann, Siyavash Moradi, Lucas de Kam, Christopher Stein, Martin Head-Gordon)
- New option for user to choose PT2 engine (MP2, RIMP2, or LMP2) for double hybrid DFT functionals; LMP2 provides scaling comparable to or better than DLPNO for double-hybrid DFT functionals (Yao Shen, Martin Head-Gordon)
- Semi-numerical K (Hartree-Fock exchange) for Hartree-Fock, range-separated functionals, and global hybrids (Jesse David DiCenso, Henryk Laqua, Martin Head-Gordon)
- Electronic circular dichroism (ECD) calculations for TDDFT (Xunkun Huang, Wan-Zhen Liang)
- The following DFT functionals are now available:

- COACH (Jiashu Liang, Martin Head-Gordon)
- CF22D (Jiashu Liang, Martin Head-Gordon)
- wB97M(OS) (Yao Shen, Martin Head-Gordon)
- XYG-OS5 (Yao Shen, Martin Head-Gordon)
- Density functional theory using complex absorbing potentials, for local density approximations, generalized gradient approximations and derived hybrids. (Charlotte Titeca, Yifan Jiang, Thomas-C. Jagau)
- The following complex-variable functionals are now available (Charlotte Titeca, Yifan Jiang, Thomas-C. Jagau)

- LDA: Slater X, VWN5 C, VWN1RPA C
- GGA: B88 X, PBE X, PBE C, LYP C
- Hybrid: all hybrid functionals composed of the above LDAs and GGAs and possibly exact HF exchange. This comprises (among others) PBE0, B3LYP and BH&HLYP.
- Density fitting (RI) improvements:

- Several performance improvements for J gradient and Hessian (Xintian Feng)
- Improved Fock XC performance via MO-based algorithm (Xintian Feng)
- JK gradient performance improvements (Xintian Feng)
- New SCF level NMR shielding feature with RI acceleration and MPI+OpenMP parallelization (Xiao Liu, Kaushik Nanda, Martin Head-Gordon)
- Analytic spin-free SF-1eX2C implementation for SCF level single point energy (Xiao Liu, Sahand Adibnia, Martin Head-Gordon)
- CAP/CBF RI-EA-CC2 implementation (Cansu Utku, Garrette Paran, Thomas Jagau)
- Implementation of new Faddeeva Finite Pulse Approximation (FFPA) method for photoionization cross-section calculations (Jason Yi, Martin Head-Gordon, C. William McCurdy)
- New FRZ MO guess for OO-DFT calculations (Nicola Bogo, Christopher J. Stein, Zeyi Zhang, Martin Head-Gordon)
- Implementation of BWs-ADC (Linus Dittmer, Adrian Dempwolff, Adrian Muller, Jonas Leitner, Andreas Dreuw)
- pTAO method for excitation energies within the TAO-DFT framework (Shaozhi Li, Jeng-Da Chai)
- Omega effective tuning for range separated hybrid functionals (Aditi Singh, Subrata Jana, Szymon Smiga, Prasanjit Samal)
- Print gradients of multiple TDDFT states (Pavel Pokhilko)
- Implementation of second moments of orbitals and densities (John Herbert)
- Improved HOMO-LUMO swap check in new DeltaSCF driver (Juanes Arias-Martinez)
- Add doublet (cation) calculations to DeltaSCF driver (Juanes Arias-Martinez)
- Enable different guesses for DeltaSCF driver (Juanes Arias-Martinez)
- Improved printing for new DeltaSCF driver (Juanes Arias-Martinez)
- **Resolved issues with:**

- Linear dependencies in DeltaSCF calculations (Juanes Arias-Martinez)
- Memory-related bug for rs-DFT frequency (Xintian Feng)
- Slowdown of DFT-based ROSCF calculations (Xintian Feng)
- Performance bug for unrestricted range-separated DFT stability analysis (Xintian Feng)
- Frequency calculations requested with MBD failed to do MBD part; they now correctly incorporate MBD using finite-difference (John Herbert)
- TDDFT NTO guess for unrestricted mixed state in new DeltaSCF driver (Juanes Arias-Martinez)
- Triplet SOMO printing in new DeltaSCF driver (Juanes Arias-Martinez)
- Memory-related crash in libfock-based JK routines when the given memory is very limited (Xintian Feng)
- Incompatibility of RI with solvent models (Xintian Feng)
- Incorrect results for DFT-D4 energy when using ghost atoms (Kuan-Yu Liu)
- Bug in printing moments of the excited-state densities (John Herbert)
- Job hanging when computing the shell radius with a loose threshold (Xintian Feng)
- **Correlated methods:**

- Numerical sparsity-based local MP2 (Zhenling Wang)
- Large speedups in RI-CC2 ground state code in libgmbpt (Hrishikesh Ram and Martin Head-Gordon)
- RI-CC2 and sRI-CC2 oscillator strengths (Chongxiao Zhao, Ruihao Bi, Qi Ou, Joohno Lee, Chenyang Li, Wenjie Dou)
- THC-sRI-CC2 properties (Chongxiao Zhao, Ruihao Bi, Qi Ou, Joohno Lee, Chenyang Li, Wenjie Dou)
- THC-sRI-CCSD ground and excited state energies (Chongxiao Zhao, Ruihao Bi, Qi Ou, Joohno Lee, Chenyang Li, Wenjie Dou)
- Added excited-state analysis for MRSF-TDDFT, including natural orbitals (NOs), natural transition orbitals (NTOs), natural difference orbitals (NDOs), and related descriptors through the libwfa framework (Arnab Chakraborty, Anna I. Krylov)
- Added new excited-state analysis features based on Earth Mover’s Distance: An accurate but more expensive transportation-simplex approach, and a faster but approximate Sinkhorn-distance approach (Zhe Wang, Martin Head-Gordon)
- MRSF-TDDFT now supports checkpoint file output for visualization (GUI = 2) and MOLDEN file generation (Arnab Chakraborty, Anna I. Krylov)
- One-Center Approximation method to calculate K-shell Auger widths using EOM-CCSD wave functions (Wojtek Skomorowski, Sonia Coriani)
- Optimized lambda equations for better performance in RI-CCSD, and RI-EOM-EE/EA/IP-CCSD (Tingting Zhao, Anna Krylov)
- Charge-displacement metrics in libwfa (John Herbert)
- CC2 and RI-CC2 Dyson orbitals for EA, IP, EE-EA, and EE-IP (3755, Mauro Gascon, Robin Moorby, Simen Camps, Tianyi Gao, Thomas Jagau)
- SOC implementation for MRSF-TDDFT (Arnab Chakraborty, Anna I. Krylov)
- Dipole and transition dipole moments with EOMEE/SF-CC2 (Simen Camps, Tianyi Gao, Mauro Gascón Navas, Thomas Jagau)
- **Resolved issues with:**

- CAS calculations skipping CAS when using old SCF driver (John Herbert)
- Error in calculation of nonorthogonal matrix elements in NOCIS/STEX (Rachel Patterson, Martin Head-Gordon)
- Error with Cholesky decomposition when using frozen core (Tingting Zhao, Anna Krylov)
- Job failure for single precision RI-CC2 calculations in CCMAN2 (Simen Camps, Thomas Jagau)
- **Incorporation of quantum nuclear effects (NEO suite):**

- Addition of electronic density fitting (RI-JK) to NEO-SCF for SPEs (Rowan Goudy, Sharon Hammes-Schiffer)
- Addition of NEO-AIMD methods for NEO-HF and NEO-DFT, including NEO Born-Oppenheimer MD (NEO-BOMD) and constrained NEO MD (CNEO-MD) (Joseph Dickinson, Sharon Hammes-Schiffer)
- Improved convergence for RPA when v_pp is off via updated initial guesses for NEO-TDDFT (Rowan Goudy, Scott M. Garner, Sharon Hammes-Schiffer)
- **Resolved issues with:**

- NEO-MRCI/NEO-CASSCF ignored NEO_ISOTOPE set in the input file, leading to incorrect results for deuterium and tritium containing systems (Jack Morgenstein, Sharon Hammes-Schiffer)
- Incorrect results for deuterium and tritium containing systems defined with NEO_ISOTOPE (Jack Morgenstein, Sharon Hammes-Schiffer)
- Segfaults in some NEO calculations using spherical functions of angular momentum 2 or higher in NEO basis (Rowan Goudy, Eno Paenurk, Sharon Hammes-Schiffer)
- Erroneous results for NEO Hessian calculations using the nuclear Hartree product representation when the nuclear basis set had linear dependencies (Eno Paenurk, Sharon Hammes-Schiffer)
- Erroneous results for NEO-SCF in certain cases when run with low memory (Rowan Goudy, Jack Morgenstein, Sharon Hammes-Schiffer)
- **Molecular dynamics, non-adiabatic dynamics, embedding, and solvation improvements:**

- Implemented pairwise harmonic confiner for optimization in internal coordinates (Chance Brandt, John Herbert)
- Added ability to change the non-additive exchange correlation functionals after supersystem SCF in projection-based embedding (Elena Kolodzeiski, Christopher Stein)
- Generalized, file-based external embedding interface enables interfacing to external packages like CP2K (Arnelle Fonlon, Kay Carter-Fenk, Dustin R. Broderick, Elena Kolodzeiski, John M. Herbert, Christopher J. Mundy)
- Significant speed up and parallelization of one-electron integrals in QM/EFP jobs provides an order of magnitude total speed up for large jobs (Lyudmila Slipchenko)
- Improved printout for QM/EFP provides essential information for debugging convergence issues (Lyudmila Slipchenko)
- Improved QM/MM functionality, including efficient constraints for QM/MM geometry optimization (Lyudmila Slipchenko)
- Resolved issues with harmonic confining jobs not opening properly in IQmol (Yuezhi Mao)
- **Fragment and energy decomposition analysis:**

- EDA OVOCV analysis and OODFT OVOCV analysis (Hengyuan Shen, Martin Head-Gordon)
- Added revised MBD parameters (MBDrev) for SAPT (Ka Un Lao, Corentin Villot)
- New MBD dispersion models for XSAPT+MBD (Keegan Paice, John Herbert)
