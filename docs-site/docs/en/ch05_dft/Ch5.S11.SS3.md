---
title: "5.11.3 Job Control"
---

## 5.11.3 Job Control

(July 4, 2026)

A CDFT calculation is requested by setting CDFT = TRUE in the
*$rem* section. A *$cdft* input section needs to be specified as described above.
Three SCF algorithms are currently available for CDFT calculations: DIIS, RCA,
and the combined RCA-DIIS algorithm. Additional job control variables are described below.

CDFT

### `CDFT`

> **Initiates a constrained DFT calculation**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Perform a Constrained DFT Calculation
>     * FALSE
>     * No Density Constraint
> * **Recommendation**: Set to TRUE if a Constrained DFT calculation is desired.

CDFT_POSTDIIS

### `CDFT_POSTDIIS`

> **Controls whether the constraint is enforced after DIIS extrapolation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * TRUE
>     * Enforce constraint after DIIS
>     * FALSE
>     * Do not enforce constraint after DIIS
> * **Recommendation**: Use the default unless convergence problems arise, in which case it may be beneficial to experiment with setting to FALSE . With this option set to TRUE , energies should be variational after the first iteration.

CDFT_PREDIIS

### `CDFT_PREDIIS`

> **Controls whether the constraint is enforced before DIIS extrapolation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Enforce constraint before DIIS
>     * FALSE
>     * Do not enforce constraint before DIIS
> * **Recommendation**: Use the default unless convergence problems arise, in which case it may be beneficial to experiment with setting to TRUE . Note that it is possible to enforce the constraint both before and after DIIS by setting both and CDFT_POSTDIIS to TRUE .

CDFT_THRESH

### `CDFT_THRESH`

> **Threshold that determines how tightly the constraint must be satisfied.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * N
>     * Constraint is satisfied to within
>     * $10^{-N}$
>     * .
> * **Recommendation**: Default value is set to match SCF_CONVERGENCE . Use the default unless problems occur.

CDFT_MAXITER

### `CDFT_MAXITER`

> **Maximum number of iterations for converging the constraint.**
>
> * **Type**: `INTEGER`
> * **Default**: `20`
> * **Options**:
>     * N
>     * A maximum of
>     * N
>     * microiterations will be attempted.
> * **Recommendation**: Default value is expected to be sufficient in most situations.

CDFT_PRINT

### `CDFT_PRINT`

> **Whether detailed information about CDFT iterations should be printed in the output file.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Print detailed information.
>     * FALSE
>     * Do not print detailed information.
> * **Recommendation**: Use the default and invoke additional printing for troubleshooting.

CDFT_BECKE_POP

### `CDFT_BECKE_POP`

> **Whether the calculation should print the Becke atomic charges at convergence**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * TRUE
>     * Print populations
>     * FALSE
>     * Do not print them
> * **Recommendation**: Use the default. Note that the Mulliken populations printed at the end of an SCF run will not typically add up to the prescribed constraint value. Only the Becke populations are guaranteed to satisfy the user-specified constraints.
