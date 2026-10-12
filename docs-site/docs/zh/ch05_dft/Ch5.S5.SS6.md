---
title: "5.5.6 增量式 DFT（Incremental DFT）"
---

## 5.5.6 增量式 DFT（Incremental DFT）

（2026 年 7 月 4 日）

增量式 DFT（Incremental DFT, IncDFT）利用差密度（difference density）和泛函值来改进 DFT 数值积分（quadrature）过程的性能，从而对可忽略的值进行更有效的筛除（screening）。启用此选项后，由于筛除更加有效，每次连续迭代的效率都会得到提升。

### `INCDFT`

> **控制在 DFT 能量计算中是否使用 IncDFT 过程。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`TRUE`
> * **可选值**：
>     * FALSE
>     * 不使用 IncDFT
>     * TRUE
>     * 使用 IncDFT
> * **建议**：开启此选项可以加快 SCF 计算，尤其是在 SCF 迭代的后期阶段。请注意，对于某些体系，使用此选项可能会导致收敛问题。

### `INCDFT_DENDIFF_THRESH`

> **设置在 IncDFT 过程中对密度矩阵值进行筛除的阈值。**
>
> * **类型**：`INTEGER`
> * **默认值**：`SCF_CONVERGENCE`
> * **可选值**：
>     * $n$
>     * 对应于阈值为
>     * $10^{-n}$
>     * 。
> * **建议**：如果默认值导致收敛问题，请将此值设置得更高以收紧阈值。

### `INCDFT_GRIDDIFF_THRESH`

> **设置在 IncDFT 过程中对泛函值进行筛除的阈值**
>
> * **类型**：`INTEGER`
> * **默认值**：`SCF_CONVERGENCE`
> * **可选值**：
>     * $n$
>     * 对应于阈值为
>     * $10^{-n}$
>     * 。
> * **建议**：如果默认值导致收敛问题，请将此值设置得更高以收紧阈值。

### `INCDFT_DENDIFF_VARTHRESH`

> **为 IncDFT 过程中筛除密度矩阵值的可变阈值设置下界。阈值将从该值开始，随后根据当前 SCF 迭代的误差而变化，直到达到由 INCDFT_DENDIFF_THRESH 指定的值。这意味着该值必须设置得比 INCDFT_DENDIFF_THRESH 更低。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * $n$
>     * 对应于阈值为
>     * $10^{-n}$
>     * 。
> * **建议**：如果默认值导致收敛问题，请将此值设置得更高以提高精度。如果仍然无效，则设为 0 并使用静态阈值。

### `INCDFT_GRIDDIFF_VARTHRESH`

> **为 IncDFT 过程中筛除泛函值的可变阈值设置下界。阈值将从该值开始，随后根据当前 SCF 迭代的误差而变化，直到达到由 INCDFT_GRIDDIFF_THRESH 指定的值。这意味着该值必须设置得比 INCDFT_GRIDDIFF_THRESH 更低。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * $n$
>     * 对应于阈值为
>     * $10^{-n}$
>     * 。
> * **建议**：如果默认值导致收敛问题，请将此值设置得更高以提高精度。如果仍然无效，则设为 0 并使用静态阈值。
