---
title: "7.6.4 Job Control"
---

## 7.6.4 Job Control

(July 4, 2026)

NOCIS, 1C-NOCIS, and STEX run as subroutines in GEN_SCFMAN. Thus, for all calculations, you must set GEN_SCFMAN = TRUE. It is also highly recommended that you run an open-shell ground state calculation prior to running your NOCIS/STEX/1C-NOCIS calculations, which are all restricted.

NOCIS

### `NOCIS`

> **Requests a NOCIS/STEX/1C-NOCIS/EA-TDDFT calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not run these methods.
>     * TRUE
>     * Run one of these methods, options controlled in
>     * $nocis
>     * .
> * **Recommendation**: None

Options below this line are set within the *$nocis* section.

### `STEX`

> **Run a STEX calculation INPUT SECTION: $nocis**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * The presence of this keyword will activate STEX.
> * **Recommendation**: None

### `ONE_CENTER`

> **Run a 1C-NOCIS calculation INPUT SECTION: $nocis**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * False
>     * Run a NOCIS calculation.
>     * True
>     * Run a 1C-NOCIS calculation.
> * **Recommendation**: None

### `ORB_OFFSET`

> **Determines the starting orbital for a NOCIS/STEX/1C-NOCIS/EA-TDDFT calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Positive integer
> * **Recommendation**: Set according to the first orbital of interest in the system in question. For example, this would be set to 0 for the O K-edge in CO ${}_{2}$ because the two O 1s orbitals lie below the C 1s, so for the C K-edge this would be set to 2.

### `NUM_REF`

> **Sets the number of reference orbitals in a NOCIS/STEX/1C-NOCIS/EA-TDDFT calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Positive integer
> * **Recommendation**: Set according to the number of consecutive orbitals of interest for the calculation. For example, for the oxygen K-edge in CO ${}_{2}$ , the number of references would be 2 (two O 1s orbitals), whereas for the carbon K-edge it would be 1 (one C 1s).

Options below this line are exclusive to 1C-NOCIS calculations for 2eOS references.

### `OS_IS`

> **Triggers a 1C-NOCIS calculation with an M ${}_{S}$ = 0 open-shell initial state (IS). INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `ROKS`
> * **Options**:
>     * CIS
>     * Employ a CIS excited-state wave function transformed into the NTO basis as the IS
>     * ROKS
>     * Employ a ROKS- or ROHF-optimized wave function (singlets or triplets) as the IS
>     * CIS_ROKS
>     * Use CIS NTOs as a guess for an RO calculation on the IS.
> * **Recommendation**: Use CIS when targeting a well-defined initial state. Else use ROSCF. Note that, if the CIS_ROKS option is used, the previous excited state job can employ TDDFT instead of CIS to provide a better guess.

### `OS_IS_CIS_STATE`

> **When using CIS or CIS_ROKS for OS_IS , specifies which CIS state to target. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $n$
>     * Positive integer
> * **Recommendation**: Set according to the desired CIS state.

### `OS_IS_OCC_VALENCE`

> **When using ROKS for OS_IS , specifies which occupied orbital to excite from. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `HOMO`
> * **Options**:
>     * $n$
>     * Positive integer
> * **Recommendation**: Set according to the desired ROKS state. This is a 0-indexed variable (the lowest orbital has index 0).

### `OS_IS_VIR_VALENCE`

> **When using ROKS for OS_IS , specifies which virtual orbital to excite into. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `LUMO`
> * **Options**:
>     * $n$
>     * Positive integer
> * **Recommendation**: Set according to the desired ROKS state. This is a 0-indexed variable (the lowest orbital has index 0).

### `OS_IS_SCF_ALGORITHM`

> **When using ROKS for OS_IS , specifies the SCF algorithm for convergence of the IS. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `GDM when`
> * **Options**:
>     * DIIS
>     * GDM
>     * GDM_LS
>     * SGM
>     * SGM_LS
> * **Recommendation**: Use defaults.

### `OS_IS_DSCF_ALGORITHM`

