---
title: "1.3.7 New Features in Q-Chem 6.0"
---

## 1.3.7 New Features in **Q-Chem** 6.0

(July 4, 2026)

## 1.3.7.1 Features in 6.0.2

- **General features and improvements:**

- Enabled Molden support for the new default geometry optimizer
- Improved output for rxn path (IRC) calculations (John Herbert)
- Improved formatting of output for orbital radii of gyration (John Herbert)
- Improved error-catching for input section (John Herbert)
- Inlcuded one-electron matrices in fchk and archive
- Resolved pure and Cartesian assignment of nuclear-electronic orbital (NEO) basis (Mathew Chow, Sharon Hammes-Schiffer)
- Resolved issues with:

- AUTOSAD/I-Hirshfeld multiplicities for highly-charged transition metal atoms (Kevin Carter-Fenk)
- molden output for penalty function optimization
- calculations of the exact gradients and derivative couplings of CIS Boys diabatic states (Vishikh Athavale, Joseph Subotnik)
- immutable SOS_UFACTOR in SOS-CIS(D) calculations
- inconsistent charges and multipole moments in DUAL_BASIS_ENERGY calculations
- SCF_GUESS_MIX calculations with SAD guess (Yuezhi Mao)
- **Density functional theory and self-consistent field:**

- Improved algorithm for RI-JK derivatives
- **Correlated methods:**

- Enabled plotting of RAS-CI properties in cube, **MolDen**, and FChk files (Abel Carreras, David Casanova)
- **Molecular dynamics, non-adiabatic dynamics, embedding, and solvation:**

- Added printing of single-atom thermodynamic information for PCM jobs (John Herbert)
- **Fragment and energy decomposition analysis improvements:**

- Resolved issues with erroneous interaction energies with mixed basis sets for fragments (Yihan Shao, Yuezhi Mao)
- **Miscellaneous:**

- Added sample jobs for SCF_ALGORITHM options NEWTON_CG and NEWTON_MINRES (Yuezhi Mao)
- Added sample job for EDA2 calculation with external charges (Yuezhi Mao, Yihan Shao)
- Renamed sample jobs for variational PA/CTA based on GEN_SCFMAN_EDA2 (Yuezhi Mao, Hengyuan Shen)
- Added SOC-NTO analysis for TDDDFT and SF-TDDFT (Saikiran Kotaru, Anna Krylov)

## 1.3.7.2 Features in 6.0.1

- **General features and improvements:**

- Restored support for IGDESP used by CHARMM (John Herbert)
- Implemented a memory-efficient GOSTSHYP algorithm (Felix Zeller)
- Enabled finite-field chemical shielding and magnetizability calculations using gauge-independent atomic orbitals (GIAOs) for HF and MP2 (Jonathan Wong, Brad Ganoe, Tim Neudecker, Adam Rettig, Xiao Liu, Joonho Lee)
- Resolved issues with:

- molden output for optimization in **Libopt3**
- **Libopt3** Hessian calculations using PCM
- writing MO coefficients and energies to qarchive file
- cleaned up topology checking printing
- fixed printing of RMS of step size during geometry optimization
- **Molecular dynamics, non-adiabatic dynamics, embedding, and solvation improvements:**

- Implemented state-specific PCM with RAS-SF (Bushra Alam, Hanjie Jiang, John Herbert, Paul Zimmerman)
- **Fragment and energy decomposition analysis improvements:**

- Resolved issues with projection-based embedding calculations where frozen (environment) occupied orbitals are not ordered based on energies (Yuezhi Mao)
- **Miscellaneous:**

- Added comments to DFT SOC calculations for identifying the progress of the job (Saikiran Kotaru)
- Added warning about not having analytic Hessians for some optimization jobs
- Added printing to distinguish CPCM1 from CPCM2

## 1.3.7.3 Features in 6.0.0

- **Changes to default behavior:**

