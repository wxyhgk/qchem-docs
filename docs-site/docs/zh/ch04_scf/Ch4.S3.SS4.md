---
title: "4.3.4 示例"
---

## 4.3.4 示例

（2026 年 7 月 4 日）

以下给出了运行基态 HF（Hartree-Fock，哈特里-福克）单点能计算的 **Q-Chem** 输入文件示例。

???+ example "示例 4.2: 水分子单点能计算的 Q-Chem 输入示例。注意，单点能的 $rem 变量声明是多余的，因为它与 Q-Chem 的默认设置相同。"
    ```qchem
    $molecule
       0  1
       O
       H1  O  oh
       H2  O  oh  H1  hoh
    
       oh  =   1.2
       hoh = 120.0
    $end
    
    $rem
       JOBTYPE       sp       Single Point energy
       METHOD        hf       Hartree-Fock
       BASIS         sto-3g   Basis set
    $end
    ```

???+ example "示例 4.3: Li 原子的 UHF/6-311G 计算。注意，此处没有指明相关方法和作业类型，因为 Q-Chem 会自动默认为不包含相关校正的单点能计算。另外，由于 $\alpha$ 电子数与 $\beta$ 电子数不相等，分子轨道（MOs）默认采用非限制形式（unrestricted formalism）。"
    ```qchem
    $molecule
       0,2
       Li
    $end
    
    $rem
       METHOD     HF       Hartree-Fock
       BASIS      6-311G   Basis set
    $end
    ```

???+ example "示例 4.4: 锂原子的 ROHF/6-311G 计算。"
    ```qchem
    $molecule
       0,2
       3
    $end
    
    $rem
       METHOD         hf       Hartree-Fock
       UNRESTRICTED   false    Restricted MOs
       BASIS          6-311G   Basis set
    $end
    ```