> **When using ROKS for OS_IS , specifies the SCF algorithm for convergence of the IS. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * MOM
>     * IMOM
>     * STEP
>     * STEP_MOM
> * **Recommendation**: When using DIIS, MOM or IMOM may be necessary to target higher valence excited states.

### `OS_IS_SCF_CONVERGENCE`

> **When using ROKS or CIS_ROKS for OS_IS , specifies the SCF convergence for the IS ROSCF calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `7 for SGM- and GDM-based solvers`
> * **Options**:
>     * $n$
>     * Positive integer
> * **Recommendation**: Modify as needed for convergence, but thresholds below 5 for descent-based methods (GDM, SGM), and 7 for others may provide unsufficiently-converged orbitals.

### `OS_IS_SGM_GRADIENT`

> **When using SGM for OS_IS_SCF_ALGORITHM , specifies the DELTA_GRADIENT_SCALE for the IS ROSCF calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `75 when using SGM as the SCF solver for the initial valence state`
> * **Options**:
>     * $n$
>     * Positive integer below 100
> * **Recommendation**: See DELTA_GRADIENT_SCALE $rem variable. If ROKS_IS_SS_MIXING is set to FALSE, try the default. Otherwise, a value of around 10 might be required. If its converging to the wrong state, try decreasing.

### `OS_IS_SS_MIXING`

