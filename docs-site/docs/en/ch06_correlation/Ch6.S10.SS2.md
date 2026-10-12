---
title: "6.10.2 dRPA Job Control"
---

## 6.10.2 dRPA Job Control

(July 4, 2026)

### `CLENSHAW_NGRID`

> **Number of grid points for the Curtis-Clenshaw quadrature.**
>
> * **Type**: `INTEGER`
> * **Default**: `40`
> * **Recommendation**: Use default.

???+ example "Example 6.27: Example of RI-DRPA with RHF orbitals applied to a water dimer"
    ```qchem
    $molecule
       0  1
       O   -2.766559    0.187083    0.566918
       H   -3.696304    1.179189   -0.642507
       H   -3.395838   -1.509891    0.389284
       O    2.587035    0.275900   -0.746442
       H    3.579141    0.918407    0.633058
       H    0.852266    0.311805   -0.156847
    $end
    
    $rem
       METHOD            RIDRPA
       BASIS             cc-pvdz
       AUX_BASIS_CORR    rimp2-cc-pvdz
       UNRESTRICTED      false
       THRESH            14
       INPUT_BOHR        true
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     gdm
       MAXSCF            1000
       SCF_GUESS         sad
       CLENSHAW_NGRID    40 !number of grid points for the Curtis-Clenshaw quadrature
       INTEGRAL_SYMMETRY false
    $end
    ```
