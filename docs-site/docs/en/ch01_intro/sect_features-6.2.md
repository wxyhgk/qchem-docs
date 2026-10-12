---
title: "1.3.5 New Features in Q-Chem 6.2"
---

## 1.3.5 New Features in **Q-Chem** 6.2

(July 4, 2026)

## 1.3.5.1 Features in 6.2.0

- **Changes to default behavior:**

- Set POINT_GROUP_SYMMETRY = FALSE for freq jobs reading guess from previous job to avoid reorientation
- Make NO_REORIENT = 1 and POINT_GROUP_SYMMETRY = 0 the defaults for harmonic confiner jobs
- Make improved initial guess Hessian the default for optimizations (INITIAL_HESSIAN = MODEL)
- Enable RI-K virtual orbital correction by default for occ-RI-K frequency jobs
- **General features and improvements:**

- NEO Multistate DFT (NEO-MSDFT) (Joseph Dickinson, Qi Yu, Sharon Hammes-Schiffer)
- Added simulation of nuclear-electronic quantum dynamics based on real-time nuclear-electronic orbital (RT-NEO) (Tao E. Li, Mathew Chow, Sharon Hammes-Schiffer)
- Added support for D3 empirical dispersion correction (energies and gradients) and Effective Core Potential (ECP) (energies and gradients) for NEO approach and RT-NEO methods (Mathew Chow, Sharon Hammes-Schiffer)
- Constrained NEO (CNEO) for a single NEO center (Eno Paenurk, Sharon Hammes-Schiffer)
- Addition of SCS-RIMP2 and SOS-OOMP2 to NEO methods (Jonathan Fetherolf, Sharon Hammes-Schiffer)
- Faster NEO-SCF via simultaneous DIIS optimization (Mathew Chow, Sharon Hammes-Schiffer)
- Add atomic multipole moment calculation using IAOs (Alexandra McIsaac, Abdulrahman Aldossary, Martin Head-Gordon)
- Update the list of occasions not allowed for the AUTOSAD $\to$ CORE fallback when atomic jobs fail (Yuezhi Mao)
- New syntax allowing external electric field to follow a bond (Tarek Scheele, Tim Neudecker)
- Real-time extension of TAO-DFT (RT-TAO) (Hung-Yi Tsai, Jeng-Da Chai)
- SCF energy prints now break one-electron terms into kinetic, nuclear attraction and remainder when SCF_FINAL_PRINT is set to TRUE
- Resolved issues with:

- Incorrect hydrogen isotope mass when using EPC functionals with NEO (Mathew Chow, Zhen (Coraline) Tao, Sharon Hammes-Schiffer)
- NEO Hessian implementation for range-separated functionals (Eno Paenurk and Sharon Hammes-Schiffer)
- Failure of the READ_REAL guess of complex RHF (Yuezhi Mao)
- **Libopt3** misclassification of structure type for near-zero eigenvalues
- “SVD Failed" invalid step error in rare geometry optimization cases
- **Density functional theory and self-consistent field:**

- Implemented DFT/CIS, including a new parameterization for x-ray spectroscopy (Aniket Mandal, John Herbert)
- Addition of new TZVP basis set for DFT/CIS to QCAUX (Aniket Mandal, John Herbert)
- Implemented suppression of open-shell mixing for ROKS calculations (Juanes Arias-Martinez, Martin Head-Gordon)
- Enable negative $s_{8}$ values for Grimme’s D4 dispersion correction
- Dipole filtering for restricted and unrestricted TDKS (John Herbert, Avik Kumar Ojha)
- Print spatial overlaps of orbitals (intermediate overlaps for occ/virt pairs) (John Herbert)
- Make virtual orbital correction after SCF convergence optional for occ-RI-K
- Enable MakeMeSAD for GEN_SCFMAN
- Add SAD guesses for cc-pV6Z and aug-cc-pV6Z
- Disable AUTOSAD guess for CDFT-CI (John Herbert)
- Disable NTOs for RPA (John Herbert)
- Resolved issues with:

- Job control through FDIFF_DER for anharmonic frequency calculations (Yuezhi Mao)
- Anharmonic frequency calculation failure with DFT (Yuezhi Mao)
- Restart initialization for unrestricted TDKS (Hung-Yi Tsai, Jeng-Da Chai)
- Bug in RI related to basis sets that use multishells (note that this does not affect most RI calculations, unless an auxiliary multishell basis is used)
- **Correlated methods:**

- Added hyperfine coupling code to calculate couplings between singlet/triplet excited CIS states (Samuel May, Joseph Subotnik)
- Generalization of 1C-NOCIS to two-electron open-shell singlets (Juanes Arias-Martinez, Hamlin Wu, Martin Head-Gordon)
- Implemented the ACP-EOMIP-CCSD method to compute partial Auger decay widths (Florian Matz, Thomas Jagau)
- Built-in implementation of calculations of cross-sections and angular distributions using Dyson orbitals (Madhubani Mukherjee, Sarai Folkestad, Anna Krylov)
- Natural Auger Orbitals for Auger decay, ICD, and related processes for CVS-EOM methods (Nayanthara K. Jayadev, Anna I. Krylov)
- Added BW-s2 method (Kevin Carter-Fenk, Martin Head-Gordon)
- Stochastic resolution of identity to CC2 (sRI-CC2) for excited state energy calculations (Chongxiao Zhao, Wenjie Dou, Joonho Lee)
- EOM-CCSDT for EE and SF states (Manisha, Prashant Uday Manohar)
- Resolved issues with:

- Legacy RI-MP2 code crashes when MEM_STATIC value is too large (Yuezhi Mao)
- Error in calculation of the separable part of the one-particle density matrix with CCSD (Yongbin Kim, Madhubani Mukherjee, Anna Krylov)
- Overwriting of Molden files for natural Auger orbitals in resonant Auger decay calculations (Nayanthara Karippara Jayadev, Anna Krylov)
- **Molecular dynamics, non-adiabatic dynamics, embedding, and solvation improvements:**

- External/embedded potential read (Huseyin Aksu, Barry Dunietz)
- Turn on PCM at the first SCF iteration when SCF_GUESS = READ,
allowing faster convergence (Yuezhi Mao)
- Turn on PCM at the first SCF iteration in the 2nd geom opt cycle for FRAGMO and AUTOSAD (Yuezhi Mao)
- Clarified ambiguous output for COSMO (John Herbert)
- Added analytic X-HCFF Hessian (Rahel Weiss, Felix Zeller, Tim Neudecker)
- Resolved issues with:

- Out-of-bound access error for SMX with ghost atoms
- Undesirable behavior of SOLVENT_METHOD = TRUE invoking Kirkwood model (John Herbert)
- Add missing qarchive files for QM/MM calculations (Xiaoliang Pan, Yihan Shao)
- Incorrectly increasing van der Waals radii for I and At atoms in jobs with multiple SMD calculations (Zheng Pei)
- **Fragment and energy decomposition analysis improvements:**

- Add additional printout for libwfa regarding ionic/covalent states (Felix Plasser)
- Resolved issues with:

- Occasional crash in non-perturbative CTA (Yuezhi Mao)
- **Post-processing features:**

- Calculations of g-tensors using ezMagnet (Sven Kähler, Antonio Cebreiro-Gallardo, Pavel Pokhilko, David Casanova, and Anna I. Krylov)
