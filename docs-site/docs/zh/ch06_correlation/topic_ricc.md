---
title: "6.12.10 耦合簇方法中的密度拟合（Resolution-of-the-Identity with CC, RI-CC）"
---

## 6.12.10 耦合簇方法中的密度拟合（RI-CC）

（2026 年 7 月 4 日）

RI 近似（见第 [6.6 节](topic_rimp2.md)）可用于耦合簇（coupled-cluster）计算，从而大幅降低积分变换的计算开销和磁盘存储需求。RI 近似可以仅应用于积分本身——此时积分仍以常规分子轨道（MO）形式生成，并执行常规的正交 CC/EOM 计算；也可以采用更完整的形式——此时使用修改后的 CC/EOM 方程，积分直接以其 RI 表示形式参与计算。后一种形式能够在存储节省和计算加速方面带来更显著的效果。

当指定了 AUX_BASIS 时，即对积分启用 RI。在 CC 计算中，只要指定了 AUX_BASIS，所有双电子积分都将采用 RI 分解形式。

默认情况下，积分将以 RI 形式存储，并调用专门的 CC/EOM 代码。通过关键字 CC_DIRECT_RI，可以将 RI 生成的积分转换回标准格式，从而以常规形式使用这些积分并调用常规的 CC 流程。该选项主要用于调试和基准测试目的。

!!! note "注意"
    针对积分的 RI 可用于所有 CCMAN/CCMAN2 方法。CCMAN 要求使用非限制（unrestricted）参考态，CCMAN2 则没有此限制。RI 也可用于需要解析梯度的任务。
    完整的 RI 实现（即以分解形式使用积分）仅在 CCMAN2 中可用。为获得最佳计算效率，可在适当时候与 FNO（见第 [6.15.1 节](sec_FNOCC.md)和第 [7.9.14 节](../ch07_excited/sec_FNO.md)）结合使用。


!!! note "注意"
    高效的 RI-CC2 实现[[532]](../bib_references/bib.md#bib546_cc2_ri)可用于 **libgfn2**；

