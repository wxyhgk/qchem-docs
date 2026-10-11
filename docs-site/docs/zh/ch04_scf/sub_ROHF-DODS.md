---
title: "4.5.18 正则 ROSCF 计算中的轨道能量缩放"
---

## 4.5.18 正则 ROSCF 计算中的轨道能量缩放

（2026 年 7 月 4 日）

对于高自旋半充满开壳层体系，通过设置 ROSCF_DODS = TRUE，可以按照 Plakhutin 和 Davidson[[1094]](../bib_references/bib.md#bib1140) 的方法执行正则 ROSCF 计算。正则 ROSCF 方法给出的总波函数与"常规" ROSCF 完全相同，因而也具有相同的总能量和正确的 $\langle\hat{S}^{2}\rangle$ 表现。与"常规" ROSCF 不同的是，它像非限制自洽场（unrestricted SCF）那样，为 $\alpha$ 电子和 $\beta$ 电子提供两套不同的轨道，并且这些轨道满足 Koopmans 定理。正因如此，正则 ROSCF 也被称为 ROSCF-DODS，其中 DODS 代表"different orbitals for different spins"（不同自旋使用不同轨道）。

一般而言，ROSCF 计算往往难以收敛，通常是因为出现了违背构造原理（aufbau principle）的情况。在 ROSCF 计算中，可以通过对 $\alpha$ 和 $\beta$ 的 RO Fock（自旋受限 Fock）矩阵的开壳层对角块施加中间缩放（intermediary scaling）来避免这些情况，所选的缩放方式能够在 SCF 迭代过程中恢复"正确的"轨道排序。该 procedures 与能级平移（level-shifting，见第 [4.5.5](sect_lshift.md) 节）类似，但要简单得多。它利用了这样一个事实：在 ROSCF 计算中，可以任意缩放 RO Fock 矩阵的对角块，而不会影响总波函数。

举个例子，考虑一个只含一个未配对 $\alpha$ 电子的体系，其中能量最高的 $\alpha$ 分子轨道（MO）属于双占据轨道空间，而属于（双）占据轨道空间的最低 $\alpha$ MO 属于（双）未占据轨道空间。假设这两个轨道的能量分别为 $-0.5$ 和 $0.5~{}E_{h}$。如果未配对电子的轨道能量为 $-0.6~{}E_{h}$，则可以对其进行任意平移，*例如*，通过将其能量乘以 $0.5~{}E_{h}$ 的因子，将其移至 $0.3~{}E_{h}$，这对应于设置 ROSCF_DIAG_SCALE_A = 50。这使得 SCF 算法更容易收敛。

该方法明显的局限在于：必须已知收敛后的轨道能量，才能选择正确的缩放因子。在实际操作中，如果遇到收敛不佳的情况，可以尝试 ROHF_DIAG_SCALE_A 与 ROHF_DIAG_SCALE_B 的不同组合。

### 作业控制（Job Control）

ROSCF_DIAG_SCALE_A

### `ROSCF_DIAG_SCALE_A`

> **在执行正则限制开壳层自洽场（restricted open-shell SCF）计算时，在 SCF 迭代过程中对开壳层对角 $\alpha$ Fock 矩阵块（从而对单占据 $\alpha$ 轨道能量）进行缩放，以缓解收敛困难体系中违背构造原理的问题。收敛之后，会恢复正确的正则轨道能量。**
>
> * **类型**：`INTEGER`
> * **默认值**：`50`
> * **选项**：
>     * $n$
>     * 将
>     * $\alpha$
>     * 轨道能量缩放的因子为
>     * $n\cdot 10^{-}2$
>     * 。
> * **建议**：若出现收敛问题，可尝试一系列不同的取值，例如 $\pm 800$ 、 $\pm 400$ 、 $\pm 200$ 、 $\pm 100$ 、 $\pm 50$ 、 $\pm 20$ 、 $\pm 10$ 。

ROSCF_DIAG_SCALE_B

### `ROSCF_DIAG_SCALE_B`

> **与 ROSCF_DIAG_SCALE_A 相同，只不过在 SCF 迭代过程中被操控的是单未占据 $\beta$ 轨道能量。**
>
> * **类型**：`INTEGER`
> * **默认值**：`50`
> * **选项**：
>     * $n$
>     * 将
>     * $\beta$
>     * 轨道能量缩放的因子为
>     * $n\cdot 10^{-}2$
>     * 。
> * **建议**：参见 ROSCF_DIAG_SCALE_A 中的建议。
