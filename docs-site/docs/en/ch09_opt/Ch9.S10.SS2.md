---
title: "9.10.2 Job Control and Examples"
---

## 9.10.2 Job Control and Examples

(July 4, 2026)

### `PIMC_NBEADSPERATOM`

> **Number of path integral time slices (“beads”) used on each atom of a PIMC simulation.**
>
> * **Type**: `INTEGER`
> * **Default**: `None.`
> * **Options**:
>     * `1`: Perform classical Boltzmann sampling. $>$
>     * `1`: Perform quantum-mechanical path integral sampling.
> * **Recommendation**: This variable controls the inherent convergence of the path integral simulation. The one-bead limit represents classical sampling and the infinite-bead limit represents exact quantum-mechanical sampling. Using 32 beads is reasonably converged for room-temperature simulations of molecular systems.

### `PIMC_TEMP`

> **Temperature, in Kelvin (K), of path integral simulations.**
>
> * **Type**: `INTEGER`
> * **Default**: `None.`
> * **Options**:
>     * User-specified number of Kelvin for PIMC or classical MC simulations.
> * **Recommendation**: None.

### `PIMC_MCMAX`

> **Number of Monte Carlo steps to sample.**
>
> * **Type**: `INTEGER`
> * **Default**: `None.`
> * **Options**:
>     * User-specified number of steps to sample.
> * **Recommendation**: This variable dictates the statistical convergence of MC/PIMC simulations. For converged simulations at least $10^{5}$ steps is recommended.

### `PIMC_WARMUP_MCMAX`

> **Number of Monte Carlo steps to sample during an equilibration period of MC/PIMC simulations.**
>
> * **Type**: `INTEGER`
> * **Default**: `None.`
> * **Options**:
>     * User-specified number of steps to sample.
> * **Recommendation**: Use this variable to equilibrate the molecule/ring polymer before collecting production statistics. Usually a short run of roughly 10% of PIMC_MCMAX is sufficient.

### `PIMC_MOVETYPE`

> **Selects the type of displacements used in MC/PIMC simulations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Cartesian displacements of all beads, with occasional (1%) center-of-mass moves.
>     * `1`: Normal-mode displacements of all modes, with occasional (1%) center-of-mass moves.
>     * `2`: Levy flights without center-of-mass moves.
> * **Recommendation**: Except for classical sampling (MC) or small bead-number quantum sampling (PIMC), Levy flights should be used. For Cartesian and normal-mode moves, the maximum displacement is adjusted during the warm-up run to the desired acceptance rate (controlled by PIMC_ACCEPT_RATE ). For Levy flights, the acceptance is solely controlled by PIMC_SNIP_LENGTH .

### `PIMC_ACCEPT_RATE`

> **Acceptance rate for MC/PIMC simulations when Cartesian or normal-mode displacements are used.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $0<n<100$: User-specified rate, given as a whole-number percentage.
> * **Recommendation**: Choose acceptance rate to maximize sampling efficiency, which is typically signified by the mean-square displacement (printed in the job output). Note that the maximum displacement is adjusted during the warm-up run to achieve roughly this acceptance rate.

### `PIMC_SNIP_LENGTH`

> **Number of “beads” to use in the Levy flight movement of the ring polymer.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $3\leq n\leq\mbox{{\small PIMC\_NBEADSPERATOM}}$: User-specified length of snippet.
> * **Recommendation**: Choose the snip length to maximize sampling efficiency. The efficiency can be estimated by the mean-square displacement between configurations, printed at the end of the output file. This efficiency will typically, however, be a trade-off between the mean-square displacement (length of statistical correlations) and the number of beads moved. Only the moved beads require recomputing the potential, i.e. , a call to Q-Chem for the electronic energy. (Note that the endpoints of the snippet remain fixed during a single move, so $n-2$ beads are actually moved for a snip length of $n$ . For 1 or 2 beads in the simulation, Cartesian moves should be used instead.)

???+ example "Example 9.47: Path integral Monte Carlo simulation of H ${}_{2}$ at room temperature"
    ```qchem
    $comment
    The number of Monte Carlo steps is deliberately set low, more typical
    values would be:
       PIMC_WARMUP_MCMAX    10000   !Equilibration run
       PIMC_MCMAX           100000  !Production run
    $end
    
    $molecule
       0  1
       H
       H 1 0.75
    $end
    
    $rem
       JOBTYPE              pimc
       METHOD               hf
       BASIS                sto-3g
       PIMC_TEMP            298
       PIMC_NBEADSPERATOM   32
       PIMC_WARMUP_MCMAX    100     !Equilibration run
       PIMC_MCMAX           1000    !Production run
       PIMC_MOVETYPE        2         !Levy flights
       PIMC_SNIP_LENGTH     10        !Moves 8 beads per MC step (10-endpts)
    $end
    ```

???+ example "Example 9.48: Classical Monte Carlo simulation of a water molecule at 500K"
    ```qchem
    $comment
    The number of Monte Carlo steps is deliberately set low, more typical
    values would be:
       PIMC_WARMUP_MCMAX    10000   !Equilibration run
       PIMC_MCMAX           100000  !Production run
    $end
    
    $molecule
       0  1
       H
       O 1 1.0
       H 2 1.0 1 104.5
    $end
    
    $rem
       JOBTYPE              pimc
       METHOD               rimp2
       BASIS                cc-pvdz
       AUX_BASIS            rimp2-cc-pvdz
       PIMC_TEMP            500
       PIMC_NBEADSPERATOM   1       !1 bead is classical sampling
       PIMC_WARMUP_MCMAX    100     !Equilibration run
       PIMC_MCMAX           1000    !Production run
       PIMC_MOVETYPE        0       !Cartesian displacements (ok for 1 bead)
       PIMC_ACCEPT_RATE     40      !During warm-up, adjusts step size to 40% acceptance
    $end
    ```
