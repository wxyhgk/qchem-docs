---
title: "11.2.2 Kirkwood-Onsager Multipole Expansion Method"
---

## 11.2.2 Kirkwood-Onsager Multipole Expansion Method

(July 4, 2026)

The simplest implicit solvation model available in **Q-Chem** is the
multipolar expansion model,[[690]](../bib_references/bib.md#bib716)

which has also been called the Kirkwood-Onsager model or sometimes the generalized Kirkwood
model.[[569]](../bib_references/bib.md#bib580)

In this approach, the solute is placed inside of a spherical cavity of radius $a$ that is surrounded by a
homogeneous dielectric medium whose dielectric constant is $\varepsilon$, and these constitute the only
parameters of the model. The term *Onsager model* is sometimes synonymous with a point-dipole
approximation for the solute’s charge density, but **Q-Chem**’s version uses a single-center multipole
expansion of the density (which can be extended to arbitrarily high order), in order to obtain an essentially
exact description of the solute’s electrostatic potential. The model then consists of using Kirkwood’s
analytic expressions for the solvation energy of each spherical harmonic function, in a spherical cavity inside
of a dielectric continuum.[[569]](../bib_references/bib.md#bib580)

Regarding the cavity radius $a$,
Onsager’s original suggestion is based on the molar volume $V_{m}$ of the pure solute,

<a id="eq:OnsagerRadius"></a>

$$
a=(3V_{m}/4\pi N_{A})^{1/3} \tag{11.1}
$$

where $N_{A}$ is Avogadro’s constant. This was later shown to be a poor choice in the context of
modern quantum chemistry calculations.[[569]](../bib_references/bib.md#bib580)

It is also common to add 0.5 Å to the value of $a$ in Eq. ([11.1](#eq:OnsagerRadius)) in
order to account for the first solvation shell,[[1490]](../bib_references/bib.md#bib1550)
 or to set $a$ equal to
the maximum distance between the solute center of
mass and the solute atoms, plus the relevant van der Waals radii. A third
option is to set $2a$ (the cavity diameter) equal to the largest
solute–solvent internuclear distance, plus the van der Waals radii of the relevant atoms.
Clearly, there is quite a bit of arbitrariness in this choice and solvation energies are quite
sensitive to the value of $a$,[[569]](../bib_references/bib.md#bib580)
 and the PCMs that are described in
Section [11.2.3](topic_pcm-em.md) have largely made the multipolar expansion method obsolete, since
the PCMs employ the exact electron density and can be used (if desired) with a spherical cavity,
although the more typical choice is a molecule-shaped van der Waals cavity.

The Kirkwood-Onsager SCRF is requested by setting SOLVENT_METHOD =
KIRKWOOD in the *$rem* section.
Some additional options can be specified in the *$solvent* section,
as described below, of which only **CavityRadius** is required.
Energies and analytic gradients for the Kirkwood-Onsager solvent model are
available for Hartree-Fock, DFT, and CCSD calculations. It is often advisable
to perform a gas-phase calculation of the solute molecule first, which can
serve as the initial guess for a subsequent Kirkwood-Onsager implicit solvent calculation.
For coupled-cluster calculations using this model, one may set
CC_SAVEAMPL = TRUE to retain the CC amplitudes from the gas-phase calculation, which
will save some time in the subsequent solution-phase calculation.

**Note: 

For CCSD calculations the Kirkwood-Onsager model works only with CCMAN2 = FALSE.
**

The following job-control options belong in the *$solvent* section, not the *$rem* section.
As with other parts of the **Q-Chem** input file, this input section is not case-sensitive.

### `CavityRadius`

> **Sets the radius of the spherical solute cavity. INPUT SECTION: $solvent**
>
> * **Type**: `FLOAT`
> * **Default**: `No default.`
> * **Options**:
>     * $a$: Cavity radius in Å.
> * **Recommendation**: None

### `Dielectric`

> **Sets the dielectric constant of the solvent continuum. INPUT SECTION: $solvent**
>
> * **Type**: `FLOAT`
> * **Default**: `78.39`
> * **Options**:
>     * $\varepsilon$: Use a (dimensionless) value of $\varepsilon$ .
> * **Recommendation**: The default value corresponds to water at 25 ${}^{\circ}$ C.

### `MultipoleOrder`

> **Determines the order to which the multipole expansion of the solute charge density is carried out. INPUT SECTION: $solvent**
>
> * **Type**: `INTEGER`
> * **Default**: `15`
> * **Options**:
>     * $\ell$: Include up to $\ell$ th order multipoles.
> * **Recommendation**: Use the default. The multipole expansion is usually converged by order $\ell$ = 15.

???+ example "Example 11.1: Multipole expansion model at the Hartree-Fock level; H ${}_{2}$ O in acetonitrile"
    ```qchem
    $molecule
       0 1
       O       0.00000000     0.00000000     0.11722303
       H      -0.75908339     0.00000000    -0.46889211
       H       0.75908339     0.00000000    -0.46889211
    $end
    
    $rem
       METHOD            HF
       BASIS             6-31g**
       SOLVENT_METHOD    Kirkwood
    $end
    
    $solvent
       CavityRadius      1.8    !   1.8 Angstrom Solute Radius
       Dielectric        35.9   !   Acetonitrile
       MultipoleOrder    15     !   this is the default value
    $end
    ```

???+ example "Example 11.2: Kirkwood-Onsager SCRF applied to hydrogen fluoride in water, performing a
gas-phase calculation first."
    ```qchem
    $molecule
       0 1
       H       0.000000     0.000000    -0.862674
       F       0.000000     0.000000     0.043813
     $end
    
    $rem
       METHOD          HF
       BASIS           6-31G*
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
       JOBTYPE           FORCE
       METHOD            HF
       BASIS             6-31G*
       SOLVENT_METHOD    KIRKWOOD
       SCF_GUESS         READ  ! read vacuum solution as a guess
    $end
    
    $solvent
       CavityRadius    2.5
    $end
    ```
