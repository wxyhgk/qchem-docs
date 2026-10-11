---
title: "10.2.6 Localized Orbital Bonding Analysis"
---

## 10.2.6 Localized Orbital Bonding Analysis

(July 4, 2026)

Localized orbital bonding analysis (LOBA) is a technique
developed by Dr. Alex Thom and Eric Sundstrom at Berkeley with Prof. Martin
Head-Gordon.[[1357]](../bib_references/bib.md#bib1416)

Inspired by the work of Rhee and Head-Gordon,[[1163]](../bib_references/bib.md#bib1216)

it makes use of the fact that the post-SCF localized occupied orbitals of a system
provide a large amount of information about the bonding in the system.

While the canonical molecular orbitals can provide information about local
reactivity and ionization energies, their delocalized nature makes them rather
uninformative when looking at the bonding in larger molecules. Localized
orbitals in contrast provide a convenient way to visualize and account for
electrons. Transformations of the orbitals within the occupied subspace do not
alter the resultant density; if a density can be represented as orbitals
localized on individual atoms, then those orbitals can be regarded as
non-bonding. If a maximally localized set of orbitals still requires some to
be delocalized between atoms, these can be regarded as bonding electrons. A
simple example is that of He${}_{2}$ versus H${}_{2}$. In the former, the delocalized
$\sigma_{g}$ and $\sigma_{u}$ canonical orbitals may be transformed into 1s
orbitals on each He atom, and there is no bond between them. This is not
possible for the H${}_{2}$ molecule, and so we can regard there being a bond
between the atoms. In cases of multiple bonding, multiple delocalized orbitals
are required.

While there are no absolute definitions of bonding and oxidation state, it has
been shown that the localized orbitals match the chemically intuitive notions
of core, non-bonded, single- and double-bonded electrons, *etc.* By combining
these localized orbitals with population analyses, LOBA allows the nature of
the bonding within a molecule to be quickly determined.

In addition, it has been found that by counting localized electrons, the
oxidation states of transition metals can be easily found. Owing to
polarization caused by ligands, an upper threshold is applied, populations
above which are regarded as “localized” on an atom, which has been calibrated
to a range of transition metals, recovering standard oxidation states ranging
from $-$II to VII.

LOBA

### `LOBA`

> **Specifies the methods to use for LOBA**
>
> * **Type**: `INTEGER`
> * **Default**: `00`
> * **Options**:
>     * $ab$
>     * $a$
>     * specifies the localization method
>     * 0 Perform Boys localization.
>     * 1 Perform PM localization.
>     * 2 Perform ER localization.
>     * $b$
>     * specifies the population analysis method
>     * 0 Do not perform LOBA. This is the default.
>     * 1 Use Mulliken population analysis.
>     * 2 Use Löwdin population analysis.
> * **Recommendation**: Boys Localization is the fastest. ER will require an auxiliary basis set. LOBA 12 provides a reasonable speed/accuracy compromise.

LOBA_THRESH

### `LOBA_THRESH`

> **Specifies the thresholds to use for LOBA**
>
> * **Type**: `INTEGER`
> * **Default**: `6015`
> * **Options**:
>     * $aabb$
>     * $aa$
>     * specifies the threshold to use for localization
>     * $bb$
>     * specifies the threshold to use for occupation
>     * Both are given as percentages.
> * **Recommendation**: Decrease $bb$ to see the smaller contributions to orbitals. Values of $aa$ between 40 and 75 have been shown to given meaningful results.

On a technical note, LOBA can function of both restricted and unrestricted
SCF calculations. The figures printed in the bonding analysis count the number
of electrons on each atom from that orbital (*i.e.*, up to 1 for unrestricted
or singly occupied restricted orbitals, and up to 2 for double occupied restricted.)
