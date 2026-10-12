---
title: "9.9.4 Thermostats"
---

## 9.9.4 Thermostats

(July 4, 2026)

Implicit in the discussion above was an assumption of conservation of energy,
which implies dynamics run in the *microcanonical* ($NVE$) ensemble.
Alternatively, the AIMD code in **Q-Chem** can sample the *canonical*
($NVT$) ensemble with the aid of thermostats. These mimic the thermal effects
of a surrounding temperature bath, and the time average of a trajectory (or
trajectories) then affords thermodynamic averages at a chosen temperature.
This option is appropriate in particular when multiple minima are thermally
accessible. All sampled information is once again saved in the `AIMD/`
subdirectory of the `$QCSCRATCH` directory for the job. Thermodynamic
averages and error analysis may be performed externally, using these data. Two
commonly used thermostat options, both of which yield proper canonical
distributions of the classical molecular motion, are implemented in **Q-Chem**
and are described in more detail below. Constant-pressure barostats (for
$NPT$ simulations) are not yet implemented.

As with any canonical sampling, the trajectory evolves at the mercy of barrier
heights. Short trajectories will sample only within the local minimum of the
initial conditions, which may be desired for sampling the properties of a given
isomer, for example. Due to the energy fluctuations induced by the thermostat,
the trajectory is neither guaranteed to stay within this potential energy well
nor guaranteed to overcome barriers to neighboring minima, except in the
infinite-sampling limit for the latter case, which is likely never reached in
practice. Importantly, the user should note that the introduction of a
thermostat destroys the validity of any real-time trajectory information;
thermostatted trajectories should *not* be used to assess real-time
dynamical observables, but only to compute thermodynamic averages.

## 9.9.4.1 Langevin Thermostat

