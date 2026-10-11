---
title: "7.10.13 ADC Job Control"
---

## 7.10.13 ADC Job Control

(July 4, 2026)

For an ADC calculation it is important to ensure that there are sufficient resources
available for the necessary integral calculations and transformations. These resources
are controlled using the *$rem* variables MEM_STATIC and MEM_TOTAL.
The memory used by ADC is currently 95% of the difference
MEM_TOTAL $-$ MEM_STATIC.

An ADC calculation is requested by setting the *$rem* variable METHOD to the
respective ADC variant. Furthermore, the number of excited
states to be calculated
has to be specified using one of the *$rem* variables EE_STATES,
EE_SINGLETS or EE_TRIPLETS.
The former variable should be used for
open-shell or unrestricted closed-shell calculations, while the latter two variables are
intended for restricted closed-shell calculations. Even though not recommended, it is
possible to use EE_STATES in a restricted calculation which translates into
EE_SINGLETS, if neither EE_SINGLETS nor EE_TRIPLETS is set.
Similarly, the use EE_SINGLETS in an unrestricted calculation will translate
into EE_STATES, if the latter is not set as well.
For IP- and EA-ADC calculations, the IP_STATES,
EOM_IP_ALPHA, EOM_IP_BETA, EA_STATES,
EOM_EA_ALPHA and EOM_EA_BETA are available to control the number and
type of ionized or electron-attached states to calculate. IP_STATES and
EA_STATES should be used in case of restricted calculations, while the
EOM_[IP/EA]_[ALPHA/BETA] keywords control the number of $\alpha$- and
$\beta$-ionized and -electron-attached states to calculate in case of unrestricted
or open-shell calculations.

All *$rem* variables to set the number of excited, ionized or electron-attached states
accept either an integer number
or a vector of integer numbers. A single number specifies that the same number of excited
states are calculated for every irreducible representation the point group of the
molecular system possesses (molecules without symmetry are treated as $C_{1}$ symmetric).
In contrast, a vector of numbers determines the number of states for each irreducible
representation explicitly. Thus, the length of the vector always has to match the number
of irreducible representations. Hereby, the excited states are labeled according to the
irreducible representation of the electronic transition which might be different from
the irreducible representation of the excited state wave function.
Users can choose to calculate any molecule as $C_{1}$ symmetric by setting
CC_SYMMETRY = FALSE.

METHOD

### `METHOD`

> **Controls the order in perturbation theory of ADC.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * ADC(1)
>     * Perform ADC(1) calculation.
>     * ADC(2)
>     * Perform ADC(2)-s, IP-ADC(2)-s or EA-ADC(2)-s calculation.
>     * ADC(2)-x
>     * Perform ADC(2)-x calculation.
>     * ADC(3)
>     * Perform ADC(3), IP-ADC(3) or EA-ADC(3) calculation.
>     * SOS-ADC(2)
>     * Perform spin-opposite scaled ADC(2)-s calculation.
>     * SOS-ADC(2)-x
>     * Perform spin-opposite scaled ADC(2)-x calculation.
>     * CVS-ADC(1)
>     * Perform ADC(1) calculation of core excitations.
>     * CVS-ADC(2)
>     * Perform ADC(2)-s calculation of core excitations.
>     * CVS-ADC(2)-x
>     * Perform ADC(2)-x calculation of core excitations.
> * **Recommendation**: None

EE_STATES

### `EE_STATES`

> **Controls the number of excited states to calculate.**
>
> * **Type**: `INTEGER/ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Number of states to calculate for each irrep or
>     * $[n_{1},n_{2},...]$
>     * Compute
>     * $n_{1}$
>     * states for the first irrep,
>     * $n_{2}$
>     * states for the second irrep, …
> * **Recommendation**: Use this variable to define the number of excited states in case of unrestricted or open-shell calculations. In restricted calculations it can also be used, if neither EE_SINGLETS nor EE_TRIPLETS is given. Then, it has the same effect as setting EE_SINGLETS .

EE_SINGLETS

### `EE_SINGLETS`

> **Controls the number of singlet excited states to calculate.**
>
> * **Type**: `INTEGER/ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Number of singlet states to calculate for each irrep or
>     * $[n_{1},n_{2},...]$
>     * Compute
>     * $n_{1}$
>     * states for the first irrep,
>     * $n_{2}$
>     * states for the second irrep, …
> * **Recommendation**: Use this variable to define the number of excited states in case of restricted calculations of singlet states. In unrestricted calculations it can also be used, if EE_STATES not set. Then, it has the same effect as setting EE_STATES .

