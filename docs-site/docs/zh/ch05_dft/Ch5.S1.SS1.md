---
title: "5.1.1 概述"
---

## 5.1.1 概述

（2026 年 7 月 4 日）

密度泛函理论（Density Functional Theory, DFT）[[700]](../bib_references/bib.md#bib733)

已成为量子力学分子研究中一种精确的、替代性的第一性原理方法。DFT 计算占据了全部量子化学计算的绝大多数，这不仅是因为其已被证实的化学精度（chemical accuracy），还因为其计算成本相对较低——与 Hartree-Fock 理论相当，但却包含了 HF 计算中所忽略的电子关联（electron correlation）处理。这两大特点表明，DFT 很可能将在未来很长一段时间内继续成为量子化学家工具箱中的领先方法。**Q-Chem** 为所有流行的密度泛函提供了快速、高效且精确的算法，使得对大分子进行计算成为可能且具有实用性。

DFT 主要是一种基于电子密度 $\rho(\mathbf{r})$（而非多电子波函数 $\Psi(\mathbf{r}_{1},\ldots,\mathbf{r}_{N})$）的电子基态结构理论。（其激发态推广形式——含时密度泛函理论（time-dependent DFT）——将在第 [7.3 节](../ch07_excited/sect_tddft.md) 中讨论。）传统波函数方法与现代 DFT 方法论之间存在诸多明显的异同。首先，多电子波函数 $\Psi$ 的基本构成单元是单电子轨道（single-electron orbitals），它与 DFT 框架中的 Kohn-Sham 轨道直接类似。其次，电子密度和多电子波函数通常都通过自洽场（SCF）方法构造，而该方法所需的矩阵元构造在形式上极为相似。

然而，以多电子波函数为基础的传统 *ab initio* 方法必须借助 SCF 之后的后处理计算（第 [6 章](../ch06_correlation/chap_correlation.md)）来纳入关联效应，而 DFT 方法则在 SCF 层面就已纳入关联。微扰理论（perturbation theory）或耦合簇理论（coupled-cluster theory）等 SCF 后（Post-SCF）方法，相对于 SCF 流程而言计算代价极其高昂。另一方面，尽管 DFT 方法在原则上是精确的，但在实践中它依赖于对一个未知的交换-关联（exchange-correlation）能量泛函进行建模。虽然更精确的泛函形式在不断被发展，但并不存在系统性地改进泛函以达到任意精度等级的方法。因此，传统方法提供了实现可系统性提升的精度等级的可能性，但计算需求可能很高；而 DFT 方法提供了一条切实可行的途径，但其理论目前尚不完整。
