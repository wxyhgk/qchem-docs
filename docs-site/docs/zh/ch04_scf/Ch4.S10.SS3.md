---
title: "4.10.3 示例"
---

## 4.10.3 示例

（2026 年 7 月 4 日）

???+ example "示例 4.30: xTB 单点能计算。"
    ```qchem
    $molecule
    0 1
    Li      0.0000000000    0.0000000000    0.0000000000
    H       0.0000000000    0.0000000000    1.6000000000
    $end
    
    $rem
    JOBTYPE           SP
    METHOD            XTB
    SCF_ALGORITHM     DIIS
    SCF_CONVERGENCE   6
    $end
    ```

???+ example "示例 4.31: xTB 几何优化。"
    ```qchem
    $molecule
    0  1
    H      -1.21420     3.05899     0
    Li     -2.89084     3.09033     0
    $end
    
    $rem
    JOBTYPE           OPT
    METHOD            XTB
    BASIS             XTB
    SCF_ALGORITHM     DIIS
    SCF_CONVERGENCE   5
    XTB_FERMI_TEMP    300
    $end
    ```
