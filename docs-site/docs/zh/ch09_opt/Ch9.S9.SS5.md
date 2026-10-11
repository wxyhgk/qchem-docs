---
title: "9.9.5 振动光谱"
---

## 9.9.5 振动光谱

（2026 年 7 月 4 日）

分子固有的核运动可通过分子对入射辐射的响应在实验上观测到。这种响应通常在临界点结构（critical-point structure）下，采用力学与电学谐振子近似（二阶导数计算）进行计算。包含非谐效应的光谱也可以通过动力学模拟获得。这些光谱由动力学响应函数生成，而响应函数涉及自相关函数的傅里叶变换。**Q-Chem** 既能提供来自速度自相关函数的振动谱密度

<a id="Ch9.E63"></a>
$$
D(\omega)\propto\int_{-\infty}^{\infty}dt\ e^{-i\omega t}\langle\vec{v}(0)\bm{\cdot}\vec{v}(t)\rangle \tag{9.63}
$$

也能提供来自偶极矩自相关函数的红外吸收强度

<a id="Ch9.E64"></a>
$$
I(\omega)\propto\frac{\omega}{2\pi}\int_{-\infty}^{\infty}dt\ e^{-i\omega t}\langle\vec{\mu}(0)\bm{\cdot}\vec{\mu}(t)\rangle \tag{9.64}
$$

这两个功能分别由 AIMD_NUCL_VACF_POINTS 和 AIMD_NUCL_DACF_POINTS 关键字激活，其取值表示自相关函数中包含的数据点数目。此外，AIMD_NUCL_SAMPLE_RATE 关键字控制这些性质的采样频率（以时间步数的数目输入）。这些在恒定能量下生成的光谱应在合适的初始条件分布上进行平均。例如，上述表达式中所示的平均应在初始条件的玻尔兹曼（Boltzmann）分布上进行。

请注意，偶极矩自相关函数可能混入转动或平动信息；尽管 **Q-Chem** 中的初始条件已消除了平动与转动，但力和传播（propagation）中的数值噪声仍可能随时间导致平动和转动。平动-转动校正由 PROJ_TRANSROT 关键字激活。

AIMD_NUCL_VACF_POINTS

### `AIMD_NUCL_VACF_POINTS`

> **在 AIMD 轨迹的速度自相关函数中使用的时间点数**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 不计算速度自相关函数。
>     * $1\leq n\leq\mbox{{\small AIMD\_STEPS}}$
>     * 计算轨迹最后
>     * $n$
>     * 个时间步的速度自相关函数。
> * **建议**：若需要 VACF，将其设置为与 AIMD_STEPS 相同的值。

AIMD_NUCL_DACF_POINTS

### `AIMD_NUCL_DACF_POINTS`

> **在 AIMD 轨迹的偶极矩自相关函数中使用的时间点数**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 不计算偶极矩自相关函数。
>     * $1\leq n\leq\mbox{{\small AIMD\_STEPS}}$
>     * 计算轨迹最后
>     * $n$
>     * 个时间步的偶极矩自相关函数。
> * **建议**：若需要 DACF，将其设置为与 AIMD_STEPS 相同的值。

AIMD_NUCL_SAMPLE_RATE

### `AIMD_NUCL_SAMPLE_RATE`

> **对速度和/或偶极矩自相关函数进行采样的速率。以步数的倍数指定；即，每步采样设为 1。**
>
> * **类型**：`INTEGER`
> * **默认值**：`无（None）。`
> * **选项**：
>     * $1\leq n\leq\mbox{{\small AIMD\_STEPS}}$
>     * 每
>     * $n$
>     * 步更新一次速度/偶极矩自相关函数。
> * **建议**：由于速度和偶极矩在从头算（ab initio）方法中都会例行计算，当需要 VACF 或 DACF 时，该变量几乎总是应设置为 1。

PROJ_TRANSROT

### `PROJ_TRANSROT`

> **在 AIMD 轨迹过程中消除平动和转动漂移。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE
>     * 不施加平动/转动校正。
>     * TRUE
>     * 施加平动/转动校正。
> * **建议**：在计算光谱时（例如参见 AIMD_NUCL_DACF_POINTS），该选项可用于消除由平动和/或转动运动引入的人为、混染峰。建议对所有基于动力学的光谱模拟将其设置为 TRUE。
