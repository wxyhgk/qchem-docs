---
title: "4.1.1 概述"
---

## 4.1.1 概述

(July 4, 2026)

理论“模型化学”（model chemistries）涉及两项主要近似。首先必须指定用于构造分子轨道（molecular orbitals, MOs）的原子轨道（atomic orbital, AO）基组（Basis Set）类型，即通过“原子轨道线性组合”（linear combination of atomic orbitals, LCAO）*假设*（ansatz），其可用选项在第 [8 章](../ch08_basis/chap_basis.md) 中讨论。其次，必须指定处理电子之间瞬时相互作用（“电子相关”，electron correlation）的方式。自洽场（Self-consistent field, SCF）方法以平均场（mean-field）的方式描述电子相关，是最简单、最经济且应用最广泛的电子结构方法。SCF 方法类别既包含 Hartree-Fock（HF）理论，也包含 Kohn-Sham（KS）密度泛函理论（Density Functional Theory, DFT）。本章概述 **Q-Chem** 的 SCF 功能，而第 [5 章](../ch05_dft/chap_DFT.md) 提供 DFT 计算的更多具体细节。第 [6 章](../ch06_correlation/chap_correlation.md) 介绍了更为精细（但计算代价也更高！）的、基于波函数的后 HF（post-HF）电子相关方法。如果您是量子化学新手，我们建议先阅读入门教科书，如参考文献  、  或  。

第 [4.2 节](sec_SCF_theory.md) 提供 SCF 方法（包括 HF 和 KS-DFT）的理论背景。从某种意义上说，前者可视为后者的一个特例，且作业控制 *$rem* 变量在两种情况下大致相同。基本的 SCF 作业控制见第 [4.3 节](sec_SCF_job-control.md)。后续各节介绍更为专门的选项，可按需查阅。尤其值得注意的有以下几项：

- SCF 计算的初始猜测（initial guess）（第 [4.4 节](sect_initialguess.md)）。当 SCF 计算不收敛时，建议修改猜测。
- 当 SCF 计算不收敛时，改变 SCF 收敛算法（第 [4.5 节](sect_convergence.md)）也是一种不错的策略。
- 针对大体系，提供了线性标度（linear-scaling）、“${\cal{O}}({N})$” 及其他低成本方法（见第 [4.6 节](sec_O_N.md)）。
- 非常规 SCF 计算。一些具有新颖物理和数学特征的非标准 SCF 方法也可用。这些方法包括：

- 双基组（dual-basis）SCF 计算（第 [4.7 节](sect_dualbasis.md)）以及 DFT 微扰理论（第 [4.8 节](sect_HFPC.md)），它们有助于获得大基组级别的质量结果，但只需在较小的基组中进行自洽迭代。
- SCF 元动力学（meta-dynamics）（第 [4.9.2 节](sec_SCF-meta-dyn.md)），可用于寻找 SCF 方程的多个解，并帮助检验所获得的解是否确实是最低极小值。

其中一些非常规 SCF 方法为 **Q-Chem** 所独有。
