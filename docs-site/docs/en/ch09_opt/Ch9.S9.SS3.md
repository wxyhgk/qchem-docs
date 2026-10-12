---
title: "9.9.3 Additional Job Control and Examples"
---

## 9.9.3 Additional Job Control and Examples

(July 4, 2026)

### `AIMD_INIT_VELOC`

> **Specifies the method for selecting initial nuclear velocities.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `THERMAL`: Random sampling of nuclear velocities from a Maxwell-Boltzmann distribution. The user must specify the temperature in Kelvin via the $rem variable AIMD_TEMP .
>     * `ZPE`: Choose velocities in order to put zero-point vibrational energy into each normal mode, with random signs. This option requires that a frequency job to be run beforehand.
>     * `QUASICLASSICAL`: Puts vibrational energy into each normal mode. In contrast to the
>     * ZPE option, here the vibrational energies are sampled from a: Boltzmann distribution at the desired simulation temperature. This also triggers several other options, as described below.
>     * `OLD`: Use the same initial velocities as the immediately preceding AIMD job.
>     * `RESTART`: Use the final velocities from a previous AIMD job, reading them from disk.
> * **Recommendation**: This variable need only be specified in the event that velocities are not specified explicitly in a $velocity section.

### `AIMD_INIT_VELOC_NANO_RANDOM`

> **Uses a more precise random seed for generating random initial velocities.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `FALSE`: Use a less precise random seed.
> * **Recommendation**: Leave this set to TRUE unless necessary. This option determines the source of the random seed used for sampling random initial velocities when AIMD_INIT_VELOC requires such. Setting the option to FALSE will have the seed based on the system time in seconds, meaning that two otherwise identical simulations starting in the same second will produce identical initial velocities. With the option set to TRUE, such collisions are virtually impossible. The option is kept for legacy purposes. There should rarely ever be a need to set it to FALSE.

### `AIMD_MOMENTS`

> **Requests that multipole moments be output at each time step.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Output the first
>     * $n$: multipole moments.
> * **Recommendation**: None

### `AIMD_TEMP`

> **Specifies a temperature (in Kelvin) for Maxwell-Boltzmann velocity sampling.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * User-specified number of Kelvin.
> * **Recommendation**: This variable is only useful in conjunction with AIMD_INIT_VELOC = THERMAL . Note that the simulations are run at constant energy, rather than constant temperature, so the mean nuclear kinetic energy will fluctuate in the course of the simulation.

### `DEUTERATE`

> **Requests that all hydrogen atoms be replaces with deuterium.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Replace hydrogens with deuterium.
> * **Recommendation**: Replacing hydrogen atoms reduces the fastest vibrational frequencies by a factor of 1.4, which allow for a larger fictitious mass and time step in ELMD calculations. There is no reason to replace hydrogens in BOMD calculations.

???+ example "Example 9.34: Simulating thermal fluctuations of the water dimer at 298 K."
    ```qchem
    $molecule
       0  1
       O   1.386977   0.011218   0.109098
       H   1.748442   0.720970  -0.431026
       H   1.741280  -0.793653  -0.281811
       O  -1.511955  -0.009629  -0.120521
       H  -0.558095   0.008225   0.047352
       H  -1.910308   0.077777   0.749067
    $end
    
    $rem
       JOBTYPE              aimd
       AIMD_METHOD          bomd
       METHOD               b3lyp
       BASIS                6-31g*
       TIME_STEP            20        (20 a.u. = 0.48 fs)
       AIMD_STEPS           1000
       AIMD_INIT_VELOC      thermal
       AIMD_TEMP            298
       FOCK_EXTRAP_ORDER    6         request Fock matrix extrapolation
       FOCK_EXTRAP_POINTS   12
    $end
    ```

