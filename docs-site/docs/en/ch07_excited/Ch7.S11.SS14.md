---
title: "7.11.14 Job Control Options for librassf"
---

## 7.11.14 Job Control Options for **librassf**

(July 4, 2026)

The **librassf** module can be enabled by setting EXCHANGE = HF,
CORRELATION = RASCI2, and LIBRASSF = 1 in the
*$rem* variable section. One should also indicate the number of roots
by setting RAS_N_ROOTS appropriately. Although the module
is called through RASCI2, most job control options are more similar to
those found in RASCI1, with the exception of RAS_N_ROOTS.

The number of spin-flips and IP/EA are determined by the *$rem* variables
RASSF_DELTA_ALPHA (the number of alpha electrons removed) and
RASSF_DELTA_BETA (the number of beta electrons added). Hole
and particle excitations can be added by setting the RAS_DO_HOLE
and RAS_DO_PART keywords. Additionally, text files containing
eigenvalues and eigenvectors can be printed via the
RASSF_WRITE_EVALS and RASSF_WRITE_EVECS keywords.

RAS_N_ROOTS

### `RAS_N_ROOTS`

> **Sets the number of RAS-CI roots to be computed.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$
>     * $n>0$
>     * Compute
>     * $n$
>     * RAS-CI states
> * **Recommendation**: None.

RASSF_DELTA_ALPHA

### `RASSF_DELTA_ALPHA`

> **Sets the number of alpha electrons to remove relative to the reference.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $0$
>     * Remove no alpha electrons (use for EA)
>     * $1$
>     * Remove one alpha electron (use for 1SF, IP)
>     * $2$
>     * Remove two alpha electrons (use for 2SF, 1SF-IP)
> * **Recommendation**: None.

RASSF_DELTA_BETA

### `RASSF_DELTA_BETA`

> **Sets the number of beta electrons to add relative to the reference.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $0$
>     * Add no beta electrons (use for IP)
>     * $1$
>     * Add one beta electron (use for 1SF, EA)
>     * $2$
>     * Add two beta electrons (use for 2SF, 1SF-EA)
> * **Recommendation**: None.

RAS_DO_HOLE

### `RAS_DO_HOLE`

> **Enables hole excitations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $0$
>     * No hole excitations (use for CAS or RAS(p))
>     * $1$
>     * Single hole excitations (use for RAS(h) or RAS(h,p))
> * **Recommendation**: None.

RAS_DO_PART

### `RAS_DO_PART`

> **Enables particle excitations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $0$
>     * No particle excitations (use for CAS or RAS(h))
>     * $1$
>     * Single particle excitations (use for RAS(p) or RAS(h,p))
> * **Recommendation**: None.

N_FROZEN_CORE

### `N_FROZEN_CORE`

> **Number of frozen core orbitals.**
>
> * **Type**: `SIZE_T`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * $n\geq 0$
>     * Number of frozen core orbitals.
> * **Recommendation**: None.

N_FROZEN_VIRTUAL

### `N_FROZEN_VIRTUAL`

> **Number of frozen virtual orbitals.**
>
> * **Type**: `SIZE_T`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * $n\geq 0$
>     * Number of frozen virtual orbitals.
> * **Recommendation**: None.

RASSF_GUESS

### `RASSF_GUESS`

> **Determines which initial set of guess vectors to use for Davidson.**
>
> * **Type**: `INTEGER`
> * **Default**: `$2$`
> * **Options**:
>     * $0$
>     * Random orthonormal guess (default for CAS)
>     * $1$
>     * Identity guess
>     * $2$
>     * CAS guess (default for RAS)
> * **Recommendation**: Starting from a CAS guess is recommended for larger molecules. If Davidson encounters issues with linearly dependent eigenvectors, consider using identity. The random orthonormal guess requires building a large $NxN$ matrix and is therefore only recommended for calculations with fewer determinants.

RASSF_WRITE_EVALS

### `RASSF_WRITE_EVALS`

> **Determines whether to write eigenvalues to an output file.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $0$
>     * Do not write eigenvalues to an output file
>     * $1$
>     * Write eigenvalues to an output file
> * **Recommendation**: None.

RASSF_WRITE_EVECS

### `RASSF_WRITE_EVECS`

> **Determines whether to write eigenvectors to an output file.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $0$
>     * Do not write eigenvectors to an output file
>     * $1$
>     * Write eigenvectors to an output file
> * **Recommendation**: None.

CAS_LOCAL

### `CAS_LOCAL`

> **Determines whether to do localization.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $0$
>     * No localization
>     * $1$
>     * Boys localization
>     * $2$
>     * Pipek-Mezey localization
> * **Recommendation**: None.

CAS_LOCAL_ALGO

### `CAS_LOCAL_ALGO`

> **Passed into localizer. Set to 1 if doing Boys localization.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $0$
>     * No localization
>     * $1$
>     * Boys localization
>     * $2$
>     * Pipek-Mezey localization
> * **Recommendation**: None.

RASSF_DO_BLOCH

### `RASSF_DO_BLOCH`

> **Determines whether to do effective Hamiltonian analysis.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $0$
>     * Skip analysis
>     * $1$
>     * Do effective Hamiltonian analysis
> * **Recommendation**: None.
