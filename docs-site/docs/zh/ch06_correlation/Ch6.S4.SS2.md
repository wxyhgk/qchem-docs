---
title: "6.4.2 算法控制与自定义"
---

## 6.4.2 算法控制与自定义

(July 4, 2026)

**Q-Chem** 所使用的直接（direct）与半直接（semi-direct）积分变换算法（*e.g.*, MP2, CIS(D)）受可用磁盘空间 $D$、内存 $C$、基函数（basis function）数目 $N$、虚轨道（virtual orbital）数目 $V$ 以及占据轨道（occupied orbital）数目 $O$ 的限制，如前文所述。关键 *$rem* 变量的通用说明如下：

### `MEM_STATIC`

> **设置 Fortran AO 积分计算与变换模块所使用的内存。**
>
> * **类型**: `INTEGER`
> * **默认值**: `192`
> * **选项**:
>     * $n$: 用户自定义的兆字节（MB）数。
> * **建议**: 对于直接和半直接 MP2 计算，该值必须超过 OVN 加上 AO 积分评估所需的内存（32–160 MB），如前文所述。

### `MEM_TOTAL`

> **设置 Q-Chem 可用的总内存，以兆字节（MB）为单位。**
>
> * **类型**: `INTEGER`
> * **默认值**: `2000`
> * **选项**:
>     * $n$: 用户自定义的兆字节（MB）数。
> * **建议**: 使用默认值，或设置为机器的物理内存。注意，如果 CCMAN 作业的内存分配总量超过 1 GB，则内存按如下方式分配：12% MEM_STATIC，50% CC_MEMORY，35% 其他内存需求：

### `CD_ALGORITHM`

> **决定 MP2 积分变换的算法。**
>
> * **类型**: `STRING`
> * **默认值**: `由程序确定。`
> * **选项**:
>     * `DIRECT`: 使用完全直接算法（仅计算能量）。
>     * `SEMI_DIRECT`: 使用基于磁盘的半直接算法。
>     * `LOCAL_OCCUPIED`: 备选能量算法（参见 6.4.1）。
> * **建议**: 半直接算法通常效率最高，一般情况下会被默认选择。

???+ example "示例 6.1: 采用冻结芯层近似（frozen core approximation）的 MP2/6-31G* 计算示例。注意 EXCHANGE $rem 变量将默认为 HF"
    ```qchem
    $molecule
       0 1
       O
       H1  O  oh
       H2  O  oh  H1  hoh
    
       oh  = 1.01
       hoh = 105
    $end
    
    $rem
       METHOD          mp2
       BASIS           6-31g*
       N_FROZEN_CORE   fc
    $end
    ```
