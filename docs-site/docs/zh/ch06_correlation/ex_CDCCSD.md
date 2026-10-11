---
title: "6.12.13 示例"
---

## 6.12.13 示例

(2026 年 7 月 4 日)

???+ example "示例 6.34: 一系列作业，使用三种耦合簇单双激发（coupled-cluster singles and doubles）类型方法计算 NH ${}_{2}$ 自由基基态的相关能（冻结核心轨道）：CCSD 本身、CC2、OD 和 QCCD。"
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

???+ example "示例 6.35: 单点 CCSDT 能量计算作业，对象为水分子（冻结核心轨道）"
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

???+ example "示例 6.36: 使用 RI-CCSD 计算水分子 CCSD 能量的作业"
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

???+ example "示例 6.37: 计算水分子 RI-CC2 能量的作业"
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

???+ example "示例 6.38: 使用 CD-CCSD 计算水分子 CCSD 能量的作业（容差 = $10^{-3}$）"
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

???+ example "示例 6.39: 使用 CD-CCSD（容差 = $10^{-3}$）结合 FNO 计算水分子 CCSD 能量的作业"
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

???+ example "示例 6.40: 使用两步（two-step）和一步（one-step）Cholesky 分解算法进行 CD-CCSD 几何优化"
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

???+ example "示例 6.41: 计算甲醛（formaldehyde）BWs-CC2 能量的作业，其中 $\alpha=1$"
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

???+ example "示例 6.42: 使用 MPR-BWs2 分区（partitioning）计算甲醛 BWs-CC2 能量的作业，其中 $A_{0}=1$ 且 $B_{0}=-1$。"
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