> **Controls whether to allow mixing between the singly-occupied orbitals during the ROKS procedure. INPUT SECTION: $nocis**
>
> * **Type**: `BOOL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Supress coupling.
>     * TRUE
>     * Allow coupling.
> * **Recommendation**: See ROKS_SS_MIXING $rem variable. Supressing coupling is useful when the resuling states are difficult to converge and / or overlap significantly with the ground state, and seems to be harmless otherwise. Certain $\pi\longrightarrow{}\pi^{*}$ excitated states are particularly susceptible to this (Example 7.7.4 ). Only works with descent-based solvers (GDM or SGM).

### `OS_FS_REFERENCE_ORB`

> **Choice of reference orbitals for the final states (FS) INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `ROKS_2EOS for singlet valence excited states`
> * **Options**:
>     * OC_NOCIS
>     * Uses ROSCF doublet core ion orbitals, rotated into the closed-shell
>     * 1C-NOCIS NTO basis
>     * QUARTET_ION
>     * Uses the ROSCF quartet core ion orbitals
>     * ROKS_2EOS
>     * Uses the
>     * $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$
>     * orbitals optimized via ROKS.
> * **Recommendation**: Use defaults.

### `OS_FS_NS_REFERENCE`

> **Specifies a single common reference to use for all core orbitals when NUM_REF > 1. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Non-negative integer
> * **Recommendation**: Experimental feature. When simulating, say, the M ${}_{2,\;3}$ -edge of an iron compound, the 3s core hole reference may be useful - while it doesn’t optimize each individual 3p core hole individually, it partially captures core hole orbital realxation and provides an unbiased reference for the set of three 3p orbitals. Note no spin-orbit coupling is implemented at the moment for these calculations.

### `OS_FS_D_ION_SCF_ALGORITHM`

> **Specifies the SCF algorithm for convergence of the doublet core ion ROSCF calculation. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `DIIS`
> * **Options**:
>     * DIIS
>     * SGM
>     * SGM_LS
> * **Recommendation**: Use default. If convergence is not possible, try SGM.

### `OS_FS_D_ION_DSCF_ALGORITHM`

> **Specifies the SCF algorithm for convergence of the doublet core ion ROSCF calculation. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `MOM when`
> * **Options**:
>     * MOM
>     * IMOM
>     * STEP
>     * STEP_MOM
> * **Recommendation**: None.

### `OS_FS_D_ION_SCF_CONVERGENCE`

> **Specifies the SCF convergence for the doublet core ion ROSCF calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $ijk...$
>     * Positive integer. i, j, k, … relate to reference 1, 2, 3, …
> * **Recommendation**: Setting this $rem variable to 0 skips the doublet core ion calculations and instead uses the valence excited state orbitals as a guess for either the quartet core ion ROHF calculation or $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS calculations. When that fails to converge the reference orbitals, attempt to use doublet core ion orbitals as a guess. Thresholds below 5 for SGM-Based solvers, or 7 for DIIS / MOM may provide insufficiently converged orbitals. This may not be as critical (and perhaps necessar) if just using them as a guess for subsequent calculations. Note DFT orbitals may serve as better guess - specify the desired functional via the ENV_METHOD $rem variable. When using closed-shell 1C-NOCIS reference orbitals for the 1C-NOCIS 2eOS calculation, proper convergence and not DFT must be used.

### `OS_FS_D_ION_SGM_GRADIENT`

> **When using SGM for OS_FS_D_ION_SCF_ALGORITHM, specifies the DELTA_GRADIENT_SCALE for the doublet core ion ROSCF calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Positive integer
> * **Recommendation**: Anecdotically, a value of 1 - 10 seems to work well for core ions. If the ROSCF calculation is not converging, try increasing.

### `OS_FS_Q_ION_SCF_ALGORITHM`

> **Specifies the SCF algorithm for convergence of the quartet core ion ROSCF calculation. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `DIIS`
> * **Options**:
>     * DIIS
>     * SGM
>     * SGM_LS
> * **Recommendation**: Use DIIS when possible. For problematic cases, use SGM.

### `OS_FS_Q_ION_DSCF_ALGORITHM`

> **Specifies the SCF algorithm for convergence of the quartet core ion ROSCF calculation. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `MOM when`
> * **Options**:
>     * MOM
>     * IMOM
>     * STEP
>     * STEP_MOM
> * **Recommendation**: For efficiency, attempt using MOM, IMOM, STEP, or STEP_MOM first (requires DIIS for OS_FS_Q_ION_SCF_ALGORITHM ). If the SCF procedure fails to converge or converges to the wrong state, do not set this rem variable and attempt using SGM in OS_FS_Q_ION_SCF_ALGORITHM .

### `OS_FS_Q_ION_SCF_CONVERGENCE`

> **Specifies the SCF convergence for the quartet core ion ROSCF calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `6 (for each reference) for SGM-based solvers`
> * **Options**:
>     * $ijk...$
>     * Positive integer. i, j, k, … relate to reference 1, 2, 3, …
> * **Recommendation**: Modify as needed for convergence, but thresholds below 5 for SGM-based methods, and 7 for others may provide unsufficiently-converged orbitals.

### `OS_FS_Q_ION_SGM_GRADIENT`

> **When using SGM for OS_FS_Q_ION_SCF_ALGORITHM, specifies the DELTA_GRADIENT_SCALE for the quartet core ion ROSCF calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Positive integer
> * **Recommendation**: Anecdotically, a value of 1 - 10 seems to work well for core ions. If the ROSCF calculation is not converging, try increasing.

### `OS_FS_2EOS_SCF_ALGORITHM`

> **Specifies the SCF algorithm for convergence of the $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS calculation. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `SGM`
> * **Options**:
>     * DIIS
>     * SGM
>     * SGM_LS
> * **Recommendation**: Use DIIS for very simple (small) molecules and low-lying valence excited states. Else, use SGM.

### `OS_FS_2EOS_DSCF_ALGORITHM`

> **Specifies the SCF algorithm for convergence of the $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS calculation. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `MOM when`
> * **Options**:
>     * MOM
>     * IMOM
>     * STEP
>     * STEP_MOM
> * **Recommendation**: Use defaults.

### `OS_FS_2EOS_SCF_CONVERGENCE`

> **Specifies the SCF convergence for the $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `6 (for each reference) for SGM-based solvers`
> * **Options**:
>     * $ijk...$
>     * Positive integer. i, j, k, … relate to reference 1, 2, 3, …
> * **Recommendation**: Modify as needed for convergence, but thresholds below 5 for SGM-based methods, and 7 for others may provide unsufficiently-converged orbitals.

### `OS_FS_2EOS_SGM_GRADIENT`

> **When using SGM for OS_FS_2EOS_SCF_ALGORITHM, specifies the DELTA_GRADIENT_SCALE for the $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ core- excited ROKS calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `75 when`
> * **Options**:
>     * $n$
>     * Positive integer below 100
> * **Recommendation**: See DELTA_GRADIENT_SCALE $rem variable. If ROKS_FS_2EOS_SS_MIXING is set to FALSE, try the default. Otherwise, a value of around 1 - 10 might be required. If its converging to the wrong state, try decreasing.

### `OS_FS_2EOS_SS_MIXING`

> **Controls whether to allow mixing between the singly-occupied orbitals during the ROKS procedure. INPUT SECTION: $nocis**
>
> * **Type**: `BOOL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Supress coupling.
>     * TRUE
>     * Allow coupling.
> * **Recommendation**: See ROKS_SS_MIXING $rem variable. Supressing coupling is useful when the resuling states are difficult to converge and / or overlap significantly with the ground state, and seems to be harmless otherwise. 1s $\longrightarrow{}$ 3s excited states, for example, are particularly susceptible to this phenomena. Only works with descent-based solvers (GDM or SGM).

