---
title: "9.11.1 引言"
---

## 9.11.1 引言

（2026 年 7 月 4 日）

对亚稳态电子态（如暂时性阴离子，temporary anions）的研究给计算化学家带来了一项重大挑战。例如，寻找一个能够描述给定暂时性阴离子电子态的 Hartree-Fock（HF）自洽场（SCF）解，通常是一项艰巨且棘手的任务。

这使得基于 HF 对暂时性阴离子执行简单 AIMD（从头算分子动力学）模拟的前景更加令人望而生畏。除了电子结构问题本身固有的困难之外，还必须考虑到这样一个事实：暂时性阴离子在形成之后，通常会受到两个相互竞争过程的影响：电子自脱落（electron autodetachment，AB${}^{-}\ \rightarrow\$AB $+$ e${}^{-}$）
和解离性电子附着（dissociative electron attachment，DEA）（AB${}^{-}\ \rightarrow\$A $+$ B${}^{-}$）。
然而，鉴于此类工作有望为暂时性阴离子的形成与其 DEA 产物之间的关联机制提供非常重要的见解，能够执行 Such 一种 AIMD 模拟的需求再怎么强调也不为过。

借助 **Q-Chem** 中复吸收势（complex absorbing potential，CAP）的解析梯度，[[108]](../bib_references/bib.md#bib95)
，
人们可以将 AIMD 模拟的一般原理与 CAP 方法（第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节）结合起来，
从而实现对暂时性阴离子的 AIMD 模拟。基于 Born-Oppenheimer 近似，这种
"CAP-AIMD"方法使得原子核能够在实时计算的复势能面（complex potential energy surface，CPES）上进行传播成为可能。[[509]](../bib_references/bib.md#bib522)

在正确的 CPES 上启动 CAP-AIMD 模拟对于模拟的成功至关重要。若未能做到这一点，将导致错误的结果。因此，在讨论如何使用 **Q-Chem** 运行 CAP-AIMD 之前，
