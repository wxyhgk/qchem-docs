---
title: "10.2.3 Multipole Moments"
---

## 10.2.3 Multipole Moments

(July 4, 2026)

This section discusses how to compute arbitrary electrostatic multipole moments
for an entire molecule, including both ground- and excited-state electron
densities. Occasionally, however, it is useful to decompose the electronic
part of the multipole moments into contributions from individual MOs. This
decomposition is especially useful for systems containing unpaired
electrons,[[1471]](../bib_references/bib.md#bib1534)
 where the first-order moments $\langle x\rangle$, $\langle y\rangle$, and $\langle z\rangle$ characterize the
centroid (mean position) of the half-filled MO, and the second-order moments
determine its radius of gyration, $R_{g}$, which characterizes the size of the
MO. Upon setting PRINT_RADII_GYRE = TRUE, **Q-Chem** will print out
centroids and radii of gyration for each occupied MO and for the overall
electron density of the Hartree-Fock or Kohn-Sham reference determinant.
If CIS or TDDFT excited states are requested, then this
keyword will also print out the centroids and radii of gyration for each
excited-state electron density.

**Note: 

These keywords only apply to SCF, DFT, CIS, and TDDFT calculations.
To compute these quantities for correlated wave functions, use keywords that specify
properties calculations for the corresponding method, as described in
Chapters [6](../ch06_correlation/chap_correlation.md) and [7](../ch07_excited/chap_excited.md). For example, to compute
CCSD or EOM-CCSD multipole moments and other properties, use
CC_REF_PROP = TRUE and CC_EOM_PROP = TRUE.
**

PRINT_RADII_GYRE

### `PRINT_RADII_GYRE`

> **Controls printing of MO centroids and radii of gyration.**
>
> * **Type**: `LOGICAL/INTEGER`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE (or 1)
>     * Print the centroid and radius of gyration for each occupied MO
>     * and each density.
>     * 2
>     * Print centroids and radii of gyration for the virtual MOs as well.
>     * FALSE (or 0)
>     * Do not calculate these quantities.
> * **Recommendation**: None

**Q-Chem** can compute Cartesian multipole moments of the charge density to
arbitrary order, both for the ground state and for excited states
calculated using the CIS or TDDFT methods.

MULTIPOLE_ORDER

### `MULTIPOLE_ORDER`

> **Determines highest order of multipole moments to print if wave function analysis requested.**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $n$
>     * Calculate moments to
>     * $n$
>     * th order.
> * **Recommendation**: Use the default unless higher multipoles are required.

CIS_MOMENTS

### `CIS_MOMENTS`

> **Controls calculation of excited-state (CIS or TDDFT) multipole moments**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not calculate excited-state moments.
>     * TRUE
>     * Calculate moments for each excited state.
> * **Recommendation**: Set to TRUE if excited-state moments are desired. (This is a trivial additional calculation.) The MULTIPOLE_ORDER controls how many multipole moments are printed.