EE_TRIPLETS

### `EE_TRIPLETS`

> **Controls the number of triplet excited states to calculate.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Number of triplet states to calculate for each irrep or
>     * $[n_{1},n_{2},...]$
>     * Compute
>     * $n_{1}$
>     * states for the first irrep,
>     * $n_{2}$
>     * states for the second irrep, …
> * **Recommendation**: Use this variable to define the number of excited states in case of restricted calculations of triplet states.

IP_STATES

### `IP_STATES`

> **Controls the number of ionized states to calculate.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Number of states to calculate for each irrep or
>     * $[n_{1},n_{2},...]$
>     * Compute
>     * $n_{1}$
>     * states for the first irrep,
>     * $n_{2}$
>     * states for the second irrep, …
> * **Recommendation**: Use this variable to define the number of ionized states in case of restricted calculations.

EOM_IP_ALPHA

### `EOM_IP_ALPHA`

> **Controls the number of $\alpha$ -ionized states to calculate.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Number of
>     * $\alpha$
>     * -ionized states to calculate for each irrep or
>     * $[n_{1},n_{2},...]$
>     * Compute
>     * $n_{1}$
>     * $\alpha$
>     * -ionized states for the first irrep,
>     * $n_{2}$
>     * $\alpha$
>     * -ionized states for the second irrep, …
> * **Recommendation**: Use this variable to define the number of $\alpha$ -ionized states in case of unrestricted or open-shell calculations.

EOM_IP_BETA

### `EOM_IP_BETA`

> **Controls the number of $\beta$ -ionized states to calculate.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Number of
>     * $\beta$
>     * -ionized states to calculate for each irrep or
>     * $[n_{1},n_{2},...]$
>     * Compute
>     * $n_{1}$
>     * $\beta$
>     * -ionized states for the first irrep,
>     * $n_{2}$
>     * $\beta$
>     * -ionized states for the second irrep, …
> * **Recommendation**: Use this variable to define the number of $\beta$ -ionized states in case of unrestricted or open-shell calculations.

EA_STATES

### `EA_STATES`

> **Controls the number of electron-attached states to calculate.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Number of states to calculate for each irrep or
>     * $[n_{1},n_{2},...]$
>     * Compute
>     * $n_{1}$
>     * states for the first irrep,
>     * $n_{2}$
>     * states for the second irrep, …
> * **Recommendation**: Use this variable to define the number of electron-attached states in case of restricted calculations.

EOM_EA_ALPHA

### `EOM_EA_ALPHA`

> **Controls the number of $\alpha$ -electron-attached states to calculate.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Number of
>     * $\alpha$
>     * -electron-attached states to calculate for each irrep or
>     * $[n_{1},n_{2},...]$
>     * Compute
>     * $n_{1}$
>     * $\alpha$
>     * -electron-attached states for the first irrep,
>     * $n_{2}$
>     * $\alpha$
>     * -electron-attached states for the second irrep, …
> * **Recommendation**: Use this variable to define the number of $\alpha$ -electron-attached states in case of unrestricted or open-shell calculations.

EOM_EA_BETA

### `EOM_EA_BETA`

> **Controls the number of $\beta$ -electron-attached states to calculate.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Number of
>     * $\beta$
>     * -electron-attached states to calculate for each irrep or
>     * $[n_{1},n_{2},...]$
>     * Compute
>     * $n_{1}$
>     * $\beta$
>     * -electron-attached states for the first irrep,
>     * $n_{2}$
>     * $\beta$
>     * -electron-attached states for the second irrep, …
> * **Recommendation**: Use this variable to define the number of $\beta$ -electron-attached states in case of unrestricted or open-shell calculations.

