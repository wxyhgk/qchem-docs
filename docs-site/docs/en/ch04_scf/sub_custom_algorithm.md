---
title: "4.5.12 User-Customized Hybrid SCF Algorithm"
---

## 4.5.12 User-Customized Hybrid SCF Algorithm

(July 4, 2026)

It is often the case that a single algorithm is not able to guarantee SCF
convergence. Meanwhile, some SCF algorithms (*e.g.*, ADIIS) can accelerate
convergence at the beginning of an SCF calculation but becomes less efficient
near the convergence. While a few hybrid algorithms (DIIS_GDM,
RCA_DIIS) have been enabled in **Q-Chem**’s original SCF
implementation, in GEN_SCFMAN, we seek for a more flexible setup for the use
of multiple SCF algorithms so that users can have a more precise control on the
SCF procedure. With the current implementation, at most four distinct
algorithms (usually more than enough) can be employed in one single SCF
calculation based on GEN_SCFMAN, and the basic job control is as follows:

GEN_SCFMAN_HYBRID_ALGO

### `GEN_SCFMAN_HYBRID_ALGO`

> **Use multiple algorithms in an SCF calculation based on GEN_SCFMAN.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Use a single SCF algorithm (given by
>     * SCF_ALGORITHM
>     * ).
>     * TRUE
>     * Use multiple SCF algorithms (to be specified).
> * **Recommendation**: Set it to TRUE when the use of more than one algorithm is desired.

GEN_SCFMAN_ALGO_1

### `GEN_SCFMAN_ALGO_1`

> **The first algorithm to be used in a hybrid-algorithm calculation.**
>
> * **Type**: `STRING`
> * **Default**: `0`
> * **Options**:
>     * All the available
>     * SCF_ALGORITHM
>     * options, including the GEN_SCFMAN
>     * additions (Section
>     * 4.3
>     * ).
> * **Recommendation**: None

GEN_SCFMAN_ITER_1

### `GEN_SCFMAN_ITER_1`

> **Maximum number of iterations given to the first algorithm. If used up, switch to the next algorithm.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * User-defined
> * **Recommendation**: None

GEN_SCFMAN_CONV_1

### `GEN_SCFMAN_CONV_1`

> **The convergence criterion given to the first algorithm. If reached, switch to the next algorithm.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * 10
>     * ${}^{-n}$
> * **Recommendation**: None

**Note: 

*$rem* variables GEN_SCFMAN_ALGO_X, GEN_SCFMAN_ITER_X,
GEN_SCFMAN_CONV_X (X = 2, 3, 4) are defined and used in a similar way.
**

???+ example "Example 4.16: B3LYP/3-21G calculation for a cadmium-imidazole complex using the ADIIS + DIIS algorithm
(an example from Ref. 601 Hu X., Yang W. J. Chem. Phys. (2010) , 132 , pp. 054109 . Link ). Due to the poor quality of the CORE guess, using a single algorithm such as DIIS or GDM fails to converge."
    ```qchem
    $molecule
       2 1
       Cd     0.000000     0.000000     0.000000
       N      0.000000     0.000000    -2.260001
       N     -0.685444     0.000000    -4.348035
       C      0.676053     0.000000    -4.385069
       C      1.085240     0.000000    -3.091231
       C     -1.044752     0.000000    -3.060220
       H      1.231530     0.000000    -5.300759
       H      2.088641     0.000000    -2.711077
       H     -2.068750     0.000000    -2.726515
       H     -1.313170     0.000000    -5.174718
    $end
    
    $rem
       EXCHANGE                 B3LYP
       BASIS                    3-21g
       UNRESTRICTED             FALSE
       THRESH                   14
       SCF_GUESS                CORE
       GEN_SCFMAN_HYBRID_ALGO   TRUE
       GEN_SCFMAN_ALGO_1        ADIIS
       GEN_SCFMAN_CONV_1        3  ! switch to DIIS when error < 1E-3
       GEN_SCFMAN_ITER_1        50
       GEN_SCFMAN_ALGO_2        DIIS
       GEN_SCFMAN_CONV_2        8
       GEN_SCFMAN_ITER_2        50
       INTEGRAL_SYMMETRY        FALSE
       POINT_GROUP_SYMMETRY     FALSE
    $end
    ```
