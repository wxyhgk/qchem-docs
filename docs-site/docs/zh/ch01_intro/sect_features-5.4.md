---
title: "1.3.8 New Features in Q-Chem 5.4"
---

## 1.3.8 New Features in **Q-Chem** 5.4

(July 4, 2026)

## 1.3.8.1 Features in 5.4.2

- •

**Changes to default behavior:**

- **–**

Made default SCF convergence criterion for supersystem and fragment jobs in EDA and BSSE calculations consistent (Yuezhi Mao)
- •

**General features and improvements:**

- **–**

Enabled mixed basis for AUTOSAD guess (Kevin Carter-Fenk, Yuezhi Mao, John Herbert)
- **–**

Enabled compatibility with the NBO7 program (John Herbert)
- **–**

Implementation of intrinsic bond orbital (IBO) analysis (Alexander Zech, Christopher Stein, Abdulrahman Aldossary, Martin Head-Gordon)
- **–**

Resolved issues with:

- *

frequency job failure when number of threads is thrice larger than number of atoms
- *

frequency job failure when CPSCF segments are equal to number of atoms
- *

incorrect alpha density generated when using new plots section format
- •

**Density functional theory and self-consistent field:**

- **–**

Enabled analytic Hessian for TPPS/TM/SCAN TDDFT calculations
- **–**

Added printing of information about memory requirements for TDDFT (John Herbert)
- **–**

Added an experimental implementation of the X2C method for relativistic quantum chemistry (Diptarka Hait, Leonardo Cunha, Richard Kang, Martin Head-Gordon)
- **–**

Improved CIS/TDA/RPA guess to avoid missing roots
- **–**

Implementation of projection-based embedding with complex basis functions (Valentina Parravicini, Thomas Jagau)
- **–**

Improved performance of the GOSTSHYP method through integral screening (Felix Zeller, Tim Neudecker, Eric Berquist)
- **–**

Resolved issues with:

- *

AIFDEM crash when a larger fragment is listed first
- *

NAN in SCF energies using VV10 functionals
- *

unrestricted RPA TDDFT analytic Hessian for singlet excited state
- *

failure to compute non-adiabatic couplings (NACs) using pure TDDFT
- *

incorrect TDDFT energies with FAST_XAS using multiple threads
- *

incorrect results from projection-based embedding using LRC-DFT as the low-level theory (Yuezhi Mao)
- *

incompletely converged energies in RPA calculations
- *

failure to evaluate spin-orbit integrals in TDDFT SOC calculations
- *

GPU acceleration of unrestricted pure DFT gradient when using BrianQC
- *

incorrect ROHF gradient when using BrianQC
- •

**Correlated methods:**

- **–**

Implementation of CCSD damped polarizability and first hyperpolarizability (Kaushik Nanda)
- **–**

Resolved issues with:

- *

wrongfully activated ECD properties with EOM-IP-CCSD (Josefine Andersen, Sonia Coriani)
- *

convergence issues in EOM-DIP and EOM-DEA methods
- *

symmetry check for v2RDM (Rain Li, Eugene DePrince)
- *

failure to write ASCI energy to checkpoint files
- •

**Molecular dynamics:**

- **–**

Enabled the use of new SCF drivers (GEN_SCFMAN = TRUE) in path integral MD
- **–**

Resolved issues with:

- *

missing energy-component file for AIMD when GEN_SCFMAN=TRUE
- •

**Fragment and energy decomposition analysis:**

- **–**

When EDA2_MOM is used with EDA_BSSE,
apply IMOM to BSSE calculations with ghost atoms to prevent collapsing to the lower-energy states (Yuezhi Mao)
- **–**

Allowed SCFMI_MOM and EDA2_MOM to preserve the electronic configuration of the frozen state (Yuezhi Mao)
- **–**

Multiple stability improvements in ALMO-EDA (Yuezhi Mao)
- **–**

