---
title: "6.13.2 (2) 三激发与四激发修正（Triples and Quadruples Corrections）"
---

## 6.13.2 (2) 三激发与四激发修正

（2026 年 7 月 4 日）

尽管上文讨论的 (T) 修正已经取得了非凡的成功，但至少对于某些重要类别的问题，在精度方面仍有进一步提升的空间。(T) 修正中包含了从四阶和五阶 Møller-Plesset 微扰理论中精心挑选的项，同时也包含了因使用已收敛的簇振幅（cluster amplitudes）来计算四阶和五阶项而产生的高阶项。因此，(T) 修正依赖于裸参考轨道（bare reference orbitals）和轨道能，就此而言，其有效性仍然取决于参考行列式（reference determinant）的质量。由于我们修正的是耦合簇（coupled-cluster）解而非单个行列式，这正是 (T) 修正中可以改进的一个方面。(T) 修正的不足在计算上体现为轨道间存在近简并（near-degeneracies）的情形，例如拉长的化学键、某些过渡态（transition states）、开壳层自由基（open shell radicals）以及双自由基（diradicals）。

Steve Gwaltney 教授在 Berkeley 与 Martin Head-Gordon 合作工作期间，提出了一类全新的非迭代修正（non iterative correction），有望在上述类型的问题案例中提升精度。[[507]](../bib_references/bib.md#bib520)
**Q-Chem** 包含了 Gwaltney 对这一新方法的实现，且仅支持能量计算。这一新修正是对耦合簇起始点的真正二阶修正（second-order correction），因此被记为 (2)。它可用于上文讨论的两种簇方法，即 OD(2) 和 CCSD(2)。[[507]](../bib_references/bib.md#bib520)
目前仅可计算能量。

(2) 方法的基础在于：不是将常规哈密顿量（Hamiltonian）拆分为微扰部分与非微扰部分，而是对一个相似变换后的哈密顿量（similarity-transformed Hamiltonian）进行拆分，其定义为 $\tilde{H}=e^{-\hat{T}}\hat{H}e^{\hat{T}}$。在求解簇问题所使用的截断空间（称为 $p$-空间）内（*e.g.*，对于 CCSD 为单激发与双激发空间），耦合簇波函数是 $\tilde{H}$ 的真正本征值。因此，我们将零阶哈密顿量 $\tilde{H}^{(0)}$ 取为 p-空间中的完整 $\tilde{H}$，而在被排除的取代（substitutions）所构成的空间（q-空间）中，我们仅取 $\tilde{H}$ 的一体部分（该部分可以被对角化）。描述 $q$-空间中电子关联的涨落势（fluctuation potential）为 $\tilde{H}-\tilde{H}^{(0)}$，而 (2) 修正随之由二阶微扰理论得出。

(2) 修正所固有的、微扰与非微扰哈密顿量之间项的重新划分，使得该修正与现有的 (T) 修正相比既表现出相似之处，也表现出差异。在二阶层次上有两类高阶关联进入：不仅有三取代（triple substitutions），还有四取代（quadruple substitutions）。四取代采用因子化 ansatz（factorization ansatz）处理，该处理在五阶 Møller-Plesset 理论中是精确的，[[731]](../bib_references/bib.md#bib764)
从而将其计算成本从 $N^{9}$ 降至 $N^{6}$。对于大基组（basis sets），这一成本仍可能高于三取代项的成本——三取代项随分子尺寸的 7 次方标度增长，且其前置因子是通常 (T) 修正的两倍。

这些修正可用于包含 4 到 10 个第一行原子的分子，具体可行性取决于计算资源以及所选基组的大小。早期证据表明，对于强关联（highly correlated）体系，(2) 修正优于 (T) 修正。[[507]](../bib_references/bib.md#bib520)
这体现在改进的势能曲线（potential curves）上，尤其是在长程区域，并且也可能延伸到问题案例中平衡态能量性质与结构性质的改善。要对新的 (2) 修正进行充分测试以对其性能做出总体评估，还需要一段时间。然而，它们显然极具前景，正因如此，**Q-Chem** 中提供了这些方法。
