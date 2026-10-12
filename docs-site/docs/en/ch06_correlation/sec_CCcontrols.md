---
title: "6.12.12 Job Control Options"
---

## 6.12.12 Job Control Options

(July 4, 2026)

There are a large number of options for the coupled-cluster singles and doubles
methods. They are documented in Appendix [B](../app_b_quickref/app_quick_ref.md), and, as the
reader will find upon following this link, it is an extensive list indeed.
Fortunately, many of them are not necessary for routine jobs. Most of the
options for non-routine jobs concern altering the default iterative procedure,
which is most often necessary for optimized orbital calculations (OD, QCCD), as
well as the active space and EOM methods discussed later in Section
[6.14](sect_ccactive.md). The more common options relating to convergence control
are discussed there, in Section [6.14.6](sect_activeopt.md). Below we list the options
that one should be aware of for routine calculations.

For memory options and parallel execution, see Section [6.17](CCparallel.md).

### `CC_CONVERGENCE`

> **Overall convergence criterion for the coupled-cluster codes. This is designed to ensure at least $n$ significant digits in the calculated energy, and automatically sets the other convergence-related variables ( CC_E_CONV , CC_T_CONV , CC_THETA_CONV , CC_THETA_GRAD_CONV ) [ $10^{-n}$ ].**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n$: Corresponding to $10^{-n}$ convergence criterion. Amplitude convergence is set automatically to match energy convergence.
> * **Recommendation**: Use the default

!!! note "Note"
    For single-point calculations, CC_E_CONV = 6 and CC_T_CONV = 4.
    Tighter amplitude convergence (CC_T_CONV = 5) is used for gradients and EOM
    calculations. When using single-precision calculations, the thresholds should be adjusted
    accordingly (see section [6.18](sec_SP_CC.md)).


### `CC_DOV_THRESH`

> **Specifies minimum allowed values for the coupled-cluster energy denominators. Smaller values are replaced by this constant during early iterations only, so the final results are unaffected, but initial convergence is improved when the HOMO-LUMO gap is small or when non-conventional references are used.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $abcde$: Integer code is mapped to $ab\times 10^{-de}$ , e.g. , $2501$ corresponds to 0.025, $99001$ corresponds to 0.99, etc.
> * **Recommendation**: Increase to 0.25, 0.5 or 0.75 for non convergent coupled-cluster calculations.

!!! note "Note"
    Works only for CCMAN jobs, not enabled in CCMAN2.


### `CC_SCALE_AMP`

> **If not 0, scales down the step for updating coupled-cluster amplitudes in cases of problematic convergence.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $abcd$: Integer code is mapped to $abcd\times 10^{-2}$ , e.g. , $90$ corresponds to 0.9
> * **Recommendation**: Use 0.9 or 0.8 for non convergent coupled-cluster calculations.

!!! note "Note"
    Now available for both CCMAN and CCMAN2.


### `CC_MAX_ITER`

> **Maximum number of iterations to optimize the coupled-cluster energy.**
>
> * **Type**: `INTEGER`
> * **Default**: `200`
> * **Options**:
>     * $n$: up to
>     * $n$: iterations to achieve convergence.
> * **Recommendation**: None

### `CC_PRINT`

> **Controls the output from post-MP2 coupled-cluster module of Q-Chem**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $0-7$: higher values can lead to deforestation…
> * **Recommendation**: Increase if you need more output and don’t like trees

### `CHOLESKY_TOL`

> **Tolerance of Cholesky decomposition of two-electron integrals**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * $n$: Corresponds to a tolerance of $10^{-n}$
> * **Recommendation**: 2 - qualitative calculations, 3 - appropriate for most cases, 4 - quantitative (error in total energy typically less than 1 $\mu$ hartree)

### `CHOLESKY_TWOSTEP`

> **Activates two-step procedure for Cholesky decomposition**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `FALSE`: use original decomposition procedure
>     * `TRUE`: use two-step procedure
> * **Recommendation**: The two-step procedure is more efficient.

### `CD_TS_SPAN_FACTOR`

> **Controls the span factor used in the pivoting procedure in Step I of the two-step Cholesky decomposition**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * $n$: Corresponds to a tolerance of $10^{-n}$
> * **Recommendation**: Using larger value (e.g., 3) may improve accuracy of the decomposition step.

### `CC_DIRECT_RI`

> **Controls use of RI and Cholesky integrals in conventional (undecomposed) form**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: use all integrals in decomposed format
>     * `TRUE`: transform all RI or Cholesky integral back to conventional format
> * **Recommendation**: By default all integrals are used in decomposed format allowing significant reduction of memory use. If all integrals are transformed back (TRUE option) no memory reduction is achieved and decomposition error is introduced, however, the integral transformation is performed significantly faster and conventional CC/EOM algorithms are used.
