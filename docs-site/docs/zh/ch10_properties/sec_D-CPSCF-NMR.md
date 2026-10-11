---
title: "10.11.3 线性标度 NMR 化学位移计算"
---

## 10.11.3 线性标度 NMR 化学位移计算

（2026 年 7 月 4 日）

在传统实现方案中，即使采用最简单的量子化学方法（如 Hartree-Fock 或 DFT），核磁共振（NMR）化学位移的计算成本也随分子体系尺寸 $M$ 呈立方增长，即 ${\cal{O}}({M^{3}})$。因此，在不考虑对称性的情况下，NMR 化学位移计算大多局限于约 100 个原子量级的分子体系。对于更大的体系，将计算量的增长降低至线性标度至关重要；这对于具有非零 HOMO/LUMO 能隙的体系是可行的，并由 Kussmann 与 Ochsenfeld 首次报道。[[1010]](../bib_references/bib.md#bib1054)

该方法相对于传统立方标度实现不会损失任何精度，并使采用 Hartree-Fock 或 DFT 方法对含 1,000 个以上原子的分子体系进行 NMR 化学位移计算成为可能。例如，对于许多分子体系，Hartree-Fock（GIAO-HF）方法在计算 ${}^{1}$H NMR 化学位移时通常可达到 0.2–0.4 ppm 的精度。[[1013]](../bib_references/bib.md#bib1051) 已有文献报道在不利用对称性的情况下，对含 1,003 个原子、8,593 个基函数的体系执行 GIAO-HF/6-31G* 计算。[[1010]](../bib_references/bib.md#bib1054) 对于不含 Hartree-Fock 交换项的密度泛函，GIAO-DFT 计算甚至更为简单快捷。

**Q-Chem** 中 NMR 磁屏蔽的各向异性（shieldings）实现采用 LinK（线性 Hartree-Fock 交换，linear Hartree-Fock exchange）方法[[1011]](../bib_references/bib.md#bib1049) 来构建交换贡献项。[[1010]](../bib_references/bib.md#bib1054) 由于密度矩阵对磁场的导数是反对称（skew-symmetric）的，其库仑型（Coulomb-type）收缩项为零。对于剩余的库仑型矩阵，采用 CFMM 方法。[[1463]](../bib_references/bib.md#bib1518) [[1010]](../bib_references/bib.md#bib1054) 此外，**Q-Chem** 中还提供了多种求解 CPSCF 方程的方法可供选择。

若要通过密度矩阵方法请求 NMR 化学位移计算，需在 *$rem* 段中将 JOBTYPE 设置为 NMR。
其他作业控制变量列于下方。

D_CPSCF_PERTNUM

### `D_CPSCF_PERTNUM`

> **指定是逐个处理微扰，还是将所有微扰一并处理。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 一并计算所有微扰密度。
>     * 1
>     * 逐个计算微扰密度。
> * **建议**: 无

D_SCF_CONV_1

### `D_SCF_CONV_1`

> **设置 level-1 迭代的收敛判据。该步骤为 level-2 计算对密度进行预条件处理，不包含任何双电子积分。**
>
> * **类型**: `INTEGER`
> * **默认值**: `4`
> * **选项**:
>     * $n<10$
>     * 将收敛阈值设置为
>     * $10^{-n}$
>     * 。
> * **建议**: level-1 收敛判据必须小于或等于 level-2 判据，否则 D-CPSCF 将无法收敛。

D_SCF_CONV_2

### `D_SCF_CONV_2`

> **设置 level-2 迭代的收敛判据。**
>
> * **类型**: `INTEGER`
> * **默认值**: `4`
> * **选项**:
>     * $n<10$
>     * 将收敛阈值设置为
>     * $10^{-n}$
>     * 。
> * **建议**: 无

D_SCF_MAX_1

### `D_SCF_MAX_1`

> **设置 level-1 迭代的最大次数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `100`
> * **选项**:
>     * $n$
>     * 由用户自定义。
> * **建议**: 使用默认值。

D_SCF_MAX_2

### `D_SCF_MAX_2`

> **设置 level-2 迭代的最大次数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `30`
> * **选项**:
>     * $n$
>     * 由用户自定义。
> * **建议**: 使用默认值。

D_SCF_DIIS

### `D_SCF_DIIS`

> **指定在 D-CPSCF 的 DIIS 外推中使用的矩阵数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `11`
> * **选项**:
>     * $n$
>     * $n$
>     * = 0 表示不使用 DIIS 外推。
> * **建议**: 使用默认值。

???+ example "示例 10.61：通过 D-CPSCF 方法计算 NMR 化学位移，展示所有输入选项。"
    ```qchem
     $molecule
     0  1
     H        0.00000        0.00000        0.00000
     C        1.10000        0.00000        0.00000
     F        1.52324        1.22917        0.00000
     F        1.52324       -0.61459        1.06450
     F        1.52324       -0.61459       -1.06450
     $end
    
     $rem
        JOBTYPE            NMR
        EXCHANGE           B3LYP
        BASIS              6-31G*
        D_CPSCF_PERTNUM    0    D-CPSCF number of perturbations at once
        D_SCF_SOLVER       430  D-SCF   leqs_solver
        D_SCF_CONV_1       4    D-SCF   leqs_conv1
        D_SCF_CONV_2       4    D-SCF   leqs_conv2
        D_SCF_MAX_1        200  D-SCF   maxiter level 1
        D_SCF_MAX_2        50   D-SCF   maxiter level 2
        D_SCF_DIIS         11   D-SCF   DIIS
        D_SCF_ITOL         2    D-SCF   conv. criterion
     $end
    ```