- Tightened default integral threshold (THRESH) to SCF_CONVERGENCE + 4 and used same threshold for DIIS and GDM
- Set default of FD_MAT_VEC_PROD to FALSE for VV10 functional (Yuezhi Mao)
- Turned off automatic evaluation of electrostatic potentils on a grid (Felix Plasser)
- Set finite difference as default for energy derivatives in electric field (Yuezhi Mao)
- **General features and improvements:**

- Next-generation interface of Q-Chem with external tools (generation of archive files in the HDF5 format)
- Implemented the nuclear-electronic orbital CCSD (NEO-CCSD) method (Fabijan Pavosevic, Sharon Hammes-Schiffer)
- Implemented NEO-TDDFT analytical gradient and Hessian (Zhen (Coraline) Tao, Patrick E. Schneider, Sharon Hammes-Schiffer)
- Enabled subset selection of atoms in NMR $J$-coupling calculations (JOBTYPE = ISSC)
via *$spin-spin* input section
- Disabled steepest descent in geometry optimization with fixed atoms
- Added delocalized natural internal coordinate optimization in new optimizer
- Updated geometry in the **MolDen** file for each step in finite difference optimizations (John Herbert)
- Stabilized density fitting for JK and MP2
- Set new optimizer as default for unconstrained optimization (GEOM_OPT_DRIVER = LIBOPT3)
- Added the minimal-augmented and heavy-augmented versions of the Karlsruhe basis sets (John Herbert)
- Removed MPI support
- Resolved issues with:

- incorrect Hirshfeld charges based on molecule input orders (Abdulrahman Aldossary)
- not-a-number (NAN) errors in SOC calculations
- missing nuclear repulsion energies in Fock projection (BASIS2) calculations
- removed restriction on number of atoms (MAX_ATOM) that can be included in random search and basin hopping
- ordering of localized MOs in formatted checkpoint files (Abdulrahman Aldossary)
- missing ECP for the def2-SVPD basis set
- failure to compute NMR properties with linearly dependent basis sets
- parsing input files with 100k+ lines
- character table of C3 point group
- **Density functional theory and self-consistent field:**

- Accelerated convergence of the SCF algorithm ADIIS and add a new combined algorithm option ADIIS_DIIS. (Yuezhi Mao)
- Enabled gauge-independent atomic orbitals (GIAOs) in SCF calculations using GEN_SCFMAN (Brad Ganoe, Tim Neudecker, Joonho Lee, Adam Rettig, Jonathan Wong)
- Disabled user setting of coefficients (via HFK_LR_COEF and HFK_SR_COEF),
if using built-in range-separated functionals
- Implemented frequency calculation and analytic Hessian for the VV10 functional (Jiashu Liang)
- Enabled generation of formatted checkpoint files in CIS/TDDFT calculations with frozen occupied/virtual orbitals via GUI = 2 (Yuezhi Mao)
- Enabled STATE_ANALYSIS for the new plot section (PLOT = 1) (Yuezhi Mao)
- Performed consistency check on TDKS Fock matrices based on the SCF convergence threshold
instead of the field amplitude (John Herbert)
- Added new energy density functionals: revSCAN, regSCAN, r++SCAN, r2SCAN, r4SCAN, TASK, mTASK, regTM, rregTM, revTM
- Enabled computing spin-orbit couplings (SOC) (1-electron and 2-electron mean-field) with TDDFT (both restricted and unrestricted) and spin-flip TDDFT (SF-TDDFT) (Saikiran Kotaru, Ana Krylov)
- Implemented analytic gradient for density-corrected DFT (DC-DFT) for self-interaction correction (Marc Coons, Bhaskar Rana, John Herbert)
- Resolved issues with:

