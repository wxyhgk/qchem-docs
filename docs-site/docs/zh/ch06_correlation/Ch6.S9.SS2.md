---
title: "6.9.2 MPR-BWs2 Job Control"
---

## 6.9.2 MPR-BWs2 Job Control

(July 4, 2026)

MPR-BWs2 has been implemented as a specific partition of the RI-BW-s2 program.
It is invoked by setting METHOD = RIBWS2 in the *$rem* section
and writing METHOD = MPR-BWS2 in the *$bws2* section.
Iterative and non-iterative parameters as well as additional variables to
control the convergence behaviour of the iterative method are also defined
in the *$bws2* section. See [6.8](topic_bws2.md) for variables unrelated to
MPR-BWs2

### `METHOD`

> **Defines the correlation energy expression to be used. INPUT SECTION: $bws2**
>
> * **Type**: `STRING`
> * **Default**: `BWS2`
> * **Options**:
>     * MPR-BWS2
> * **Recommendation**: In order to activate MPR-BWs2, the method keyword has to be set to MPR-BWS2 or MPRBWS2

### `MPR_A0`

> **Controls the value of the $A_{0}$ parameter. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `1000`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the value of
>     * $A_{0}$
>     * .
> * **Recommendation**: Since $A_{0}$ is equal to $\alpha$ in BW-s2 theory, its standard value is set to $\alpha=A_{0}=1$ and recreates BW-s2. If both MPR_A0 and ALPHA are defined in the input file, the last read takes priority.

### `MPR_A1`

> **Controls the value of the $A_{1}$ parameter.. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the value of
>     * $A_{1}$
>     * .
> * **Recommendation**: Large values lead to convergence issues.

### `MPR_A2`

> **Controls the value of the $A_{2}$ parameter.. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the value of
>     * $A_{2}$
>     * .
> * **Recommendation**: Large values lead to convergence issues.

### `MPR_A3`

> **Controls the value of the $A_{3}$ parameter.. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the value of
>     * $A_{3}$
>     * .
> * **Recommendation**: Large values lead to convergence issues.

### `MPR_A4`

> **Controls the value of the $A_{4}$ parameter.. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the value of
>     * $A_{4}$
>     * .
> * **Recommendation**: Large values lead to convergence issues.

### `MPR_B0`

> **Controls the value of the $B_{0}$ parameter.. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the value of
>     * $B_{0}$
>     * .
> * **Recommendation**: Large values lead to convergence issues.

### `MPR_B1`

> **Controls the value of the $B_{1}$ parameter.. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the value of
>     * $B_{1}$
>     * .
> * **Recommendation**: Large values lead to convergence issues.

### `MPR_B3`

> **Controls the value of the $B_{3}$ parameter.. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the value of
>     * $B_{3}$
>     * .
> * **Recommendation**: Large values lead to convergence issues.

### `MPR_B4`

> **Controls the value of the $B_{4}$ parameter.. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the value of
>     * $B_{4}$
>     * .
> * **Recommendation**: Large values lead to convergence issues.

### `MPR_A0_NONITER`

> **Controls the value of the $A_{0}$ parameter for non-iterative contributions. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the non-iterative value of
>     * $A_{0}$
>     * .
> * **Recommendation**: Arbitrary values are possible.

### `MPR_A1_NONITER`

> **Controls the value of the $A_{1}$ parameter for non-iterative contributions. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the non-iterative value of
>     * $A_{1}$
>     * .
> * **Recommendation**: Arbitrary values are possible.

### `MPR_A2_NONITER`

> **Controls the value of the $A_{2}$ parameter for non-iterative contributions. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the non-iterative value of
>     * $A_{2}$
>     * .
> * **Recommendation**: Arbitrary values are possible.

### `MPR_A3_NONITER`

> **Controls the value of the $A_{3}$ parameter for non-iterative contributions. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the non-iterative value of
>     * $A_{3}$
>     * .
> * **Recommendation**: Arbitrary values are possible.

### `MPR_A4_NONITER`

> **Controls the value of the $A_{4}$ parameter for non-iterative contributions. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the non-iterative value of
>     * $A_{4}$
>     * .
> * **Recommendation**: Arbitrary values are possible.

### `MPR_B0_NONITER`

> **Controls the value of the $B_{0}$ parameter for non-iterative contributions. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the non-iterative value of
>     * $B_{0}$
>     * .
> * **Recommendation**: Arbitrary values are possible.

