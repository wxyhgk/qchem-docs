---
title: "7.3.12 示例"
---

## 7.3.12 示例

（2026 年 7 月 4 日）

???+ example "示例 7.31: 本示例展示两个作业，分别请求含时密度泛函理论（Time-Dependent Density Functional Theory, TDDFT）计算的不同变体。第一个作业使用默认值 RPA = FALSE，在 Tamm-Dancoff 近似（Tamm-Dancoff Approximation, TDA）下执行 TDDFT 计算。第二个作业设置 RPA = TRUE，同时执行 TDA 和完整的 TDDFT 计算。"
    ```qchem
    $comment
       methyl peroxy radical
       TDDFT/TDA and full TDDFT with 6-31+G*
    $end
    
    $molecule
       0  2
       C  1.00412  -0.18045    0.00000
       O -0.24600   0.59615    0.00000
       O -1.31237  -0.23026    0.00000
       H  1.81077   0.56720    0.00000
       H  1.03665  -0.80545   -0.90480
       H  1.03665  -0.80545    0.90480
    $end
    
    $rem
       EXCHANGE          b
       CORRELATION       lyp
       CIS_N_ROOTS       5
       BASIS             6-31+G*
       SCF_CONVERGENCE   7
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       EXCHANGE          b
       CORRELATION       lyp
       CIS_N_ROOTS       5
       CIS_MAX_CYCLES    40
       RPA               true
       BASIS             6-31+G*
       SCF_CONVERGENCE   7
    $end
    ```

???+ example "示例 7.32: 本示例展示在缩减的激发空间中（仅包含定域在甲酰胺上的轨道）计算甲酰胺-水络合物激发态的过程。"
    ```qchem
    $comment
       formamide-water TDDFT/TDA in reduced excitation space
    $end
    
    $molecule
       0 1
       H  1.13  0.49 -0.75
       C  0.31  0.50 -0.03
       N -0.28 -0.71  0.08
       H -1.09 -0.75  0.67
       H  0.23 -1.62 -0.22
       O -0.21  1.51  0.47
       O -2.69  1.94 -0.59
       H -2.59  2.08 -1.53
       H -1.83  1.63 -0.30
    $end
    
    $rem
       EXCHANGE          b3lyp
       CIS_N_ROOTS       10
       BASIS             6-31++G**
       TRNSS             TRUE
       TRTYPE            1
       CUTOCC            60
       CUTVIR            40
       CISTR_PRINT       TRUE
       N_SOL             6
    $end
    
    $solute
    1
    2
    3
    4
    5
    6
    $end
    ```