???+ example "Example 7.40: NOCIS for the nitrogen K-edge of N ${}_{2}$"
    ```qchem
    $molecule
       0 1
       N     0.000000     0.000000     0.564990
       N     0.000000     0.000000    -0.564990
    $end
    
    $rem
       METHOD           hf
       BASIS            sto-3g
       UNRESTRICTED     false
       GEN_SCFMAN       true
       NOCIS            true
       THRESH           14
       MAX_SCF_CYCLES   500
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    ! the default behavior is NOCIS
    $nocis
       ORB_OFFSET       0
       NUM_REF          2
    $end
    ```

???+ example "Example 7.41: STEX for the carbon K-edge of CN"
    ```qchem
    $molecule
       0 2
       C  0.0000000   0.0000000  -0.6258140
       N  0.0000000   0.0000000   0.5364120
    $end
    
    $rem
       METHOD            hf
       BASIS             sto-3g
       SCF_GUESS         core
       SCF_ALGORITHM     diis_gdm
       MAX_SCF_CYCLES    5000
       THRESH            14
       SCF_CONVERGENCE   10
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
       METHOD            hf
       BASIS             sto-3g
       SCF_GUESS         read
       UNRESTRICTED      false
       SCF_ALGORITHM     diis_gdm
       GEN_SCFMAN        true
       NOCIS             true
       MAX_SCF_CYCLES    5000
       THRESH            14
       SCF_CONVERGENCE   10
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    $nocis
       STEX
       ORB_OFFSET        1
       NUM_REF           1
    $end
    ```

???+ example "Example 7.42: 1C-NOCIS for the oxygen K-edge of O ${}_{2}$"
    ```qchem
    $molecule
       0 3
       O    0.0000000   0.0000000    0.6021380
       O    0.0000000   0.0000000   -0.6021380
    $end
    
    $rem
       METHOD           hf
       BASIS            sto-3g
       GEN_SCFMAN       true
       THRESH           14
       MAX_SCF_CYCLES   500
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
       UNRESTRICTED     false
       SCF_GUESS        read
       METHOD           hf
       BASIS            sto-3g
       GEN_SCFMAN       true
       NOCIS            true
       THRESH           14
       MAX_SCF_CYCLES   500
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $nocis
       ONE_CENTER
       ORB_OFFSET       0
       NUM_REF          2
    $end
    ```

