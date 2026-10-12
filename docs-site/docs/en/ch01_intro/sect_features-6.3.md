---
title: "1.3.4 New Features in Q-Chem 6.3"
---

## 1.3.4 New Features in **Q-Chem** 6.3

(July 4, 2026)

## 1.3.4.1 Features in 6.3.0

- **Changes to keywords and default behavior:**

- Use MDQ-uFERF as default for EDA2 jobs (EDA_UFERF = TRUE) (Hengyuan Shen, Abdulrahman Aldossary, Martin Head-Gordon)
- Add REM control option for fragment CPSCF max iterations (FRAG_CPSCF_MAXITER) (Yuezhi Mao)
- Change alpha in BW-s2 jobs to n/1000 rather than n/100 (Linus Dittmer, Nikolay V. Tkachenko, Martin Head-Gordon)
- Make O-V projection the default for basis2 calculations (BASISPROJTYPE = OVPROJECTION) (Kuan-Yu Liu)
- All NEO jobs will now use a tight initial guess by default (Mathew Chow, Sharon Hammes-Schiffer)
- Use nuclear core guess by default for NEO jobs with ghost atoms (Mathew Chow, Sharon Hammes-Schiffer)
- Use simultaneous SCF by default for NEO calculations (NEO_SIMULTANEOUS_SCF = TRUE) (Mathew Chow, Sharon Hammes-Schiffer)
- **General features and improvements:**

- MPI parallelization for finite-difference and many-body expansion calculations
- Added torsional and flat-bottom potential restraints for geometry optimizations (Chance W. Lander, Yihan Shao)
- Added bond stretch, r12pr34, angle, 1 to midpoint of 2 atoms, 1 to COM, and dihedral restraints to list of available restrained PES scan options (Chance W. Lander, Yihan Shao)
- Re-enabled NTOs for RPAs, corrected to use proper particle and hole density matrices (John Herbert)
- New mechanochemical pressure model using PV term energy correction (Felix Zeller)
- **Resolved issues with:**

- Hessian calculation rerun unnecessarily when GEOM_OPT_HESSIAN = READ in **Libopt3** (Yuezhi Mao)
- Remove bottlenecks in electronic JK gradient evaluation in libneo and librtneo (Mathew Chow, Sharon Hammes-Schiffer)
- Eliminate NaN values in Feshbach-Fano calculations for large, diffuse basis sets (Saikat Roy, Wojciech Skomorowski)
- Fix orbitals not being printed to .fchk file used by **IQmol** (Kuan-Yu Liu)
- Enable FAST_XAS crash with STATE_ANALYSIS = TRUE or GUI = 2 (Kaushik Nanda)
- Fix incompatibility of SCF_FINAL_PRINT and DC-DFT (John Herbert)
- Fix failure to conserve molecular point-group symmetry in **Libopt3** (Andrew Gilbert)
- Fix file error when calculating TS-VDW forces (John Herbert)
- **Density functional theory and self-consistent field:**

- New “Robust SCF” procedure provides more reliable SCF convergence via automated choice of algorithm and defaults (Kaushik Nanda)
- Performance enhancements for medium to large DFT calculations (Xintian Feng)
- Canonical ROHF/ROSCF (Adrian L. Dempwolff)
- Charge-transfer metrics for TDDFT (John Herbert)
- TDDFT-1D provides improved TDDFT/TDA where the crossing of S1/S0 states is smooth (Vishikh Athavale, Hung-Hsuan Teh, Joseph Subotnik)
- **Resolved issues with:**

- Crash of ALMO-CIS/TDA with large basis sets (Yuezhi Mao)
- DFT numerical quadrature consistency check not always performed (Xintian Feng)
- **Correlated methods:**

