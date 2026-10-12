---
title: "5.3.8 Semi-Empirical Functionals"
---

## 5.3.8 Semi-Empirical Functionals

(July 4, 2026)

## 5.3.8.1 Grimme “3c” Methods

The following methods are available in **Q-Chem**:

- **HF-3c**: It is an HF-based semi-empirical method which is used with a
minimal basis called MINIX. All the elements from H to Xe are supported. For the elements
from Rb ($Z=37$) to Xe ($Z=54$), def2-ECP must be used.[[1329]](../bib_references/bib.md#bib1388)
- **PBEh-3c**: It is a DFT based method which is used with def2-mSVP basis
set.This is available for all the elements from H to Rn. For the elements from Rb
($Z=37$) to Rn ($Z=86$), def2-ECP has to be used. It is a more accurate
method than HF-3c as it has correlation,[[487]](../bib_references/bib.md#bib508)

although the double-$\zeta$ basis set makes it more expensive for large molecules.

!!! note "Note"
    - The HF-3c and PBEh-3c methods were parameterized for use with the aforementioned
    basis sets. Although **Q-Chem** does not enforce this, other basis sets should not be
    used unless there is a good reason for doing so, and only then with caution as the
    results may not match published accuracy.

    - Analytic frequencies are available for these DFT-3c methods,

    with derivatives of the “3c” term computed numerically. In most cases this should be
    invisible to the user; see Section [5.3.8.2](#sec:3c-JobControl) for job control settings related
    to semi-numerical calculation of the Hessian.


## 5.3.8.2 Job Control and Examples for DFT-3c

### `FDIFF_STENCIL_3C`

> **Specifies whether to use a 5-point stencil for derivatives of the “3c” part of DFT-3c.**
>
> * **Type**: `STRING`
> * **Default**: `No default`
> * **Options**:
>     * `5`: Use the 5-point stencil
> * **Recommendation**: If this variable is not specified then Q-Chem will use a 3-point stencil, which has proven adequate in previous testing. Use the 5-point stencil only if questions arise about the accuracy of the semi-numerical frequencies.

???+ example "Example 5.4: HF-3c calculation on the I ${}^{-}$ (H ${}_{2}$ O) complex."
    ```qchem
    $rem
     method  hf-3c
     basis   minix
     ecp     def2-ecp
    $end
    
    $molecule
    -1 1
            I         0.6539056222    0.0300979939    0.0000000000
            O        -2.8593081518    0.0835488510    0.0000000000
            H        -1.8947008157    0.2596704547    0.0000000000
            H        -2.8641221666   -0.8778240298    0.0000000000
    $end
    
    ```

???+ example "Example 5.5: PBEh-3c calculation on (H ${}_{2}$ O) ${}_{2}$ ."
    ```qchem
    $molecule
       0 1
       O  -1.551007  -0.114520   0.000000
       H  -1.934259   0.762503   0.000000
       H  -0.599677   0.040712   0.000000
       O   1.350625   0.111469   0.000000
       H   1.680398  -0.373741  -0.758561
       H   1.680398  -0.373741   0.758561
    $end
    
    $rem
       METHOD           PBEh-3c
       BASIS            def2-mSVP
       XC_GRID          000099000590
       INCDFT           0
       INCFOCK          0
       SCF_CONVERGENCE  8
       THRESH           14
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
