---
title: "7.5.2 Job Control"
---

## 7.5.2 Job Control

(July 4, 2026)

**Q-Chem** features **libnoci**, a package dedicated to running
NOCI calculations, and accessed using USE_LIBNOCI = TRUE.
The **libnoci** implementation introduces flexible job control, whereby the method
used to generate multiple states for the NOCI basis can be defined by the user.
Initially, a set of reference determinants must be chosen, either using a
single SCF calculation or by reading sets or orbital coefficients from file
as requested by the *$rem* variable NOCI_REFGEN.
From these reference states, multiple non-orthogonal states are then
created either using SCF metadynamics, or as excitations from the reference
determinants, as requested by the *$rem* variable NOCI_DETGEN.
When generating multiple using excitations within an active space, the
active orbitals are controlled using the *$active_orbitals* input section.
For example:

> ```qchem
> $active_orbitals
>     1 4 11 14
> $end
> ```

The $\beta$ orbitals are offset by the total number of $\alpha$ molecular
orbitals (*e.g.* the above example selects $\alpha$ orbitals 1 and 4, along with
$\beta$ orbitals 1 and 4, with a total of 10 $\alpha$ MOs including occupied
and virtual orbitals). The resulting multiple determinants are then
individually relaxed at the SCF level, unless this is explicitly skipped using
SKIP_SCFMAN = TRUE. Finally, NOCI is run using the full set of
multiple determinants identified.

The **libnoci** package also incorporates compatibility with the new SCF
metadynamics implementation (see Section [4.9.3](../ch04_scf/subsubsec_SCFMetadynNOCI.md)), as
well as the holomorphic Hartree–Fock approach which allows multiple
Hartree–Fock solutions to be continued across all geometries (see
Section. [4.9.4](../ch04_scf/sec_HoloHF.md)).

USE_LIBNOCI

### `USE_LIBNOCI`

> **Turn on the use of libnoci for running NOCI calculations.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * False
>     * Do not use
>     * libnoci
>     * (uses original
>     * Q-Chem
>     * implementation).
>     * True
>     * Use the
>     * libnoci
>     * implementation.
> * **Recommendation**: The $rem variables detailed below are only available in libnoci .

NOCI_REFGEN

### `NOCI_REFGEN`

> **Control how the initial reference determinants are created.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Generate initial reference determinant from a single SCF calculation.
>     * 1
>     * Read (multiple) initial reference determinants from a previous calculation.
> * **Recommendation**: The specific reference determinants to be read from a previous calculation can be indicated using SCF_READMINIMA .

NOCI_DETGEN

### `NOCI_DETGEN`

> **Control how the multiple determinants for NOCI are created.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Use only the initial reference determinants.
>     * 1
>     * Generate CIS excitations from each reference determinant.
>     * 2
>     * Generate all FCI excitations from each reference determinant.
>     * 3
>     * Generate
>     * $n$
>     * multiple determinants using SCF metadynamics, where
>     * $n$
>     * is specified
>     * using
>     * SCF_SAVEMINIMA
>     * =
>     * $n$
>     * .
>     * 4
>     * Generate all CAS excitations from each reference determinant, where the active orbitals
>     * are specified using the
>     * $active_orbitals
>     * input section.
> * **Recommendation**: By default, these multiple determinants are optimized at the SCF level before running NOCI. This behavior can be turned off using by specifying SKIP_SCFMAN = TRUE .

NOCI_NEIGVAL

### `NOCI_NEIGVAL`

> **The number of NOCI eigenvalues to be printed.**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $n$
>     * Positive integer
> * **Recommendation**: Increase this to print progressively higher NOCI energies.

NOCI_PRINT

### `NOCI_PRINT`

> **Specify the debug print level of NOCI.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $n$
>     * Positive integer
> * **Recommendation**: Increase this for additional debug information.

???+ example "Example 7.39: NOCI for H ${}_{2}$ run in the libnoci implementation, with multiple determinants
generated using SCF metadynamics."
    ```qchem
    $molecule
       0 1
       H    0.0000000   0.0000000   0.0000000
       H    0.0000000   0.0000000   4.0000000
    $end
    
    $rem
       EXCHANGE                   hf
       CORRELATION                noci
       UNRESTRICTED               true
       BASIS                      sto-3g
       SCF_CONVERGENCE            10
       MAX_SCF_CYCLES             1000
       MOM_START                  1
       USE_LIBNOCI                true
       SCF_SAVEMINIMA             4
       SCF_MINFIND_RANDOMMIXING   30000
       SCF_MINFIND_MIXMETHOD      1
       NOCI_REFGEN                0
       NOCI_DETGEN                3
       NOCI_NEIGVAL               4
    $end
    ```
