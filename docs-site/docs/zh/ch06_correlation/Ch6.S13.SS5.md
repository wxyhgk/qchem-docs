---
title: "6.13.5 示例"
---

## 6.13.5 示例

（2026 年 7 月 4 日）

???+ example "示例 6.43: 两个任务，分别使用标准的 CCSD(T) 方法与新的 CCSD(2) 近似方法计算相关能（correlation energy）并进行比较，二者均采用冻结芯（frozen core）近似。这要求在 CCSD(2) 的输入中将 CC_INCL_CORE_CORR 指定为 FALSE。"
    ```qchem
    $molecule
       0  2
       O
       H  O  0.97907
    $end
    
    $rem
       METHOD          ccsd(t)
       BASIS           cc-pvtz
       N_FROZEN_CORE   fc
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD              ccsd(2)
       BASIS               cc-pvtz
       N_FROZEN_CORE       fc
       CC_INCL_CORE_CORR   false
    $end
    ```

???+ example "示例 6.44: 使用 libpt 进行标准的 CCSD(T) 计算"
    ```qchem
    $molecule
       0  2
       O
       H  O  0.97907
    $end
    
    $rem
       METHOD          ccsd(t)
       BASIS           cc-pvtz
       N_FROZEN_CORE   fc
       USE_LIBPT       true
    $end
    ```
