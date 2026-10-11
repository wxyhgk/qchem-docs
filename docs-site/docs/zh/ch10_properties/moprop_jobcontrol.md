---
title: "10.10.3 Job Control for the MOProp Module"
---

## 10.10.3 Job Control for the MOProp Module

(July 4, 2026)

The MOProp module is invoked by specifying a job number using the
MOPROP *$rem* variable. In addition to electric properties, this
module can also compute NMR chemical shifts (MOPROP = NMR); this
functionality is described in Section [10.11](sec_magnetic.md).

MOPROP

### `MOPROP`

> **Specifies the job number for MOProp module.**
>
> * **Type**: `STRING`
> * **Default**: `0`
> * **Options**:
>     * NMR
>     * NMR chemical shielding tensors.
>     * STATIC_POLAR
>     * Static polarizability.
>     * ISSC
>     * Indirect nuclear spin–spin coupling tensors.
>     * DYN_POLAR
>     * Dynamic polarizability.
>     * HYPERPOL
>     * First hyperpolarizability using Wigner’s
>     * $2n+1$
>     * rule.
> * **Recommendation**: None

MOPROP_PERTNUM

### `MOPROP_PERTNUM`

> **Set the number of perturbed densities that will to be treated together.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * All at once.
>     * $n$
>     * Treat the perturbed densities batch-wise.
> * **Recommendation**: Use the default. For large systems, limiting this number may be required to avoid memory exhaustion.

MOPROP_CONV_1ST

### `MOPROP_CONV_1ST`

> **Sets the convergence criteria for CPSCF and 1st order TDSCF.**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n<10$
>     * Convergence threshold set to
>     * $10^{-n}$
>     * .
> * **Recommendation**: None

MOPROP_CONV_2ND

### `MOPROP_CONV_2ND`

> **Sets the convergence criterion for second-order TDSCF.**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n<10$
>     * Convergence threshold set to
>     * $10^{-n}$
>     * .
> * **Recommendation**: None

MOPROP_MAXITER_1ST

### `MOPROP_MAXITER_1ST`

> **The maximum number of iterations for CPSCF and first-order TDSCF.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $n$
>     * Set maximum number of iterations to
>     * $n$
>     * .
> * **Recommendation**: Use the default.

MOPROP_MAXITER_2ND

### `MOPROP_MAXITER_2ND`

> **The maximum number of iterations for second-order TDSCF.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $n$
>     * Set maximum number of iterations to
>     * $n$
>     * .
> * **Recommendation**: Use the default.

MOPROP_ISSC_PRINT_REDUCED

### `MOPROP_ISSC_PRINT_REDUCED`

> **Specifies whether the isotope-independent reduced coupling tensor $\mathbf{K}$ should be printed in addition to the isotope-dependent $\mathbf{J}$ -tensor when calculating indirect nuclear spin-spin couplings.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not print
>     * $\mathbf{K}$
>     * .
>     * TRUE
>     * Print
>     * $\mathbf{K}$
>     * .
> * **Recommendation**: None

MOPROP_ISSC_SKIP_FC

### `MOPROP_ISSC_SKIP_FC`

> **Specifies whether to skip the calculation of the Fermi contact contribution to the indirect nuclear spin-spin coupling tensor.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Calculate Fermi contact contribution.
>     * TRUE
>     * Skip Fermi contact contribution.
> * **Recommendation**: None

MOPROP_ISSC_SKIP_SD

### `MOPROP_ISSC_SKIP_SD`

> **Specifies whether to skip the calculation of the spin-dipole contribution to the indirect nuclear spin-spin coupling tensor.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Calculate spin-dipole contribution.
>     * TRUE
>     * Skip spin-dipole contribution.
> * **Recommendation**: None

MOPROP_ISSC_SKIP_PSO

### `MOPROP_ISSC_SKIP_PSO`

> **Specifies whether to skip the calculation of the paramagnetic spin-orbit contribution to the indirect nuclear spin-spin coupling tensor.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Calculate paramagnetic spin-orbit contribution.
>     * TRUE
>     * Skip paramagnetic spin-orbit contribution.
> * **Recommendation**: None

MOPROP_ISSC_SKIP_DSO

### `MOPROP_ISSC_SKIP_DSO`

> **Specifies whether to skip the calculation of the diamagnetic spin-orbit contribution to the indirect nuclear spin-spin coupling tensor.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Calculate diamagnetic spin-orbit contribution.
>     * TRUE
>     * Skip diamagnetic spin-orbit contribution.
> * **Recommendation**: None

MOPROP_DIIS

### `MOPROP_DIIS`

> **Controls the use of Pulay’s DIIS in solving the CPSCF equations.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * 0
>     * Turn off DIIS.
>     * 5
>     * Turn on DIIS.
> * **Recommendation**: None

MOPROP_DIIS_DIM_SS

### `MOPROP_DIIS_DIM_SS`

> **Specified the DIIS subspace dimension.**
>
> * **Type**: `INTEGER`
> * **Default**: `20`
> * **Options**:
>     * 0
>     * No DIIS.
>     * $n$
>     * Use a subspace of dimension
>     * $n$
>     * .
> * **Recommendation**: None

SAVE_LAST_GPX

### `SAVE_LAST_GPX`

> **Save the last $\mathbf{G}[\mathbf{P}^{x}]$ when calculating dynamic polarizabilities in order to call the MOProp code in a second run, via MOPROP = 104 (which is otherwise the same as MOPROP = HYPERPOL).**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * False
>     * 1
>     * True
> * **Recommendation**: None

MOPROP_RESTART

### `MOPROP_RESTART`

> **Specifies the option for restarting MOProp calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Not a restart calculation.
>     * 1
>     * Restart from a previous calculation using the same scratch directory.
> * **Recommendation**: Need to also include "SCF_GUESS READ" and "SKIP_SCFMAN TRUE" to ensure the same set of MOs.