???+ example "Example 7.43: 1C-NOCIS 2eOS for the oxygen K-edge of the first singlet excited state of water. A CIS calculation on is used to provide a guess for the ROKS optimization of the target valence state."
    ```qchem
    $comment
      CIS calculation on water to generate the target initial state.
    $end
    
    $molecule
      0   1
      O   0.0000      0.0000      0.1173
      H   0.0000      0.7572     -0.4692
      H   0.0000     -0.7572     -0.4692
    $end
    
    $rem
      METHOD               HF
      UNRESTRICTED         FALSE
      BASIS                DEF2-SVP
      SYMMETRY             FALSE
      SYM_IGNORE           TRUE
      GEN_SCFMAN           TRUE
      SCF_ALGORITHM        DIIS_GDM
      CIS_N_ROOTS          3
      CIS_SINGLETS         TRUE
      CIS_TRIPLETS         FALSE
      REL_X2C              TRUE
      THRESH               14
      MEM_TOTAL            1000
      MEM_STATIC           100
      NTO_PAIRS            3
    $end
    
    @@@
    
    $comment
      1C-NOCIS 2eOS singlet calculation.
    $end
    
    $molecule
      read
    $end
    
    $rem
      METHOD               HF
      UNRESTRICTED         FALSE
      BASIS                DEF2-SVP
      SYMMETRY             FALSE
      SYM_IGNORE           TRUE
      GEN_SCFMAN           TRUE
      SCF_GUESS            READ
      MAX_SCF_CYCLES       0
      REL_X2C              TRUE
      NOCIS                1
      THRESH               14
      MEM_TOTAL            1000
      MEM_STATIC           100
    $end
    
    $nocis
      SINGLETS
      ONE_CENTER
      OS_IS                CIS ! Use CIS NTOs for the valence excited state (IS)
    $end
    ```

???+ example "Example 7.44: 1C-NOCIS 2eOS for the nitrogen K-edge of the first singlet excited state of pyrazine. The canonical orbitals are used as a guess for the ROKS optimization of the target valence state."
    ```qchem
    $comment
      1C-NOCIS 2eOS singlet calculation on pyrazine for the lowest excited state.
    $end
    
    $molecule
      0   1
      N   0.0000      0.0000      1.3814
      N   0.0000      0.0000     -1.3814
      C   0.0000      1.1192      0.6914
      C   0.0000     -1.1192      0.6914
      C   0.0000     -1.1192     -0.6914
      C   0.0000      1.1192     -0.6914
      H   0.0000      2.0412      1.2411
      H   0.0000     -2.0412      1.2411
      H   0.0000     -2.0412     -1.2411
      H   0.0000      2.0412     -1.2411
    $end
    
    $rem
      METHOD               HF
      UNRESTRICTED         FALSE
      BASIS                STO-3G
      SYMMETRY             FALSE
      SYM_IGNORE           TRUE
      GEN_SCFMAN           TRUE
      REL_X2C              TRUE
      NOCIS                1
      THRESH               14
      MEM_TOTAL            1000
      MEM_STATIC           100
    $end
    
    $nocis
      SINGLETS
      ONE_CENTER
      LOCALIZE_ORBITALS              2         ! Localize the two nitrogen 1s orbitals
      NUM_REF                        2         ! Two nitrogen atoms
      OS_IS                          ROKS      ! Use ROKS for the valence excited state (IS)
    $end
    ```

???+ example "Example 7.45: 1C-NOCIS 2eOS for the oxygen K-edge of the triplet ground state of molecular oxygen. The default reference orbitals for triplets are the quartet core ion orbtials. Note it begins from a closed-shell job."
    ```qchem
    $comment
      1C-NOCIS 2eOS triplet calculation. Note we begin from a closed-shell reference.
    $end
    
    $molecule
      0   1
      O   0.0000      0.0000      0.60375
      O   0.0000      0.0000     -0.60375
    $end
    
    $rem
      METHOD               HF
      UNRESTRICTED         FALSE
      BASIS                STO-3G
      SYMMETRY             FALSE
      SYM_IGNORE           TRUE
      GEN_SCFMAN           TRUE
      SCF_ALGORITHM        DIIS_GDM
      REL_X2C              TRUE
      NOCIS                1
      THRESH               14
      MEM_TOTAL            1000
      MEM_STATIC           100
    $end
    
    $nocis
      TRIPLETS                            ! Activate a triplet 2eOS reference
      ONE_CENTER                          ! One-center approximation
      LOCALIZE_ORBITALS              2    ! Localize 2 orbitals
      NUM_REF                        2    ! Two oxygen atoms
      OS_IS                          ROKS ! Use ROHF to converge the valence excited state (IS)
      OS_FS_Q_ION_SCF_CONVERGENCE    88   ! Convergence of the quartet core ion orbitals
    $end
    ```
