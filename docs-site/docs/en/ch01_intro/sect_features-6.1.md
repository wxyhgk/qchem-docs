---
title: "1.3.6 New Features in Q-Chem 6.1"
---

## 1.3.6 New Features in **Q-Chem** 6.1

(July 4, 2026)

## 1.3.6.1 Features in 6.1.1

- •

**Changes to default behavior:**

- **–**

Set TDKS = FALSE in fragment REM variable (*$rem_frgm*) section (John Herbert)
- **–**

Remove redundant CIS_ and SET_ variables (John Herbert)
- **–**

Update the XDM damping parameters and added variables for user control (John Herbert)
- **–**

Formatted printing of SCF energy (John Herbert)
- •

**General features and improvements:**

- **–**

Add ability to print CHELPG grid points and weights (John Herbert)
- **–**

Add Fock matrix correction for RI-JK kernels (Xintian Feng)
- **–**

Increase precision for orbital energies printout, allowing 1s energies to be obtained for heavy elements (John Herbert)
- •

**Density functional theory and self-consistent field:**

- **–**

Add XYG3, XYGJ-OS to the list of available methods (Yuezhi Mao)
- **–**

Disable double-hybrids and post-HF methods with CDFT (Yuezhi Mao)
- **–**

Improved error catching in TRNSS LR-TDDFT code for core-level excitations (John Herbert)
- **–**

Maximum Overlap Method for ROKS Calculations (Kevin Carter-Fenk, Martin Head-Gordon)
- **–**

Fixed issues with:

- *

unclear value of NATOMS_MOL1 in XDM user interface (John Herbert)
- *

$\kappa$ value printing in XDM10 (John Herbert)
- •

**Correlated methods:**

- **–**

Added hyperfine coupling code to calculate couplings between singlet/triplet excited CIS states (Samuel May, Joseph Subotnik)
- **–**

Improved MOM functionality in the ccman2 Davidson solver (Florian Matz, Quyen Nguyen, Thomas-C. Jagau)
- **–**

Support for TDDFT/TDA-SOC overlaps and external magnetic fields (Yanze Wu, Joseph Subotnik)
- **–**

Acceleration for TDDFT/TDA-SOC derivative coupling calculations, especially for time-reversal cases (Yanze Wu, Joseph Subotnik)
- **–**

Added triplet support for CIS/TDDFT overlaps (Yanze Wu, Joseph Subotnik)
- **–**

Added correct header label for NOONs in CAS-SCF calculation output (John Herbert)
- **–**

Implemented stochastic resolution of indentity approximation to CC2 model (sRI-CC2) for ground-state and excited state energy calculations (Chongxiao Zhao, Wenjie Dou, and Joonho Lee)
- **–**

Fixed issues with:

- *

typo in SOC output labels (“ms=1" changed to “ms=-1") (Yanze Wu, Joseph Subotnik)
- *

acceptor-donor order dependence in RAS-FCD and RAS-FED (Aaditya Manjanath, Chao-Ping Hsu)
- •

**Molecular dynamics, non-adiabatic dynamics, embedding, and solvation:**

- **–**

Enable SM$x$ debug printing (John Herbert)
- **–**

Improve error catching for incorrect PCM inputs (John Herbert)
- **–**

Fixed issues with:

- *

error handling for **Td_CEq_NonEq** in PCM with SF-TDDFT calculations (John Herbert)
- *

printing bug in PCM (Kuan-Yu Liu)
- •

**Fragment and energy decomposition analysis:**

- **–**

Change the fragment index convention in non-perturbative PolA/CTA to start from 1 (Yuezhi Mao)
- •

**Miscellaneous:**

- **–**

Disable analytic nuclear Hessian for ROKS jobs (Yuezhi Mao)
- **–**

Formatted printing for TDDFT with truncated subspace (John Herbert)
- **–**

Replace term “Energy Transfer" with "Polarization Energy" in non-perturbative PolA/CTA (Yuezhi Mao)
- **–**

