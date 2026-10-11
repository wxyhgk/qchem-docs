---
title: "7.1.1 概述"
---

## 7.1.1 概述

（2026 年 7 月 4 日）

与基态计算一样，进行一次合适的激发态计算需要恰当选择方法和基组（Basis Set）。从历史上看，有效建模电子激发态方法的发展一直落后于基态处理方法的进展。部分原因在于激发态波函数（wave function）的特征种类繁多，使得在不针对具体分子甚至具体态指定波函数形式的情况下，很难开发出广泛适用的方法。不过近年来，用于处理激发态的单参考（single-reference）*ab initio* 方法层级体系已开始形成。总体而言，**Q-Chem** 包含的方法能够对较低的光学允许态（optically allowed states）给出定性一致的結果，许多情况下还能与实验实现定量一致。对于涉及双电子激发的态，情况则不那么令人满意，但即便如此，有时也能得到合理的结果。此外，某些激发态方法可以处理开壳层（open-shell）波函数，*e.g.* 双自由基（diradicals）和三自由基（triradicals）、电离态和电子附着态等。

在激发态计算中，与基态计算一样，用户必须在计算成本和精度之间做出权衡。本章将 **Q-Chem** 的激发态方法能力归纳为以下几大类：

- •

基于单电子波函数的方法（第 [7.2](sect_noncorr.md) 节）。
这类激发态处理的复杂程度大致与 Hartree-Fock 基态方法相当，即基本上忽略电子相关（electron correlation）。单激发组态相互作用（CIS）是该类型的常用主力方法。CIS 的自旋翻转（spin-flip）变体将其推广到双自由基及其他 HOMO-LUMO 能隙较小的情形。
- •

含时密度泛函理论（Time-Dependent Density Functional Theory, TDDFT，第 [7.3](sect_tddft.md) 节）。TDDFT 是将 DFT 推广到激发态的一种广泛应用的方法。其计算成本仅比 CIS 计算略高，但由于考虑了电子相关，TDDFT 通常能显著提高精度。它同样具有自旋翻转变体（以及其改进版本——混合参考 SF-TDDFT），可用于研究双自由基、三自由基以及化学键断裂。
- •

用于激发态 $\Delta$SCF 态的最大重叠法（Maximum Overlap Method, MOM）（第 [7.7.2](ex_OpSing.md) 节）。该方法克服了 TDDFT 的某些缺陷，特别适用于建模电荷转移（charge-transfer）和里德堡（Rydberg）跃迁以及核心激发态（core-excited states）。
- •

受限开壳层 Kohn-Sham（Restricted Open-Shell Kohn-Sham, ROKS）方法是一种自旋纯化、轨道优化的激发态处理方法（第 [7.7.4](ex_ESROKS.md) 节）。
它在建模电荷转移态和核心激发方面非常精确。
- •

平方梯度最小化（Square Gradient Minimization, SGM）算法可用于收敛 $\Delta$SCF 和 ROKS 激发态。有关实际使用 SGM 的详情见第 [4.5.15](../ch04_scf/sect_SGM-SCF.md) 节。
- •

态目标能量投影（State-Targeted Energy Projection, STEP）算法（第 [7.7.8](ex_ROSTEP.md) 节）可用于 $\Delta$SCF 和 ROKS 激发态。其计算成本低于 SGM，且通常比 MOM 更稳健。
- •

基于波函数的电子相关处理方法（第 [7.8](sect_excorr.md)、[7.10](sect_exadc.md)、[7.11](topic_rasi.md) 和 [7.9](topic_eomcc.md) 节）。
粗略地说，这些方法是第 [6](../ch06_correlation/chap_correlation.md) 章所讨论的基态波函数电子相关方法在激发态上的对应物。它们比第 [7.2](sect_noncorr.md) 节的方法更精确，但计算量也显著更大。这些方法还能描述某些多组态（multi-configurational）波函数，例如 problematic 的双基自由基、双自由基、三自由基等。

**注意：