CC_SYMMETRY

### `CC_SYMMETRY`

> **Activates point-group symmetry in the ADC calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * TRUE
>     * Employ point-group symmetry
>     * FALSE
>     * Do not use point-group symmetry
> * **Recommendation**: None

ADC_DENSITY_ORDER

### `ADC_DENSITY_ORDER`

> **Controls the order of the ground state density used for the computation of third-order ADC matrix elements (non-CVS methods only).**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * 3
>     * Use a third-order ground state density computed from the IP-ADC(3)
>     * effective transition moments and the corresponding
>     * fourth order static self-energy according to the
>     * $\Sigma(4)$
>     * scheme
>     * 4
>     * Use an improved third-order ground state density and the corresponding
>     * improved fourth-order static self-energy computed according to the
>     * self-consistent
>     * $\Sigma(4+)$
>     * procedure
> * **Recommendation**: In case of IP-ADC(3) calculations, employing the $\Sigma(4+)$ scheme provides more accurate ionization potentials and ionized state dipole moments.

ADC_DENSITY_MAXITER

### `ADC_DENSITY_MAXITER`

> **When setting ADC_DENSITY_ORDER = 4, this keyword controls the maximum number of DIIS iterations carried out in the $\Sigma(4+)$ procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `1000`
> * **Options**:
>     * $n$
>     * User-defined integer.
> * **Recommendation**: Use the default value.

ADC_DIRECT

### `ADC_DIRECT`

> **For third-order ADC methods, this keyword controls if some large intermediate tensor contractions should be carried out in advance and the result saved in memory for later use or if these quantities should be evaluated directly whenever they are encountered.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Directly evaluate some
>     * $N^{6}$
>     * -scaling tensor contractions. This will reduce the memory
>     * requirement by
>     * $\sim$
>     * 10 %.
>     * FALSE
>     * Precompute all possible
>     * $N^{6}$
>     * -scaling intermediates. This will speed up ADC(3)
>     * calculations considerably (by a factor of
>     * $\sim$
>     * 3 in case of ADC(3) for
>     * $N$
>     * -electron excitations and somewhat less for IP- and EA-ADC(3)).
> * **Recommendation**: Use the default value unless memory is the bottleneck.

ADC_STRICT_ISR

### `ADC_STRICT_ISR`

> **Controls how second-order ground state contributions are treated in the calculation of second- and third-order IP- and EA-ADC state properties using the second-order ISR formalism.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Scale the second-order part of the ground state contribution to one-electron
>     * properties of ionized/electron-attached states by the
>     * one-hole/one-particle character of the respective states
>     * as implied by the strict ISR derivation.
>     * FALSE
>     * Use the full second-order ground state contribution for each
>     * ionized/electron-attached state property.
> * **Recommendation**: Use the default value. Both options are, however, valid second-order treatments of ionized/electron-attached state properties and should yield very similar results for states with predominant one-hole/one-particle chaaracter.

ADC_DO_DYSON

### `ADC_DO_DYSON`

> **Controls if Dyson orbitals are output in case of IP- and EA-ADC calculations. This keyword only takes effect when used together with STATE_ANALYSIS = TRUE . See Section 10.2.12 for further details.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Output Dyson orbitals as cube files.
>     * FALSE
>     * Do not output Dyson orbitals.
> * **Recommendation**: Set to TRUE if visualization of ionization/electron-attachment processes is desired.

ADC_CAP

### `ADC_CAP`

> **Controls the type of CAP/ADC calculation to be performed.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 1
>     * Perform a subspace-projected CAP/ADC calculation.
> * **Recommendation**: Set to 1 for the computation of CAP/ADC subspace projections.

CAP_X

### `CAP_X`

