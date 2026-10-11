---
title: "11.5.7 运行 EFP 计算任务"
---

## 11.5.7 运行 EFP 计算任务

（2026 年 7 月 4 日）

当前版本支持由以下区域组成的体系的单点能计算：
($i$) *从头算（ab initio）*区域与 EFP 区域（QM/MM）；或 ($ii$) 仅含 EFP 区域。
对于静电嵌入（electrostatic embedding）QM/MM 模型，已启用约束 QM 区域几何优化，
如 [11.5.6](sec_EFP-QMMM.md) 所述。

*从头算*区域可以用常规量子方法来描述，例如 HF、DFT（密度泛函理论，Density Functional Theory），或包含激发态方法在内的关联方法[CIS、CIS(D)、TDDFT、ADC、EOM-CCSD 方法]。关于 EFP 与 EOM-CCSD 及 CIS(D) 接口的理论细节可参阅
参考文献 [[1272]](../bib_references/bib.md#bib1325)
 和 [[711]](../bib_references/bib.md#bib743)
。ADC/EFP 模型描述见参考文献 [[1230]](../bib_references/bib.md#bib1285)
。

**注意：

EFP 同时提供了对电子激发态的隐式修正（通过轨道响应）和显式修正（作为可极化 EFP 碎片的瞬时响应）。经 EFP 修正后的激发能会输出在输出文件的属性（property）部分。
**

EF（有效片段，Effective Fragment）之间会计算静电（electrostatic）、极化（polarization）、交换排斥（exchange-repulsion）和色散（dispersion）贡献；而*从头算*区域与 EF 区域之间仅计算静电项和极化项。

*从头算*区域通过常规的 **Q-Chem** 输入来指定，即使用 *$molecule* 和 *$rem* 段。在不含 QM 部分的计算中，*$molecule* 段应包含一个哑原子（dummy atom，例如氦）。

EF 的位置在 *$efp_fragments* 段中指定。
