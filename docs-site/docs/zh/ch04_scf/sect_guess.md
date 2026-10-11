---
title: "4.4.2 初猜类型（Initial Guess Types）"
---

## 4.4.2 初猜类型（Initial Guess Types）

（2026 年 7 月 4 日）

**核哈密顿量（Core Hamiltonian）**

核哈密顿量初猜 simply 通过对角化式 ([4.19](Ch4.S2.SS2.md#eq417)) 中的核哈密顿量矩阵来获得初猜分子轨道（MO）系数。它也常被称为单电子初猜（one-electron guess），因为它完全忽略电子间相互作用。尽管该初猜对单电子体系是精确的，但由于缺少排斥效应，会导致原子的壳层结构不正确，并使所有电子都聚集到体系中最重的原子上；相关讨论参见文献 [[797]](../bib_references/bib.md#bib831)。
由于这些效应，核初猜通常极不准确，只应作为最后的手段使用；各类 SAD 和 SAP 初猜提供了好得多的替代选择。

**原子密度叠加（Superposition of Atomic Densities, SAD）**

SAD 初猜[[801]](../bib_references/bib.md#bib1446)
通过累加预先计算的、球平均的原子密度矩阵来构造。SAD 初猜通常能带来稳健的收敛，在使用大基组和/或大分子时尤其重要。需要注意与 SAD 初猜相关的三个问题：

1. **1.**

不会得到分子轨道，这意味着需要轨道的 SCF 算法（即第 [4.5](sect_convergence.md)
节讨论的直接最小化方法）无法直接使用 SAD 初猜。不过，对于一般基组（BASIS = GEN），它可以按下文所述在线（on-the-fly）生成，但对混合基组（BASIS = MIXED）则不行。
2. **2.**

SAD 初猜不适用于一般（读入的）基组（所有内部基组都有预先计算的初猜）；以及
3. **3.**

SAD 初猜不是幂等的，因此*至少*需要两次 SCF 迭代，以确保 SCF 正确收敛（即密度矩阵的幂等性）。

**纯化原子密度叠加（Purified SAD, SADMO）**

纯化后的
SAD 初猜（在文献 [[797]](../bib_references/bib.md#bib831)
中称为 "SADMO"），除消除了上述问题 [1](#sad-noorb) 和 [3](#sad-noid)
之外，与 SAD 初猜完全相同。SADMO 初猜通过对角化非幂等的 SAD 密度矩阵来获得初猜轨道及相应的占据数，随后按照构造原理（aufbau）占据 SAD 自然轨道，重新构造出一个幂等的密度矩阵。由于初始密度矩阵是用 SAD 初猜生成的，SADMO 初猜同样不适用于一般（读入的）基组。

**原子势叠加（Superposition of Atomic Potentials, SAP）**

SAP 初猜[[797]](../bib_references/bib.md#bib831)
是对核初猜的重大改进，它既能正确描述原子的壳层结构，又保持了简单的形式。SAP 初猜通过叠加预先计算的原子势来引入核初猜所缺失的电子间相互作用，这些原子势由全数值计算导出；[[798]](../bib_references/bib.md#bib832)
**Q-Chem** 中使用的原子势则由采用球平均密度的非相对论、仅交换（exchange-only）LDA 计算导出。[[799]](../bib_references/bib.md#bib833)
如文献 [[797]](../bib_references/bib.md#bib831)
所建议，原子势矩阵通过与 DFT 计算所用网格类似的分子网格上的数值求积来评估；该网格由 *$rem*
变量 GUESS_GRID 控制。重要的是，SAP 初猜是非迭代的，可用于元素周期表中从 H 到 Og 的所有元素，并且既可用于内部基组，也可用于一般（读入的）基组，从而在其他选项失效的情况下仍能提供相当准确的初始猜测。请注意，SAP 初猜在旧版 SCF 代码中不可用，只能在 GEN_SCFMAN 中使用。

**在线（自动化）原子密度叠加（On-the-fly/Automated SAD, AUTOSAD）**

与依赖预先计算的密度矩阵的 SAD 选项不同，AUTOSAD 初猜通过对体系中所有不等价原子分别运行独立的原子计算，在线地获得与具体方法相关的 SAD 初猜。作为一种 SAD 初猜，AUTOSAD 密度矩阵不是幂等的，且该初猜不会生成分子轨道，因此无法直接使用直接最小化方法。与 SAD 选项不同，AUTOSAD 既可用于内部定义的基组，也可用于用户定义的（一般）基组，但目前不支持混合基组。注意，当在波函数方法中使用单一的内部基组时，无需使用 AUTOSAD，因为此时 AUTOSAD 密度与预先计算的 SAD 密度完全等价。预先计算的 SAD 初猜基于 Hartree-Fock 原子密度，而 AUTOSAD 使用在 *$rem* 中指定的 SCF 方法。

**广义 Wolfsberg-Helmholtz（Generalized Wolfsberg-Helmholtz, GWH）**

GWH 初猜
程序[[1487]](../bib_references/bib.md#bib1547)
结合了式 ([4.12](Ch4.S2.SS1.md#eq411)) 中的重叠矩阵元与式 ([4.19](Ch4.S2.SS2.md#eq417)) 中核哈密顿量矩阵的对角元。这一初始猜测通常甚至比核哈密顿量初猜更差。[[797]](../bib_references/bib.md#bib831)

其构造方式为

<a id="eq444"></a>

$$
H_{\mu\upsilon}=c_{x}S_{\mu\upsilon}(H_{\mu\mu}+\tfrac{1}{2}H_{\upsilon\upsilon})\;. \tag{4.29}
$$

其中 $c_{x}$ 为常数，通常取 $c_{x}=1.75$。

上述各选项的选择（或是否读入轨道）由以下 *$rem* 变量控制：

SCF_GUESS

### `SCF_GUESS`

> **指定 SCF 所使用的初始猜测程序。**
>
> * **类型**：`STRING`
> * **默认值**：`SAD`
> * **选项**：
>     * CORE
>     * 对角化核哈密顿量
>     * SAD
>     * 原子密度叠加
>     * 801
>     * Lenthe J. H. Van et al.
>     * J. Comput. Chem.
>     * (2006)
>     * ,
>     * 27
>     * ,
>     * pp. 926
>     * .
>     * 链接
>     * SAP
>     * 原子势叠加
>     * 797
>     * Lehtola S.
>     * J. Chem. Theory Comput.
>     * (2019)
>     * ,
>     * 15
>     * ,
>     * pp. 1593
>     * .
>     * 链接
>     * （仅当以下取值时可用
>     * GEN_SCFMAN
>     * =
>     * TRUE
>     * ）
>     * AUTOSAD
>     * 在线（on-the-fly）原子密度叠加
>     * SADMO
>     * 纯化原子密度叠加（仅随
>     * 标准基组可用）
>     * GWH
>     * 采用广义 Wolfsberg-Helmholtz 近似
>     * READ
>     * 从磁盘读取先前的 MO
>     * FRAGMO
>     * 叠加已收敛的
>     * 片段 MO（参见第
>     * 12.3
>     * 节）
> * **建议**：对于标准基组，建议使用 SAD、AUTOSAD 或 SADMO 初猜。无论使用标准基组还是用户自定义的一般基组，均推荐使用 AUTOSAD，且其为默认选项。若这些选项均失效，请使用 SAP 初猜；仅将 GWH 或核哈密顿量初猜作为最后手段。对于混合基组，目前仅可用 AUTOSAD、SAP、GWH 和核哈密顿量初猜。对于 ROHF，从相应阳离子或阴离子的 SCF 计算中 READ 初猜可能很有用。注意，由于密度被球对称化，这可能使原子体系（尤其是过渡金属）倾向于非期望的状态。在片段 MO 计算中使用 FRAGMO。

SCF_GUESS_ALWAYS

### `SCF_GUESS_ALWAYS`

> **开关，用于强制在每一轮 SCF 迭代开始时重新生成新的初始猜测（用于几何优化）。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`False`
> * **选项**：
>     * False
>     * 在优化的每一轮 SCF 迭代中不生成新的初猜；若可用，
>     * 则使用上一次 SCF 计算的 MO 作为初猜，
>     * （如果存在的话）。
>     * True
>     * 在几何优化的每一轮 SCF 迭代中
>     * 生成新的初猜。
> * **建议**：除非出现 SCF 收敛问题，否则使用默认值。

GUESS_GRID

### `GUESS_GRID`

> **指定生成 SAP 初猜时使用的网格类型。其选项与 *$rem* 变量 XC_GRID 相同。**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **选项**：
>     * 0
>     * 对 H、C、N 和 O 使用 SG-0；对其他所有原子使用 SG-1。
>     * $n$
>     * 对所有原子使用 SG-
>     * $n$
>     *，其中
>     * $n=1,2$
>     * 或 3
>     * $XY$
>     * 由两个六位整数
>     * $X$
>     * 和
>     * $Y$
>     * 组成的字符串，其中
>     * $X$
>     * 是径向点数，
>     * $Y$
>     * 是角向点数；可能的 Lebedev 角向点数必须是
>     * 表
>     * 5.2
>     * （位于
>     * 第
>     * 5.5
>     * 节）中允许的取值之一。
>     * $-XY$
>     * 用于高斯-勒让德（Gauss-Legendre）网格的类似格式，六位整数
>     * $X$
>     * 表示径向点数，六位整数
>     * $Y$
>     * 给出具
>     * 高斯-勒让德角向点数，
>     * $Y=2N^{2}$
>     * 。
> * **建议**：如果 SAP 初猜较差，可能需要使用更大的网格。
