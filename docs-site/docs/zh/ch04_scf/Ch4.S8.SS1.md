---
title: "4.8.1 引言"
---

## 4.8.1 引言

（2026 年 7 月 4 日）

与第 [4.7](sect_dualbasis.md) 节的双基组方法密切相关但更为通用的，是 Deng 等人[[318]](../bib_references/bib.md#bib322)
发展的 Hartree-Fock 微扰校正（Hartree-Fock Perturbative Correction, HFPC）方法。
一次 HFPC 计算由以下步骤构成：先在较小的一级基组（primary basis）中进行迭代的 HF 计算，随后在较大的二级基组（secondary basis）中仅进行一次 Fock 矩阵构建、对角化与能量求值。在下文中，我们用 HF/basis 表示常规的 HF 计算，用 HFPC/primary/secondary 表示 HFPC 计算。若一级基组含有 $n$ 个基函数，则 $2m$ 电子体系的受限 Hartree-Fock（restricted HF）矩阵元为

<a id="Ch4.E65"></a>

$$
F_{\mu\nu}=h_{\mu\nu}+\sum_{\lambda\sigma}^{n}P_{\lambda\sigma}\left[(\mu\nu|\lambda\sigma)-\frac{1}{2}(\mu\lambda|\nu\sigma)\right] \tag{4.65}
$$

在一级基组中求解 Roothaan-Hall 方程可得到分子轨道及相应的密度矩阵 $\mathbf{P}$。在 HFPC 计算中，随后利用 $\mathbf{P}$ 在含 $N$ 个基函数的更大二级基组中构建新的 Fock 矩阵 $\mathbf{F}^{[1]}$

<a id="eq:F1"></a>

$$
F_{ab}^{[1]}=h_{ab}+\sum_{\lambda\sigma}^{n}P_{\lambda\sigma}\left[(ab|\lambda\sigma)-\frac{1}{2}(a\lambda|b\sigma)\right] \tag{4.66}
$$

其中 $\lambda$、$\sigma$ 表示一级基组函数，$a$、$b$ 表示二级基组函数。对 $\mathbf{F}^{[1]}$ 进行对角化可获得改进的分子轨道及相应的密度矩阵 $\mathbf{P}^{[1]}$。HFPC 能量由下式给出

<a id="eq:EHFPC"></a>

$$
E^{\text{HFPC}}=\sum_{ab}^{N}P^{[1]}_{ab}h_{ab}+\frac{1}{2}\sum_{abcd}^{N}P^{[1]}_{ab}P^{[1]}_{cd}\bigl{[}2(ab|cd)-(ac|bd)\bigr{]} \tag{4.67}
$$

其中 $a$、$b$、$c$、$d$ 均表示二级基组函数。这与双基组 HF（DBHF）的能量求值不同——后者使用的是 $\mathbf{PP}^{[1]}$ 而非 $\mathbf{P}^{[1]}\mathbf{P}^{[1]}$。纳入关于 $\mathbf{PP}^{[1]}$ 的二次项贡献，正是 HFPC 比 DBHF 更精确的关键原因。

与双基组 HF 不同，HFPC 并不要求小基组必须是大基组的真子集，因此可以在任意两个基组之间“跳跃”。在一套涵盖总能量与反应能量的大规模、多样化数据集上对 HFPC 进行的基准研究表明，对于一系列 primary/secondary 基组组合，HFPC 方案可将一级计算的误差降低约两个数量级，而成本仅为完整二级计算的大约三分之一。[[318]](../bib_references/bib.md#bib322)

HFPC 的密度泛函版本（“DFPC”）[[320]](../bib_references/bib.md#bib324)
旨在将使用小基组与小网格的纯 DFT 计算的低成本，与使用大基组和大网格的杂化（hybrid）计算的高精度结合起来。DFPC 方法的动机来自 Nakajima 和 Hirao[[974]](../bib_references/bib.md#bib1015)
的双泛函（dual-functional）方法以及 Tozer 等人的双网格（dual-grid）方案。

将这些特性融合起来便得到了三重微扰：对泛函、对网格以及对基组的微扰。我们把这种方法称为密度泛函“三跳（triple jumping）”方法。
