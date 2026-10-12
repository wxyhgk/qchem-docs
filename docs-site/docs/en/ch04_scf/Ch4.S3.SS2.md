---
title: "4.3.2 Job Control"
---

## 4.3.2 Job Control

(July 4, 2026)

The following two *$rem* variables must be specified in order to run HF calculations:

### `METHOD`

> **Specifies the exchange-correlation functional.**
>
> * **Type**: `STRING`
> * **Default**: `No default`
> * **Options**:
>     * `NAME`: Use =
>     * `NAME`: , where
>     * `NAME`: is one of the following: HF for Hartree-Fock theory; one of the DFT methods listed in Section 5.3.5 .; one of the correlated methods listed in Sections 7.9 , 7.10 , and 7.8 ;
> * **Recommendation**: In general, consult the literature to guide your selection. Our recommendations for DFT are indicated in bold in Section 5.3.5 .

### `BASIS`

> **Specifies the basis sets to be used.**
>
> * **Type**: `STRING`
> * **Default**: `No default basis set`
> * **Options**:
>     * `General, Gen`: User defined ( $basis keyword required).
>     * `Symbol`: Use standard basis sets as per Chapter
>     * `8`: .
>     * `Mixed`: Use a mixture of basis sets (see Chapter
>     * `8`: ).
> * **Recommendation**: Consult literature and reviews to aid your selection.

In addition, the following *$rem* variables can be used to customize the SCF calculation:

### `GEN_SCFMAN`

> **Use GEN_SCFMAN for the present SCF calculation.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `TRUE`
> * **Options**:
>     * `FALSE`: Use the previous SCF code.
>     * `TRUE`: Use GEN_SCFMAN.
> * **Recommendation**: Set to FALSE in cases where features not yet supported by GEN_SCFMAN are needed.

### `ORBITAL_ENERGY_PREC`

> **Obtain additional digits of precision in the orbital energies.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Standard printout with 4 decimal digits (in Hartree).
>     * `1`: 5 decimal digits.
>     * `2`: Scientific notation with 10 digits of precision.
> * **Recommendation**: Set as desired. Has no effect in cases where the orbital symmetry labels are printed; use SYM_IGNORE = TRUE if additional precision is needed in such cases.

### `PRINT_ORBITALS`

> **Prints orbital coefficients with atom labels in analysis part of output.**
>
> * **Type**: `INTEGER/LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not print any orbitals.
>     * `TRUE`: Prints occupied orbitals plus 5 virtual orbitals.
>     * `NVIRT`: Number of virtual orbitals to print.
> * **Recommendation**: Use true unless more virtual orbitals are desired.

### `SCF_CONVERGENCE`

> **SCF is considered converged when the wave function error is less that $10^{-\mathrm{SCF\_CONVERGENCE}}$ . Adjust the value of THRESH at the same time.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * `User-defined`
> * **Recommendation**: Tighter criteria are recommended for geometry optimization and vibration analysis. Larger values provide more significant figures, at greater computational cost. Beginning with Q-Chem 3.0, the DIIS error is measured by the maximum error rather than the RMS error that was used in earlier versions.

### `UNRESTRICTED`

> **Controls the use of restricted or unrestricted orbitals.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Constrain the spatial part of the alpha and beta orbitals to be the same.
>     * `TRUE`: Do not Constrain the spatial part of the alpha and beta orbitals.
> * **Recommendation**: Use the default unless ROHF is desired. Note that for unrestricted calculations on systems with an even number of electrons it is usually necessary to break $\alpha$ / $\beta$ symmetry in the initial guess, by using SCF_GUESS_MIX or providing $occupied information (see Section 4.4 on initial guesses).

The calculations using other more special orbital types are controlled by the
following *$rem* variables (they are not effective if GEN_SCFMAN =
FALSE):

### `OS_ROSCF`

> **Run an open-shell singlet ROSCF calculation with GEN_SCFMAN.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: OS_ROSCF calculation is performed.
>     * `FALSE`: Do not run OS_ROSCF (it will run a closed-shell RSCF calculation instead).
> * **Recommendation**: Set to TRUE if desired.

### `ROSCF_DODS`

> **Run a canonical restricted open-shell calculation (also called “ROSCF-DODS”, where DODS stands for different orbitals for different spins) with GEN_SCFMAN. Available for high-spin half-filled open-shell systems.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Perform a canonical ROSCF calculation.
>     * `FALSE`: Do not perform a canonical ROSCF calculation (run an open-shell USCF calculation instead).
> * **Recommendation**: Set to TRUE if desired.

### `GHF`

> **Run a generalized Hartree-Fock calculation with GEN_SCFMAN.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Run a GHF calculation.
>     * `FALSE`: Do not use GHF.
> * **Recommendation**: Set to TRUE if desired.

### `COMPLEX`

> **Run an SCF calculation with complex MOs using GEN_SCFMAN.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Use complex orbitals.
>     * `FALSE`: Use real orbitals.
> * **Recommendation**: Set to TRUE if desired.

### `COMPLEX_MIX`

> **Mix a certain percentage of the real part of the HOMO to the imaginary part of the LUMO.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0–100`: The mix angle = $\pi\cdot$ /100.
> * **Recommendation**: It may help find the stable complex solution (similar idea as SCF_GUESS_MIX ).

???+ example "Example 4.1: Restricted open-shell singlet ROSCF calculation for the first excited state of
formaldehyde using GEN_SCFMAN. The first job provides the guess orbitals
through a restricted SCF calculation."
    ```qchem
    $molecule
       0 1
       H -0.940372  0.000000  1.268098
       H  0.940372  0.000000  1.268098
       C  0.000000  0.000000  0.682557
       O  0.000000  0.000000 -0.518752
    $end
    
    $rem
       GEN_SCFMAN        true
       METHOD            wb97x-d
       BASIS             def2-svpd
       THRESH            14
       SCF_CONVERGENCE   9
    point_group_symmetry False
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE           sp
       METHOD            wb97x-d
       BASIS             def2-svpd
       GEN_SCFMAN        true
       OS_ROSCF          true
       THRESH            14
       SCF_CONVERGENCE   9
       SCF_ALGORITHM     diis
    point_group_symmetry False
       SCF_GUESS         read
    $end
    ```
