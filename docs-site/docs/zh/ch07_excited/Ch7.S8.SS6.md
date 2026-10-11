---
title: "7.8.6 CIS(D) 作业控制与示例"
---

## 7.8.6 CIS(D) 作业控制与示例

（2026 年 7 月 4 日）

**Q-Chem** 中的传统（legacy）CIS(D) 算法由 **Q-Chem** 的 CCMAN/CCMAN2 模块处理，并共享许多 *$rem* 选项。RI-CIS(D)、SOS-CIS(D) 和 SOS-CIS(D${}_{0}$) 不依赖于耦合簇程序例程。不使用此传统 CIS(D) 方法的用户可直接跳至第 [7.8.7](subsect_RI-CIS_D.md) 节。

与所有 post-HF（后 Hartree-Fock）计算一样，确保有足够的资源用于必要的积分计算和积分变换至关重要。对于 CIS(D)，这些资源通过 *$rem* 变量 CC_MEMORY、MEM_STATIC 和 MEM_TOTAL 控制（参见第 [6.12.12](../ch06_correlation/sec_CCcontrols.md) 节）。

要请求 CIS(D) 计算，应将 METHOD *$rem* 变量设置为 CIS(D)，并通过 EE_STATES（或在适当情况下使用 EE_SINGLETS 和 EE_TRIPLETS）指定要计算的激发态数目。或者，当 EXCHANGE = HF、CORRELATION = CI 且 EOM_CORR = CIS(D) 时也会执行 CIS(D)。SF-CIS(D) 通过使用 SF_STATES 调用。

EE_STATES

### `EE_STATES`

> **设置要查找的激发态根（roots）数目。对于闭壳层参考态，默认归入 EE_SINGLETS。对于开壳层参考态，指定所有低能态。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示（irrep）中查找
>     * $i$
>     * 个激发态，
>     * 在第二个不可约表示中查找
>     * $j$
>     * 个态，
>     * 依此类推。
> * **建议**：无

EE_SINGLETS

### `EE_SINGLETS`

> **设置要查找的单重态（singlet）激发态根数目。仅对闭壳层参考态有效。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中查找
>     * $i$
>     * 个激发态，
>     * 在第二个不可约表示中查找
>     * $j$
>     * 个态，
>     * 依此类推。
> * **建议**：无

EE_TRIPLETS

### `EE_TRIPLETS`

> **设置要查找的三重态（triplet）激发态根数目。仅对闭壳层参考态有效。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中查找
>     * $i$
>     * 个激发态，
>     * 在第二个不可约表示中查找
>     * $j$
>     * 个态，
>     * 依此类推。
> * **建议**：无

SF_STATES

### `SF_STATES`

> **设置要查找的自旋翻转（spin-flip）目标态根数目。**
>
> * **类型**：`INTEGER/INTEGER ARRAY`
> * **默认值**：`0`
> * **选项**：
>     * $[i,j,k\ldots]$
>     * 在第一个不可约表示中查找
>     * $i$
>     * 个 SF 态，
>     * 在第二个不可约表示中查找
>     * $j$
>     * 个态，
>     * 依此类推。
> * **建议**：无

**注意：**

在激发态计算中，指定的是*跃迁（transition）*的对称性，而非*目标态（target state）*的对称性。目标态的对称性等于参考态对称性与跃迁对称性的直积。对于闭壳层分子，参考态是全对称的，因此目标态的对称性与跃迁的对称性相同；但对于开壳层参考态，情况则并非如此。
**

CC_STATE_TO_OPT

### `CC_STATE_TO_OPT`

> **指定要优化哪个态。**
>
> * **类型**：`INTEGER ARRAY`
> * **默认值**：`None`
> * **选项**：
>     * [
>     * $i$
>     * ,
>     * $j$
>     * ]
>     * 优化第
>     * $i$
>     * 个不可约表示中的第
>     * $j$
>     * 个态。
> * **建议**：无

**注意：**

由于 CIS(D) 没有解析梯度，在进行几何优化和频率计算时应关闭对称性，并且在假设 $C_{1}$ 对称性的前提下指定 CC_STATE_TO_OPT，*即*写为 [1,N]，其中 N 为要优化的态的编号（态从 1 开始编号）。
**

???+ example "示例 7.64: 在实验测得的基态几何构型（$C_{2v}$ 对称性）下，臭氧的 CIS(D) 激发能计算"
    ```qchem
    $molecule
       0 1
       O
       O  1  RE
       O  2  RE  1  A
    
       RE = 1.272
       A  = 116.8
    $end
    
    $rem
       METHOD           CIS(D)
       BASIS            6-31G*
       N_FROZEN_CORE    3            use frozen core
       EE_SINGLETS      [2,2,2,2]    find 2 lowest singlets in each irrep.
       EE_TRIPLETS      [2,2,2,2]    find 2 lowest triplets in each irrep.
       CCMAN2           false
    $end
    ```

???+ example "示例 7.65: 水的最低三重态的 CIS(D) 几何优化。对于有限差分计算，对称性会被自动关闭"
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
       JOBTYPE            opt
       BASIS              3-21g
       METHOD             cis(d)
       EE_TRIPLETS        1  calculate one lowest triplet
       CC_STATE_TO_OPT    [1,1] optimize the lowest state (1st state in 1st irrep)
    $end
    ```

???+ example "示例 7.66: 在实验测得的基态几何构型（$C_{2v}$ 对称性）下，臭氧的 CIS(D) 激发能与跃迁性质计算（在所有态之间）"
    ```qchem
    $molecule
       0 1
       O
       O  1  RE
       O  2  RE  1  A
    
       RE = 1.272
       A  = 116.8
    $end
    
    $rem
       BASIS              6-31G*
       PURCAR             2            Non-spherical (6D)
       METHOD             CIS(D)
       EE_SINGLETS        [2,2,2,2]
       EE_TRIPLETS        [2,2,2,2]
       CC_TRANS_PROP      1
       CCMAN2             FALSE
    $end
    ```
