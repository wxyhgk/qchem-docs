---
title: "11.5.9 片段库（Library of Fragments）"
---

## 11.5.9 片段库（Library of Fragments）

（2026 年 7 月 4 日）

有效片段（effective fragment, EF）是刚性结构，其势能由对每个独特的孤立片段进行的一组*ab initio*计算生成。有效片段势（EFP）包括：($i$) 多极矩（由 Stone 的分布式多极分析（Distributed Multipolar Analysis）产生），用于库仑项和极化项；($ii$) 以定域分子轨道（localized molecular orbital, LMO）质心为中心（通过耦合微扰 Hartree-Fock 计算获得）的静态极化率张量，用于极化计算；($iii$) 以 LMO 为中心（由含时 HF 计算生成）的动态极化率张量，用于色散计算；以及 ($iv$) 交换排斥项所需的 Fock 矩阵、基组（basis set）和定域轨道。此外，EF 势还包含原子坐标、多极展开点的坐标（通常为原子位置和键的中点位置）、LMO 质心坐标、静电与极化屏蔽参数，以及 EF 原子的原子标签。

**Q-Chem** 提供了一个标准片段库，其中含有预先计算好的有效片段势。目前该库包含常见的有机溶剂、核酸碱基，以及来自非共价相互作用 S22 和 S66 数据集的分子；见表 [11.10](#tbl:EFP)。片段库位于 `$QCAUX/fraglib` 目录中。EFP 采用 **gamess** 格式。

表 11.10：**Q-Chem** 中可用的标准片段

| acetone | ACETONE_L |
| --- | --- |
| acetonitrile | ACETONITRILE_L |
| adenine | ADENINE_L |
| ammonia | AMMONIA_L |
| benzene | BENZENE_L |
| carbon tetrachloride | CCL4_L |
| cytosine C1 | CYTOSINE_C1_L |
| cytosine C2a | CYTOSINE_C2A_L |
| cytosine C2b | CYTOSINE_C2B_L |
| cytosine C3a | CYTOSINE_C3A_L |
| cytosine C3b | CYTOSINE_C3B_L |
| dichloromethane | DCM_L |
| dimethyl sulfoxide | DMSO_L |
| guanine enol N7 | GUANINE_EN7_L |
| guanine enol N9 | GUANINE_EN9_L |
| guanine enol N9RN7 | GUANINE_EN9RN7_L |
| guanine keton N7 | GUANINE_KN7_L |
| guanine keton N9 | GUANINE_KN9_L |
| methane | METHANE_L |
| methanol | METHANOL_L |
| phenol | PHENOL_L |
| thymine | THYMINE_L |
| toluene | TOLUENE_L |
| water | WATER_L |
| acetamide, S66, gas phase | ACETAMIDE_L |
| acetamide, S66, H-bonded dimer | ACETAMIDE_HB_L |
| acetic acid, S66, gas phase | ACETICAC_L |
| acetic acid, S66, H-bonded dimer | ACETICAC_HB_L |
| adenine, S22 stack dimer | ADENINE_L |
| adenine, S22 WC dimer | ADENINE_WC_L |
| 2-aminopyridine, S22 | AMINOPYRIDINE_L |
| cyclopentane, S66 | CPENTANE_L |
| ethylene | ETHENE_L |
| acetylene | ETHYNE_L |
| formic acid, S22 H-bonded dimer | FORMICAC_HB_L |
| formamide, S22 dimer | FORMID_L |
| hydrogen cyanide | HCN_L |
| indole, S22 | INDOLE_L |
| methylamine, S66 | MENH2_L |
| neopentane, S66 | NEOPENTANE_L |
| $O_{2}$ | O2_L |
| pentane, S66 | PENTANE_L |
| peptide, S66 | PEPTIDE_L |
| pyrazine | PYRAZINE_L |
| pyridine, S66 | PYRIDINE_L |
| 2-pyridoxine, S22 | PYRIDOXINE_L |
| thymine, S22 stack dimer | THYMINE_L |
| thymine, S22 WC dimer | THYMINE_WC_L |
| uracil, S66, gas phase | URACIL_L |
| uracil, S66, H-bonded dimer | URACIL_HB_L |

**注意：**

**Q-Chem** 片段库中的片段名称后均附加了 “_L”，以便与用户自定义的片段区分开来。
**

标准片段的参数按如下方式计算。溶剂分子的几何结构采用 MP2/cc-pVTZ 优化；核酸碱基的几何结构采用 RI-MP2/cc-pVTZ 优化。S22 和 S66 数据集分子的几何结构相关讨论见参考文献 [[393]](../bib_references/bib.md#bib401)。EFP 参数是在 **gamess** 中获得的。为生成静电多极矩和静电屏蔽参数，采用了解析 DMA 程序：非芳香化合物使用 6-31+G* 基组，芳香化合物和核酸碱基使用 6-31G* 基组。势的其余部分，*即*、静态与动态极化率张量、波函数、Fock 矩阵等，均使用 6-311++G(3df,2p) 基组获得。
