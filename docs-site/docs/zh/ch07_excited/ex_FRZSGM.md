---
title: "7.7.6 Freeze-and-Release Calculations"
---

## 7.7.6 Freeze-and-Release Calculations

(July 4, 2026)

The $\Delta$SCF approach recasts the excited-state problem as variational optimization of the
electronic energy belonging to one or more electronic configurations generated using a single set of MOs.
Although this procedure can yield accurate results for excited-state energies and
properties,[[143]](../bib_references/bib.md#bib133)
 variational convergence on the
excited-state electronic hypersurface is more difficult than for ground-state calculations.
Furthermore, the performance of variational optimization algorithms is intrinsically
sensitive to their initial guess, meaning that the ground-state MOs are not always
suitable for starting the calculation of an excited state in which the polarization
of the electron density changes significantly, *e.g.*, a charge-transfer excitation.
The use of a poor guess may result in convergence to another electronic state, like
in variational collapse to the ground state, slow convergence, or no convergence at all.
Because of that, it is desirable to develop guess-refinement algorithms to improve the
quality of the initial guess and, consequently, the convergence of the excited-state electron density.

Recently, Schmerwitz *et al.* proposed to perform a constrained optimization
on the ground-state MOs (*frozen* step), whose result is then used to set up
a full MO relaxation (*release* step).[[1212]](../bib_references/bib.md#bib1267)

A constrained optimization algorithm inspired by this contribution was implemented in **Q-Chem**,[[144]](../bib_references/bib.md#bib134)

named the FRZ MO guess.
This method was applied to the calculation of challenging CT excitations in supramolecular
complexes in combination with the SGM algorithm of
Section [7.7.5](ex_BEDSCF.md).[[511]](../bib_references/bib.md#bib526)

We call this a freeze-and-release electronic structure method, FRZ-SGM.

![Figure 7.1: $\mathbf{C}$ matrix partitioning for frozen electron-and-hole constrained optimization.
Panel A shows the example of a double excitation from MO no. 2, with the energy $\varepsilon_{2}$ ,
to MO no. 4, with the energy $\varepsilon_{4}$ , on an arbitrary energy axis E.
The $\mathbf{C}$ matrix is given in the general form in panel B.
Active doubly-occupied vectors are highlighted in red, active virtual orbitals in green,
and all frozen vectors in grey.](../assets/x1.png)

*Figure 7.1: $\mathbf{C}$ matrix partitioning for frozen electron-and-hole constrained optimization.
Panel A shows the example of a double excitation from MO no. 2, with the energy $\varepsilon_{2}$ ,
to MO no. 4, with the energy $\varepsilon_{4}$ , on an arbitrary energy axis E.
The $\mathbf{C}$ matrix is given in the general form in panel B.
Active doubly-occupied vectors are highlighted in red, active virtual orbitals in green,
and all frozen vectors in grey.*

To set up an electronic structure calculation with constrained orbitals, it is necessary
to group the MO rotations in *active* and *frozen* when updating the
$\mathbf{C}$ matrix with a unitary transformation.
In restricted Kohn–Sham (RKS) theory, this matrix is partitioned into occupied and
unoccupied (virtual) *sub-spaces*.
We start by describing the simplest case of the RKS matrix and then extend our
formulation to unrestricted Kohn–Sham (UKS) theory.
It is important to **manually reorder** the MO column vectors in the
$\mathbf{C}$ matrix at the beginning of a calculation to have the right occupied/virtual
MOs frozen. In frozen RKS, the $\mathbf{C}$ matrix has the structure outlined in
Fig. [7.1](#fig:FRZ-Cmat), where the size of the frozen blocks is given by the a_frozen and
va_frozen *$rem* variables, for the doubly-occupied and virtual
blocks, respectively.
**It is up to the user to reorder the MOs** to have the excited electron(s) in
the rightmost block of the D block and the hole(s) in the rightmost block of the V block;
this is done using the *$reorder_alpha* input section.
This structure will be used to construct the MO rotations, as well as to calculate the
corresponding gradients and steps.
In the simple example shown in panel A of Fig. [7.1](#fig:FRZ-Cmat), a double excitation is
computed by exciting one $\alpha$ and one $\beta$ electron from MO no. 2 to MO no. 4,
and the MOs are sorted in the order 1-4-3-5-6-2.
The D${}_{\mathrm{f}}$ and V${}_{\mathrm{f}}$ blocks contain only MOs no. 4 and 2, respectively.
The block structure emerging for the $\mathbf{C}$ matrix by partitioning into active
and frozen parts is depicted in panel B of Fig. [7.1](#fig:FRZ-Cmat), using the general
notation introduced above.

This structure is extended to the UKS electronic structure.
In the UKS case, two separate RKS calculations are performed on the $\alpha$ and
$\beta$ MO sets. Since one can have excitations of $\alpha$ and $\beta$ electrons,
the b_frozen and vb_frozen are introduced to freeze the $\beta$ MOs.
The $\beta$ MOs can be reordered using the *$reorder_beta* input section.

FROZEN_ORBITAL

### `FROZEN_ORBITAL`

> **turns on the constrained optimization library (prints in the output A frozen … calculation will be performed using … ).**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not perform a constrained optimization.
>     * TRUE
>     * Perform a constrained optimization.
> * **Recommendation**: Only works with the GDM optimization algorithm. For a the constrained optimization to be effective, the user must manually reorder the MOs as explained above.

A_FROZEN

### `A_FROZEN`

> **Sets the number of frozen $\alpha$ MOs in a RKS or UKS calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * No frozen vectors.
>     * Af
>     * Freeze the last Af occupied
>     * $\alpha$
>     * MOs.
> * **Recommendation**: None

VA_FROZEN

### `VA_FROZEN`

> **Sets the number of frozen virtual $\alpha$ MOs in a RKS or UKS calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `FALSE`
> * **Options**:
>     * 0
>     * No frozen vectors.
>     * VAf
>     * Freeze the last VAf virtual
>     * $\alpha$
>     * MOs.
> * **Recommendation**: None

B_FROZEN

### `B_FROZEN`

> **Sets the number of frozen $\beta$ MOs in a UKS calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * No frozen vectors.
>     * Bf
>     * Freeze the last Bf occupied
>     * $\beta$
>     * MOs.
> * **Recommendation**: None

VB_FROZEN

### `VB_FROZEN`

> **Sets the number of frozen virtual $\beta$ MOs in a UKS calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `FALSE`
> * **Options**:
>     * 0
>     * No frozen vectors.
>     * VBf
>     * Freeze the last VBf virtual
>     * $\beta$
>     * MOs.
> * **Recommendation**: None

???+ example "Example 7.7.56: Example input for the freeze-and-release calculation of the lowest-lying
intermolecular charge transfer excitation in a tetrafluorethylene–ethylene
dimer using the FRZ-SGM method 144 Bogo N. et al. Phys. Chem. Chem. Phys. (2025) , 27 , pp. 17533 . Link ."
    ```qchem
    $molecule
    0 1
    F     -1.394866    -1.110938     -0.741831
    F     -1.394866     1.110938     -0.741831
    F      1.394866    -1.110938     -0.741831
    F      1.394866     1.110938     -0.741831
    C     -0.667784     0.000000     -0.759941
    C      0.667784     0.000000     -0.759941
    H     -1.244242     0.935429      2.658551
    H     -1.244242    -0.935429      2.658551
    H      1.244242     0.935429      2.658551
    H      1.244242    -0.935429      2.658551
    C     -0.674558     0.000000      2.662317
    C      0.674558     0.000000      2.662317
    $end
    
    $rem
       thresh              12
       scf_convergence     8
       method              LRC-wPBE
       basis               def2-TZVP
       scf_algorithm       diis_gdm
       sym_ignore          true
       symmetry            false
    $end
    
    @@@
    
    $rem
       frozen_orbital      true
       a_frozen            1
       va_frozen           1
       scf_algorithm       gdm
       unrestricted        true
       thresh              10
       scf_convergence     6
       method              LRC-wPBE
       basis               def2-TZVP
       scf_guess           read
       scf_max_cycles      500
       sym_ignore          true
       symmetry            false
    $end
    
    $molecule
    read
    $end
    
    $reorder_alphas
    1:31 33:272 32
    $end
    
    @@@
    
    $rem
    unrestricted        true
    scf_guess           read
    scf_algorithm       sgm_ls
    method              LRC-wPBE
    basis               def2-TZVP
    sym_ignore          true
    symmetry            false
    SCF_MAX_CYCLES      200
    scf_convergence     5
    THRESH              14
    $end
    
    $molecule
    read
    $end
    ```
