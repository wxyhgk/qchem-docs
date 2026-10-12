---
title: "11.4 Q-Chem/Charmm Interface"
---

# 11.4 **Q-Chem**/**Charmm** Interface

(July 4, 2026)

**Q-Chem** can be used a QM back-end for QM/MM calculations using the **Charmm**
package.[[1492]](../bib_references/bib.md#bib1551)
 In this case, both software packages are required
to perform the calculations, but all the code required for communication
between the programs is incorporated in the released versions. Stand-alone
QM/MM calculations are described in Section [11.3](sec_QMMM.md).

QM/MM jobs that use the **Charmm** interface are controlled using the following *$rem* keywords:

### `QM_MM`

> **Turns on the Q-Chem / Charmm interface.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Do QM/MM calculation through the Q-Chem / Charmm interface.
>     * `FALSE`: Turn this feature off.
> * **Recommendation**: Use the default unless running calculations with Charmm .

### `QMMM_PRINT`

> **Controls the amount of output printed from a QM/MM job.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Limit molecule, point charge, and analysis printing.
>     * `FALSE`: Normal printing.
> * **Recommendation**: Use the default unless running calculations with Charmm .

### `QMMM_CHARGES`

> **Controls the printing of QM charges to file.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Writes a charges.dat file with the Mulliken charges from the QM region.
>     * `FALSE`: No file written.
> * **Recommendation**: Use the default unless running calculations with Charmm where charges on the QM region need to be saved.

### `ESP_EFIELD`

> **Triggers the calculation of the electrostatic potential (ESP) and/or the electric field at the positions of the MM charges.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Computes ESP only.
>     * `1`: Computes ESP and electric field.
>     * `2`: Computes electric field only.
> * **Recommendation**: None.

### `GEOM_PRINT`

> **Controls the amount of geometric information printed at each step.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Prints out all geometric information; bond distances, angles, torsions.
>     * `FALSE`: Normal printing of distance matrix.
> * **Recommendation**: Use if you want to be able to quickly examine geometric parameters at the beginning and end of optimizations. Only prints in the beginning of single point energy calculations.

### `QMMM_FULL_HESSIAN`

> **Trigger the evaluation of the full QM/MM Hessian.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Evaluates full Hessian.
>     * `FALSE`: Hessian for QM-QM block only.
> * **Recommendation**: None

### `LINK_ATOM_PROJECTION`

> **Controls whether to perform a link-atom projection**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Performs the projection
>     * `FALSE`: No projection
> * **Recommendation**: Necessary in a full QM/MM Hessian evaluation on a system with link atoms

### `HESS_AND_GRAD`

> **Enables the evaluation of both analytical gradient and Hessian in a single job**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Evaluates both gradient and Hessian.
>     * `FALSE`: Evaluates Hessian only.
> * **Recommendation**: Use only in a frequency (and thus Hessian) evaluation.

### `GAUSSIAN_BLUR`

> **Enables the use of Gaussian-delocalized external charges in a QM/MM calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Delocalizes external charges with Gaussian functions.
>     * `FALSE`: Point charges
> * **Recommendation**: None

### `SKIP_CHARGE_SELF_INTERACT`

> **Ignores the electrostatic interactions among external charges in a QM/MM calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: No electrostatic interactions among external charges.
>     * `FALSE`: Computes the electrostatic interactions among external charges.
> * **Recommendation**: None

???+ example "Example 11.27: Do a basic QM/MM optimization of the water dimer. You need Charmm to do
this but this is the Q-Chem file that is needed to test the QM/MM functionality. These are the bare necessities for a Q-Chem / Charmm QM/MM calculation."
    ```qchem
    $molecule
       0 1
       O    -0.91126   1.09227   1.02007
       H    -1.75684   1.51867   1.28260
       H    -0.55929   1.74495   0.36940
    $end
    
    $rem
       METHOD        hf        ! HF Exchange
       BASIS         cc-pvdz   ! Correlation Consistent Basis
       QM_MM         true      ! Turn on QM/MM calculation
       JOBTYPE       force     ! Need this for QM/MM optimizations
    $end
    
    $external_charges
       1.20426      -0.64330   0.79922  -0.83400
       1.01723      -1.36906   1.39217   0.41700
       0.43830      -0.06644   0.91277   0.41700
    $end
    ```

The **Q-Chem**/**Charmm** interface is unique in that:

- The external point charges can be replaced with Gaussian-delocalized
charges with a finite width.[[300]](../bib_references/bib.md#bib304)
 This is an empirical way to
include the delocalized character of the electron density of atoms in the MM
region. This can be important for the electrostatic interaction of the QM
region with nearby atoms in the MM region.
- We allow the evaluation of the full QM/MM Hessian.[[1491]](../bib_references/bib.md#bib1552)

When link atoms are inserted to saturate the QM region, all Hessian
elements associated with link atoms are automatically projected onto their QM
and MM host atoms.
- For systems with a large number of MM atoms, one can define blocks
consisting of multiple MM atoms (*i.e.*, mobile blocks) and efficiently evaluate
the corresponding mobile-block Hessian (MBH) for normal mode analysis.
