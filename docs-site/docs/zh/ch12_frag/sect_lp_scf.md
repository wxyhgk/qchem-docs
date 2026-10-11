---
title: "12.5.1 局域投影 SCF"
---

## 12.5.1 局域投影 SCF

（2026 年 7 月 4 日）

受约束的局域投影 SCF（Locally-Projected SCF）是一种高效的方法，可用于消除由弱相互作用组分（如分子团簇和分子复合物）构成的体系计算中的 SCF 对角化瓶颈。[[683]](../bib_references/bib.md#bib705)
该方法基于面向分子相互作用的局域投影 SCF（SCF-MI）方程。[[1314]](../bib_references/bib.md#bib1371)
在 SCF-MI 方法中，某一片段上的占据分子轨道只能由同一片段的原子轨道展开。这种约束产生了定域在片段上的非正交分子轨道（MO），称为绝对定域分子轨道（Absolutely-Localized Molecular Orbitals, ALMOs）。ALMO 近似排除了片段间的电荷转移。它同时也防止一个片段上的电子借用其他片段的原子轨道来弥补自身原子轨道（AO）的不完备性，因此消除了片段间结合能中的基组重叠误差（BSSE）。局域投影 SCF 方法针对 ALMO 系数对 SCF 能量进行迭代极小化。该算法的收敛可通过局域投影形式的 DIIS 外推（extrapolation）方法加以加速。[[683]](../bib_references/bib.md#bib705)

ALMO 近似显著减少了波函数的变分自由度。局域投影 SCF 方法相对于常规 SCF 方法的计算优势会随着基组（Basis Set）规模和片段数量的增大而增长。尽管 SCF-MI 仍为立方标度（cubic scaling），但由于其前置因子（prefactor）非常小，实际上消除了对角化步骤在此类计算中的瓶颈地位。在当前实现中，SCF-MI 方法并不会加速 Fock 矩阵的求值，因此在以 Fock 矩阵构建为主导的计算中，其性能并不明显优于常规 SCF。

目前已实现两种局域投影方案。一种基于 Stoll 等人的局域投影方程，[[1314]](../bib_references/bib.md#bib1371)
另一种使用 Gianinetti 等人的局域投影方程。[[440]](../bib_references/bib.md#bib451)
这两种方法性能相当。Stoll 迭代仅比 Gianinetti 迭代略快，但 Stoll 方程的收敛可能稍难一些。Stoll 方程产生的 ALMO 还具备片段内正交的性质。局域投影 SCF 计算类型的选择通过为 FRGM_METHOD 关键字指定 STOLL 或 GIA 来完成。

???+ example "示例 12.6: Stoll 局域投影 SCF 方法"
    ```qchem
    $molecule
       0 1
       --
       -1 1
       B       0.068635     0.164710     0.123580
       F      -1.197609     0.568437    -0.412655
       F       0.139421    -1.260255    -0.022586
       F       1.118151     0.800969    -0.486494
       F       0.017532     0.431309     1.531508
       --
       +1 1
       N      -2.132381    -1.230625     1.436633
       H      -1.523820    -1.918931     0.977471
       H      -2.381590    -0.543695     0.713005
       H      -1.541511    -0.726505     2.109346
       H      -2.948798    -1.657993     1.873482
    $end
    
    $rem
       METHOD          BP86
       BASIS           6-31(+,+)G(d,p)
       FRGM_METHOD     STOLL
    $end
    
    $rem_frgm
       SCF_CONVERGENCE 2
       THRESH          5
    $end
    ```
