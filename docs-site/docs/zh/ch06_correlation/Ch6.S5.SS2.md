---
title: "6.5.2 EPAO 评估选项"
---

## 6.5.2 EPAO 评估选项

(July 4, 2026)

当执行局部 MP2（local MP2）计算（通过 CORRELATION 选项设置为 LOCAL_MP2 来请求）时，SCF 计算收敛之后的第一个新步骤是抽取一组张成占据空间（occupied space）的极化原子轨道最小组（extended polarized atomic orbitals, EPAOs）的基组。该基组有三种有效的选择，由下面描述的 PAO_METHOD 和 EPAO_ITERATE 关键字控制。

- •

**非迭代 EPAO（Non-iterated EPAOs）：** 初始猜测 EPAO 是局部 MP2 计算的默认选项，其定义如下。对每个原子，将协变密度矩阵（SPS）对角化，得到的本征值是近似的自然轨道（natural orbital）占据数，得到的本征向量是对应的原子轨道。保留占据数最大的 $m$ 个本征向量（其中 $m$ 为当前原子的最小组维数）。这个非正交的最小组先经过对称正交化（symmetrically orthogonalized），然后再按参考文献 [[789]](../bib_references/bib.md#bib820) 中讨论的方式进行修正，以确保这些函数严格张成刚刚完成的完整 SCF 计算的占据空间。这些轨道可以记作 EPAO(0)，表示在猜测之后没有执行任何迭代。一般而言，采用此选项获得的局部 MP2 结果的质量与下面的 EPAO 选项非常接近，但它要快得多且完全稳健。对于上文讨论的扭转势垒（torsional barrier）计算示例，[[790]](../bib_references/bib.md#bib819)
 与完整 MP2 计算相比，TRIM 的 RMS 偏差为 0.03 kcal/mol，当采用 EPAO(0) 轨道而非 EPAOs 时，该偏差仅增大到 0.04 kcal/mol。
- •

**EPAO：** EPAO 由最小化一个定域化泛函（localization functional）来定义，如参考文献 [[789]](../bib_references/bib.md#bib820)
 所述。这些函数被设计为适用于局部 MP2 计算，并且在迄今进行的所有测试中都取得了极好的结果。遗憾的是，对于大分子而言，该泛函难以收敛，至少用目前发展到此阶段的算法是这样。因此它不是默认选项，而是通过为 EPAO_ITERATE 指定一个（较大的）值来开启，如下所述。
- •

**PAO：** 如果 SCF 计算是在分子优化的最小组（molecule-optimized minimal basis）下进行的（如第 [4 章](../ch04_scf/chap_scf.md)所述），则所得的 PAO-SCF 计算可以用常规 MP2 或局部 MP2 来校正电子相关。PAO-SCF 计算会改变 SCF 能量，因此不是默认选项。在 CORRELATION = LOCAL_MP2 的作业中指定 PAO_METHOD = PAO 即可启用此功能。

### `PAO_METHOD`

> **控制所请求的 PAO 计算类型。**
>
> * **类型**：`STRING`
> * **默认值**：`EPAO`
> * **选项**：
>     * EPAO
>     * 通过最小化离域化函数（delocalization function）来求取 EPAO。
>     * PAO
>     * 在分子优化的最小组下进行 SCF 计算。
> * **建议**：无

### `EPAO_ITERATE`

> **控制 EPAO 计算的迭代次数（参见 PAO_METHOD）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * 对 EPAO 进行最多
>     * $n$
>     * 次迭代的优化。
> * **建议**：使用默认值。对于不太大的分子，可以通过使用优化后的 EPAO 来测试结果对最小组函数类型的敏感性，此时取 $n=500$ 是合理的。

### `EPAO_WEIGHTS`

> **控制 EPAO 计算的算法与权重（参见 PAO_METHOD）。**
>
> * **类型**：`INTEGER`
> * **默认值**：`115`
> * **选项**：
>     * 15
>     * 标准权重，仅进行 1
>     * ${}^{\mathrm{st}}$
>     * 阶优化。
> * **建议**：使用默认值，除非遇到收敛失败。

局部 MP2 计算（通过 CORRELATION 选项设置为 LOCAL_MP2 来请求）由以下步骤组成：

- •

SCF 收敛之后，求取一组 EPAO 最小组。
- •

随后计算 TRIM（以及 DIM）局部 MP2 能量（梯度目前尚不可用）。

上述局部 MP2 方法高效实现细节见 Michael Lee 博士近期的博士论文。

这里我们仅简要概述该程序的功能。这些局部 MP2 方法所带来的计算优势随分子大小和基组的不同而变化。作为一个粗略的总体估计，TRIM MP2 计算可行的分子尺寸约为在同一台计算机上常规 MP2 计算可行尺寸的两倍，这是它们的主要优势。我们的实现非常适合大基组计算。AO 基双电子积分被求取四次。DIM MP2 计算作为 TRIM MP2 的副产品执行，但尚未单独实现针对 DIM 的优化算法。

局部 MP2 计算的资源需求如下：

- •

*内存（Memory）：* 积分变换的内存需求不超过 $OON$，并经过阈值控制，使其渐近地随分子尺寸线性增长。完成局部 MP2 能量评估还需要约 32$N^{2}$ 的额外内存。
- •

*磁盘（Disk）：* 磁盘空间需求仅约为 $8OVN$，但不受阈值控制。相比完整 MP2 计算（在四次积分求取的情况下需要 $OVN^{2}$/4 的磁盘空间），这是一个非常大的削减。局部 MP2 的磁盘空间需求不可调。

局部 MP2 能量的评估不需要任何进一步的自定义设置。应指定足够大的 MEM_STATIC（至少 80–160 Mb）以保证 AO 基双电子积分的高效求取，但所有大型临时数组（scratch arrays）都从 MEM_TOTAL 分配。

???+ example "示例 6.2: 使用局部 TRIM 模型对 MP2 进行相对能量评估，采用 6-311G** 基组。能量差为丙烯醛（acrolein）的内旋转势垒，第一个几何构型为平面反式（planar trans），第二个为过渡结构（transition structure）。"
    ```qchem
    $molecule
       0 1
       C
       C  1  1.32095
       C  2  1.47845  1  121.19
       O  3  1.18974  2  123.83  1   180.00
       H  1  1.07686  2  121.50  3     0.00
       H  1  1.07450  2  122.09  3   180.00
       H  2  1.07549  1  122.34  3   180.00
       H  3  1.09486  2  115.27  4   180.00
    $end
    
    $rem
       METHOD        local_mp2
       BASIS         6-311g**
    $end
    
    @@@
    
    $molecule
       0 1
       C
       C  1  1.31656
       C  2  1.49838  1  123.44
       O  3  1.18747  2  123.81  1   92.28
       H  1  1.07631  2  122.03  3   -0.31
       H  1  1.07484  2  121.43  3  180.28
       H  2  1.07813  1  120.96  3  180.34
       H  3  1.09387  2  115.87  4  179.07
    $end
    
    $rem
       METHOD        local_mp2
       BASIS         6-311g**
    $end
    ```
