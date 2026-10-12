---
title: "4.4.4 Modifying the Occupied Molecular Orbitals"
---

## 4.4.4 Modifying the Occupied Molecular Orbitals

(July 4, 2026)

It is sometimes useful for the occupied guess orbitals to be other than the
lowest $N_{\alpha}$ (or $N_{\beta}$) orbitals. Reasons why one may need
to do this include:

- •

To converge to a state of different symmetry or orbital occupation.
- •

To break spatial symmetry.
- •

To break spin symmetry, as in unrestricted calculations on molecules with
an even number of electrons.

There are two mechanisms for modifying a set of guess orbitals: either by
SCF_GUESS_MIX, or by specifying the orbitals to occupy. **Q-Chem**
users may define the occupied guess orbitals using the *$occupied* or *$swap_occupied_virtual*
keywords. In the former, occupied guess orbitals are defined by listing the
$\alpha$ orbitals to be occupied on the first line and $\beta$ on the second. In the
former, only pair of orbitals that needs to be swapped is specified.

**Note: 

(1) To prevent **Q-Chem** to change orbital occupation during SCF procedure,
MOM_START option is often used in combination with
*$occupied* or *$swap_occupied_virtual* keywords.
(2) The need for orbitals renders these options incompatible with the SAD
guess. Most often, they are used with SCF_GUESS = READ.
**

The format for modifying occupied guess orbitals is as follows:

> ```qchem
> $occupied
>    1  2  3  4 ...  NAlpha
>    1  2  3  4 ...  NBeta
> $end
> ```

or alternatively

> ```qchem
> $swap_occupied_virtual
>    <spin> <io1> <iv1>
>    <spin> <io2> <iv2>
> $end
> ```

Occupied and virtual orbitals can also be swapped

> ```qchem
> $swap_occupied_virtual
>    alpha  5  6
>    beta   6  7
> $end
> ```

This is identical to

> ```qchem
> $occupied
>    1 2 3 4 6 5 7
>    1 2 3 4 5 7 6
> $end
> ```

or

> ```qchem
> $occupied
>    1:4 6 5 7
>    1:5 7 6
> $end
> ```

The other *$rem* variables related to altering the orbital occupancies are:

### `SCF_GUESS_PRINT`

> **Controls printing of guess MOs, Fock and density matrices.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not print guesses.
>     * `SAD`
>     * `1`: Atomic density matrices and molecular matrix.
>     * `2`: Level 1 plus density matrices.
>     * `CORE and GWH`
>     * `1`: No extra output.
>     * `2`: Level 1 plus Fock and density matrices and, MO coefficients and eigenvalues.
>     * `READ`
>     * `1`: No extra output
>     * `2`: Level 1 plus density matrices, MO coefficients and eigenvalues.
> * **Recommendation**: None

### `SCF_GUESS_MIX`

> **Controls mixing of LUMO and HOMO to break symmetry in the initial guess. For unrestricted jobs, the mixing is performed only for the alpha orbitals.**
>
> * **Type**: `INTEGER`
> * **Default**: `0 (FALSE)`
> * **Options**:
>     * `0 (FALSE)`: Do not mix HOMO and LUMO in SCF guess.
>     * `1 (TRUE)`: Add 10% of LUMO to HOMO to break symmetry.
>     * $n$: Add $10n$ % of LUMO to HOMO ( $0<n<10$ ).
> * **Recommendation**: When performing unrestricted calculations on molecules with an even number of electrons, it is often necessary to break alpha/beta symmetry in the initial guess with this option, or by specifying input for $occupied .

???+ example "Example 4.6: Input for an unrestricted HF calculation on H ${}_{2}$ in the
dissociation limit, showing the use of SCF_GUESS_MIX = 2
(corresponding to 20% of the alpha LUMO mixed with the alpha HOMO).
Geometric direct minimization with DIIS is used to converge the SCF, together
with MAX_DIIS_CYCLES = 1 (using the default value for MAX_DIIS_CYCLES , the DIIS procedure just oscillates)."
    ```qchem
    $molecule
       0  1
       H  0.000   0.000   0.0
       H  0.000   0.000 -10.0
    $end
    
    $rem
       METHOD           =  hf
       BASIS            =  6-31g**
       UNRESTRICTED     =  true
       SCF_ALGORITHM    =  diis_gdm
       MAX_DIIS_CYCLES  =  1
       SCF_GUESS        =  gwh
       SCF_GUESS_MIX    =  2
    $end
    ```
