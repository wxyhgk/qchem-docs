---
title: "7.11.11 Job Control for the RASCI1 Implementation"
---

## 7.11.11 Job Control for the RASCI1 Implementation

(July 4, 2026)

At present the RASCI1 and RASCI2 implementations employ different keywords
(which will be reconciled in a future version). This subsection applies to
RASCI1 (spin adapted algorithm using exact integrals).

The use of the RASCI1 methodology is controlled by setting the *$rem* variable
CORRELATION to RASCI and EXCHANGE should be set to
HF. The RASCI1 implementation is only compatible with the use of
restricted orbitals, *i.e.*, UNRESTRICTED = FALSE.

The minimum input also requires specifying the desired (non-zero) value for
RAS_ROOTS, the number of electrons in the “active” RAS2 space and
the number of orbitals in RAS1 and RAS2 subspaces.

### `RAS_ROOTS`

> **Sets the number of RAS-CI roots to be computed.**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$: $n>0$ Compute
>     * $n$: RAS-CI states
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_ELEC`

> **Sets the number of electrons in RAS2 (active electrons).**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$: User-defined integer, $n>0$
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_ELEC_ALPHA`

> **Sets the number of spin- $\alpha$ electrons in RAS2 (active electrons).**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$: User-defined integer, $n>0$
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_ELEC_BETA`

> **Sets the number of spin- $\beta$ electrons in RAS2 (active electrons).**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$: User-defined integer, $n>0$
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_ACT`

> **Sets the number of orbitals in RAS2 (active orbitals).**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n$: User-defined integer, $n>0$
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_OCC`

> **Sets the number of orbitals in RAS1**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: User-defined integer, $n>0$
> * **Recommendation**: These are the initial doubly occupied orbitals (RAS1) before including $hole$ type of excitations. The RAS1 space starts from the lowest orbital up to , i.e. no frozen orbitals option available yet. Only works with RAS-CI.

### `RAS_DO_HOLE`

> **Controls the presence of hole excitations in the RAS-CI wave function.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Include hole configurations (RAS1 to RAS2 excitations)
>     * `FALSE`: Do not include hole configurations
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_DO_PART`

> **Controls the presence of particle excitations in the RAS-CI wave function.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Include particle configurations (RAS2 to RAS3 excitations)
>     * `FALSE`: Do not include particle configurations
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_AMPL_PRINT`

> **Defines the absolute threshold ( $\times 10^{2}$ ) for the CI amplitudes to be printed.**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $n$: User-defined integer, $n\geq 0$
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_ACT_ORB`

> **Sets the user-selected active orbitals (RAS2 orbitals).**
>
> * **Type**: `INTEGER ARRAY`
> * **Default**: `From`
> * **Options**:
>     * $[i,j,k...]$: The number of orbitals must be equal to the RAS_ACT variable
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_NATORB`

> **Controls the computation of the natural orbital occupancies.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Compute natural orbital occupancies for all states
>     * `FALSE`: Do not compute natural orbital occupancies
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_NATORB_STATE`

> **Saves the natural orbitals of the $i$ th RAS-CI computed state into the .fchk file.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $i$: Saves the natural orbitals for the $i$ th state
> * **Recommendation**: None. Only works with RAS-CI and if GUI = 2.

### `RAS_GUESS_CS`

> **Controls the number of closed shell guess configurations in RAS-CI.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Imposes to start with
>     * $n$: closed shell guesses
> * **Recommendation**: Only relevant for the computation of singlet states. Only works with RAS-CI.

### `RAS_SPIN_MULT`

> **Specifies the spin multiplicity of the roots to be computed**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `0`: Compute any spin multiplicity $2n+1$ User-defined integer, $n\geq 0$
> * **Recommendation**: option is only available for $M_{S}=0$ systems, that is, with the same number of $\alpha$ and $\beta$ electrons.

### `RAS_PT2`

