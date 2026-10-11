---
title: "5.4.1 Overview"
---

## 5.4.1 Overview

(July 4, 2026)

Basic SCF job control was described in Section [4.3](../ch04_scf/sec_SCF_job-control.md) in the
context of Hartree-Fock theory and is largely the same for DFT. The keywords
METHOD and BASIS are required, although for DFT the former
could be substituted by specifying EXCHANGE and CORRELATION
instead.

Starting Q-Chem v7.0, MPI+OMP-parallel DFT calculations are available with the
replicated-Fock approach for the RHF, UHF, and ROHF ans̈atze and DIIS, GDM,
and the robust SCF algorithms, similar to HF SCF calculations
(Section [4.3](../ch04_scf/sec_SCF_job-control.md)).

METHOD

### `METHOD`

> **Specifies the exchange-correlation functional.**
>
> * **Type**: `STRING`
> * **Default**: `No default`
> * **Options**:
>     * NAME
>     * Use
>     * =
>     * NAME
>     * , where
>     * NAME
>     * is either
>     * HF
>     * for Hartree-Fock theory or
>     * else one of the DFT methods listed in Section
>     * 5.3.5
>     * .
> * **Recommendation**: In general, consult the literature to guide your selection. Our recommendations for DFT are indicated in bold in Section 5.3.5 .

EXCHANGE

### `EXCHANGE`

> **Specifies the exchange functional (or most exchange-correlation functionals for backwards compatibility).**
>
> * **Type**: `STRING`
> * **Default**: `No default`
> * **Options**:
>     * NAME
>     * Use
>     * =
>     * NAME
>     * , where
>     * NAME
>     * is either:
>     * 1) One of the exchange functionals listed in Section
>     * 5.3.3
>     * 2) One of the XC functionals listed in Section
>     * 5.3.5
>     * that is not marked with an
>     * asterisk.
>     * 3)
>     * GEN
>     * , for a user-defined functional (see Section
>     * 5.3.7
>     * ).
> * **Recommendation**: In general, consult the literature to guide your selection. Our recommendations are indicated in bold in Sections 5.3.5 and 5.3.3 .

CORRELATION

### `CORRELATION`

> **Specifies the correlation functional.**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * NAME
>     * Use
>     * =
>     * NAME
>     * , where
>     * NAME
>     * is one of the correlation functionals
>     * listed in Section
>     * 5.3.4
>     * .
> * **Recommendation**: In general, consult the literature to guide your selection. Our recommendations are indicated in bold in Section 5.3.4 .

The following *$rem* variables are related to the choice of the quadrature grid required to integrate the XC part of the
functional, which does not appear in Hartree-Fock theory. DFT quadrature grids are described in Section [5.5](sect_quadrature.md).

FAST_XC

### `FAST_XC`

> **Controls direct variable thresholds to accelerate exchange-correlation (XC) in DFT.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Turn
>     * on.
>     * FALSE
>     * Do not use
>     * .
> * **Recommendation**: Caution: improves the speed of a DFT calculation, but may occasionally cause the SCF calculation to diverge.

XC_GRID

### `XC_GRID`

> **Specifies the type of grid to use for DFT calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `Functional-dependent; see Table`
> * **Options**:
>     * 0
>     * Use SG-0 for H, C, N, and O; SG-1 for all other atoms.
>     * $n$
>     * Use SG-
>     * $n$
>     * for all atoms,
>     * $n=1,2$
>     * , or 3
>     * $XY$
>     * A string of two six-digit integers
>     * $X$
>     * and
>     * $Y$
>     * , where
>     * $X$
>     * is the number of radial points
>     * and
>     * $Y$
>     * is the number of angular points where possible numbers of Lebedev angular
>     * points, which must be an allowed value from Table
>     * 5.2
>     * in
>     * Section
>     * 5.5
>     * .
>     * $-XY$
>     * Similar format for Gauss-Legendre grids, with the six-digit integer
>     * $X$
>     * corresponding
>     * to the number of radial points and the six-digit integer
>     * $Y$
>     * providing the number of
>     * Gauss-Legendre angular points,
>     * $Y=2N^{2}$
>     * .
> * **Recommendation**: Use the default unless numerical integration problems arise. Larger grids may be required for optimization and frequency calculations.

NL_GRID

### `NL_GRID`

> **Specifies the grid to use for non-local correlation.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * Same as for XC_GRID
> * **Recommendation**: Use the default unless computational cost becomes prohibitive, in which case SG-0 may be used. XC_GRID should generally be finer than NL_GRID.

XC_SMART_GRID

### `XC_SMART_GRID`

> **Uses SG-0 (where available) for early SCF cycles, and switches to the (larger) target grid specified by XC_GRID for final cycles of the SCF.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE (or 1)
>     * Use the smaller grid for the initial cycles.
>     * FALSE (or 0)
>     * Use the target grid for all SCF cycles.
> * **Recommendation**: The use of the smart grid can save some time on initial SCF cycles.
