---
title: "7.9.28 势能面交叉最小化"
---

## 7.9.28 势能面交叉最小化

（2026 年 7 月 4 日）

EOM-CCSD 也可作为激发态方法用于寻找最小能量交叉点（Minimum Energy Crossing Points, MECPs）。关于 MECP 计算的更一般性信息，请参见第 [9.8.3](../ch09_opt/sect_MECP.md) 节。

势能面交叉优化过程用于寻找交叉 seam（交叉集）上的能量极小点。在 seam 上，势能面在垂直于由以下两个矢量所张成平面的子空间中是简并的：梯度差

<a id="Ch7.E125"></a>

$$
{\rm\bf g}=\frac{\partial}{\partial{\rm\bf q}}(E_{1}-E_{2}) \tag{7.125}
$$

以及导数耦合

<a id="Ch7.E126"></a>

$$
{\rm\bf h}=\left\langle\Psi_{1}\left|\frac{\partial{\rm\bf H}}{\partial{\rm\bf
q}}\right|\Psi_{2}\right\rangle \tag{7.126}
$$

目前 **Q-Chem** 无法为具有非零导数耦合的态定位交叉极小点。幸运的是，这种情况并不常见。不同多重度态的锥形交叉 seam 上的极小点可以找到，因为其导数耦合为零。不同点群对称性态的交叉 seam 上的极小点同样可以定位。

要运行势能面（PES）交叉最小化，必须分别采用 CCSD 和 EOM-CCSD 方法进行基态和激发态计算。

**注意：**

MECP 优化仅适用于具有解析梯度的方法。
无法通过有限差分方式计算两个梯度。
**

## 7.9.28.1 作业控制选项

**注意：**

在执行基于耦合簇（Coupled-Cluster）的 MECP 计算时，必须使用
XOPT_STATE_1 和 XOPT_STATE_2 关键字，而不能使用
MECP_STATE1 和 MECP_STATE2。
**

XOPT_STATE_1, XOPT_STATE_2

### `XOPT_STATE_1, XOPT_STATE_2`

> **指定将要搜索其交叉点的两个电子态。**
>
> * **类型**: `[INTEGER, INTEGER, INTEGER]`
> * **默认值**: `无默认值（必须指定该选项才能运行此计算）`
> * **选项**:
>     * [spin, irrep, state]
>     * spin = 0
>     * 处理低自旋（low spin）态，
>     * 另见 EE_SINGLETS 或 IP_STATES,EA_STATES。
>     * spin = 1
>     * 处理高自旋（high spin）态，
>     * 另见 EE_TRIPLETS。
>     * irrep
>     * 指定该态所属的不可约表示（irreducible representation）；例如，在
>     * $C_{2v}$
>     * 点群中，
>     * 不可约表示按 1、2、3、4 依次对应
>     * $A_{1}$
>     * 、
>     * $A_{2}$
>     * 、
>     * $B_{1}$
>     * 和
>     * $B_{2}$
>     * 。
>     * state
>     * 指定不可约表示内的态序号，state = 1 表示最低的激发
>     * 态，state = 2 表示第二激发态，
>     * 以此类推。
>     * .
>     * 0, 0, -1
>     * 基态。
> * **建议**: 目前只能计算自旋或对称性不同的态之间的交叉。

**注意：**

只有在使用闭壳层 RHF 参考时才能指定自旋。
对于开壳层参考，所有态被统一处理，另见
EE_STATES。例如，在自旋翻转（spin-flip）计算中，无论目标态的实际多重度为何，均使用 spin = 0。
**

XOPT_SEAM_ONLY

### `XOPT_SEAM_ONLY`

> **仅执行交叉 seam 搜索，不进行最小化。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 在交叉 seam 上找到一个点后即停止。
>     * FALSE
>     * 对交叉 seam 执行最小化。
> * **建议**: 对于自由度很多的体系，可以先将该选项设为 TRUE 以定位 seam，然后以该几何结构作为最小化的起始点，这可能很有用。

## 7.9.28.2 示例

???+ example "示例 7.164: 在 EOM-EE-CCSD 级别下优化 N ${}_{3}^{+}$ 离子的 Ã ${}^{1}$ B ${}_{2}$ 态与 B̃ ${}^{1}$ A ${}_{2}$ 态的交叉点。"
    ```qchem
    $molecule
       1 1
       N1
       N2 N1 rnn
       N3 N2 rnn N1 annn
    
       rnn=1.46
       annn=70.0
    $end
    
    $rem
       JOBTYPE                opt
       METHOD                 eom-ccsd
       BASIS                  6-31g
       EE_SINGLETS            [0,2,0,2]   C2v point group symmetry
       XOPT_STATE_1           [0,4,1]     1B2 low spin state
       XOPT_STATE_2           [0,2,2]     2A2 low spin state
       XOPT_SEAM_ONLY         true        Find the seam only
       GEOM_OPT_TOL_GRADIENT  100
    $end
    
    $opt
    CONSTRAINT                Set constraints on the N-N bond lengths
       stre  1  2  1.46
       stre  2  3  1.46
    ENDCONSTRAINT
    $end
    
    @@@
    
    $molecule
       READ
    $end
    
    $rem
       JOBTYPE                opt         Optimize the intersection seam
       METHOD                 eom-ccsd
       BASIS                  6-31g
       EE_SINGLETS            [0,2,0,2]
       XOPT_STATE_1           [0,4,1]
       XOPT_STATE_2           [0,2,2]
       GEOM_OPT_TOL_GRADIENT  30
       GEOM_OPT_DRIVER        optimize
    $end
    ```

???+ example "示例 7.165: 在 EOM-IP-CCSD 级别下优化 NO ${}_{2}$ 分子的 Ã ${}^{2}$ A ${}_{1}$ 态与 B̃ ${}^{2}$ B ${}_{1}$ 态的交叉点。"
    ```qchem
    $molecule
       -1  1
       N1
       O2  N1  rno
       O3  N1  rno  O2  aono
    
       rno  = 1.3040
       aono = 106.7
    $end
    
    $rem
       JOBTYPE                opt         Optimize the intersection seam
       UNRESTRICTED           true
       METHOD                 eom-ccsd
       N_FROZEN_CORE          0
       BASIS                  6-31g
       IP_STATES              [1,0,1,0]   C2v point group symmetry
       EOM_FAKE_IPEA          1
       XOPT_STATE_1           [0,1,1]     1A1 low spin state
       XOPT_STATE_2           [0,3,1]     1B1 low spin state
       GEOM_OPT_TOL_GRADIENT  30          Tighten gradient tolerance
       CCMAN2                 false
    $END
    ```