在大多数相关激发态计算中，核心电子（core electrons）默认被冻结（见第 [6.2](../ch06_correlation/sec_core.md) 节）。
**

一般而言，适用于基态密度泛函理论（Density Functional Theory, DFT）或 Hartree-Fock 计算的基组，同样适合描述价激发态（valence excited states）。然而，许多激发态包含来自弥散里德堡轨道（diffuse Rydberg orbitals）的显著贡献，因此通常建议使用包含附加弥散函数的基组。对于许多有机分子的低层价激发态，6-31+G* 或 aug-cc-pVDZ 基组是一个合理的折中选择。为了描述真正的里德堡激发态，**Q-Chem** 允许用户添加两组或更多组弥散函数（见第 [8](../ch08_basis/chap_basis.md) 章）。例如，6-311(2+)G* 基组在重原子上包含两组弥散函数，通常足以描述价激发态和里德堡激发态。

**Q-Chem** 支持四种主要的激发态计算类型：

- •

**垂直吸收光谱

**这是在地态几何构型下计算分子的激发态，适用于吸收光谱。支持进行垂直吸收计算的方法有：CIS、RPA、XCIS、SF-XCIS、CIS(D)、ADC(2)-s、ADC(2)-x、ADC(3)、RAS-SF、EOM-CCSD 或 EOM-OD，以及 EOM-CCSDT，每种方法将依次讨论。
用于模拟 X 射线吸收光谱的核心激发态计算可以通过 TDDFT 以及 EOM-CCSD 和 ADC 在核层（core-valence separated, CVS）近似下进行（第 [7.12](sec_CoreLevels.md) 节）。所有基于 ADC 和 EOM 的方法都可以与可极化连续介质模型（polarizable continuum model, PCM）结合，按态特异非平衡（state-specific nonequilibrium）方案模拟溶液中的吸收光谱。
大多数 EOM 方法可以与显式溶剂处理相结合，采用经典（QM/MM）和可极化（QM/EFP）嵌入。
- •

**紫外-可见光以外的电子光谱

****Q-Chem** 可计算其他类型的电子光谱，包括电子圆二色性（electronic circular dichroism）、旋光（optical rotations）和双光子跃迁（two-photon transitions）。
还可以扩展到核层光谱。
- •

**可视化

**可以通过附着/脱离密度（attachment/detachment density）分析（适用于 CIS、RPA、TDDFT、ADC、EOM-CC）或绘制跃迁密度（transition density）来可视化激发态（见第 [3](../ch03_inputs/chap_inputs.md) 章和第 [10](../ch10_properties/chap_properties.md) 章中的 *$plots* 说明）。
CIS、EOM-CCSD 和 ADC 方法可以计算跃迁密度。
附着/脱离密度分析的理论基础在本章第 [7.13.2](sect_AttachDetach.md) 节讨论（更多细节见第 [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) 节）。
此外，对于 CCSD 和 EOM-CCSD 波函数，可以计算并绘制从基态和电子激发态电离（ionization）或从电子附着态脱离（detachment）的戴森轨道（Dyson orbitals）。对于
RAS-SF 方法（第 [7.11](topic_rasi.md) 节），可以绘制所计算电子态的自然轨道（natural orbitals）。
- •

**激发态几何优化**

优化激发态势能面上驻点的几何结构，对于理解基态与激发态之间发生的几何弛豫非常有价值。UCIS、RCIS、TDDFT 和 EOM-CCSD 提供解析一阶导数。
激发态优化也可以使用有限差分方法进行，然而这些方法可能非常耗时。
- •

**势能面交叉点的优化**

可以利用 EOM-CCSD、CIS 和 TD-DFT 框架下的解析梯度定位并优化势能面之间的接缝（seams）。
- •

**性质

**可以计算 ADC、EOM-CCSD、EOM-MP2、EOM-OD、RAS-SF 和 CIS 波函数的偶极矩、电子密度的空间范围以及 $\langle\hat{S}^{2}\rangle$ 值等性质。
静态极化率（static polarizabilities）适用于 CCSD、EOM-EE-CCSD 和 EOM-SF-CCSD 方法。
- •

