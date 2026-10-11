---
title: "7.6.2 静态交换（Static Exchange, STEX）"
---

## 7.6.2 静态交换（Static Exchange）

（2026 年 7 月 4 日）

在最简单的形式中，STEX[[605]](../bib_references/bib.md#bib628) 通过对电离体系的 Fock 矩阵的虚空间进行对角化来计算激发能。当将 STEX 用于多个核电离（core-ionized）态时，[[28]](../bib_references/bib.md#bib12)
 其基本假设是：非正交行列式之间的耦合可以忽略不计，且所有相关的激发行列式都可以通过向核电离态单电子附着（electron-attachment）的方式构造。从这一角度看，STEX 可视为 NOCIS 的一种近似。

STEX 算法与 NOCIS 非常相似。基态计算在构造参考行列式之前，先对参考轨道进行 Boys 定域化。这样，STEX 可被视为 NOCIS 的近似。
