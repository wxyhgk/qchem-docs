---
title: "6.6.9 双基组 MP2（Dual-Basis MP2）"
---

## 6.6.9 双基组 MP2（Dual-Basis MP2）

（2026 年 7 月 4 日）

前述各节在计算开销加速方面取得的成功，往往使得底层自洽场（SCF）计算的成本占据主导地位。双基组方法（dual-basis method）提供了一种将 SCF 加速约一个数量级的手段，且伴随的误差极小（参见第 [4.7](../ch04_scf/sect_dualbasis.md) 节）。这一双基组参考能量可以与 RI-MP2 计算相结合，用于能量[[1300]](../bib_references/bib.md#bib1355)以及解析一阶导数[[332]](../bib_references/bib.md#bib335)的计算。在后一种情形下，由于能够在较小的基组（Basis Set）中求解响应（$Z$-vector）方程，梯度计算可获得除 SCF 之外的额外节省。详细信息及作业控制选项参见第 [4.7](../ch04_scf/sect_dualbasis.md) 节。
