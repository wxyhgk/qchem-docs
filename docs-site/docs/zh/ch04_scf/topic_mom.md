---
title: "4.5.14 最大重叠方法（MOM）"
---

## 4.5.14 最大重叠方法（Maximum Overlap Method, MOM）

（2026 年 7 月 4 日）

一般而言，DIIS  procedure（第 [4.5.3](sect_diis.md) 节）的成功率非常高。偶尔会遇到的一种困难是：自洽场（SCF）在交替的迭代步中占据两组不同的轨道，从而导致振荡并无法收敛。这一问题可以通过选择新的占据轨道与先前占据轨道集合重叠度（overlap）最大的占据方式来解决。**Q-Chem** 实现了由 Andrew Gilbert 和 Peter Gill 提出的最大重叠方法（MOM）[[443]](../bib_references/bib.md#bib455)。借助 GEN_SCFMAN，MOM 算法可以与 DIIS 算法配合使用，应用于 R、U 和 RO 自洽场计算。

因此，在涉及轨道占据翻转（flipping of orbital occupancies）的收敛问题中，MOM 是 DIIS 的一个有用补充。它由 *$rem* 变量 MOM_START 控制，该变量指定首次启用 MOM 过程的 SCF 迭代步。在设置 MOM_START 的取值时，有两种有用的策略：若希望保持初始组态，应将其设置为从第一步循环开始启用；反之，若希望辅助收敛，则应在较晚的迭代步才启用，以避免一直锁定可能与收敛组态相差甚远的初始组态。

与 MOM 相关的 *$rem* 变量完整列表如下：

### `MOM_PRINT`

> **控制 MOM 过程内部是否输出打印信息。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `FALSE`: 关闭打印输出
>     * `TRUE`: 开启打印输出。
> * **建议**: 无

### `MOM_START`

> **决定在何时启用 MOM 以稳定 DIIS 迭代。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0 (FALSE)`
> * **可选值**:
>     * `0 (FALSE)`: 不使用 MOM
>     * $n$: MOM 从第 $n$ 步循环开始启用 .
> * **建议**: 若希望保留初始轨道，设置为 1。若要用 MOM 辅助收敛，应先运行一次不使用 MOM 的 SCF，以确定 SCF 从哪一步开始振荡，并将 MOM 设置为在振荡开始之前稍早处启用。

### `MOM_METHOD`

> **确定在每一步 SCF 循环中用于最大化重叠度的目标轨道。**
>
> * **类型**: `INTEGER`
> * **默认值**: `MOM`
> * **可选值**:
>     * `MOM`: 最大化与上一步 SCF 循环轨道的重叠度。
>     * `IMOM`: 最大化与初始猜测（initial guess）轨道的重叠度。
> * **建议**: 若能获得合适的猜测轨道，则 IMOM 可以更可靠地收敛到所需解。75 Barca G. M. J., Gilbert A. T. B., Gill P. M. W. J. Chem. Theory Comput. (2018) , 14 , 第 1501 页。链接

???+ example "示例 4.4.17：一个演示如何收敛 DMX 的 ${}^{3}\!A_{2}$ 态 ROHF 计算的例子。注意其中从先前的闭壳层（closed-shell）计算读入轨道，以及使用 MOM 来维持轨道占据。若不使用 MOM，得到的是 ${}^{3}B_{1}$ 态。"
    ```qchem
    $molecule
      +1 1
       C       0.000000     0.000000     0.990770
       H       0.000000     0.000000     2.081970
       C      -1.233954     0.000000     0.290926
       C      -2.444677     0.000000     1.001437
       H      -2.464545     0.000000     2.089088
       H      -3.400657     0.000000     0.486785
       C      -1.175344     0.000000    -1.151599
       H      -2.151707     0.000000    -1.649364
       C       0.000000     0.000000    -1.928130
       C       1.175344     0.000000    -1.151599
       H       2.151707     0.000000    -1.649364
       C       1.233954     0.000000     0.290926
       C       2.444677     0.000000     1.001437
       H       2.464545     0.000000     2.089088
       H       3.400657     0.000000     0.486785
    $end
    
    $rem
       UNRESTRICTED      false
       METHOD            hf
       BASIS             6-31+G*
       SCF_GUESS         core
       THRESH            12
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       UNRESTRICTED      false
       METHOD            hf
       BASIS             6-31+G*
       SCF_GUESS         read
       MOM_START         1
       THRESH            12
    $end
    
    $occupied
       1:26 28
       1:26 28
    $end
    
    @@@
    
    $molecule
       -1 3
       read
    $end
    
    $rem
       UNRESTRICTED      false
       METHOD            hf
       BASIS             6-31+G*
       SCF_GUESS         read
       THRESH            12
    $end
    ```
