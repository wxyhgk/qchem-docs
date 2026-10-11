---
title: "6.23.1 引言"
---

## 6.23.1 引言

（2026 年 7 月 4 日）

本节所介绍的方法涉及对二电子约化密度矩阵（two-electron reduced-density matrix，2-RDM，${}^{2}\mathbf{D}$）的直接变分优化，并施加必要的系综 $N$-可表示性（ensemble $N$-representability）条件。[[431]](../bib_references/bib.md#bib441)

此类条件对 2-RDM 施加限制，以确保其可由 $N$ 电子密度矩阵的系综导出。若对 2-RDM 的 $N$-可表示性加以精确强制，则变分 2-RDM（variational 2-RDM，v2RDM）方法与全组态相互作用（full configuration interaction，全 CI）等价。这类计算通常在计算上不可行，因此 v2RDM 优化一般只在若干二粒子或三粒子条件的子集下进行。当仅部分强制 $N$-可表示性时，v2RDM 方法给出全 CI 能量的下界。

在 **Q-Chem** 中，所有 v2RDM 优化均在以下条件下进行：

- •

2-RDM 是半正定的
- •

单电子约化密度矩阵（one-electron reduced-density matrix，1-RDM）是半正定的
- •

2-RDM 的迹等于电子对数 $N(N-1)$
- •

2-RDM 的每个自旋块能正确地收缩到 1-RDM 相应的自旋块
- •

$\hat{M}_{S}$ 的期望值为 $\frac{1}{2}(N_{\alpha}-N_{\beta})$（最大自旋投影）

此外，可以对 2-RDM 施加可选的自旋约束，使得 $\langle\hat{S}^{2}\rangle=S(S+1)$（以 $\hbar^{2}$ 为单位），其中 $S$ 为自旋量子数。请注意，对 $\hat{S}^{2}$ 期望值的这一约束并不能严格保证 2-RDM 对应于 $\hat{S}^{2}$ 的本征函数。若没有额外的约束，v2RDM 优化会得到质量低劣的 2-RDM，其能量远低于全 CI 的结果。要获得合理的结果，至少需要强制额外的对概率密度矩阵（pair-probability density matrices）的正性，包括两空穴约化密度矩阵（two-hole reduced-density matrix，${}^{2}\mathbf{Q}$）和粒子-空穴约化密度矩阵（particle-hole reduced-density matrix，${}^{2}\mathbf{G}$）。${}^{2}\mathbf{D}$、${}^{2}\mathbf{Q}$ 与 ${}^{2}\mathbf{G}$ 的正性构成了 Garrod 与 Percus 提出的 DQG 约束。[[430]](../bib_references/bib.md#bib442)
 对许多体系而言，DQG 约束能够给出对电子结构的合理描述。然而，若追求高精度，有时需要考虑对更高阶约化密度矩阵的约束（*例如* 三电子约化密度矩阵 [3-RDM]）。在 **Q-Chem** 中，v2RDM 优化可以在 T1 与 T2 部分三粒子条件（partial three-particle conditions）[[369]](../bib_references/bib.md#bib372)
 下进行，这些条件并不显式依赖于 3-RDM；也可以在全 3-正性（full 3-positivity）条件下进行，后者包括三粒子约化密度矩阵（${}^{3}\mathbf{D}$）、三空穴约化密度矩阵（${}^{3}\mathbf{Q}$）、二粒子-一空穴约化密度矩阵（${}^{3}\mathbf{E}$）以及一粒子-二空穴约化密度矩阵（${}^{3}\mathbf{F}$）。全 3-正性条件可自动保证各部分条件成立。[[929]](../bib_references/bib.md#bib967)

v2RDM 计算中所施加的正性条件通过 *$rem* 变量 RDM_POSITIVITY 控制。

v2RDM 方法的主要用途在于基于活性空间（active space）的强关联（非动力学关联）描述。描述强关联最常用的活性空间方法是完备活性空间自洽场（complete active space self-consistent field，CASSCF）方法。通过在活性空间内进行 v2RDM 计算，并将 v2RDM 与轨道优化程序相耦合，可以得到一种 v2RDM 驱动的 CASSCF 程序[[441]](../bib_references/bib.md#bib452)
，它给出常规基于 CI 的 CASSCF 能量的下界。由于 v2RDM-CASSCF 方法相对于活性轨道数目呈多项式标度，与 CI-CASSCF（*例如*，18 个电子分布在 18 个轨道中）相比，v2RDM-CASSCF 能够处理大得多的活性空间（*例如*，50 个电子分布在 50 个轨道中）。

请注意，v2RDM-CASSCF 仅描述活性轨道之间的电子关联。对其余关联效应，可以通过多组态对密度泛函理论（multiconfiguration pair-density functional theory，MC-PDFT）方法[[886]](../bib_references/bib.md#bib920)
获得计算代价低廉的估计，该方法将能量表示为于顶对密度（on-top pair density，OTPD）的泛函。在 **Q-Chem** 的 MC-PDFT 实现中，OTPD 由变分优化后的 2-RDM 导出，如文献 [[966]](../bib_references/bib.md#bib1007)
 所述。

目前的 v2RDM、v2RDM-CASSCF 与 MC-PDFT 实现必须对二电子积分使用密度拟合（density fitting，DF）近似。对于具有大活性空间的 v2RDM-CASSCF 计算，由于轨道优化/积分变换步骤的效率提升，使用 DF 积分尤其有利。若未设置 *$rem* 关键字 AUX_BASIS，v2RDM 计算将会失败。当请求冻结分子轨道（frozen molecular orbitals）时，无法使用解析梯度。活性空间的指定方式在下方的示例中演示。当请求格式化检查点文件（formatted checkpoint file）时，自然轨道会保存在其中。