> **For ADC methods, in combination with a smoothed Voronoi-CAP ( CAP_TYPE = 2) or a spherical CAP ( CAP_TYPE = 0), this keyword controls the lower limit for a series of CAP onsets, where the upper limit is given by CAP_X_END . The parameter value in a.u. is obtained by multiplying the given integer by $10^{-3}$ . In this case, the onset value defines the region around the molecule with zero CAP strength. In combination with a cuboid CAP ( CAP_TYPE = 1) or in general for other electronic structure methods (see 7.9.10 for further details), this keyword controls the CAP onset in $x$ direction.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * User-defined integer.
> * **Recommendation**: Usually, values of 2000 to 4000 (corresponding to onset values between 2.0 and 4.0 a.u.) give reasonable results.

CAP_X_STEP

### `CAP_X_STEP`

> **Controls the step size for a series of CAP onsets between CAP_X and CAP_X_END . The parameter value in a.u. is obtained by multiplying the given integer by $10^{-3}$ . Currently only used in ADC methods.**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * $n>0$
>     * User-defined integer.
> * **Recommendation**: None.

CAP_X_END

### `CAP_X_END`

> **Controls the upper onset limit for a series of CAP onsets, where the lower limit is given by CAP_X . The parameter value in a.u. is obtained by multiplying the given integer by $10^{-3}$ . Currently only used in ADC methods.**
>
> * **Type**: `INTEGER`
> * **Default**: `CAP_X`
> * **Options**:
>     * $n>\text{\mbox{{\small CAP\_X}}}$
>     * User-defined integer.
> * **Recommendation**: Use this keyword if CAP onset series are desired.

ADC_PROP_ES

### `ADC_PROP_ES`

> **Controls the calculation of excited, ionized or electron-attached state properties (currently only dipole moments and $\hat{r}^{2}$ expectation values).**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Calculate excited, ionized or electron-attached state properties.
>     * FALSE
>     * Do not compute state properties.
> * **Recommendation**: Set to TRUE , if properties are required.

ADC_PROP_ES2ES

### `ADC_PROP_ES2ES`

> **Controls the calculation of transition properties between excited, ionized or electron-attached states (currently only transition dipole moments and oscillator strengths). For ADC for $N$ -electron excitations, this keyword also controls the computation of two-photon absorption cross-sections of excited states using the sum-over-states expression.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Calculate state-to-state transition properties.
>     * FALSE
>     * Do not compute transition properties between excited, ionized or
>     * electron-attached states.
> * **Recommendation**: Set to TRUE , if state-to-state properties (ADC, IP-ADC, EA-ADC) or sum-over-states two-photon absorption cross-sections (only ADC) are required.

ADC_PROP_TPA

### `ADC_PROP_TPA`

> **Controls the calculation of two-photon absorption cross-sections of excited states using matrix inversion techniques.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Calculate two-photon absorption cross-sections.
>     * FALSE
>     * Do not compute two-photon absorption cross-sections.
> * **Recommendation**: Set to TRUE , if to obtain two-photon absorption cross-sections.

STATE_ANALYSIS

### `STATE_ANALYSIS`

> **Controls the analysis and export of excited, ionized or electron-attached state densities and orbitals (see 10.2.12 for details).**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Perform excited state analyses.
>     * FALSE
>     * No excited state analyses or export will be performed.
> * **Recommendation**: Set to TRUE , if detailed analysis of the excited, ionized or electron-attached states is required or if density or orbital plots are needed.

ADC_C_T

### `ADC_C_T`

> **Set the spin-opposite scaling parameter $c_{T}$ for an SOS-ADC(2) calculation. The parameter value is obtained by multiplying the given integer by $10^{-3}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `1300`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $n\cdot 10^{-3}$
> * **Recommendation**: Use the default.

ADC_C_C

### `ADC_C_C`

> **Set the spin-opposite scaling parameter $c_{c}$ for the ADC(2) calculation. The parameter value is obtained by multiplying the given integer by $10^{-3}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `1170`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $n\cdot 10^{-3}$
> * **Recommendation**: Use the default.

ADC_C_X

### `ADC_C_X`

> **Set the spin-opposite scaling parameter $c_{x}$ for the ADC(2)-x calculation. The parameter value is obtained by multiplying the given integer by $10^{-3}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `1300`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $n\cdot 10^{-3}$
> * **Recommendation**: Use the default.

ADC_NGUESS_SINGLES