- EOM-CCSDT for EE, SF, IP, EA, DIP and DEA (Manisha, Prashant Uday Manohar)
- Added parallel performance to EOM-CCSDT (Manisha)
- Analytic gradients for EOM-DEA/DIP-CCSD methods (Tingting Zhao, Anna Krylov)
- SOC and $<S^{2}>$ calculations for EOM-DEA/DIP-CCSD methods (Tingting Zhao, Sai Kotaru, Sahil Gulania, Pavel Pokhilko, Anna Krylov)
- Automated calculations of Coulomb wave for caluclations of Auger rates within the Feshbach–Fano framework (Saikat Roi, Wojciech Skomorowski)
- Auger Channel Projection EOMIP-CCSD with frozen core and open shell references (Robin Moorby, Florian Matz, Thomas Jagau)
- Complex-valued RI-EOM-CCSD (Simen Camps, Cansu Utku, Thomas Jagau)
- EOM-(EE/SF)-CCSD dynamic polarizability for imaginary frequencies (Kaushik Nanda)
- Improved EOM-CC anisotropic polarizability formula (Kaushik Nanda)
- CC2 with size-consistent Brillouin–Wigner Partitioning (Linus Dittmer, Nikolay V. Tkachenko, Martin Head-Gordon)
- Maximum Physical Regularization for size-consistent Brillouin-Wigner Theory (Linus Dittmer, Nikolay V. Tkachenko, Martin Head-Gordon)
- BW-S2 performance improvements (Zhenling Wang, Martin Head-Gordon)
- Extend 1eX2C to calculate spin-orbit coupling components (Richard Kang, Martin Head-Gordon)
- New algorithm to accelerate 1C-NOCIS calculations using generalized non-orthogonal Slater-Condon rules (Rachel Lynn Patterson, Martin Head-Gordon)
- Implementation of coupling between Dyson orbitals and the continuum (plane wave) (Madhubani Mukherjee, Anna I. Krylov)
- Add a switch to control averaging in DO/PW coupling calculation (Madhubani Mukherjee, Anna I. Krylov)
- **Resolved issues with:**

- Coupled cluster PES scans erroneously reporting SCF energy (Kaushik Nanda)
- Convergence difficulties in DIP-EOM-CCSDT (Manisha)
- Crash due to memory allocation issues in Auger decay width calculations for certain basis sets (Saikat Roy, Wojciech Skomorowski)
- **Molecular dynamics, non-adiabatic dynamics, embedding, and solvation:**

- SAPT+PCM, dielectric boundaries for (X)SAPT calculations (John Herbert)
- Heterogeneous PCM allows users to modify the dielectric for each atom in PCM (John Herbert)
- Seminumerical frequency support for the SMD solvation model (John Herbert)
- Energy-based generalized many-body expansion (GMBE) implementation (Jake A. Tan, Francisco Ballesteros, Ka Un Lao)
- Density matrix-based generalized many-body expansion (GMBE) implementation (Jake A. Tan, Francisco Ballesteros, Ka Un Lao)
- Allow user-defined vdW radii for Poisson equation solver, PEqS (John Herbert)
- Enable user to explicitly set polarization screening factor in EFP (Kaushik Nanda)
- **Resolved issues with:**

- Many-body calculations with gradients fail with FILE_MO_COEFS error (Kaushik Nanda, Ryan Steele)
- Missing EFP polarization energy at every SCF step when USE_LIBQINTS = TRUE (Xintian Feng)
- Disabled NAC calculations with SMD (John Herbert)
- Printing spatial overlaps of occ-virt orbital pairs, SPATIAL_OVERLAP_ANALYSIS (John Herbert)
- **Fragment and energy decomposition analysis:**

- Broken bond orbitals (BBOs) (Alistair J. Sterling, Daniel S. Levine, Abdul Aldossary, Martin Head-Gordon)
- Enable ALMO(MSDFT) diabatic coupling calculation involving $\Delta$SCF excited states (Yuezhi Mao)
- Uncoupled FERF (Hengyuan Shen, Abdul Aldossary, Martin Head-Gordon)
- **Incorporation of quantum nuclear effects (NEO suite):**

- NEO-MCSCF (Christopher Malbon, Sharon Hammes-Schiffer)
- NEO-MRCI (Christopher Malbon, Sharon Hammes-Schiffer)
- NEO-PCM analytic Hessian for solution phase frequency and normal mode analysis (Mathew Chow, Sharon Hammes-Schiffer)
- External point charges are now supported for NEO electrostatic embedding calculations (Mathew Chow, Sharon Hammes-Schiffer)
- Enabled exchange-correlation functionals that have additional dispersion correction baked-in (e.g., wB97X-D, wB97X-D3, B3LYP-D3(BJ), etc.) to be used in NEO-DFT (Mathew Chow, Sharon Hammes-Schiffer)
- Added full DFT-D support for NEO (energies, gradients, Hessians) and RT-NEO (real-time and real-time-Ehrenfest) calculations (Mathew Chow, Sharon Hammes-Schiffer)
- Pseudopotentials are now fully supported with NEO (including energies, gradients, and Hessians) (Mathew Chow, Sharon Hammes-Schiffer)
- DIIS_GDM is now supported for the NEO simultaneous solver (Mathew Chow, Sharon Hammes-Schiffer)
- **Improved performance by:**

