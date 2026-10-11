---
title: "7.11.1 引言"
---

## 7.11.1 引言

(July 4, 2026)

限制活性空间自旋翻转（restricted active space spin-flip, RAS-SF）是一种特殊形式的组态相互作用（configuration interaction, CI），它能够以单参考（single-reference）形式、以适中的计算成本描述基态和低激发态[[203]](../bib_references/bib.md#bib201)，
包括强相关体系。RAS-SF 方法本质上是一种计算成本远低于完全活性空间自洽场（Complete Active Space SCF, CASSCF）方法的替代方案。RAS-SF 通常的工作方式是在一个活性空间内执行完全 CI（full CI）计算，该活性空间由限制性开壳层 HF（restricted open shell HF, ROHF）参考行列式的半占据轨道定义。这样就避开了 CASSCF 中态特定轨道优化的困难。而进入活性空间（空穴，hole）和离开活性空间（粒子，particle）的单激发则代之以提供态特定的弛豫。与大多数基于 CI 的方法不同，RAS-SF 既是尺寸一致（size-consistent）的，又是变分（variational）的；并且在固定自旋翻转数目的情况下，计算成本随体系尺寸的增加较为温和。但须注意，成本随自旋翻转数目的增长呈指数关系！已有研究表明，RAS-SF 能够处理多自由基（polyradicals）的多个低电子态，并可可靠地预测基态多重度。[[203]](../bib_references/bib.md#bib201)

RAS-SF 也可以看作更一般的 RAS-CI 方法族中的一个特定情形。例如，可以不像上述那样通过自旋翻转来定义活性空间，而是读入其他类型的初始轨道，以此方式计算的电子激发可视为一种 RAS-EE-CI 方法（尽管一般会失去尺寸一致性）。与 EOM-CC 方法类似（见第 [7.9](topic_eomcc.md) 节），可以从任意电子组态作为参考出发，使用一般的激发类型算符构造其他目标的 RAS-CI 波函数。例如，可以构造一个移除任意数目粒子的电离变体，即 RAS-$n$IP-CI。相应的电子附着变体则是 RAS-$n$EA-CI。[[209]](../bib_references/bib.md#bib203)

**Q-Chem** 提供了两个版本的 RAS-CI 代码，其功能不同且互补。其中一个代码（通过指定 CORRELATION = RASCI 调用）
由 David Casanova 编写；[[209]](../bib_references/bib.md#bib203)
 下文我们将此代码称为
RASCI1。第二个实现（通过指定 CORRELATION = RASCI2 调用）主要由 Paul
Zimmerman 完成；[[1584]](../bib_references/bib.md#bib1647)
 下文我们称其为 RASCI2。
两个代码均可用于计算若干态特定及态间性质，
例如自旋-轨道耦合（如第 [7.9.21.4](sec_EOMGRAD.md#sec:EOMSOC) 节所述）。[[191]](../bib_references/bib.md#bib186)

RASCI1 代码采用积分驱动（integral-driven）的实现（精确积分）并对 CI 组态进行自旋适配（spin-adaptation），从而减小了对角化的维度。**Q-Chem** 中 RASCI1 的当前实现
允许计算具有任意数目 $\alpha$ 和 $\beta$
电子的体系，每个态的多重度（$\langle\hat{S}^{2}\rangle$）会与态能一同打印输出。由于所有底层积分例程均已并行化，共享内存并行执行可缩短计算时间。

RASCI2 代码能够模拟闭壳层和开壳层体系（*即*，电子数为偶数和奇数的体系），采用恒等分辨（resolution of the identity, RI）近似进行快速积分求值，支持共享内存并行操作，并可分析 $\langle\hat{S}^{2}\rangle$ 值和自然轨道（natural orbitals）。自然轨道以 **MolDen** 可读格式存储在 `$QCSCRATCH` 目录下一个名为 "`NOs`" 的文件夹中。共享内存并行的调用方式如第 [2.2.1.1](../ch02_install/ssect_general-usage.md#sec:parallel) 节所述。RASCI2 输入需要指定一个辅助基组（auxiliary basis set），类似于 RI-MP2 计算（见
第 [6.6.2](../ch06_correlation/sect_rimp2.md) 节）。除此之外，活性空间以及空穴和粒子激发的指定方式与 RASCI1 相同。

**注意：**

**由于 RASCI2 使用了 RI 近似，两个代码计算得到的总能量
会有细微差别。不过，不同态之间的能量差应当彼此高度吻合。
**
