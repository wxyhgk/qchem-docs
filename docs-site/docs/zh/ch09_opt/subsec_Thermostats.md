---
title: "9.9.4 恒温器"
---

## 9.9.4 恒温器

(July 4, 2026)

上述讨论中隐含了一个能量守恒的假设，这意味着动力学是在*微正则*（$NVE$）系综下运行的。
或者，借助恒温器（Thermostat），**Q-Chem** 中的 AIMD 代码也可以采样*正则*
（$NVT$）系综。恒温器模拟周围温度热浴的热效应，而轨迹（或多条轨迹）的时间平均
即可给出在选定温度下的热力学平均值。当多个极小值在热力学上均可及时，此选项尤其适用。
所有采样信息同样保存在作业的 `$QCSCRATCH` 目录下的 `AIMD/` 子目录中。
可利用这些数据在外部进行热力学平均值计算与误差分析。**Q-Chem** 中实现了两种常用的
恒温器选项，二者均能给出经典分子运动的正确正则分布，下面将对其进行更详细的描述。
恒压调压器（barostat，用于 $NPT$ 模拟）尚未实现。

与任何正则采样一样，轨迹的演化受制于势垒高度。短轨迹只会采样初始条件所在的
局部极小值范围内——例如，当需要采样某一给定异构体的性质时，这可能正是所需的效果。
由于恒温器引起的能量涨落，无法保证轨迹停留在该势能阱内，也无法保证轨迹能够
越过势垒到达相邻的极小值（除后一种情形在无限采样极限下成立之外，而该极限在实践中
很可能永远无法达到）。重要的是，用户应注意：引入恒温器会破坏任何实时轨迹信息的
有效性；带恒温器的轨迹*不应*用于评估实时动力学可观测量，而仅用于计算热力学平均值。

## 9.9.4.1 Langevin 恒温器

