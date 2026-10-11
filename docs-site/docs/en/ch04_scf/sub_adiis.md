---
title: "4.5.10 Augmented Roothaan Hall Energy DIIS (ADIIS)"
---

## 4.5.10 Augmented Roothaan Hall Energy DIIS (ADIIS)

(July 4, 2026)

Similar to RCA/EDIIS,[[186]](../bib_references/bib.md#bib182)

the ADIIS algorithm proposed by Hu and Yang [[601]](../bib_references/bib.md#bib624)
 is also supposed to
accelerate SCF convergence in cases where DIIS performs poorly in the initial
iterations. This algorithm also involves a Fock matrix extrapolation scheme:

<a id="eq:adiis_fock"></a>

$$
\tilde{\mathbf{F}}_{n+1}=\sum_{i=1}^{n}c_{i}\mathbf{F}_{i} \tag{4.42}
$$

where $\tilde{\mathbf{F}}_{n+1}$ is the extrapolated Fock matrix to be diagonalized to generate
the updated MOs and electron density, $\mathbf{F}_{i}=\mathbf{F}[\mathbf{P}_{i}]$ is
the Fock matrix constructed from the density matrix of the $i$-th iteration, and $\{c_{i}\}$
are the extrapolation coefficients, which are obtained by minimizing the augmented
Roothaan-Hall (ARH) energy function of an extrapolated density
$\tilde{\mathbf{P}}_{i+1}=\sum_{i=1}^{n}\mathbf{P}_{i}$

<a id="A3.S8.EGx3"></a>

$$
\displaystyle f^{\mathrm{ADIIS}}(c_{1},\dots,c_{n})=E[\mathbf{P}_{n}]+\sum_{i=1}^{n}c_{i}(\mathbf{P}_{i}-\mathbf{P}_{n})\cdot\mathbf{F}_{n} \tag{4.43}
$$

while subjected to the constraint $\sum_{i=1}^{n}c_{i}=1,c_{i}\geq 0$ for all $i$.
As suggested in the original literature, [[601]](../bib_references/bib.md#bib624)
 variable substitutions are conducted
($c_{i}=t_{i}^{2}/\sum_{i}t_{i}^{2}$) to convert the constrained optimization to a standard,
unconstrained optimization problem (optimizers such as L-BFGS can be used to solve the latter).
Note that while the sums in Eqs. [4.42](#eq:adiis_fock) and [4.43](#eq:adiis_obj) runs from 1 to $n$, in
practice it is unnecessary to extrapolate using all $\mathbf{P}_{i}$ and $\mathbf{F}_{i}$ obtained
in the previous SCF cycles. In the **Q-Chem** implementation of ADIIS, the number of
$\mathbf{P}_{i}$’s and $\mathbf{F}_{i}$’s used in the extrapolation has a maximum of 6.

The ADIIS algorithm is known to become less efficient in the region close to SCF
convergence. Therefore, it is desirable to use the “ADIIS+DIIS” algorithm, which carries out
ADIIS when the SCF error is below a threshold or the number of ADIIS iterations reaches a
certain value. This hybrid algorithm, which can be invoked by setting “SCF_ALGORITHM
= ADIIS_DIIS” in **Q-Chem**, was shown to afford accelerated convergence for cases
where DIIS alone was unable or took much longer to converge the SCF problem. [[601]](../bib_references/bib.md#bib624)

ADIIS_INNER_CONV

### `ADIIS_INNER_CONV`

> **Convergence criterion for the ADIIS inner loops (L-BFGS optimization of Eq. 4.43 )**
>
> * **Type**: `INTEGER`
> * **Default**: `12`
> * **Options**:
>     * $n$
>     * Using 10
>     * ${}^{-n}$
>     * as the convergence criterion for the ADIIS inner loops
> * **Recommendation**: Use the default

THRESH_ADIIS_SWITCH

### `THRESH_ADIIS_SWITCH`

> **The threshold for switching from ADIIS to DIIS in a ADIIS-DIIS calculations**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * $n$
>     * Switching from ADIIS to DIIS when the SCF error is below
>     * $10^{-n}$
> * **Recommendation**: 3 or 4 is suitable

MAX_ADIIS_CYCLES

### `MAX_ADIIS_CYCLES`

> **The maximum number of ADIIS cycles before switching to DIIS in a ADIIS-DIIS calculations**
>
> * **Type**: `INTEGER`
> * **Default**: `30`
> * **Options**:
>     * $N$
>     * Doing at most
>     * $N$
>     * ADIIS iterations before switching to DIIS
> * **Recommendation**: Use the default; typically there is no benefit of doing ADIIS for too many iterations

???+ example "Example 4.14: B3LYP/3-21G calculation for the Cd(II)-imidazole
complex using the ADIIS_DIIS algorithm (switching
to DIIS when the error is below 10 ${}^{-3}$ ). The SADMO
guess is used."
    ```qchem
    $molecule
    2 1
    Cd     0.000000     0.000000     0.000000
     N     0.000000     0.000000    -2.260001
     N    -0.685444     0.000000    -4.348035
     C     0.676053     0.000000    -4.385069
     C     1.085240     0.000000    -3.091231
     C    -1.044752     0.000000    -3.060220
     H     1.231530     0.000000    -5.300759
     H     2.088641     0.000000    -2.711077
     H    -2.068750     0.000000    -2.726515
     H    -1.313170     0.000000    -5.174718
    $end
    
    $rem
    METHOD          B3LYP
    BASIS           3-21G
    THRESH          14
    SCF_GUESS       SADMO
    SCF_ALGORITHM   ADIIS_DIIS
    SCF_CONVERGENCE 8
    INTEGRAL_SYMMETRY    FALSE
    POINT_GROUP_SYMMETRY FALSE
    $end
    ```
