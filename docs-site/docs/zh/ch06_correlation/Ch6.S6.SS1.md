---
title: "6.6.1 引言"
---

## 6.6.1 引言

（2026 年 7 月 4 日）

对于尺寸固定的分子，增加*每个原子*的基函数数目 $n$，会导致重要的四中心双电子积分数目以 ${\cal{O}}({n^{4}})$ 的规模增长，因为不可忽略的乘积电荷分布 $|\mu\nu\rangle$ 的数目以 ${\cal{O}}({n^{2}})$ 的规模增长。其结果是，使用大尺寸（高质量）基组展开在计算上代价高昂。或许克服这一“基组质量”瓶颈最实用的途径，就是采用辅助基组展开。[[387]](../bib_references/bib.md#bib395)

能够利用辅助基组来加速各类电子关联方法（包括能量计算与解析梯度计算），是 **Q-Chem** 的一项重要特性。

辅助基组 $\{|K\rangle\}$ 用于近似高斯基组函数的乘积：

<a id="Ch6.E25"></a>

$$
|\mu\nu\rangle\approx|\widetilde{\mu\nu}\rangle=\sum_{K}|K\rangle C_{\mu\nu}^{K} \tag{6.25}
$$

辅助基组展开早已提出，如今被广泛认可为一种行之有效且强大的方法，有时也被同义地称为恒等分辨（resolution of the identity, RI）或密度拟合（density fitting, DF）。采用辅助基组展开时，大规模电子结构计算的计算代价随 $n$ 的增长速率可降低至大约 $n^{3}$。

若 $n$ 固定而分子尺寸增大，辅助基组展开会降低计算所对应的前置因子（pre-factor），而不改变标度关系。关键在于前置因子可以减少 5 倍、10 倍甚至更多。之所以能够实现如此大幅度的加速，是因为已证明：达到合理精度所需的辅助函数数目 $X$ 仅约为 $N$ 的 3 到 4 倍。

辅助基组展开系数 $\mathbf{C}$ 由最小化拟合分布与真实分布之间的偏差 $\langle\mu\nu-\widetilde{\mu\nu}|{\mu\nu-\widetilde{\mu\nu}}\rangle$ 来确定，由此得到如下线性方程组：

<a id="Ch6.E26"></a>

$$
\sum_{L}{\left\langle{K\left|L\right.}\right\rangle}C_{\mu\nu}^{L}=\left\langle{K\left|{\mu\nu}\right.}\right\rangle \tag{6.26}
$$

显然，求解拟合方程只需要二中心和三中心积分，因此（四中心的）双电子积分可近似表示为如下针对给定辅助基组选择的最优表达式：

<a id="Ch6.E27"></a>

$$
\langle\mu\nu|\lambda\sigma\rangle\approx\langle\widetilde{\mu\nu}|\widetilde{\lambda\sigma}\rangle=\sum_{K,L}C_{\mu\nu}^{L}\langle L|K\rangle C_{\lambda\sigma}^{K} \tag{6.27}
$$

在辅助基组完备的极限情况下（*即* 包含原子轨道的所有乘积），上述拟合过程将是精确的。然而实际上辅助基组总是不完备的（如前所述，$X\approx 3N)$，因为这正是提升计算效率的关键所在。

Karlsruhe 研究小组为二阶微扰（MP2）关联能计算开发了标准化的辅助基组。[[1439]](../bib_references/bib.md#bib1501)
 使用这些基组时，关联能的绝对误差很小（*e.g.*，低于每原子 60 $\mu$Hartree），而相对能量的误差则更小。与此同时，可实现 3–30$\times$ 的加速。这一进展使得在电子关联计算中常规使用辅助基组成为可能。

能够利用辅助基组展开的关联计算方法将在本节其余部分（MP2 及类 MP2 方法）以及第 [6.19](sect_pairing.md) 节（简化活性空间耦合簇方法，如 PP、PP(2)、IP、RP）中介绍。当通过
AUX_BASIS_CORR 或
AUX_BASIS 关键字提供有效的辅助基组选择时，这些方法会自动采用辅助基组展开，其用法与 BASIS
关键字相同。
此处不再需要 PURECART *$rem*，即使所使用的辅助基组没有预定义的值也是如此。
在这类情况下，内置的自动化过程默认即可实现 PURECART *$rem* 的效果。