Replace term “Charge Transfer" with "On-Fragment Charge Shift" in non-perturbative PolA/CTA (Yuezhi Mao)
- **–**

TDDFT formatted print for core-level excitations (John Herbert)

## 1.3.6.2 Features in 6.1.0

- •

**Changes to default behavior:**

- **–**

Renamed SASF_RPA to SASF_CIS
- **–**

Renamed TDDFT_PCM to TDDFT_LR_PCM (John Herbert)
- **–**

Renamed SYMMETRY to INTEGRAL_SYMMETRY and made INTEGRAL_SYMMETRY default to FALSE
- **–**

Added POINT_GROUP_SYMMETRY
- **–**

Add ENABLE_ARCHIVE keyword to control writing of archive files (Eric Berquist, Peter McLaughlin)
- •

**General features and improvements:**

- **–**

Implemented gauge-independent atomic orbital (GIAO) basis for SCF calculations (Jonathan Wong, Brad Ganoe, Tim Neudecker, Adam Rettig, Xiao Liu, Joonho Lee)
- **–**

Implemented the GIAO complex calculations for DFT jobs (Jiashu Liang)
- **–**

Implemented on-the-fly SQC and Ehrenfest nonadiabatic dynamics algorithms using restricted CIS and
TDDFT/TDA (Justin Talbot, Stephen J. Cotton, Martin Head-Gordon)
- **–**

Implemented slater transition method and transition potential method for calculating core-level binding energies
and x-ray absorption spectra (Subrata Jana, John Herbert)
- **–**

Generated data for vibronic decomposition analysis (Kuan-Yu Liu, Peter McLaughlin, Andrew Gilbert)
- **–**

Enabled state following with **Libopt3**.
- **–**

Changed transition state geometry optimization default to new optimizer (Peter McLaughlin)
- **–**

Implemented new initial model Hessian for geometry optimization (Peter McLaughlin)
- **–**

Enabled new plots section format for ESP cube plots (Yuezhi Mao)
- **–**

Added vibrational circular dichroism (VCD) spectroscopy (Yu Zhang, Kuan-Yu Liu, Eric Berquist, Evgeny Epifanovsky)
- **–**

Added RRHO print out (Abdul Aldossary, Alistair Sterling, Tim Schramm)
- **–**

Added computation of MO overlaps at displaced geometries (John Herbert)
- **–**

Resolved issues with:

- *

performance of B97M-V gradients
- *

NEO-epc19 deuterium mass being passed incorrectly (Zhen (Coraline) Tao, Mathew Chow, Sharon Hammes-Schiffer)
- *

NEO-epc19 gradients (Zhen (Coraline) Tao, Mathew Chow, Sharon Hammes-Schiffer)
- *

NEO-epc172 Hessian and multiple proton NEO Hessian (Zhen (Coraline) Tao, Mathew Chow, Sharon Hammes-Schiffer)
- *

missing STEP constraint in RHF jobs (Kevin Carter-Fenk)
- *

Gaussian blur failing to work with ECP (John Herbert)
- *

many-body expansion job failure above fourth order
- •

**Density functional theory and self-consistent field:**

- **–**

Enabled spin-orbit NTO analysis for TDDFT and SF-TDDFT (Saikiran Kotaru)
- **–**

Implemented electron-affinity time-dependent density functional theory (Kevin Carter-Fenk, Juan Arias-Martinez, Leonardo Cunha)
- **–**

Enabled projection-based embedding with ECPs (Valentina Parravicini, Thomas Jagau)
- **–**

Added a memory check before SCF for DFT jobs
- **–**

Improved EA-TDDFT/STEX job control (Kevin Carter-Fenk)
- **–**

Added SPADE localization capabilities and initial guess functionality in EA-TDDFT/STEX jobs (Kevin Carter-Fenk)
- **–**

Resolved issues with:

- *

