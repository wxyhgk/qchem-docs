---
title: "4.3.3 附加选项"
---

## 4.3.3 附加选项

（2026 年 7 月 4 日）

下面列出的是若干用于自定义 SCF 计算的实用选项。这里仅对这些 *$rem* 变量的功能作简要概述。所有与 SCF 相关的变量完整列表见附录 [B](../app_b_quickref/app_quick_ref.md)。另有几个重要子主题单独讨论，包括用于大分子的 ${\cal{O}}({N})$ 方法（第 [4.6](sec_O(N).md) 节）、自定义初始猜测（第 [4.4](sect_initialguess.md) 节），以及 SCF 计算的收敛（第 [4.5](sect_convergence.md) 节）。

INTEGRALS_BUFFER

### `INTEGRALS_BUFFER`

> **控制内存内（in-core）积分存储缓冲区的大小。**
>
> * **类型**：`INTEGER`
> * **默认值**：`15`
> * **选项**：
>     * 由用户自定义大小。
> * **建议**：使用默认值，或就硬件限制咨询系统管理员。

DIRECT_SCF

### `DIRECT_SCF`

> **控制直接 SCF（direct SCF）。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`由程序决定。`
> * **选项**：
>     * TRUE
>     * 强制使用直接 SCF。
>     * FALSE
>     * 不使用直接 SCF。
> * **建议**：使用默认值；直接 SCF 会关闭内存内积分。

METECO

### `METECO`

> **设置丢弃壳层对（shell-pair）的阈值判据。**
>
> * **类型**：`INTEGER`
> * **默认值**：`2`
> * **选项**：
>     * 1
>     * 丢弃比机器精度低四个数量级的壳层对。
>     * 2
>     * 丢弃低于 10
>     * ${}^{-\mathrm{THRESH}}$
>     * 的壳层对。
> * **建议**：使用默认值。

S2THRESH

### `S2THRESH`

> **忽略重叠积分的截断值，通过 $10^{-\mathrm{S2THRESH}}$（$\leq 16$）的二电子壳层对阈值来定义。**
>
> * **类型**：`INTEGER`
> * **默认值**：`与` THRESH `相同`
> * **选项**：
>     * $n$
>     * 对应阈值为
>     * $10^{-n}$
>     * 。
> * **建议**：如果程序发现重叠矩阵出现负本征值，则增大该值。

THRESH

### `THRESH`

> **忽略二电子积分的截断值。$10^{-\mathrm{THRESH}}$（$\leq 16$）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`8`
> * **选项**：
>     * $n$
>     * 对应阈值为
>     * $10^{-n}$
>     * 。
> * **建议**：该值应满足 $\geq$ 3 + SCF_CONVERGENCE，尽管自 Q-Chem 6.0 起（在大多数情况下）默认值为 = 4 + SCF_CONVERGENCE。参见文献 479 Gray M., Bowling P. E., Herbert J. M. J. Phys. Chem. A (2024) , 128 , pp. 7739 。该文献给出了在存在弥散基函数时 THRESH 的推荐取值——此时通常需要更严格的阈值，而过松的阈值可能导致收敛变慢或收敛失败。

STABILITY_ANALYSIS

### `STABILITY_ANALYSIS`

> **对 HF 或 DFT 解执行稳定性分析。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 执行稳定性分析。
>     * FALSE
>     * 不执行稳定性分析。
> * **建议**：当怀疑 HF 或 DFT 解不稳定时，设置为 TRUE。

SCF_PRINT

### `SCF_PRINT`

> **控制 SCF 过程写入 Q-Chem 输出文件的输出详细程度。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 最精简、简洁、有用且必要的输出。
>     * 1
>     * 在级别 0 基础上增加 SCF 电子能量的分项 breakdown。
>     * 2
>     * 在级别 1 基础上增加每一步（cycle）的密度矩阵、Fock 矩阵和 MO 矩阵。
>     * 3
>     * 在级别 2 基础上增加每一步的二电子 Fock 矩阵分量（Coulomb、HF 交换、轨道动能以及 DFT 交换-关联矩阵）。
> * **建议**：谨慎使用；级别 2 或更高可能产生极大的输出文件。只有在 scfman 中（GEN_SCFMAN = FALSE）才能输出全部信息。若 GEN_SCFMAN 设为 TRUE 且 SCF_PRINT > 1，输出中仅包含级别 1 信息加上 MO 矩阵。这些级别主要用于程序调试。

SCF_FINAL_PRINT

### `SCF_FINAL_PRINT`

> **控制 SCF 结束时 SCF 过程写入 Q-Chem 输出文件的输出详细程度。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 不额外输出。
>     * 1
>     * 轨道能量及 SCF 能量的分项 breakdown。
>     * 2
>     * 在级别 1 基础上增加分子轨道（MO）和密度矩阵。
>     * 3
>     * 在级别 2 基础上增加 Fock 矩阵。
> * **建议**：能量的分项 breakdown 通常很有用（级别 1）。
