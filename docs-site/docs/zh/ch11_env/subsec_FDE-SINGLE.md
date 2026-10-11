---
title: "11.7.4 单片段计算"
---

## 11.7.4 单片段计算（Single-Fragment Calculations）

（2026 年 7 月 4 日）

FDE-Man 允许用户通过导入原子轨道（atomic-orbital, AO）矩阵表示的嵌入势来执行嵌入计算。因此，构造嵌入势所需的所有设置项都不再需要。此外，当 MOLECULE 段中只给出*一个分子*时，单片段模式（single-fragment mode）会被自动启用。

### `import_vmat`

> **以 AO 矩阵表示导入嵌入势。期望的文件名为 FDE_vembmat.txt，且该文件不包含文件头。所有与片段 B 及嵌入势相关的关键字都将导致报错。输入段（INPUT SECTION）：$fde**
>
> * **类型**：`BOOLEAN`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 读取嵌入势并将其添加到 Fock 矩阵中。
>     * FALSE
>     * 不读取嵌入势，使用其他选项。
> * **建议**：无

**注意：

该功能作为独立模块构建，在单片段模式下只能使用 import_rhoA 和 print_props=1 选项。
**

用户也可以利用单片段模式，从密度矩阵中获取 Mulliken 电荷和 ChElPG 电荷。为此，需要导入片段 A 的密度，并将 **charges** 设置为下列选项之一。导入片段 A 的密度矩阵的方法如前所述。

### `charges`

> **以 AO 矩阵表示的密度矩阵计算 Mulliken 电荷或 ChElPG 电荷。必须将 import_rhoA 选项设置为 TRUE。输入段（INPUT SECTION）：$fde**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * Mulliken
>     * 从体系 A 的密度矩阵计算 Mulliken 电荷。
>     * CHELPG
>     * 从体系 A 的密度矩阵计算 ChElPG 电荷。
