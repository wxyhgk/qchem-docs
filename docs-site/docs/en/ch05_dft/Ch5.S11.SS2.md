---
title: "5.11.2 Manner of Counting Electrons"
---

## 5.11.2 Manner of Counting Electrons

(July 4, 2026)

## Becke Partition:

In density functional theory calculations, the integration over the total density is
evaluated on a molecular grid that is systematically broken up into interlocking
multi-center atomic quadrature grids.[[94]](../bib_references/bib.md#bib73)
 This atomic quadrature
scheme is predicated on the definition of atomic cell functions $P_{a}(\textbf{r})$,
that define smoothed Voronoi polyhedra centered about each atom. These cell
functions are products of switching functions that define the atomic cell of atom
$a$, and fall rapidly from $\approx 1$ near the nucleus of $a$, to $\approx 0$
near any other nucleus. The integration weights provided by this scheme are
multiplied into the Lebedev quadrature weights in any practical DFT calculation:

<a id="eq:_becke_cell"></a>

$$
w_{n}(\mathbf{r})=\frac{P_{n}(\mathbf{r})}{\sum\limits_{m}P_{m}(\mathbf{r})} \tag{5.72}
$$

In some cases, it may be useful to print out the atomic Becke populations that
are defined by these atomic cell functions. Becke population analysis may be
requested by setting POP_BECKE to TRUE in the input file.

POP_BECKE

### `POP_BECKE`

> **Controls the printing of atomic Becke populations.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Print atomic Becke populations.
>     * FALSE
>     * Do not print atomic Becke populations.
> * **Recommendation**: None

The default quadrature scheme uses atomic cell functions that intersect
precisely at bond midpoints. Consequently, the default atomic cell functions
will yield physically meaningless atomic populations. However, it is possible
to shift the intersect of the atomic cell functions using an atomic radius
criterion.[[94]](../bib_references/bib.md#bib73)
 In shifting the intersect of neighboring atomic
cell functions, the point at which the Becke weights begin to fall from
$\approx 1$ to $\approx 0$ changes depending on the atomic radius of each atom.
While the choice of atomic radius is arbitrary, these atomic cell shifts
introduce a physical basis for the partitioning of the underlying atomic
quadrature. Two choices for atomic radii exist in **Q-Chem** for use with Becke
weights, namely the empirically derived radii introduced by Bragg and
Slater[[1268]](../bib_references/bib.md#bib1321)
 and the *ab initio*-derived weights
due to Pacios.[[1034]](../bib_references/bib.md#bib1077)

BECKE_SHIFT

### `BECKE_SHIFT`

> **Controls atomic cell shifting in determination of Becke weights.**
>
> * **Type**: `STRING`
> * **Default**: `BRAGG_SLATER`
> * **Options**:
>     * UNSHIFTED
>     * Use Becke weighting without atomic size corrections,
>     * based on bond midpoints.
>     * BRAGG_SLATER
>     * Use the empirical radii introduced by Bragg and Slater.
>     * UNIVERSAL_DENSITY
>     * Use the
>     * ab initio
>     * radii introduced by Pacios.
> * **Recommendation**: If interested in the partitioning of the default atomic quadrature, use UNSHIFTED . If using for physical interpretation, choose BRAGG_SLATER or UNIVERSAL_DENSITY . All cDFT calculations and calculations where POP_BECKE = TRUE will default to BRAGG_SLATER radii, otherwise the default grid is UNSHIFTED .

## Fragment-Based Hirshfeld Partition:

A much less arbitrary scheme with which to count electrons comes from the fragment-based Hirshfeld
partition.[[1160]](../bib_references/bib.md#bib1214)

The fragment-based Hirshfeld (FBH) partition uses weights constructed from isolated fragment densities in the form,

<a id="Ch5.E73"></a>

$$
w_{n}(\text{{r}})=\frac{\rho_{n}(\text{{r}})}{\sum\limits_{m}\rho_{m}(\text{{r}})}~{}, \tag{5.73}
$$

where $\rho_{n}(\text{{r}})$ is the density of the isolated fragment, $n$.
Note that unlike the atomic Becke partition, the FBH partition is not
constructed from linear combinations of atomic weights, but is instead built from whole fragment densities.
The FBH partition comes directly from the densities of the isolated fragments,
which are not as arbitrary as the choosing the effective atomic radii in the Becke partition.
In order to apply FBH partitioning, one must define fragments within the *$molecule* section
to host the constraints, but the input for the *$cdft* section remains unchanged and still applies
constraints on a per-atom basis.

CDFT_POP

### `CDFT_POP`

> **Sets the charge partitioning scheme for cDFT or cDFT-CI jobs.**
>
> * **Type**: `STRING`
> * **Default**: `BECKE`
> * **Options**:
>     * BECKE
>     * Linear combination of atomic Becke functions
>     * FBH
>     * Fragment-based Hirshfeld partition
> * **Recommendation**: None
