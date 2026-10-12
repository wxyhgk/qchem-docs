---
title: "6.12.1 引言"
---

## 6.12.1 引言

（2026 年 7 月 4 日）

以下各节简要介绍了 **Q-Chem** 中提供的各种基于耦合簇（Coupled-Cluster, CC）的方法，其中大多数是耦合簇理论（coupled-cluster theory）的变体。使这些方法得以在 **Q-Chem** 中实现的基础面向对象（object-oriented）工具由 Anna Krylov 和 David Sherrill 完成，他们最初在伯克利（Berkeley）与 Martin Head-Gordon 合作开展工作，随后分别独立地在南加州大学（University of Southern California）和佐治亚理工学院（Georgia Tech）继续相关研究。在伯克利期间，Krylov 和 Sherrill 还开发了优化轨道耦合簇方法（optimized orbital coupled-cluster method），Ed Byrd 对此提供了额外协助。该代码向 MP3、MP4、CCSD 和 QCISD 的扩展由伯克利的 Steve Gwaltney 完成，而向 QCCD 的扩展则由伯克利的 Ed Byrd 实现。原始的张量库（tensor library）以及 CC/EOM 方法套件由 **Q-Chem** 的 CCMAN 模块负责处理。此后，Evgeny Epifanovsky 等人在 Krylov 课题组开发了一套新代码（称为 CCMAN2），并已启动从 CCMAN 到 CCMAN2 的逐步过渡。在过渡期间，两套代码均可通过 CCMAN2 关键字供用户使用。最后，还有一个名为 **libgmbpt** 的新模块，旨在便于对非常大的体系进行关联计算。该模块现已包含 RI-CC2 和随机（stochastic）RI-CC2 方法的高效实现。

### `CORRELATION`

> **指定由 CCMAN/CCMAN2 处理的关联理论级别。**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **可选项**：
>     * CCMP2
>     * 由 CCMAN/CCMAN2 处理的常规 MP2
>     * MP3
>     * CCMAN 和 CCMAN2
>     * MP4SDQ
>     * CCMAN
>     * MP4
>     * CCMAN
>     * CCD
>     * CCMAN 和 CCMAN2
>     * CCD(2)
>     * CCMAN
>     * CCSD
>     * CCMAN 和 CCMAN2
>     * CCSDT
>     * CCMAN2
>     * CC2
>     * CCMAN2 和 LIBGMBPT
>     * CCSD(T)
>     * CCMAN 和 CCMAN2
>     * CCSD(2)
>     * CCMAN
>     * CCSD(fT)
>     * CCMAN 和 CCMAN2
>     * CCSD(dT)
>     * CCMAN
>     * CCSDT
>     * CCMAN2
>     * CCVB-SD
>     * CCMAN2
>     * QCISD
>     * CCMAN 和 CCMAN2
>     * QCISD(T)
>     * CCMAN 和 CCMAN2
>     * OD
>     * CCMAN
>     * OD(T)
>     * CCMAN
>     * OD(2)
>     * CCMAN
>     * VOD
>     * CCMAN
>     * VOD(2)
>     * CCMAN
>     * QCCD
>     * CCMAN
>     * QCCD(T)
>     * CCMAN
>     * QCCD(2)
>     * CCMAN
>     * VQCCD
>     * CCMAN
>     * VQCCD(T)
>     * CCMAN
>     * VQCCD(2)
>     * CCMAN
> * **建议**：请参阅相关文献以获取指导。

**注意：

CCMAN2 中实现的所有方法均可与 PCM 隐式溶剂模型（implicit solvation models）组合使用（处于"零级"（zeroth-order）水平，详见第 [11.2.1 节](../ch11_env/topic_solvation_Intro.md)），也可与 EFP 方法（第 [11.5 节](../ch11_env/sect_efp.md)）组合使用。
仅可获取能量和非弛豫性质（unrelaxed properties），不支持梯度计算。**
