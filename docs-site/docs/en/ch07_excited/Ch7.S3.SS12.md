---
title: "7.3.12 Examples"
---

## 7.3.12 Examples

(July 4, 2026)

???+ example "Example 7.31: This example shows two jobs which request variants of time-dependent density
functional theory calculations. The first job, using the default value of RPA = FALSE , performs TDDFT in the Tamm-Dancoff approximation
(TDA). The second job, with RPA = TRUE performs a both TDA
and full TDDFT calculations."
    ```qchem
    $comment
       methyl peroxy radical
       TDDFT/TDA and full TDDFT with 6-31+G*
    $end
    
    $molecule
       0  2
       C  1.00412  -0.18045    0.00000
       O -0.24600   0.59615    0.00000
       O -1.31237  -0.23026    0.00000
       H  1.81077   0.56720    0.00000
       H  1.03665  -0.80545   -0.90480
       H  1.03665  -0.80545    0.90480
    $end
    
    $rem
       EXCHANGE          b
       CORRELATION       lyp
       CIS_N_ROOTS       5
       BASIS             6-31+G*
       SCF_CONVERGENCE   7
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       EXCHANGE          b
       CORRELATION       lyp
       CIS_N_ROOTS       5
       CIS_MAX_CYCLES    40
       RPA               true
       BASIS             6-31+G*
       SCF_CONVERGENCE   7
    $end
    ```

???+ example "Example 7.32: This example shows a calculation of the excited states of a formamide-water
complex within a reduced excitation space of the orbitals located on formamide."
    ```qchem
    $comment
       formamide-water TDDFT/TDA in reduced excitation space
    $end
    
    $molecule
       0 1
       H  1.13  0.49 -0.75
       C  0.31  0.50 -0.03
       N -0.28 -0.71  0.08
       H -1.09 -0.75  0.67
       H  0.23 -1.62 -0.22
       O -0.21  1.51  0.47
       O -2.69  1.94 -0.59
       H -2.59  2.08 -1.53
       H -1.83  1.63 -0.30
    $end
    
    $rem
       EXCHANGE          b3lyp
       CIS_N_ROOTS       10
       BASIS             6-31++G**
       TRNSS             TRUE
       TRTYPE            1
       CUTOCC            60
       CUTVIR            40
       CISTR_PRINT       TRUE
       N_SOL             6
    $end
    
    $solute
    1
    2
    3
    4
    5
    6
    $end
    ```
