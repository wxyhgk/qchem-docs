---
title: "9.5.1 施加外力"
---

## 9.5.1 施加外力

（2026 年 7 月 4 日）

2009 年，人们提出了三种在恒定外力作用下优化分子几何结构的方法，分别称为*力修饰势能面*（Force-Modified Potential Energy Surface, FMPES）[[1022]](../bib_references/bib.md#bib1064)、
*显式包含外力*（External Force is Explicitly Included, EFEI）[[1164]](../bib_references/bib.md#bib1217)

以及*受迫几何优化*（Enforced Geometry Optimization, EGO）[[1488]](../bib_references/bib.md#bib1549)。
这些方法彼此紧密相关，感兴趣的读者可参阅文献 [[1296]](../bib_references/bib.md#bib1351)，其中详细讨论了它们之间的异同。为简便起见，本文统一使用 EFEI 这一术语。EFEI 计算是一种几何优化，其做法是在由用户指定的两个原子的核梯度上，加上一个与外力大小相等的常数。外力沿连接这两个原子的矢量方向施加，从而将它们拉开。当分子的回复力等于外力时，几何优化即达到收敛。EFEI 方法也可用于从头算分子动力学（AIMD）模拟（参见[第 9.9 节](topic_aimd.md)），此时在每一个时间步长中都施加该力。

**Q-Chem** 5.4 是首个采用新语法来指定 EFEI 计算的版本，该语法要求在 *$rem* 区段中设置 DISTORT = TRUE（参见[第 9.5 节](sec_Pressure.md)）：

> ```qchem
> $distort
>    model efei
>    force [atom1 atom2 force1]
>    force [atom3 atom4 force2]
>    ...
> $end
> ```

此处，*atom1* 和 *atom2* 是施加外力的两个原子的序号。*force1* 是以纳牛（nN）为单位、作用在 *atom1* 和 *atom2* 上的力值之和。若该值为正，则大小为 *force1*/2 的机械力分别作用于这两个原子，从而将它们拉开；若该值为负，则原子之间受到吸引力。此外，还可以通过在 *$distort* 区段中添加行的方式，选择性地指定其他受力的原子对。
