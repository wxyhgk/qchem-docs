---
title: "10.14.2 Job Control"
---

## 10.14.2 Job Control

(July 4, 2026)

Only one keyword is necessary in the *$rem* section to activate the response
module. All other options are controlled through the *$response* input section.

RESPONSE

### `RESPONSE`

> **Activate the general response property module.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE (or 0)
>     * Don’t activate the general response property module.
>     * TRUE (or 1)
>     * Activate the general response property module.
> * **Recommendation**: None.

### `ORDER`

> **Sets the maximum order of response theory to perform. INPUT SECTION: $response**
>
> * **Type**: `STRING`
> * **Default**: `LINEAR`
> * **Options**:
>     * LINEAR
>     * Perform up through linear response.
> * **Recommendation**: None. Currently, only linear response is implemented.

### `SOLVER`

> **Sets the algorithm for solving the response equations. INPUT SECTION: $response**
>
> * **Type**: `STRING`
> * **Default**: `DIIS`
> * **Options**:
>     * LINEAR
>     * Iteratively solve the response equations without convergence acceleration.
>     * DIIS
>     * Iteratively solve the response equations using DIIS for convergence acceleration.
> * **Recommendation**: DIIS

### `HAMILTONIAN`

> **Sets the approximation used for the orbital Hessian. INPUT SECTION: $response**
>
> * **Type**: `STRING`
> * **Default**: `RPA`
> * **Options**:
>     * RPA
>     * No approximations.
>     * TDA
>     * Same as the CIS approximation.
>     * CIS
>     * Synonym for TDA.
> * **Recommendation**: None.

### `SPIN`

> **Does the operator access same spin (singlet) or different spin (triplet) states? INPUT SECTION: $response**
>
> * **Type**: `STRING`
> * **Default**: `SINGLET`
> * **Options**:
>     * SINGLET
>     * Operator is spin-conserving.
>     * TRIPLET
>     * Operator is not spin-conserving.
> * **Recommendation**: None. Care must be taken as all operators in a single calculation will be forced to follow this option.

### `MAXITER`

> **Maximum number of iterations. INPUT SECTION: $response**
>
> * **Type**: `INTEGER`
> * **Default**: `60`
> * **Options**:
>     * $n$
>     * Maximum number of iterations.
> * **Recommendation**: Use the default value.

### `CONV`

> **Convergence threshold. For the DIIS solver, this is the DIIS error norm. For the linear solver, this is the response vector RMSD between iterations. INPUT SECTION: $response**
>
> * **Type**: `INTEGER`
> * **Default**: `8`
> * **Options**:
>     * $n$
>     * Sets the convergence threshold to
>     * $10^{-n}$
>     * .
> * **Recommendation**: Use the default value.

### `DIIS_START`

> **Iteration number to start DIIS. Before this, linear iterations are performed. INPUT SECTION: $response**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $n$
>     * Iteration number to start DIIS.
> * **Recommendation**: Use the default value.

### `DIIS_VECTORS`

> **Maximum number of DIIS vectors to keep. INPUT SECTION: $response**
>
> * **Type**: `INTEGER`
> * **Default**: `7`
> * **Options**:
>     * $n>0$
>     * Maximum number of DIIS vectors to keep.
> * **Recommendation**: Use the default value.

### `RHF_AS_UHF`

> **Should the response equations be solved as though an unrestricted reference is being used? INPUT SECTION: $response**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Treat an RHF wave function as though it were UHF.
>     * FALSE
>     * Treat an RHF wave function as RHF.
> * **Recommendation**: Use the default value. Only useful for debugging.

### `PRINT_LEVEL`

> **Sets a general printing level across the response module. INPUT SECTION: $response**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * 1
>     * Print the initial guess and the final results.
>     * 2
>     * 1 + iterations and comments.
>     * 10
>     * Kill trees.
> * **Recommendation**: Use the default value.

### `RUN_TYPE`

> **Should a single response calculation be performed, or should all permutations of the orbital Hessian and excitation type be performed? INPUT SECTION: $response**
>
> * **Type**: `STRING`
> * **Default**: `SINGLE`
> * **Options**:
>     * SINGLE
>     * Use only the orbital Hessian and excitation type specified in
>     * their respective keywords.
>     * ALL
>     * Use all permutations of RPA/TDA and singlet/triplet.
> * **Recommendation**: Use the default value, unless a comparison between approximations and excitation types is desired.

### `SAVE`

> **Save any quantities to disk? INPUT SECTION: $response**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Don’t save any quantities to disk.
>     * 1
>     * Save quantities in MO basis.
>     * 2
>     * Save quantities in MO and AO bases.
> * **Recommendation**: None.

### `READ`

> **Read any quantities from disk? INPUT SECTION: $response**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Don’t read any quantities from disk.
>     * 1
>     * Read quantities in MO basis.
>     * 2
>     * Read quantities in AO basis.
> * **Recommendation**: None.

### `DUMP_AO_INTEGRALS`

> **Should AO-basis property integrals be saved to disk? INPUT SECTION: $response**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Save AO-basis property integrals to disk.
>     * FALSE
>     * Don’t save AO-basis property integrals to disk.
> * **Recommendation**: None.

### `FORCE_NOT_NONORTHOGONAL`

> **Should the canonical response equations be solved, ignoring the identity of the underlying orbitals? INPUT SECTION: $response**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * FALSE
> * **Recommendation**: Leave as false. Using the standard (canonical) response equations with non-orthogonal MOs will give incorrect results.

### `FORCE_NONORTHOGONAL`

> **Should the non-orthogonal response equations be solved, ignoring the identity of the underlying orbitals? INPUT SECTION: $response**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * FALSE
> * **Recommendation**: Leave as false. When used with canonical MOs, this should give the same answer as with the standard equations, but at greater computational cost.

### `FREQUENCY`

> **Strength of one or more incident fields in atomic units. A separate response calculation will be performed for every field strength. 0.0 corresponds to the static limit. INPUT SECTION: $response**
>
> * **Type**: `DOUBLE`
> * **Default**: `0.0`
> * **Options**:
>     * $l\,m\,n\,\dots$
>     * One or more field strengths separated by spaces.
> * **Recommendation**: None.
