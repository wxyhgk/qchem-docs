---
title: "9.8.2 Job Control and Examples"
---

## 9.8.2 Job Control and Examples

(July 4, 2026)

In order to perform nonadiabatic coupling calculations, the
*$derivative_coupling* section must be given:

> ```qchem
> $derivative_coupling
> <one line comment>
> i, j, k, ...
> $end
> ```

Nonadiabatic couplings will then be computed between all pairs of the states
$i,j,k,\ldots$; use “0” to request the HF or DFT reference state, “1”
for the first excited state, etc. Note that the derivative couplings are have
dimensions of inverse length and are printed in atomic units, *i.e.*, bohr${}^{-1}$.

CALC_NAC

### `CALC_NAC`

> **Determines whether we are calculating nonadiabatic couplings.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Calculate nonadiabatic couplings.
>     * FALSE
>     * Do not calculate nonadiabatic couplings.
> * **Recommendation**: None.

CIS_DER_NUMSTATE

### `CIS_DER_NUMSTATE`

> **Determines among how many states we calculate nonadiabatic couplings. These states must be specified in the $derivative_coupling section.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not calculate nonadiabatic couplings.
>     * $n$
>     * Calculate
>     * $n(n-1)/2$
>     * pairs of nonadiabatic couplings.
> * **Recommendation**: None.

SET_QUADRATIC

### `SET_QUADRATIC`

> **Determines whether to include full quadratic response contributions for TDDFT.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Include full quadratic response contributions for TDDFT.
>     * FALSE
>     * Use pseudo-wave function approach.
> * **Recommendation**: The pseudo-wave function approach is usually accurate enough and is free of accidental singularities. Consult Refs. 1548 Zhang X., Herbert J. M. J. Chem. Phys. (2015) , 142 , pp. 064109 . Link and 1029 Ou Q. et al. J. Chem. Phys. (2015) , 142 , pp. 064114 . Link for additional guidance.

???+ example "Example 9.26: Nonadiabatic couplings among the lowest five singlet states of ethylene,
computed at the TD-B3LYP level using the pseudo-wave function approach."
    ```qchem
    $molecule
       0 1
       C    1.85082356   -1.78953123    0.00000000
       H    2.38603593   -2.71605577    0.00000000
       H    0.78082359   -1.78977646    0.00000000
       C    2.52815456   -0.61573833    0.00000000
       H    1.99294220    0.31078621    0.00000000
       H    3.59815453   -0.61549310    0.00000000
    $end
    
    $rem
       EXCHANGE           b3lyp
       BASIS              6-31G*
       CIS_N_ROOTS        4
       CIS_TRIPLETS       false
       MAX_CIS_CYCLES     50
       CIS_DER_NUMSTATE   5
       CALC_NAC           true
    $end
    
    $derivative_coupling
       0 is the reference state
       0 1 2 3 4
    $end
    ```

???+ example "Example 9.27: Nonadiabatic couplings between $S_{1}$ and $S_{3}$ states of ethylene using
BH&HLYP and spin-flip TDDFT."
    ```qchem
    $molecule
       0 3
       C    1.85082356   -1.78953123    0.00000000
       H    2.38603593   -2.71605577    0.00000000
       H    0.78082359   -1.78977646    0.00000000
       C    2.52815456   -0.61573833    0.00000000
       H    1.99294220    0.31078621    0.00000000
       H    3.59815453   -0.61549310    0.00000000
    $end
    
    $rem
       EXCHANGE           bhhlyp
       BASIS              6-31G*
       SPIN_FLIP          true
       UNRESTRICTED       true
       CIS_N_ROOTS        4
       CIS_TRIPLETS       false
       MAX_CIS_CYCLES     50
       CIS_DER_NUMSTATE   2
       CALC_NAC           true
    $end
    
    $derivative_coupling
       comment
       1 3
    $end
    ```

???+ example "Example 9.28: Nonadiabatic couplings between $S_{1}$ and $S_{2}$ states of ethylene computed via
quadratic response theory at the TD-B3LYP level."
    ```qchem
    $molecule
       0 1
       C    1.85082356   -1.78953123    0.00000000
       H    2.38603593   -2.71605577    0.00000000
       H    0.78082359   -1.78977646    0.00000000
       C    2.52815456   -0.61573833    0.00000000
       H    1.99294220    0.31078621    0.00000000
       H    3.59815453   -0.61549310    0.00000000
    $end
    
    $rem
       EXCHANGE          b3lyp
       BASIS             6-31G*
       CIS_N_ROOTS       4
       CIS_TRIPLETS      false
       RPA               true
       MAX_CIS_CYCLES    50
       CIS_DER_NUMSTATE  2
       CALC_NAC          true
       SET_QUADRATIC     true ! include full quadratic response
    $end
    
    $derivative_coupling
       comment
       1 2
    $end
    ```
