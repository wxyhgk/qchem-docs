---
title: "7.11.12 RASCI2 的任务控制选项"
---

## 7.11.12 RASCI2 的任务控制选项

(2026 年 7 月 4 日)

目前 RASCI1 和 RASCI2 的实现使用不同的关键字（将在未来版本中统一）。本节适用于 RASCI2（偶数与奇数电子体系，采用分辨恒等式（Resolution of the Identity, RI）近似的行列式驱动算法）。

RAS-CI2 方法的使用通过将 CORRELATION = RASCI2 且 EXCHANGE = HF 来控制。最基本的输入还要求指定 RAS_N_ROOTS 所需的（非零）值，以及构成"活性" RAS2 空间的活性占据轨道和虚轨道数目。RASCI2 计算还需要通过 AUX_BASIS 指定一个辅助基组。

RAS_N_ROOTS

### `RAS_N_ROOTS`

> **设置要计算的 RAS-CI 根（态）数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * $n$
>     * $n>0$
>     * 计算
>     * $n$
>     * 个 RAS-CI 态
> * **建议**: 无。仅适用于 RASCI2

RAS_ACT_OCC

### `RAS_ACT_OCC`

> **设置进入 RAS 活性空间的占据轨道数目。**
>
> * **类型**: `Integer`
> * **默认值**: `None`
> * **选项**:
>     * $n$
>     * 用户定义的整数
> * **建议**: 无。仅适用于 RASCI2

RAS_ACT_VIR

### `RAS_ACT_VIR`

> **设置进入 RAS 活性空间的虚轨道数目。**
>
> * **类型**: `Integer`
> * **默认值**: `None`
> * **选项**:
>     * $n$
>     * 用户定义的整数
> * **建议**: 无。仅适用于 RASCI2。

RAS_ACT_DIFF

### `RAS_ACT_DIFF`

> **设置 $\alpha$ 电子与 $\beta$ 电子数目的差异，从而控制计算中所用的激发级别。**
>
> * **类型**: `Integer`
> * **默认值**: `None`
> * **选项**:
>     * 1
>     * 奇数个电子或阳离子
>     * 0
>     * 偶数个电子
>     * $-1$
>     * 阴离子
>     * $n$
>     * $n<-99$
>     * 在 DDCI 激发级别触发 RAS2-SF
>     * $n=-451$
>     * 以及
>     * $n=-452$
>     * 触发重启（restart）机制，将每个态的最新最佳猜测波函数恢复至所请求的态数目
> * **建议**: 设置为 0 适用于大多数单重态体系。仅适用于 RASCI2。

请注意，其他可用于控制 RASCI2 计算评估的 *$rem* 变量包括：MAX_CIS_CYCLES（Davidson 迭代的最大次数），以及 N_FROZEN_CORE 和 N_FROZEN_VIRTUAL（从 RASCI2 计算中排除-core 和/或虚轨道）。更多细节请参阅下方的示例输入。

RAS_CALC_SOC

### `RAS_CALC_SOC`

> **控制是否仅对 RAS2 任务计算自旋-轨道耦合（Spin-Orbit Coupling, SOC）常数。**
>
> * **类型**: `Integer/Logical`
> * **默认值**: `False`
> * **选项**:
>     * False
>     * 不执行 SOC 计算。
>     * True
>     * 执行 SOC 计算。
> * **建议**: 该 $rem 变量用于控制自旋-轨道耦合（SOC）分析部分。

注意：对于 SOC 计算，RASCI2 方法默认同时计算单电子和双电子平均场贡献。SOC 分析之后可以触发 SOC-NTO 分析。NTO 分析需要两个额外参数，MOLDEN_FORMAT 和 NTO_PAIRS。这两个变量的详细信息见以下 *$rem* 各节：

MOLDEN_FORMAT

### `MOLDEN_FORMAT`

> **将 RASCI2 SOC 分析中 NTO 的输出格式设置为 MolDen 格式。**
>
> * **类型**: `Logical`
> * **默认值**: `False`
> * **选项**:
>     * True
>     * 在
>     * Q-Chem
>     * 输出文件末尾追加
>     * MolDen
>     * 输入文件。
> * **建议**: 目前，RASCI2 中的 SOC-NTO 分析仅支持 MolDen 格式，暂不支持其他可视化工具。更多信息请参阅"使用 MolDen 可视化轨道"一节。

NTO_PAIRS

### `NTO_PAIRS`

> **控制在 RASCI2 SOC 分析部分计算得到的 SOC 跃迁的空穴/粒子 NTO 对的输出。**
>
> * **类型**: `Integer`
> * **默认值**: `0`
> * **选项**:
>     * $N$
>     * 为每个 SOC 跃迁写出
>     * $N$
>     * 对 NTO。
> * **建议**: 若启用（$N>0$），每个跃迁至少会打印两对 NTO。如需更多 NTO，请增大 $N$ 的值。有关 NTO 可视化的信息，请参见 7.13.3 节。

RAS_PCM_INIT

### `RAS_PCM_INIT`

> **在 RAS-SF 中触发态特定（state-specific）PCM 溶剂化计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 包含溶剂化
> * **建议**: 这会触发型定溶剂化的非平衡（nonequilibrium）版本。平衡版本还需要额外的关键字。
