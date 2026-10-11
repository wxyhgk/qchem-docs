---
title: "5.5.1 Introduction"
---

## 5.5.1 Introduction

(July 4, 2026)

In practical DFT calculations, the forms of the approximate
exchange-correlation functionals used are quite complicated, such that the
required integrals involving the functionals generally cannot be evaluated
analytically. **Q-Chem** evaluates these integrals through numerical quadrature
directly applied to the exchange-correlation integrand. Several standard
quadrature grids are available (“SG-$n$”, $n=0,1,2,3$), with a default
value that is automatically set according to the complexity of the functional in question.

The quadrature approach in **Q-Chem** is generally similar to that found in many
DFT programs. The multi-center XC integrals are first partitioned into
“atomic” contributions using a nuclear weight function. **Q-Chem** uses the
nuclear partitioning of Becke,[[94]](../bib_references/bib.md#bib73)
 though without the “atomic
size adjustments” of Ref. [[94]](../bib_references/bib.md#bib73)
. The atomic integrals are
then evaluated through standard one-center numerical techniques. Thus, the
exchange-correlation energy is obtained as

<a id="eq439"></a>
$$
E_{\mathrm{XC}}=\sum_{A}^{\rm atoms}\sum_{i\in A}^{\rm points}w_{Ai}f(\mathbf{r}_{Ai})\;, \tag{5.15}
$$

where the function $f$ is the aforementioned XC integrand and the quantities
$w_{Ai}$ are the quadrature weights. The sum over $i$ runs over grid points
belonging to atom $A$, which are located at positions $\mathbf{r}_{Ai}=\mathbf{R}_{A}+\mathbf{r}_{i}$, so this approach requires only the choice
of a suitable one-center integration grid (to define the $\mathbf{r}_{i}$),
which is independent of nuclear configuration. These grids are implemented in
**Q-Chem** in a way that ensures that the $E_{\rm XC}$ is rotationally-invariant,
*i.e.*, that is does not change when the molecule undergoes rigid rotation in
space.[[648]](../bib_references/bib.md#bib672)

Quadrature grids are further separated into radial and angular parts. Within
**Q-Chem**, the radial part is usually treated by the Euler-Maclaurin scheme
proposed by Murray *et al.*,[[967]](../bib_references/bib.md#bib1009)
 which maps the semi-infinite
domain $[0,\infty)$ onto $[0,1)$ and applies the extended trapezoid rule to the
transformed integrand. Alternatively, Gill and Chien proposed a radial scheme
based on a Gaussian quadrature on the interval $[0,1]$ with a different weight
function.[[240]](../bib_references/bib.md#bib241)
 This “MultiExp" radial quadrature is exact for
integrands that are a linear combination of a geometric sequence of exponential
functions, and is therefore well suited to evaluating atomic integrals.
However, the task of generating the MultiExp quadrature points becomes
increasingly ill-conditioned as the number of radial points increases, so that
a “double exponential" radial quadrature[[953]](../bib_references/bib.md#bib993)
 is used
for the largest standard grids in **Q-Chem**,[[953]](../bib_references/bib.md#bib993)

namely SG-2 and SG-3.[[301]](../bib_references/bib.md#bib305)
 (See
Section [5.5.3](sect_standard-quad.md).)
