---
title: "7.10.2 代数图解构造（ADC）方案"
---

## 7.10.2 代数图解构造（ADC）方案

（2026 年 7 月 4 日）

极化传播子的代数图解构造（Algebraic Diagrammatic Construction, ADC）是一种源于格林函数（Green's function）理论的激发态方法。它最初是通过对极化传播子进行图解微扰展开、并采用哈密顿量的 Møller-Plesset 分区推导而来的。[[1210]](../bib_references/bib.md#bib1262)
另一种推导方式则基于中间态表示（Intermediate State Representation, ISR），[[1209]](../bib_references/bib.md#bib1264)
下面将介绍后者。

通过 ISR 推导 ADC 方程的出发点是精确的 $N$ 电子基态 $\left|\Psi_{0}^{N}\right>$。从 $\left|\Psi_{0}^{N}\right>$ 出发，作用物理激发算符 $\hat{C}_{J}$ 即可得到一组完备的关联激发态。

<a id="eq:adc_pp_precursor_states"></a>
$$
\left|\bar{\Psi}_{J}^{N}\right>=\hat{C}_{J}\left|\Psi_{0}^{N}\right> \tag{7.133}
$$

其中

<a id="eq:adc_pp_excitation_operator"></a>
$$
\left\{\hat{C}_{J}\right\}=\left\{c^{\dagger}_{a}c_{i};c^{\dagger}_{a}c^{\dagger}_{b}c_{i}c_{j},i<j,a<b;\ldots\right\} \tag{7.134}
$$

然而，所得到的激发态并不构成正交归一基。为了从 $|\bar{\Psi}_{J}^{N}\rangle$ 构造一组正交归一基，从精确基态、单激发态、双激发态等出发，依次对各激发类中的激发态采用 Gram-Schmidt 正交化方案。这一过程最终给出中间态基 $\{|\tilde{\Psi}_{J}^{N}\rangle\}$，在该基下体系的哈密顿量可以表示为一个厄米的 ADC 矩阵

<a id="Ch7.E135"></a>
$$
M_{IJ}=\left<\tilde{\Psi}_{I}^{N}\right|\hat{H}-E_{0}^{N}\left|\tilde{\Psi}_{J}^{N}\right> \tag{7.135}
$$

这里，体系的哈密顿量以精确基态能量 $E_{0}^{N}$ 进行了平移。求解 ISR 长期方程（secular equation）

<a id="Ch7.E136"></a>
$$
\mathbf{M}\mathbf{X}=\mathbf{X}\mathbf{\Omega},\;\;\text{ with }\;\;\mathbf{X}^{\dagger}\mathbf{X}=\mathbf{1} \tag{7.136}
$$

可得精确激发能 $\Omega_{n}$ 作为本征值。由本征矢量可以按中间态的形式构造出精确的激发态

<a id="Ch7.E137"></a>
$$
\left|\Psi_{n}^{N}\right>=\sum_{J}X_{nJ}\left|\tilde{\Psi}_{J}^{N}\right> \tag{7.137}
$$

这同时也使得偶极跃迁矩可以通过下式计算

<a id="Ch7.E138"></a>
$$
T_{n}=\left<\Psi_{n}^{N}\right|\hat{\mu}\left|\Psi_{0}^{N}\right>=\sum_{J}X_{nJ}^{\dagger}\left<\tilde{\Psi}_{J}^{N}\right|\hat{\mu}\left|\Psi_{0}^{N}\right>, \tag{7.138}
$$

以及激发态性质可以通过下式计算

<a id="Ch7.E139"></a>
$$
O_{n}=\left<\Psi_{n}^{N}\right|\hat{o}\left|\Psi_{n}^{N}\right>=\sum_{I,J}X_{nI}^{\dagger}X_{nJ}\left<\tilde{\Psi}_{I}^{N}\right|\hat{o}\left|\Psi_{J}^{N}\right>, \tag{7.139}
$$

其中 $O_{n}$ 是与算符 $\hat{o}$ 相关联的性质。

迄今为止，在 ADC 方案的推导中使用的都是精确的 $N$ 电子基态，由此得到的是精确的激发能和精确的激发态波函数。由于精确基态通常是未知的，在推导 ISR 方程时必须采用合适的近似。一个显而易见的选择是 $n$ 阶 Møller-Plesset 基态，这样就得到了 ADC 方案的 $n$ 阶近似。相应的 ADC 方程已被详细推导至三阶。[[1371]](../bib_references/bib.md#bib1432)

由于依赖于 Møller-Plesset 基态，$n$ 阶 ADC 方案只应应用于那些基态能够由相应的 MP($n$) 方法良好描述的分子体系。

与 Møller-Plesset 微扰理论类似，第一个超越第 [7.2](sect_noncorr.md) 节中非关联波函数方法的 ADC 方案是 ADC(2)。ADC(2) 有 *严格（strict）* 和 *扩展（extended）* 两种变体，通常分别记作 ADC(2)-s 和 ADC(2)-x。严格变体 ADC(2)-s 的计算量随基组大小的五次方 scaling（标度）。ADC(2)-s 的激发能及相应激发态的质量与 CIS(D)（第 [7.8](sect_excorr.md) 节）或 CC2 所得结果相当。更准确地说，以单激发组分为主的激发态能够被 ADC(2)-s 良好描述，而具有双激发组分的激发态其能量通常偏高。ADC(2)-x 变体的计算量随基组的六次方标度，改善了对双激发态的处理，但代价是在单激发态与双激发态之间引入了不平衡。其结果是，与主要具有单激发特征的态相比，ADC(2)-x 中双激发态的激发能被显著降低，而两类态的激发能都存在相对较大的误差。尽管如此，通过与 ADC(2)-s 结果进行比较，ADC(2)-x 计算可以用作诊断低能谱区中双激发态重要性的工具。对单激发态和双激发态都明显更好的描述由三阶 ADC 方案 ADC(3) 提供。ADC(3) 所得激发能的精度几乎可与 CC3 相媲美，而计算量仅随基组的六次方标度。[[528]](../bib_references/bib.md#bib542)