- Simultaneous GDM optimization for NEO-HF and NEO-DFT methods (Mathew Chow, Sharon Hammes-Schiffer)
- Nuclear SCF initial guess (Mathew Chow, Sharon Hammes-Schiffer)
- Generalized simultaneous DIIS and GDM optimization to treat ’N’ number of quantum protons to achieve faster NEO Hartree Product calculations (Mathew Chow, Sharon Hammes-Schiffer)
- Various improvements to simultaneous NEO-PCM calculations, including support with Hartree product and multiple proton CNEO Hessian calculations (Mathew Chow, Sharon Hammes-Schiffer)
- Updates and improvements to general orbital optimizer library (Christopher Malbon, Sharon Hammes-Schiffer)
- Performance improvements to CNEO Hessian calculations via addition of preconditioner (Eno Paenurk, Sharon Hammes-Schiffer)
- Improved stability and performance for NEO Hessian and CNEO Hessian codes (Mathew Chow, Sharon Hammes-Schiffer)
- **Resolved issues with:**

- Fixed issue where nuclear AUTOSAD would not read NEO_PURECART for child instructions (Mathew Chow, Sharon Hammes-Schiffer)
- Fixed issue where MAX_SCF_CYCLES did not have an effect on the simultaneous NEO-SCF solvers (Mathew Chow, Sharon Hammes-Schiffer)
- Fixed memory issue for calculations using NEO simultaneous SCF combined with NEO Hartree product (Mathew Chow, Sharon Hammes-Schiffer)

## 1.3.4.2 Features in 6.3.1

- **Changes to keywords and default behavior:**

- Removed rel2e section
- Added backstop for TD-DFT analysis tools that conflict with STATE_ANALYSIS (John Herbert)
- **General features and improvements:**

- Upgraded DFT-D4 to version 3.7.0
- Included energy and gradient for each step of harmonic confiner calculations (John Herbert)
- Improved output format (John Herbert, Yuezhi Mao)
- Resolved issues with HF-3c and PBEh-3c analytic frequencies (John Herbert)
- **Density functional theory and self-consistent field:**

- Added outer cavity correction to Gaussians on surface tesserae simulate hydrostatic pressure (GOSTSHYP) calculations (Felix Zeller, Nico Kissing, Tim Neudecker)
- Added adjustable max iteration in CIS-1D calculations (John Herbert)
- Added clean, consistent printout of energy components for double hybrids
- **Resolved issues with:**

- Incorrect results for double hybrid functionals
- Numerical issues with sr-PBE correlation functional (Abel Carreras, David Casanova)
- **Correlated methods:**

- Improved Green funtions integrals and Feshbach calculations (Saikat Roy, Wojciech Skomorowski)
- **Resolved issues with:**

- Segmentation fault in some CASSCF calculations
- RAS-CI calculations (Abel Carreras, David Casanova)
- Guess vector for triplet states in EOM-DEA/DIP-CCSD (Tingting Zhao, Anna Krylov)
- **Incorporation of quantum nuclear effects (NEO suite):**

- **Resolved issues with:**

- NEO TDDFT initial guess (Christopher Malbon, Sharon Hammes-Schiffer)
- SMD TS and a few other refinements to NEO calcuations (Mathew Chow, Sharon Hammes-Schiffer)
- NEO and CNEO Hessian when nuclear J-K terms is removed (Mathew Chow, Sharon Hammes-Schiffer)
- NEO-MRCI energies and NEO-CI calculations (Christopher Malbon, Sharon Hammes-Schiffer)
- **Fragment and energy decomposition analysis improvements:**

- Improved the ALMO-TDA calculations (Yuezhi Mao)
- Resolved issues with EDA calculations when CT is disabled (Markus Weiss)