### `MPR_B1_NONITER`

> **Controls the value of the $B_{1}$ parameter for non-iterative contributions. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the non-iterative value of
>     * $B_{1}$
>     * .
> * **Recommendation**: Arbitrary values are possible.

### `MPR_B3_NONITER`

> **Controls the value of the $B_{3}$ parameter for non-iterative contributions. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the non-iterative value of
>     * $B_{3}$
>     * .
> * **Recommendation**: Arbitrary values are possible.

### `MPR_B4_NONITER`

> **Controls the value of the $B_{4}$ parameter for non-iterative contributions. INPUT SECTION: $bws2**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * where
>     * $n/1000$
>     * is the non-iterative value of
>     * $B_{4}$
>     * .
> * **Recommendation**: Arbitrary values are possible.

### `PARAM_GRADIENT`

> **Controls whether or not to compute the derivative of the energy with respect to parameters. INPUT SECTION: $bws2**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Computes the iterative and non-iterative parameter gradient.
>     * FALSE
>     * Does not compute the parameter gradient.
> * **Recommendation**: If required, set to TRUE.

???+ example "Example 6.24: MPR-BWs2 calculation on formaldehyde with $A_{0}=1$ and $B_{0}=-1$ ."
    ```qchem
    $comment
        Standard MPR-BWs2 calculation
    $end
    
    $molecule
    0 1
    C   0.0000      0.0000      0.0000
    O   0.0000      0.0000     -1.2195
    H   0.9391      0.0000      0.5422
    H  -0.9391      0.0000      0.5422
    $end
    
    $rem
    JOBTYPE             SP
    METHOD              RIBWS2              ! activate RI-BWS2 driver
    BASIS               DEF2-SVP
    AUX_BASIS           RIMP2-DEF2-SVP      ! auxilliary basis is required
    SYM_IGNORE          TRUE
    SYMMETRY            FALSE
    $end
    
    $bws2
    METHOD              MPR-BWS2            ! activate MPR-BWs2
    MPR_A0              1000                ! A_0 = 1.0
    MPR_B0              -1000               ! B_0 = -1.0
    MAX_CYCLES          50
    $end
    ```

???+ example "Example 6.25: MPR-BWs2 calculation on formaldehyde with non-iterative contributions."
    ```qchem
    $comment
        MPR-BWs2 calculation with non-iterative contributions
    $end
    
    $molecule
    0 1
    C   0.0000      0.0000      0.0000
    O   0.0000      0.0000     -1.2195
    H   0.9391      0.0000      0.5422
    H  -0.9391      0.0000      0.5422
    $end
    
    $rem
    JOBTYPE             SP
    METHOD              RIBWS2              ! activate RI-BWS2 driver
    BASIS               DEF2-SVP
    AUX_BASIS           RIMP2-DEF2-SVP      ! auxilliary basis is required
    SYM_IGNORE          TRUE
    SYMMETRY            FALSE
    $end
    
    $bws2
    METHOD              MPR-BWS2            ! activate MPR-BWs2
    MPR_A0              500                 ! A_0 = 0.5
    MPR_B1_NONITER      -1500               ! non-iterative B_0 = -1.5
    MAX_CYCLES          50
    $end
    ```

???+ example "Example 6.26: MPR-BWs2 calculation on formaldehyde including the parameter gradient."
    ```qchem
    $comment
        MPR-BWs2 calculation with parameter gradient
    $end
    
    $molecule
    0 1
    C   0.0000      0.0000      0.0000
    O   0.0000      0.0000     -1.2195
    H   0.9391      0.0000      0.5422
    H  -0.9391      0.0000      0.5422
    $end
    
    $rem
    JOBTYPE             SP
    METHOD              RIBWS2              ! activate RI-BWS2 driver
    BASIS               DEF2-SVP
    AUX_BASIS           RIMP2-DEF2-SVP      ! auxilliary basis is required
    SYM_IGNORE          TRUE
    SYMMETRY            FALSE
    $end
    
    $bws2
    METHOD              MPR-BWS2            ! activate MPR-BWs2
    MPR_A0              1500                ! A_0 = 1.5
    MAX_CYCLES          50
    PARAM_GRADIENT      TRUE                ! activate parameter gradient
    $end
    ```
