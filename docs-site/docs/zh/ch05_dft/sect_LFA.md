---
title: "5.10.3 Localized Fermi-Amaldi (LFA) Schemes"
---

## 5.10.3 Localized Fermi-Amaldi (LFA) Schemes

(July 4, 2026)

Another alternative, proposed by Pan, Fang and Chai,[[1037]](../bib_references/bib.md#bib226)
 is to
use a *localized* version of Fermi-Amaldi exchange-correlation functional.
The resulting exchange density functional, whose functional derivative has the
correct $-1/r$ asymptotic behavior, can be directly added to any semi-local
density functional. Three variants of this method were proposed in
Ref. [[1037]](../bib_references/bib.md#bib226)
. The simplest of these, the strictly-localized
Fermi-Amaldi (LFAs) scheme, is implemented in **Q-Chem**, for molecules
consisting of atoms with $Z\leq 55$.

???+ example "Example 5.24: LFAs-PBE single-point TD-DFT calculation with water molecule"
    ```qchem
    $comment
       Use LFAs-PBE potential for ground-state calculations, followed by
       TDDFT calculations with an adiabatic PBE XC kernel.
    $end
    
    $molecule
       0  1
       O
       H1  O  oh
       H2  O  oh  H1  hoh
    
       oh  =   1.0
       hoh = 110.0
    $end
    
    $rem
       EXCHANGE      gen
       BASIS         6-311(2+,2+)G**
       CIS_N_ROOTS   30
       RPA           true
    $end
    
    $xc_functional
       X   PBE   1.0
       C   PBE   1.0
       X   LFAs  1.0
    $end
    ```
