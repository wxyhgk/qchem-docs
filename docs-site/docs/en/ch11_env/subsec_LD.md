---
title: "11.2.10 Langevin Dipoles Model"
---

## 11.2.10 Langevin Dipoles Model

(July 4, 2026)

**Q-Chem** provides the option to calculate molecular properties in aqueous
solution and the magnitudes of the hydration free energies by the Langevin
dipoles (LD) solvation model developed by Florián and Warshel.[[394]](../bib_references/bib.md#bib402)

In this model, a solute molecule is surrounded by a sphere of point
dipoles, with centers on a cubic lattice. Each of these “Langevin” dipoles
changes its size and orientation in the electrostatic field of the solute and
the other Langevin dipoles. The electrostatic field from the solute is
determined rigorously by the integration of its charge density, whereas for
dipole–dipole interactions, a 12 Å cutoff is used. The **Q-Chem**/**ChemSol** 1.0 implementation of the LD model is fully self-consistent in that
the molecular quantum mechanical calculation takes into account solute–solvent
interactions. Further details on the implementation and parameterization of
this model can be found in the literature.[[394]](../bib_references/bib.md#bib402)

The results of **ChemSol** calculations are printed in the standard output file.
Below is a part of the output for a calculation on the methoxide anion
(corresponding to the sample input given later on, and the sample file in the
`$QC/samples` directory).

| Energy Component | Value / kcal mol ${}^{-1}$ |
| --- | --- |
| LD Electrostatic energy | $-86.14$ |
| Hydrophobic energy | 0.28 |
| van der Waals energy | $-1.95$ |
| Bulk correction | $-10.07$ |
| Solvation free energy, $\Delta G$ (ILD) | $-97.87$ |

Table 11.8: 
Results of the iterative Langevin Dipoles (ILD) solvation model, for aqueous methoxide.

The total hydration free energy, $\Delta G$(ILD) is calculated as a sum of
several contributions. Note that the electrostatic part of $\Delta G$ is
calculated by using the linear-response approximation[[394]](../bib_references/bib.md#bib402)
 and
contains contributions from the *polarization* of the solute charge
distribution due to its interaction with the solvent. This results from the
self-consistent implementation of the Langevin dipoles model within **Q-Chem**.

To perform an LD calculation in **Q-Chem**, specify normal job-control variables
for a Hartree-Fock or DFT calculation, and set SOLVENT_METHOD =
CHEM_SOL in the *$rem* section. Additional fine-tuning is
accomplished using a set of keywords in a *$chem_sol* input section. The
remainder of this section summarizes these keywords.

### `EField`

> **Determines how the solute charge distribution is approximated in evaluating the electrostatic field of the solute. INPUT SECTION: $chem_sol**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 1
>     * Exact solute charge distribution is used.
>     * 0
>     * Solute charge distribution is approximated by Mulliken atomic charges.
> * **Recommendation**: None. The Mulliken-based procedure is faster but less rigorous.

### `NGrids`

> **Sets the number of grids used to calculate the average hydration free energy. INPUT SECTION: $chem_sol**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$
>     * Use
>     * $n$
>     * different grids.
> * **Recommendation**: None. The maximum allowed value of $n$ is 20.

### `Print`

> **Controls printing in the ChemSol part of the Q-Chem output file. INPUT SECTION: $chem_sol**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Limited printing
>     * 1
>     * Full printing
> * **Recommendation**: None.

### `ReadRadii`

> **Read user-defined atomic radii from section $van_der_waals . INPUT SECTION: $chem_sol**
>
> * **Type**: `None`
> * **Default**: `Off`
> * **Options**:
>     * No options. Specify the keyword to use user-defined atomic radii.
> * **Recommendation**: None.

Accurate calculations of hydration free energies require a judicious choice of
the solute–solvent boundary in terms of atom-type dependent parameters. The
default atomic van der Waals radii available in **Q-Chem** were chosen to provide
reasonable hydration free energies for most solutes and basis sets. These
parameters basically coincide with the **ChemSol** 2.0 radii given in
Ref. [[395]](../bib_references/bib.md#bib403)
. The only difference between the **Q-Chem** and
**ChemSol** 2.0 atomic radii stems from the fact that **Q-Chem** parameter set
uses radii for carbon and oxygen that are independent of the atom’s
hybridization state. User-defined atomic radii can be specified by declaring
the option **ReadRadii** in the *$chem_sol* input section, and then placing
the radii in the *$van_der_waals* section. Two different (and mutually exclusive)
formats can be used, as shown below.

> ```qchem
> $van_der_waals
> 1
> atomic_number   vdW_radius
> ...
> $end
> 
> $van_der_waals
> 2
> sequential_atom_number   vdW_radius
> ...
> $end
> ```

The purpose of the second format is to permit the user to customize the radius
of specific atoms, in the order that they appear in the *$molecule* section,
rather than simply by atomic numbers as in format 1. The radii of atoms that
are not listed in the *$van_der_waals* input will be assigned default values. The atomic
radii that were used in the calculation are printed in the **ChemSol** part of
the output file in the column denoted *rp*. All radii should be given in
Ångstroms.

???+ example "Example 11.19: A Langevin dipoles calculation on the methoxide anion. A customized value is
specified for the radius of the carbon atom."
    ```qchem
    $molecule
      -1  1
       C   0.0000   0.0000  -0.5274
       O   0.0000   0.0000   0.7831
       H   0.0000   1.0140  -1.0335
       H   0.8782  -0.5070  -1.0335
       H  -0.8782  -0.5070  -1.0335
    $end
    
    $rem
       METHOD            hf
       BASIS             6-31G
       SCF_CONVERGENCE   6
       SOLVENT_METHOD    Chem_Sol
    $end
    
    $chem_sol
    ReadRadii
    $end
    
    $van_der_waals
    2
    1 2.5
    $end
    ```
