---
title: "6.10.2 dRPA 作业控制"
---

## 6.10.2 dRPA 作业控制

（2026 年 7 月 4 日）

### `CLENSHAW_NGRID`

> **用于 Curtis-Clenshaw 求积的网格点数目。**
>
> * **类型**：`INTEGER`
> * **默认值**：`40`
> * **建议**：使用默认值。

???+ example "示例 6.27：采用 RHF 轨道的 RI-DRPA 应用于水二聚体"
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
       METHOD            RIDRPA
       BASIS             cc-pvdz
       AUX_BASIS_CORR    rimp2-cc-pvdz
       UNRESTRICTED      false
       THRESH            14
       INPUT_BOHR        true
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     gdm
       MAXSCF            1000
       SCF_GUESS         gdm
       MAXSCF            1000
       SCF_GUESS         1000
    $end
    ```
