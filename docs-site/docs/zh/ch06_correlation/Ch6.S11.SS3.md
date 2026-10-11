---
title: "6.11.3 示例"
---

## 6.11.3 示例

(2026 年 7 月 4 日)

???+ example "示例 6.28：将使用 RHF 轨道的 RI-MP3 应用于水二聚体。"
    ```qchem
    $molecule
       0  1
       O   -2.766559    0.187083    0.566918
       H   -3.696304    1.179189   -0.642507
       H   -3.395838   -1.509891    0.389284
       O    2.587035    0.275900   -0.746442
       H    3.579141    0.918407    0.633058
       H    0.852266    0.311805   -0.156847
    $end
    
    $rem
       METHOD            RIMP3
       BASIS             cc-pvdz
       UNRESTRICTED      false
       AUX_BASIS_CORR    rimp2-cc-pvdz
       THRESH            14
       INPUT_BOHR        true
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     gdm
       MAXSCF            1000
       INTEGRAL_SYMMETRY false
    $end
    ```

???+ example "示例 6.29：将使用 BLYP 轨道的标度 RI-MP3（RI-MP2.5）应用于水-氨二聚体。"
    ```qchem
    $molecule
       0  1
       O    0.0000000000 -0.0578657100 -1.4797930300
       H    0.0000000000  0.8229338400 -1.8554147400
       H    0.0000000000  0.0794956700 -0.5193425300
       N    0.0000000000  0.0143639400  1.4645462800
       H    0.0000000000 -0.9810485700  1.6534477900
       H   -0.8134835100  0.3987677600  1.9293404900
       H    0.8134835100  0.3987677600  1.9293404900
    $end
    
    $rem
       METHOD               blyp
       BASIS                cc-pvdz
       UNRESTRICTED         false
       THRESH               14
       SCF_CONVERGENCE      8
       SCF_ALGORITHM        gdm
       MAXSCF               1000
       GEN_SCFMAN           true
       GEN_SCFMAN_FINAL     true
       INTEGRAL_SYMMETRY    false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       CORRELATION          rimp3
       BASIS                cc-pvdz
       AUX_BASIS_CORR       rimp2-cc-pvdz
       UNRESTRICTED         false
       THRESH               14
       SCF_CONVERGENCE      8
       MAXSCF               0
       SCF_GUESS            read
       MP2_RESTART_NO_SCF   true
       SKIP_SCFMAN          true
       SCF_ALGORITHM        diis
       INTEGRAL_SYMMETRY    false
       GEN_SCFMAN           false   ! forces HF Fock build and energy evaluation
       GEN_SCFMAN_FINAL     false   ! forces HF Fock build and energy evaluation
       MP2_SCALING          1000000 ! 1.0
       MP3_SCALING          500000  ! 0.5
    $end
    ```

???+ example "示例 6.30：将使用 $\kappa$ -OOMP2 轨道的标度 RI-MP3（RI-MP2.8）应用于氟化氢二聚体。"
    ```qchem
    $molecule
       0  1
       H    0.0000000000    0.8026798200    1.6952932900
       F    0.0000000000   -0.0459666600    1.3403481800
       H    0.0000000000   -0.1204078700   -0.4908284000
       F    0.0000000000    0.0097694500   -1.4042497800
    $end
    
    $rem
       EXCHANGE             hf
       BASIS                cc-pvdz
       UNRESTRICTED         false
       AUX_BASIS_CORR       rimp2-cc-pvdz
       DO_O2                3
       REGULARIZED_O2       2
       REG_VARIABLE         1450
       THRESH               14
       SCF_CONVERGENCE      8
       SCF_ALGORITHM        gdm
       MAXSCF               1000
       GEN_SCFMAN           true
       GEN_SCFMAN_FINAL     true
       INTEGRAL_SYMMETRY    false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       CORRELATION          rimp3
       BASIS                cc-pvdz
       UNRESTRICTED         false
       AUX_BASIS_CORR       rimp2-cc-pvdz
       THRESH               14
       SCF_CONVERGENCE      8
       MAXSCF               0
       SCF_GUESS            read    ! read in k-OOMP2 orbitals
       MP2_RESTART_NO_SCF   true
       SKIP_SCFMAN          true
       SCF_ALGORITHM        diis
       INTEGRAL_SYMMETRY    false
       GEN_SCFMAN           false   ! forces HF Fock build and energy evaluation
       GEN_SCFMAN_FINAL     false   ! forces HF Fock build and energy evaluation
       MP2_SCALING          1000000 ! 1.0
       MP3_SCALING          800000  ! 0.8
    $end
    ```
