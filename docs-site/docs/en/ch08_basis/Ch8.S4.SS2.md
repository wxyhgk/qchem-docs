---
title: "8.4.2 Job Control"
---

## 8.4.2 Job Control

(July 4, 2026)

In order to use a user-defined basis set, the BASIS *$rem* must be
set to GENERAL or GEN.

When using a non-standard basis set which incorporates $d$ or higher angular
momentum basis functions, the *$rem* variable PURECART needs to be
set. This *$rem* variable indicates to the **Q-Chem** program how to handle the
angular form of the basis functions. As indicated above, each integer
represents an angular momentum type which can be defined as either pure (1) or
Cartesian (2). For example, 1111 specifies that $d$, $f$, $g$ and $h$ basis
functions should have pure form whereas 1121 indicates that $d$- $g$- and
$h$-functions are pure but $f$ functions are Cartesian. These four-digit
codes can be used even if the basis does not contain $g$ or $h$ functions;
PURECART = 1111 (or 2222) specifies to use pure (or Cartesian)
functions for all angular momentum types.

PURECART

### `PURECART`

> **INTEGER**
>
> * **Type**: `Controls the use of pure (spherical harmonic) or Cartesian angular forms`
> * **Default**: `1111`
> * **Options**:
>     * $hgfd$
>     * Use 1 for pure and 2 for Cartesian.
> * **Recommendation**: This is pre-defined for all standard basis sets

In standard basis sets all functions are pure, except for the $d$ functions
in $n$-21G–type bases (*e.g.*, 3-21G) and $n$-31G bases (*e.g.*, 6-31G,
6-31G*,6-31+G*, $\ldots$). In particular, the 6-311G series uses pure
functions for both $d$ and $f$.[[718]](../bib_references/bib.md#bib750)

Note that other electronic structure codes may use Cartesian functions
for basis sets of the same name, in which case absolute energies will differ.
Set PURECART = 2222 to request Cartesian Gaussian functions, if desired.
