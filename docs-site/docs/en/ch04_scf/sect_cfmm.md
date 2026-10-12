---
title: "4.6.2 Continuous Fast Multipole Method (CFMM)"
---

## 4.6.2 Continuous Fast Multipole Method (CFMM)

(July 4, 2026)

The quantum chemical Coulomb problem, perhaps better known as the DFT
bottleneck, has been at the forefront of many research efforts throughout the
1990s. The quadratic computational scaling behavior conventionally seen in the
construction of the Coulomb matrix in DFT or HF calculations has prevented the
application of *ab initio* methods to molecules containing many hundreds
of atoms. **Q-Chem** Inc., in collaboration with White and Head-Gordon at the
University of California at Berkeley, and Gill now at the Australian National
University, were the first to develop the generalization of Greengard’s Fast
Multipole Method

 (FMM) to continuous charged matter
distributions in the form of the CFMM, which is the first linear scaling
algorithm for DFT calculations. This initial breakthrough has since lead to an
increasing number of linear scaling alternatives and analogies, but for Coulomb
interactions, the CFMM remains state of the art. There are two computationally
intensive contributions to the Coulomb interactions which we discuss in turn:

- •

Long-range interactions, which are treated by the CFMM
- •

Short-range interactions, corresponding to overlapping charge
distributions, which are treated by a specialized “J-matrix engine”
together with **Q-Chem**’s state-of-the art two-electron integral methods.

The Continuous Fast Multipole Method was the first implemented linear scaling
algorithm for the construction of the $\mathbf{J}$ matrix. In collaboration with
**Q-Chem** Inc., Dr. Chris White began the development of the CFMM by more
efficiently deriving[[1459]](../bib_references/bib.md#bib1519)
 the original Fast Multipole Method
before generalizing it to the CFMM.[[1464]](../bib_references/bib.md#bib1520)
 The generalization applied
by White *et al.* allowed the principles underlying the success of the FMM to be
applied to *arbitrary* (subject to constraints in evaluating the related
integrals) continuous, but localized, matter distributions. White and
coworkers further improved the underlying CFMM
algorithm,[[1460]](../bib_references/bib.md#bib1522)
 then implemented it
efficiently,[[1465]](../bib_references/bib.md#bib1521)
 achieving performance that is an order of
magnitude faster than some competing implementations.

The success of the CFMM follows similarly with that of the FMM, in that the
charge system is subdivided into a hierarchy of boxes. Local charge
distributions are then systematically organized into multipole representations
so that each distribution interacts with local expansions of the potential due
to all distant charge distributions. Local and distant distributions are
distinguished by a well-separated (WS) index, which is the number of boxes that
must separate two collections of charges before they may be considered distant
and can interact through multipole expansions; near-field interactions must be
calculated directly. In the CFMM each distribution is given its own WS index
and is sorted on the basis of the WS index, and the position of their space
centers. The implementation in **Q-Chem** has allowed the efficiency gains of
contracted basis functions to be maintained.

The CFMM algorithm can be summarized in five steps:

1. 1.

Form and translate multipoles.
2. 2.

Convert multipoles to local Taylor expansions.
3. 3.

Translate Taylor information to the lowest level.
4. 4.

Evaluate Taylor expansions to obtain the far-field potential.
5. 5.

Perform direct interactions between overlapping distributions.

Accuracy can be carefully controlled by due consideration of tree depth,
truncation of the multipole expansion and the definition of the extent of
charge distributions in accordance with a rigorous mathematical error bound.
As a rough guide, 10 poles are adequate for single point energy calculations,
while 25 poles yield sufficient accuracy for gradient calculations. Subdivision
of boxes to yield a one-dimensional length of about 8 boxes works quite well
for systems of up to about one hundred atoms. Larger molecular systems, or
ones which are extended along one dimension, will benefit from an increase in
this number. The program automatically selects an appropriate number of boxes
by default.

For the evaluation of the remaining short-range interactions, **Q-Chem**
incorporates efficient J-matrix engines, originated by White and
Head-Gordon.[[1462]](../bib_references/bib.md#bib1524)
 These are analytically exact methods that are
based on standard two-electron integral methods, but with an interesting twist.
If one knows that the two-electron integrals are going to be summed into a
Coulomb matrix, one can ask whether they are in fact the most efficient
intermediates for this specific task. Or, can one instead find a more compact
and computationally efficient set of intermediates by folding the density
matrix into the recurrence relations for the two-electron integrals. For
integrals that are not highly contracted (*i.e.*, are not linear combinations of
more than a few Gaussians), the answer is a dramatic yes. This is the basis of
the J-matrix approach, and **Q-Chem** includes the latest algorithm developed by
Yihan Shao working with Martin Head-Gordon at Berkeley for this purpose.
Shao’s J-engine is employed for both energies[[1240]](../bib_references/bib.md#bib1292)
 and
forces,[[1241]](../bib_references/bib.md#bib1293)
 and gives substantial speedups relative to the use of
two-electron integrals without any approximation—roughly a factor of 10 for
energies and 30 for forces at the level of an uncontracted $dddd$ shell
quartet, and increasing with angular momentum). Its use is automatically
selected for integrals with low degrees of contraction, while regular integrals
are employed when the degree of contraction is high, following the state of the
art PRISM approach of Gill and coworkers.[[22]](../bib_references/bib.md#bib6)

The CFMM is controlled by the following input parameters:

### `CFMM_ORDER`

> **Controls the order of the multipole expansions in CFMM calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `15`
> * **Options**:
>     * $n$: Use multipole expansions of order
>     * $n$
> * **Recommendation**: Use the default.

### `GRAIN`

> **Controls the number of lowest-level boxes in one dimension for CFMM.**
>
> * **Type**: `INTEGER`
> * **Default**: `-1`
> * **Options**:
>     * `-1`: Program decides best value, turning on CFMM when useful
>     * `1`: Do not use CFMM $n\geq 8$ Use CFMM with
>     * $n$: lowest-level boxes in one dimension
> * **Recommendation**: This is an expert option; either use the default, or use a value of 1 if CFMM is not desired.
