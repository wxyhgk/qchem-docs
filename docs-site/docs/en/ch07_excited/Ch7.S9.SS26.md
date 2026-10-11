---
title: "7.9.26 Job Control for EOM-CC(2,3)"
---

## 7.9.26 Job Control for EOM-CC(2,3)

(July 4, 2026)

EOM-CC(2,3) is invoked by METHOD=EOM-CC(2,3).
The following options are available:

EOM_PRECONV_SD

### `EOM_PRECONV_SD`

> **Solves the EOM-CCSD equations, prints energies, then uses EOM-CCSD vectors as initial vectors in EOM-CC(2,3). Very convenient for calculations using energy additivity schemes.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Do
>     * $n$
>     * SD iterations
> * **Recommendation**: Turning this option on is recommended

CC_REST_AMPL

### `CC_REST_AMPL`

> **Forces the integrals, $T$ , and $R$ amplitudes to be determined in the full space even though the CC_REST_OCC and CC_REST_VIR keywords are used.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * FALSE
>     * Do apply restrictions
>     * TRUE
>     * Do not apply restrictions
> * **Recommendation**: None

CC_REST_TRIPLES

### `CC_REST_TRIPLES`

> **Restricts $R_{3}$ amplitudes to the active space, i.e. , one electron should be removed from the active occupied orbital and one electron should be added to the active virtual orbital.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 1
>     * Applies the restrictions
> * **Recommendation**: None

CC_REST_OCC

### `CC_REST_OCC`

> **Sets the number of restricted occupied orbitals including frozen occupied orbitals.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Restrict
>     * $n$
>     * occupied orbitals.
> * **Recommendation**: None

CC_REST_VIR

### `CC_REST_VIR`

> **Sets the number of restricted virtual orbitals including frozen virtual orbitals.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Restrict
>     * $n$
>     * virtual orbitals.
> * **Recommendation**: None

To select the active space, orbitals can be reordered by specifying the new
order in the *$reorder_mo*section. The section consists of two rows of
numbers ($\alpha$ and $\beta$ sets), starting from $1$, and ending with
$n$, where $n$ is the number of the last orbital specified.

The following example *$reorder_mo* section shows orbitals 16 and 17 swapped for
both $\alpha$ and $\beta$ electrons:

> ```qchem
> $reorder_mo
>    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15   17  16
>    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15   17  16
> $end
> ```

## 7.9.26.1 Examples

???+ example "Example 7.158: EOM-SF(2,3) calculations of methylene."
    ```qchem
    $molecule
       0 3
       C
       H 1 CH
       H 1 CH 2 HCH
    
       CH  = 1.07
       HCH = 111.0
    $end
    
    $rem
       METHOD             eom-cc(2,3)
       BASIS              6-31G
       SF_STATES          [2,0,0,2]
       N_FROZEN_CORE      1
       N_FROZEN_VIRTUAL   1
       EOM_PRECONV_SD     20 Get EOM-CCSD energies first (max_iter=20).
    $end
    ```

???+ example "Example 7.159: This is active-space EOM-SF(2,3) calculations for methane with an elongated CC
bond. HF MOs should be reordered as specified in the $reorder_mo section such
that active space for triples consists of sigma and sigma* orbitals."
    ```qchem
    $molecule
       0 3
       C
       H  1  CH
       H  1  CHX  2  HCH
       H  1  CH   2  HCH  3  A120
       H  1  CH   2  HCH  4  A120
    
       CH   = 1.086
       HCH  = 109.4712206
       A120 = 120.
       CHX  = 1.8
    $end
    
    $rem
       METHOD            eom-cc(2,3)
       BASIS             6-31G*
       SF_STATES         [1,0]
       N_FROZEN_CORE     1
       EOM_PRECONV_SD    20   does eom-ccsd first, max_iter=20
       CC_REST_TRIPLES   1   triples are restricted to the active space only
       CC_REST_AMPL      0   ccsd and eom singles and doubles are full-space
       CC_REST_OCC       4   specifies active space
       CC_REST_VIR       17  specifies active space
       PRINT_ORBITALS    10  (number of virtuals to print)
    $end
    
    $reorder_mo
       1 2 5 4 3
       1 2 3 4 5
    $end
    ```

???+ example "Example 7.160: EOM-IP-CC(2,3) calculation of three lowest electronic states of water cation."
    ```qchem
    $molecule
    0 1
       H   0.774767     0.000000     0.458565
       O   0.000000     0.000000    -0.114641
       H  -0.774767     0.000000     0.458565
    $end
    
    $rem
       METHOD       eom-cc(2,3)
       BASIS        6-311G
       IP_STATES    [1,0,1,1]
    $end
    ```
