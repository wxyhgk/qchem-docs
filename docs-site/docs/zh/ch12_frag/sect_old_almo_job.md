---
title: "12.5.5 Job Control Options"
---

## 12.5.5 Job Control Options

(July 4, 2026)

FRGM_METHOD

### `FRGM_METHOD`

> **Specifies a locally-projected method.**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * STOLL
>     * Locally-projected SCF equations of Stoll are solved.
>     * GIA
>     * Locally-projected SCF equations of Gianinetti are solved.
>     * NOSCF_RS
>     * Single Roothaan-step correction to the
>     * FRAGMO
>     * initial guess.
>     * NOSCF_ARS
>     * Approximate single Roothaan-step correction to the
>     * FRAGMO
>     * initial guess.
>     * NOSCF_DRS
>     * Double Roothaan-step correction to the
>     * FRAGMO
>     * initial guess.
>     * NOSCF_RS_FOCK
>     * Non-converged SCF energy of the single Roothaan-step MOs.
> * **Recommendation**: STOLL and GIA are for variational optimization of the ALMOs. NOSCF options are for computationally fast corrections of the FRAGMO initial guess.

FRGM_LPCORR

### `FRGM_LPCORR`

> **Specifies a correction method performed after the locally-projected equations are converged.**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * ARS
>     * Approximate Roothaan-step perturbative correction.
>     * RS
>     * Single Roothaan-step perturbative correction.
>     * EXACT_SCF
>     * Full SCF variational correction.
>     * ARS_EXACT_SCF
>     * Both
>     * ARS
>     * and
>     * EXACT_SCF
>     * in a single job.
>     * RS_EXACT_SCF
>     * Both
>     * RS
>     * and
>     * EXACT_SCF
>     * in a single job.
> * **Recommendation**: For large basis sets use ARS , use RS if ARS fails.

SCF_PRINT_FRGM

### `SCF_PRINT_FRGM`

> **Controls the output of Q-Chem jobs on isolated fragments.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * The output is printed to the parent job output file.
>     * FALSE
>     * The output is not printed.
> * **Recommendation**: Use TRUE if details about isolated fragments are important.

EDA_BSSE

### `EDA_BSSE`

> **Calculates the BSSE correction when performing the energy decomposition analysis.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE/FALSE
> * **Recommendation**: Set to TRUE unless a very large basis set is used.

EDA_COVP

### `EDA_COVP`

> **Perform COVP analysis when evaluating the RS or ARS charge-transfer correction. COVP analysis is currently implemented only for systems of two fragments.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE/FALSE
> * **Recommendation**: Set to TRUE to perform COVP analysis in an EDA or SCF-MI(RS) job.

EDA_PRINT_COVP

### `EDA_PRINT_COVP`

> **Replace the final MOs with the CVOP orbitals in the end of the run.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE/FALSE
> * **Recommendation**: Set to TRUE to print COVP orbitals instead of conventional MOs.

NVO_LIN_MAX_ITE

### `NVO_LIN_MAX_ITE`

> **Maximum number of iterations in the preconditioned conjugate gradient solver of the single-excitation amplitude equations.**
>
> * **Type**: `INTEGER`
> * **Default**: `30`
> * **Options**:
>     * $n$
>     * User–defined number of iterations.
> * **Recommendation**: None.

NVO_LIN_CONVERGENCE

### `NVO_LIN_CONVERGENCE`

> **Target error factor in the preconditioned conjugate gradient solver of the single-excitation amplitude equations.**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * $n$
>     * User–defined number.
> * **Recommendation**: Solution of the single-excitation amplitude equations is considered converged if the maximum residual is less than $10^{-n}$ multiplied by the current DIIS error. For the ARS correction, $n$ is automatically set to 1 since the locally-projected DIIS error is normally several orders of magnitude smaller than the full DIIS error.

NVO_METHOD

### `NVO_METHOD`

> **Sets method to be used to converge solution of the single-excitation amplitude equations.**
>
> * **Type**: `INTEGER`
> * **Default**: `9`
> * **Options**:
>     * $n$
>     * User–defined number.
> * **Recommendation**: This is an experimental option. Use the default.

NVO_UVV_PRECISION

### `NVO_UVV_PRECISION`

> **Controls convergence of the Taylor series when calculating the $U_{vv}$ block from the single-excitation amplitudes. Series is considered converged when the maximum element of the term is less than $10^{-n}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `11`
> * **Options**:
>     * $n$
>     * User–defined number.
> * **Recommendation**: must be the same as or larger than THRESH .

NVO_UVV_MAXPWR

### `NVO_UVV_MAXPWR`

> **Controls convergence of the Taylor series when calculating the $U_{vv}$ block from the single-excitation amplitudes. If the series is not converged at the $n$ th term, more expensive direct inversion is used to calculate the $U_{vv}$ block.**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $n$
>     * User–defined number.
> * **Recommendation**: None.

NVO_TRUNCATE_DIST

### `NVO_TRUNCATE_DIST`

> **Specifies which atomic blocks of the Fock matrix are used to construct the preconditioner.**
>
> * **Type**: `INTEGER`
> * **Default**: `$-$`
> * **Options**:
>     * $n>0$
>     * If distance between a pair of atoms is more than
>     * $n$
>     * Ångstroms
>     * do not include the atomic block.
>     * $-$
>     * 2
>     * Do not use distance threshold, use
>     * NVO_TRUNCATE_PRECOND
>     * instead.
>     * $-$
>     * 1
>     * Include all blocks.
>     * 0
>     * Include diagonal blocks only.
> * **Recommendation**: This option does not affect the final result. However, it affects the rate of the PCG algorithm convergence. For small systems, use the default.

NVO_TRUNCATE_PRECOND

### `NVO_TRUNCATE_PRECOND`

> **Specifies which atomic blocks of the Fock matrix are used to construct the preconditioner. This variable is used only if NVO_TRUNCATE_DIST is set to $-2$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * $n$
>     * If the maximum element in an atomic block is less than
>     * $10^{-n}$
>     * do not include
>     * the block.
> * **Recommendation**: Use the default. Increasing $n$ improves convergence of the PCG algorithm but overall may slow down calculations.
