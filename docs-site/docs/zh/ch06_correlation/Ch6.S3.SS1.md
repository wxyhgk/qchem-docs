---
title: "6.3.1 概述"
---

## 6.3.1 概述

(July 4, 2026)

Møller-Plesset 微扰理论（Møller-Plesset Perturbation Theory）[[957]](../bib_references/bib.md#bib998)
 是一种被广泛使用的、用于近似分子相关能的方法。特别而言，
二阶 Møller-Plesset 微扰理论（MP2）是超越 Hartree-Fock 近似之后
最简单且最有用的理论层次之一。**Q-Chem** 中提供的常规 MP2 方法与局域 MP2 方法
分别在 [6.4](sect_exactmp.md) 节与 [6.5](topic_lmp2.md) 节中详细讨论。MP3 方法仍偶尔被使用，
而 MP4 计算则相当常见地被用作 G2 与 G3 热化学方法的一部分。[[296]](../bib_references/bib.md#bib297)
 本节余下部分将回顾 Møller-Plesset 理论的理论基础。

Hartree-Fock 波函数 $\Psi_{0}$ 与能量 $E_{0}$ 是精确 Hamiltonian 本征值问题
（即 Schrödinger 电子波方程，见式 ([4.5](../ch04_scf/Ch4.S2.SS1.md#eq404))）的
*近似*解（本征函数与本征值）。不过，HF 波函数与能量对于
Hartree-Fock Hamiltonian $H_{0}$ 的本征值问题而言是精确解。若我们假设
Hartree-Fock 波函数 $\Psi_{0}$ 与能量 $E_{0}$ 接近精确波函数 $\Psi$ 与能量 $E$，
则现在可以将精确 Hamiltonian 算符写为

<a id="eq500"></a>
$$
H=H_{0}+\lambda V \tag{6.1}
$$

其中 $V$ 为微扰项，$\lambda$ 为无量纲参数。
将精确波函数与能量按 HF 波函数与能量展开，可得

<a id="eq501"></a>
$$
E=E^{(0)}+\lambda E^{(1)}+\lambda^{2}E^{(2)}+\lambda^{3}E^{(3)}+\ldots \tag{6.2}
$$

以及

<a id="eq02"></a>
$$
\Psi=\Psi_{0}+\lambda\Psi^{(1)}+\lambda^{2}\Psi^{(2)}+\lambda^{3}\Psi^{(3)}+\ldots \tag{6.3}
$$

将这些展开式代入 Schrödinger 方程，并按 $\lambda$ 的幂次整理各项，可得

<a id="eq503"></a>
$$
H_{0}\Psi_{0}=E^{(0)}\Psi_{0} \tag{6.4}
$$

<a id="eq504"></a>
$$
H_{0}\Psi^{(1)}+V\Psi_{0}=E^{(0)}\Psi^{(1)}+E^{(1)}\Psi_{0} \tag{6.5}
$$

<a id="eq505"></a>
$$
H_{0}\Psi^{(2)}+V\Psi^{(1)}=E^{(0)}\Psi^{(2)}+E^{(1)}\Psi^{(1)}+E^{(2)}\Psi_{0} \tag{6.6}
$$

依此类推。将上述每个方程左乘 $\Psi_{0}$ 并对全空间积分，即可得到 $n$ 阶
（MP$n$）能量的如下表达式：

<a id="eq506"></a>
$$
E^{(0)}=\langle{\Psi_{0}}|H_{0}|{\Psi_{0}}\rangle \tag{6.7}
$$

<a id="eq507"></a>
$$
E^{(1)}=\langle{\Psi_{0}}|V|{\Psi_{0}}\rangle \tag{6.8}
$$

<a id="eq508"></a>
$$
E^{(2)}=\left\langle{\Psi_{0}}|V|{\Psi^{(1)}}\right\rangle \tag{6.9}
$$

因此，Hartree-Fock 能量

<a id="eq509"></a>
$$
E_{0}=\left\langle{\Psi_{0}}\right|H_{0}+V\left|{\Psi_{0}}\right\rangle \tag{6.10}
$$

恰好是零阶能量与一阶能量之和

<a id="eq510"></a>
$$
E_{0}=E^{(0)}+E^{(1)} \tag{6.11}
$$

于是相关能可以写为

<a id="eq511"></a>
$$
E_{\mathrm{corr}}=E_{0}^{(2)}+E_{0}^{(3)}+E_{0}^{(4)}+\ldots \tag{6.12}
$$

其中第一项即为 MP2 能量。

可以证明，MP2 能量可以（用自旋轨道的形式）写为

<a id="eq512"></a>
$$
E_{0}^{(2)}=-\frac{1}{4}\sum_{ab}^{\mathrm{virt}}{\sum_{ij}^{\mathrm{occ}}{\frac{\left|{\left\langle{ab}\right|\left|{ij}\right\rangle}\right|^{2}}{\varepsilon_{a}+\varepsilon_{b}-\varepsilon_{i}-\varepsilon_{j}}}} \tag{6.13}
$$

其中

<a id="eq513"></a>
$$
\left\langle ab||ij\right\rangle=\left\langle ab|ij\right\rangle-\left\langle
ab|ji\right\rangle \tag{6.14}
$$

且

<a id="eq514"></a>
$$
\left\langle{ab}|{cd}\right\rangle=\int\int\psi_{a}(\mathbf{r}_{1})\psi_{c}(\mathbf{r}_{1})\frac{1}{r_{12}}\psi_{b}(\mathbf{r}_{2})\psi_{d}(\mathbf{r}_{2})d\mathbf{r}_{1}d\mathbf{r}_{2} \tag{6.15}
$$

该式可以用二电子排斥积分表示为

<a id="eq515"></a>
$$
\left\langle{ab}|{cd}\right\rangle=\sum_{\mu}\sum_{\nu}\sum_{\lambda}\sum_{\sigma}C_{\mu a}C_{\nu c}C_{\lambda b}C_{\sigma d}\left(\mu\nu|\lambda\sigma\right) \tag{6.16}
$$

更高阶项的表达式形式类似，但其代数复杂度与计算复杂度要大得多。MP3 以及尤其是 MP4
（即相关能的三阶与四阶贡献）都偶尔会被使用，不过它们正日益被后续章节所描述的
耦合簇（coupled-cluster）方法所取代。MP3 对磁盘与内存的需求与
[6.12](topic_ccsd.md) 节讨论的自洽对关联（self-consistent pair correlation）方法相似，
而 MP4 的计算开销则与 [6.13](topic_ccni.md) 节讨论的 (T) 修正相似。
