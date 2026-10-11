---
title: "4.5.9 松弛约束算法（RCA）"
---

## 4.5.9 松弛约束算法（Relaxed Constraint Algorithm, RCA）

（2026 年 7 月 4 日）

松弛约束算法（RCA）是一种巧妙而简单的自洽场（SCF）能量极小化方法，在初始猜测较差的情况下尤为有效。例如，当采用用户指定基组（Basis Set）时（必须使用"核"猜测或 GWH 猜测），或者当近简并效应意味着初始猜测很可能相对于期望的收敛解占据了错误的轨道时，就属于这种情况。

简而言之，RCA 将 SCF 问题视为能量关于密度矩阵的函数 $E(\mathbf{P})$ 在约束条件下的极小化问题。[[186]](../bib_references/bib.md#bib182)
 其约束条件是密度矩阵必须满足幂等性（idempotent），即 $\mathbf{P}\cdot\mathbf{P}=\mathbf{P}$，这基本上强制占据数只能为零或一。RCA 的核心思想在于，这一约束可以被松弛，以允许亚幂等（sub-idempotent）密度矩阵，即 $\mathbf{P}\cdot\mathbf{P}\leq\mathbf{P}$。该条件迫使占据数介于零和一之间。从物理上看，我们预期任何具有分数占据数的态都可以通过将电子从高能轨道转移到低能轨道来降低其能量。因此，若我们在松弛后的亚幂等约束条件下求解 $E(\mathbf{P})$ 的极小值，我们期望最终的解仍然会是幂等的。

事实上，对于 Hartree-Fock 方法，这一结论可以被严格证明。对于密度泛函理论（Density Functional Theory, DFT），极小值可能具有分数占据数，但这些占据数可以用系综 DFT（ensemble DFT）给出物理解释。松弛约束之所以更易于处理，是因为可以容易地证明：只要线性组合系数介于零和一之间，亚幂等矩阵的线性组合也一定是亚幂等的。利用这一性质，可以以一种保证每一步能量都下降的方式来加速收敛。

**Q-Chem** 中 RCA 的实现紧密遵循 RCA 算法的"能量 DIIS（Energy DIIS）"实现。[[735]](../bib_references/bib.md#bib768)
 在这里，当前密度矩阵被写成先前各密度矩阵的线性组合：

<a id="Ch4.E39"></a>
$$
\mathbf{P}(x)=\sum_{i}x_{i}\mathbf{P}_{i} \tag{4.39}
$$

在非常好的近似下（对 Hartree-Fock 方法是精确的），$\mathbf{P}(x)$ 的能量可以写成关于 $x$ 的二次函数：

<a id="Ch4.E40"></a>
$$
\mathbf{E}(x)=\sum_{i}E_{i}x_{i}+\frac{1}{2}\sum_{i}x_{i}(\mathbf{P}_{i}-\mathbf{P}_{j})\cdot(\mathbf{F}_{i}-\mathbf{F}_{j})x_{j} \tag{4.40}
$$

在每次迭代中，选取 $x$ 以在约束条件"所有 $x_{i}$ 均介于零和一之间"下极小化 $\mathbf{E}(x)$。$\mathbf{P}(x)$ 对应的 Fock 矩阵进一步被写成先前各 Fock 矩阵的线性组合，

<a id="Ch4.E41"></a>
$$
\mathbf{F}(x)=\sum_{i}x_{i}\mathbf{F}_{i}+\delta\mathbf{F}_{xc}(x) \tag{4.41}
$$

其中 $\delta\mathbf{F}_{xc}(x)$ 表示交换-关联（exchange-correlation）部分的一个（通常很小的）变化，该变化在 $x$ 确定之后计算一次。我们注意到，这种外推方式与 DIIS 所使用的非常相似。然而，与 DIIS 不同，该过程保证在每次迭代都能降低能量 $\mathbf{E}(x)$。

在实践中，RCA 方法非常适合处理收敛困难的情形，因为它对 DIIS 中可能出现的轨道 erratic 交换（轨道剧烈 swapping）现象具有免疫能力。另一方面，RCA 在接近收敛时的表现相对较差，需要相对较多的迭代步数才能提高一个已经较好的近似解的精度。因此在很多情况下， advantageous 的做法是先运行若干初始步的 RCA，然后在达到指定的迭代次数或达到某个目标收敛阈值之后切换到 DIIS。最后，注意 RCA 本质上将能量视为密度矩阵的函数，因此它不能应用于显式基于轨道的限制性开壳层（restricted open shell）计算。注意：RCA 与 INCDFT 的交互效果不佳，因此当请求 RCA 或 RCA_DIIS 计算时，INCDFT 默认被禁用。若要在此类计算中启用 INCDFT，请在 *$rem* 区段中设置 INCDFT = 2。RCA 与增量式 Fock 构建（incremental Fock builds）的交互也可能不佳；如果 RCA 无法收敛，在某些情况下设置 INCFOCK = FALSE
可能会改善收敛性。

下面列出了 RCA 的作业控制变量（Job-control variables），并附有一个使用示例。

RCA_PRINT

### `RCA_PRINT`

> **控制 RCA SCF 优化的输出信息。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * 0
>     * 不输出任何信息
>     * 1
>     * RCA 摘要信息
>     * 2
>     * 级别 1 加上 RCA 系数
>     * 3
>     * 级别 2 加上 RCA 迭代详情
> * **建议**: 无

MAX_RCA_CYCLES

### `MAX_RCA_CYCLES`

> **当 SCF_ALGORITHM 为 RCA_DIIS 时，切换到 DIIS 之前 RCA 迭代的最大次数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `50`
> * **可选值**:
>     * N
>     * 在切换到 DIIS 之前执行 N 次 RCA 迭代
> * **建议**: 无

THRESH_RCA_SWITCH

### `THRESH_RCA_SWITCH`

> **当 SCF_ALGORITHM 为 RCA_DIIS 时，RCA 与 DIIS 之间切换的阈值。**
>
> * **类型**: `INTEGER`
> * **默认值**: `3`
> * **可选值**:
>     * N
>     * 当误差（Error）小于
>     * $10^{-N}$
>     * 时，算法从 RCA 切换为 DIIS。
> * **建议**: 无

???+ example "示例 4.13: 将 RCA_DIIS 算法应用于自由基"
    ```qchem
    $molecule
    0 2
       H    1.004123   -0.180454    0.000000
       O   -0.246002    0.596152    0.000000
       O   -1.312366   -0.230256    0.000000
    $end
    
    $rem
       UNRESTRICTED         true
       METHOD               hf
       BASIS                cc-pVDZ
       SCF_GUESS            gwh
       SCF_ALGORITHM        RCA_DIIS
       THRESH               9
    $end
    ```
