---
title: "6.15.1 冻结自然轨道"
---

## 6.15.1 冻结自然轨道

（2026 年 7 月 4 日）

若采用冻结自然轨道（Frozen Natural Orbitals, FNO）方法对虚轨道空间进行截断，可带来巨大的计算开销节省。例如，仅使用完整虚轨道空间的 $f$ 比例，每一轮 CCSD 迭代即可获得 $1/(1-f)^{4}$ 倍的加速（CCSD 的计算量随虚轨道空间大小的四次方增长）。基于 FNO 的截断方法由 Bartlett 及其合作者首次引入基态耦合簇（CC）方法[[1287]](../bib_references/bib.md#bib1342)
；将该方法推广至 EOM-CC 框架下的电离态 recently 已被提出并完成基准测试[[748]](../bib_references/bib.md#bib781)
，详见第 [7.9.14](../ch07_excited/sec_FNO.md) 节。

FNO 由 MP2 密度矩阵的虚-虚块（virtual-virtual block）的本征态求得（计算量按 ${\cal{O}}({N^{5}})$ 标度），其本征值即为相应 FNO 的占据数。通过用户指定的阈值，可在 CC 计算中将占据数最小的 FNO 予以冻结。该做法可用于 CCSD、CCSD(T)、CCSD(2)、CCSD(dT)、CCSD(fT)，以及 CCD、OD、QCCD、VQCCD，并适用于这些波函数的所有可能的三重激发修正。

截断可采用两种不同的方案。第一种方案是直接指定所保留的虚轨道总数，*e.g.*，以虚轨道总数的百分比形式给出，如文献 [[1349]](../bib_references/bib.md#bib1408)
 中所做的那样。第二种方案是指定需要在截断后的空间中恢复的（虚空间）总自然占据数百分比。这两种判据分别被称为 POVO（虚轨道百分比，percentage of virtual orbitals）与 OCCT（占据阈值，occupation threshold）截断[[748]](../bib_references/bib.md#bib781)
。

由于 OCCT 判据基于特定分子的相关能，因此相比 POVO 能给出更一致的结果。在电离能计算中，采用 99–99.5% 的自然占据阈值，相对于完整虚轨道空间结果的误差可低于 1 kcal/mol[[748]](../bib_references/bib.md#bib781)
。误差随所恢复的总自然占据数呈线性下降，这一性质可被利用，通过对截断计算结果外推得到完整虚轨道空间下的值。这种外推方案称为外推 FNO（extrapolated FNO, XFNO）方法[[748]](../bib_references/bib.md#bib781)
。基态与电离态的总能量随 OCCT 的变化均呈现该线性行为。因此，即使这两个态并非在同一理论水平下计算，XFNO 方案依然可用，*e.g.*，在绝热能量差以及 EOM-IP-CC(2,3) 计算中。（更多讨论见文献 [[748]](../bib_references/bib.md#bib781)
。）

FNO 截断常常导致 CCSD 与 EOM 流程的收敛变慢。尽管如此，尽管迭代次数增多，基于 FNO 的轨道空间截断仍能显著降低计算成本，而精度的下降微乎其微[[748]](../bib_references/bib.md#bib781)
。

由于实现上的限制，FNO/OSFNO 不能使用点群对称性，对称性将被自动禁用。
请将输入文件相应地设置为 CC_SYMMETRY = FALSE。

对于开壳层体系，已发展出开壳层 FNO（open-shell FNO, OSFNO），用于 EOM-SF-CC 计算。
基准测试表明，对多种分子的单重态–三重态能隙，其误差可忽略不计。
更多细节请参见第 [7.9.14](../ch07_excited/sec_FNO.md) 节及文献 [[1104]](../bib_references/bib.md#bib1153)
。

CC_FNO_THRESH

### `CC_FNO_THRESH`

> **初始化 FNO 截断，并为两种截断判据（OCCT 和 POVO）设置所用阈值**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **可选值**：
>     * 取值范围
>     * 0000-10000
>     * $abcd$
>     * 对应于
>     * $ab.cd$
>     * %
> * **建议**：无

CC_FNO_USEPOP

### `CC_FNO_USEPOP`

> **截断方案的选择**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **可选值**：
>     * 0
>     * POVO
> * **建议**：无

???+ example "示例 6.48：使用 FNO 且 POVO = 65% 的 CCSD(T) 计算"
    ```qchem
    $molecule
       0 1
       O
       H 1 1.0
       H 1 1.0 2 100.
    $end
    
    $rem
       METHOD          CCSD(T)
       BASIS           6-311+G(2df,2pd)
       CC_FNO_THRESH   6500   65% of the virtual space
       CC_FNO_USEPOP   0
    $end
    ```
