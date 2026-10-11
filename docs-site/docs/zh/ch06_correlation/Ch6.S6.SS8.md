---
title: "6.6.8 RI-TRIM MP2 能量"
---

## 6.6.8 RI-TRIM MP2 能量

（2026 年 7 月 4 日）

MP2 理论的分子内三原子体（triatomics in molecules, TRIM）局域相关近似[[790]](../bib_references/bib.md#bib819)已在第 [6.5.1](sect_trim.md) 节中详细描述，该节同时讨论了本程序基于常规四中心双电子积分对这一方法的实现。自 **Q-Chem** v. 3.0 起，提供了 TRIM 模型的辅助基组（auxiliary basis）实现。
新的 RI-TRIM MP2 能量算法[[331]](../bib_references/bib.md#bib334)

极大地加速了这些局域相关计算（对相关能部分，通常可加速一个数量级甚至更多），其计算量随分子尺寸的四次方（4th power）增长。与常规 RI-MP2 相比，计算中电子相关部分的加速倍率与分子中的原子数成正比。例如，对于一个十六肽（hexadecapeptide），加速倍率约为 4。[[331]](../bib_references/bib.md#bib334)
TRIM 模型同样可以应用于上文讨论的缩放反平行自旋（scaled opposite spin）模型。与本节讨论的其他基于 RI 的模型一样，当任务的运行时间是一个重要考量因素时，我们建议使用 RI-TRIM MP2 而非常规的 TRIM MP2 代码。与 RI-MP2 本身类似，调用 TRIM MP2 的方式是在请求 CORRELATION = RILMP2 之余，在 `$rem` 中加入 AUX_BASIS。

???+ example "示例 6.19: RI-TRIM MP2 能量计算示例"
    ```qchem
    $molecule
       0 3
       C1
       H1   C1   1.07726
       H2   C1   1.07726   H1   131.60824
    $end
    
    $rem
       METHOD         rilmp2
       BASIS          cc-pVDZ
       AUX_BASIS      rimp2-cc-pVDZ
       PURECART       1111
       UNRESTRICTED   true
       INTEGRAL_SYMMETRY false
    $end
    ```
