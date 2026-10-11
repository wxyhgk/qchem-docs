---
title: "6.15.2 Non-Hartree-Fock Orbitals in Correlated Calculations"
---

## 6.15.2 Non-Hartree-Fock Orbitals in Correlated Calculations

(July 4, 2026)

In cases of problematic open-shell references, *e.g.*, strongly
spin-contaminated doublet radicals, one may choose to use DFT orbitals, which
can yield significantly improved results.[[111]](../bib_references/bib.md#bib97)
 This can be
achieved by first doing DFT calculation and then reading the orbitals and
turning the SCF procedure off. Note GEN_SCFMAN must be set to false
for the orbitals to be properly pseudocanonicalized.

???+ example "Example 6.49: CCSD calculation of triplet methylene using B3LYP orbitals"
    ```qchem
    $molecule
       0 3
       C
       H  1  CH
       H  1  CH  2  HCH
    
       CH  = 1.07
       HCH = 111.0
    $end
    
    $rem
       EXCHANGE        b3lyp
       BASIS           cc-pvdz
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       BASIS           cc-pvdz
       METHOD          ccsd
       SCF_GUESS       read
       MAX_SCF_CYCLES  0
       N_FROZEN_CORE   1
    $end
    ```
