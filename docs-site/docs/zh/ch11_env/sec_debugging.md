---
title: "11.5.8 EFP 作业的调试"
---

## 11.5.8 EFP 作业的调试

（2026 年 7 月 4 日更新）

QM/EFP 模型的关键优势在于对体系进行可极化的自洽场（SCF）描述。然而，实现自洽极化也可能带来挑战。在极性体系的计算中，极化灾难（Polarization Catastrophe，即某些片段上的诱导偶极矩无限增大）是一种常见情形。但在大多数情况下，极化灾难的发生源于糟糕的结构（例如原子重叠或间距过近的结构），或源于有效片段（Effective Fragment）的糟糕参数（多极矩发散、极化率数值过大）。关键词 EFP_PRINT 控制 EFP 计算进程信息及片段信息的输出量。具体而言，EFP_PRINT=1 会输出少量关于各 EFP 相关步骤耗时以及诱导偶极矩收敛情况的附加细节；而 EFP_PRINT=2 则会在特定片段上出现过大诱导偶极矩以及片段间静电能过大的情况下输出警告，这可能提示片段之间出现了非物理的过近接触。

关键词 EFP_POL_DAMP 和 EFP_POL_DAMP_TT_VALUE 控制体系中所有片段的极化阻尼（Polarization Damping）参数。极化阻尼的默认值（即在小片段间距下对静电场和极化场进行屏蔽处理的参数）设为 0.6（参见 [[1271]](../bib_references/bib.md#bib1324)
 以及式 [11.71](sec_theory.md#eq:pol_damp_1)）。EFP_POL_DAMP_TT_VALUE 可覆盖此默认设置，数值越小提供的屏蔽越强。单个片段的极化阻尼还可以通过片段参数文件中的 POLAB 设置进一步调整（详见 `https://libefp2.github.io/parameters.html#additional-efp-parameters`）。
