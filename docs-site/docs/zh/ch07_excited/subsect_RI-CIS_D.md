---
title: "7.8.7 RI-CIS(D)、SOS-CIS(D) 与 SOS-CIS(D 0)：作业控制与示例"
---

## 7.8.7 RI-CIS(D)、SOS-CIS(D) 与 SOS-CIS(D${}_{0}$)：作业控制与示例

（2026 年 7 月 4 日）

将 *$rem* 关键字 METHOD 分别设置为
RICIS(D)、SOSCIS(D) 和 SOSCIS(D0)，即可激活这些方法。
其余关键字与 [7.2.2 节](subsec_CIS.md)中介绍的 CIS 方法相同。由于这些方法依赖于
RI 近似，因此需要按照 RI-MP2（[6.6 节](../ch06_correlation/topic_rimp2.md)）中的相同指南来设置
AUX_BASIS。

### `METHOD`

> **所选的激发态方法**
>
> * **类型**: `STRING`
> * **默认值**: `None`
> * **可选值**:
>     * `RICIS(D)`: 激活 RI-CIS(D) SOSCIS(D) 激活 SOS-CIS(D) SOSCIS(D0) 激活 SOS-CIS(D ${}_{0}$ )
> * **建议**: 无

### `CIS_N_ROOTS`

> **设置要求解的激发态根数**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$: $n>0$ 求解
>     * $n$: 个激发态
> * **建议**: 无

### `CIS_SINGLETS`

> **求解单重激发态（对自旋非限制体系将被忽略）**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **可选值**:
>     * `TRUE`: 求解单重态
>     * `FALSE`: 不求解单重态。
> * **建议**: 无

### `CIS_TRIPLETS`

> **求解三重激发态（对自旋非限制体系将被忽略）**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **可选值**:
>     * `TRUE`: 求解三重态
>     * `FALSE`: 不求解三重态。
> * **建议**: 无

### `CIS_STATE_DERIV`

> **在使用 SOS-CIS(D ${}_{0}$ ) 进行几何优化和振动分析时，设置用于解析梯度计算的激发态索引**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$: 选择第
>     * $n$: 个态。
> * **建议**: 需检查在优化过程中各态的顺序是否发生变化。对于闭壳层体系，必须将 CIS_SINGLETS 或 CIS_TRIPLETS 之一设置为 false。

### `MEM_STATIC`

> **为各个程序模块设置内存**
>
> * **类型**: `INTEGER`
> * **默认值**: `192`
> * **可选值**:
>     * $n$: 用户自定义的内存大小（以兆字节计）。
> * **建议**: 至少需要 $150(N^{2}+N)D$（$N$：基函数数目，$D$：双精度存储单元的大小，通常为 8）。由于还需要存储若干大小为 $N^{2}$ 的矩阵，因此额外需要 32–160 MB 的内存。

### `MEM_TOTAL`

> **设置 Q-Chem 可用的总内存**
>
> * **类型**: `INTEGER`
> * **默认值**: `2000`
> * **可选值**:
>     * $n$: 用户自定义的内存大小（以兆字节计）
> * **建议**: RI-CIS(D) 的最低内存需求约为 MEM_STATIC + max $(3SVXD,3X^{2}D)$（$S$：激发态数目，$X$：辅助基函数数目，$D$：双精度存储单元的大小，通常为 8）。不过，由于 RI-CIS(D) 采用分批（batching）方案来高效计算电子排斥积分，指定更多内存会显著加快计算速度。如果不确定该使用多少，请尽可能多地分配内存，但绝不要超过实际可用的内存量。SOS-CIS(D) 和 SOS-CIS(D ${}_{0}$ ) 的最低内存需求约为 MEM_STATIC + $20X^{2}D$。当为 SOS-CIS(D ${}_{0}$ ) 梯度计算额外提供 $30X^{2}D$ 的内存空间时，其效率会更高。与 RI-CIS(D) 一样，如果不确定该使用多少，请尽可能多地分配内存。这些计算中实际使用的内存大小会打印在输出文件中，以便为所需内存提供参考。

### `SOS_FACTOR`

> **设置缩放参数 $c_{T}$**
>
> * **类型**: `INTEGER`
> * **默认值**: `1300000`
> * **可选值**:
>     * $n$: $c_{T}=n/1000000$
> * **建议**: 使用默认值

### `SOS_UFACTOR`

> **设置缩放参数 $c_{U}$**
>
> * **类型**: `INTEGER`
> * **默认值**: `151`
> * **可选值**:
>     * $n$: $c_{U}=n/100$
> * **建议**: 使用默认值

???+ example "示例 7.67: RI-CIS(D) 计算的输入。"
    ```qchem
    $molecule
       0 1
       C     0.667472     0.000000     0.000000
       C    -0.667472     0.000000     0.000000
       H     1.237553     0.922911     0.000000
       H     1.237553    -0.922911     0.000000
       H    -1.237553     0.922911     0.000000
       H    -1.237553    -0.922911     0.000000
    $end
    
    $rem
       METHOD          ricis(d)
       BASIS           aug-cc-pVDZ
       MEM_TOTAL       1000
       MEM_STATIC      100
       AO2MO_DISK      1000
       AUX_BASIS       rimp2-aug-cc-pVDZ
       PURECART        1111
       CIS_N_ROOTS     10
       CIS_SINGLETS    true
       CIS_TRIPLETS    false
    $end
    ```

???+ example "示例 7.68: SOS-CIS(D) 计算的输入。"
    ```qchem
    $molecule
       0 1
       C    -0.627782     0.141553     0.000000
       O     0.730618    -0.073475     0.000000
       H    -1.133677    -0.033018    -0.942848
       H    -1.133677    -0.033018     0.942848
    $end
    
    $rem
       METHOD          soscis(d)
       BASIS           aug-cc-pVDZ
       MEM_TOTAL       1000
       MEM_STATIC      100
       AO2MO_DISK      500000     ! 0.5 Terabyte of disk space available
       AUX_BASIS       rimp2-aug-cc-pVDZ
       PURECART        1111
       CIS_N_ROOTS     5
       CIS_SINGLETS    true
       CIS_TRIPLETS    true
    $end
    ```

???+ example "示例 7.69: 在 S ${}_{2}$ 面上进行 SOS-CIS(D ${}_{0}$ ) 几何优化的输入。"
    ```qchem
    $molecule
       0 1
       o
       h  1  r
       h  1  r  2  a
    
       r  0.95
       a  104.0
    $end
    
    $rem
       JOBTYPE           = opt
       METHOD            = soscis(d0)
       BASIS             = 6-31G**
       AUX_BASIS         = rimp2-VDZ
       PURECART          = 1112
       CIS_STATE_DERIV   = 2
       CIS_N_ROOTS       = 5
       CIS_SINGLETS      = true
       CIS_TRIPLETS      = false
    $end
    ```