随机白噪声 Langevin 恒温器（AIMD_THERMOSTAT = LANGEVIN）将施加于原子核动量的
随机"踢击"与耗散性的摩擦项相结合。这两种贡献之间的平衡模拟了与周围热浴之间的
能量交换。由此产生的轨迹在长时间采样极限下会生成正确的正则分布。**Q-Chem** 中的
实现遵循 Bussi 和 Parrinello[[176]](../bib_references/bib.md#bib171)
 提出的速度 Verlet 形式，
该形式对所有时间步长和恒温器参数而言都是有效的传播器。恒温器与模拟体系中的每个
自由度相耦合。MD 积分时间步长（TIME_STEP）的选取方式与 NVE 轨迹中相同。
因此，该恒温器唯一可由用户控制的参数是隐含热浴对轨迹产生影响的时间尺度。
AIMD_LANGEVIN_TIMESCALE 关键字以飞秒（femtosecond）为单位确定此参数。
对于更习惯从摩擦强度角度思考的用户而言，该参数与摩擦的倒数成正比。
时间尺度参数取小值时产生"紧"恒温器，它会将体系强有力地维持在选定温度附近，
但通常不允许快速的结构柔性。（定性来说，可将此类模拟想象为在糖浆中采样。
不过，这一类比仅适用于热力学采样性质，并不暗示溶剂有任何电子层面的作用！）
这些较小的值通常更适合小体系，因为其较少的自由度不能快速交换能量，
并可能表现出非遍历（non-ergodic）行为。另一方面，较大的时间尺度参数值允许
更灵活的结构采样，其代价是（短期的）偏离目标平均温度的程度更大。
这些较大的值更适合较大体系，因为大量自由度之间固有的微正则能量交换
本身就已经趋向正则性质。（可将此区间想象为在轻质有机溶剂中采样。）
重要的是，在无限采样极限下，热力学平均值完全不受此时间尺度参数的影响。
相反，时间尺度仅控制系综被探索的效率。若追求最高效率，用户可外部计算
目标观测量的时间关联函数导出的寿命，并使寿命随此时间尺度参数达到最小值。
在轨迹结束时，将计算得到的平均温度与所请求的目标温度进行比较，以作验证之用。

???+ example "示例 9.39: 使用带 Langevin 恒温器的 AIMD 进行正则（ $NVT$ ）采样"
    ```qchem
    $comment
       Short example of using the Langevin thermostat
       for canonical (NVT) sampling
    $end
    
    $molecule
       0 1
       H
       O  1  1.0
       H  2  1.0  1  104.5
    $end
    
    $rem
       JOBTYPE                  aimd
       EXCHANGE                 hf
       BASIS                    sto-3g
       AIMD_TIME_STEP           20      !in au
       AIMD_STEPS               100
       AIMD_THERMOSTAT          langevin
       AIMD_INIT_VELOC          thermal
       AIMD_TEMP                298     !in K - initial conditions AND thermostat
       AIMD_LANGEVIN_TIMESCALE  100     !in fs
    $end
    ```

## 9.9.4.2 Nosé-Hoover 恒温器

还有一种可选的恒温器方法，即 Nosé-Hoover
恒温器[[914]](../bib_references/bib.md#bib950)
（也称为 Nosé-Hoover"链"），它通过在扩展相空间中执行微正则
（$NVE$）轨迹来模拟周围热浴的作用。通过允许能量与耦合到目标体系的一串
虚拟粒子交换，可针对代表真实体系的那些自由度正确获得
$NVT$ 采样。（只有目标体系的性质被保存在 `$QCSCRATCH/AIMD` 中用于后续分析和
可视化，虚拟的 Nosé-Hoover 自由度不会被保存。）**Q-Chem** 中的实现遵循
Martyna 的方法[[914]](../bib_references/bib.md#bib950)
，该方法在 Nosé[[1000]](../bib_references/bib.md#bib1041)
 和 Hoover[[592]](../bib_references/bib.md#bib615)
 原始扩展拉格朗日方法的基础上进行了增强，利用一串辅助自由度来恢复刚性体系的
遍历性，从而给出正确的 $NVT$ 系综。与 Langevin 恒温器不同，体系粒子与辅助链
粒子的集合可以以时间可逆的方式传播，无需随机扰动。

**Q-Chem** 的实现并不直接设置辅助链粒子的质量和力常数，而是关注恒温器的
时间尺度，这一点与上文所述 Langevin 恒温器相同。时间尺度参数由关键字
NOSE_HOOVER_TIMESCALE 控制，以飞秒为单位。此功能的另一个唯一可由用户
控制的参数是 Nosé-Hoover 链的长度，通常选择 3–6 个虚拟粒子。重要的是，
**Q-Chem** 中的当前实现为与整个体系相耦合的*单条*链。将每个自由度分别与
各自恒温器耦合的全面恒温方法（有时用于特别刚性的体系）尚未实现，对于此类情况
建议使用 Langevin 恒温器。对于大体系和/或易变形（fluxional）体系，
单链 Nosé-Hoover 方法是适用的。

???+ example "示例 9.40: 使用带 Nosé-Hoover 链恒温器的 AIMD 进行正则（ $NVT$ ）采样"
    ```qchem
    $molecule
       0 1
       H
       O 1 1.0
       H 2 1.0 1 104.5
    $end
    
    $rem
       JOBTYPE                 aimd
       EXCHANGE                hf
       BASIS                   sto-3g
       AIMD_TIME_STEP          20      !in au
       AIMD_STEPS              100
       AIMD_THERMOSTAT         nose_hoover
       AIMD_INIT_VELOC         thermal
       AIMD_TEMP               298     !in K - initial conditions AND thermostat
       NOSE_HOOVER_LENGTH      3       !chain length
       NOSE_HOOVER_TIMESCALE   100     !in fs
    $end
    ```

AIMD_THERMOSTAT

### `AIMD_THERMOSTAT`

> **对 AIMD 轨迹施加恒温控制。**
>
> * **类型**: `INTEGER`
> * **默认值**: `none`
> * **选项**:
>     * LANGEVIN
>     * 随机白噪声 Langevin 恒温器
>     * NOSE_HOOVER
>     * 时间可逆的 Nosé-Hoover 链恒温器
> * **建议**: 采样正则（NVT）系综时可使用任一恒温器。

AIMD_LANGEVIN_TIMESCALE

### `AIMD_LANGEVIN_TIMESCALE`

> **设置 Langevin 恒温器的时间尺度（强度）**
>
> * **类型**: `INTEGER`
> * **默认值**: `none`
> * **选项**:
>     * $n$
>     * 恒温器时间尺度，以 $n$
>     * fs
> * **建议**: 较小的值（约 100）对应更紧的恒温器，但可能阻碍快速采样。较大的值（ $\geq 1000$ ）允许更快速的采样，但可能需要更长时间才能达到热平衡。

NOSE_HOOVER_LENGTH

### `NOSE_HOOVER_LENGTH`

> **设置 Nosé-Hoover 恒温器的链长**
>
> * **类型**: `INTEGER`
> * **默认值**: `none`
> * **选项**:
>     * $n$
>     * 辅助变量的链长为
>     * $n$
> * **建议**: 通常取 3-6

NOSE_HOOVER_TIMESCALE

### `NOSE_HOOVER_TIMESCALE`

> **设置 Nosé-Hoover 恒温器的时间尺度（强度）**
>
> * **类型**: `INTEGER`
> * **默认值**: `none`
> * **选项**:
>     * $n$
>     * 恒温器时间尺度，以 $n$
>     * fs 为单位
> * **建议**: 较小的值（约 100）对应更紧的恒温器，但可能阻碍快速采样。较大的值（ $\geq 1000$ ）允许更快速的采样，但可能需要更长时间才能达到热平衡。
