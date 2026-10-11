---
title: "6.6.8 RI-TRIM MP2 Energies"
---

## 6.6.8 RI-TRIM MP2 Energies

(July 4, 2026)

The triatomics in molecules (TRIM) local correlation approximation to MP2
theory[[790]](../bib_references/bib.md#bib819)
 was described in detail in Section [6.5.1](sect_trim.md), which
also discussed our implementation of this approach based on conventional
four-center two-electron integrals. Starting from **Q-Chem** v. 3.0, an auxiliary
basis implementation of the TRIM model is available.
The new RI-TRIM MP2 energy algorithm[[331]](../bib_references/bib.md#bib334)

greatly accelerates these local correlation calculations
(often by an order of magnitude or more for the correlation part), which scale
with the 4th power of molecule size. The electron correlation part of
the calculation is speeded up over normal RI-MP2 by a factor proportional to
the number of atoms in the molecule. For a hexadecapeptide, for instance, the
speedup is approximately a factor of 4.[[331]](../bib_references/bib.md#bib334)
 The TRIM model
can also be applied to the scaled opposite spin models discussed above. As for
the other RI-based models discussed in this section, we recommend using
RI-TRIM MP2 instead of the conventional TRIM MP2 code whenever run-time of the
job is a significant issue. As for RI-MP2 itself, TRIM MP2 is invoked by
adding AUX_BASIS *$rem*s to the input deck,
in addition to requesting CORRELATION = RILMP2.

???+ example "Example 6.19: Example of RI-TRIM MP2 energy evaluation"
    ```qchem
    $molecule
       0 3
       C1
       H1   C1   1.07726
       H2   C1   1.07726   H1   131.60824
    $end
    
    $rem
       METHOD         rilmp2
       BASIS          cc-pVDZ
       AUX_BASIS      rimp2-cc-pVDZ
       PURECART       1111
       UNRESTRICTED   true
       INTEGRAL_SYMMETRY false
    $end
    ```
