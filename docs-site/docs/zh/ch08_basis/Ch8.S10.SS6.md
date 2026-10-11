---
title: "8.10.6 ECPs and Electron Correlation"
---

## 8.10.6 ECPs and Electron Correlation

(July 4, 2026)

The ECP package is integrated with the electron correlation package and it is
therefore possible to apply any of **Q-Chem**’s post-Hartree-Fock methods to
systems in which some of the atoms may bear pseudopotentials. Of course, the
correlation energy contribution arising from core electrons that have been
replaced by an ECP is *not* included. In this sense, correlation energies
with ECPs are comparable to correlation energies from frozen-core calculations.
However, the use of ECPs effectively removes both core electrons *and* the
corresponding virtual (unoccupied) orbitals.

In a DFT calculation with ECPs, the exchange-correlation energy is obtained
entirely from the non-core electrons. This will be satisfactory if there are
no chemically important cores/valence effects but may introduce
significant errors if not, particularly if you are using a “large-core” ECP.
Any of the local, gradient-corrected and hybrid functionals discussed in
Chapter [5](../ch05_dft/chap_DFT.md) may be used and you may also perform ECP calculations
with user-defined hybrid functionals.

???+ example "Example 8.11: Optimization of the structure of Se ${}_{8}$ using HF/fit-LANL2DZ,
followed by a single-point energy calculation at the MP2/fit-LANL2DZ level."
    ```qchem
    $molecule
       0  1
       x1
       x2   x1  xx
       Se1  x1  sx  x2  90.
       Se2  x1  sx  x2  90.  Se1  90.
       Se3  x1  sx  x2  90.  Se2  90.
       Se4  x1  sx  x2  90.  Se3  90.
       Se5  x2  sx  x1  90.  Se1  45.
       Se6  x2  sx  x1  90.  Se5  90.
       Se7  x2  sx  x1  90.  Se6  90.
       Se8  x2  sx  x1  90.  Se7  90.
    
       xx = 1.2
       sx = 2.8
    $end
    
    $rem
       JOBTYPE    opt
       METHOD     hf
       ECP        fit-lanl2dz
       BASIS      lanl2dz
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE       sp        Single-point energy
       METHOD        mp2       MP2 correlation energy
       ECP           fit-lanl2dz   Hay-Wadt ECP and basis
       BASIS         lanl2dz
       SCF_GUESS     read      Read in the MOs
    $end
    ```