Implemented non-perturbative CT analysis for ALMO-EDA (Hengyuan Shen, Srimukh Prasad, Martin Head-Gordon)
- **–**

Resolved issues with:

- *

final print of the one-side CT energy in VFB CT analysis incorrectly contained the contribution from SMD’s CDS (non-electrostatic) term, when using the SMD solvent model (Yuezhi Mao)
- *

double-counting of environment frozen core orbitals with default N_FROZEN_CORE setting for projection-based embedding (Yuezhi Mao)
- *

display of preparation energy for ALMO-EDA (Yuezhi Mao)
- *

many-body expansion (MBE) geometry optimization (John Herbert)
- *

convergence of linear solvers for orthogonal frozen decomposition (Yuezhi Mao)
- *

the dispersion term in classic frozen decomposition in non-*Aufbau* ALMO-EDA (Yuezhi Mao)
- •

**Miscellaneous:**

- **–**

Disabled analytic force calculation with projection-based embedding (Yuezhi Mao)
- **–**

Disabled complex SCF for fragment jobs (Yuezhi Mao)
- **–**

Resolved issue with NAN printing `efield` file for in QM/MM calculations when external charges are set to zero
- **–**

Added warning that CDFT does not support algorithms other than DIIS and RCA (Yuezhi Mao)
- **–**

Added warning when 3c methods are used without recommended basis sets (John Herbert)
- **–**

Added NBO version number in output (John Herbert)
- **–**

Fixed minor spelling errors in the printing of TDDFT (Bushra Alam, John Herbert)

## 1.3.8.2 Features in 5.4.1

- •

**Changes to default behavior:**

- **–**

Renamed Onsanger SOLVENT_METHOD to Kirkwood (John Herbert)
- **–**

Updated the SM8 solvation model to use Cartesian Gaussians (PURCAR = 2222) (John Herbert)
- **–**

Renamed spin-specific keywords to EA_ALPHA, EA_BETA, IP_ALPHA and IP_BETA (Wojtek Skomorowski)
- •

**General features and improvements:**

- **–**

Added Intrinsic Atomic Orbitals (IAO) and Intrinsic Bond Orbitals (IBO) (Abdulrahman Aldossary, Alexander Zech, Christopher Stein)
- **–**

Added a new localization method, Oxidation State Localized Orbitals (OSLO) (Abdulrahman Aldossary, Alexander Zech, Christopher Stein)
- **–**

Included installation of Romberg utilities
- •

**Density functional theory and self-consistent field:**

- **–**

Implemented hybrid functionals for TAO-DFT (Jeng-Da Chai)
- **–**

Improved efficiency of range-separated DFT frequency calculations when run in parallel with shared memory and multithreading
- **–**

Added option to turn off ground-state PCM calculations for TDDFT (John Herbert)
- **–**

Added option to enforce level shifting in every SCF cycle for state-targeted energy projection (STEP) (Kevin Carter-Fenk)
- **–**

Implemented projection-based embedding for unrestricted calculations (Yuezhi Mao)
- **–**

Added printing of more digits for the TDDFT transition strength
- **–**

Improved SCF guess for optimization jobs using BASIS2
- **–**

Resolved issues with:

- *

segmentation fault in CIS frequency calculations when using libqints
- *

index out of bounds error with TDKS sample in manual (Hung-Yi Tsai, Jeng-Da Chai)
- *

errors in unrestricted TDDFT Hessian calculations
- *

small error in RPA excitation energies
- *

incorrect SCF energy with libqints-based SRC-DFT
- *

crash when computing numerical derivatives with BASIS = GEN
- *

crash while running large frequency jobs due to insufficient memory in CPSCF
- *

incorrect evaluation of iterative Hirshfeld charges (Abdulrahman Aldossary)
- •

**Correlated methods:**

- **–**

Added options for custom scaling in complex basis function calculations (Florian Matz, Thomas Jagau)
- **–**

