---
title: "6.21.4 示例"
---

## 6.21.4 示例

(2026 年 7 月 4 日)

???+ example "示例 6.6.59: 三重态乙烯的 iFCI $n=2$ 计算。使用 PP 三重态作为参考。"
    ```qchem
    $molecule
       0 1
       C         0.0000000000    0.0000000000    0.0020303630
       C         0.0000000000    0.0000000000    1.3369696370
       H         0.9228964204    0.0000000000   -0.5679991115
       H        -0.9228964204    0.0000000000   -0.5679991115
       H         0.9228964204    0.0000000000    1.9069991115
       H        -0.9228964204    0.0000000000    1.9069991115
    $end
    
    $rem
       METHOD               hf
       BASIS                6-31G*
       SCF_ALGORITHM        rca_diis
       INTEGRAL_SYMMETRY    off
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       0 3
       read
    $end
    
    $rem
       EXCHANGE             HF
       CORRELATION          CCVB
       CCVB_METHOD          4
       GVB_RESTART          0
       GVB_ORB_CONV         6
       BASIS                6-31G*
       UNRESTRICTED         false
       SCF_GUESS            read
       INTEGRAL_SYMMETRY    off
       POINT_GROUP_SYMMETRY false
       GEN_SCFMAN           false  !works only with this setting
    $end
    
    @@@
    
    $molecule
       0 1
       read
    $end
    
    $rem
       EXCHANGE             HF
       CORRELATION          IFCI
       BASIS                6-31G*
       AUX_BASIS            RIMP2-VDZ
       IFCI_TUPLES          2
       IFCI_READ            0
       IFCI_TRIPLETS        1
       IFCI_ZETA            55
       HBCI_EPS1            1000
       IFCI_REF_ITER        0
    $end
    ```