???+ example "Example 9.35: Propagating $\rm F^{-}(H_{2}O)_{4}$ on its first excited-state potential energy
surface, calculated at the CIS level."
    ```qchem
    $comment
      Note, only a few time steps are taken, a more appropriate
      number would be:
       AIMD_STEPS       827   500 fs
    $end
    
    $molecule
       -1   1
       O  -1.969902  -1.946636   0.714962
       H  -2.155172  -1.153127   1.216596
       H  -1.018352  -1.980061   0.682456
       O  -1.974264   0.720358   1.942703
       H  -2.153919   1.222737   1.148346
       H  -1.023012   0.684200   1.980531
       O  -1.962151   1.947857  -0.723321
       H  -2.143937   1.154349  -1.226245
       H  -1.010860   1.980414  -0.682958
       O  -1.957618  -0.718815  -1.950659
       H  -2.145835  -1.221322  -1.158379
       H  -1.005985  -0.682951  -1.978284
       F   1.431477   0.000499   0.010220
    $end
    
    $rem
       JOBTYPE           aimd
       AIMD_METHOD       bomd
       METHOD            hf
       BASIS             6-31+G*
       ECP               SRLC
       PURECART          1111
       CIS_N_ROOTS       3
       CIS_TRIPLETS      false
       CIS_STATE_DERIV   1         propagate on first excited state
       AIMD_INIT_VELOC   thermal
       AIMD_TEMP         150
       TIME_STEP         25
       AIMD_STEPS        10
    $end
    ```

???+ example "Example 9.36: Simulating vibrations of the NaCl molecule using ELMD."
    ```qchem
    $molecule
       0  1
       Na   0.000000   0.000000  -1.742298
       Cl   0.000000   0.000000   0.761479
    $end
    
    $rem
       JOBTYPE    freq
       METHOD     b3lyp
       ECP        fit-sbkjc
       BASIS      sbkjc
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE           aimd
       METHOD            b3lyp
       ECP               fit-sbkjc
       BASIS             sbkjc
       TIME_STEP         14
       AIMD_STEPS        500
       AIMD_METHOD       curvy
       AIMD_FICT_MASS    360
       AIMD_INIT_VELOC   zpe
    $end
    ```

**Q-Chem** has the ability to do AIMD with frozen bonds by using RATTLE
algorithm.[[45]](../bib_references/bib.md#bib28)
 It can be requested by setting the rem variable
AIMD_INTEGRATION to RATTLE. Constraints are imposed via the
*$rattle* input section, whose format is shown below.

> ```qchem
> $rattle
>    bond  atom1  atom2  value
>    ....  .....  .....  .....
> $end
> ```

!!! note "Note"
    The bond length values should be in Ångstrom units.


The convergence threshold and the number of maximum iterations for RATTLE steps
are controlled by the following *$rem* variables: RATTLE_THRESH (with
a default value of 6) and RATTLE_MAXIT (with a default value of 100).

???+ example "Example 9.37: Simulating water molecule using RATTLE algorithm."
    ```qchem
    $molecule
       0 1
       O
       H 1 0.95
       H 1 0.96 2 104.5
    $end
    
    $rem
       JOBTYPE             aimd
       METHOD              b3lyp
       BASIS               6-31G*
       TIME_STEP           15
       AIMD_STEPS          10
       AIMD_INIT_VELOC     thermal Boltzmann distribution
       AIMD_TEMP           300     (in Kelvin)
       AIMD_PRINT          1
       AIMD_INTEGRATION    RATTLE
       DEBUG_RANDOM_SEED   true
    $end
    
    $rattle
       bond 1 2 0.950
       bond 1 3 0.950
       bond 2 3 1.565
    $end
    ```

???+ example "Example 9.38: Excited-state AIMD with exciton analysis at each step."
    ```qchem
    $comment
    AIMD trajectory with wave-function analysis performed at each step.
    This is invoved by  STATE_ANALYSIS=true and AIMD_PRINT=2
    $end
    
    $molecule
    0 1
      O   -2.1904701    0.5202006    0.0237374
      H   -1.2011437    0.4799213    0.0090967
      H   -2.4798356   -0.3698583   -0.2997841
    $end
    
    $rem
       JOBTYPE              aimd
       METHOD               hf
       BASIS                6-31+G*
       CIS_N_ROOTS          3
       CIS_TRIPLETS         false
       AIMD_STEPS           5
       TIME_STEP            40
       AIMD_INIT_VELOC      thermal
       AIMD_TEMP            500
       AIMD_INTEGRATION     vverlet
       CIS_STATE_DERIV      1
       STATE_ANALYSIS       true
       AIMD_PRINT           2
    $end
    
    ```
