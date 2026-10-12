---
title: "1.3.19 Summary of Features in Q-Chem Versions 3. x"
---

## 1.3.19 Summary of Features in **Q-Chem** Versions 3.$\,$*x*

(July 4, 2026)

- DFT functionals and algorithms:

- Long-ranged corrected (LRC) functionals, also known as range-separated hybrid functionals (M. A. Rohrdanz and J. M. Herbert)
- Constrained DFT (Q. Wu and T. Van Voorhis)
- Grimme’s “DFT-D” empirical dispersion corrections (C.-D. Sherrill)
- “Incremental” DFT method that significantly accelerates exchange-correlation quadrature in later SCF cycles (S. T. Brown)
- Efficient SG-0 quadrature grid with approximately half the number of grid points relative to SG-1 (S.-H. Chien)
- Solvation models:

- SM8 model
(A. V. Marenich, R. M. Olson, C. P. Kelly, C. J. Cramer, and D. G. Truhlar)
- Kirkwood-Onsager reaction-field model
(C.-L. Cheng, T. Van Voorhis, K. Thanthiriwatte, and S. R. Gwaltney)
- Chipman’s SS(V)PE model (S. T. Brown)
- Second-order perturbation theory algorithms for ground and excited states:

- Dual-basis RIMP2 energy and analytical gradient (R. P. Steele, R. A. DiStasio Jr., and M. Head-Gordon)
- O2 energy and gradient (R. C. Lochan and M. Head-Gordon)
- SOS-CIS(D), SOS-CIS(D${}_{0}$), and RI-CIS(D) for excited states (D. Casanova, Y. M. Rhee, and M. Head-Gordon)
- Efficient resolution-of-identity (RI) implementations of MP2 and SOS-MP2 (including both energies and gradients),
and of RI-TRIM and RI-CIS(D) energies (Y. Jung, R. A. DiStasio, Jr., R. C. Lochan, and Y. M. Rhee)
- Coupled-cluster methods (P. A. Pieniazek, E. Epifanovsky, A. I. Krylov):

- IP-CISD and EOM-IP-CCSD energy and gradient
- Multi-threaded (OpenMP) parallel coupled-cluster calculations
- Potential energy surface crossing minimization with CCSD and EOM-CCSD methods (E. Epifanovsky)
- Dyson orbitals for ionization from the ground and excited states within CCSD and EOM-CCSD methods (M. Oana)
- QM/MM methods (H. L. Woodcock, A. Ghysels, Y. Shao, J. Kong, and H. B. Brooks)

- **Q-Chem**/**Charmm** interface (H. L. Woodcock)
- Full QM/MM Hessian evaluation and approximate mobile-block-Hessian evaluation
- Two-layer ONIOM model (Y. Shao).
- Integration with the **Molaris** simulation package (E. Rosta).
- Improved two-electron integrals package

- Rewrite of the Head-Gordon–Pople algorithm for modern computer architectures (Y. Shao)
- Fourier Transform Coulomb method for linear-scaling construction of the Coulomb matrix, even for basis sets
with high angular moment and diffuse functions (L. Fusti-Molnar)
- Dual basis self-consistent field calculations, offering an order-of-magnitude reduction in the cost of large-basis
DFT calculations (J. Kong and R. P. Steele)
- Enhancements to the correlation package including:

- Most extensive range of EOM-CCSD methods available including
EOM-SF-CCSD, EOM-EE-CCSD, EOM-DIP-CCSD, EOM-IP/EA-CCSD (A. I. Krylov).
- Available for RHF, UHF, and ROHF references.
- Analytic gradients and properties calculations (permanent and transition dipoles *etc.*.).
- Full use of Abelian point-group symmetry.
- Coupled-cluster perfect-paring methods applicable to systems with $>100$ active electrons (M. Head-Gordon)
- Transition structure search using the “growing string” algorithm (A. Heyden and B. Peters):
- *Ab initio* molecular dynamics (J. M. Herbert)
- Linear scaling properties for large systems (J. Kussmann, C. Ochsenfeld):

- NMR chemical shifts
- Static and dynamic polarizabilities
- Static hyper-polarizabilities, optical rectification, and electro-optical Pockels effect
- Anharmonic frequencies (C. Y. Lin)
- Wave function analysis tools:

- Analysis of intermolecular interactions with ALMO-EDA (R. Z. Khaliullin and M. Head-Gordon)
- Electron transfer analysis (Z.-Q. You and C.-P. Hsu)
- Spin densities at the nuclei (V. A. Rassolov)
- Position, momentum, and Wigner intracules (N. A. Besley and D. P. O’Neill)
- Graphical user interface (GUI) options:

- **IQmol**, a fully integrated GUI. **IQmol** includes input file generator and contextual help, molecular builder,
job submission tool, and visualization kit (molecular orbital and density viewer, frequencies, etc).
For the latest version and download/installation instructions, please see the **IQmol** homepage
(`http://www.iqmol.org`).
- Seamless integration with the **Spartan** package
(see `www.wavefun.com`).
- Support for several other public-domain visualization programs:

- **WebMO**

`https://www.webmo.net`
- **Avogadro**

`https://avogadro.cc`
- **MolDen**

`http://www.cmbi.ru.nl/molden`
- **MacMolPlt** (via a **MolDen**-formatted input file) 

`https://brettbode.github.io/wxmacmolplt`
- **JMol**

`http://jmol.sourceforge.net/`
