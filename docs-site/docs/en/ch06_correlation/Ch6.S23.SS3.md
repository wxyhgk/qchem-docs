---
title: "6.23.3 v2RDM Job Control"
---

## 6.23.3 v2RDM Job Control

(July 4, 2026)

### `RDM_POSITIVITY`

> **Indicates positivity conditions enforced in the v2RDM optimization.**
>
> * **Type**: `STRING`
> * **Default**: `DQG`
> * **Options**:
>     * `DQG,`: Two-electron conditions
>     * `DQGT1`: Two-electron conditions plus the T1 partial three-electron conditions
>     * `DQGT2`: Two-electron conditions plus the T2 partial three-electron conditions
>     * `DQGT1T2`: Two-electron conditions plus the T1 and T2 partial three-electron conditions
>     * `DQG3POS`: Two-electron conditions plus the full three-electron conditions
> * **Recommendation**: For high-accuracy, use DQG3POS or DQGT2 , although such computations become impractical for large active spaces. For large active spaces ( e.g. , n > 16 for CAS(n, n)), use DQG.

### `RDM_CONSTRAIN_SPIN`

> **Indicates if the spin-constraints are enforced.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Enforce spin-constraints.
>     * `FALSE`: Do not enforce spin-constraints.
> * **Recommendation**: Use default.

### `PDFT_EXCHANGE`

> **Specifies the exchange functional to be used in MC-PDFT calculation.**
>
> * **Type**: `STRING`
> * **Default**: `No default`
> * **Options**:
>     * `NAME`: Use =
>     * `NAME`: , where
>     * `NAME`: must be one of the LDA or GGA exchange functionals listed in Section 5.3.3 . This keyword is only invoked when method is set to RDM(PDFT).
> * **Recommendation**: In general, consult the literature to guide your selection.

### `PDFT_CORRELATION`

> **Specifies the correlation functional to be used in MC-PDFT calculation.**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * `NAME`: Use =
>     * `NAME`: , where
>     * `NAME`: is one of the LDA or GGA correlation functionals listed in Section 5.3.4 . This keyword is only invoked when method is set to RDM(PDFT).
> * **Recommendation**: In general, consult the literature to guide your selection.

### `RDM_E_CONVERGENCE`

> **The threshold for the primal-dual energy gap.**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $N$: for a threshold of $10^{-N}$
> * **Recommendation**: Increase for gradient computations.

### `RDM_EPS_CONVERGENCE`

> **The threshold for the error in the primal and dual constraints.**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $N$: for a threshold of $10^{-N}$
> * **Recommendation**: Increase for gradient computations.

### `RDM_MAXITER`

> **Maximum number of diagonalization steps in the BPSDP solver.**
>
> * **Type**: `INTEGER`
> * **Default**: `50000`
> * **Options**:
>     * $N>0$
> * **Recommendation**: Increase for computations that are difficult to converge.

### `RDM_CG_CONVERGENCE`

> **The minimum threshold for the conjugate gradient solver.**
>
> * **Type**: `INTEGER`
> * **Default**: `12`
> * **Options**:
>     * $N$: for a threshold of $10^{-N}$
> * **Recommendation**: Should be at least ( RDM_EPS_CONVERGENCE +2).

### `RDM_CG_MAXITER`

> **Maximum number of iterations for each conjugate gradient computations in the BPSDP algorithm.**
>
> * **Type**: `INTEGER`
> * **Default**: `1000`
> * **Options**:
>     * $N>0$
> * **Recommendation**: Use default unless problems arise.

### `RDM_TAU`

> **Step-length parameter used in the BPSDP solver.**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $N$: for a value of 0.1 * $N$
> * **Recommendation**: should range between 10 and 16 for $1.0\leq\tau\leq 1.6$ .

### `RDM_MU_UPDATE_FREQUENCY`

> **The number of v2RDM iterations after which the penalty parameter $\mu$ is updated.**
>
> * **Type**: `INTEGER`
> * **Default**: `200`
> * **Options**:
>     * $N>0$
> * **Recommendation**: Change if convergence problems arise.

### `RDM_TPDM_GUESS`

> **Initial guess for the RDMs**
>
> * **Type**: `STRING`
> * **Default**: `HF_GUESS`
> * **Options**:
>     * `HF_GUESS`: Use RDMs from Hartree-Fock calculations as the initial density for the semidefinite solver
>     * `RANDOM_GUESS`: Use random numbers as the initial density for the semidefinite solver
> * **Recommendation**: Use default unless convergence problems arise.

### `RDM_DIAGONALIZER`

> **The algorithm used to diagonalize matrices inside semidefinite programming.**
>
> * **Type**: `INTEGER`
> * **Default**: `11`
> * **Options**:
>     * `0`: Use parallel LAPACK function DSYEV
>     * `1`: Use parallel LAPACK function DSYEVD
>     * `10`: Use multiple simultaneous calls to serial LAPACK function DSYEV
>     * `11`: Use multiple simultaneous calls to serial LAPACK function DSYEVD
> * **Recommendation**: Use default. Under certain circumstances ( e.g. , low symmetry), algorithm 1 may be faster.

### `RDM_PRINT`

> **Controls the amount of printing.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Print minimal information.
>     * `1`: Print information about all iterations.
> * **Recommendation**: Use 1 to analyze convergence issues.

### `RDM_ORBOPT_GRADIENT_CONVERGENCE`

> **The threshold for the orbital gradient during orbital optimization.**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $N$: for threshold of $10^{-N}$
> * **Recommendation**: Tighten for gradient computations.

### `RDM_ORBOPT_ENERGY_CONVERGENCE`

> **The threshold for energy convergence during orbital optimization.**
>
> * **Type**: `INTEGER`
> * **Default**: `8`
> * **Options**:
>     * $N$: for threshold of $10^{-N}$
> * **Recommendation**: Tighten for gradient computations.

### `RDM_ORBOPT_MAXITER`

> **The maximum number of orbital optimization steps each time the orbital optimization routine is called.**
>
> * **Type**: `INTEGER`
> * **Default**: `20`
> * **Options**:
>     * $N>0$
> * **Recommendation**: Use default unless convergence problems arise.

### `RDM_ORBOPT_FREQUENCY`

> **The number of v2RDM iterations after which the orbital optimization routine is called.**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * $N>0$
> * **Recommendation**: Use default unless convergence problems arise.
