---
title: "7.10.12 冻结密度嵌入：FDE-ADC 方法"
---

## 7.10.12 冻结密度嵌入：FDE-ADC 方法

（2026 年 7 月 4 日）

FDE-ADC[[1121]](../bib_references/bib.md#bib1168) 是一种基于冻结密度嵌入理论（Frozen Density Embedding Theory, FDET）[[1453]](../bib_references/bib.md#bib1515)，将嵌入物种与其环境之间的相互作用纳入 ADC($n$) 计算的方法。

FDE-ADC 支持 2s、2x 和 3 阶的 ADC 及 CVS-ADC 方法，常规的 ADC 作业控制关键字同样适用。

FDE-ADC 方法首先为嵌入体系 (A) 使用 MP($n$) 密度、为环境 (B) 使用 DFT 或 HF 密度生成嵌入势。然后进行 Hartree-Fock 计算，在此过程中将嵌入势添加到 Fock 算符中。嵌入的 Hartree-Fock 轨道作为后续 ADC 计算的输入，从而得到嵌入性质（垂直激发能、振子强度等）。关于 FDE-ADC 方法和 FDE-ADC 作业控制的更多信息，请参见第 [11.7.2.1](../ch11_env/subsec_FDE_MAN.md#subsubsec:FDE_ADC) 节。
