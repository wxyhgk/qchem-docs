---
title: "7.7.10 Δ SCF Driver"
---

## 7.7.10 $\Delta$SCF Driver

(July 4, 2026)

The *$delta_scf* input section can be used to control $\Delta$SCF singlet, doublet, and triplet
excited state calculations with more ease. This section is enabled by setting DELTA_SCF
= TRUE in the *$rem* input section. A basic job demonstrating the defaults
is given in Example 7.7.10.

### `DELTA_SCF`

> **Trigger a $\Delta$ SCF calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: $\Delta$ SCF calculation will not be performed.
>     * `TRUE`: $\Delta$ SCF will be performed.
> * **Recommendation**: Set to TRUE if $\Delta$ SCF calculation is desired.

???+ example "Example 7.61: By default, restricted open-shell SCF calculations are performed for both the singlet, doublet (cation),
and the triplet states associated with the HOMO $\to$ LUMO transition."
    ```qchem
    $comment
      Basic DeltaSCF calculation on formamide.
      HOMO (n) -> LUMO (pi*) transition.
    $end
    
    $molecule
      0   1
      C   0.00096902 0.00000000  0.41970774
      O   1.20026422 0.00000000  0.23240832
      N  -0.93604020 0.00000000 -0.56208780
      H  -0.44521491 0.00000000  1.42281135
      H  -0.64165047 0.00000000 -1.52189668
      H  -1.91364957 0.00000000 -0.34413077
    $end
    
    $rem
      METHOD     wB97X-D
      BASIS      STO-3G
      DELTA_SCF  TRUE
    $end
    ```

