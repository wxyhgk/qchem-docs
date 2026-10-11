---
title: "4.3.2 Job Control"
---

## 4.3.2 作业控制（Job Control）

(July 4, 2026)

若要运行 HF 计算，必须指定以下两个 *$rem* 变量：

METHOD

### `METHOD`

> **指定交换-关联泛函。**
>
> * **类型**: `STRING`
> * **默认值**: `无默认值`
> * **选项**:
>     * NAME
>     * Use
>     * =
>     * NAME
>     * , where
>     * NAME
>     * is one of the following:
>     * HF
>     * for Hartree-Fock theory;
>     * one of the DFT methods listed in Section
>     * 5.3.5
>     * .;
>     * one of the correlated methods listed in Sections
>     * 7.9
>     * ,
>     * 7.10
>     * , and
>     * 7.8
>     * ;
> * **建议**: 一般而言，请参考文献以指导你的选择。我们对密度泛函理论（DFT）的推荐在第 5.3.5 节中以粗体标出。

BASIS

### `BASIS`

> **指定要使用的基组（Basis Set）。**
>
> * **类型**: `STRING`
> * **默认值**: `无默认基组`
> * **选项**:
>     * General, Gen
>     * User defined (
>     * $basis
>     * keyword required).
>     * Symbol
>     * Use standard basis sets as per Chapter
>     * 8
>     * .
>     * Mixed
>     * Use a mixture of basis sets (see Chapter
>     * 8
>     * ).
> * **建议**: 请参考文献和综述以辅助你的选择。

此外，可以使用以下 *$rem* 变量来自定义自洽场（SCF）计算：

GEN_SCFMAN

### `GEN_SCFMAN`

> **对当前 SCF 计算使用 GEN_SCFMAN。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `TRUE`
> * **选项**:
>     * FALSE
>     * Use the previous SCF code.
>     * TRUE
>     * Use GEN_SCFMAN.
> * **建议**: 在需要用到 GEN_SCFMAN 尚未支持的功能时，设置为 FALSE。

ORBITAL_ENERGY_PREC

### `ORBITAL_ENERGY_PREC`

> **获取更高精度的轨道能数值位数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * Standard printout with 4 decimal digits (in Hartree).
>     * 1
>     * 5 decimal digits.
>     * 2
>     * Scientific notation with 10 digits of precision.
> * **建议**: 按需设置。在打印轨道对称性标签的情况下本变量无效；若在此类情况下需要更高精度，请使用 SYM_IGNORE = TRUE。

PRINT_ORBITALS

### `PRINT_ORBITALS`

> **在输出的分析部分打印带原子标签的轨道系数。**
>
> * **类型**: `INTEGER/LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * Do not print any orbitals.
>     * TRUE
>     * Prints occupied orbitals plus 5 virtual orbitals.
>     * NVIRT
>     * Number of virtual orbitals to print.
> * **建议**: 使用 true，除非需要打印更多虚轨道。

SCF_CONVERGENCE

### `SCF_CONVERGENCE`

> **当波函数误差小于 $10^{-\mathrm{SCF\_CONVERGENCE}}$ 时，即认为 SCF 已收敛。请同时调整 THRESH 的取值。**
>
> * **类型**: `INTEGER`
> * **默认值**: `5`
> * **选项**:
>     * User-defined
> * **建议**: 对于几何优化和振动分析，推荐使用更严格的收敛判据。较大的数值可提供更多有效数字，但计算代价也更高。从 Q-Chem 3.0 开始，DIIS 误差以最大误差衡量，而非早期版本所使用的均方根（RMS）误差。

UNRESTRICTED

### `UNRESTRICTED`

> **控制使用受限轨道还是非受限轨道。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * Constrain the spatial part of the alpha and beta orbitals to be the same.
>     * TRUE
>     * Do not Constrain the spatial part of the alpha and beta orbitals.
> * **建议**: 除非需要 ROHF，否则使用默认值。注意，对电子数为偶数的体系进行非受限计算时，通常需要在初始猜测中打破 $\alpha$ / $\beta$ 对称性，方法是使用 SCF_GUESS_MIX 或提供 $occupied 信息（见第 4.4 节关于初始猜测的内容）。

使用其他更特殊轨道类型的计算由以下 *$rem* 变量控制（当 GEN_SCFMAN = FALSE 时它们不起作用）：

OS_ROSCF

### `OS_ROSCF`

> **使用 GEN_SCFMAN 进行开壳层单重态 ROSCF 计算。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * OS_ROSCF calculation is performed.
>     * FALSE
>     * Do not run OS_ROSCF (it will run a closed-shell RSCF calculation instead).
> * **建议**: 按需设置为 TRUE。

ROSCF_DODS

### `ROSCF_DODS`

> **使用 GEN_SCFMAN 进行正则受限开壳层计算（也称为 "ROSCF-DODS"，其中 DODS 表示不同自旋使用不同轨道，different orbitals for different spins）。仅适用于高自旋半满开壳层体系。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * Perform a canonical ROSCF calculation.
>     * FALSE
>     * Do not perform a canonical ROSCF calculation (run an open-shell USCF
>     * calculation instead).
> * **建议**: 按需设置为 TRUE。

GHF

### `GHF`

> **使用 GEN_SCFMAN 进行广义 Hartree-Fock（GHF）计算。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * Run a GHF calculation.
>     * FALSE
>     * Do not use GHF.
> * **建议**: 按需设置为 TRUE。

COMPLEX

### `COMPLEX`

> **使用 GEN_SCFMAN 进行基于复数分子轨道（MO）的 SCF 计算。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * Use complex orbitals.
>     * FALSE
>     * Use real orbitals.
> * **建议**: 按需设置为 TRUE。

COMPLEX_MIX

### `COMPLEX_MIX`

> **将实部 HOMO 的某一百分比混合到 LUMO 的虚部中。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0–100
>     * The mix angle =
>     * $\pi\cdot$
>     * /100.
> * **建议**: 这可能有助于找到稳定的复数解（与 SCF_GUESS_MIX 的思路类似）。

???+ example "示例 4.1: 使用 GEN_SCFMAN 对甲醛第一激发态进行受限开壳层单重态 ROSCF 计算。第一个作业通过受限 SCF 计算提供猜测轨道。"
    ```qchem
    $molecule
       0 1
       H -0.940372  0.000000  1.268098
       H  0.940372  0.000000  1.268098
       C  0.000000  0.000000  0.682557
       O  0.000000  0.000000 -0.518752
    $end
    
    $rem
       GEN_SCFMAN        true
       METHOD            wb97x-d
       BASIS             def2-svpd
       THRESH            14
       SCF_CONVERGENCE   9
    point_group_symmetry False
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE           sp
       METHOD            wb97x-d
       BASIS             def2-svpd
       GEN_SCFMAN        true
       OS_ROSCF          true
       THRESH            14
       SCF_CONVERGENCE   9
       SCF_ALGORITHM     diis
    point_group_symmetry False
       SCF_GUESS         read
    $end
    ```
