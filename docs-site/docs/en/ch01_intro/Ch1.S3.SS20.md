---
title: "1.3.20 Summary of Features Prior to Q-Chem 3.0"
---

## 1.3.20 Summary of Features Prior to **Q-Chem** 3.0

(July 4, 2026)

- •

Efficient algorithms for large-molecule density functional calculations:

- **–**

CFMM for linear scaling Coulomb interactions (energies and gradients) (C. A. White).
- **–**

Second-generation J-engine and J-force engine (Y. Shao).
- **–**

LinK for exchange energies and forces (C. Ochsenfeld and C. A. White).
- **–**

Linear scaling DFT exchange-correlation quadrature.
- •

Local, gradient-corrected, and hybrid DFT functionals:

- **–**

Slater, Becke, GGA91 and Gill ‘96 exchange functionals.
- **–**

VWN, PZ81, Wigner, Perdew86, LYP and GGA91 correlation functionals.
- **–**

EDF1 exchange-correlation functional (R. Adamson).
- **–**

B3LYP, B3P and user-definable hybrid functionals.
- **–**

Analytical gradients and analytical frequencies.
- **–**

SG-0 standard quadrature grid (S.-H. Chien).
- **–**

Lebedev grids up to 5294 points (S. T. Brown).
- •

High level wave function-based electron correlation methods

- **–**

Efficient semi-direct MP2 energies and gradients.
- **–**

MP3, MP4, QCISD, CCSD energies.
- **–**

OD and QCCD energies and analytical gradients.
- **–**

Triples corrections (QCISD(T), CCSD(T) and OD(T) energies).
- **–**

CCSD(2) and OD(2) energies.
- **–**

Active space coupled cluster methods: VOD, VQCCD, VOD(2).
- **–**

Local second order Møller-Plesset (MP2) methods (DIM and TRIM).
- **–**

Improved definitions of core electrons for post-HF correlation (V. A. Rassolov).
- •

Extensive excited state capabilities:

- **–**

CIS energies, analytical gradients and analytical frequencies.
- **–**

CIS(D) energies.
- **–**

Time-dependent density functional theory energies (TDDFT).
- **–**

Coupled cluster excited state energies, OD and VOD (A. I. Krylov).
- **–**

Coupled-cluster excited-state geometry optimizations.
- **–**

Coupled-cluster property calculations (dipoles, transition dipoles).
- **–**

Spin-flip calculations for CCSD and TDDFT excited states
(A. I. Krylov and Y. Shao).
- •

High performance geometry and transition structure optimization (J. Baker):

- **–**

Optimizes in Cartesian, *Z*-matrix or delocalized internal coordinates.
- **–**

Impose bond angle, dihedral angle (torsion) or out-of-plane bend constraints.
- **–**

Freezes atoms in Cartesian coordinates.
- **–**

Constraints do not need to be satisfied in the starting structure.
- **–**

Geometry optimization in the presence of fixed point charges.
- **–**

Intrinsic reaction coordinate (IRC) following code.
- •

Evaluation and visualization of molecular properties

- **–**

Kirkwood-Onsager, SS(V)PE, and Langevin dipoles solvation models.
- **–**

Evaluate densities, electrostatic potentials, orbitals over cubes for plotting.
- **–**

Natural Bond Orbital (NBO) analysis.
- **–**

Attachment/detachment densities for excited states via CIS, TDDFT.
- **–**

Vibrational analysis after evaluation of the nuclear coordinate Hessian.
- **–**

Isotopic substitution for frequency calculations (R. Doerksen).
- **–**

NMR chemical shifts (J. Kussmann).
- **–**

Atoms in Molecules (AIMPAC) support (J. Ritchie).
- **–**

Stability analysis of SCF wave functions (Y. Shao).
- **–**

Calculation of position and momentum molecular intracules
A. Lee, N. A. Besley, and D. P. O’Neill).
- •

Flexible basis set and effective core potential (ECP) functionality:
(Ross Adamson and Peter Gill)

- **–**

Wide range of built-in basis sets and ECPs.
- **–**

Basis set superposition error correction.
- **–**

Support for mixed and user-defined basis sets.
- **–**

Effective core potentials for energies and gradients.
- **–**

Highly efficient PRISM-based algorithms to evaluate ECP matrix elements.
- **–**

Faster and more accurate ECP second derivatives for frequencies.
