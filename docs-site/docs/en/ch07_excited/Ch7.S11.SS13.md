---
title: "7.11.13 Job Control Options for casman"
---

## 7.11.13 Job Control Options for **casman**

(July 4, 2026)

In **casman**, the built-in methods can be run by simply setting the value of CORRELATION accordingly:

CORRELATION

### `CORRELATION`

> **Sets the pre-defined method to use for casman .**
>
> * **Type**: `STRING`
> * **Default**: `None.`
> * **Options**:
>     * SF-CAS
>     * CAS-SF with no perturbative corrections (or a custom method)
>     * SF-CAS(h,p)
>     * CAS-SF with perturbative corrections for hole (h) and particle (p) excitations
>     * SF-CAS(S)
>     * CAS-SF with perturbative corrections for single (h,p,hp) excitations
>     * SF-CAS(2x)
>     * CAS-SF with perturbative corrections for 2x (h,p,hp,hh,pp) excitations
>     * SF-CAS(3x)
>     * CAS-SF with perturbative corrections for 3x (h,p,hp,hh,pp,hhp,hpp) excitations
>     * SF-CAS(3x)+D
>     * CAS-SF with perturbative corrections for (h,p,hp,hh,pp,hhp,hpp) + MP2 RAS1
>     * $\rightarrow$
>     * RAS3 double excitations
> * **Recommendation**: None.

If a custom excitation scheme is required, one can set CORRELATION = SF-CAS and
set the following variables manually. (If you are using one of the built-in methods, setting these
variables manually should be avoided, since they are automatically set up appropriately
by **Q-Chem** if CORRELATION is not SF-CAS.)

RAS_N_SPIN_FLIP

### `RAS_N_SPIN_FLIP`

> **Sets the number of spin-flips.**
>
> * **Type**: `INTEGER`
> * **Default**: `Maximum number of spin-flips (`
> * **Options**:
>     * $n$
>     * Do
>     * $n$
>     * spin-flips
> * **Recommendation**: None.

CAS_DO_NDPT

### `CAS_DO_NDPT`

> **Do non-degenerate perturbation theory?**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Do non-degenerate perturbation theory.
>     * FALSE
>     * Do not use non-degenerate perturbation theory.
> * **Recommendation**: None.

CAS_QDPT_ORDER

### `CAS_QDPT_ORDER`

> **Order of terms kept in the quasi-degenerate perturbation theory denominator expansion.**
>
> * **Type**: `INTEGER`
> * **Default**: `None.`
> * **Options**:
>     * $n$
>     * Keep terms of order
>     * $n$
>     * in the denominator expansion.
> * **Recommendation**: None.

CAS_DO_1X

### `CAS_DO_1X`

> **Do perturbative hole (h) and particle (p) correction?**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Do perturbative hole (h) and particle (p) correction
>     * FALSE
>     * Do not do perturbative hole (h) and particle (p) correction
> * **Recommendation**: None.

CAS_DO_SINGLES

### `CAS_DO_SINGLES`

> **Do perturbative singles (h,p,hp) correction?**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Do perturbative singles correction
>     * FALSE
>     * Do not do perturbative singles correction
> * **Recommendation**: None.

CAS_DO_2x

### `CAS_DO_2x`

> **Do perturbative 2x (h,p,hp,hh,pp) correction?**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Do perturbative 2x correction
>     * FALSE
>     * Do not do perturbative 2x correction
> * **Recommendation**: None.

CAS_DO_3x

### `CAS_DO_3x`

> **Do perturbative 3x (h,p,hp,hh,pp,hhp,hpp) correction?**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Do perturbative 3x correction
>     * FALSE
>     * Do not do perturbative 3x correction
> * **Recommendation**: None.

CAS_DO_DOUBLES

### `CAS_DO_DOUBLES`

> **Do perturbative (h,p,hp,hh,pp,hhp,hpp) correction + MP2 RAS1 $\rightarrow$ RAS3 doubles?**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Do perturbative (h,p,hp,hh,pp,hhp,hpp) + MP2 RAS1
>     * $\rightarrow$
>     * RAS3 doubles correction
>     * FALSE
>     * Do not do the correction
> * **Recommendation**: None.

CAS_LEVEL_SHIFT

### `CAS_LEVEL_SHIFT`

> **Use a denominator level-shift?**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Use the denominator level-shift
>     * FALSE
>     * Do not use the denominator level-shift
> * **Recommendation**: None.

CAS_SPARSE

### `CAS_SPARSE`

> **Use a sparse matrix multiply when forming the effective Hamiltonian?**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Use sparse matrix multiply in forming effective Hamiltonian
>     * FALSE
>     * Do not use sparse matrix multiply in forming effective Hamiltonian
> * **Recommendation**: None. Can be useful for larger numbers of spin-flips.
