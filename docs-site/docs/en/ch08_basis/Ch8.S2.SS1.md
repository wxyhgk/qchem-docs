---
title: "8.2.1 Overview"
---

## 8.2.1 Overview

(July 4, 2026)

**Q-Chem** is equipped with many standard basis sets,[[11]](../bib_references/bib.md#bib14) and allows
the user to specify the required basis set by its standard symbolic
representation. The available built-in basis sets include the following types:

- Pople basis sets[[131]](../bib_references/bib.md#bib121)
- Dunning basis sets[[354]](../bib_references/bib.md#bib359)
- Correlation-consistent (cc) Dunning basis sets, including:

- Standard cc-pVXZ and aug-cc-pVXZ (X = D, T, Q, 5, and 6)[[355]](../bib_references/bib.md#bib360)
- Partially-augmented “calendar” versions,[[1039]](../bib_references/bib.md#bib1083)

may-, jun-, and jul-cc-pVXZ (X = D, T, Q)
- Versions with core–valence polarization functions,[[1122]](../bib_references/bib.md#bib1169)

cc-pCVXZ and cc-pwCVXZ (X = D, T, Q)
- Partially-augmented core–valence polarization basis sets jun-, jul-, and aug-cc-pCVXZ (X = D, T, Q)
- Pseudopotential (PP) basis sets for heavy elements, cc-pVXZ-PP and aug-cc-pVXZ-PP (X = D, T, Q)[[1080]](../bib_references/bib.md#bib1125)
- Ahlrichs basis sets[[1202]](../bib_references/bib.md#bib1256)
- Karlsruhe “def2” basis sets,[[1438]](../bib_references/bib.md#bib1504)
 including

- Augmented versions,[[1147]](../bib_references/bib.md#bib1199)
 such as def2-SVPD
- Partially-augmented versions,[[481]](../bib_references/bib.md#bib492)
 such as def2-ha-SVP and def2-ha-SVP
- Jensen polarization consistent basis sets[[635]](../bib_references/bib.md#bib661)
- Universal Gaussian basis set (UGBS)[[310]](../bib_references/bib.md#bib315)

In addition, **Q-Chem** supports the following features:

- Extra diffuse functions available for high quality excited-state calculations.
- Standard polarization functions.
- $s$, $p$, $sp$, $d$, $f$, $g$ and $h$ angular momentum types of basis functions (for energy calculations, up to $k$ are supported).
- Pure and Cartesian basis functions.
- Mixed basis sets (see Section [8.5](sect_mixedbas.md)).
- Basis set superposition error (BSSE) corrections.
- Automatic, on-the-fly
generation of a superposition of atomic densities (SAD) guess for any basis set (including general and mixed basis sets)
and any SCF level of theory (see Section [4.4.2](../ch04_scf/sect_guess.md)).

The following *$rem* keyword controls the basis set:

### `BASIS`

> **Sets the basis set to be used.**
>
> * **Type**: `STRING`
> * **Default**: `No default basis set`
> * **Options**:
>     * `General, Gen`: User-defined. See section below
>     * `Symbol`: Use standard basis sets as in the table below
>     * `Mixed`: Use a combination of different basis sets
> * **Recommendation**: Consult literature and reviews to aid your selection.