> **Perform second-order perturbative correction to RAS-CI energy**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Compute RASCI(2) energy corrections
>     * `FALSE`: Do not compute RASCI(2) energy corrections
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_PT2_PARTITION`

> **Specifies the partitioning scheme in RASCI(2)**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `2`: Epstein-Nesbet (EN) partitioning
>     * `0`: Do both DK and EN partitionings
> * **Recommendation**: Only for RAS-CI if RAS_PT2 is set to true.

### `RAS_PT2_VSHIFT`

> **Defines the energy level shift ( $\times 10^{3}~{}au$ ) in RASCI(2)**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: User-defined integer
> * **Recommendation**: Only for RAS-CI if RAS_PT2 is set to true.

### `RAS_SRDFT`

> **Perform short-range density functional RAS-CI calculation**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Compute RASCI- $sr$ DFT states and energies
>     * `FALSE`: Do not perform a RASCI- $sr$ DFT calculation
> * **Recommendation**: None. Only works with RAS-CI. RAS_SRDFT_EXC and RAS_SRDFT_COR need to be set.

### `RAS_SRDFT_EXC`

> **Define short-range exchange functional**
>
> * **Type**: `STRING`
> * **Default**: `No default`
> * **Options**:
>     * `NAME`: Use =
>     * `NAME`: , where
>     * `NAME`: is one of the short-range exchange functionals listed in Section 5.3.3
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_SRDFT_COR`

> **Define short-range correlation functional**
>
> * **Type**: `STRING`
> * **Default**: `No default`
> * **Options**:
>     * `NAME`: Use =
>     * `NAME`: , where
>     * `NAME`: is one of the short-range correlation functionals listed in Section 5.3.4
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_OMEGA`

> **Sets the Coulomb range-separation parameter within the RAS-CI- $sr$ DFT method.**
>
> * **Type**: `INTEGER`
> * **Default**: `400`
> * **Options**:
>     * $n$: Corresponding to $\omega=n/1000$ , in units of bohr ${}^{-1}$
> * **Recommendation**: None. Range-separation parameter is typical indicated by $\omega$ or $\mu$ . Only works with RAS-CI.

### `RAS_SRDFT_DAMP`

> **Sets damping factor ( $\alpha<1$ ) in the RAS-CI- $sr$ DFT method.**
>
> * **Type**: `REAL`
> * **Default**: `0.5`
> * **Options**:
>     * $\alpha$: Damping factor $0<\alpha<1$
> * **Recommendation**: Modify in case of convergence issues along the RAS-CI- $sr$ DFT iterations. Only works with RAS-CI

### `RAS_SRDFT_SA_ROOTS`

> **Sets the list of roots used to build the state averaged reference density in RAS-CI- sr DFT.**
>
> * **Type**: `INTEGER ARRAY`
> * **Default**: `All computed states`
> * **Options**:
>     * $[i,j,k\ldots]$: List of states.
> * **Recommendation**: None. Only works with RAS-CI

### `RAS_NFRAG`

> **If $n>0$ activates the excitation analysis in RAS-CI**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Number of fragments to be considered
> * **Recommendation**: Only for RAS-CI. The printed information level is controlled by RAS_PRINT .

### `RAS_NFRAG_ATOMS`

> **Sets the number of atoms in each fragment.**
>
> * **Type**: `INTEGER ARRAY`
> * **Default**: `None`
> * **Options**:
>     * $[i,j,k...]$: The sum of the numbers must be equal to the total number of atoms in the systems
> * **Recommendation**: None. Only works with RAS-CI.

### `RAS_FRAG_SETS`

> **Defines the number of orbitals in each disjoint set to perform orbital localization.**
>
> * **Type**: `INTEGER ARRAY`
> * **Default**: `[NOcc,NAct,NVir]`
> * **Options**:
>     * $[i,j,k...]$: Defines sets of canonical MOs to be localized into
>     * $n$: fragments
> * **Recommendation**: Setting within RAS1, RAS2 and RAS3 spaces alleviates the computational cost of the localization procedure. It might also result in improved fragment orbitals. Only works with RAS-CI.

### `CALC_SOC`

> **Controls whether to calculate the SOC constants for EOM-CC, RAS-CI, TDDFT/TDA and TDDFT.**
>
> * **Type**: `INTEGER/LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not perform the SOC calculation.
>     * `TRUE`: Perform the SOC calculation.
> * **Recommendation**: In addition to TRUE and FALSE , the EOM-CC code has more variants of SOC evaluation; see Section 7.9.21.4 .

### `RAS_SOC_2E`

> **Controls whether to compute two-electron mean-field contribution to RAS-CI SOC.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `FALSE`: Do not compute two-electron mean-field contribution.
>     * `TRUE`: Compute two-electron mean-field contribution.
> * **Recommendation**: None.

### `RAS_SOC_SYM_DENS`

> **Controls whether to perform averaging of $\alpha$ and $\beta$ densities.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not average $\alpha$ and $\beta$ densities .
>     * `TRUE`: Average $\alpha$ and $\beta$ densities.
> * **Recommendation**: None.
