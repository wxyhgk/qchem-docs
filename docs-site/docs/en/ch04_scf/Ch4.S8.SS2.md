---
title: "4.8.2 Job Control"
---

## 4.8.2 Job Control

(July 4, 2026)

HFPC/DFPC calculations are controlled with the following *$rem*. HFPT
turns on the HFPC/DFPC approximation. Note that HFPT_BASIS specifies
the secondary basis set.

### `HFPT`

> **Activates HFPC/DFPC calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `Single-point energy only`
> * **Recommendation**: Use Dual-Basis to capture large-basis effects at smaller basis cost. See reference for recommended basis set, functional, and grid pairings.

### `HFPT_BASIS`

> **Specifies the secondary basis in a HFPC/DFPC calculation.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `None`
> * **Recommendation**: See reference for recommended basis set, functional, and grid pairings.

### `DFPT_XC_GRID`

> **Specifies the secondary grid in a HFPC/DFPC calculation.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `None`
> * **Recommendation**: See reference for recommended basis set, functional, and grid pairings.

### `DFPT_EXCHANGE`

> **Specifies the secondary functional in a HFPC/DFPC calculation.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `None`
> * **Recommendation**: See reference for recommended basis set, functional, and grid pairings.
