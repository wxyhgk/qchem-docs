---
title: "7.7.8 State-Targeted Energy Projection"
---

## 7.7.8 State-Targeted Energy Projection

(July 4, 2026)

The state-targeted energy projection (STEP) method[[196]](../bib_references/bib.md#bib189)

supplies a robust and cost-effective alternative to the MOM and IMOM
procedures that were described in Section [7.7.2](ex_OpSing.md).
STEP applies a level shift via a simple modification of the Fock matrix,

<a id="Ch7.E80"></a>
$$
\text{{F}}^{\prime}=\text{{F}}+\eta\text{{SQS}}\;, \tag{7.80}
$$

where **Q** is the matrix representation of the projector onto the user-defined virtual space,
and $\eta$ is a parameter.
The level shift supplied by $\eta\text{{SQS}}$ elevates the energy of virtual orbital $\psi_{a}$ from
$\varepsilon_{a}$ to $\varepsilon_{a}+\eta$ for each unoccupied orbital that is contained in **Q**.
The parameter $\eta$ is chosen to provide the smallest level shift that retains the desired electron configuration
and is defined as follows:

<a id="eq:eta-shift"></a>
$$
\eta=|\varepsilon_{\text{HOMO}}-\varepsilon_{\text{LUMO}}|+\epsilon^{\prime} \tag{7.81}
$$

The HOMO/LUMO gap in Eq. ([7.81](#eq:eta-shift)) pertains to the HOMO and LUMO of the user-defined
configuration; meaning that like the MOM procedure, STEP requires a set of initial-guess molecular orbitals
(usually from a ground state calculation).
The small empirical parameter $\epsilon^{\prime}$ controls the magnitude of the gap between the occupied
and unoccupied orbitals and is settable by the *$rem* variable STEP_EPSILON.
Application of the STEP level shift constrains the solutions of the SCF equations to prevent variational
collapse by forcing an *aufbau* occupation of the desired occupied space at every SCF cycle.

The implementation of STEP in **Q-Chem** takes advantage of the fact that faster convergence is generally
achieved by allowing a dynamic level shift parameter $\eta$ that changes each cycle depending on the new HOMO/LUMO gap,
which differs from the static $\eta$ parameter reported in Ref. [[196]](../bib_references/bib.md#bib189)
.
In the most extreme of cases, if the desired *aufbau* configuration is trivially satisfied without application of a level shift projection,
STEP will set $\eta=0$, which allows for unconstrained occupied/virtual rotations in optimizing the Fock matrix
and thus for rapid convergence to the desired state.
The parameter $\epsilon^{\prime}$ is nonetheless held constant as to allow control over the relative magnitude of the level shift
in cases where one is necessary throughout the optimization.

In more difficult cases, the dynamic level-shift approach (while more efficient) can lead to variational collapse.
If the dynamic level-shift is insufficient, reverting
to the implementation that was originally reported in Ref. [[196]](../bib_references/bib.md#bib189)
 can increase
the robustness of STEP appreciably. In this approach, the level-shift parameter in Eq. ([7.81](#eq:eta-shift))
is always active at every SCF cycle such that $\eta$ is never zero.

STEP can be applied directly as a $\Delta$SCF procedure, wherein spin contamination of the excited state is
often introduced, or within a restricted open-shell framework (Section [7.7.4](ex_ESROKS.md))
in order to directly converge spin-pure excited states. The STEP algorithm is available for
restricted, unrestricted, and restricted open-shell orbitals in **Q-Chem**.

Job control for $\Delta$SCF (R- or U-STEP) and RO-STEP calculations:
After STEP is activated in the *$rem* section,
the remainder of the options for STEP are handled through the *$step* input section.

STEP

### `STEP`

> **Activates the STEP procedure.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not apply the STEP level-shift algorithm.
>     * TRUE
>     * Apply the STEP level-shift algorithm.
> * **Recommendation**: None

### `Epsilon`

> **Scales the size of the occupied/virtual gap imposed by the level-shift by $N$ /100 Hartree. INPUT SECTION: $step**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $N$
> * **Recommendation**: Use the default unless convergence issues arise, in which case a larger value can be used until the desired state is found. Be aware that increasing the occupied/virtual gap in level-shift algorithms slows convergence so it may be advisable to increase SCF_MAX_CYCLES if large shifts are required.

### `Print`

> **Controls the print level for STEP algorithm information. INPUT SECTION: $step**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 0
>     * Do not print any information about STEP between SCF cycles.
>     * 1
>     * Print the level-shift applied at each SCF cycle (R- and U-STEP).
>     * 2
>     * Print the level-shift for both mixed and triplet states at each SCF cycle (RO-STEP).
> * **Recommendation**: Use the default. Level shifts of 0 indicate that an aufbau criterion is sufficient to determine orbital occupation, and shifts $>0$ imply non- aufbau selection of the occupied space.

### `Always_Active`

> **Toggles the original implementation of STEP where the level-shift is static (applied every cycle). INPUT SECTION: $step**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * alpha
>     * Apply a constant level-shift to the alpha spin orbitals.
>     * beta
>     * Apply a constant level-shift to the beta spin orbitals.
>     * both
>     * Apply a constant level-shift to both alpha and beta spin orbitals.
> * **Recommendation**: Use in cases where the dynamic level-shift does not achieve satisfactory results. In the case of U-STEP, the constraint need only be applied to orbitals that must maintain a non- aufbau configuration ( i.e. an alpha-electron promotion requires only the alpha constraint, but two-electron promotions will require both constraints). For RO-STEP this keyword is set to both by default and cannot be turned off. In R-STEP it is only sensible to use both if the desired doubly-excited configuration cannot be found with the dynamic level-shift parameter.

ROKS

### `ROKS`

> **Controls whether ROKS calculation will be performed.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * ROKS is not performed.
>     * TRUE
>     * ROKS will be performed.
> * **Recommendation**: Set to TRUE if ROKS calculation is desired. UNRESTRICTED = FALSE should also be ensured.

???+ example "Example 7.58: Lowest energy $\pi\rightarrow\pi^{\ast}$ transition in acetylene using a $\Delta$ SCF approach with STEP."
    ```qchem
    $comment
       Ground state calculation for reference orbitals
    $end
    
    $molecule
       0 1
       C    0.0000000000   -0.0000000177   -0.6043240964
       C    0.0000000000    0.0000000000    0.6043240820
       H    0.0000000000    0.0000000654   -1.6654864149
       H    0.0000000000    0.0000000198    1.6654865011
    $end
    
    $rem
       METHOD            b3lyp
       BASIS             def2-tzvpd
       SCF_CONVERGENCE   7
    $end
    
    @@@
    
    $comment
       Actual U-STEP calculation
    $end
    
    $molecule
       read
    $end
    
    $rem
       METHOD            b3lyp
       BASIS             def2-tzvpd
       SCF_GUESS         read
       STEP              true
       UNRESTRICTED      true
       SCF_CONVERGENCE   7
    $end
    
    ! default level-shift is 0.1 Hartree
    ! beta orbital promotion means only betas need constrained
    $step
    Epsilon 10
    Always_Active   beta
    $end
    
    $occupied
       1:7
       1:6 8
    $end
    ```

???+ example "Example 7.59: A spin-pure lowest energy $\pi\rightarrow\pi^{\ast}$ transition in acetylene using ROKS with STEP."
    ```qchem
    $comment
       Generates the ground-state reference orbitals
    $end
    
    $molecule
       0 1
       C    0.0000000000   -0.0000000177   -0.6043240964
       C    0.0000000000    0.0000000000    0.6043240820
       H    0.0000000000    0.0000000654   -1.6654864149
       H    0.0000000000    0.0000000198    1.6654865011
    $end
    
    $rem
       METHOD            b3lyp
       BASIS             def2-tzvpd
       SCF_CONVERGENCE   7
    $end
    
    @@@
    
    $comment
       Actual RO-STEP calculation
    $end
    
    $molecule
       read
    $end
    
    $rem
       METHOD            b3lyp
       BASIS             def2-tzvpd
       SCF_ALGORITHM     gdm ! usually recommended with ROKS, but not necessary
       SCF_GUESS         read
       ROKS              true
       STEP              true
       SCF_CONVERGENCE   7
    $end
    
    ! prints all level-shift information
    $step
    Epsilon 10
    Print   2
    $end
    
    $reorder_mo
       1 2 3 4 5 6 7
       1 2 3 4 5 6 7
    $end
    ```
