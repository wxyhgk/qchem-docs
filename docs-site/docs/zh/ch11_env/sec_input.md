---
title: "11.5.7 运行 EFP 任务"
---

## 11.5.7 运行 EFP 任务

（2026 年 7 月 4 日）

当前版本支持以下两类体系的单点能计算：（$i$）由 *ab initio*（从头算）区域与 EFP 区域组成的体系（QM/MM）；或（$ii$）仅含 EFP 区域的体系。对于静电embedding 的 QM/MM 模型，支持对 QM 区域的约束几何优化，详见 [11.5.6](sec_EFP-QMMM.md)。

*ab initio* 区域可以采用常规量子化学方法描述，例如 HF、DFT（密度泛函理论，Density Functional Theory, DFT）或包含激发态方法的相关方法 [CIS、CIS(D)、TDDFT、ADC、EOM-CCSD 方法]。关于 EFP 与 EOM-CCSD 及 CIS(D) 接口的理论细节可参见文献 [1272]](../bib_references/bib.md#bib1325) 和 [[711]](../bib_references/bib.md#bib743)。ADC/EFP 模型在文献 [[1230]](../bib_references/bib.md#bib1285) 中有描述。

**注意：

EFP 为电子激发态同时提供隐式（通过轨道响应）与显式（通过极化 EFP 片段的瞬时响应）校正。经 EFP 修正后的激发能会在输出文件的性质（property）部分打印。
**

在 EFP 片段（EFs）之间会计算静电、极化、交换排斥与色散等贡献项；而在 *ab initio* 区域与 EF 区域之间只计算静电项和极化项。

*ab initio* 区域通过常规的 **Q-Chem** 输入中的 *$molecule* 和 *$rem* 输入段指定。在没有 QM 部分的计算中，*$molecule* 输入段应包含一个虚拟原子（例如氦）。

EFP 片段（EFs）的位置在 *$efp_fragments* 输入段中指定。片段支持两种几何格式，由 EFP_COORD_XYZ 关键字控制：欧拉角（Euler angle）格式和 XYZ 格式。在欧拉角格式中，该输入段的每一行包含一个单独片段的信息：片段名称及其位置，位置由质心坐标（$x$、$y$、$z$）以及相对于片段坐标系的欧拉旋转角（$\alpha$、$\beta$、$\gamma$）指定，*即*片段库中所提供的标准片段的坐标。在 XYZ 格式中，片段名称写在第一行，其后三行依次给出片段前三个原子的名称及（$x$、$y$、$z$）坐标。
