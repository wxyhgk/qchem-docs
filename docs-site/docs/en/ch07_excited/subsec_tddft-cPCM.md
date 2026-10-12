---
title: "7.3.7 TDDFT + PCM for Excitation and Emission Energies in Solution"
---

## 7.3.7 TDDFT + PCM for Excitation and Emission Energies in Solution

(July 4, 2026)

As described in Section [11.2.3](../ch11_env/topic_pcm-em.md), polarizable continuum models (PCMs) are
a simple means of including solvation effects in quantum chemistry calculations
at the level of the dielectric continuum. In this section, the available options
in **Q-Chem** for PCM solvation of TDDFT excited states are discussed. For further details
on the associated keywords, see Sections [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM)
and [11.2.4](../ch11_env/subsec_PCM_job_control.md). For background information on PCM solvation models,
see Ref. [[569]](../bib_references/bib.md#bib580)
.

TDDFT can be combined with PCM in two different formalisms: *linear response* (LR)-
and *state-specific* (SS)-PCM. The LR-PCM approach[[183]](../bib_references/bib.md#bib178)
 employs the transition density
between the ground and excited state and describes the coupling between the excitation
process on the solute and the solvent environment. (For more details, see
Section [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM).) LR-PCM entails only a minor additional
computational cost. However, the use of the transition density limits its applicability
to optically-allowed transitions, whereas the LR-PCM contribution vanishes for
charge-transfer states or singlet to triplet excitations. In **Q-Chem**, TDDFT/LR-PCM
is available for excitation energies, as well as excited-state energy gradients and
Hessians,[[844]](../bib_references/bib.md#bib876)

to allow for geometry optimization and vibrational frequency calculations as described in
Section [7.3.8](subsec_tddft-hessian.md).

The state-specific PCM formalism[[182]](../bib_references/bib.md#bib179)

is difference-density-based
and takes into account the instantaneous response of the solvent to the change in
the solute wave function. This contribution is not included with LR-PCM and is non-zero
even for vanishing transition densities in optically-forbidden transitions.
**Q-Chem** includes SS-PCM both as a perturbative correction[[1530]](../bib_references/bib.md#bib1593)

(ptSS-PCM) as well as in two fully iterative implementations.
Generally, the SS-PCM implementation for TDDFT[[412]](../bib_references/bib.md#bib421)
 follows
closely the ADC($n$)-family of methods described in Section [7.10.11](topic_abs-adc.md).
The ptSS-PCM approach,[[1530]](../bib_references/bib.md#bib1593)
 which is
alternatively called corrected linear-response (cLR-PCM),[[190]](../bib_references/bib.md#bib185)

evaluates a state-specific correction based on the TDDFT excited state density
for each calculated state. This first-order correction excludes the response of
the excited state density to the state-specific reaction field, as to include this response requires
an iterative procedure. The ptSS-PCM approach can be combined with a perturbative approximation to LR-PCM,
ptLR-PCM. For more details, see Section [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM).

To go beyond a first-order correction, one of the iterative implementations
of SS-PCM has to be used. Here, a state-specific Schrödinger equation
is solved self-consistently via iterative optimization of the reaction field
for a specific state. In **Q-Chem**, iterative SS-PCM is implemented[[412]](../bib_references/bib.md#bib421)

either via *external iteration*
(EI-SS-PCM, sometimes called the Improta-Barone-Scalmani-Frisch approach),[[612]](../bib_references/bib.md#bib635)

or else via *internal iteration* (II-SS-PCM,
otherwise known as the *vertical excitation model* or VEM).[[908]](../bib_references/bib.md#bib944)

Whereas ptSS-PCM adds only negligible computational cost, the iterative procedures
increase it by a factor of the required number of iterations.

Excited-state solvation with TDDFT is available in two regimes:
*equilibrium* and *nonequilibrium*
solvation. Nonequilibrium solvation applies to fast processes
(*e.g.*, during vertical excitation or emission), in which the slow nuclear degrees of
freedom of the solvent remain equilibrated with respect to the initial state.
Hence, the solute has to be
modeled for an out-of-equilibrium state of the (implicit) solvent, with only the
fast electronic polarization of the solvent relaxed using the final state’s charge density. This fast
solvent response is governed by the infinite-frequency or “optical” dielectric constant ($\varepsilon_{\infty}$),
often taken to be the square of the solvent’s index of refraction:
$\varepsilon_{\infty}=n_{\text{refr}}^{2}$.[[569]](../bib_references/bib.md#bib580)

Equilibrium solvation, on the other hand,
is appropriate for excited states with a sufficiently long lifetime to allow for complete
relaxation of the solvent. Here, the zero-frequency or static dielectric constant
($\varepsilon_{0}$) is the relevant one, as it includes all polarization mechanisms including both the
fast electronic degrees of freedom and the slow vibrational and orientational degrees of freedom.

## 7.3.7.1 Linear-Response PCM

LR-PCM for TDDFT is activated by setting TDDFT_LR_PCM = TRUE
in the *$pcm* section. The default is a nonequilibrium
calculation employing the optical dielectric constant $\varepsilon_{\infty}$
for the excited state, whereas the static dielectric constant is employed for the
ground-state solvation of the used MOs.
This corresponds to the “full linear response theory” of Ref. [[844]](../bib_references/bib.md#bib876)
.
The value of $\varepsilon_{\infty}$ is specified using the keyword **OpticalDielectric** in the *$solvent* input section,
or can be chosen from a list of preset values as described in Section [11.2.4.3](../ch11_env/subsec_PCM_job_control.md#subsubsec:PCM-solvent-Elst);
an equilibrium calculation in the excited state could be requested by setting **OpticalDielectric** equal to the
value of the solvent’s static dielectric constant.

A perturbative approximation to full
LR-PCM is also available, along with state-specific corrections that are somewhat more
theoretically rigorous,[[569]](../bib_references/bib.md#bib580)
 and have also been implemented for
TDDFT.[[940]](../bib_references/bib.md#bib979)
 This approach is described in further detail below
in Sections [7.3.7.2](#subsubsec:tddft-PCM-iterSS) and [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM).
If the C-PCM model is used, then analytical excited-state energy gradients are available for TDDFT + LR-PCM
and are automatically used if LR-PCM is activated for TDDFT geometry optimization.
As excited-state geometry optimization presupposes equilibration of the solute structure
in the excited state, it is probably appropriate to employ the static dielectric constant for geometry optimization.

The LR-PCM approach considers the solvent response to the electronic transition density
and provides only for optically-allowed transitions a non-vanishing contribution.
Optically-forbidden transitions should be described with a state-specific PCM. This includes
triplet excited states accessed from a singlet ground state and also charge-transfer
states with a vanishing transition density

???+ example "Example 7.14: TDDFT/LR-C-PCM low-lying vertical excitation energy"
    ```qchem
    $molecule
       0 1
       C    0.0   0.0   0.0
       O    0.0   0.0   1.21
    $end
    
    $rem
       EXCHANGE         B3lyp
       CIS_N_ROOTS      10
       CIS_SINGLETS     true
       CIS_TRIPLETS     true
       RPA              TRUE
       BASIS            6-31+G*
       XC_GRID          1
       SOLVENT_METHOD   pcm
    $end
    
    $pcm
       Theory   CPCM
       Method   SWIG
       Solver   Inversion
       Radii    Bondi
    $end
    
    $solvent
       Dielectric         78.39
       OpticalDielectric  1.777849
    $end
    ```

### `TDDFT_LR_PCM`

> **Controls LR-PCM for TDDFT, i.e. , whether or not to add the LR-PCM contributions to the TDDFT eigenvalue problem.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `FALSE`: Do not do LR-PCM (0th-order solvent correction only).
>     * `TRUE`: Perform full LR-PCM.
> * **Recommendation**: Assuming that PCM solvation is turned on for the ground state ( SOLVENT_METHOD = PCM in the $rem section), then disabling LR-PCM by setting = FALSE will afford a “0th-order” solvation correction, in which solvent-polarized MOs and energy levels are used in what is otherwise equivalent to a gas-phase TDDFT calculation. This is the first step in more sophisticated “nonequilibrium” TDDFT + PCM methods, which are discussed in Section 11.2.3.3 . The LR-PCM correction to the excitation energies has some peculiar properties, such as the fact that it vanishes for optically-forbidden states, 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . Link and the state-specific approaches that are discussed in Section 11.2.3.3 are likely preferable.

## 7.3.7.2 State-Specific PCM

The state-specific PCM jobs are controlled with the StateSpecific keyword in the *$pcm* block,
which can be employed to activate either a perturbative or one of the iterative SS-PCMs.

### `StateSpecific`

> **Specifies which the state-specific PCM will be used. INPUT SECTION: $pcm**
>
> * **Type**: `Various`
> * **Default**: `NONE`
> * **Options**:
>     * `Perturb`: Perform ptSS and ptLR for vertical excitations.
>     * `External`: Perform self-consistent EI-SS-PCM to the excited state (for emission).
>     * `Internal`: Perform self-consistent II-SS-PCM to the excited state (for emission or excitation).
> * **Recommendation**: Use for vertical excitation energies ptSS-PCM or in very polar cases the nonequilibrium II-SS-PCM, and equilibrium EI-SS-PCM for emission energies of long-lived excited states.

**1. Perturbative State-Specific (ptSS) PCM**

Perturbative state-specific PCM (ptSS-PCM)[[1530]](../bib_references/bib.md#bib1593)

is activated by setting
**StateSpecific** = **Perturb** in the *$pcm* block. By default, the ptSS correction
is evaluated in the nonequilibrium regime governed by the optical dielectric constant
(**OpticalDielectric** in the *$solvent* block). To force an *equilibrium* ptSS-PCM
calculation, **OpticalDielectric** must be set to the static value,
$\varepsilon_{0}$. To separate the fast and slow contributions to the reaction field,
the charge-separation procedure is chosen with the **ChargeSeparation** keyword.
(**Marcus** is the default, for more information, see Section [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM)
and Ref. [[1530]](../bib_references/bib.md#bib1593)
.)
Alternatively, setting **NonEquilibrium** = **TRUE** results in a default
nonequilibrium ptSS-PCM calculation with **Marcus** charge separation and
deactivated LR-PCM. The ptSS-PCM output provides for each calculated state both a ptSS
and a ptLR-correction. In the nonequilibrium case, the corrected energy corresponds to the
vertical excitation energy. Results are provided both with the unrelaxed density and the relaxed
density, if the latter has been recommended. Results based on the relaxed density are recommended.[[1530]](../bib_references/bib.md#bib1593)

### `NonEquilibrium`

> **Activate nonequilibrium ptSS-PCM. INPUT SECTION: $pcm**
>
> * **Type**: `STRING`
> * **Default**: `False`
> * **Options**:
>     * `TRUE`: Activate nonequilibrium ptSS-PCM.
>     * `FALSE`: Deactivate nonequilibrium ptSS-PCM.
> * **Recommendation**: activates a default ptSS-PCM calculation with Marcus charge separation and no additional LR-PCM.

### `ChargeSeparation`

> **Partition fast and slow charges in solvent equilibrium state INPUT SECTION: $pcm**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * `Marcus`: Do slow/fast charge separation with the Marcus partition.
>     * `Pekar`: Do slow/fast charge separation with the Pekar partition.
> * **Recommendation**: Charge separation is used in conjunction with the StateSpecific keyword in $pcm .

???+ example "Example 7.15: PCM solvation effects on the vertical excitation energies of planar DMABN using the ptSS and ptLR methods."
    ```qchem
    $molecule
       0  1
       C     0.000046   -0.000398    1.904953
       C     1.210027    0.000379    1.186051
       C     1.214640   -0.000065   -0.194515
       C     0.000164   -0.000616   -0.933832
       C    -1.214349   -0.001557   -0.194687
       C    -1.209753   -0.001846    1.185775
       H     2.151949    0.001377    1.722018
       H     2.164371    0.000481   -0.709640
       H    -2.164082   -0.002008   -0.709781
       H    -2.151763   -0.002287    1.721615
       C    -0.000227    0.001061    3.325302
       N    -0.000475    0.002405    4.484321
       N     0.000053   -0.000156   -2.297372
       C    -1.258656    0.001284   -3.036994
       H    -1.041042    0.001615   -4.102376
       H    -1.860897   -0.885647   -2.811117
       H    -1.859247    0.889133   -2.810237
       C     1.258563   -0.000660   -3.037285
       H     1.860651    0.886208   -2.810755
       H     1.859362   -0.888604   -2.811461
       H     1.040664   -0.000097   -4.102609
    $end
    
    $rem
       EXCHANGE              LRC-wPBEPBE
       OMEGA                 260
       BASIS                 6-31G*
       CIS_N_ROOTS           10
       RPA                   2
       CIS_SINGLETS          1
       CIS_TRIPLETS          0
       CIS_RELAXED_DENSITY   TRUE
       SOLVENT_METHOD        PCM
    $end
    
    $pcm
       NonEquilibrium
       Theory                 IEFPCM
       StateSpecific          Perturb
    $end
    
    $solvent
       Dielectric             35.688000       ! Acetonitrile
       OpticalDielectric      1.806874
    $end
    ```

**2. Iterative State-Specific PCM**

The control options for iterative state-specific PCM, as implemented in Ref. [[412]](../bib_references/bib.md#bib421)
,
follow the same setup as for the ADC($n$)-family of methods described in Section [7.10.11](topic_abs-adc.md).
By setting the keyword **EqSolv** to the intended maximum number of iterations,
self-consistent SS-PCM is activated for the reference state indicated in **EqState**.
Iterations are performed until either the maximum number of iterations is reached or
the convergence criteria are satisfied. These criteria are based on the excited-state energy
and the surface charges and are set using **Eqs_Conv**.
During the iterative optimization of the reaction field, states may change
their ordering (root-flipping). Automatic state-following (**EqState_Follow** = **true**)
based on a combination of the electrostatic potential at the surface, the energy changes,
and excited state dipole moments is available. It performs well for separated states
or states of substantially different character (*i.e.* charge-transfer and locally excited states)
but can break down for similar states close to their crossing points.

Note that the excited state energy with iterative state-specific PCMs is only
physically meaningful for the reference state (marked in the output as “EqS-reference”).
For all other states, only energies relative to the self-consistent reference state can be interpreted.
The iterative equilibrium SS-PCM output lists the emission energy to the ground state (only EI-SS-PCM),
as well as transition energies to the other excited states (both EI- and II-SS-PCM)
in zeroth- and first-order (with nonequilibrium ptSS correction).
For nonequilibrium II-SS-PCM, only the vertical excitation energy to the self-consistently
optimized excited state is physically meaningful. For the nonequilibrium II-SS-PCM
and ptSS-PCM calculations, again the **ChargeSeparation** keyword is employed.

### `EqSolv`

> **Main switch of the self-consistent SS-PCM procedure. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: No self-consistent SS-PCM.
>     * `1`: Single SS-PCM calculation (SCF + TDDFT) with the solvent field found on disk. $n>1$ Do a maximum of
>     * $n$: automatic solvent-field iterations.
> * **Recommendation**: We recommend to use 15 steps max. Typical convergence is 3–5 steps. In difficult cases 6–12. If the solvent-field iteration do not converge in 15 steps, something is wrong. For EI-SS-PCM jobs make sure a solvent field was written to disk by a previous job. II-SS-PCM will automatically begin by setting up the solvent field.

### `EqState`

> **Specifies the state for which the solvent field is to be optimized. INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * `1`: energetically lowest excited state
>     * `2`: 2nd lowest excited state $\cdots$
> * **Recommendation**: Given that only one class of excited states is calculated, the state will be selected according to its energetic position shown in the “Exited-State Summary” of the output file.

### `Eqs_Conv`

> **Controls the convergence of the solvent-field iterations by setting the convergence criteria (a mixture of SCF energy (EI-SS-PCM) or excited state energy (II-SS-PCM) and charge-vector). SCF energy criterion computes as $10^{-n}$ $E_{h}$ . INPUT SECTION: $pcm**
>
> * **Type**: `INTEGER`
> * **Default**: `SCF_CONVERGENCE`
> * **Options**:
>     * `3`: May be sufficient for emission energies
>     * `4`: Assured converged total energies (2.7 meV)
>     * `5`: Very tight
> * **Recommendation**: Use the default.

### `EqState_Follow`

> **Controls the automatic state-following based on the electrostatic potential at the surface, excited state energy changes, and excited state dipole moments. INPUT SECTION: $pcm**
>
> * **Type**: `NONE`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Activate automatic state-following
>     * `FALSE`: Deactivate automatic state-following.
> * **Recommendation**: State-Following works well for separated states of different character and can become problematic for nearly degenerate states. It can be advisable to deactivate state-following if similar states are close.

**2. (A) External-Iteration SS-PCM**

EI-SS-PCM, otherwise known as Improta-Barone-Scalmani-Frisch PCM,[[612]](../bib_references/bib.md#bib635)

is activated by setting **StateSpecific** = **External** in the *$pcm* section. EI-SS-PCM
iterates over both the SCF and TDDFT calculation by returning the excited-state reaction field
into a frozen-Reaction-Field (fRF) SCF. Prior to this, the reaction field has to be set up in a separate
job by setting **StateSpecific** = External without adding the keyword **EqSolv**.
In the following iterative job, the reference state (**EqState**) can then be chosen freely
among the states calculated prior, and iterations can be restarted in the same way
(*e.g.*, to manually correct the automatic state-following).
The EI-SS-PCM convergence is judged based on the change in the surface charge vector
and the fRF-SCF energy, in order to converge all excited states to the same level.
Additionally, the self-ptSS term indicates convergence though it is not used as an
actual convergence criterion.

EI-SS-PCM is always performed as equilibrium solvation employing the full dielectric response
of the solvent based on the static dielectric constant (**Dielectric**). Non-equilibrium
emission and transition energies are calculated in first order at the ptSS-PCM level. EI-SS-PCM
provides the correct solution of the state-specific Schrödinger equation without
contamination from the ground state MOs, and hence, should be used whenever the excited state
is to be treated on equal footing with the ground state.

???+ example "Example 7.7.16: TDDFT with External Iteration SS-PCM for nitrate in acetonitrile."
    ```qchem
    $molecule
       -1 1
       N    -0.068642000000     -0.600693000000     -0.723424000000
       O     0.349666000000      0.711166000000      1.187490000000
       O    -0.948593000000      0.200668000000     -0.956940000000
       O     0.659040000000     -0.386002000000      0.402650000000
    $end
    
    $rem
       jobtype    ¯¯         sp
       method ¯¯             PBE0
       basis  ¯¯¯           3-21g
    point_group_symmetry False
       cis_n_roots             2           ! Number of excited states
       cis_singlets            true
       cis_triplets            false
       rpa                     false       ! Tamm-Dancoff approximation
       cis_moments             true        ! Excited state multipole moments
       cis_relaxed_density     true        ! Excited state density relaxation
       solvent_method        ¯ pcm
    $end
    
    $pcm
       StateSpecific           External    ! Keyword for External Iteration SS-PCM
       LinearResponse          false       ! Switch of LR-PCM
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       jobtype ¯¯             sp
       method ¯¯             PBE0
       basis ¯¯¯             3-21g
    point_group_symmetry False
       cis_n_roots             2
       cis_singlets            true
       cis_triplets            false
       rpa                     false
       cis_moments             true
       cis_relaxed_density     true
       solvent_method          pcm
    $end
    
    $pcm
       StateSpecific           External
       Eqsolv                  15          ! Max. Number of iterations
       Eqstate                 1           ! Ref. State to be equilibrated
       Eqs_Conv                4           ! Conv. criterion for SCF energy and surface charges
       EqState_Follow          true        ! State Following to remain on the same Ref. State
       LinearResponse          false
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    ```

**2. (B) Internal-Iteration SS-PCM**

II-SS-PCM, otherwise known as the vertical excitation model (VEM),[[908]](../bib_references/bib.md#bib944)

is activated by setting the keyword **StateSpecific** = **Internal**.
II-SS-PCM retains the same ground state wave-function in the iterations
but exchanges the ground and excited-state reaction field during the TDDFT calculation.
This leads to slight contamination of the excited state by the ground state MOs.
II-SS-PCM is available both for equilibrium (adiabatic excitation model, AEM) and nonequilibrium (VEM), and
with either the full matrix (f) or only the diagonal elements (d) of the excited state
reaction field, as described in Ref. [[908]](../bib_references/bib.md#bib944)
. To choose the exact model,
the keyword **InternalIteration** is set to
**VEM(d)**, **VEM(f)**, **AEM(d)**, or **AEM(f)**.
In contrast to EI-SS-PCM, the II-SS-PCM approach automatically begins with a setup calculation to
produce the initial excited state reaction field for the iterations, which then cannot be restarted.
To still allow besides the automatic also for manual state following, a specific sequence of states
can be listed by appending the chosen method in **InternalIteration** with -state.
The sequence is terminated by a zero, after which state-following is re-engaged. For II-SS-PCM,
convergence is judged on the reference state energy and the surface charge vector.

A nonequilibrium II-SS-PCM or VEM calculation corresponds to an iterative version of
nonequilibrium ptSS-PCM for vertical excitation energies. Here, also the response of the
density to the fast excited state reaction field is included. Hence, the VEM result
for the converged reference state (indicated by “EqS-reference” in the output)
corresponds to the vertical excitation energy, while the other states have no physical meaning.

Equilibrium II-SS-PCM or AEM, on the other hand, provides the excited reference state energy
and transition energies to other excited states. However, emission energies from the reference
state to the ground state are adiabatic because the ground state orbitals are not affected by the
excited state reaction field. To obtain vertical emission energies, a further
fRF ground state calculation has to be performed by setting **RF_ptSS_Save** = **true**
and loading the reaction field in a consecutive job by setting **RF_ptSS_Read** = **true**.
See Section [7.7.9](sect_ROKS_neq-PCM.md) for further information.

### `InternalIteration`

> **Controls the used internal iteration SS-PCM model. Additionally, a sequence of state to be followed can be appended after adding -state . INPUT SECTION: $pcm**
>
> * **Type**: `NONE`
> * **Default**: `NONE`
> * **Options**:
>     * `VEM(f)`: Activate nonequilibrium II-SS-PCM (VEM) with the full matrix contribution.
>     * `VEM(d)`: Activate nonequilibrium II-SS-PCM (VEM) with only diagonal matrix elements.
>     * `AEM(f)`: Activate equilibrium II-SS-PCM (AEM) with the full matrix contribution.
>     * `AEM(d)`: Activate equilibrium II-SS-PCM (AEM) with only diagonal matrix elements.
>     * `…-state x y z … 0`: Specify sequence of states to be followed (terminate with 0).
> * **Recommendation**: The nonequilibrium versions (VEM) provide vertical excitation energies, while in equilibrium (AEM) the initial state for emission energies is prepared. By attaching the -state ending an explicit sequence of states to be followed can be provided. After terminating with a zero, state-following will be re-engaged.

???+ example "Example 7.7.17: TDDFT with Internal Iteration SS-PCM and the additional ground state calculation for
vertical emission energies of nitrate in acetonitrile."
    ```qchem
    $molecule
       -1 1
       N    -0.068642000000     -0.600693000000     -0.723424000000
       O     0.349666000000      0.711166000000      1.187490000000
       O    -0.948593000000      0.200668000000     -0.956940000000
       O     0.659040000000     -0.386002000000      0.402650000000
    $end
    
    $rem
       jobtype ¯¯             sp
       method ¯¯             PBE0
       basis ¯¯¯             3-21g
    point_group_symmetry False
       cis_n_roots             4           ! Number of excited states
       cis_singlets            true
       cis_triplets            false
       rpa                     false       ! Tamm-Dancoff approximation
       cis_moments             true        ! Excited state multipole moments
       cis_relaxed_density     true        ! Excited state density relaxation
       solvent_method          pcm
    $end
    
    $pcm
       StateSpecific           Internal    ! Keyword for Internal Iteration SS-PCM
       ChargeSeparation        MARCUS      ! Keyword for the charge separation
       InternalIteration       AEM(f)      ! Procedure (VEM(f), VEM(d), AEM(f), or AEM(d)) + state sequence (add e.g.: -state 1 3 1 0)
       Eqsolv                  10          ! Max. Number of iterations
       Eqstate                 1           ! Ref. State to be equilibrated
       Eqs_Conv                4           ! Conv. criterion for SCF energy and surface charges
       EqState_Follow          true        ! State Following to remain on the same Ref. State
       theory                  iefpcm      ! PCM Theory (else CPCM)
       rf_ptss_save            true        ! Save the eq. reaction field of Ref. State
       LinearResponse          false       ! Switch of LR-PCM
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       jobtype                 sp
       method ¯¯             PBE0
       basis                   3-21g
    point_group_symmetry False
       solvent_method          pcm
    $end
    
    $pcm
       theory                  iefpcm
       rf_ptss_read            true        ! Flag to read the reaction field and do RF-ptSS calc
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    
    ```
