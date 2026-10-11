---
title: "7.7.6 冻结-释放（Freeze-and-Release）计算"
---

## 7.7.6 冻结-释放（Freeze-and-Release）计算

（2026 年 7 月 4 日）

$\Delta$SCF 方法将激发态问题重新表述为：使用一组分子轨道（Molecular Orbitals, MOs）生成的一个或多个电子组态所对应的电子能量进行变分优化。
尽管这一流程可以为激发态能量和性质[[143]](../bib_references/bib.md#bib133)
提供精确的结果，但激发态电子势能面上的变分收敛比基态计算更为困难。
此外，变分优化算法的性能本质上对其初始猜测（initial guess）十分敏感，这意味着基态 MOs 并不总是适合用于启动电子密度极化发生显著变化的激发态计算，*e.g.*，电荷转移（charge-transfer）激发。
使用较差的猜测可能导致收敛到另一个电子态，例如变分塌缩（variational collapse）至基态、收敛缓慢，或完全不收敛。
因此，开发猜测精化（guess-refinement）算法以提高初始猜测的质量，进而改善激发态电子密度的收敛性，是非常必要的。

最近，Schmerwitz *et al.* 提出先对基态 MOs 进行受约束优化（*frozen*，冻结步骤），然后将其结果用于设置完整的 MO 弛豫（*release*，释放步骤）。[[1212]](../bib_references/bib.md#bib1267)

**Q-Chem** 中实现了一种受该工作启发的受约束优化算法，[[144]](../bib_references/bib.md#bib134)

称为 FRZ MO 猜测（FRZ MO guess）。
该方法与第 [7.7.5](ex_BEDSCF.md) 节的 SGM 算法相结合，用于超分子复合物中具挑战性的电荷转移（CT）激发计算。[[511]](../bib_references/bib.md#bib526)

我们称这种电子结构方法为冻结-释放电子结构方法，即 FRZ-SGM。

![Figure 7.1: $\mathbf{C}$ matrix partitioning for frozen electron-and-hole constrained optimization.
Panel A shows the example of a double excitation from MO no. 2, with the energy $\varepsilon_{2}$ ,
to MO no. 4, with the energy $\varepsilon_{4}$ , on an arbitrary energy axis E.
The $\mathbf{C}$ matrix is given in the general form in panel B.
Active doubly-occupied vectors are highlighted in red, active virtual orbitals in green,
and all frozen vectors in grey.](../assets/x1.png)

*图 7.1：冻结电子-空穴受约束优化中 $\mathbf{C}$ 矩阵的分区。
面板 A 展示了在任意能量轴 E 上，从能量为 $\varepsilon_{2}$ 的 2 号 MO 到能量为 $\varepsilon_{4}$ 的 4 号 MO 的双重激发示例。
面板 B 给出了 $\mathbf{C}$ 矩阵的一般形式。
活性双占据向量以红色高亮，活性虚轨道以绿色高亮，所有冻结向量以灰色表示。*

要设置带约束轨道的电子结构计算，在用酉变换（unitary transformation）更新 $\mathbf{C}$ 矩阵时，需要将 MO 旋转分组为*活性（active）*和*冻结（frozen）*两类。
在受限 Kohn–Sham（Restricted Kohn–Sham, RKS）理论中，该矩阵被划分为占据和未占据（虚）*子空间（sub-spaces）*。
我们先描述最简单的 RKS 矩阵情形，然后将公式推广到非受限 Kohn–Sham（Unrestricted Kohn–Sham, UKS）理论。
在计算开始时需要**手动重新排序** $\mathbf{C}$ 矩阵中的 MO 列向量，以便正确地冻结相应的占据/虚 MO。在冻结 RKS 中，$\mathbf{C}$ 矩阵具有图 [7.1](#fig:FRZ-Cmat) 所示的结构，其中冻结块的大小由 *$rem* 变量 a_frozen 和 va_frozen 分别针对双占据块和虚块给出。
**重新排序 MO 由用户自行负责**，需要将激发电子置于 D 块最右侧的块中，将空穴置于 V 块最右侧的块中；
这是通过 *$reorder_alpha* 输入段完成的。
该结构将用于构造 MO 旋转，以及计算相应的梯度和步长。
在图 [7.1](#fig:FRZ-Cmat) 面板 A 所示的简单示例中，通过将 1 个 $\alpha$ 电子和 1 个 $\beta$ 电子从 2 号 MO 激发到 4 号 MO 来计算双重激发，且 MOs 按 1-4-3-5-6-2 的顺序排列。
D${}_{\mathrm{f}}$ 和 V${}_{\mathrm{f}}$ 块分别只包含 4 号和 2 号 MO。
图 [7.1](#fig:FRZ-Cmat) 面板 B 使用上文引入的通用记号，描绘了通过将 $\mathbf{C}$ 矩阵划分为活性和冻结部分而形成的块结构。

该结构可推广到 UKS 电子结构。
在 UKS 情形下，分别对 $\alpha$ 和 $\beta$ MO 集合执行两次独立的 RKS 计算。由于可能存在 $\alpha$ 和 $\beta$ 电子的激发，因此引入 b_frozen 和 vb_frozen 来冻结 $\beta$ MOs。
$\beta$ MOs 可以使用 *$reorder_beta* 输入段进行重新排序。

FROZEN_ORBITAL

### `FROZEN_ORBITAL`

> **启用受约束优化库（在输出文件中打印 A frozen … calculation will be performed using … ）。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不执行受约束优化。
>     * TRUE
>     * 执行受约束优化。
> * **建议**: 仅与 GDM 优化算法配合使用。为使受约束优化有效，用户必须按照上文说明手动重新排序 MOs。

A_FROZEN

### `A_FROZEN`

> **设置在 RKS 或 UKS 计算中冻结的 $\alpha$ MOs 数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 不冻结任何向量。
>     * Af
>     * 冻结最后 Af 个占据
>     * $\alpha$
>     * MOs。
> * **建议**: 无

VA_FROZEN

### `VA_FROZEN`

> **设置在 RKS 或 UKS 计算中冻结的虚 $\alpha$ MOs 数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `FALSE`
> * **选项**:
>     * 0
>     * 不冻结任何向量。
>     * VAf
>     * 冻结最后 VAf 个虚
>     * $\alpha$
>     * MOs。
> * **建议**: 无

B_FROZEN

### `B_FROZEN`

> **设置在 UKS 计算中冻结的 $\beta$ MOs 数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不冻结任何向量。
>     * Bf
>     * 冻结最后 Bf 个占据
>     * $\beta$
>     * MOs。
> * **建议**: 无

VB_FROZEN

### `VB_FROZEN`

> **设置在 UKS 计算中冻结的虚 $\beta$ MOs 数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `FALSE`
> * **选项**:
>     * 0
>     * 不冻结任何向量。
>     * VBf
>     * 冻结最后 VBf 个虚
>     * $\beta$
>     * MOs。
> * **建议**: 无

???+ example "示例 7.7.56：使用 FRZ-SGM 方法计算四氟乙烯–乙烯二聚体中最低层间分子间电荷转移激发的冻结-释放计算输入示例 144 Bogo N. et al. Phys. Chem. Chem. Phys. (2025) , 27 , pp. 17533 . Link ."
    ```qchem
    $molecule
    0 1
    F     -1.394866    -1.110938     -0.741831
    F     -1.394866     1.110938     -0.741831
    F      1.394866    -1.110938     -0.741831
    F      1.394866     1.110938     -0.741831
    C     -0.667784     0.000000     -0.759941
    C      0.667784     0.000000     -0.759941
    H     -1.244242     0.935429      2.658551
    H     -1.244242    -0.935429      2.658551
    H      1.244242     0.935429      2.658551
    H      1.244242    -0.935429      2.658551
    C     -0.674558     0.000000      2.662317
    C      0.674558     0.000000      2.662317
    $end
    
    $rem
       thresh              12
       scf_convergence     8
       method              LRC-wPBE
       basis               def2-TZVP
       scf_algorithm       diis_gdm
       sym_ignore          true
       symmetry            false
    $end
    
    @@@
    
    $rem
       frozen_orbital      true
       a_frozen            1
       va_frozen           1
       scf_algorithm       gdm
       unrestricted        true
       thresh              10
       scf_convergence     6
       method              LRC-wPBE
       basis               def2-TZVP
       scf_max_cycles      500
       sym_ignore          true
       symmetry            false
    $end
    
    $molecule
    read
    $end
    
    $reorder_alpha
    1 8
    2 10
    3 11
    4 12
    5 13
    6 14
    7 15
    8 1
    9 9
    10 2
    11 3
    12 4
    13 5
    14 6
    15 7
    $end
    
    @@@
    
    $rem
       frozen_orbital      false
       scf_algorithm       sgm
       cis_nroots          10
       unrestricted        true
       thresh              12
       method              LRC-wPBE
       basis               def2-TZVP
       scf_guess           read
       sym_ignore          true
       symmetry            false
    $end
    
    $molecule
    read
    $end
    
    $sgm
       sgm_evals 30
       sgm_es_threshold 1.0d-4
    $end
    ```
