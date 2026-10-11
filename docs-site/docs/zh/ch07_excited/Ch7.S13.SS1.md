---
title: "7.13.1 引言"
---

## 7.13.1 引言

（2026 年 7 月 4 日）

随着激发态 *ab initio*（第一性原理）计算方法日益普及，如何从这类计算中提取化学意义成为了人们关注的问题。分析分子激发态的方法有多种，它们都基于一阶约化密度矩阵（reduced one-particle density matrices, OPDMs）。此类分析中所利用的两类对象是：(i) 基态与激发态 OPDM 之间的差值，以及 (ii) 连接基态与激发态的跃迁 OPDM（transition OPDM）。对于 CIS 和 TDDFT/TDA 波函数，这两个量是相同的，并且可以直接映射为 CIS 振幅；[[572]](../bib_references/bib.md#bib586)

然而，对于关联波函数，这两个对象并不相同。最基本的分析包括计算电子 attaching（附着）与 detaching（离去）密度[[538]](../bib_references/bib.md#bib555)

（在 TDDFT 框架下分别等价于粒子密度与空穴密度），[[572]](../bib_references/bib.md#bib586)

以及自然跃迁轨道（natural transition orbitals, NTOs）。[[913]](../bib_references/bib.md#bib947)

这些量使人能够获得对激发态最紧凑的描述。更详细的分析则可以进一步揭示激发态本质的额外信息。详尽的描述与示例可参见相关文献，[[1099]](../bib_references/bib.md#bib1142)

其中还包括对 TDDFT/TDA 计算可视化工具的综述。[[572]](../bib_references/bib.md#bib586)

本节介绍附着/离去密度分析以及自然跃迁轨道背后的理论背景，而关于生成适合绘制这些量的输入数据的具体细节，则在第 [10](../ch10_properties/chap_properties.md) 章中单独描述，该章还介绍了其他激发态分析工具。出于历史原因，某些功能存在重复的实现。例如，CIS 和 TDDFT 波函数既可以使用最初内置的代码进行分析，也可以使用较新的模块 **libwfa** 进行分析。
