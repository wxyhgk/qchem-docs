---
title: "4.5.3 Direct Inversion in the Iterative Subspace (DIIS)"
---

## 4.5.3 Direct Inversion in the Iterative Subspace (DIIS)

(July 4, 2026)

diis

The SCF implementation of the Direct Inversion in the Iterative Subspace (DIIS)
method[[1136]](../bib_references/bib.md#bib1182)
 uses the property of an SCF solution that
requires the density matrix to commute with the Fock matrix:

<a id="eq:DIIS-error"></a>

$$
\mathbf{SPF}-\mathbf{FPS}=\bm{0}\;. \tag{4.30}
$$

During the SCF cycles, prior to achieving self-consistency, it is therefore
possible to define an error vector **e${}_{i}$**, which is non-zero except
at convergence:

<a id="eq446"></a>

$$
{\rm{\bf SP}}_{i}{\rm{\bf F}}_{i}-{\rm{\bf F}}_{i}{\rm{\bf P}}_{i}{\rm{\bf S}}={\rm{\bf e}}_{i} \tag{4.31}
$$

Here $\mathbf{P}_{i}$ is obtained by diagonalizing $\mathbf{F}_{i}$, and

<a id="eq447"></a>

$$
\mathbf{F}_{k}=\sum\limits_{j=1}^{k-1}{c_{j}{\rm{\bf F}}_{j}} \tag{4.32}
$$

The DIIS coefficients $c_{k}$, are obtained by a least-squares constrained
minimization of the error vectors, *viz*

<a id="eq448"></a>

$$
Z=\left({\sum\limits_{k}{c_{k}{\rm{\bf e}}_{k}}}\right)\cdot\left({\sum\limits_{k}{c_{k}{\rm{\bf e}}_{k}}}\right) \tag{4.33}
$$

where the constraint $\sum_{k}c_{k}=1$
is imposed to yield a set of linear equations, of dimension $N+1$:

<a id="eq450"></a>

$$
\left({{\begin{array}[]{*{4}c}{{\rm{\bf e}}_{1}\cdot{\rm{\bf e}}_{1}}&\cdots&{{\rm{\bf e}}_{1}\cdot{\rm{\bf e}}_{N}}&1\\
\vdots&\ddots&\vdots&\vdots\\
{{\rm{\bf e}}_{N}\cdot{\rm{\bf e}}_{1}}&\cdots&{{\rm{\bf e}}_{N}\cdot{\rm{\bf e}}_{N}}&1\\
1&\cdots&1&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{c_{1}}\\
\vdots\\
{c_{N}}\\
\lambda\\
\end{array}}}\right)=\left({{\begin{array}[]{*{1}c}0\\
\vdots\\
0\\
1\\
\end{array}}}\right)\;. \tag{4.34}
$$

Convergence criteria require the largest element of the $N$th error vector to
be below a cutoff threshold, usually $10^{-5}$  a.u. for single point
energies, but often increased to $10^{-8}$ a.u.  for optimizations and
frequency calculations.

The rate of convergence may be improved by restricting the number of previous
Fock matrices used for determining the DIIS coefficients,

<a id="eq451"></a>

$$
\mathbf{F}_{k}=\sum_{j=k-(L+1)}^{k-1}c_{j}\,\mathbf{F}_{j}\;. \tag{4.35}
$$

Here $L$ is the size of the DIIS subspace, which is set using the *$rem* variable
DIIS_SUBSPACE_SIZE. As the Fock matrix nears
self-consistency, the linear matrix equations in Eq. ([4.34](#eq450)) tend to become
severely ill-conditioned and it is often necessary to reset the DIIS subspace
(this is automatically carried out by the program).

Finally, on a practical note, we observe that DIIS has a tendency to converge
to global minima rather than local minima when employed for SCF calculations.
This seems to be because only at convergence is the density matrix in the DIIS
iterations idempotent. On the way to convergence, one is not on the true energy
surface, and this seems to permit DIIS to “tunnel” through barriers in wave
function space. This is usually a desirable property, and is the motivation for
the options that permit initial DIIS iterations before switching to direct
minimization to converge to the minimum in difficult cases.

The following *$rem* variables permit some customization of the DIIS
iterations:

DIIS_SUBSPACE_SIZE

### `DIIS_SUBSPACE_SIZE`

> **Controls the size of the DIIS and/or RCA subspace during the SCF.**
>
> * **Type**: `INTEGER`
> * **Default**: `15`
> * **Options**:
>     * User-defined
> * **Recommendation**: None

DIIS_PRINT

### `DIIS_PRINT`

> **Controls the output from DIIS SCF optimization.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Minimal print out.
>     * 1
>     * Chosen method and DIIS coefficients and solutions.
>     * 2
>     * Level 1 plus changes in multipole moments.
>     * 3
>     * Level 2 plus Multipole moments.
>     * 4
>     * Level 3 plus extrapolated Fock matrices.
> * **Recommendation**: Use the default

DIIS_ERR_RMS

### `DIIS_ERR_RMS`

> **Determines the metric used to gauge the magnitude of the error vector $\mathbf{SPF}-\mathbf{FPS}$ [Eq. ( 4.30 )].**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * TRUE
>     * Use the RMS value of the error vector to measure convergence.
>     * FALSE
>     * Use the maximum value of
>     * $\mathbf{SPF}-\mathbf{FPS}$
>     * instead.
> * **Recommendation**: Use the default.

DIIS_SEPARATE_ERRVEC

### `DIIS_SEPARATE_ERRVEC`

> **Control optimization of DIIS error vector in unrestricted calculations.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Use a combined
>     * $\alpha$
>     * and
>     * $\beta$
>     * error vector.
>     * TRUE
>     * Use separate error vectors for the
>     * $\alpha$
>     * and
>     * $\beta$
>     * spaces.
> * **Recommendation**: When using DIIS in Q-Chem a convenient optimization for unrestricted calculations is to sum the $\alpha$ and $\beta$ error vectors into a single vector which is used for extrapolation. This is often extremely effective, but in some pathological systems with symmetry breaking, can lead to false solutions being detected, where the $\alpha$ and $\beta$ components of the error vector cancel exactly giving a zero DIIS error. While an extremely uncommon occurrence, if it is suspected, set = TRUE to check.
