---
title: "8.10.7 Forces and Vibrational Frequencies with ECPs"
---

## 8.10.7 Forces and Vibrational Frequencies with ECPs

(July 4, 2026)

It is important to be able to optimize geometries using pseudopotentials and
for this purpose **Q-Chem** contains analytical first derivatives of the nuclear
potential energy term for ECPs.

The ECP package is also integrated with the vibrational analysis package and
it is therefore possible to compute the vibrational frequencies (and hence the
infrared and Raman spectra) of systems in which some of the atoms may bear
ECPs. Starting with **Q-Chem** version 5.0, fully analytical second derivatives
of ECPs are available.

???+ example "Example 8.12: Structure and vibrational frequencies of TeO ${}_{2}$ using Hartree-Fock theory
and the Stuttgart relativistic large-core ECPs. Note that the vibrational
frequency job reads both the optimized structure and the molecular orbitals
from the geometry optimization job that precedes it."
    ```qchem
    $molecule
       0  1
       Te
       O1  Te  r
       O2  Te  r  O1  a
    
       r = 1.8
       a = 108
    $end
    
    $rem
       JOBTYPE    opt
       METHOD     hf
       ECP        srlc
       BASIS      srlc
       geom_opt_driver optimize
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE     freq
       METHOD      hf
       ECP         srlc
       BASIS      srlc
       SCF_GUESS   read
    $end
    
    ```
