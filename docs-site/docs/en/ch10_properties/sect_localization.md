---
title: "10.3.2 Orbital Localization"
---

## 10.3.2 Orbital Localization

(July 4, 2026)

## 10.3.2.1 Overview

The concept of localized orbitals has already been visited in this manual in
the context of perfect-pairing and methods. As the SCF energy is independent
of the partitioning of the electron density into orbitals, there is
considerable flexibility as to how this may be done. The canonical picture,
where the orbitals are eigenfunctions of the Fock operator is useful in
determining reactivity, for, through Koopmans’ theorem, the orbital energy
eigenvalues give information about the corresponding ionization energies and
electron affinities. As a consequence, the HOMO and LUMO are very informative
as to the reactive sites of a molecule. In addition, in small molecules, the
canonical orbitals lead us to the chemical description of $\sigma$ and $\pi$ bonds.

In large molecules, however, the canonical orbitals are often very delocalized,
and so information about chemical bonding is not readily available from them.
Here, orbital localization techniques can be of great value in visualizing the
bonding, as localized orbitals often correspond to the chemically intuitive
orbitals which might be expected.

**Q-Chem** has three post-SCF localization methods available. These can be
performed separately over both occupied and virtual spaces. The localization
scheme attributed to Boys[[154]](../bib_references/bib.md#bib146)
 minimizes the radial
extent of the localized orbitals, *i.e.*, the second moment $\sum_{i}\langle ii||{\bf r}_{1}-{\bf r}_{2}|^{2}|ii\rangle$, and although is relatively fast, does not separate
$\sigma$ and $\pi$ orbitals, leading to two “banana-orbitals” in the case of a
double bond.[[1093]](../bib_references/bib.md#bib1138)
 Pipek-Mezey localized
orbitals[[1093]](../bib_references/bib.md#bib1138)
 maximize the locality of Mulliken populations, and
are of a similar cost to Boys localized orbitals, but maintain $\sigma-\pi$
separation. Edmiston-Ruedenberg localized orbitals[[361]](../bib_references/bib.md#bib366)

maximize the self-repulsion of the orbitals, $\sum_{i}\langle ii|\frac{1}{r}|ii\rangle$. This is more computationally expensive to calculate
as it requires a two-electron property to be evaluated, but can be reduced to
cubic-scaling cost (with respect to the number of occupied orbitals),
via the resolution of identity approximation.[[1320]](../bib_references/bib.md#bib1378)

### `BOYSCALC`

> **Specifies how Boys localized orbitals are to be calculated**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not perform any Boys localization.
>     * `1`: Localize core and valence together.
>     * `2`: Do separate localizations on core and valence.
> * **Recommendation**: None

### `ERCALC`

> **Specifies how Edmiston-Ruedenberg localized orbitals are to be calculated**
>
> * **Type**: `INTEGER`
> * **Default**: `06000`
> * **Options**:
>     * $aabcd$: $aa$ specifies the convergence threshold. If $aa>3$ , the threshold is set to $10^{-aa}$ . The default is 6. If $aa=1$ , the calculation is aborted after the guess, allowing Pipek-Mezey orbitals to be extracted. $b$ specifies the guess: 0 Boys localized orbitals. This is the default 1 Pipek-Mezey localized orbitals. $c$ specifies restart options (if restarting from an ER calculation): 0 No restart. This is the default 1 Read in MOs from last ER calculation. 2 Read in MOs and RI integrals from last ER calculation. $d$ specifies how to treat core orbitals 0 Do not perform ER localization. This is the default. 1 Localize core and valence together. 2 Do separate localizations on core and valence. 3 Localize only the valence electrons. 4 Use the $localize section.
> * **Recommendation**: ERCALC 1 will usually suffice, which uses threshold $10^{-6}$ .

The *$localize* section may be used to specify orbitals subject to ER
localization if require. It contains a list of the orbitals to include in the
localization. These may span multiple lines. If the user wishes to specify
separate beta orbitals to localize, include a zero before listing the beta
orbitals, which acts as a separator, *e.g.*,

> ```qchem
> $localize
>    2 3 4 0
>    2 3 4 5 6
> $end
> ```

## 10.3.2.2 Virtual Orbital Localization

Virtual orbitals can be advantageous to be localized in many scenarios. One
scenario where this is useful is generalized valence bond (GVB) methods, where
each bonding orbital is paired with its antibonding orbital through Sano
procedure. Currently this is done in GVBMAN when PP or CCVB is run. An
improved guess has been proposed that has been shown to converge
faster.[[37]](../bib_references/bib.md#bib20)
 The new subroutine is a stand-alone version that
can generate these antibonding orbitals and exit without initiating a GVB
calculation. It can do Boys, Pipek-Mezey, or Edmiston-Rudenberg localization
for the occupied space depending on GVB_LOCAL = 1, 2, or 3,
respectively, while 0 performs it on the canonical orbitals. The subroutine
also prints out each occupied orbital’s Mulliken charge, delocalization
measure, and variance, in which it automatically detects the bonding orbitals
and generates an antibonding guess for each. A population analysis based on
this effective minimal basis can also be done using EDA_POP_ANAL = 1.
The number of bonds can be enforced by taking the highest
GVB_N_PAIRS specified, with no guarantee of them being bonding,
*i.e.* they can be core or lone pairs. This is currently implemented for
restricted and restricted Open-shell spin symmetries; work on the unrestricted case is underway.

### `ANTIBOND`

> **Triggers Antibond subroutine to generate antibonding orbitals after a converged SCF**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Does not localize the virtual space.
>     * `1`: Localizes the virtual space, one antibonding for every bond.
>     * `2,3`: Fill the virtual space with antibonding orbitals-like guesses.
>     * `4`: Does Frozen Natural Orbitals and leaves them on scratch for future jobs or visualization.
> * **Recommendation**: None

### `DOMODSANO`

> **Specifies whether to do modified Sano or the original one**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Does original Sano procedure (similar to GVBMAN).
>     * `1`: Does an improved Sano procedure that’s more localized.
>     * `2`: Does another variation of Sano.
> * **Recommendation**: 1 is always better