### `ADC_NGUESS_SINGLES`

> **Controls the number of excited state guess vectors which are single excitations, one-hole ionizations and one-particle electron-attachments in case of ADC, IP-ADC and EA-ADC, respectively. If the number of requested excited states exceeds the total number of guess vectors (singles and doubles), this parameter is automatically adjusted, so that the number of guess vectors matches the number of requested excited states.**
>
> * **Type**: `INTEGER`
> * **Default**: `Equals to the number of excited states requested.`
> * **Options**:
>     * $n$
>     * User-defined integer.
> * **Recommendation**: Increase if there are convergence problems.

ADC_NGUESS_DOUBLES

### `ADC_NGUESS_DOUBLES`

> **Controls the number of excited state guess vectors which are double excitations, two-hole-one-particle ionizations and one-hole-two-particle electron-attachments in case of ADC, IP-ADC and EA-ADC, respectively.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * User-defined integer.

ADC_DO_DIIS

### `ADC_DO_DIIS`

> **Activates the use of the DIIS algorithm for the calculation of ADC(2) excited states.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Use DIIS algorithm.
>     * FALSE
>     * Do diagonalization using Davidson algorithm.
> * **Recommendation**: None.

ADC_DIIS_START

### `ADC_DIIS_START`

> **Controls the iteration step at which DIIS is turned on.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $n$
>     * User-defined integer.
> * **Recommendation**: Set to a large number to switch off DIIS steps.

ADC_DIIS_SIZE

### `ADC_DIIS_SIZE`

> **Controls the size of the DIIS subspace.**
>
> * **Type**: `INTEGER`
> * **Default**: `7`
> * **Options**:
>     * $n$
>     * User-defined integer
> * **Recommendation**: None

ADC_DIIS_MAXITER

### `ADC_DIIS_MAXITER`

> **Controls the maximum number of DIIS iterations.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $n$
>     * User-defined integer.
> * **Recommendation**: Increase in case of slow convergence.

ADC_DIIS_ECONV

### `ADC_DIIS_ECONV`

> **Controls the convergence criterion for the excited state energy during DIIS.**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $10^{-n}$
> * **Recommendation**: None

ADC_DIIS_RCONV

### `ADC_DIIS_RCONV`

> **Convergence criterion for the residual vector norm of the excited state during DIIS.**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $10^{-n}$
> * **Recommendation**: None

ADC_DAVIDSON_MAXSUBSPACE

### `ADC_DAVIDSON_MAXSUBSPACE`

> **Controls the maximum subspace size for the Davidson procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `$5\times$`
> * **Options**:
>     * $n$
>     * User-defined integer.
> * **Recommendation**: Should be at least 2–4 $\times$ the number of excited states to calculate. The larger the value the more disk space is required.

ADC_DAVIDSON_MAXITER

### `ADC_DAVIDSON_MAXITER`

> **Controls the maximum number of iterations of the Davidson procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `60`
> * **Options**:
>     * $n$
>     * Number of iterations
> * **Recommendation**: Use the default unless convergence problems are encountered.

ADC_DAVIDSON_CONV

### `ADC_DAVIDSON_CONV`

> **Controls the convergence criterion of the Davidson procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `$6$`
> * **Options**:
>     * $n\leq 12$
>     * Corresponding to
>     * $10^{-n}$
>     * .
> * **Recommendation**: Use the default unless higher accuracy is required or convergence problems are encountered.

ADC_DAVIDSON_THRESH

### `ADC_DAVIDSON_THRESH`

> **Controls the threshold for the norm of expansion vectors to be added during the Davidson procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `Twice the value of`
> * **Options**:
>     * $n\leq 14$
>     * Corresponding to
>     * $10^{-n}$
> * **Recommendation**: Use the default unless convergence problems are encountered. The threshold value $10^{-n}$ should always be smaller than the convergence criterion ADC_DAVIDSON_CONV .

ADC_PRINT

### `ADC_PRINT`

> **Controls the amount of printing during an ADC calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 0
>     * Quiet: almost only results are printed.
>     * 1
>     * Normal: basic status information and results are printed.
>     * 2
>     * Debug: more status information, extended information on timings.
>     * …
> * **Recommendation**: Use the default.

