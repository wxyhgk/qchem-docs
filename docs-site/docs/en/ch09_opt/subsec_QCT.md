---
title: "9.9.6 Quasi-Classical Molecular Dynamics"
---

## 9.9.6 Quasi-Classical Molecular Dynamics

(July 4, 2026)

So-called “quasi-classical”
trajectories[[668]](../bib_references/bib.md#bib693)
 (QCT) put vibrational
energy into each mode in the initial velocity setup step, which can improve on
the results of purely classical simulations, for example in the calculation of
photoelectron[[747]](../bib_references/bib.md#bib780)
 or infrared
spectra.[[1142]](../bib_references/bib.md#bib1194)
 Improvements include better agreement of
spectral linewidths with experiment at lower temperatures and better agreement
of vibrational frequencies with anharmonic calculations.

The improvements at low temperatures can be understood by recalling that even
at low temperature there is nuclear motion due to zero-point motion. This is
included in the quasi-classical initial velocities, thus leading to finite peak
widths even at low temperatures. In contrast to that the classical simulations
yield zero peak width in the low temperature limit, because the thermal kinetic
energy goes to zero as temperature decreases. Likewise, even at room
temperature the quantum vibrational energy for high-frequency modes is often
significantly larger than the classical kinetic energy. QCT-MD therefore
typically samples regions of the potential energy surface that are higher in
energy and thus more anharmonic than the low-energy regions accessible to
classical simulations. These two effects can lead to improved peak widths as
well as a more realistic sampling of the anharmonic parts of the potential
energy surface. However, the QCT-MD method also has important limitations which
are described below and that the user has to monitor for carefully.

In our QCT-MD implementation the initial vibrational quantum numbers are
generated as random numbers sampled from a vibrational Boltzmann distribution
at the desired simulation temperature. In order to enable reproducibility of
the results, each trajectory (and thus its set of vibrational quantum numbers)
is denoted by a unique number using the AIMD_QCT_WHICH_TRAJECTORY
variable. In order to loop over different initial conditions, run trajectories
with different choices for AIMD_QCT_WHICH_TRAJECTORY. It is also
possible to assign initial velocities corresponding to an average over a
certain number of trajectories by choosing a negative value. Further technical
details of our QCT-MD implementation are described in detail in Appendix A of
Ref. [[747]](../bib_references/bib.md#bib780)
.

### `AIMD_QCT_WHICH_TRAJECTORY`

> **Picks a set of vibrational quantum numbers from a random distribution.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $n$: Picks the
>     * $n$: th set of random initial velocities. $-n$ Uses an average over
>     * $n$: random initial velocities.
> * **Recommendation**: Pick a positive number if you want the initial velocities to correspond to a particular set of vibrational occupation numbers and choose a different number for each of your trajectories. If initial velocities are desired that corresponds to an average over $n$ trajectories, pick a negative number.

Below is a simple example input for running a QCT-MD simulation of the
vibrational spectrum of water. Most input variables are the same as for
classical MD as described above. The use of quasi-classical initial conditions
is triggered by setting the AIMD_INIT_VELOC variable to
QUASICLASSICAL.

???+ example "Example 9.41: Simulating the IR spectrum of water using QCT-MD."
    ```qchem
    $molecule
       0  1
       O     0.000000    0.000000    0.520401
       H    -1.475015    0.000000   -0.557186
       H     1.475015    0.000000   -0.557186
    $end
    
    $rem
       JOBTYPE                     freq
       INPUT_BOHR                  true
       METHOD                      hf
       BASIS                       3-21g
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
       JOBTYPE                     aimd
       INPUT_BOHR                  true
       METHOD                      hf
       BASIS                       3-21g
       SCF_CONVERGENCE             6
       TIME_STEP                   20    !  (in atomic units)
       AIMD_STEPS                  1250  !  600 fs total simulation time
       AIMD_TEMP                   12
       AIMD_PRINT                  2
       FOCK_EXTRAP_ORDER           6     ! Use a 6th-order extrapolation
       FOCK_EXTRAP_POINTS          12    ! of the previous 12 Fock matrices
       AIMD_MOMENTS                1
       AIMD_NUCL_SAMPLE_RATE       5
       AIMD_NUCL_VACF_POINTS       1000
       AIMD_INIT_VELOC             quasiclassical
       AIMD_QCT_WHICH_TRAJECTORY   1     ! Loop over several values to get
                                         ! the correct Boltzmann distribution.
    $end
    ```

Other types of spectra can be calculated by calculating spectral properties
along the trajectories. For example, we observed that photoelectron spectra can
be approximated quite well by calculating vertical detachment energies (VDEs)
along the trajectories and generating the spectrum as a histogram of the
VDEs.[[747]](../bib_references/bib.md#bib780)
 We have included several simple scripts in the
`$QC/aimdman/tools` subdirectory that we hope the user will find helpful
and that may serve as the basis for developing more sophisticated tools. For
example, we include scripts that allow to perform calculations along a
trajectory (`md_calculate_along_trajectory`) or to calculate vertical
detachment energies along a trajectory (`calculate_rel_energies`).

Another application of the QCT code is to generate random geometries
sampled from the vibrational wave function via a Monte Carlo algorithm.
This is triggered by setting both the AIMD_QCT_INITPOS
and AIMD_QCT_WHICH_TRAJECTORY
variables to negative numbers, say $-m$ and $-n$, and setting
AIMD_STEPS to zero. This will generate $m$ random geometries
sampled from the vibrational wave function corresponding to an average
over $n$ trajectories at the user-specified simulation temperature.

### `AIMD_QCT_INITPOS`

> **Chooses the initial geometry in a QCT-MD simulation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $0$: Use the equilibrium geometry.
>     * $n$: Picks a random geometry according to the harmonic vibrational wave function. $-n$ Generates
>     * $n$: random geometries sampled from the harmonic vibrational wave function.
> * **Recommendation**: None.

For systems that are described well within the harmonic oscillator model and
for properties that rely mainly on the ground-state dynamics, this simple MC
approach may yield qualitatively correct spectra. In fact, one may argue that
it is preferable over QCT-MD for describing vibrational effects at very low
temperatures, since the geometries are sampled from a true quantum distribution
(as opposed to classical and quasi-classical MD). We have included another
script in the *$QC/aimdman/tools* directory to help with the calculation
of vibrationally averaged properties (`monte_geom`).

???+ example "Example 9.42: MC sampling of the vibrational wave function for HCl.
1000 random geometries for HCl are generated based on the harmonic vibrational
wave function at 1 Kelvin. The wave function is averaged over 1000
sets of random vibrational quantum numbers ( i.e. , the ground state in
this case due to the low temperature)."
    ```qchem
    $molecule
       0 1
       H    0.000000    0.000000   -1.216166
       Cl   0.000000    0.000000    0.071539
    $end
    
    $rem
       JOBTYPE                    freq
       METHOD                     b3lyp
       BASIS                      6-311++G**
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE                    aimd
       METHOD                     B3LYP
       BASIS                      6-311++G**
       SCF_CONVERGENCE            1
       MAX_SCF_CYCLES             0
       TIME_STEP                  20     (in atomic units)
       AIMD_STEPS                 0
       AIMD_INIT_VELOC            quasiclassical
       AIMD_QCT_VIBSEED           1
       AIMD_QCT_VELSEED           2
       AIMD_TEMP                  1     (in Kelvin)
       AIMD_QCT_WHICH_TRAJECTORY  -1000 ! set to the desired trajectory number
       AIMD_QCT_INITPOS           -1000
    $end
    ```

It is also possible make some modes inactive, *i.e.*, to put vibrational energy
into a subset of modes (all other are set to zero). The list of active modes
can be specified using the *$qct_active_modes* section. Furthermore, the
vibrational quantum numbers for each mode can be specified explicitly using the
*$qct_vib_distribution* input section. It is also possible to set the phases
using *$qct_vib_phase* (allowed values are 1 and $-$1). Below is a simple sample
input:

```qchem
$qct_active_modes
  1
$end

$qct_vib_distribution
  0
$end

$qct_vib_phase
  1
$end
...
```

Finally we turn to a brief description of the limitations of QCT-MD. Perhaps
the most severe limitation stems from the so-called “kinetic energy spilling”
problem,[[298]](../bib_references/bib.md#bib302)
 which means that there can be an artificial transfer
of kinetic energy between modes. This can happen because the initial
velocities are chosen according to quantum energy levels, which are usually
much higher than those of the corresponding classical systems. Furthermore, the
classical equations of motion also allow for the transfer of non-integer
multiples of the zero-point energy between the modes, which leads to different
selection rules for the transfer of kinetic energy. Typically, energy spills
from high-energy into low-energy modes, leading to spurious “hot” dynamics.
A second problem is that QCT-MD is actually based on classical Newtonian
dynamics, which means that the probability distribution at low temperatures can
be qualitatively wrong compared to the true quantum distribution.[[747]](../bib_references/bib.md#bib780)

**Q-Chem** implements a routine to monitor the kinetic energy within each normal
mode along the trajectory and that is automatically switched on for
quasi-classical simulations. It is thus possible to monitor for trajectories in
which the kinetic energy in one or more modes becomes significantly larger than
the initial energy. Such trajectories should be discarded. (Alternatively, see
Ref. [[298]](../bib_references/bib.md#bib302)
 for a different approach to the zero-point leakage
problem.) Furthermore, this monitoring routine prints the squares of the
(harmonic) vibrational wave function along the trajectory. This makes it
possible to weight low-temperature results with the harmonic quantum
distribution to alleviate the failure of classical dynamics for low
temperatures.
