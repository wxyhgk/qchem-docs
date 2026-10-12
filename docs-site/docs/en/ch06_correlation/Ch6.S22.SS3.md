---
title: "6.22.3 ASCI Job Control"
---

## 6.22.3 ASCI Job Control

(July 4, 2026)

Active space specification and convergence details are controlled by the *$rem*
variables described in Section [6.20.2](subsec_casscf_rems.md). During the course of an ASCI
calculation, a file named `wf_data` is created in the scratch directory containing
information on the determinants and weights in the ASCI wave function.

### `ASCI_DIAG`

> **Specifies the diagonalization procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * `1`: Davidson solver
>     * `2`: Eigen sparse matrix solver
> * **Recommendation**: Use 2 for best trade-off of speed and memory usage. If memory usage becomes to great, switch to 1 .

### `ASCI_NDETS`

> **Specifies the number of determinants to include in the ASCI wave function.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $N$: for a wave function with $N$ determinants
> * **Recommendation**: Typical ASCI expansions range from 50,000 to 2,000,000 determinants depending on active space size, complexity of problem, and desired accuracy

### `ASCI_CDETS`

> **Specifies the number of determinants to search over during ASCI wave function growth steps.**
>
> * **Type**: `INTEGER`
> * **Default**: `-5`
> * **Options**:
>     * $N>0$: search from the top $N$ determinants $N<0$ search from the top determinants whose cumulative weight in the wave function corresponds to $1-2^{N}$
> * **Recommendation**: Using a dynamically determined value ( $N<0$ ) gives better results.

### `ASCI_USE_NAT_ORBS`

> **Specifies whether rotation to a natural orbital basis should be carried out between growth steps.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: rotate to a natural orbital basis between growth wave function growth steps
>     * `FALSE`: do not rotate to a natural orbital basis
> * **Recommendation**: Natural orbital rotations significantly improve the compactness and therefore accuracy of the ASCI wave function.

### `ASCI_DAVIDSON_GUESS`

> **Specifies the truncated CI guess used for ASCI’s Davidson solver.**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * $N$: Order of the truncated CI to solve explicitly ASCI Davidson guess.
> * **Recommendation**: Accurate excited states and rapid convergence of the ground state benefit from a good zero-order guess for the low energy spectrum. The default is often sufficient.

### `ASCI_SKIP_PT2`

> **Specifies whether ASCI PT2 correction should be calculated.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: compute ASCI PT2 contribution
>     * `TRUE`: do not compute ASCI PT2 contribution
> * **Recommendation**: The PT2 correction is essential to obtaining converged ASCI energies.

### `ASCI_RESTART`

> **Specifies whether to initialize the ASCI wave function with the wf_data file.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: read CI coefficients from the wf_data file
>     * `FALSE`: do not read the CI coefficients from disk
### `ASCI_SPIN_PURIFY`

> **Indicates whether or not the ASCI wave function should be augmented with missing determinants to ensure a spin-pure state.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: augment the wave function with determinants to ensure a spin eigenstate
>     * `FALSE`: do not augment the wave function
???+ example "Example 6.60: CASCI calculation for the lowest triplet ( $M_{s}=1$ ) state of N ${}_{2}$ . The adaptive
sampling method is employed to tackle a large active space (14e, 32o). The PT2
correction is performed on top of the ASCI wave function."
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.8
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvtz
       CAS_METHOD        1     !1 for CAS-CI, 2 for CASSCF
       CAS_M_S           2     !M_s value*2 (2: triplet)
       ASCI_DIAG         2     !Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC        14    !N_elec
       CAS_N_ORB         32    !N_orb
       CAS_N_ROOTS       1     !N_roots
       CAS_SOLVER        2     !2=ASCI, 1=Olsen, 0=naive
       ASCI_NDETS        28000 !Number of ASCI Determinants
       THRESH            14
       MAX_SCF_CYCLES    400
       SCF_CONVERGENCE   8
       MEM_TOTAL         4000
       MEM_STATIC        1000
       ROSCF             true
       SCF_ALGORITHM     diis_gdm
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "Example 6.61: ASCI-SCF (using adaptive sapling for CAS) calculation for the ground state of
N ${}_{2}$ with a large active space (14e, 32o). The PT2 correction is not performed
in this case."
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.8
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvtz
       CAS_METHOD        2  !1 for CAS-CI, 2 for CASSCF
       CAS_M_S           0  !M_s value*2
       ASCI_DIAG         2  !Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC        14 !N_elec
       CAS_N_ORB         32 !N_orb
       CAS_N_ROOTS       1 !N_roots
       CAS_SOLVER        2 !2=ASCI, 1=Olsen, 0=naive
       ASCI_NDETS        28000 !Number of ASCI Determinants
       ASCI_SKIP_PT2     1
       THRESH            14
       MAX_SCF_CYCLES    400
       SCF_CONVERGENCE   6
       MEM_TOTAL         4000
       MEM_STATIC        1000
       SCF_ALGORITHM     diis_gdm
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
