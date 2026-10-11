---
title: "4.5.15 Square Gradient Minimization (SGM)"
---

## 4.5.15 Square Gradient Minimization (SGM)

(July 4, 2026)

The GDM method (Section [4.5.7](sect_gdm.md))
is an extremely effective energy minimizer but it cannot reliably be
applied to optimize excited-state orbitals, as such states are typically
unstable stationary points in orbital-rotation space. Energy minimization
based approaches therefore tend to ‘slip’ from these saddle points to some
local minima (often the ground state, a phenomenon often described as
‘variational collapse’).

Diptarka Hait and Martin Head-Gordon have proposed an alternative way to
optimize excited state orbitals, by minimizing the square of the energy
gradient against orbital degrees of freedom.[[511]](../bib_references/bib.md#bib526)
 This energy
gradient should be zero for all stationary points in energy, and thus all such
stationary points are global minima of the squared energy gradient $\Delta$.
Quasi-Newton methods therefore can reliably converge to the stationary point
closest to the initial guess orbitals by minimizing $\Delta$, without the risk
of variational collapse. The resulting SGM approach is thus essentially an
extension of GDM that converges to the closest state (*i.e.*, stationary point in
orbital space) to the initial guess, as opposed to the closest energy minimum.
SGM consequently can be used for reliable excited state optimization within a
direct minimization framework, similar to how the MOM algorithm of
Section [4.5.14](topic_mom.md) can be used in conjunction with iterative
diagonalization methods like DIIS. Further details about SGM applying for
excited-state orbital optimization can be found in Section [7.7.5](../ch07_excited/ex_BEDSCF.md).
Full details of the SGM algorithm are provided in Ref. [[511]](../bib_references/bib.md#bib526)
.

The use of SGM is controlled by the SCF_ALGORITHM variable in the
*$rem* section:

SCF_ALGORITHM

### `SCF_ALGORITHM`

> **Algorithm used for converging the SCF.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * SGM
>     * SGM_LS
>     * SGM_QLS
>     * for R and U orbitals only
> * **Recommendation**: SGM should be used for RO and or OS_RO orbitals only. SGM_LS is recommended for R or U orbitals, though it can also be used for RO and OS_RO orbitals. SGM_QLS is a slower, but more robust option for R and U calculations.

DELTA_GRADIENT_SCALE

### `DELTA_GRADIENT_SCALE`

> **Scales the gradient of $\Delta$ by $N$ /100, which can be useful for cases with troublesome convergence by reducing step size.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $N$
> * **Recommendation**: Use default. For problematic cases 50, 25, 10 or even 1 could be useful.
