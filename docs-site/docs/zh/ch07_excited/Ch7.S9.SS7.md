---
title: "7.9.7 EOM-DIP-CCSD"
---

## 7.9.7 EOM-DIP-CCSD

（2026 年 7 月 4 日）

双电离势（double-ionization potential, DIP）是 EOM-CCSD 的另一种非电子数守恒（non-electron-conserving）变体。[[740]](../bib_references/bib.md#bib773)

在 DIP 方法中，目标态是通过从参考态上剥离（detach）两个电子而得到的：

<a id="DIP:WF"></a>
$$
\Psi_{k}=\hat{R}_{N-2}\Psi_{0}(N+2), \tag{7.100}
$$

其中激发算符 $R$ 具有如下形式：

<a id="eq:R-IP"></a>
$$
\hat{R}=\frac{1}{2}\sum_{ij}r_{ij}ji+\frac{1}{6}\sum_{ijka}r_{ijk}^{a}a^{\dagger}kji. \tag{7.101}
$$

在 EOM-DIP 计算中，参考态通常选取一个性质良好的闭壳层（closed-shell）态。EOM-DIP 是描述具有“$n$ 个轨道中有 $2n-2$ 个电子”这类电子简并的分子的有力工具。此类体系最简单的例子是符合“两个电子占据两个轨道”图像的双自由基（diradicals）。此外，对于“三个轨道中有四个电子”的波函数，或 Auger 衰变（Auger decay）中的价层 $2h$ 态，DIP 更是首选方法。

EOM-DIP-CCSD 方法的精度与其他 EOM-CCSD 模型相当，*i.e.*，约为 0.1–0.3 eV。EOM-DIP-CCSD 的计算标度为 ${\cal{O}}({N^{6}})$，与其他 EOM-CCSD 方法类似。不过，其计算成本相对于（*e.g.*）EOM-EE-CCSD 而言更低，并且随基组（Basis Set）规模的增大而上升得更缓慢。要发起一次 EOM-DIP 计算，可使用 DIP_STATES，或 DIP_SINGLETS 与 DIP_TRIPLETS。
在特定情形下，也可以使用 DIP_AA_STATES、DIP_BB_STATES、DIP_BA_STATES 这些关键词。

**注意：

如果参考态相对于电子剥离（electron detachment）不稳定，EOM-DIP 的表现可能不佳。详见第 [7.9.13](sec_CAGE.md) 节。
**

**注意：

在 EOM-DIP-CCSD 的某些应用中，EOM 部分只包含 2$h$ 算符。这类计算对应于 EOM_PRECONV_DOUBLES = TRUE 计算所得到的能量。
**

（已保存至 `/Users/wxyhgk/Documents/Quamtum_Chemistry_md/QChem/7.9.7_EOM-DIP-CCSD_zh.md`）
