---
title: "9.7.1 概述"
---

## 9.7.1 概述

（2026 年 7 月 4 日）

反应路径（reaction path）的概念在化学上直观易懂（即从反应物到产物的一条途径），但在理论上却有些含糊，因为大多数数学定义都依赖于所选的坐标系。势能面（Potential Energy Surface, PES）上的驻点（stationary point）与这种选择无关，但连接各驻点的路径则不然，因此“反应路径”存在多种数学定义。**Q-Chem** 采用内禀反应坐标（Intrinsic Reaction Coordinate, IRC）的定义，该定义最早由 Fukui 提出[[417]](../bib_references/bib.md#bib426)，
 如今已成为量子化学中相当标准的选择。IRC 本质上是一系列从过渡态（transition state）出发、沿最速下降方向下坡的小步路径。

反应路径极不可能是直线，因此若沿梯度方向走一个有限步长，就会偏离“真实”的反应路径。一系列小的最速下降步会沿实际反应路径来回曲折前进（这种行为称为“缝合”，stitching）。Ishida *et al.*[[615]](../bib_references/bib.md#bib638)
 开发了一种预测-校正（predictor-corrector）算法，在初始最速下降步之后进行第二次梯度计算，随后沿两梯度的角平分线做直线搜索以回到路径上，此算法后来由 Schmidt *et al.*进一步改进[[1214]](../bib_references/bib.md#bib1268)。

这正是 **Q-Chem** 所采用的方法。它不能用于从过渡态出发的第一个下坡步，因为此时梯度为零，所以取而代之的是沿虚频对应的 Hessian 模式走一步。

反应路径可以在 $Z$-矩阵坐标、笛卡尔坐标或质量加权笛卡尔坐标（mass-weighted Cartesian coordinates）中定义和跟踪。其中后者代表由 Fukui 定义的“真实” IRC[[417]](../bib_references/bib.md#bib426)。
 如果跟踪反应路径的目的仅仅是确定给定的过渡态连接了哪两个局部极小值——这可以说是 IRC 算法的主要用途——那么坐标系的选择就无关紧要。要使用 IRC 程序，必须已获得过渡态几何结构和精确的 Hessian 矩阵。这两者必须通过先前的两次计算得到，即分别使用
JOBTYPE = TS（过渡态结构搜索）和
JOBTYPE = FREQ（Hessian 计算）。作业控制变量及示例见下文。

通过在 *$rem* 段中设置 JOBTYPE = RPATH
即可调用 IRC 计算，其他 *$rem* 变量将在下面说明。IRC 计算可从
第 9.3 节[9.3](sec_better_TS_guess.md)中讨论的方法中获益，以获得过渡态结构的良好初始猜测。最终路径（正向和反向两个方向）作为一系列代表路径上各步的笛卡尔坐标几何结构，打印在 **Q-Chem** 输出文件的末尾。此输出的格式是标准格式，可被 Visual Molecular Dynamics (VMD) 程序等读取[[W. Humphrey, A. Dalke, and K. Schulten (1996)]](../bib_references/bib.md#bib627)。

RPATH_COORDS

### `RPATH_COORDS`

> **决定在 IRC 搜索中使用哪种坐标系。**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **选项**：
>     * 0
>     * 使用质量加权坐标。
>     * 1
>     * 使用笛卡尔坐标。
>     * 2
>     * 使用
>     * Z
>     * -矩阵坐标。
> * **建议**：使用默认值。注意，使用 $Z$-矩阵坐标要求几何结构以 $Z$-矩阵格式输入。

RPATH_DIRECTION

### `RPATH_DIRECTION`

> **决定首先要沿本征模式的哪个方向下降。在 Hessian 对角化之前通常无法预知该方向。**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **选项**：
>     * 1
>     * 先沿本征模式的正方向下降，然后在负方向重新启动。
>     * -1
>     * 先沿本征模式的负方向下降，然后在正方向重新启动。
> * **建议**：通常无法先验地确定应沿哪个方向进行，因此会自动考虑两个方向。读取反应路径作业最终几何结构的作业将使用第二个方向的最后一步。

RPATH_MAX_CYCLES

### `RPATH_MAX_CYCLES`

> **指定在反应路径上要寻找的最大点数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`20`
> * **选项**：
>     * $n$
>     * 用户自定义的循环次数。
> * **建议**：如果希望到达极小值但用默认值未能达到，则使用更多的点。

RPATH_MAX_STEPSIZE

### `RPATH_MAX_STEPSIZE`

> **指定所采取的最大步长（以 0.001 a.u. 为单位）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`150`
> * **选项**：
>     * $n$
>     * 步长 =
>     * $n$
>     * /1000 a.u.
> * **建议**：无。

RPATH_TOL_DISPLACEMENT

### `RPATH_TOL_DISPLACEMENT`

> **指定步长的收敛阈值。如果算法选择的步长小于该值，则认为路径已到达极小值。**
>
> * **类型**：`INTEGER`
> * **默认值**：`5000`
> * **选项**：
>     * $n$
>     * 用户自定义。容差 =
>     * $n$
>     * /1000000 a.u.
> * **建议**：使用默认值。注意，此选项只控制结束 RPATH 作业的阈值，对计算的中间步骤没有任何影响。较小的值会使反应路径在更接近真实极小值处终止。然而，在不调整 RPATH_MAX_STEPSIZE 的情况下使用较小的值，可能导致在极小值附近的振荡。

RPATH_PRINT

### `RPATH_PRINT`

> **指定输出打印级别。**
>
> * **类型**：`INTEGER`
> * **默认值**：`2`
> * **选项**：
>     * $n$
> * **建议**：使用默认值，因为更高级别并不会打印多少额外信息。大部分输出来自于沿反应路径所执行的多次单点能计算。

???+ example "示例 9.25：反应路径搜索。注意共有三个必需作业：先进行 TS 搜索，
接着进行频率（Hessian）计算，最后进行 IRC 计算。"
    ```qchem
    $molecule
       0 1
       C
       H 1 1.20191
       N 1 1.22178 2 72.76337
    $end
    
    $rem
       JOBTYPE            ts
       BASIS              sto-3g
       METHOD             hf
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE            freq
       METHOD             hf
       BASIS              sto-3g
       SCF_GUESS          read
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE            rpath
       BASIS              sto-3g
       METHOD             hf
       SCF_GUESS          read
       RPATH_MAX_CYCLES   50
    $end
    ```
