---
title: "4.5.18 Orbital Energy Scaling in Canonical ROSCF Calculations"
---

## 4.5.18 Orbital Energy Scaling in Canonical ROSCF Calculations

(July 4, 2026)

For high-spin half-filled open-shell systems, canonical ROSCF calculations
according to Plakhutin and Davidson[[1094]](../bib_references/bib.md#bib1140)
 can be performed by
setting ROSCF_DODS = TRUE. The canonical ROSCF method
provides the same total wave function and, thus, total energy and correct
$\langle\hat{S}^{2}\rangle$ behavior as “conventional” ROSCF.
Other than “conventional” ROSCF, it features two different sets of orbitals for
$\alpha$ and $\beta$ electrons, as unrestrcited SCF does, which fulfill
Koopmans’ theorem. Because of this, canonical ROSCF is also called ROSCF-DODS,
where DODS stands for “different orbitals for different spins”.

In general, ROSCF calculations can be hard to converge, often because of
violations of the aufbau principle. In ROSCF calculations, these situations
can be avoided when applying an intermediary scaling to the open-shell
diagonal blocks of the $\alpha$ and $\beta$ RO Fock matrices, chosen such that
the “correct” orbital ordering is restored during the SCF iterations. The
procedure is similar to level-shifting (Section [4.5.5](sect_lshift.md)) but much
simpler. It exploits the fact that in ROSCF calculations, the diagonal blocks
of the RO Fock matrices can be arbitrarily scaled without affecting the total
wave function.

As an example, consider a system with a single unpaired $\alpha$ electron,
where the highest $\alpha$ MO belongs to the doubly-occupied orbital space
and the lowest $\alpha$ MO belonging to the (doubly-) unoccupied orbital space.
Suppose that these orbitals have energies of
$-0.5$ and $0.5~{}E_{h}$, respectively. If the unpaired
electron has an orbital energy of $-0.6~{}E_{h}$, it might be arbitrarily shifted, *e.g.*,
to $0.3~{}E_{h}$ by scaling its energy with a factor of $0.5~{}E_{h}$,
corresponding to a setting of ROSCF_DIAG_SCALE_A = 50.
This makes life easier for the SCF algorithm.

The obvious caveat of this procedure is that the converged orbital energies
need to be known in order to choose the correct scaling factors. In practice,
one can try different combinations of ROHF_DIAG_SCALE_A and
ROHF_DIAG_SCALE_B, if poor convergence behavior is encountered.

## 4.5.18.1 Job Control

### `ROSCF_DIAG_SCALE_A`

> **When performing canonical restricted open-shell SCF calculations, scale the open-shell diagonal $\alpha$ Fock matrix block (and, thus, singly occupied $\alpha$ orbital energies) during the SCF iterations in order to mitigate aufbau principle violations in case of poorly converging systems. After convergence, proper canonical orbital energies are restored.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $n$: Scale $\alpha$ orbital energies by a factor of $n\cdot 10^{-}2$ .
> * **Recommendation**: In case of convergence issues, try series of different values, e.g., $\pm 800$ , $\pm 400$ , $\pm 200$ , $\pm 100$ , $\pm 50$ , $\pm 20$ , $\pm 10$ .

### `ROSCF_DIAG_SCALE_B`

> **The same as ROSCF_DIAG_SCALE_A , except that singly unpccupied $\beta$ orbital energies are manipulated during the SCF iterations.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $n$: Scale $\beta$ orbital energies by a factor of $n\cdot 10^{-}2$ .
> * **Recommendation**: See ROSCF_DIAG_SCALE_A for recommendations.
