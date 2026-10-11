---
title: "5.5.5 Multi-resolution Exchange-Correlation (MRXC) Method"
---

## 5.5.5 Multi-resolution Exchange-Correlation (MRXC) Method

(July 4, 2026)

The multi-resolution exchange-correlation (MRXC) method is a new approach, courtesy of the
**Q-Chem** development team,[[706]](../bib_references/bib.md#bib738)

for accelerating computation of the exchange-correlation (XC) energy and matrix for any
given density functional.
As explained in Section [4.6.5](../ch04_scf/sect_FTC.md), XC functionals are sufficiently complicated integration
of them is usually performed by numerical quadrature.
There are two basic types of quadrature. One is the atom-centered
grid (ACG), a superposition of atomic quadrature described in Section [4.6.5](../ch04_scf/sect_FTC.md).
The ACG has high density of points near the nucleus to handle the compact core
density and low density of points in the valence and non-bonding region where
the electron density is smooth. The other type is even-spaced cubic grid
(ESCG), which is typically used together with pseudopotentials and plane-wave
basis functions where only the valence and non-bonded electron density is
assumed smooth. In quantum chemistry, an ACG is more often used as it can
handle accurately all-electron calculations of molecules. MRXC combines those
two integration schemes seamlessly to achieve an optimal computational
efficiency by placing the calculation of the smooth part of the density and XC
matrix onto the ESCG. The computation associated with the smooth fraction of
the electron density is the major bottleneck of the XC part of a DFT
calculation and can be done at a much faster rate on the ESCG due to its low
resolution. Fast Fourier transform and B-spline interpolation are employed for
the accurate transformation between the two types of grids such that the final
results remain the same as they would be on the ACG alone, yet a speedup of
several times is achieved for the XC matrix.
The smooth part of the calculation with MRXC can also be combined
with FTC (see Section [4.6.5](../ch04_scf/sect_FTC.md)) to achieve a further gain in efficiency.

MRXC

### `MRXC`

> **Controls the use of MRXC.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not use MRXC
>     * 1
>     * Use MRXC in the evaluation of the XC part
> * **Recommendation**: MRXC is very efficient for medium and large molecules, especially when medium and large basis sets are used.

The following two keywords control the smoothness precision. The default value
is carefully selected to maintain high accuracy.

MRXC_CLASS_THRESH_MULT

### `MRXC_CLASS_THRESH_MULT`

> **Controls the of smoothness precision**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $im$
>     * An integer
> * **Recommendation**: A prefactor in the threshold for MRXC error control: $im\times 10^{-io}$

MRXC_CLASS_THRESH_ORDER

### `MRXC_CLASS_THRESH_ORDER`

> **Controls the of smoothness precision**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $io$
>     * An integer
> * **Recommendation**: The exponent in the threshold of the MRXC error control: $im\times 10^{-io}$

The next keyword controls the order of the B-spline interpolation:

LOCAL_INTERP_ORDER

### `LOCAL_INTERP_ORDER`

> **Controls the order of the B-spline**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n$
>     * An integer
> * **Recommendation**: The default value is sufficiently accurate
