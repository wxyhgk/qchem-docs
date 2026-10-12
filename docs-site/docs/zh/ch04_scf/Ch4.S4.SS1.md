---
title: "4.4.1 引言"
---

## 4.4.1 引言

(July 4, 2026)

自洽场（SCF）理论中的 Roothaan-Hall 方程与 Pople-Nesbet 方程对于分子轨道系数而言是非线性的。与许多涉及非线性方程的数学问题一样，在采用某种技术搜索数值解之前，必须先生成一个初始猜测（initial guess）。如果猜测质量较差，用于求解数值解的迭代过程可能会收敛得非常缓慢，需要大量迭代；最坏的情况下，该过程甚至可能发散。

因此，在 *ab initio* SCF 计算中，初始猜测的质量至关重要（至少）出于以下两个主要原因：

- 确保 SCF 收敛到合适的基态。SCF 计算往往会收敛到波函数空间中的不同局部极小值，具体取决于初始猜测落在"LCAO 空间"的哪个区域。
- 对于基函数数目众多、每次迭代都需重新计算电子排斥积分（ERIs）的任务，使用一个接近最终解的高质量初始猜测，可以通过减少 SCF 迭代次数而显著缩短总计算时间。

基于上述原因，几乎所有用户迟早都会希望了解用于定制初始猜测的各种可选项。
**Q-Chem** 目前提供以下几种初始猜测选项：

- 原子密度叠加（Superposition of Atomic Densities, SAD）
- 原子势叠加（Superposition of Atomic Potentials, SAP，仅在 GEN_SCFMAN = TRUE 时可用）
- 实时（自动化）原子密度叠加（On-the-fly (automated) Superposition of Atomic Densities, AUTOSAD）
- 纯化的 SAD 猜测（提供分子轨道；SADMO）
- 核心哈密顿量（Core Hamiltonian, CORE）
- 广义 Wolfsberg-Helmholtz（Generalized Wolfsberg-Helmholtz, GWH）
- 从磁盘读取先前求得的分子轨道（MOs）。（READ）
- 在这些猜测中，前六种（SAD、SAP、AUTOSAD、SADMO、CORE、GWH）由程序自动生成，而 READ 选项则允许用户复用以往计算的结果。

关于这些初始猜测的详细讨论，请分别参阅后续各节。
