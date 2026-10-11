---
title: "4.6.8 occ-RI-K Exchange Algorithm"
---

## 4.6.8 occ-RI-K Exchange Algorithm

(July 4, 2026)

The occupied orbital RI-K (occ-RI-K) algorithm[[892]](../bib_references/bib.md#bib926)
 is a new scheme for
building the exchange matrix (K) partially in the MO basis using the RI
approximation. occ-RI-K typically matches current alternatives in terms of both
the accuracy (energetics identical to standard RI-K) and convergence
(essentially unchanged relative to conventional methods). On the other hand,
this algorithm exhibits significant speedups over conventional integral
evaluation (14x) and standard RI-K (3.3x) for a test system, a graphene
fragment (C${}_{68}$H${}_{22}$) using cc-pVQZ basis set (4400 basis functions),
whereas the speedup increases with the size of the AO basis set. Thus occ-RI-K
helps to make larger basis set hybrid DFT calculations more feasible, which is
quite desirable for achieving improved accuracy in DFT calculations with modern
functionals.

The idea of the occ-RI-K formalism comes from a simple observation that
the exchange energy $E_{K}$ and its gradient can be evaluated from the diagonal
elements of the exchange matrix in the occupied-occupied block $K_{ii}$, and
occupied-virtual block $K_{ia}$, respectively, rather than the full matrix
in the AO representation, $K_{\mu\nu}$. Mathematically,

<a id="A3.S8.EGx6"></a>

$$
\displaystyle E_{K} \tag{4.53}
$$

and

<a id="eq4occ-RI-K2"></a>

$$
\frac{\partial E_{K}}{\partial\Delta_{ai}}=2K_{ai} \tag{4.54}
$$

where $\Delta$ is a skew-symmetric matrix used to parameterize the unitary
transformation $U$, which represents the variations of the MO coefficients
as follows:

<a id="eq4occ-RI-K3"></a>

$$
U=e^{(\Delta-\Delta^{T})}. \tag{4.55}
$$

From Eq. [4.53](#eq4occ-RI-K1) and [4.54](#eq4occ-RI-K2) it is evident that the exchange
energy and gradient need just $K_{i\nu}$ rather than $K_{\mu\nu}$.

In regular RI-K one has to compute two quartic terms,[[1442]](../bib_references/bib.md#bib1502)

whereas there are three quartic terms for the occ-RI-K algorithm. The speedup of the
latter with respect to former can be explained from the following ratio of
operations; refer to Ref. [[892]](../bib_references/bib.md#bib926)
 for details.

<a id="A3.S8.EGx7"></a>

$$
\displaystyle\frac{\mbox{\#~{}of~{}RI-K~{}quartic~{}operations}}{\mbox{\#~{}of~{}occ-RI-K~{}quartic~{}operations}}=\frac{oNX^{2}+oN^{2}X}{o^{2}X^{2}+o^{2}NX+o^{2}NX}=\frac{N(X+N)}{o(X+2N)} \tag{4.56}
$$

With a conservative approximation of $X\approx 2N$, the speedup is
$\frac{3}{4}(N/o)$. The occ-RI-K algorithm also involves some cubic steps which
should be negligible in the very large molecule limit. Tests in the
Ref. [[892]](../bib_references/bib.md#bib926)
 suggest that occ-RI-K for small systems with
large basis will gain less speed than a large system with small basis, because
the cubic terms will be more dominant for the former than the latter case.

In the course of SCF iteration, the occ-RI-K method does not require us to
construct the exact Fock matrix explicitly. Rather, $k_{i\nu}$ contributes to
the Fock matrix in the mixed MO and AO representations ($F_{i\nu}$) and yields
orbital gradient and DIIS error vectors for converging SCF. On the other hand,
since occ-RI-K does not provide exactly the same unoccupied eigenvalues, the
diagonalization updates can differ from the conventional SCF procedure. In
Ref. [[892]](../bib_references/bib.md#bib926)
, occ-RI-K was found to require, on average, the
same number of SCF iterations to converge and to yield accurate energies.

The occ-RI-K can be invoked by either setting OCC_RI_K to be true, or (since **Q-Chem** 5.2) specifying
auxiliary basis set for K using AUX_BASIS_K.

OCC_RI_K

### `OCC_RI_K`

> **Controls the use of the occ-RI-K approximation for constructing the exchange matrix**
>
> * **Type**: `LOGICAL`
> * **Default**: `False`
> * **Options**:
>     * True
>     * Use occ-RI-K.
> * **Recommendation**: Larger the system, better the performance

## 4.6.8.1 occ-RI-K for exchange energy gradient evaluation

A very attractive feature of occ-RI-K framework is that one can compute the
exchange energy gradient with respect to nuclear coordinates with the same
leading quartic-scaling operations as the energy calculation.

The occ-RI-K formulation yields the following formula for the gradient
of exchange energy in global Coulomb-metric RI:

<a id="A3.S8.EGx8"></a>

$$
\displaystyle E_{K}^{x} \tag{4.57}
$$

The superscript $x$ represents the derivative with respect to a
nuclear coordinate. Note that the derivatives of the MO coefficients
$c_{\mu i}$ are not included here, because they are already
included in the total energy derivative calculation by **Q-Chem**
via the derivative of the overlap matrix.

In Eq. [4.57](#eq4occ-RI-K-grad), the construction of the density fitting
coefficients ($C_{\mu\nu}^{P}$) has the worst scaling of $\mathcal{O}(M^{4})$
because it involves MO to AO back transformations:

<a id="A3.S8.EGx9"></a>

$$
\displaystyle C_{\mu\nu}^{P}=\sum_{ij}c_{\mu i}c_{\nu j}C_{ij}^{P} \tag{4.58}
$$

where the operation cost is $o^{2}NX+o[\mathrm{NB2}]X$.

RI_K_GRAD

### `RI_K_GRAD`

> **Turn on the nuclear gradient calculations**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Use occ-RI-K based gradient
> * **Recommendation**: Use "RI_J false"

???+ example "Example 4.21: Q-Chem input for a energy and gradient calculations with occ-RI-K method."
    ```qchem
    $molecule
       0   1
       C    0.0000000    0.3057430    5.7138876
       C    0.0000000   -0.5442831    4.4256275
       C    0.0000000    0.3675825    3.1787857
       C    0.0000000   -0.4853210    1.8908707
       C    0.0000000    0.4264823    0.6439435
       C    0.0000000   -0.4264823   -0.6439435
       C    0.0000000    0.4853210   -1.8908707
       C    0.0000000   -0.3675825   -3.1787857
       C    0.0000000    0.5442831   -4.4256275
       C    0.0000000   -0.3057430   -5.7138876
       H    0.8973039    0.9418895    5.7433715
       H   -0.8973039    0.9418895    5.7433715
       H   -0.8965960   -1.1827891    4.4155828
       H    0.8965960   -1.1827891    4.4155828
       H    0.8966512    1.0057416    3.1940146
       H   -0.8966512    1.0057416    3.1940146
       H   -0.8966512   -1.1234851    1.8761493
       H    0.8966512   -1.1234851    1.8761493
       H    0.8966507    1.0646443    0.6587590
       H   -0.8966507    1.0646443    0.6587590
       H   -0.8966507   -1.0646443   -0.6587590
       H    0.8966507   -1.0646443   -0.6587590
       H    0.8966512    1.1234851   -1.8761493
       H   -0.8966512    1.1234851   -1.8761493
       H   -0.8966512   -1.0057416   -3.1940146
       H    0.8966512   -1.0057416   -3.1940146
       H    0.8965960    1.1827891   -4.4155828
       H   -0.8965960    1.1827891   -4.4155828
       H    0.8973039   -0.9418895   -5.7433715
       H    0.0000000    0.3580832   -6.5913113
       H   -0.8973039   -0.9418895   -5.7433715
       H    0.0000000   -0.3580832    6.5913113
    $end
    
    $rem
       JOBTYPE         force
       EXCHANGE        HF
       BASIS           cc-pVTZ
       AUX_BASIS       cc-pVTZ-JK
       OCC_RI_K        1
       RI_K_GRAD       1
       INCFOCK         0
       PURECART        1111
    $end
    ```