Improved projected CAP-EOM-CC (James Gayvert)
- **–**

Implemented EOM-DEA-CCSD two-photon absorption (Kaushik Nanda, Sahil Gulania, Anna Krylov)
- **–**

Implemented complex-valued CC2 and RI-CCSD (Cansu Utku, Garrette Pauley Paran, Thomas Jagau)
- **–**

Implemented effective nuclear charge approximation for SOCs using EOM (Saikiran Kotaru, Anna Krylov)
- **–**

Resolved issues with:

- *

freezing string method (FSM) reading SCF energy instead of correlated energy value
- *

missing triples corrections for EOM calculations in ccman2 (Pavel Pokhilko)
- *

using frozen core and virtual orbitals in projector-based embedding calculations (Yuezhi Mao)
- •

**Large systems, QM/MM, and solvation:**

- **–**

Implemented user-defined permittivity grid for Poisson equation solver (PEqS) (Suranjan Kumar Paul)
- **–**

Enabled SCRF for GEN_SCFMAN-based ROHF/ROKS calculations (Yuezhi Mao)
- **–**

Implemented state-specific PCM/TDDFT (SS-PCM/TDDFT) method based on the constrained equilibrium theory (Haisheng Ren, Fan Wang, Xiangyuan Li, Yingli Su)
- **–**

Improved GROMACS QM/MM interface (Vale Cofer-Shabica)
- **–**

Improved gradient performance of the SM8 solvation model (John Herbert)
- **–**

Improved memory usage of the SM8 solvation model (John Herbert)
- **–**

Added TDDFT_LR_PCM to control linear-response solvent correction (John Herbert)
- •

**Fragment and energy decomposition analysis:**

- **–**

Enabled the linearized approximation in projection-based embedding (Yuezhi Mao)
- **–**

Implemented POD2L and POD2GS for projection operator diabatization (POD) (Yuezhi Mao)
- **–**

Enabled calculation of couplings between multiple pairs of diabatic orbitals for POD (Yuezhi Mao)
- **–**

Added printing of separate energy components in the SAPT output (John Herbert)

## 1.3.8.3 Features in 5.4.0

- •

**Changes to default behavior:**

- **–**

Use of automatically generated superposition of atomic densities SCF guess for custom basis sets (Yuezhi Mao, Kevin Carter-Fenk)
- **–**

Use atomic size-corrected Becke weights for CDFT (Kevin Carter-Fenk)
- •

**General features and improvements:**

- **–**

New methods to distort molecules using force and pressure: HCFF, X-HCFF, GOSTSHYP (Tim Stauch, Maximilian Scheurer)
- **–**

Overhauled library of standard basis sets for consistency with Basis Set Exchange and extended support through element 118
- **–**

Improved stability of ECP fitting and updated definitions of fitted ECPs (CRENBS, CRENBL, HWMB, LACVP, LANL2DZ, SBKJC)
- **–**

Evaluation of electric field at nuclei (Yuezhi Mao)
- **–**

Frequency calculations for rigid fixed-atom constraints (Saswata Dasgupta)
- **–**

Save additional calculation output files to unique folder
- **–**

Resolved issues with:

- *

inconsistent application of quadrupole field to resolve orbital degeneracies
- *

definition of jun-cc-pVDZ basis set (John Herbert)
- *

some jobs crashing with the FILE_SET_SYM_REP read error
- *

cleaning up in PES scan jobs on Windows
- *

unnecessary gradient evaluation at every point of frozen PES scan
- •

**Features and improvements in density functional theory and self-consistent field:**

- **–**

TAO-DFT for global hybrid GGAs (Jeng-Da Chai)
- **–**

Vibronic and resonance Raman spectroscopy (Xunkun Huang, Huili Ma, WanZhen Liang)
- **–**

Integrated DFT-D4 empirical dispersion model (Kuan-Yu Liu, Romit Chakraborty)
- **–**

