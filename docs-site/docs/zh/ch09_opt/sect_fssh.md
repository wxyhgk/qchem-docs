---
title: "9.9.7 Fewest-Switches Surface Hopping"
---

## 9.9.7 Fewest-Switches Surface Hopping

(July 4, 2026)

As discussed in Section [9.8](topic_namd.md), optimization of minimum-energy
crossing points (MECPs) along conical seams, followed by optimization of
minimum-energy pathways that connect these MECPs to other points of interest on
ground- and excited-state potential energy surfaces, affords an appealing
one-dimensional picture of photochemical reactivity that is analogous to the
“reactant $\rightarrow$ transition state $\rightarrow$ product” picture of ground-state
chemistry. Just as the ground-state reaction is not obligated to proceed
*exactly* through the transition-state geometry, however, an excited-state
reaction need not proceed precisely through the MECP and the particulars of
nuclear kinetic energy can lead to deviations. This is arguably more of an
issue for excited-state reactions, where the existence of multiple conical
intersections can easily lead to multiple potential reaction mechanisms. AIMD
potentially offers a way to sample over the available mechanisms in order to
deduce which ones are important in an automated way, but must be extended in
the photochemical case to reactions that involve more than one Born-Oppenheimer
potential energy surface.

The most widely-used trajectory-based method for nonadiabatic simulations is
Tully’s “fewest-switches” surface-hopping (FSSH) algorithm.[[1379]](../bib_references/bib.md#bib1440)

In this approach, classical
trajectories are propagated on a single potential energy surface, but can
undergo “hops” to a different potential surface in regions of near-degeneracy
between surfaces. The probability of these stochastic hops is governed by the
magnitude of the nonadiabatic coupling [Eq. ([9.50](subsec_NACMEs_and_CIs.md#eq:hJK))].
Considering the ensemble average of a swarm of trajectories then provides
information about, *e.g.*, branching ratios for photochemical reactions.

The FSSH algorithm, based on the AIMD code, is available in **Q-Chem** for any
electronic structure method where analytic derivative couplings are available,
which at present means CIS, TDDFT, and their spin-flip analogues (see
Section [9.8.1](subsec_NACMEs_and_CIs.md)). The nuclear dynamics component of the
simulation is specified just as in an AIMD calculation. Artificial decoherence
can be added to the calculation at additional cost according to the augmented
FSSH (AFSSH) method,[[1321]](../bib_references/bib.md#bib1382)
 which
enforces stochastic wave function collapse at a rate proportional to the
difference in forces between the trajectory on the active surface and position
moments propagated the other surfaces. At every time step, the component of
the wave function on each active surface is printed to the output file. These
amplitudes, as well as the position and momentum moments (if AFSSH is
requested), is also printed to a text file called `SurfaceHopper` located
in the `$QC/AIMD` sub-directory of the job’s scratch directory.

In order to request a FSSH calculation, only a few additional *$rem* variables
must be added to those necessary for an excited-state AIMD simulation. At
present, FSSH calculations can only be performed using Born-Oppenheimer
molecular dynamics (BOMD) method. Furthermore, the optimized velocity Verlet
(OVV) integration method is not supported for FSSH calculations.

FSSH_LOWESTSURFACE

### `FSSH_LOWESTSURFACE`

> **Specifies the lowest-energy state considered in a surface hopping calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$
>     * Only states
>     * $n$
>     * and above are considered in a FSSH calculation.
> * **Recommendation**: None

FSSH_NSURFACES

### `FSSH_NSURFACES`

> **Specifies the number of states considered in a surface hopping calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$
>     * $n$
>     * states are considered in the surface hopping calculation.
> * **Recommendation**: Any states which may come close in energy to the active surface should be included in the surface hopping calculation.

FSSH_INITIALSURFACE

### `FSSH_INITIALSURFACE`

> **Specifies the initial state in a surface hopping calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$
>     * An integer between
>     * FSSH_LOWESTSURFACE
>     * and
>     * FSSH_LOWESTSURFACE
>     * $+$
>     * FSSH_NSURFACES
>     * $-1$
>     * .
> * **Recommendation**: None

AFSSH

### `AFSSH`

> **Adds decoherence approximation to surface hopping calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Traditional surface hopping, no decoherence.
>     * 1
>     * Use augmented fewest-switches surface hopping (AFSSH).
> * **Recommendation**: AFSSH will increase the cost of the calculation, but may improve accuracy for some systems. See Refs. 1321 Subotnik J. E., Shenvi N. J. Chem. Phys. (2011) , 134 , pp. 024105 . Link , 1324 Subotnik J. E. J. Phys. Chem. A (2011) , 114 , pp. 12083 . Link , 749 Landry B. R., Subotnik J. E. J. Chem. Phys. (2012) , 137 , pp. 22A513 . Link for more detail.

AIMD_SHORT_TIME_STEP

### `AIMD_SHORT_TIME_STEP`

> **Specifies a shorter electronic time step for FSSH calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `TIME_STEP`
> * **Options**:
>     * $n$
>     * Specify an electronic time step duration of
>     * $n$
>     * /
>     * AIMD_TIME_STEP_CONVERSION
>     * a.u. If
>     * $n$
>     * is less than the nuclear time step variable
>     * TIME_STEP
>     * , the
>     * electronic wave function will be integrated multiple times per nuclear time step,
>     * using a linear interpolation of nuclear quantities such as the energy gradient and
>     * derivative coupling. Note that
>     * $n$
>     * must divide
>     * TIME_STEP
>     * evenly.
> * **Recommendation**: Make as large as possible while keeping the trace of the density matrix close to unity during long simulations. Note that while specifying an appropriate duration for the electronic time step is essential for maintaining accurate wave function time evolution, the electronic-only time steps employ linear interpolation to estimate important quantities. Consequently, a short electronic time step is not a substitute for a reasonable nuclear time step.

FSSH_CONTINUE

### `FSSH_CONTINUE`

> **Restart a FSSH calculation from a previous run, using the file 396.0. When this is enabled, the initial conditions of the surface hopping calculation will be set, including the correct wave function amplitudes, initial surface, and position/momentum moments (if AFSSH) from the final step of some prior calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $0$
>     * Start fresh calculation.
>     * $1$
>     * Restart from previous run.
> * **Recommendation**: None

???+ example "Example 9.44: FSSH simulation. Note that analytic derivative couplings must be requested
via CALC_NAC , but it is unnecessary to include a $derivative_coupling section. The same is true for CIS_STATE_DERIV ,
which will be set to the initial active surface automatically. Finally, one
must be careful to choose a small enough time step for systems that have
energetic access to a region of large derivative coupling, hence the choice for AIMD_TIME_STEP_CONVERSION and TIME_STEP ."
    ```qchem
    $molecule
       0 1
       C   -1.620294    0.348677   -0.008838
       C   -0.399206   -0.437493   -0.012535
       C   -0.105193   -1.296810   -1.081340
       H   -0.789110   -1.374693   -1.905080
       C    1.069016   -2.045054   -1.072304
       H    1.292495   -2.701157   -1.889686
       C    1.956240   -1.940324    0.002842
       H    2.859680   -2.517019    0.008420
       C    1.666259   -1.084065    1.071007
       H    2.348104   -1.005765    1.894140
       C    0.495542   -0.335701    1.065497
       H    0.253287    0.325843    1.871866
       O   -1.931045    1.124872    0.911738
       H   -2.269528    0.227813   -0.865645
    $end
    
    $rem
       JOBTYPE                    aimd
       EXCHANGE                   hf
       BASIS                      3-21g
       CIS_N_ROOTS                3
       CIS_SINGLETS               false
       CIS_TRIPLETS               true
       PROJ_TRANSROT              true
       FSSH_LOWESTSURFACE         1
       FSSH_NSURFACES             3   ! hop between T1 and T2
       FSSH_INITIALSURFACE        1   ! start on T1
       AFSSH                      0   ! no decoherence
       CALC_NAC                   true
       AIMD_STEPS                 50  ! Typically more would be used
       TIME_STEP                  14
       AIMD_SHORT_TIME_STEP       2
       AIMD_TIME_STEP_CONVERSION  1   ! Do not alter time_step duration
       AIMD_PRINT                 1
       AIMD_INIT_VELOC            thermal
       AIMD_TEMP                  300 # K
       AIMD_INTEGRATION           vverlet
       FOCK_EXTRAP_ORDER          6
       FOCK_EXTRAP_POINTS         12
       INTEGRAL_SYMMETRY          off
       POINT_GROUP_SYMMETRY       false
    $end
    ```