ADC_CVS

### `ADC_CVS`

> **Activates the use of the CVS approximation for the calculation of CVS-ADC core-excited states.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Activates the CVS approximation.
>     * FALSE
>     * Do not compute core-excited states using the CVS approximation.
> * **Recommendation**: Set to TRUE , if to obtain core-excited states for the simulation of x-ray absorption spectra. In the case of TRUE , the $rem variable CC_REST_OCC has to be defined as well.

CC_REST_OCC

### `CC_REST_OCC`

> **Sets the number of restricted occupied orbitals including active core occupied orbitals.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Restrict
>     * $n$
>     * energetically lowest occupied orbitals to correspond to the
>     * active core space.
> * **Recommendation**: Example: cytosine with the molecular formula C ${}_{4}$ H ${}_{5}$ N ${}_{3}$ O includes one oxygen atom. To calculate O 1s core-excited states, $n$ has to be set to 1, because the 1s orbital of oxygen is the energetically lowest. To obtain the N 1s core excitations, the integer $n$ has to be set to 4, because the 1s orbital of the oxygen atom is included as well, since it is energetically below the three 1s orbitals of the nitrogen atoms. Accordingly, to simulate the C 1s spectrum of cytosine, $n$ must be set to 8.

SF_STATES

### `SF_STATES`

> **Controls the number of excited spin-flip states to calculate.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n>0$
>     * Number of states to calculate for each irrep or
>     * $[n_{1},n_{2},...]$
>     * Compute
>     * $n_{1}$
>     * states for the first irrep,
>     * $n_{2}$
>     * states for the second irrep, …
> * **Recommendation**: Use this variable to define the number of excited states in the case of a spin-flip calculation. SF-ADC is available for ADC(2)-s, ADC(2)-x and ADC(3).

**Keywords for SS-PCM control in *$pcm***:

### `EQSOLV`

> **Main switch of the self-consistent SS-PCM procedure. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * No self-consistent SS-PCM.
>     * 1
>     * Single SS-PCM calculation (SCF+ADC) with the solvent field found on disk.
>     * $n>$
>     * 1
>     * Do a maximum of
>     * $n$
>     * automatic solvent-field iterations.
> * **Recommendation**: We recommend to use 15 steps max. Typical convergence is 3-5 steps. In difficult cases 6-12. If the solvent-field iteration do not converge in 15 steps, something is wrong. Make sure that a solvent field has been stored on disk by a previous job.

### `EQSTATE`

> **Specifies the state for which the solvent field is to be optimized. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * MP2 ground state (for PTED approach)
>     * 1
>     * energetically lowest excited state
>     * 2
>     * 2nd lowest excited state
>     * …
> * **Recommendation**: Given that only one class of excited states is calculated, the state will be selected according to its energetic position shown in the “Exited-State Summary” of the output file. A maximum of 99 states is stored and can be selected.

### `EQS_CONV`

> **Controls the convergence of the solvent-field iterations by setting the convergence criteria (a mixture of SCF energy and charge-vector). SCF energy criterion computes as $10^{-\rm value}$ $E_{h}$ . INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `SCF_CONVERGENCE`
> * **Options**:
>     * 3
>     * May be sufficient for emission energies
>     * 4
>     * Assured converged total energies (2.7 meV)
>     * 5
>     * Really tight
> * **Recommendation**: Use the default.

### `EQS_REF`

> **Allows to specify which state is to be treated as the reference state in the ADC part of the calculation. Does in contrast to EQSTATE not affect which solvent field is loaded in the SCF step. Only has to be used when singlets are computed in the solvent field of a triplet reference. Note that (converged) singlets states are always counted before triplets, and thus to select $T_{1}$ in a calculation with EE_SINGLETS = 2 this has to be set to 3. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `Same as`
> * **Options**:
>     * 1
>     * First excited state
>     * 2
>     * Second excited state
>     * …
> * **Recommendation**: Only needed when computing singlet states in the solvent field of a triplet reference.
