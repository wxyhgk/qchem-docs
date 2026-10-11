---
title: "9.10.2 作业控制与示例"
---

## 9.10.2 作业控制与示例

（2026 年 7 月 4 日）

PIMC_NBEADSPERATOM

### `PIMC_NBEADSPERATOM`

> **在路径积分蒙特卡洛（PIMC）模拟中，每个原子所使用的路径积分时间切片（“珠子”，beads）数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None.`
> * **选项**:
>     * 1
>     * 执行经典玻尔兹曼（Boltzmann）采样。
>     * $>$
>     * 1
>     * 执行量子力学路径积分采样。
> * **建议**: 该变量控制路径积分模拟固有的收敛性。单珠子（one-bead）极限代表经典采样，而无限珠子极限代表精确的量子力学采样。对于分子体系的室温模拟，使用 32 个珠子即可达到较为合理的收敛。

PIMC_TEMP

### `PIMC_TEMP`

> **路径积分模拟的温度，单位为开尔文（K）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None.`
> * **选项**:
>     * 由用户为 PIMC 或经典蒙特卡洛（MC）模拟指定的开尔文数值。
> * **建议**: 无。

PIMC_MCMAX

### `PIMC_MCMAX`

> **要采样的蒙特卡洛（MC）步数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None.`
> * **选项**:
>     * 由用户指定的采样步数。
> * **建议**: 该变量决定 MC/PIMC 模拟的统计收敛性。对于收敛的模拟，建议至少进行 $10^{5}$ 步。

PIMC_WARMUP_MCMAX

### `PIMC_WARMUP_MCMAX`

> **在 MC/PIMC 模拟的平衡（ equilibration ）阶段要采样的蒙特卡洛步数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None.`
> * **选项**:
>     * 由用户指定的采样步数。
> * **建议**: 使用该变量在收集生产（production）统计量之前对分子/环形聚合物进行平衡。通常，进行约为 PIMC_MCMAX 10% 的短程运行即可满足需要。

PIMC_MOVETYPE

### `PIMC_MOVETYPE`

> **选择 MC/PIMC 模拟中使用的位移类型。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 所有珠子的笛卡尔（Cartesian）位移，并偶尔（1%）进行质心移动。
>     * 1
>     * 所有正则模的位移，并偶尔（1%）进行质心移动。
>     * 2
>     * 莱维飞行（Levy flights），不进行质心移动。
> * **建议**: 除经典采样（MC）或珠子数较少的量子采样（PIMC）外，应使用莱维飞行。对于笛卡尔位移和正则模移动，最大位移会在预热（warm-up）运行期间调整为期望的接受率（由 PIMC_ACCEPT_RATE 控制）。对于莱维飞行，接受率仅由 PIMC_SNIP_LENGTH 控制。

PIMC_ACCEPT_RATE

### `PIMC_ACCEPT_RATE`

> **当使用笛卡尔位移或正则模位移时，MC/PIMC 模拟的接受率。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * $0<n<100$
>     * 由用户指定的比率，以整数百分比形式给出。
> * **建议**: 选择合适的接受率以使采样效率最大化，这通常由均方位移（mean-square displacement，输出在作业输出中）来表征。注意，最大位移会在预热运行期间进行调整，以达到大致对应的接受率。

PIMC_SNIP_LENGTH

### `PIMC_SNIP_LENGTH`

> **在环形聚合物的莱维飞行移动中使用的“珠子”数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * $3\leq n\leq\mbox{{\small PIMC\_NBEADSPERATOM}}$
>     * 由用户指定的片段（snippet）长度。
> * **建议**: 选择合适的片段长度以使采样效率最大化。该效率可以通过构型之间的均方位移来估计，其值输出在输出文件的末尾。不过，这种效率通常需要在均方位移（统计相关性的长度）与被移动珠子的数目之间进行权衡。只有被移动的珠子才需要重新计算势能，即需要调用一次 Q-Chem 来计算电子能量。（注意，在一次移动中片段的两个端点保持固定，因此对于长度为 $n$ 的片段，实际移动的是 $n-2$ 个珠子。若模拟中只有 1 个或 2 个珠子，则应改用笛卡尔位移。）

???+ example "示例 9.47: 室温下 H ${}_{2}$ 的路径积分蒙特卡洛模拟"
    ```qchem
    $comment
    The number of Monte Carlo steps is deliberately set low, more typical
    values would be:
       PIMC_WARMUP_MCMAX    10000   !Equilibration run
       PIMC_MCMAX           100000  !Production run
    $end
    
    $molecule
       0  1
       H
       H 1 0.75
    $end
    
    $rem
       JOBTYPE              pimc
       METHOD               hf
       BASIS                sto-3g
       PIMC_TEMP            298
       PIMC_NBEADSPERATOM   32
       PIMC_WARMUP_MCMAX    100     !Equilibration run
       PIMC_MCMAX           1000    !Production run
       PIMC_MOVETYPE        2         !Levy flights
       PIMC_SNIP_LENGTH     10        !Moves 8 beads per MC step (10-endpts)
    $end
    ```

???+ example "示例 9.48: 500K 下水分子的经典蒙特卡洛模拟"
    ```qchem
    $comment
    The number of Monte Carlo steps is deliberately set low, more typical
    values would be:
       PIMC_WARMUP_MCMAX    10000   !Equilibration run
       PIMC_MCMAX           100000  !Production run
    $end
    
    $molecule
       0  1
       H
       O 1 1.0
       H 2 1.0 1 104.5
    $end
    
    $rem
       JOBTYPE              pimc
       METHOD               rimp2
       BASIS                cc-pvdz
       AUX_BASIS            rimp2-cc-pvdz
       PIMC_TEMP            500
       PIMC_NBEADSPERATOM   1       !1 bead is classical sampling
       PIMC_WARMUP_MCMAX    100     !Equilibration run
       PIMC_MCMAX           1000    !Production run
       PIMC_MOVETYPE        0       !Cartesian displacements (ok for 1 bead)
       PIMC_ACCEPT_RATE     40      !During warm-up, adjusts step size to 40% acceptance
    $end
    ```
