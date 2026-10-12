---
title: "8.2.1 概述"
---

## 8.2.1 概述

(July 4, 2026)

**Q-Chem** 内置了许多标准基组（Basis Set），[[11]](../bib_references/bib.md#bib14) 并允许用户通过标准符号表示法指定所需的基组。可用的内置基组包括以下类型：

- •

Pople 基组[[131]](../bib_references/bib.md#bib121)
- •

Dunning 基组[[354]](../bib_references/bib.md#bib359)
- •

相关性一致（correlation-consistent，cc）Dunning 基组，包括：

- **–**

标准的 cc-pVXZ 与 aug-cc-pVXZ（X = D、T、Q、5 和 6）[[355]](../bib_references/bib.md#bib360)
- **–**

部分加弥散（partially-augmented）的“日历”版本，[[1039]](../bib_references/bib.md#bib1083)

即 may-、jun- 和 jul-cc-pVXZ（X = D、T、Q）
- **–**

带芯-价极化函数（core–valence polarization functions）的版本，[[1122]](../bib_references/bib.md#bib1169)

即 cc-pCVXZ 与 cc-pwCVXZ（X = D、T、Q）
- **–**

部分加弥散的芯-价极化基组 jun-、jul- 与 aug-cc-pCVXZ（X = D、T、Q）
- **–**

针对重元素的赝势（Pseudopotential，PP）基组，cc-pVXZ-PP 与 aug-cc-pVXZ-PP（X = D、T、Q）[[1080]](../bib_references/bib.md#bib1125)
- •

Ahlrichs 基组[[1202]](../bib_references/bib.md#bib1256)
- •

Karlsruhe “def2” 基组，[[1438]](../bib_references/bib.md#bib1504)
 包括

- **–**

加弥散版本，[[1147]](../bib_references/bib.md#bib1199)
 例如 def2-SVPD
- **–**

部分加弥散版本，[[481]](../bib_references/bib.md#bib492)
 例如 def2-ha-SVP 和 def2-ha-SVP
- •

Jensen 极化一致（polarization consistent）基组[[635]](../bib_references/bib.md#bib661)
- •

通用高斯基组（Universal Gaussian basis set，UGBS）[[310]](../bib_references/bib.md#bib315)

此外，**Q-Chem** 还支持以下特性：

- •

可用于高质量激发态计算的额外弥散函数（diffuse functions）。
- •

标准极化函数（polarization functions）。
- •

基函数的 $s$、$p$、$sp$、$d$、$f$、$g$ 和 $h$ 角动量类型（对于能量计算，最高支持到 $k$）。
- •

纯函数（Pure）与笛卡尔（Cartesian）基函数。
- •

混合基组（Mixed basis sets）（参见第 [8.5](sect_mixedbas.md) 节）。
- •

基组重叠误差（basis set superposition error，BSSE）校正。
- •

针对任意基组（包括一般基组和混合基组）及任意自洽场（SCF）理论级别，自动、即时（on-the-fly）生成原子密度叠加（superposition of atomic densities，SAD）初始猜测（guess）（参见第 [4.4.2](../ch04_scf/sect_guess.md) 节）。

以下 *$rem* 关键字用于控制基组：

### `BASIS`

> **设置所使用的基组。**
>
> * **类型**：`STRING`
> * **默认值**：`No default basis set`（无默认基组）
> * **选项**：
>     * General、Gen
>     * 用户自定义（User-defined）。参见下文各小节
>     * Symbol
>     * 使用下表中所列的标准基组
>     * Mixed
>     * 使用不同基组的组合
> * **建议**：请参阅相关文献与综述以辅助选择。
