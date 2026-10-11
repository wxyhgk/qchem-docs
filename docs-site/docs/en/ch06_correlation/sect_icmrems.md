---
title: "6.21.3 Job Control for iFCI"
---

## 6.21.3 Job Control for iFCI

(July 4, 2026)

IFCI_TUPLES

### `IFCI_TUPLES`

> **Level of $n$ -body expansion to solve. Note that $n>2$ can be computationally costly.**
>
> * **Type**: `INTEGER`
> * **Default**: `Must be set.`
> * **Options**:
>     * 1
>     * $n=1$
>     * 2
>     * $n=2$
>     * 3
>     * $n=3$
>     * 4
>     * $n=4$
> * **Recommendation**: Use $n=2$ for initial system analysis, $n>2$ for higher accuracy.

IFCI_READ

### `IFCI_READ`

> **Restarts iFCI with existing TUPLES_1E_DATA file , if it exists.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Start from scratch
>     * 1
>     * Restart from previous file
> * **Recommendation**: Use 0 if no previous run files exist. Use 1 if intending to restart from previous data.

IFCI_TRIPLETS

### `IFCI_TRIPLETS`

> **Set state to solve.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Singlet
>     * 1
>     * Triplet
>     * 2
>     * Quintet
> * **Recommendation**: None

IFCI_ZETA

### `IFCI_ZETA`

> **Convergence for each iFCI increment. Note that the format is $\zeta=$ $/10$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `55`
> * **Options**:
>     * 45
>     * Loose
>     * 55
>     * Moderate
>     * 65
>     * Tight
>     * 75
>     * Tighter
>     * 85
>     * Quite tight
>     * 95
>     * Maximum
> * **Recommendation**: Use 65 and increase to 75 to check convergence.

HBCI_EPS1

### `HBCI_EPS1`

> **Determines dimension of HBCI space.**
>
> * **Type**: `INTEGER`
> * **Default**: `1000`
> * **Options**:
>     * $N$
>     * HBCI
>     * $\varepsilon_{1}$
>     * in
>     * $\mu$
>     * E
>     * ${}_{\mathrm{h}}$
> * **Recommendation**: Use default or 500 for tighter convergence.

IFCI_TUPLE_THRESH

### `IFCI_TUPLE_THRESH`

> **Collapse near-degenerate geminals within threshold into one body.**
>
> * **Type**: `INTEGER`
> * **Default**: `2500`
> * **Options**:
>     * $n$
>     * in
>     * $\mu$
>     * E
>     * ${}_{\mathrm{h}}$
> * **Recommendation**: Use default unless there are sets of highly correlating occupied orbitals.

IFCI_TRIPLES_SCREEN

### `IFCI_TRIPLES_SCREEN`

> **Cutoff ( $\mathcal{C}_{3}$ ) for determining if a 3-body term is significant.**
>
> * **Type**: `INTEGER`
> * **Default**: `1000`
> * **Options**:
>     * $n$
>     * where
>     * $\mathcal{C}_{3}=10^{-\zeta}\times n$
>     * in E
>     * ${}_{\mathrm{h}}$
> * **Recommendation**: Use the default unless looser (higher $n$ ) or tighter (lower $n$ ) consideration of triads for a given system is desired. Setting to 0 computes all triads (costly).

IFCI_QUAD_SCREEN

### `IFCI_QUAD_SCREEN`

> **Cutoff ( $\mathcal{C}_{4}$ ) for determining if a 4-body term is significant.**
>
> * **Type**: `INTEGER`
> * **Default**: `IFCI_TRIPLES_SCREEN`
> * **Options**:
>     * $n$
>     * where
>     * $\mathcal{C}_{4}=10^{-\zeta}\times n$
>     * in E
>     * ${}_{\mathrm{h}}$
> * **Recommendation**: Same as IFCI_TRIPLES_SCREEN but note that $4$ -body terms are significantly more costly.

IFCI_STATE_ADD

### `IFCI_STATE_ADD`

> **Adds additional states to HBCI solver when there is degeneracy amongst states.**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $n$
>     * Add states within
>     * $n$
>     * mE
>     * ${}_{\mathrm{h}}$
> * **Recommendation**: Use default unless it is known that degenerate states are present.

IFCI_PRINT

### `IFCI_PRINT`

> **Larger number gives more output.**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * 1
>     * Minimal output
>     * 2
>     * Readable output
>     * 3
>     * Extra output
>     * 4
>     * Excessive output
>     * 5+
>     * Bug testing output
> * **Recommendation**: 2 is recommended, 1-3 is appropriate, larger than 4 is unnecessary (consider yourself warned).

IFCI_NO_THRESH

### `IFCI_NO_THRESH`

> **Equivalent to HBCI $\varepsilon_{1}$ for increment-specific NO generation step.**
>
> * **Type**: `INTEGER`
> * **Default**: `1000`
> * **Options**:
>     * $n$
>     * in
>     * $\mu$
>     * E
>     * ${}_{\mathrm{h}}$
> * **Recommendation**: Set to equal HBCI_EPS1 .

IFCI_REF_ITER

### `IFCI_REF_ITER`

> **Use HF or PP reference density.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 0
>     * HF
>     * 1
>     * PP
> * **Recommendation**: Use 0.

IFCI_OCC

### `IFCI_OCC`

> **Specifies the number of active occupied orbitals.**
>
> * **Type**: `INTEGER`
> * **Default**: `Full valence.`
> * **Options**:
>     * $n$
>     * Include
>     * $n$
>     * orbitals in the active space
>     * $-1$
>     * Full valence
> * **Recommendation**: Use full valence active space.