TDA excited state frequencies crash
- *

double counting in VV10 calculations
- *

meta-GGA TDDFT analytical frequency
- •

**Correlated methods:**

- **–**

Added ability to obtain partial widths for CCSD calculations on core-vacant states (Florian Matz, Thomas Jagau)
- **–**

Implemented RI-CC2-EOM-SF, EA, and IP (Garrette Paran, Thomas Jagau, Cansu Utku)
- **–**

Implemented CCSDT (Prashant Uday Manohar, Manisha)
- **–**

Enable the use of new plots section format for the excited-state analysis of ADC jobs (Yuezhi Mao)
- **–**

Correct coefficient of EOM-CC 2PA cross section with circular polarization (Kaushik Nanda)
- **–**

Add **Dalton** solver for damped CC equations to speed up convergence (Kaushik Nanda)
- **–**

Allow user-defined active and inactive frozen-core orbitals for fc-CVS-EOM-CC calculations (Kaushik Nanda)
- **–**

Resolved issues with:

- *

Failure of iFCI when using GEN_SCFMAN
- *

Failure when calculating CC transition properties from the initial CCSD state when both CVS-EOM-EE-CCSD and CVS-EOM-IP-CCSD states are requested together (Kaushik Nanda)
- •

**Molecular dynamics, non-adiabatic dynamics, embedding, and solvation:**

- **–**

Implemented PCM contribution for nuclear-electronic orbital (NEO) method (NEO) (Mathew Chow, Sharon Hammes-Schiffer)
- **–**

Disabled $N=14$ PCM discretization grid (John Herbert)
- **–**

New and improved state-specific (SS)-PCM-TDDFT (Thomas Froitzheim, John Herbert, Jan-Michael Mewes, Stefan Grimme)
- **–**

Print clearer errors for incorrect PEqS input formatting (John Herbert)
- **–**

Resolved issues with:

- *

SMD gradient with IEF-PCM electrostatics (John Herbert)
- *

SS(V)PE and IEF-PCM gradients in NEO calculations (Mathew Chow, Sharon Hammes-Schiffer)
- *

AIMD crash with DACF calculations (J. A. Gyamfi, Thomas C. Jagau)
- *

Failure of frozen energy gradient calculations with implicit solvent when IDERIV = 0 (Yuezhi Mao)
- •

**Fragment and energy decomposition analysis:**

- **–**

Implemented decomposition of molecular polarizability using the iterative Hirshfeld scheme (Yihan Shao, Yuezhi Mao)
- **–**

Implemented force decomposition analysis (Abdulrahman Aldossary, Yuezhi Mao, Marti Gimferrer)
- **–**

Added POL and NOCV analysis for EDA2 (Hengyuan Shen)
- **–**

Enabled calculation of non-perturbative PolA/CTA with ALMO-EDA2 (Hengyuan Shen, Yuezhi Mao)
- **–**

Added pre- and post-processing scripts for XSAPT (Montgomery Gray, John Herbert)
- **–**

Resolved issues with:

- *

schema-related crash for FSSH jobs (Yuezhi Mao, Justin Talbot)
- *

error in MO SAPT calculation of $E^{(1)}_{\text{elst}}$ and $E^{(1)}_{\text{exch}}$ (Montgomery Gary, John Herbert)
- •

**Miscellaneous:**

- **–**

Disabled SMD for MECP (John Herbert)
- **–**

Added ability to define solvent dielectric constants in PCM using solvent name (John Herbert)
- **–**

Added warning for BrianQC jobs if the feature is not supported
GEN_SCFMAN = FALSE
- **–**

Remove an outdated warning about use of ECPs with Gaussian blurring (John Herbert)
- **–**

Enabled comments in all input sections (John Herbert)
- **–**

Fixed memory leak for X2C with ROHF orbitals (Kevin Carter-Fenk)
- **–**

Allow input parser to interpret 1 as TRUE (Eric Berquist)
