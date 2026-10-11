---
title: "7.9.6 用于双自由基与三自由基的自旋翻转方法"
---

## 7.9.6 用于双自由基与三自由基的自旋翻转方法

（2026 年 7 月 4 日）

自旋翻转（Spin-Flip, SF）方法[[726]](../bib_references/bib.md#bib757)

用于解决因 HOMO-LUMO 能隙过小而给波函数的单行列式描述带来的问题。闭壳层单重态与开壳层单重态均可在单一参考下描述，即将其视为从三重态参考态出发的自旋翻转（例如 $\alpha\rightarrow\beta$）激发；相对于对应的单重态而言，该三重态参考的动力学关联与非动力学关联效应都更小。这是因为由自旋相同电子之间的泡利（Pauli）不相容原理所产生的交换空穴（exchange hole），可以部分补偿平均场 Hartree–Fock 模型对库仑空穴（coulomb hole）描述不佳的问题。此外，由于两个 $\alpha$ 电子无法成键，当核间距离被拉伸时不会发生断键，三重态波函数基本上仍保持单参考的特征。自旋翻转方法在描述双自由基、三自由基以及某些问题重重的双重态方面也已被证明十分有用。

自旋翻转方法可用于 CIS、CIS(D)、CC2、CISD、CISDT、OD、CCSD、EOM-(2,3) 以及 CCSDT 理论级别，同时也支持自旋完备（spin complete）的 SF-XCIS（见第 [7.2.3.2](Ch7.S2.SS3.md#topic:sf) 节）。还提供了 ${\cal{O}}({N^{7}})$ 量级的非迭代三重激发修正——例如 (dT) 与 (fT)。
对于 OD 和 CCSD 模型，还可计算以下非松弛（non-relaxed）性质：偶极矩、跃迁偶极矩、自旋-轨道耦合（SOCs）、自旋平方算符的本征值（$\langle\hat{S}^{2}\rangle$）以及密度。SF-CIS 和 EOM-SF-CCSD 方法还可解析梯度。由 EOM-SF 波函数构造 Heisenberg 空间与 Hubbard 空间中的有效哈密顿量，将在第 [13.6](../ch13_specialized/sec_EffHam.md) 节中介绍。要发起自旋翻转计算，需使用 *$rem* 段中的 SF_STATES，并配合所选关联级别的相应 *$rem* 设置——通过 METHOD（推荐使用）或使用较旧的关键词（CORRELATION，以及可选的 EOM_CORR）。请注意，应当使用高多重度的三重态或四重态参考态。

还实现了几种双重自旋翻转（double SF）方法。[[207]](../bib_references/bib.md#bib200)

要调用这些方法，请使用 DSF_STATES。
