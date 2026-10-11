---
title: "10.8.5 Localized Mode Vibrational Analysis"
---

## 10.8.5 Localized Mode Vibrational Analysis

(July 4, 2026)

The computation of harmonic frequencies leads to molecular vibrations described
by coordinates which are often highly de-localized. For larger molecules many
vibrational modes can potentially contribute to a single observed spectral
band, and information about the interaction between localized chemical units
can become less readily available. In certain cases, localizing vibrational
modes using procedures similar to the localized orbital schemes discussed
previously in this manual can therefore provide a more chemically intuitive way
of analyzing spectral data,[[620]](../bib_references/bib.md#bib640)
 interpreting
two-dimensional vibrational spectra,[[524]](../bib_references/bib.md#bib537)
 or improving
calculations that go beyond the harmonic
approximation.[[239]](../bib_references/bib.md#bib240)
 It is also possible to
include only a subset of the normal modes in the localization calculation by
invoking the LOCALFREQ_SELECT rem variable. This can be useful to
improve convergence in larger molecules or to explore the coupling between
specific vibrational modes. These modes are defined in the *$alist* block.
Alternatively it is possible to localize high and low frequency
modes separately in a single calculation using LOCALFREQ_GROUPS and
related inputs.

LOCALFREQ

### `LOCALFREQ`

> **Controls whether a vibrational mode localization calculation is performed.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 1
>     * Localized mode calculation with a Pipek-Mezey like criterion.
>     * 2
>     * Localized mode calculation with a Boys like criterion.
> * **Recommendation**: None

LOCALFREQ_THRESH

### `LOCALFREQ_THRESH`

> **Mode localization is considered converged when the change in the localization criterion is less than $10^{\mathrm{-LOCALFREQ\_THRESH}}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n$
>     * User-specified integer.
> * **Recommendation**: None

LOCALFREQ_MAX_ITER

### `LOCALFREQ_MAX_ITER`

> **Controls the maximum number of mode localization sweeps permitted.**
>
> * **Type**: `INTEGER`
> * **Default**: `200`
> * **Options**:
>     * $n$
>     * User-specified integer.
> * **Recommendation**: None

LOCALFREQ_SELECT

### `LOCALFREQ_SELECT`

> **Select a subset of normal modes for subsequent anharmonic frequency analysis.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Select a subset of normal modes.
> * **Recommendation**: None

LOCALFREQ_GROUPS

### `LOCALFREQ_GROUPS`

> **Select the number of groups of frequencies to be localized separately within a localized mode calculation. The size of the groups are then controlled using the LOCALFREQ_GROUP1 , LOCALFREQ_GROUP2 , and LOCALFREQ_GROUP3 keywords.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 1
>     * Define one subset of modes to localize independently.
>     * 2
>     * Define two subsets of modes to localize independently.
>     * 3
>     * Define three subsets of modes to localize independently.
> * **Recommendation**: None

LOCALFREQ_GROUP1

### `LOCALFREQ_GROUP1`

> **Select the number of modes to include in the first subset of modes to localize independently when the keyword LOCALFREQ_GROUPS > 0.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * User-specified integer.
> * **Recommendation**: Modes will be included starting with the lowest frequency mode and then in ascending energy order up to the defined value.

LOCALFREQ_GROUP2 and LOCALFREQ_GROUP3 are defined similarly.