New implementation of direct propagation of the time-dependent Kohn-Sham equation (real-time TDKS) with support for unrestricted SCF and implicit solvation (Ying Zhu, John Herbert)
- **–**

State-targeted energy projection method (Kevin Carter-Fenk, John Herbert)
- **–**

Multiple improvements to frozen-density embedding methods (Cristina Gonzalez-Espinoza, Alexander Zech, Tomasz A. Wesolowski)
- **–**

Faster algorithm for $\omega$GDD tuning (John Herbert)
- **–**

Faster algorithm for $\omega$EFF tuning (Aditi Singh, Subrata Jana and Szymon Śmiga)
- **–**

Improvements in the IP/EA omega tuning scripts for long range corrected functionals (John Herbert)
- **–**

Support for high angular momentum in DFT frequency calculations
- **–**

Superposition of atomic potentials (SAP) guess for SCF (Yu Zhang, Susi Lehtola)
- **–**

Expand density functionals available for NMR chemical shift calculations (Jiashu Liang, Khadiza Begam, Barry Dunietz, Yihan Shao)
- **–**

Nuclear gradient and analytical 2nd functional derivative of the VV10 functional (Jiashu Liang)
- **–**

Performance improvements in the evaluation of DFT-D3 nuclear hessian contribution
- **–**

Consistent constrained DFT and SCF convergence criteria (Kevin Carter-Fenk)
- **–**

NVIDIA GPU computing improvements via interface with BrianQC:

- *

Accelerated force and vibrational frequency computations with range-separated functionals
- *

Accelerated Fock derivative computation in DFT vibrational frequency jobs
- **–**

Resolved issues with:

- *

buffer overflow in a special case of very large DFT jobs
- *

a special case of crashing unrestricted CIS derivative coupling calculations
- *

evaluation of finite-difference nonlocal correlation orbital Hessian (Yuezhi Mao)
- *

use of AO integrals in general response module
- *

differences in DFT quadrature between Linux and macOS
- *

using ghost atoms in MBD-vdW calculations (Kevin Carter-Fenk, Evgeny Epifanovsky)
- *

using arbitrary density functionals for MBD-vdW and TS-vdW
- *

crashing large CIS state following calculations
- *

SOC constants with unrestricted TDDFT
- *

RI-J/RI-K gradient
- *

DFT hyperpolarizabilities
- •

**Features and improvements in correlated methods:**

- **–**

Calculation of electronic $g$-tensors with CCSD (Sven Kähler, Anna Krylov);
- **–**

Calculation of electronic circular dichroism (ECD) using EOM-CC (Josefine Andersen, Sonia Coriani)
- **–**

Evaluation of spin-orbit couplings using CVS-EOM methods, L-edge XAS/XES spectroscopy calculations (Marta Vidal, Pavel Pokhilko, Sonia Coriani)
- **–**

Feshbach method with EOM-CC states and Coulomb wave expanded in terms of plane wave Gaussian type orbitals (Wojciech Skomorowski)
- **–**

Improved performance in small to medium CC/EOM jobs via in-core computations
- **–**

Improvements in projected CAP EOM-CC (James Gayvert)
- **–**

IP/EA-ADC methods and intermediate state representation (ISR) properties (Adrian Dempwolff, Matthias Schneider, Alexander Paul)
- **–**

Dramatic speedup of ADC(3) (Adrian Dempwolff)
- **–**

Improved fourth-order static self-energy for all ADC variants (PP (EE), IP, EA) (Adrian Dempwolff)
- **–**

Subspace-projected CAP-ADC for all ADC variants (PP (EE), IP, EA) (Adrian Dempwolff)
- **–**

Evaluation of spin-orbit couplings using RAS-CI and RAS2-SF methods (Abel Carreras, Anna Krylov, David Casanova, Hanjie Jiang, Pavel Pokhilko, Paul M. Zimmerman)
- **–**

