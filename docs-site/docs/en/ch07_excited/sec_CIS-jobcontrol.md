---
title: "7.2.4 Job Control Options"
---

## 7.2.4 Job Control Options

(July 4, 2026)

Basic job control variables to run CIS and related methods are discussed in Section [7.2.4.1](#sec:CIS-jobcontrol:Basic)
and more advanced options are listed in Section [7.2.4.2](#sec:CIS-jobcontrol:Advanced).

## 7.2.4.1 Basic Job Control

CIS-type jobs are requested by setting the *$rem* variable EXCHANGE =
HF and CORRELATION = NONE, as in a ground-state
Hartree-Fock calculation, but then also specifying a number of excited-state
roots using the *$rem* keyword CIS_N_ROOTS.

**Note: 

For RHF case, $n$ singlets and $n$ triplets will be computed, unless
specified otherwise by using CIS_TRIPLETS and CIS_SINGLETS.
**

### `CIS_N_ROOTS`

> **Sets the number of CI-Singles (CIS) excited state roots to find.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: $n>0$ Looks for
>     * $n$: CIS excited states.
> * **Recommendation**: None

### `CIS_SINGLETS`

> **Solve for singlet excited states in RCIS calculations (ignored for UCIS).**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Solve for singlet states.
>     * `FALSE`: Do not solve for singlet states.
> * **Recommendation**: None

### `CIS_TRIPLETS`

> **Solve for triplet excited states in RCIS calculations (ignored for UCIS).**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Solve for triplet states.
>     * `FALSE`: Do not solve for triplet states.
> * **Recommendation**: None

### `CIS_STATE_DERIV`

> **Sets CIS state for excited state optimizations and vibrational analysis.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Select the
>     * $n$: th state.
> * **Recommendation**: Check to see that the states do not change order during an optimization, due to state crossings.

### `CIS_STATE_MULTIGRAD`

> **Selects the SCF and all CIS/TDDFT states for the gradient evaluations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: Evaluates gradients for all CIS/TDDFT states.
>     * `2`: Evaluates gradients for the SCF and all CIS/TDDFT states.
> * **Recommendation**: The need depends on the specific application. If only one gradient is needed, use CIS_STATE_DERIV instead.

### `RPA`

> **Do an RPA calculation in addition to a CIS or TDDFT/TDA calculation.**
>
> * **Type**: `LOGICAL/INTEGER`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not do an RPA calculation.
>     * `TRUE`: Do an RPA calculation.
>     * `2`: Do an RPA calculation without running CIS or TDDFT/TDA first.
> * **Recommendation**: RPA = 2 is not available for restricted open-shell wave functions.

### `SPIN_FLIP`

> **Selects whether to perform a standard excited state calculation, or a spin-flip calculation. In the most common uses, spin multiplicity should be set to 3 for systems with an even number of electrons, and 4 for systems with an odd number of electrons.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE/FALSE`
> * **Recommendation**: None

### `SPIN_FLIP_XCIS`

> **Controls whether to do a SF-XCIS calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not do an SF-XCIS calculation.
>     * `TRUE`: Do an SF-XCIS calculation (requires ROHF triplet ground state).
> * **Recommendation**: None

### `SFX_AMP_OCC_A`

> **Defines a custom amplitude guess vector in SF-XCIS method.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: builds a guess amplitude with an $\alpha$ -hole in the
>     * $n$: th orbital (requires SFX_AMP_VIR_B).
> * **Recommendation**: Only use when default guess is not satisfactory.

### `SFX_AMP_VIR_B`

> **Defines a user-specified amplitude guess vector in SF-XCIS method.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: builds a guess amplitude with a $\beta$ -particle in the
>     * $n$: th orbital (requires SFX_AMP_OCC_A).
> * **Recommendation**: Only use when default guess is not satisfactory.

### `XCIS`

> **Controls whether to do an XCIS calculation in addition to a CIS calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not do a XCIS calculation.
>     * `TRUE`: Do a XCIS calculation (requires ROHF ground state).
> * **Recommendation**: None

### `SASF_CIS`

> **Controls whether to do an SA-SF-CIS/DFT calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not do a SA-SF-CIS/DFT calculation.
>     * `TRUE`: Do a SA-SF-CIS/DFT calculation.
> * **Recommendation**: The SA-SF method requires a restricted open-shell ground-state calculation.

### `DFTCIS`

> **Controls whether to do a DFT/CIS calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not do a DFT/CIS calculation.
>     * `TRUE`: Do a DFT/CIS calculation.
> * **Recommendation**: None

### `DFTCIS_PARAMS`

> **Selects what variant of DFT/CIS**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do CIS
>     * `1`: Do B3LYP/CIS
>     * `2`: Do CAM-B3LYP/CIS
> * **Recommendation**: Requires DFTCIS to be set to 1 or 2.

## 7.2.4.2 Additional CIS Customization

Additional variables for fine-tuning CIS and related calculations are provided below.

### `N_FROZEN_CORE`

> **Controls the number of frozen core orbitals.**
>
> * **Type**: `INTEGER/STRING`
> * **Default**: `0`
> * **Options**:
>     * `FC`: Frozen core approximation.
>     * $n$: Freeze
>     * $n$: core orbitals.
> * **Recommendation**: There is no computational advantage to using frozen core for CIS, and analytical derivatives are only available when no orbitals are frozen. It is helpful when calculating CIS(D) corrections (see Section 7.8 ).

**Note: 

In correlated calculation, the default setting is N_FROZEN_CORE=FC.
**

### `N_FROZEN_VIRTUAL`

> **Controls the number of frozen virtual orbitals.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Freeze
>     * $n$: virtual orbitals.
> * **Recommendation**: There is no computational advantage to using frozen virtuals for CIS, and analytical derivatives are only available when no orbitals are frozen.

### `MAX_CIS_CYCLES`

> **Maximum number of CIS iterative cycles allowed.**
>
> * **Type**: `INTEGER`
> * **Default**: `30`
> * **Options**:
>     * $n$: User-defined number of cycles.
> * **Recommendation**: Default is usually sufficient.

### `MAX_CIS_SUBSPACE`

> **Maximum number of subspace vectors allowed in the CIS iterations**
>
> * **Type**: `INTEGER`
> * **Default**: `As many as required to converge all roots`
> * **Options**:
>     * $n$: User-defined number of subspace vectors
> * **Recommendation**: The default is usually appropriate, unless a large number of states are requested for a large molecule. The total memory required to store the subspace vectors is bounded above by $2nOV$ , where $O$ and $V$ represent the number of occupied and virtual orbitals, respectively. $n$ can be reduced to save memory, at the cost of a larger number of CIS iterations. Convergence may be impaired if $n$ is not much larger than CIS_N_ROOTS .

### `CIS_CONVERGENCE`

> **CIS is considered converged when error is less than $10^{-\mathrm{CIS\_CONVERGENCE}}$**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n$: Corresponding to $10^{-n}$
> * **Recommendation**: Also controls convergence of the CPSCF equations.

### `CIS_DYNAMIC_MEM`

> **Controls whether to use static or dynamic memory in CIS and TDDFT calculations.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Partly use static memory
>     * `TRUE`: Fully use dynamic memory
> * **Recommendation**: The default control requires static memory ( MEM_STATIC ) sufficient to hold an array whose size grows by $2\times OV\times N_{\text{roots}}$ at each CIS iteration, where $N_{\text{roots}}$ is the number of unconverged roots ( $\leq$ CIS_N_ROOTS ). For a large calculation, one has to specify a large value for MEM_STATIC , which is not recommended (see Chapter 2 ). Therefore, it is recommended to use dynamic memory for large calculations.

### `CIS_RELAXED_DENSITY`

> **Use the relaxed CIS density for attachment/detachment density analysis as well as for for the general excited-state analysis of Section 10.2.12 .**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not use the relaxed CIS density in analysis.
>     * `TRUE`: Use the relaxed CIS density in analysis.
> * **Recommendation**: None

### `CIS_GUESS_DISK`

> **Read the CIS guess from disk (previous calculation).**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Create a new guess.
>     * `TRUE`: Read the guess from disk.
> * **Recommendation**: Requires a guess from previous calculation.

### `CIS_GUESS_DISK_TYPE`

> **Determines the type of guesses to be read from disk**
>
> * **Type**: `INTEGER`
> * **Default**: `Nil`
> * **Options**:
>     * `0`: Read triplets only
>     * `1`: Read triplets and singlets
>     * `2`: Read singlets only
> * **Recommendation**: Must be specified if CIS_GUESS_DISK is TRUE .

### `STS_MOM`

> **Control calculation of the transition moments between excited states in CIS and TDDFT calculations (including spin-flip variants).**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not calculate state-to-state transition moments.
>     * `TRUE`: Do calculate state-to-state transition moments.
> * **Recommendation**: When set to true requests the state-to-state dipole transition moments for all pairs of excited states and for each excited state with the ground state. This is not available for restricted open-shell wave functions.

### `CIS_MOMENTS`

> **Controls calculation of excited-state (CIS or TDDFT) multipole moments.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not calculate excited-state moments.
>     * `TRUE`: Calculate moments for each excited state.
> * **Recommendation**: Set to TRUE if excited-state moments are desired. (This is a trivial additional calculation.) The MULTIPOLE_ORDER controls how many multipole moments are printed. This option is not available for spin-flip methods.