**跃迁性质与态间相互作用

**几乎所有激发态方法都可以计算跃迁偶极矩和振子强度（oscillator strengths）。
EOM-EE-CCSD 和 ADC 方法可计算双光子吸收的矩阵元与截面积。
EOM-CCSD、RAS-SF、CIS 和 TDDFT 波函数可计算自旋-轨道耦合（spin-orbit couplings）及角动量算符的矩阵元。
Dyson 轨道适用于 EOM-CC 波函数。跃迁性质可以在参考态与目标态之间（*e.g.*，HF-CIS）或不同目标态之间（*e.g.*，CIS-CIS 或 CCSD-EOM-CCSD）计算。
- •

**激发态振动分析**

在给定优化后的激发态几何结构下，**Q-Chem** 可以计算驻点处的力常数以预测激发态振动频率。
驻点还可以被表征为极小点、过渡态结构或 $n$ 阶鞍点。
激发态解析振动分析只能使用 UCIS、RCIS 和 TDDFT 方法进行，这些方法有高效的解析二阶导数可用。EOM-CCSD 频率也可以通过解析一阶导数和有限差分求得的二阶导数获得。EOM-OD 频率只能通过有限差分计算获得。

**注意：

EOM-CC 和大多数 CI 代码是 CCMAN 和 CCMAN2 的一部分。CCMAN 是一个正在逐步淘汰的遗留代码。所有新开发和性能增强特性都在 CCMAN2 中实现。
**

METHOD

### `METHOD`

> **指定计算的理论级别。**
>
> * **类型**: `STRING`
> * **默认值**: `None`
> * **选项**:
>     * CIS
>     * 第
>     * 7.2.2
>     * 节
>     * CIS(D)
>     * 第
>     * 7.8.2
>     * 节
>     * RI-CIS(D)
>     * 第
>     * 7.8.3
>     * 节
>     * SOS-CIS(D)
>     * 第
>     * 7.8.4
>     * 节
>     * SOS-CIS(D0)
>     * 第
>     * 7.8.5
>     * 节
>     * CISD
>     * 第
>     * 7.9.3
>     * 节
>     * CISDT
>     * 第
>     * 7.9.3
>     * 节
>     * EOM-OD
>     * 第
>     * 7.9.3
>     * 节
>     * EOM-CC2
>     * 第
>     * 7.9.4
>     * 节
>     * EOM-CCSD
>     * 第
>     * 7.9.3
>     * 节
>     * EOM-CCSDT
>     * 第
>     * 7.9.23
>     * 节
>     * EOM-MP2
>     * 第
>     * 7.9.5.1
>     * 节
>     * EOM-MP2T
>     * 第
>     * 7.9.5.1
>     * 节
>     * EOM-CCSD-S(D)
>     * 第
>     * 7.9.5.2
>     * 节
>     * EOM-MP2-S(D)
>     * 第
>     * 7.9.5.2
>     * 节
>     * EOM-CCSD(dT)
>     * 第
>     * 7.9.27
>     * 节
>     * EOM-CCSD(fT)
>     * 第
>     * 7.9.27
>     * 节
>     * EOM-CC(2,3)
>     * 第
>     * 7.9.24
>     * 节
>     * ADC(0)
>     * 第
>     * 7.10
>     * 节
>     * ADC(1)
>     * 第
>     * 7.10
>     * 节
>     * ADC(2)
>     * 第
>     * 7.10
>     * 节
>     * ADC(2)-X
>     * 第
>     * 7.10
>     * 节
>     * ADC(3)
>     * 第
>     * 7.10
>     * 节
>     * SOS-ADC(2)
>     * 第
>     * 7.10
>     * 节
>     * RAS-SF
>     * 第
>     * 7.11
>     * 节
> * **备注**: 请参见各章节
