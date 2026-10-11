---
title: "5.10.2 LB94 Scheme"
---

## 5.10.2 LB94 Scheme

(July 4, 2026)

An asymptotically corrected (AC) exchange potential proposed by van Leeuwen and
Baerends is[[1386]](../bib_references/bib.md#bib1445)

<a id="eq:vx_LB"></a>
$$
v_{x}^{\text{LB}}=-\beta\left(\frac{x^{2}}{1+3\beta\mbox{sinh}^{-1}(x)}\right) \tag{5.66}
$$

where $x=\|\hat{\bm{\nabla}}\rho\|/\rho^{4/3}$ is the reduced
density gradient. For an exponentially-decaying density, this potential
reduces to $-1/r$ in the asymptotic region of molecular systems. The LB94 xc
potential is formed by a linear combination of LDA XC potential and the LB
exchange potential:[[1386]](../bib_references/bib.md#bib1445)

<a id="Ch5.E67"></a>
$$
v_{xc}^{\text{LB94}}=v_{xc}^{\text{LDA}}+v_{x}^{\text{LB}}\;. \tag{5.67}
$$

The parameter $\beta$ in Eq. ([5.66](#eq:vx_LB)) was determined by fitting to the
exact XC potential for Be atom. As mentioned in Refs. [[213]](../bib_references/bib.md#bib210)

and [[580]](../bib_references/bib.md#bib602)
, for TDDFT calculations, it is sufficient to
include the AC XC potential for ground-state calculations followed by TDDFT
calculations with an adiabatic LDA XC kernel. The implementation of the LB94 XC
potential in **Q-Chem** takes this approach, using the LB94 XC potential for the
ground state calculations, followed by a TDDFT calculation with an adiabatic
LDA XC kernel. This TDLDA/LB94 approach has been widely applied to study
excited-state properties of large molecules.

Since the LB exchange potential in Eq. ([5.66](#eq:vx_LB)) does not come from the
functional derivative of an exchange energy functional, the Levy-Perdew virial
relation[[811]](../bib_references/bib.md#bib845)
 is used instead to obtain the exchange energy:

<a id="Ch5.E68"></a>
$$
E_{x}^{\text{LB}}=-\int v_{x}^{\text{LB}}[\rho](\textbf{r})\bigl{[}3\rho(\mathbf{r})+\mathbf{r}\bm{\cdot}\hat{\bm{\nabla}}\rho(\mathbf{r})\bigr{]}\;d\mathbf{r} \tag{5.68}
$$

An LB94 calculation is requested by setting EXCHANGE = LB94
in the *$rem* section. Additional job control and examples appear below.

LB94_BETA

### `LB94_BETA`

> **Sets the $\beta$ parameter for the LB94 XC potential**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $\beta=n/10000$
>     * .
> * **Recommendation**: Use the default.

???+ example "Example 5.23: Applications of LB94 XC potential to N ${}_{2}$ molecule."
    ```qchem
    $comment
       TDLDA/LB94 calculation is performed for excitation energies.
    $end
    
    $molecule
       0 1
       N    0.0000    0.0000    0.0000
       N    1.0977    0.0000    0.0000
    $end
    
    $rem
       EXCHANGE      lb94
       BASIS         6-311(2+,2+)G**
       CIS_N_ROOTS   30
       RPA           true
    $end
    ```