- incorrect results of fractional electron SCF calculations using GEN_SCFMAN (Yuezhi Mao)
- hanging qints (USE_LIBQINTS = TRUE) jobs with large number of OpenMP threads
- non-variational initial SCF guess for ADIIS (Yuezhi Mao)
- incorrect memory estimation in TDDFT/TDA calculations
- crash of TDA excited state frequency jobs
- crash of geometry optimization with fixed atoms
- frequency calculations using basis functions with g or higher angular momenta
- sign error with TDDFT spin-orbit coupling calculations (Nicole Bellonzi)
- crash of projection-based embedding calculations (Yuezhi Mao)
- incorrect result of RPA TDDFT frequency using non-Pople basis set
- insufficient memory allocation for NMR calculations with meta-GGA functionals
- erroneous results in DC-DFT calculations using hybrid functionals with larger basis sets (Marc Coons, Bhaskar Rana, John Herbert)
- crash of excited state potential energy surface scans with CIS/TDDFT (John Herbert)
- **Correlated methods:**

- Implemented EOM oscillator strengths in velocity and mixed gauges (Josefine Andersen, Sonia Coriani)
- Implemented CCSD optical rotation evaluation (Josefine Andersen, Kaushik Nanda)
- Implemented the fragment charge difference (FCD) scheme in RASMAN2 (Chou-Hsun (Jeff) Yang, Aaditya Manjanath, Chao-Ping (Cherri) Hsu)
- Implemented complex-valued CC2, RI-CC2, and RI-CCSD (Cansu Utku, Garrette Paran, Thomas Jagau)
- Implemented the complex absorption potential (CAP) method in AIMD calculations (Jerryman A. Gyamfi, Thomas Jagau)
- Implemented the v2RDM-CASSCF-PDFT method using density fitted basis sets (Mohammad Mostafanejad, Run Li, A. Eugene DePrince III)
- Resolved formatting error in output of SOC calculation with RAS-CI method (Abel Carreras, David Casanova)
- **Molecular dynamics, non-adiabatic dynamics, embedding, and solvation:**

- Implemented projection-based embedding with complex basis functions (Valentina Parravicini, Thomas Jagau)
- Enabled user-defined permittivity grid for Poisson equation solver (PEqS) (Suranjan Paul)
- Improved PCM printing (John Herbert)
- Implemented CIS and TDDFT wave function overlaps including their spin-flip variants for (A)FSSH (Theta Chen, Junhan Chen, Zuxin Jin, Vishikh Athavale, Vale Cofer-Shabica, Joe Subotnik)
- Resolved issues with QM/MM optimzation not reading previous MOs as a guess for the next cycle
- **Fragment and energy decomposition analysis:**

- Implemented pairwise fragment excitation energy decomposition analysis (EDA) in QM/EFP calculations (Lyudmila Slipchenko)
- Increased the maximum angular momentum of basis functions to 5 for XSAPT calculations
- Implemented SPADE- and ALMO-based partitioning schemes for electric field calculations (Yuezhi Mao)
- Implemented a new MP2 EDA scheme and added a non-perturbative polarization analysis for DFT EDA (Kevin Ikeda, Hengyuan Shen)
- Enabled ALMO-CIS/TDA calculations with excitation amplitudes localized on one fragment (Yuezhi Mao)
- Enabled ALMO-CIS/TDA calculations with excitation from one fragment’s occupied orbitals to all virtuals in the system (Yuezhi Mao)
- Enabled ALMO-CIS/TDA calculations with excitation from one fragment’s occupied orbitals to another’s virtual orbitals (Yuezhi Mao)
- Enabled user-defined occupied-virtual pairs in ALMO-CIS/TDA calculations (Yuezhi Mao)
- Resolved miscellaneous issues with ALMO-CIS and excited-state ALMO-EDA calculations (Yuezhi Mao)
- **Miscellaneous:**

- Printed orbital kinetic energies using SCF_PRINT = 3
- Enabled EXTERNAL_CHARGES specification in an external file (Vale Cofer-Shabica, Joseph Subotnik)
- Added parameter check for many-body dispersion calculations (John Herbert)
- Restored finite difference for $\omega$B97M-2 and the XYG series of energy functionals
- Restored finite difference banner for SA-SF-RPA
