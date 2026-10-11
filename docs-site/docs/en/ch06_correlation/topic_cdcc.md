---
title: "6.12.11 Cholesky Decomposition with CC (CD-CC)"
---

## 6.12.11 Cholesky Decomposition with CC (CD-CC)

(July 4, 2026)

Two-electron integrals can be decomposed using Cholesky
decomposition[[366]](../bib_references/bib.md#bib762)
 giving rise to the same representation as in
RI and substantially reducing the cost of integral transformation, disk storage
requirements, and improving parallel performance:

<a id="Ch6.E79"></a>

$$
(\mu\nu|\lambda\sigma)\approx\sum_{P=1}^{M}B_{\mu\nu}^{P}B_{\lambda\sigma}^{P}, \tag{6.79}
$$

The rank of Cholesky decomposition, $M$, is typically 3-10 times larger than
the number of basis functions $N$ (Ref. [[49]](../bib_references/bib.md#bib32)
); it
depends on the decomposition threshold $\delta$ and is considerably smaller
than the full rank of the matrix,
$N(N+1)/2$ (Refs. [[49]](../bib_references/bib.md#bib32)
).
Cholesky decomposition removes linear dependencies in product
densities $(\mu\nu|$,[[49]](../bib_references/bib.md#bib32)
 allowing one to obtain compact
approximation to the original matrix with accuracy, in principle, up to machine
precision.

Decomposition threshold $\delta$ is the only parameter that controls accuracy
and the rank of the decomposition. Cholesky decomposition is invoked by
specifying CHOLESKY_TOL that defines the accuracy with which
decomposition should be performed. For most calculations tolerance of $\delta=10^{-3}$ gives a good balance between accuracy and compactness of the rank.
Tolerance of $\delta=10^{-2}$ can be used for exploratory calculations and
$\delta=10^{-4}$ for high-accuracy calculations. Similar to RI,
Cholesky-decomposed integrals can be transformed back, into the canonical MO
form, using CC_DIRECT_RI keyword.

The default execution uses the new two-step algorithm for the
decomposition.[[1215]](../bib_references/bib.md#bib1265)

The old algorithm[[366]](../bib_references/bib.md#bib762)
 can be
invoked by specifying CHOLESKY_TWOSTEP = FALSE.
The two-step algorithm uses additional parameter,
CD_TS_SPAN_FACTOR, which is defaulted to 2. A larger value may
be used to increase accuracy, as illustrated by Example [6.12.13](ex_CDCCSD.md).

**Note: 

Cholesky decomposition is available for all CCMAN2 methods, including
energy, analytic gradients, and properties calculations.
For maximum computational efficiency, combine with FNO (see Sections
[6.15.1](sec_FNOCC.md) and [7.9.14](../ch07_excited/sec_FNO.md)) when appropriate.
**

Examples [6.12.13](ex_CDCCSD.md), [6.12.13](ex_CDCCSD.md), and [6.12.13](ex_CDCCSD.md) illustrate the usage of this feature.
