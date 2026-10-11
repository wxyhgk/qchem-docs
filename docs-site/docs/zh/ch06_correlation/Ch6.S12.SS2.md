---
title: "6.12.2 耦合簇单激发与双激发方法 (CCSD)"
---

## 6.12.2 耦合簇单激发与双激发方法（Coupled Cluster Singles and Doubles, CCSD）

(2026 年 7 月 4 日)

以自洽方式处理对关联（pair correlations）的标准方法是耦合簇（coupled-cluster）方法，其簇算符（cluster operator）包含所有单激发与双激发替换，[[1138]](../bib_references/bib.md#bib1186)
 简称为 CCSD。对于稳定闭壳层（closed-shell）分子的几何结构与振动频率，CCSD 给出的结果仅略优于 MP2。然而，对于反应性物种，如过渡态结构（transition structures）和自由基（radicals），MP2 的表现相当不稳定，而 CCSD 则具有显著的优势。

完整教科书式的 CCSD 阐述超出了本手册的范围，且已有若干全面的参考文献可供查阅。不过，简要概述其主要方程可能仍有所裨益。CCSD 波函数为：

<a id="eq518"></a>

$$
\left|{\Psi_{\mathrm{CCSD}}}\right\rangle=\exp\left({\hat{T}_{1}+\hat{T}_{2}}\right)\left|{\Phi_{0}}\right\rangle \tag{6.58}
$$

其中单激发与双激发算符可通过其作用于参考单行列式（在 CCSD 中通常取 Hartree-Fock 行列式）的效果来定义：

<a id="eq519"></a>

$$
\hat{T}_{1}\left|{\Phi_{0}}\right\rangle=\sum_{i}^{\mathrm{occ}}{\sum_{a}^{\mathrm{virt}}{t_{i}^{a}}}\left|{\Phi_{i}^{a}}\right\rangle \tag{6.59}
$$

<a id="eq520"></a>

$$
\hat{T}_{2}\left|{\Phi_{0}}\right\rangle=\frac{1}{4}\sum_{ij}^{\mathrm{occ}}{\sum_{ab}^{\mathrm{virt}}{t_{ij}^{ab}}}\left|{\Phi_{ij}^{ab}}\right\rangle \tag{6.60}
$$

由于 $\langle E\rangle_{\mathrm{CCSD}}$ 表达式终止于与完全组态相互作用（full configuration interaction）相同的复杂度级别（！），因此无法通过对单激发与双激发振幅（amplitudes）进行变分最小化来确定 CCSD 能量。所以，取而代之的是在由参考行列式、所有单激发替换以及所有双激发替换所张成的子空间中满足薛定谔方程（Schrödinger equation）。用这些函数进行投影并对全空间积分，即可提供足够的方程组，将能量以及单、双激发振幅作为一组非线性方程组的解来确定。这些方程可符号化地写为如下形式：

<a id="A3.S8.EGx22"></a>

$$
\displaystyle E_{\mathrm{CCSD}} \tag{6.61}
$$

其结果是一组方程，由此得到的能量不一定具有变分性（*即*，未必高于真实能量），但它是严格尺寸一致（size-consistent）的。这些方程对于双电子体系也是精确的；并且在分子可视为相互作用电子对集合的程度上，这正是预期 CCSD 结果具有实用精度的依据。

在基组（Basis Set）选择固定的情况下，求解 CCSD 方程所需的计算量随分子尺寸的六次方 Scaling。磁盘存储空间随分子尺寸的四次方扩展，涉及多组双激发振幅以及分子轨道基下的双电子积分。因此，相对于 MP2 理论所提升的精度是以高昂的计算代价换来的。基于这些标度关系，若先对较小体系进行试算，则相对容易地估计在更大分子（或更大基组）上进行 CCSD 计算的可行性（或不可行性）。
**Q-Chem** 针对 RHF 和 UHF 参考（包括冻结核心，frozen core）同时支持 CCSD 能量与解析梯度。对于 ROHF，仅提供能量和非弛豫性质（unrelaxed properties）。
可用的性质包括偶极矩、角动量投影、$\langle\hat{S}^{2}\rangle$、静态极化率（static polarizabilities）以及 g 张量（详见第 [7.9.21](../ch07_excited/sec_EOMGRAD.md) 节）。
