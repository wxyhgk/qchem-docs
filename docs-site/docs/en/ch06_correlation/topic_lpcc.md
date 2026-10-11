---
title: "6.14.5 Local Pair Models for Valence Correlations Beyond Doubles"
---

## 6.14.5 Local Pair Models for Valence Correlations Beyond Doubles

(July 4, 2026)

Working with Prof. Head-Gordon at Berkeley, John Parkhill has developed
implementations for pair models which couple 4 and 6 electrons together
quantitatively. Because these truncate the coupled cluster equations at
quadruples and hextuples respectively they have been termed the “Perfect
Quadruples” and “Perfect Hextuples” models. These can be viewed as local
approximations to CASSCF. The PQ and PH models are executed through an
extension of **Q-Chem**’s coupled cluster code, and several options defined for
those models will have the same effects although the mechanism may be different
(CC_DIIS_START, CC_DIIS_SIZE, CC_DOV_THRESH, CC_CONV, *etc.*).

In the course of implementation, the non-local coupled cluster models were also
implemented up to ${\hat{T}}_{6}$. Because the algorithms are explicitly sparse
their costs relative to the existing implementations of CCSD are much higher
(and should never be used in lieu of an existing CCMAN code), but this
capability may be useful for development purposes, and when computable, models
above CCSDTQ are highly accurate. To use PQ, PH, their dynamically correlated
“+SD” versions or this machine generated cluster code set: METHOD =
MGC.

MGC_AMODEL

### `MGC_AMODEL`

> **Choice of approximate cluster model.**
>
> * **Type**: `INTEGER`
> * **Default**: `Determines`
> * **Options**:
>     * 0
>     * Local Active-Space Amplitude iterations (pre-calculate GVB orbitals with
>     * your method of choice (RPP is good)).
>     * 7
>     * Optimize-Orbitals using the VOD 2-step solver.
>     * (Experimental-only use with MGC_AMPS = 2, 24 ,246)
>     * 8
>     * Traditional Coupled Cluster up to CCSDTQPH.
>     * 9
>     * MR-CC version of the Pair-Models. (Experimental)
> * **Recommendation**: None

MGC_NLPAIRS

### `MGC_NLPAIRS`

> **Number of local pairs on an amplitude.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * Must be greater than 1, which corresponds to the PP model.
>     * 2 for PQ, and 3 for PH.
> * **Recommendation**: None

MGC_AMPS

### `MGC_AMPS`

> **Choice of Amplitude Truncation**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * 2
>     * $\leq$
>     * n
>     * $\leq$
>     * 123456, a sorted list of integers for every amplitude
>     * which will be iterated. Choose 1234 for PQ and 123456 for PH
> * **Recommendation**: None

MGC_LOCALINTS

### `MGC_LOCALINTS`

> **Pair filter on an integrals.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * Enforces a pair filter on the 2-electron integrals, significantly
>     * reducing computational cost. Generally useful for more than 1 pair locality.
> * **Recommendation**: None

MGC_LOCALINTER

### `MGC_LOCALINTER`

> **Pair filter on an intermediate.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * Any nonzero value enforces the pair constraint on intermediates,
>     * significantly reducing computational cost. Not recommended for
>     * $\leq$
>     * 2 pair locality
> * **Recommendation**: None