Once DELTA_SCF is set to TRUE in the *$rem* section, the keywords to be described
shortly can be used in the *$delta_scf* input section. The desired orbital to excite from (hole state)
and to excite into (particle state) are requested with the keywords **SOMO_1** and **SOMO_2**
(for singly-occupied molecular orbitals), respectively. Doublet (cation, $m_{s}=1/2$) or triplet ($m_{s}=1$)
states can be calculated with either ROSCF or USCF by setting **doublet** or **triplet** to
**restricted** or **unrestricted**. Unrestricted spin-symmetry broken states ($m_{s}=0$, see
Section [7.7.3](sect_OpSing.md)) are requested by setting **singlet** to **unrestricted** whereas setting
**singlet** to **restricted** triggers a spin-pure ROKS calculation (Section [7.7.4](ex_ESROKS.md))
If the triplet state (restricted or unrestricted) is requested in addition to the spin-symmetry broken state,
the code will calculate the approximate energy of the spin-pure singlet state using the approximate spin-
projection method, as detailed in Section [7.7.3](sect_OpSing.md).[[1511]](../bib_references/bib.md#bib1574)

### `Singlet`

> **Carry out either a spin-symmetry broken or restricted-open shell singlet calculation. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `Restricted`
> * **Options**:
>     * `Restricted`: Perform a restricted open-shell singlet (ROKS) SCF calculation.
>     * `Unrestricted`: Perform an unrestricted spin-symmetry broken SCF calculation.
> * **Recommendation**: Consult the literature.

### `Doublet`

> **Carry out a $m_{s}=1/2$ doublet calculation (cation with respect to the closed-shell reference). INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `Restricted`
> * **Options**:
>     * `Restricted`: Perform a restricted open-shell doublet SCF calculation.
>     * `Unrestricted`: Perform an unrestricted doublet SCF calculation.
> * **Recommendation**: Carry out restricted if possible.

### `Triplet`

> **Carry out a $m_{s}=1$ triplet calculation. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `Restricted`
> * **Options**:
>     * `Restricted`: Perform a restricted open-shell triplet SCF calculation.
>     * `Unrestricted`: Perform an unrestricted triplet SCF calculation.
> * **Recommendation**: Carry out restricted if possible.

### `SOMO_1`

> **Specify the occupied orbital to excited from. INPUT SECTION: $delta_scf**
>
> * **Type**: `INTEGER`
> * **Default**: `HOMO`
> * **Options**:
>     * $0<n<$: LUMO Any integer $n\in$ [1, HOMO] is allowed
> * **Recommendation**: Chose the desired orbital to excited from based on prior inspection of the ground state orbitals and the desired state to target.

### `SOMO_2`

> **Specify the virtual orbital to excited into. INPUT SECTION: $delta_scf**
>
> * **Type**: `INTEGER`
> * **Default**: `LUMO`
> * **Options**:
>     * `HOMO`: $<n$ Any integer greater than or equal to the LUMO.
> * **Recommendation**: Chose the desired orbital to excite into based on prior inspection of the ground state orbitals and the desired state to target.

???+ example "Example 7.62: A unrestricted triplet and spin-symmetry broken SCF calculation.
The desired core excitation is targeted via the SOMO_1 and SOMO_2 keywords"
    ```qchem
    $comment
      DeltaSCF calculation on the 1s -> 3s (LUMO + 3) core excited state of Ne.
    $end
    
    $molecule
      0  1
      Ne
    $end
    
    $rem
      METHOD            SCAN
      BASIS             cc-pCVDZ
      INTEGRAL_SYMMETRY FALSE
      DELTA_SCF         TRUE
    $end
    
    $delta_scf
      SOMO_1   1
      SOMO_2   9
      singlet  unrestricted
      triplet  unrestricted
    $end
    ```

???+ example "Example 7.63: A restricted open-shell singlet SCF calculation. Note that when only singlet or triplet are set, only the requested calculation will be performed (as opposed to the default which is both). SOMO_1 and SOMO_2 are once again used to target a specific core excited state ( $1s\to 3s$ ) of hydrogen fluoride.
Compare this example to Example 7.7.5"
    ```qchem
    $comment
      DeltaSCF calculation on the 1s -> 3s (LUMO + 1) core excited
      state of HF. Only a restricted open-shell singlet calculation
      is requested.
    $end
    
    $molecule
      0  1
      F       0.0000  0.0000  0.0000
      H       0.0000  0.0000  0.9168
    $end
    
    $rem
      METHOD            SCAN
      BASIS             aug-cc-pCVTZ
      INTEGRAL_SYMMETRY FALSE
      DELTA_SCF         TRUE
    $end
    
    $delta_scf
      SOMO_1                1
      SOMO_2                7
      singlet               restricted
      singlet_SCF_algorithm SGM
      singlet_SGM_gradient  50
      singlet_SOMO_mixing   false
    $end
    ```

The code will automatically measure three useful quantities:

- •

Overlaps between the ground state SOMOs used as a guess, the singlet (or mixed-state) SOMOs,
and the triplet SOMOs; this serves as a measure to ensure the $\Delta$SCF orbital optimizations
are indeed converging to the desired excited states.
- •

Transition dipole moment between the ground state and the singlet excited state.
- •

Non-orthogonal overlap between the closed-shell ground state and the singlet excited state
determinants (see Section [7.7.4](ex_ESROKS.md) on SOMO mixing in ROKS calculations).

When the SOMO overlaps of the guess are poor (significantly smaller than unity), the $\Delta$SCF calculations
are likely converging to a solution of different character than that provided by the guess. There are two
SCF parameters that can be modified to help your calculation converge to the desired solution: the initial guess
and the SCF algorithm. Aside from the standard guess (converged closed-shell MOs), the doublet cation MOs can be
used as a guess for the singlet or triplet calculation. These can some times be easier to converge and provide an
improved starting point for the SCF procedure. For the singlet calculations, the triplet orbitals themselves
can also serve as a guess. Finally, the natural transition orbitals (NTOs) of a TDDFT calculation (Section 
[7.13.3](sect_NTOs.md)) can also be used as a guess. Note that in this case, you must carry a TDDFT calculation
in a previous (sequential) input in order to save the amplitudes, and set MAX_SCF_CYCLES to 0
and GEN_SCFMAN to TRUE, in order to leave the canonical orbitals untouched and transform
them properly into the NTO basis. The variable **TDDFT_state_guess** controls which TDDFT state
is used as the guess.

### `Singlet_SCF_Guess`

> **Specify the guess used for the singlet (or symmetry-broken) SCF calculation. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `closed_shell`
> * **Options**:
>     * closed_shell, doublet, triplet, tddft_nto
> * **Recommendation**: For certain excitations where there is significant orbital relaxation, such as core excitations, the doublet core ionized state may be easier to converge and serve as a useful starting point.

### `Doublet_SCF_Guess`

> **Specify the guess used for the doublet. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `closed_shell`
> * **Options**:
>     * `closed_shell, tddft_nto`
> * **Recommendation**: The canonical MOs are rotated into the NTO basis and an electron is removed from the hole level for the TDDFT NTO guess.

### `Triplet_SCF_Guess`

> **Specify the guess used for the triplet SCF calculation. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `closed_shell`
> * **Options**:
>     * closed_shell, doublet, tddft_nto
> * **Recommendation**: For certain excitations where there is significant orbital relaxation, such as core excitations, the doublet core ionized state may be easier to converge and serve as a useful starting point.

### `TDDFT_state_guess`

> **Specify the TDDFT state to be used as guess. INPUT SECTION: $delta_scf**
>
> * **Type**: `INT`
> * **Default**: `1, if the TDDFT NTOs were requested as the guess for any calculation`
> * **Options**:
>     * $n>0$: Any integer greater than 1
> * **Recommendation**: Choose according to the TDDFT you’re interested in targeting.

In addition to the guess, the SCF algorithm employed is also crucial for efficiently converging to the desired
SCF solution. The $\Delta$SCF driver has sensible defaults depending on the state desired: GDM
(Section [4.5.7](../ch04_scf/sect_gdm.md)) if the HOMO $\rightarrow{}$ LUMO transition is sought, or the MOM (Section [7.7.2](ex_OpSing.md))
algorithm if a higher excited state is requested. However, in some instances, GDM may be very useful in
converging higher excited states that avoid variational collapse due to symmetry, or else the HOMO
$\rightarrow{}$ LUMO transition may not be the lowest excited state and GDM will collapse to a different
solution. Else, the MOM algorithm may fail to converge. Consult the literature regarding the merits and
shortcomings of different SCF algorithms for excited-state calculations and choose from the variety of
solvers available in **Q-Chem** (Sections [4.5](../ch04_scf/sect_convergence.md), [7.7.2](ex_OpSing.md), [7.7.5](ex_BEDSCF.md), and [7.7.8](ex_ROSTEP.md)).

### `Singlet_SCF_Algorithm`

> **Specify the algorithm used to converge the singlet (or symmetry-broken) SCF calculation. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `GDM if`
> * **Options**:
>     * DIIS, GDM, GDM_LS, MOM, IMOM, STEP, STEP_MOM, SGM, SGM_LS
> * **Recommendation**: DIIS, GDM, and GDM_LS are suitable for the HOMO $\rightarrow$ LUMO transition. If higher excited states are desired use MOM, STEP, SGM, or one of their variants. When using ROKS and encountering large overlaps with the ground state, try using either GDM or SGM in conjunction with Singlet_SOMO_Mixing = false .

### `Doublet_SCF_Algorithm`

> **Specify the algorithm used to converge the doublet SCF calculation. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `GDM if`
> * **Options**:
>     * DIIS, GDM, GDM_LS, MOM, IMOM, STEP, STEP_MOM, SGM, SGM_LS
> * **Recommendation**: DIIS, GDM, and GDM_LS are suitable for the HOMO ionization. If ionization from deeper orbitals are desired, use MOM, STEP, SGM, or one of their variants.

### `Triplet_SCF_Algorithm`

> **Specify the algorithm used to converge the triplet SCF calculation. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `GDM if`
> * **Options**:
>     * DIIS, GDM, GDM_LS, MOM, IMOM, STEP, STEP_MOM, SGM, SGM_LS
> * **Recommendation**: DIIS, GDM, and GDM_LS are suitable for the HOMO $\to$ LUMO transition. If higher excited states are desired use MOM, STEP, SGM, or one of their variants.

Naturally, the convergence thresholds can also be adjusted. The $\Delta$SCF driver sets practical
thresholds depending on the nature of the SCF solver.

### `Singet_SCF_Convergence`

> **Specify the energy convergence threshold for the singlet (or symmetry-broken) SCF calculation. INPUT SECTION: $delta_scf**
>
> * **Type**: `INTEGER`
> * **Default**: `5 if`
> * **Options**:
>     * $n$: Any positive integer.
> * **Recommendation**: Follow defaults.

### `Doublet_SCF_Convergence`

> **Specify the energy convergence threshold for the doublet SCF calculation. INPUT SECTION: $delta_scf**
>
> * **Type**: `INTEGER`
> * **Default**: `5 if`
> * **Options**:
>     * $n$: Any positive integer.
> * **Recommendation**: Follow defaults.

### `Triplet_SCF_Convergence`

> **Specify the energy convergence threshold for the triplet SCF calculation. INPUT SECTION: $delta_scf**
>
> * **Type**: `INTEGER`
> * **Default**: `5 if`
> * **Options**:
>     * $n$: Any positive integer.
> * **Recommendation**: Follow defaults.

When SGM is employed as an SCF solver, the scale factor for the (square) of the orbital gradient can be adjusted .

### `Singlet_SGM_Gradient`

> **Only relevant if Singlet_SCF_Algorithm is set to SGM . See DELTA_GRADIENT_SCALE in Section 7.7.5 . INPUT SECTION: $delta_scf**
>
> * **Type**: `INTEGER`
> * **Default**: `75`
> * **Options**:
>     * $n$: Any integer $n\in[1,100]$ .
> * **Recommendation**: See documentation on DELTA_GRADIENT_SCALE .

### `Doublet_SGM_Gradient`

> **Only relevant if Doublet_SCF_Algorithm is set to SGM . See DELTA_GRADIENT_SCALE in Section 7.7.5 . INPUT SECTION: $delta_scf**
>
> * **Type**: `INTEGER`
> * **Default**: `75`
> * **Options**:
>     * $n$: Any integer between $[1,100]$ .
> * **Recommendation**: See documentation on DELTA_GRADIENT_SCALE .

### `Triplet_SGM_Gradient`

> **Only relevant if Triplet_SCF_Algorithm is set to SGM . See DELTA_GRADIENT_SCALE in Section 7.7.5 . INPUT SECTION: $delta_scf**
>
> * **Type**: `INTEGER`
> * **Default**: `75`
> * **Options**:
>     * $n$: Any integer between $[1,100]$ .
> * **Recommendation**: See documentation on DELTA_GRADIENT_SCALE .

Exclusively for ROKS calculations on singlet states, the mixing between the SOMOs can either be allowed or supressed.

### `Singlet_SOMO_Mixing`

> **Only relevant when singlet is set to true . Refer to ROKS_SS_MIXING in Section 7.7.4 . INPUT SECTION: $delta_scf**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Supressing mixing between SOMOs.
>     * `TRUE`: Allow mixing of SOMOs.
> * **Recommendation**: See documentation on ROKS_SS_MIXING .

The $\Delta$SCF driver allows you to produce cube plots of the SOMOs; these are essential to visually inspect
the character of the SCF solutions found ($n\to\pi^{\ast}$, $\pi\to$ Rydberg, $1s\to\sigma^{\ast}$, etc.) and,
in addition to the SOMO orbital overlaps printed in the output, help you verify that the SCF calculations are
converging to the state you are seeking.

### `Singlet_SOMO_Print`

> **Plots the SOMOs of the singlet (or spin symmetry-broken) state. Make sure you activate the $plots section in the input file. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `Both`
> * **Options**:
>     * `Alpha`: Plots the SOMOs of the alpha orbitals
>     * `Beta`: Plots the SOMOs of the beta orbitals
>     * `Both`: Plots the SOMOs of both the alpha and beta orbitals
> * **Recommendation**: Inspect the orbitals when in doubts about the SCF solution.

### `Doublet_SOMO_Print`

> **Plots the SOMOs of the doublet state. Make sure you activate the $plots section in the input file. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `Both`
> * **Options**:
>     * Alpha Plots the SOMOs of the alpha orbitals: Beta Plots the SOMOs of the beta orbitals Both Plots the SOMOs of both the alpha and beta orbitals
> * **Recommendation**: Inspect the orbitals when in doubts about the SCF solution.

### `Triplet_SOMO_Print`

> **Plots the SOMOs of the triplet state. Make sure you activate the $plots section in the input file. INPUT SECTION: $delta_scf**
>
> * **Type**: `STRING`
> * **Default**: `Both`
> * **Options**:
>     * Alpha Plots the SOMOs of the alpha orbitals: Beta Plots the SOMOs of the beta orbitals Both Plots the SOMOs of both the alpha and beta orbitals
> * **Recommendation**: Inspect the orbitals when in doubts about the SCF solution.

Finally, when describing core excitations for highly symmetrical molecules (*e.g.*, ethylene, N${}_{2}$, or
benzene) where the core orbitals delocalize over the entire molecule, it is necessary to localize
the core orbitals for accurate excitation energies with $\Delta$SCF.[[168]](../bib_references/bib.md#bib162)

This can be accomplished with the following keywords:

### `Localize`

> **Localize the given number of orbitals using the Boys method (refer to Section 10.3.2 ). INPUT SECTION: $delta_scf**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * $n>1$: Any integer $n\in[2,N_{\text{occ}}]$
> * **Recommendation**: Set this variable to the total number of core orbitals to localize (for example, 2 in N ${}_{2}$ or 6 in benzene).

### `Localize_Offset`

> **Sets the offset to begin selecting the number of orbitals to localize, as requested with the localize variable. INPUT SECTION: $delta_scf**
>
> * **Type**: `INTEGER`
> * **Default**: `$\text{HOMO}-n$`
> * **Options**:
>     * $x$: Any integer $x\in[1,\text{HOMO}-n]$
> * **Recommendation**: Consider the number of atoms with orbitals lower in energy than those you are interested on and set this variable to that number. For example, set $x=2$ when attempting to reach the carbon K-edge in CS ${}_{2}$ , due to the two 1s sulfur orbitals.

If you are unable to converge to the desired solution after exploring different SCF guesses and algorithms, as
evidenced by the printed overlaps and by visual inspection, it is suggested you attempt the calculation using a
standard input as described previously in this section (*i.e.*, using sequential inputs and the *$reorder_mo* or
*$occupied* sections) for greater control of the SCF procedure.
