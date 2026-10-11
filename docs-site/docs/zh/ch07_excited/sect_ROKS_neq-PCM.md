---
title: "7.7.9 Non-Equilibrium Solvation for ROKS and Δ SCF"
---

## 7.7.9 Non-Equilibrium Solvation for ROKS and $\Delta$SCF

(July 4, 2026)

Both $\Delta$SCF calculations (*e.g.*, based on MOM) and ROKS calculations can be performed with
continuum solvation effects modeled by a polarizable continuum model (PCM).
(The solvation model itself is described in Section [11.2.3](../ch11_env/topic_pcm-em.md).) As for the ground state,
the self-consistent PCM treatment along the SCF procedure provides *equilibrium*
solvation of the calculated excited state (set SOLVENT_METHOD = PCM
and include the *$pcm* block). During equilibrium solvation, both slow (nuclear)
and fast (electronic) solvent degrees of freedom are relaxed (governed by
**Dielectric** in the *$solvent* block), as is appropriate for long-lived states.
However, fast vertical excitation or emission occurs on a shorter timescale,
requiring the relaxation of only the fast electronic solvent polarization
(governed by **Dielectric_Infi**, see Section [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM)).
In **Q-Chem**, such *nonequilibrium* solvation effects can be included
to first order with a perturbative state-specific (ptSS) correction.[[1530]](../bib_references/bib.md#bib1593)

To begin with, a nonequilibrium $\Delta$SCF or ROKS calculation requires
equilibrium solvation of the initial state (ground state for absorption
and excited state for emission). By activating **RF_ptSS_Save**= **true**
in the *$pcm* block, the equilibrated reaction field is
then stored on disk. Setting **RF_ptSS_Read** = **true** in an
arbitrary later job for the final state reads the reaction field again.
This automatically triggers a frozen reaction-field (fRF) SCF with the
stored reaction field of the initial state. The resulting SCF energy
corresponds to a zeroth order calculation of the final state in the
reaction field of the initial state. To obtain the first-order
nonequilibrium result, the fast solvent polarization is relaxed
for the final state by adding a perturbative ptSS correction, which is
printed after the converged fRF-SCF calculation.

### `RF_ptSS_Save`

> **Save the current reaction field to disk. INPUT SECTION: $pcm**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Save the reaction field in the current job.
>     * FALSE
>     * Do not save the reaction field in the current job.
> * **Recommendation**: The reaction field is saved for the reference state, which is for $\Delta$ SCF or ROKS just the SCF result, but for TDDFT + II-SS-PCM the chosen reference state (see Section 7.3.7.2 ). Activating RF_ptSS_SAVE for several subsequent jobs overwrites the reaction field.

### `RF_ptSS_Read`

> **Read the reaction field from disk and perform a fRF-SCF + ptSS-PCM calculation with it. INPUT SECTION: $pcm**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Read the reaction field in the current job.
>     * FALSE
>     * Do not read the reaction field in the current job.
> * **Recommendation**: The SCF result corresponds to zeroth order solvation of the final state. For first-order nonequilibrium solvation add the ptSS correction printed after the fRF-SCF.

???+ example "Example 7.60: Vertical excitation energy of formaldehyde in acetonitrile with ROKS + PCM and a nonequilibrium ptSS-PCM correction."
    ```qchem
    $rem
       method               pbe0
       basis                def2-SVP
       scf_convergence      8
       point_group_symmetry false
       solvent_method       pcm
    $end
    
    $pcm
       theory              iefpcm
       rf_ptss_save        true            ! Save the final ground state reaction field
    $end
    
    $solvent
       Dielectric          35.688000       ! Acetonitrile
       Dielectric_Infi     1.806874
    $end
    
    $molecule
       0 1
       H      -0.940372    0.000000    1.268098
       H       0.940372    0.000000    1.268098
       C       0.000000    0.000000    0.682557
       O       0.000000    0.000000   -0.518752
    $end
    
    @@@
    
    $rem
       method               pbe0
       basis                def2-SVP
       scf_guess            read
       roks                 true
       unrestricted         false
       scf_convergence      8
       point_group_symmetry false
       solvent_method       pcm
    $end
    
    $pcm
       theory              iefpcm
       rf_ptss_read        true            ! Read the prior reaction field and start fRF-SCF
    $end
    
    $solvent
       Dielectric          35.688000       ! Acetonitrile
       Dielectric_Infi     1.806874
    $end
    
    $molecule
       0 1
       read
    $end
    ```
