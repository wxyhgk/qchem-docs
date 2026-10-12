---
title: "9.4.3 冻结原子（Frozen Atoms）"
---

## 9.4.3 冻结原子（Frozen Atoms）

（2026 年 7 月 4 日）

原子的绝对位置可以通过 *FIXED* 区段（section）来冻结。该区段以 *FIXED* 关键字作为首行开始，以末行的 *ENDFIXED* 关键字结束。冻结某个原子的一个或多个坐标的格式为：

`atom    coordinate_reference`

*coordinate_reference* 可以是 $X$、$Y$、$Z$ 至多三个字符的任意组合，用于指定要冻结的坐标：$X$、$Y$、$Z$、*XY*、*XZ*、*YZ*、*XYZ*。用于指定冻结方向的字符必须紧邻排列。*例如*，

> ```qchem
> FIXED
> 2 XY
> ENDFIXED
> ```

表示冻结原子 2 的 $x$ 坐标和 $y$ 坐标，而

> ```qchem
> FIXED
> 2 X Y
> ENDFIXED
> ```

则会产生错误的结果。

**注意：

当在 *$opt* 中指定 *FIXED* 区段时，几何优化将在笛卡尔坐标（Cartesian coordinates）下进行。
**

请注意，对于带有冻结原子约束的体系，*频率（frequency）* 计算通常会产生虚频（imaginary frequencies）。其原因是：频率计算所得到的 Hessian 矩阵，与冻结原子优化过程中计算的梯度在物理意义上并不一致。
一种可能的解决办法是直接将 Hessian 中与冻结原子相关的元素置零。这样可以消除冻结原子对简正模式（normal modes）的贡献，并减少所计算频率的数目。对于一个含 $N$ 个原子的体系，若冻结了 $n$ 个原子，则简正模式的数目为 $3(N-n)-6$，若体系为线性分子则为 $3(N-n)-5$。这种“置零”方法可以通过一对 *$rem* 变量 FRZN_OPT 和 FRZ_ATOMS 来启用，详见下文说明。另一种更优雅的做法是用软的谐振约束势（soft harmonic confining potentials）替代严格固定的原子位置，这在效果上能达到相同的目的，同时允许所有原子坐标发生弛豫（*即*，优化），从而可以进行正确的振动频率计算。用谐振约束势替代冻结原子约束的方法在第 [9.4.7 节](subsec_HarmonicConfiner.md) 中描述。

### `FRZN_OPT`

> **控制本作业在频率计算中是否使用 Hessian 置零技术**
>
> * **类型**: `LOGICAL`
> * **默认值**: `False`
> * **可选值**:
>     * `False`: 不使用置零的 Hessian
>     * `True`: 使用置零的 Hessian
> * **建议**: False

### `FRZ_ATOMS`

> **控制冻结原子的数目**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值`
> * **可选值**:
>     * 用户自定义
> * **建议**: 无

**注意：

上述两个 *$rem* 变量仅与频率计算相关；在带有冻结原子的几何优化中并不需要它们。
**

???+ example "示例 9.12: 在冻结第一个水分子结构的条件下优化水二聚体结构"
    ```qchem
    $molecule
     0 1
     O   -1.551007  -0.114520   0.000000
     H   -1.934259   0.762503   0.000000
     H   -0.599677   0.040712   0.000000
     O    1.350625   0.111469   0.000000
     H    1.680398  -0.373741  -0.758561
     H    1.680398  -0.373741   0.758561
    $end
    
    $rem
     JOBTYPE          OPT
     METHOD           B3LYP
     BASIS            6-31G(D)
     SCF_CONVERGENCE  8
    $end
    
    $opt
     FIXED
     1:3  XYZ
     ENDFIXED
    $end
    ```

???+ example "示例 9.13: 使用 Hessian 置零技术进行频率计算。注意冻结原子的索引在 $frozen_opt 区段中指定。"
    ```qchem
    $molecule
       0 1
       C        -0.0014570824    1.4001468208    0.0000000000
       H        -0.0030029737    2.4867609686    0.0000000000
       C        -1.2093554750    0.6986986619    0.0000000000
       H        -2.1525287416    1.2392252926    0.0000000000
       C        -1.2094237515   -0.6985901650    0.0000000000
       H        -2.1508487680   -1.2427180000    0.0000000000
       C        -0.0003285453   -1.3965954363    0.0000000000
       H        -0.0006460438   -2.4839940415    0.0000000000
       C         1.2098250013   -0.6978846084    0.0000000000
       H         2.1493830451   -1.2446769146    0.0000000000
       C         1.2133329176    0.6987868208    0.0000000000
       H         2.1550504173    1.2408406009    0.0000000000
    $end
    
    $rem
       JOBTYPE      freq
       METHOD       b3lyp
       BASIS        6-31G*
       FRZN_OPT     1  ! Turns on the freq calculation with frozen Hessians
       FRZ_ATOMS    2  ! No. of frozen atoms
       POINT_GROUP_SYMMETRY false
       INTEGRAL_SYMMETRY    false
    $end
    
    $frozen_opt
    1 11
    $end
    ```