A stochastic, white-noise Langevin thermostat (AIMD_THERMOSTAT =
LANGEVIN) combines random “kicks” to the nuclear momenta with a
dissipative, friction term. The balance of these two contributions mimics the
exchange of energy with a surrounding heat bath. The resulting trajectory, in
the long-time sampling limit, generates the correct canonical distribution.
The implementation in **Q-Chem** follows the velocity Verlet formulation of Bussi
and Parrinello,[[176]](../bib_references/bib.md#bib171)
 which remains a valid propagator for all time
steps and thermostat parameters. The thermostat is coupled to each degree of
freedom in the simulated system. The MD integration time step
(TIME_STEP) should be chosen in the same manner as in an NVE
trajectory. The only user-controllable parameter for this thermostat,
therefore, is the timescale over which the implied bath influences the
trajectory. The AIMD_LANGEVIN_TIMESCALE keyword determines this
parameter, in units of femtoseconds. For users who are more accustomed to
thinking in terms of friction strength, this parameter is proportional to the
inverse friction. A small value of the timescale parameter yields a “tight”
thermostat, which strongly maintains the system at the chosen temperature but
does not typically allow for rapid configurational flexibility.
(Qualitatively, one may think of such simulations as sampling in molasses.
This analogy, however, only applies to the thermodynamic sampling properties
and does not suggest any electronic role of the solvent!) These small values
are generally more appropriate for small systems, where the few degrees of
freedom do not rapidly exchange energy and behave may behave in a non-ergodic
fashion. Alternatively, large values of the time-scale parameter allow for
more flexible configurational sampling, with the tradeoff of more (short-term)
deviation from the desired average temperature. These larger values are more
appropriate for larger systems since the inherent, microcanonical exchange of
energy within the large number of degrees of freedom already tends toward
canonical properties. (Think of this regime as sampling in a light, organic
solvent.) Importantly, thermodynamic averages in the infinite-sampling limit
are completely independent of this time-scale parameter. Instead, the time
scale merely controls the efficiency with which the ensemble is explored. If
maximum efficiency is desired, the user may externally compute lifetimes from
the time correlation function of the desired observable and minimize the
lifetime as a function of this timescale parameter. At the end of the
trajectory, the average computed temperature is compared to the requested
target temperature for validation purposes.

???+ example "Example 9.39: Canonical ( $NVT$ ) sampling using AIMD with the Langevin thermostat"
    ```qchem
    $comment
       Short example of using the Langevin thermostat
       for canonical (NVT) sampling
    $end
    
    $molecule
       0 1
       H
       O  1  1.0
       H  2  1.0  1  104.5
    $end
    
    $rem
       JOBTYPE                  aimd
       EXCHANGE                 hf
       BASIS                    sto-3g
       AIMD_TIME_STEP           20      !in au
       AIMD_STEPS               100
       AIMD_THERMOSTAT          langevin
       AIMD_INIT_VELOC          thermal
       AIMD_TEMP                298     !in K - initial conditions AND thermostat
       AIMD_LANGEVIN_TIMESCALE  100     !in fs
    $end
    ```

## 9.9.4.2 Nosé-Hoover Thermostat

An alternative thermostat approach is also available, namely, the Nosé-Hoover
thermostat[[914]](../bib_references/bib.md#bib950)
 (also known as a Nosé-Hoover “chain”), which
mimics the role of a surrounding thermal bath by performing a microcanonical
($NVE$) trajectory in an extended phase space. By allowing energy to be
exchanged with a chain of fictitious particles that are coupled to the target
system, $NVT$ sampling is properly obtained for those degrees of freedom that
represent the real system. (Only the target system properties are saved in
`$QCSCRATCH/AIMD` for subsequent analysis and visualization, not the
fictitious Nosé-Hoover degrees of freedom.) The implementation in **Q-Chem**
follows that of Martyna,[[914]](../bib_references/bib.md#bib950)
 which augments the original
extended-Lagrangian approach of Nosé[[1000]](../bib_references/bib.md#bib1041)
 and
Hoover,[[592]](../bib_references/bib.md#bib615)
 using a chain of auxiliary degrees of freedom to
restore ergodicity in stiff systems and thus afford the correct $NVT$
ensemble. Unlike the Langevin thermostat, the collection of system and
auxiliary chain particles can be propagated in a time-reversible fashion with
no need for stochastic perturbations.

Rather than directly setting the masses and force constants of the auxiliary
chain particles, the **Q-Chem** implementation focuses instead, on the time scale
of the thermostat, as was the case for the Langevin thermostat described above.
The time-scale parameter is controlled by the keyword
NOSE_HOOVER_TIMESCALE, given in units of femtoseconds. The only
other user-controllable parameter for this function is the length of the
Nosé-Hoover chain, which is typically chosen to be 3–6 fictitious
particles. Importantly, the version in **Q-Chem** is currently implemented as a
*single* chain that is coupled to the system, as a whole. Comprehensive
thermostatting in which every single degree of freedom is coupled to its own
thermostat, which is sometimes used for particularly stiff systems, is not
implemented and for such cases the Langevin thermostat is recommended instead.
For large and/or fluxional systems, the single-chain Nosé-Hoover
approach is appropriate.

???+ example "Example 9.40: Canonical ( $NVT$ ) sampling using AIMD with the Nosé-Hoover chain thermostat"
    ```qchem
    $molecule
       0 1
       H
       O 1 1.0
       H 2 1.0 1 104.5
    $end
    
    $rem
       JOBTYPE                 aimd
       EXCHANGE                hf
       BASIS                   sto-3g
       AIMD_TIME_STEP          20      !in au
       AIMD_STEPS              100
       AIMD_THERMOSTAT         nose_hoover
       AIMD_INIT_VELOC         thermal
       AIMD_TEMP               298     !in K - initial conditions AND thermostat
       NOSE_HOOVER_LENGTH      3       !chain length
       NOSE_HOOVER_TIMESCALE   100     !in fs
    $end
    ```

### `AIMD_THERMOSTAT`

> **Applies thermostatting to AIMD trajectories.**
>
> * **Type**: `INTEGER`
> * **Default**: `none`
> * **Options**:
>     * `LANGEVIN`: Stochastic, white-noise Langevin thermostat
>     * `NOSE_HOOVER`: Time-reversible, Nosé-Hoovery chain thermostat
> * **Recommendation**: Use either thermostat for sampling the canonical (NVT) ensemble.

### `AIMD_LANGEVIN_TIMESCALE`

> **Sets the timescale (strength) of the Langevin thermostat**
>
> * **Type**: `INTEGER`
> * **Default**: `none`
> * **Options**:
>     * $n$: Thermostat timescale,asn
>     * $n$: fs
> * **Recommendation**: Smaller values (roughly 100) equate to tighter thermostats but may inhibit rapid sampling. Larger values ( $\geq 1000$ ) allow for more rapid sampling but may take longer to reach thermal equilibrium.

### `NOSE_HOOVER_LENGTH`

> **Sets the chain length for the Nosé-Hoover thermostat**
>
> * **Type**: `INTEGER`
> * **Default**: `none`
> * **Options**:
>     * $n$: Chain length of
>     * $n$: auxiliary variables
> * **Recommendation**: Typically 3-6

### `NOSE_HOOVER_TIMESCALE`

> **Sets the timescale (strength) of the Nosé-Hoover thermostat**
>
> * **Type**: `INTEGER`
> * **Default**: `none`
> * **Options**:
>     * $n$: Thermostat timescale, as
>     * $n$: fs
> * **Recommendation**: Smaller values (roughly 100) equate to tighter thermostats but may inhibit rapid sampling. Larger values ( $\geq 1000$ ) allow for more rapid sampling but may take longer to reach thermal equilibrium.
