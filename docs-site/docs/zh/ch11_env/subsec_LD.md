---
title: "11.2.10 Langevin 偶极子模型"
---

## 11.2.10 Langevin 偶极子模型

（2026 年 7 月 4 日）

**Q-Chem** 提供了使用由 Florián 和 Warshel 开发的 Langevin 偶极子（Langevin Dipoles, LD）溶剂化模型来计算水溶液中分子性质及水合自由能大小的选项[[394]](../bib_references/bib.md#bib402)。

在该模型中，溶质分子被包围在一层球面点偶极子之中，这些偶极子的中心位于立方格点上。每个这样的“Langevin”偶极子都会根据溶质及其他 Langevin 偶极子所产生的静电场改变其大小和取向。来自溶质的静电场通过对其电荷密度进行严格积分来确定，而偶极子–偶极子相互作用则采用 12 Å 的截断半径。**Q-Chem**/**ChemSol** 1.0 对 LD 模型的实现是完全自洽的，其中分子的量子力学计算考虑了溶质–溶剂相互作用。有关该模型实现与参数化的更多细节，可参见文献[[394]](../bib_references/bib.md#bib402)。

**ChemSol** 计算的结果会输出到标准输出文件中。下面给出了对甲醇阴离子（methoxide anion）进行计算的部分输出结果（与后文给出的示例输入相对应，示例文件位于 `$QC/samples` 目录中）。

| 能量分量 | 数值 / kcal mol ${}^{-1}$ |
| --- | --- |
| LD 静电能 | $-86.14$ |
| 疏水能 | 0.28 |
| van der Waals 能 | $-1.95$ |
| 体相校正（Bulk correction） | $-10.07$ |
| 溶剂化自由能 $\Delta G$（ILD） | $-97.87$ |

表 11.8： 
采用迭代 Langevin 偶极子（Iterative Langevin Dipoles, ILD）溶剂化模型对水溶液中甲醇阴离子的计算结果。

总水合自由能 $\Delta G$(ILD) 由若干贡献项相加得到。请注意，$\Delta G$ 的静电部分是利用线性响应近似[[394]](../bib_references/bib.md#bib402)计算的，其中包含了由于溶质电荷分布与溶剂相互作用而产生的*极化*贡献。这正是 Langevin 偶极子模型在 **Q-Chem** 中以自洽方式实现所带来的结果。

要在 **Q-Chem** 中执行 LD 计算，请为 Hartree-Fock 或 DFT 计算指定常规的作业控制变量，并在 *$rem* 段中设置 SOLVENT_METHOD = CHEM_SOL。进一步的精细调节可通过在 *$chem_sol* 输入段中使用一组关键字来实现。本节其余部分对这些关键字进行概述。

### `EField`

> **决定在计算溶质静电场时如何近似溶质的电荷分布。输入段：$chem_sol**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **可选值**：
>     * 1
>     * 使用精确的溶质电荷分布。
>     * 0
>     * 用 Mulliken 原子电荷近似溶质电荷分布。
> * **建议**：无。基于 Mulliken 电荷的方法更快，但严谨性较差。

### `NGrids`

> **设置用于计算平均水合自由能的网格数目。输入段：$chem_sol**
>
> * **类型**：`INTEGER`
> * **默认值**：`5`
> * **可选值**：
>     * $n$
>     * 使用
>     * $n$
>     * 个不同的网格。
> * **建议**：无。$n$ 允许的最大值为 20。

### `Print`

> **控制 Q-Chem 输出文件中 ChemSol 部分的打印信息。输入段：$chem_sol**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * 0
>     * 有限打印
>     * 1
>     * 完整打印
> * **建议**：无。

### `ReadRadii`

> **从 $van_der_waals 段读取用户定义的原子半径。输入段：$chem_sol**
>
> * **类型**：`None`
> * **默认值**：`Off`
> * **可选值**：
>     * 无选项。指定该关键字以使用用户定义的原子半径。
> * **建议**：无。

要准确计算水合自由能，就需要根据依赖于原子类型的参数谨慎选择溶质–溶剂边界。**Q-Chem** 中可用的默认原子 van der Waals 半径经过挑选，能够对大多数溶质和基组给出合理的水合自由能。这些参数基本上与文献[[395]](../bib_references/bib.md#bib403)中给出的 **ChemSol** 2.0 半径一致。**Q-Chem** 与 **ChemSol** 2.0 原子半径之间的唯一差别在于：**Q-Chem** 的参数集对碳和氧使用的半径与原子的杂化状态无关。用户可以在 *$chem_sol* 输入段中声明 **ReadRadii** 选项，然后将半径写入 *$van_der_waals* 段，从而指定用户自定义的原子半径。可以使用两种不同的（互斥的）格式，如下所示。

> ```qchem
> $van_der_waals
> 1
> atomic_number   vdW_radius
> ...
> $end
> 
> $van_der_waals
> 2
> sequential_atom_number   vdW_radius
> ...
> $end
> ```

第二种格式的目的是允许用户按照原子在 *$molecule* 段中出现的顺序来自定义特定原子的半径，而不是像格式 1 那样仅按原子序数指定。未在 *$van_der_waals* 输入中列出的原子将被赋予默认半径值。计算中实际使用的原子半径会在输出文件的 **ChemSol** 部分中以 *rp* 列打印出来。所有半径均应以埃（Ångstroms）为单位给出。

???+ example "示例 11.19: 对甲醇阴离子进行 Langevin 偶极子计算。为碳原子的半径指定了一个自定义值。"
    ```qchem
    $molecule
      -1  1
       C   0.0000   0.0000  -0.5274
       O   0.0000   0.0000   0.7831
       H   0.0000   1.0140  -1.0335
       H   0.8782  -0.5070  -1.0335
       H  -0.8782  -0.5070  -1.0335
    $end
    
    $rem
       METHOD            hf
       BASIS             6-31G
       SCF_CONVERGENCE   6
       SOLVENT_METHOD    Chem_Sol
    $end
    
    $chem_sol
    ReadRadii
    $end
    
    $van_der_waals
    2
    1 2.5
    $end
    ```
