---
title: "6.13.1 (T) 三激发修正（(T) Triples Corrections）"
---

## 6.13.1 (T) 三激发修正

（2026 年 7 月 4 日）

若要在反应能及相关性质上达到化学精度（chemical accuracy），就必须考虑同时涉及三个电子的电子关联效应，这种效应体现为相对于平均场（mean field）单行列式参考（reference）的三激发替换（triple substitutions），并在 MP4 中出现。包含三激发替换的最佳标准方法是 CCSD(T)[[1141]](../bib_references/bib.md#bib1193)
 与 QCISD(T) 方法。[[1113]](../bib_references/bib.md#bib1162)
这些方法的精度在众多情形中已有充分记载，并且总体而言，相较于其起点方法（CCSD 或 QCISD）带来了极为显著的提升。这些修正的计算开销随分子尺寸呈七次方增长（或对固定分子尺寸而言，随基函数（Basis Function）数目呈四次方增长），不过相对于起始的耦合簇（coupled-cluster）计算并不需要额外的磁盘资源。**Q-Chem** 支持计算 CCSD(T) 与 QCISD(T) 能量，以及相应的、针对上一小节所讨论的优化双激发（optimized doubles）方法的 OD(T) 修正。上述所有 (T) 修正目前尚不可用于计算梯度（Gradients）与性质（properties）。
