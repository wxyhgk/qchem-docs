---
title: "4.5.9 Relaxed Constraint Algorithm (RCA)"
---

## 4.5.9 Relaxed Constraint Algorithm (RCA)

(July 4, 2026)

The relaxed constraint algorithm (RCA) is an ingenious and simple means of
minimizing the SCF energy that is particularly effective in cases where the
initial guess is poor. The latter is true, for example, when employing a
user-specified basis (when the “core” or GWH guess must be employed) or when
near-degeneracy effects imply that the initial guess will likely occupy the
wrong orbitals relative to the desired converged solution.

Briefly, RCA begins with the SCF problem as a constrained minimization of the
energy as a function of the density matrix,
$E(\mathbf{P})$.[[186]](../bib_references/bib.md#bib182)
 The constraint is that the density
matrix be idempotent, $\mathbf{P}\cdot\mathbf{P}=\mathbf{P}$, which basically forces the
occupation numbers to be either zero or one. The fundamental realization of
RCA is that this constraint can be relaxed to allow sub-idempotent density
matrices, $\mathbf{P}\cdot\mathbf{P}\leq\mathbf{P}$. This condition forces the occupation
numbers to be between zero and one. Physically, we expect that any state with
fractional occupations can lower its energy by moving electrons from higher
energy orbitals to lower ones. Thus, if we solve for the minimum of $E(\mathbf{P})$
subject to the relaxed sub-idempotent constraint, we expect that the ultimate
solution will nonetheless be idempotent.

In fact, for Hartree-Fock this can be rigorously proven. For density
functional theory, it is possible that the minimum will have fractional
occupation numbers but these occupations have a physical interpretation in
terms of ensemble DFT. The reason the relaxed constraint is easier to deal
with is that it is easy to prove that a linear combination of sub-idempotent
matrices is also sub-idempotent as long as the linear coefficients are between
zero and one. By exploiting this property, convergence can be accelerated in a
way that guarantees the energy will go down at every step.

The implementation of RCA in **Q-Chem** closely follows the “Energy DIIS”
implementation of the RCA algorithm.[[735]](../bib_references/bib.md#bib768)
 Here, the current
density matrix is written as a linear combination of the previous density
matrices:

<a id="Ch4.E39"></a>
$$
\mathbf{P}(x)=\sum_{i}x_{i}\mathbf{P}_{i} \tag{4.39}
$$

To a very good approximation (exact for Hartree-Fock) the energy for $\mathbf{P}(x)$
can be written as a quadratic function of x:

<a id="Ch4.E40"></a>
$$
\mathbf{E}(x)=\sum_{i}E_{i}x_{i}+\frac{1}{2}\sum_{i}x_{i}(\mathbf{P}_{i}-\mathbf{P}_{j})\cdot(\mathbf{F}_{i}-\mathbf{F}_{j})x_{j} \tag{4.40}
$$

At each iteration, $x$ is chosen to minimize $\mathbf{E}(x)$ subject to the
constraint that all of the $x_{i}$ are between zero and one. The Fock matrix for
$\mathbf{P}(x)$ is further written as a linear combination of the previous Fock
matrices,

<a id="Ch4.E41"></a>
$$
\mathbf{F}(x)=\sum_{i}x_{i}\mathbf{F}_{i}+\delta\mathbf{F}_{xc}(x) \tag{4.41}
$$

where $\delta\mathbf{F}_{xc}(x)$ denotes a (usually quite small) change in the
exchange-correlation part that is computed once $x$ has been determined. We
note that this extrapolation is very similar to that used by DIIS. However,
this procedure is guaranteed to reduce the energy $\mathbf{E}(x)$ at every
iteration, unlike DIIS.

In practice, the RCA approach is ideally suited to difficult convergence
situations because it is immune to the erratic orbital swapping that can occur
in DIIS. On the other hand, RCA appears to perform relatively poorly near
convergence, requiring a relatively large number of steps to improve the
precision of a good approximate solution. It is thus advantageous in many
cases to run RCA for the initial steps and then switch to DIIS either after
some specified number of iterations or after some target convergence threshold
has been reached. Finally, note that by its nature RCA considers the energy as
a function of the density matrix. As a result, it cannot be applied to
restricted open shell calculations which are explicitly orbital-based. Note:
RCA interacts poorly with INCDFT, so INCDFT is disabled by default when an RCA
or RCA_DIIS calculation is requested. To enable INCDFT with such a
calculation, set INCDFT = 2 in the *$rem* section. RCA may also have
poor interactions with incremental Fock builds; if RCA fails to converge,
setting INCFOCK = FALSE
may improve convergence in some cases.

Job-control variables for RCA are listed below, along with an example of its use.

RCA_PRINT

### `RCA_PRINT`

> **Controls the output from RCA SCF optimizations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * No print out
>     * 1
>     * RCA summary information
>     * 2
>     * Level 1 plus RCA coefficients
>     * 3
>     * Level 2 plus RCA iteration details
> * **Recommendation**: None

MAX_RCA_CYCLES

### `MAX_RCA_CYCLES`

> **The maximum number of RCA iterations before switching to DIIS when SCF_ALGORITHM is RCA_DIIS.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * N
>     * N RCA iterations before switching to DIIS
> * **Recommendation**: None

THRESH_RCA_SWITCH

### `THRESH_RCA_SWITCH`

> **The threshold for switching between RCA and DIIS when SCF_ALGORITHM is RCA_DIIS.**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * N
>     * Algorithm changes from RCA to DIIS when Error is less than
>     * $10^{-N}$
>     * .
> * **Recommendation**: None

???+ example "Example 4.13: RCA_DIIS algorithm applied a radical"
    ```qchem
    $molecule
    0 2
       H    1.004123   -0.180454    0.000000
       O   -0.246002    0.596152    0.000000
       O   -1.312366   -0.230256    0.000000
    $end
    
    $rem
       UNRESTRICTED         true
       METHOD               hf
       BASIS                cc-pVDZ
       SCF_GUESS            gwh
       SCF_ALGORITHM        RCA_DIIS
       THRESH               9
    $end
    ```
