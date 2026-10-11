---
title: "6.6.2 RI-MP2 能量与梯度。"
---

## 6.6.2 RI-MP2 能量与梯度。

(July 4, 2026)

按照惯例，使用辅助基组（auxiliary basis）近似计算的 MP2 能量被称为“分辨率恒等”（resolution of the identity）MP2，简称 RI-MP2。只需指定上文讨论的 AUX_BASIS 关键字，即可启用 RI-MP2 能量与梯度计算。如前所述，当采用合适的标准化辅助基组（auxiliary basis set）时，RI-MP2 能量[[387]](../bib_references/bib.md#bib395) 和梯度[[1440]](../bib_references/bib.md#bib1500) 的计算显著快于最佳的常规 MP2 能量与梯度计算，且精度损失可以忽略不计。因此，对于关心周转时间的计算任务，推荐使用 RI-MP2。磁盘需求非常 modest；只需保存各种三指标（3-index）数组即可。内存需求的增长速度慢于我们的常规 MP2 算法——仅随分子尺寸呈二次方增长。能量和解析梯度评估的最低内存需求约为 3$X^{2}$，其中 $X$ 是辅助基函数的数目，此外积分评估和其他小数组还需要一些额外内存。

事实上，对于不太大的分子（重原子数不超过 20 或 30 个），RI-MP2 对电子相关（electron correlation）的处理极其高效，以至于整个计算主要由初始的 Hartree-Fock 计算主导。尽管作为分子尺寸的函数，RI-MP2 处理的开销随分子尺寸的-scaling 仍然更陡峭（只是 RI 方法的前置因子要小得多）。其标度（scaling）相对于分子尺寸仍为五阶，只对较大分子的初始 SCF 计算起主导作用。因此，对于中等尺寸分子（尤其是使用大基组时）的 RI-MP2 能量评估，建议使用双基组（dual basis）HF 方法以进一步改善执行时间（见第 [4.7](../ch04_scf/sect_dualbasis.md) 节）。

关于所需内存的大小，需要考虑以下几点。

MEM_STATIC

### `MEM_STATIC`

> **在 Q-Chem 4.1 或更早版本中，用于设置 AO 积分评估及其变换（transformation）的内存。**
>
> * **类型**: `INTEGER`
> * **默认值**: `192`
> * **选项**:
>     * $n$
>     * 用户自定义的兆字节（megabytes）数。
> * **建议**: 在 Q-Chem 4.1 或更早版本中进行 RI-MP2 计算时，需要 $150(ON+V)$ 的内存。由于还需要存储若干尺寸为 $N^{2}$ 的矩阵，因此需要额外 32–160 MB 的内存。

MEM_TOTAL

### `MEM_TOTAL`

> **设置 Q-Chem 可用的总内存（以兆字节计）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `2000`
> * **选项**:
>     * $n$
>     * 用户自定义的兆字节（megabytes）数。
> * **建议**: 使用默认值，或设置为机器的物理内存。最低需求为 $3X^{2}$ 。

???+ example "示例 6.4: RI-MP2 几何优化的 Q-Chem 输入。"
    ```qchem
    $molecule
       0 1
       O
       H  1  0.9
       F  1  1.4  2  100.
    $end
    
    $rem
       JOBTYPE       opt
       METHOD        rimp2
       BASIS         cc-pvtz
       AUX_BASIS     rimp2-cc-pvtz
       INTEGRAL_SYMMETRY false
    $end
    ```
