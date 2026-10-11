---
title: "6.12.13 Examples"
---

## 6.12.13 Examples

(July 4, 2026)

???+ example "Example 6.34: A series of jobs evaluating the correlation energy (with core orbitals frozen)
of the ground state of the NH ${}_{2}$ radical with three methods of
coupled-cluster singles and doubles type: CCSD itself, CC2, OD, and QCCD."
    ```qchem
    $molecule
       0  2
       N
       H1  N  1.02805
       H2  N  1.02805  H1  103.34
    $end
    
    $rem
       METHOD          ccsd
       BASIS           6-31g*
       N_FROZEN_CORE   fc
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD          cc2
       BASIS           6-31g*
       N_FROZEN_CORE   fc
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD          od
       BASIS           6-31g*
       N_FROZEN_CORE   fc
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD          qccd
       BASIS           6-31g*
       N_FROZEN_CORE   fc
    $end
    ```

???+ example "Example 6.35: A job for single point CCSDT energy of water with (core orbitals frozen)"
    ```qchem
    $molecule
    0 1
    O
    H 1 R1
    H 1 R1 2 A
    
    R1=1.0
    A=104.0
    $end
    
    $rem
       BASIS  =  cc-pVDZ
       METHOD  =  CCSDT
       N_FROZEN_CORE FC
    $end
    ```

???+ example "Example 6.36: A job evaluating CCSD energy of water using RI-CCSD"
    ```qchem
    $molecule
      0 1
      O
      H1 O OH
      H2 O OH H1 HOH
    
      OH  = 0.947
      HOH = 105.5
    $end
    
    $rem
       METHOD          ccsd
       BASIS           aug-cc-pvdz
       AUX_BASIS       rimp2-aug-cc-pvdz
    $end
    ```

???+ example "Example 6.37: A job evaluating the RI-CC2 energy of water"
    ```qchem
    $molecule
      0 1
      O
      H1 O OH
      H2 O OH H1 HOH
    
      OH  = 0.947
      HOH = 105.5
    $end
    
    $rem
       METHOD          cc2
       BASIS           aug-cc-pvdz
       AUX_BASIS       rimp2-aug-cc-pvdz
    $end
    ```

???+ example "Example 6.38: A job evaluating CCSD energy of water using CD-CCSD (tolerance = $10^{-3}$ )"
    ```qchem
    $molecule
      0 1
      O
      H1 O OH
      H2 O OH H1 HOH
    
      OH  = 0.947
      HOH = 105.5
    $end
    
    $rem
       METHOD          ccsd
       BASIS           aug-cc-pvdz
       CHOLESKY_TOL    3
    $end
    ```

???+ example "Example 6.39: A job evaluating CCSD energy of water using CD-CCSD (tolerance = $10^{-3}$ )
with FNO"
    ```qchem
    $comment
    CCSD energy with Cholesky and FNO
    $end
    
    $molecule
       0 1
       O
       H1 O OH
       H2 O OH H1 HOH
    
       OH  = 0.947
       HOH = 105.5
    $end
    
    $rem
       METHOD          ccsd
       BASIS           aug-cc-pvdz
       CHOLESKY_TOL    3
       CC_FNO_THRESH   9950
    $end
    ```

???+ example "Example 6.40: CD-CCSD geometry optimization with two-step and one-step Cholesky decomposition algorithm"
    ```qchem
    $comment
    Water optimization with CCSD and two-step Cholesky decomposition using default two-step algorithm and a tight span factor
    $end
    
    $molecule
    0 1
    H       0.7948652144     0.0000000000     0.4759723739
    O       0.0000000000     0.0000000000    -0.0900186824
    H      -0.7948652144     0.0000000000     0.4759723739
    $end
    
    $rem
      job_type =opt
      method = ccsd
      basis = 6-31G
      n_frozen_core = 0
      symmetry = On
      CHOLESKY_TOL=5        ! tolerance
      CD_TS_SPAN_FACTOR=3   !span factor to select diagonals
    $end
    
    @@@
    $comment
    Water optimization with CCSD and two-step Cholesky decomposition using old decomposition algorithm
    $end
    
    $molecule
    0 1
    H       0.7948652144     0.0000000000     0.4759723739
    O       0.0000000000     0.0000000000    -0.0900186824
    H      -0.7948652144     0.0000000000     0.4759723739
    $end
    
    $rem
      job_type =opt
      method = ccsd
      basis = 6-31G
      n_frozen_core = 0
      symmetry = On
      CHOLESKY_TOL=5        ! tolerance
      cholesky_twostep =false   !use olf algorithm
    $end
    ```

???+ example "Example 6.41: A job evaluating the BWs-CC2 energy of formaldehyde with $\alpha=1$"
    ```qchem
    $molecule
    0 1
    C   0.0000      0.0000      0.0000
    O   0.0000      0.0000     -1.2195
    H   0.9391      0.0000      0.5422
    H  -0.9391      0.0000      0.5422
    $end
    
    $rem
    JOBTYPE             SP
    METHOD              RIBWS2              ! activate RI-BWS2 driver
    BASIS               DEF2-SVP
    AUX_BASIS           RIMP2-DEF2-SVP      ! auxilliary basis is required
    SYM_IGNORE          TRUE
    SYMMETRY            FALSE
    $end
    
    $bws2
    METHOD              BWS2                ! Use BW-s2 partition
    EXC_METHOD          CC2                 ! Do a subsequent BWs-CC2 calculation
    ALPHA               1000                ! a = 1.0
    MAX_CYCLES          50
    $end
    ```

???+ example "Example 6.42: A job evaluating the BWs-CC2 energy of formaldehyde using the MPR-BWs2
partitioning with $A_{0}=1$ and $B_{0}=-1$ ."
    ```qchem
    $molecule
    0 1
    C   0.0000      0.0000      0.0000
    O   0.0000      0.0000     -1.2195
    H   0.9391      0.0000      0.5422
    H  -0.9391      0.0000      0.5422
    $end
    
    $rem
    JOBTYPE             SP
    METHOD              RIBWS2              ! activate RI-BWS2 driver
    BASIS               DEF2-SVP
    AUX_BASIS           RIMP2-DEF2-SVP      ! auxilliary basis is required
    SYM_IGNORE          TRUE
    SYMMETRY            FALSE
    $end
    
    $bws2
    METHOD              MPR-BWS2            ! Use MPR-BWs2 partition
    EXC_METHOD          CC2                 ! Do a subsequent BWs-CC2 calculation
    MPR_A0              1000                ! A_0 = 1.0
    MPR_B0              -1000               ! B_0 = -1.0
    MAX_CYCLES          50
    $end
    ```
