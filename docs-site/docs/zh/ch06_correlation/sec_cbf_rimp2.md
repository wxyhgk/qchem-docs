---
title: "6.6.10 RI-MP2 Method for Complex Basis Functions"
---

## 6.6.10 RI-MP2 Method for Complex Basis Functions

(July 4, 2026)

Based on the general implementation of complex basis functions in libqints by
White, Head-Gordon, and McCurdy,[[1457]](../bib_references/bib.md#bib1525)

(see Section [4.9.5](../ch04_scf/sec_cbfscf.md)) an RI-MP2 method for
complex resonance energies has been implemented.[[1397]](../bib_references/bib.md#bib592)

This method is currently limited to closed-shell cases. The RI approximation
can be applied to the complex MP2 energy as well as to the Coulomb
and exchange parts of the complex HF energy. The use of the RI approximation is
particularly advantageous for electronic resonances since their treatment using
complex-scaled methods requires large bases with many diffuse functions.
In many cases, RI reduces computation times by a factor of 10 or more.
Also, there is no need to include complex-scaled functions in the auxiliary basis set;
standard auxiliary bases provide excellent results.[[1398]](../bib_references/bib.md#bib593)

The full basis set is supplied through the keyword COMPLEX_BASIS,
while BASIS specifies the unscaled part thereof. This process is described in Section [8.7](../ch08_basis/sect_zbas.md). In complete analogy,
the auxiliary basis set is specified using the keywords COMPLEX_AUX_BASIS
and AUX_BASIS. The keyword COMPLEX_RI_JK
controls whether the RI approximation is invoked only for the MP2 part or for the
HF reference as well.

See Sections [4.9.5](../ch04_scf/sec_cbfscf.md) and [7.9.10](../ch07_excited/sub_cc_cs_cap.md) for more information about
electronic resonances, functionalities offered by **Q-Chem** in this context,
and the corresponding keywords.

???+ example "Example 6.20: Q-Chem input for an RI-MP2 calculation of the complex resonance energy (=
Stark-shifted energy and tunnel ionization rate) of N ${}_{2}$ in a static electric
field of a strength of 0.1 a.u."
    ```qchem
    $molecule
       0 1
       N  0.00  0.00  0.55
       N  0.00  0.00 -0.55
    $end
    
    $rem
       CORRELATION           RIMP2
       BASIS                 6-31G
       COMPLEX_BASIS         6-31G*
       AUX_BASIS             rimp2-aug-cc-pVDZ
       COMPLEX_AUX_BASIS     rimp2-aug-cc-pVDZ
       COMPLEX_RI_JK         true
       COMPLEX_CCMAN         true
       SCF_GUESS             gwh
       SCF_CONVERGENCE       10
       COMPLEX_EXPONENTS     1
       COMPLEX_THETA         80
       COMPLEX_SCF           1
       COMPLEX_SCF_GUESS     1
       COMPLEX_N_ELECTRONS   0
       COMPLEX_METSCF        1
       GEN_SCFMAN            true
       THRESH                14
       PURECART              1111
       INTEGRAL_SYMMETRY     false
       POINT_GROUP_SYMMETRY  false
    $end
    
    $complex_ccman
       stark_z   1000
       cs_alpha  1000
       cs_theta  0
    $end
    ```