Use of resolution-of-the-identity integrals in LibRASSF-based implementation of RAS-SF (Shannon Houck)
- **–**

Implementation of the Bloch effective Hamiltonian approach within LibRASSF-based RAS-SF (Shannon Houck)
- **–**

Experimental implementation of the CC2 and RI-CC2 methods (Garrette Paran, Thomas Jagau)
- **–**

Implementation of the Brueckner CC2 method (Adam Rettig)
- **–**

Implementation of direct RPA for the ground state correlation energy (Joonho Lee)
- **–**

Cubic storage RI-MP3 and Laplace-transformed RI-MP2 and RI-MP3 (Joonho Lee)
- **–**

Added access to $\kappa$-regularized orbital optimized MP2 via METHOD = KOOMP2
- **–**

New implementation of v2RDM and v2RDM-CASSCF solvers (Rain Li, Wayne Mullinax, Eugene DePrince, Marcus Liebenthal)
- **–**

Improved defaults in incremental FCI (Alan Rask)
- **–**

Experimental implementation of tensor hypercontraction methods (Joonho Lee)
- **–**

Resolved issues with:

- *

2 GB limit on temporary files in CC/EOM/ADC calculations on Windows
- *

evaluation of analytic gradients of $\kappa$-regularized OO-MP2
- *

crashing in fragment excitation difference (FED) calculations due to insufficient memory (Aaditya Manjanath)
- *

crashing in large RI-MP2 calculations
- *

initial guess in EOM-DIP-CCSD calculations
- *

crashing in large RI-CCSD calculations
- •

**Features and improvements in molecular dynamics:**

- **–**

New AIMD variable (AIMD_INIT_VELOC_NANO_RANDOM) for better random seeds (Tarek Scheele)
- **–**

Resolved issues with:

- *

activating vibrational spectra computation in special cases
- •

**Features and improvements for large systems, QM/MM, and solvation:**

- **–**

AIRBED: A simplified density functional theory model for physisorption on surfaces (Nick Besley, Stephen Mason)
- **–**

Resolved issues with:

- *

SM12 crashes with general basis set (Yuezhi Mao)
- *

MM finite difference force calculations
- *

printing of EFG principal components
- *

SM12 gradient
- *

implicit solvation in SCF and DFT response property calculations
- *

requiring explicit derivative level to be set for IEF-PCM frequencies (John Herbert)
- *

RI-MP2 + PCM jobs
- *

out-of-memory error in large SMD jobs
- •

**Features and improvements for fragment and energy decomposition analysis methods:**

- **–**

Enable geometry optimization on POL and VFB-CT surfaces in the presence of solvent (Yuezhi Mao)
- **–**

Enable ALMO-EDA for systems with non-*Aufbau* electronic configurations (Yuezhi Mao)
- **–**

Enable the separation of electrostatic and non-electrostatic terms in SMD solvation energy (Yuezhi Mao)
- **–**

Improve error message when attempting ROHF-based SCFMI and EDA
- **–**

Improve error message when attempting to use unsupported solvent models with SCFMI and EDA
- **–**

Control number of subspace vectors and convergence threshold in SAPT CPSCF (Kevin Carter-Fenk)
- **–**

Improved SAPT+aiD$x$ and SAPT+MBD keywords (Kevin Carter-Fenk)
- **–**

Resolved issues with:

- *

crashing during large projection-based embedding calculations (Yuezhi Mao)
- *

requiring explicit derivative level to be set for adiabatic EDA geometries and frequencies (Yuezhi Mao)
- *

interoperability between SAPT features and various SAPT basis sets (Kevin Carter-Fenk)
- *

crashing when using SAPT(KS) + cDFT with fragment-based Hirshfeld populations (Kevin Carter-Fenk)
- *

memory usage in XSAPT (Kevin Carter-Fenk, John Herbert)
