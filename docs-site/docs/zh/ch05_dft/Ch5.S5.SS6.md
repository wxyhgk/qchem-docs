---
title: "5.5.6 Incremental DFT"
---

## 5.5.6 Incremental DFT

(July 4, 2026)

Incremental DFT (IncDFT) uses the difference density and functional values to improve the
performance of the DFT quadrature procedure by providing a better screening of negligible
values. Using this option will yield improved efficiency at each successive iteration
due to more effective screening.

INCDFT

### `INCDFT`

> **Toggles the use of the IncDFT procedure for DFT energy calculations.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * FALSE
>     * Do not use IncDFT
>     * TRUE
>     * Use IncDFT
> * **Recommendation**: Turning this option on can lead to faster SCF calculations, particularly towards the end of the SCF. Please note that for some systems use of this option may lead to convergence problems.

INCDFT_DENDIFF_THRESH

### `INCDFT_DENDIFF_THRESH`

> **Sets the threshold for screening density matrix values in the IncDFT procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `SCF_CONVERGENCE`
> * **Options**:
>     * $n$
>     * Corresponding to a threshold of
>     * $10^{-n}$
>     * .
> * **Recommendation**: If the default value causes convergence problems, set this value higher to tighten the threshold.

INCDFT_GRIDDIFF_THRESH

### `INCDFT_GRIDDIFF_THRESH`

> **Sets the threshold for screening functional values in the IncDFT procedure**
>
> * **Type**: `INTEGER`
> * **Default**: `SCF_CONVERGENCE`
> * **Options**:
>     * $n$
>     * Corresponding to a threshold of
>     * $10^{-n}$
>     * .
> * **Recommendation**: If the default value causes convergence problems, set this value higher to tighten the threshold.

INCDFT_DENDIFF_VARTHRESH

### `INCDFT_DENDIFF_VARTHRESH`

> **Sets the lower bound for the variable threshold for screening density matrix values in the IncDFT procedure. The threshold will begin at this value and then vary depending on the error in the current SCF iteration until the value specified by INCDFT_DENDIFF_THRESH is reached. This means this value must be set lower than INCDFT_DENDIFF_THRESH .**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Corresponding to a threshold of
>     * $10^{-n}$
>     * .
> * **Recommendation**: If the default value causes convergence problems, set this value higher to tighten accuracy. If this fails, set to 0 and use a static threshold.

INCDFT_GRIDDIFF_VARTHRESH

### `INCDFT_GRIDDIFF_VARTHRESH`

> **Sets the lower bound for the variable threshold for screening the functional values in the IncDFT procedure. The threshold will begin at this value and then vary depending on the error in the current SCF iteration until the value specified by INCDFT_GRIDDIFF_THRESH is reached. This means that this value must be set lower than INCDFT_GRIDDIFF_THRESH .**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Corresponding to a threshold of
>     * $10^{-n}$
>     * .
> * **Recommendation**: If the default value causes convergence problems, set this value higher to tighten accuracy. If this fails, set to 0 and use a static threshold.
