---
title: "4.6.6 Resolution of the Identity Fock Matrix Methods"
---

## 4.6.6 Resolution of the Identity Fock Matrix Methods

(July 4, 2026)

Evaluation of the Fock matrix (both Coulomb, J, and exchange, K, pieces) can be
sped up by an approximation known as the resolution-of-the-identity (RI-JK).
Essentially, the full complexity in common basis sets required to describe
chemical bonding is not necessary to describe the mean-field Coulomb and
exchange interactions between electrons. That is, $\rho$ in the left side of

<a id="A3.S8.EGx4"></a>

$$
\displaystyle(\mu\nu|\rho)=\sum_{\lambda\sigma}(\mu\nu|\lambda\sigma)\mathbf{P}_{\lambda\sigma} \tag{4.51}
$$

is much less complicated than an individual $\lambda\sigma$ function pair. The
same principle applies to the FTC method in subsection [4.6.5](sect_FTC.md), in which
case the slowly varying piece of the electron density is replaced with a
plane-wave expansion.

With the RI-JK approximation, the Coulomb interactions of the function pair
$\rho(r)=\lambda\sigma(r)P_{\lambda\sigma}$ are fit by a smaller set of
atom-centered basis functions. In terms of $J$:

<a id="A3.S8.EGx5"></a>

$$
\displaystyle\sum_{\lambda\sigma}\int\textrm{d}^{3}\mathbf{r}_{1}P_{\lambda\sigma}\lambda\sigma(\mathbf{r}_{1})\frac{1}{|\mathbf{r}_{1}-\mathbf{r}|}\approx\sum_{K}\int\textrm{d}^{3}\mathbf{r}_{1}P_{K}K(\mathbf{r}_{1})\frac{1}{|\mathbf{r}_{1}-\mathbf{r}|} \tag{4.52}
$$

The coefficients $P_{K}$ must be determined to accurately represent the
potential. This is done by performing a least-squared minimization of the
difference between $P_{\lambda\sigma}\lambda\sigma(\mathbf{r}_{1})$ and $P_{K}K(\mathbf{r}_{1})$, *with differences measured by the Coulomb metric*. This
requires a matrix inversion over the space of auxiliary basis functions, which
may be done rapidly by Cholesky decomposition.

The RI-J can be invoked by either setting RI_J to be true, or (since **Q-Chem** 5.2) specifying
auxiliary basis set for J using AUX_BASIS_J.

The RI method applied to the Fock matrix may be further enhanced by performing
*local* fitting of a density or function pair element. This is the
basis of the atomic-RI method (ARI), which has been developed for both Coulomb
(J) matrix[[1280]](../bib_references/bib.md#bib1333)
 and exchange (K) matrix evaluation.[[1281]](../bib_references/bib.md#bib1334)

In ARI, only nearby auxiliary functions $K(\mathbf{r})$ are employed to fit the
target function. This reduces the asymptotic scaling of the matrix-inversion
step as well as that of many intermediate steps in the digestion of RI
integrals. Briefly, atom-centered auxiliary functions on nearby atoms are only
used if they are within the “outer” radius ($R_{1}$) of the fitting region.
Between $R_{1}$ and the “inner” radius ($R_{0}$), the amplitude of interacting
auxiliary functions is smoothed by a function that goes from zero to one and
has continuous derivatives. To optimize efficiency, the van der Waals radius
of the atom is included in the cutoff so that smaller atoms are dropped from
the fitting radius sooner. The values of $R_{0}$ and $R_{1}$ are specified as REM
variables as described below.

RI_J

### `RI_J`

> **Toggles the use of the RI algorithm to compute J.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Turn on RI for J.
> * **Recommendation**: For large (especially 1D and 2D) molecules the approximation may yield significant improvements in Fock evaluation time when used with ARI .

RI_K

### `RI_K`

> **Toggles the use of the RI algorithm to compute K.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Turn on RI for K.
> * **Recommendation**: For large (especially 1D and 2D) molecules the approximation may yield significant improvements in Fock evaluation time when used with ARI .

ARI

### `ARI`

> **Toggles the use of the atomic resolution-of-the-identity (ARI) approximation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Turn on ARI.
> * **Recommendation**: For large (especially 1D and 2D) molecules the approximation may yield significant improvements in Fock evaluation time.

ARI_R0

### `ARI_R0`

> **Determines the value of the inner fitting radius (in Ångstroms)**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $n$
>     * User defined radius.
> * **Recommendation**: For some systems the default value may be too small and the calculation will become unstable.

ARI_R1

### `ARI_R1`

> **Determines the value of the outer fitting radius (in Ångstroms)**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$
>     * User defined radius.
> * **Recommendation**: For some systems the default value may be too small and the calculation will become unstable. This value also determines, in part, the smoothness of the potential energy surface.
