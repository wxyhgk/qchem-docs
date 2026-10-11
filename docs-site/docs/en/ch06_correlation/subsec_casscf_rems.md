---
title: "6.20.2 CAS-CI and CASSCF Job Control Options"
---

## 6.20.2 CAS-CI and CASSCF Job Control Options

(July 4, 2026)

CAS_METHOD

### `CAS_METHOD`

> **Indicates whether orbital optimization is requested.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Not running a CAS calculation
>     * 1
>     * CAS-CI (no orbital optimization)
>     * 2
>     * CASSCF (orbital optimization)
> * **Recommendation**: Use 2 for best accuracy, but such computations may become infeasible for large active spaces.

CAS_M_S

### `CAS_M_S`

> **The number of unpaired electrons desired in the CAS wave function.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $N$
>     * for a wave function with
>     * $N$
>     * unpaired electrons

CAS_N_ELEC

### `CAS_N_ELEC`

> **Specifies the number of active electrons.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $N$
>     * include
>     * $N$
>     * electrons in the active space
>     * -1
>     * include all electrons in the active space
> * **Recommendation**: Use the smallest active space possible for the given system.

CAS_N_ORB

### `CAS_N_ORB`

> **Specifies the number of active orbitals.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $N$
>     * include
>     * $N$
>     * orbitals in the active space
>     * -1
>     * include all orbitals in the active space
> * **Recommendation**: Use the smallest active space possible for the given system.

CAS_N_ROOTS

### `CAS_N_ROOTS`

> **Specifies the number of electronic states to determine.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * $N$
>     * solve for
>     * $N$
>     * roots of the Hamiltonian

CAS_THRESH

### `CAS_THRESH`

> **Specifies the threshold for matrix elements to be included in the CAS Hamiltonian.**
>
> * **Type**: `INTEGER`
> * **Default**: `12`
> * **Options**:
>     * $N$
>     * for a threshold of
>     * $10^{-N}$

CAS_SAVE_NAT_ORBS

### `CAS_SAVE_NAT_ORBS`

> **Save the CAS natural orbitals in place of the reference orbitals.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * overwrite the reference orbitals with CAS natural orbitals
>     * FALSE
>     * do not save the CAS natural orbitals

MAX_CASSCF_CYCLES

### `MAX_CASSCF_CYCLES`

> **Maximum number of orbital optimization cycles for CASSCF.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $N$
>     * set maximum number of optimization cycles to
>     * $N$

CAS_USE_RI

### `CAS_USE_RI`

> **Indicates whether the resolution of the identity approximation should be used.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Compute 2-electron integrals analytically
>     * TRUE
>     * Use the RI approximation for 2-electron integrals
> * **Recommendation**: Analytic integrals are more accurate, RI integrals are faster

CAS_DAVIDSON_TOL

### `CAS_DAVIDSON_TOL`

> **Specifies the tolerance for the Davidson solver used in CAS.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $N$
>     * for a threshold of
>     * $10^{-N}$
> * **Recommendation**: The default should be suitable in most cases

CAS_DAVIDSON_MAXVECTORS

### `CAS_DAVIDSON_MAXVECTORS`

> **Specifies the maximum number of vectors to augment the Davidson search space in CAS.**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * $N$
>     * sets the maximum Davidson subspace size to
>     * $N$
>     * +
>     * CAS_N_ROOTS
> * **Recommendation**: The default should be suitable in most cases

CAS_SOLVER

### `CAS_SOLVER`

> **Specifies the solver to be used for the active space.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 1
>     * CAS-CI/CASSCF
>     * 2
>     * ASCI (see Section
>     * 6.22
>     * )
>     * 3
>     * Truncated CI (CIS, CISD, CISDT, etc.)

TRUNC_CI_LEVEL

### `TRUNC_CI_LEVEL`

> **Specifies the order of truncated CI to be used in the active space.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not carry out truncated CI
>     * 1
>     * CIS
>     * 2
>     * CISD
>     * 3
>     * CISDT
>     * 4
>     * CISDTQ
>     * etc.

???+ example "Example 6.55: CASCI(6,14) calculation for the ground state of N ${}_{2}$ ."
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.8
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvtz
       CAS_METHOD        1    ! 1 for CAS-CI, 2 for CASSCF
       CAS_M_S           0    ! M_s value*2
       ASCI_DIAG         2    ! Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC        6    ! N_elec
       CAS_N_ORB         14   ! N_orb
       CAS_N_ROOTS       1    ! N_roots
       CAS_SOLVER        1    ! 2=ASCI, 1=Olsen, 0=naive
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

???+ example "Example 6.56: CASSCF(6,6) calculation for the ground state of N ${}_{2}$ ."
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.8
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvtz
       CAS_METHOD        2    !1 for CAS-CI, 2 for CASSCF
       CAS_M_S           0    !M_s value*2
       ASCI_DIAG         2    !Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC        6    !N_elec
       CAS_N_ORB         6    !N_orb
       CAS_N_ROOTS       1    !N_roots
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

???+ example "Example 6.57: Geometry optimization of the ground state of N ${}_{2}$ at the
CASSCF(6,6)/cc-pVTZ level of theory."
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.3
    $end
    
    $rem
       JOBTYPE              opt
       EXCHANGE             hf
       BASIS                cc-pvtz
       CAS_METHOD           2    !1 for CAS-CI, 2 for CASSCF
       CAS_M_S              0    !M_s value*2
       ASCI_DIAG            2    !Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC           6    !N_elec
       CAS_N_ORB            6    !N_orb
       CAS_N_ROOTS          1    !N_roots
       CAS_SAVE_NAT_ORBS    true !overwrite MOs with CAS natural orbs
       THRESH               14
       MAX_SCF_CYCLES       400
       SCF_CONVERGENCE      6
       MEM_TOTAL            4000
       MEM_STATIC           1000
       SCF_ALGORITHM        diis_gdm
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "Example 6.58: Truncated CI (S, D, T) calculation for the ground state N ${}_{2}$ using the CASCI routines."
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.1
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvdz
       CAS_METHOD        1   !1 for CAS-CI, 2 for CASSCF
       CAS_M_S           0   !M_s value*2
       ASCI_DIAG         2   !Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC        6   !N_elec
       CAS_N_ORB        -1   !N_orb (-1: include all orbitals in active space)
       CAS_N_ROOTS       1   !N_roots
       CAS_SOLVER        3   !2=ASCI, 1=Olsen, 0=naive, 3=truncated CI
       TRUNC_CI_LEVEL    3   !include up to triples excitations
       THRESH            14
       MAX_SCF_CYCLES    400
       SCF_CONVERGENCE   6
       MEM_TOTAL         4000
       MEM_STATIC        1000
       SCF_ALGORITHM     diis_gdm
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    ```
