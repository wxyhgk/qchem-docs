---
title: "11.2.4 PCM 任务控制"
---

## 11.2.4 PCM 任务控制

(2026 年 7 月 4 日)

通过在 *$rem* 输入段中设置 SOLVENT_METHOD = PCM 即可请求 PCM 计算。如上所述，PCM 家族包含多种不同的理论模型，因此可能需要进行额外的微调，具体如下所述。

## 11.2.4.1 *$pcm* 输入段

大部分 PCM 任务控制是通过 *$pcm* 输入段中指定的选项来实现的，该输入段允许用户指定将使用哪一种 PCM 模型、采用何种算法求解 PCM 方程，以及其他选项。*$pcm* 输入段的格式与 *$rem* 输入段类似：

> ```qchem
> $pcm
>    <Keyword>  <parameter/option>
> $end
> ```

**注意：

以下任务控制变量*只能*放在 *$pcm* 输入段中。
请勿将其放入 *$rem* 输入段中。
**

### `Theory`

> **指定将使用的极化连续介质模型（Polarizable Continuum Model）。输入段：$pcm**
>
> * **类型**：`STRING`
> * **默认值**：`CPCM`
> * **选项**：
>     * CPCM
>     * 导体近似 PCM（Conductor-like PCM），见文献
>     * 275
>     * Cossi M. et al.
>     * J. Comput. Chem.
>     * (2003)
>     * ,
>     * 24
>     * ,
>     * pp. 669
>     * .
>     * Link
>     * ,
>     * 其中
>     * $f_{\varepsilon}=(\varepsilon-1)/\varepsilon$
>     * 。
>     * CPCM1
>     * 等价于 CPCM。
>     * CPCM2
>     * 最初的导体近似屏蔽模型（conductor-like screening model），见文献       * ，其中
>     * $f_{\varepsilon}=(\varepsilon-1)/(\varepsilon+1/2)$
>     * 。
>     * IEFPCM
>     * 采用非对称
>     * $\mathbf{K}$
>     * 矩阵的 IEF-PCM。
>     * SSVPE
>     * SS(V)PE 模型，等价于采用对称
>     * $\mathbf{K}$
>     * 矩阵的 IEF-PCM。
> * **建议**：IEF-PCM/SS(V)PE 模型比 C-PCM 更为精细，在形式上也更适合低介电常数的溶剂，但使用起来也更复杂。实际上，这些模型之间往往差别不大；参见文献 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . Link 。关于两种版本的 C-PCM 以及式 ( 11.3 ) 中 $f_{\varepsilon}$ 的选取，有文献建议对中性溶质取 $x=0$，对离子取 $x=1/2$；关于这些区别的讨论，请再次参见文献 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . Link 。

### `Method`

> **指定将使用的表面离散化方法。输入段：$pcm**
>
> * **类型**：`STRING`
> * **默认值**：`SwiG`
> * **选项**：
>     * SwiG
>     * 切换/高斯（Switching/Gaussian）方法
>     * ISwiG
>     * 采用替代切换函数的“改进型”切换/高斯方法
>     * Spherical
>     * 对空腔表面使用单个固定球面。
>     * Fixed
>     * 使用离散的点电荷而非平滑高斯函数。
> * **建议**：推荐使用 SwiG，仅仅是因为它比 ISwiG 的切换函数效率略高。另一方面，ISwiG 在概念上具有一些更具吸引力的特性，在某些情况下可能更优。关于这些差异的讨论，请参见文献 754 Lange A. W., Herbert J. M. J. Chem. Phys. (2010) , 133 , pp. 244111 . Link 、756 Lange A. W., Herbert J. M. Chem. Phys. Lett. (2011) , 509 , pp. 77 . Link 。Fixed 选项使用 Li 和 Jensen 提出的可变分片数（Variable Tesserae Number, VTN）算法，812 Li H., Jensen J. H. J. Comput. Chem. (2004) , 25 , pp. 1449 . Link 并配合 Lebedev 网格点。VTN 使用不带切换函数或高斯模糊的点电荷，因此可能出现不连续性，从而在解析梯度中引起误差，并导致几何优化收敛缓慢。753 Lange A. W., Herbert J. M. J. Phys. Chem. Lett. (2010) , 1 , pp. 556 . Link 除非需要与文献中的其他计算结果进行对比，否则不建议使用该方法。

### `Solver`

> **指定用于求解 PCM 方程的算法。输入段：$pcm**
>
> * **类型**：`STRING`
> * **默认值**：`INVERSION`
> * **选项**：
>     * INVERSION
>     * 直接矩阵求逆
>     * CG
>     * 迭代共轭梯度法
> * **建议**：对于较小的溶质分子，矩阵求逆更快，因为在单点能计算中它只需执行一次。然而，当离散化点数接近或超过 $\sim$ 10,000 时，建议使用 CG 求解器（它必须在每次 SCF 迭代中都执行一次）。用于大规模 MM/PCM 和 QM/MM/PCM 计算的线性标度选项将在第 11.2.5 节 中讨论。

### `SwitchThresh`

> **用于判定是否舍弃空腔表面上网格点的阈值。输入部分：$pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `8`
> * **选项**:
>     * $n$
>     * 当切换函数（switching function）小于
>     * $10^{-n}$
>     * 时舍弃网格点。
> * **建议**: 使用默认值，经验证该值可在机器精度范围内避免不连续性。增大 $n$ 可降低 PCM 计算的成本，但可能在势能面中引入不连续性。如果计算中的 PCM 部分开销过大，更好的办法是减少离散化点的数目（即下文所述的 HeavyPoints 和 HPoints），或改用 Solver = CG，而不是调整该参数。

溶质空腔的构建是该模型的重要组成部分，用户应就此查阅相关文献，尤其是关于原子球所采用的半径。**Q-Chem** 提供的默认值对应于几十年来形成的共识做法，即使用经因子 $\alpha_{\text{vdW}}=1.2$ 缩放的范德华（vdW）半径 $\{R_{\text{vdW},A}\}$；参见式 ([11.4](topic_pcm-em.md#eq:PCM_atomic_radii))。最广泛使用的 vdW 半径是由 Bondi 根据晶体学数据确定的，[[146]](../bib_references/bib.md#bib136)
 只不过氢的半径后来被调整为
1.1 Å，[[1186]](../bib_references/bib.md#bib1240)
 而 Bondi 未涉及的主族元素的半径则是在之后的
工作中给出的。[[889]](../bib_references/bib.md#bib923)
 **Q-Chem** 默认使用这套扩展的 vdW 半径，为简便起见，我们将其统称为 “Bondi 半径”，无论其来源于 Bondi 的原始论文还是后来的工作。另外，也可以使用来自通用力场（Universal Force Field, UFF）的原子半径。[[1146]](../bib_references/bib.md#bib1198)
 UFF 半径的主要吸引力在于它们对元素周期表中所有原子都有定义，不过这些半径在 PCM 应用中的质量尚不明确。

### `Radii`

> **指定用于定义溶质空腔的原子范德华半径（van der Waals Radii）集合。输入部分：$pcm**
>
> * **类型**: `STRING`
> * **默认值**: `Bondi`
> * **选项**:
>     * Bondi
>     * 使用（扩展的）Bondi 半径集合（参见文献
>     * 1186
>     * Rowland R. S., Taylor R.
>     * J. Phys. Chem.
>     * (1996)
>     * ,
>     * 100
>     * ,
>     * pp. 7384
>     * .
>     * Link
>     * ）。
>     * FF
>     * 使用来自分子力学力场的 Lennard-Jones 半径。
>     * UFF
>     * 使用来自通用力场（Universal Force Field）的半径（参见文献
>     * 1146
>     * Rappé A. K. et al.
>     * J. Am. Chem. Soc.
>     * (1992)
>     * ,
>     * 114
>     * ,
>     * pp. 10024
>     * .
>     * Link
>     * ）。
>     * Read
>     * 从
>     * $van_der_waals
>     * 输入部分读取原子半径。
> * **建议**: Bondi 半径被广泛使用。选项 FF 要求用户在 $rem 部分通过 FORCE_FIELD 变量指定分子力学力场，并在 $molecule 部分定义原子类型（见第 11.3 节）。使用 UFF 半径时则不需要这些设置。对于用户自定义半径，$van_der_waals 输入部分的格式见第 11.2.10 节。

### `vdwScale`

> **用于定义溶质空腔的原子范德华半径的缩放因子。输入部分：$pcm**
>
> * **类型**: `FLOAT`
> * **默认值**: `1.2`
> * **选项**:
>     * $\alpha$
>     * 使用缩放因子
>     * $\alpha>0$
>     * 。
> * **建议**: 该默认值在 PCM 计算中被广泛使用，但如果采用溶剂可及表面（solvent-accessible surface），取值 1.0 可能更为合适。

### `SASradius`

> **以给定的溶剂探针半径构建“溶剂可及”表面。输入部分：$pcm**
>
> * **类型**: `FLOAT`
> * **默认值**: `0.0`
> * **选项**:
>     * $r$
>     * 使用溶剂探针半径
>     * $r$
>     * ，单位为 Å。
> * **建议**: 溶剂探针半径会加到溶质原子经缩放后的范德华半径上。水常用的溶剂探针半径为 1.4 Å，但历史上也曾使用更小的值（0.2–0.5 Å）。 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . Link

### `SurfaceType`

> **选择溶质空腔表面的构建方式。输入部分：$pcm**
>
> * **类型**: `STRING`
> * **默认值**: `VDW_SAS`
> * **选项**:
>     * VDW_SAS
>     * 范德华表面或溶剂可及表面
>     * SES
>     * 溶剂排除表面（solvent-excluded surface）
> * **建议**: vdW 表面和溶剂可及表面（SAS）均仅由原子球构成，因此二者共用相同的选项；唯一区别在于是否指定溶剂探针半径 SASradius。对于真正的 vdW 表面，探针半径应为零（此即默认值）；而对于 SAS，传统上原子半径不进行缩放，因此应将 vdwScale 设为 1.0（这并非默认值）。对于 SES，仅有 SwiG 离散化方案可用，但它可以与任何（缩放或未缩放的）原子半径集合，或经 SASradius 增大的半径配合使用。

请注意 **Radii** 关键字的说明：用户可以使用 *$van_der_waals* 输入部分为空腔构建指定自己的原子半径。
若要为给定分子指定全部半径，请使用第 [11.2.10](subsec_LD.md) 节中描述的 *$van_der_waals* 部分的格式。
或者，如果只是需要指定某个半径集合中所缺失的半径（例如 Bondi 半径集合并未对整个元素周期表给出定义），
则无需设置 **Radii** = **Read** 即可实现。此时保持
**Radii** = **Bondi**（或其他选项）不变，但加入一个采用如下格式的 *$van_der_waals* 部分：

> ```qchem
> $van_der_waals
> atomic_number   vdW_radius
> $end
> ```

用户自定义半径不应用任何缩放因子。注意，对于某个特定原子半径，$R=0$ 是允许的，
此时该原子不用于构建空腔表面。
这一特性便于构建“联合原子”（united atom）
空腔，[[78]](../bib_references/bib.md#bib60)
 即氢原子不再单独成球，同时增大重原子半径以作补偿。
作为对 vdW 半径 $\{R_{\text{vdW},A}\}$ 进行缩放的替代方案，用户可以
为每个半径添加一个探针半径 $R_{\text{probe}}$ [参见式 ([11.4](topic_pcm-em.md#eq:PCM_atomic_radii))]，以获得 SAS 空腔。

历史上，空腔表面的离散化一直采用将空腔表面积划分为有限多边形“小面元”（tesserae）的
“镶嵌”（tessellation）方法。（GEPOL 算法[[1044]](../bib_references/bib.md#bib1089)
 可能是使用最广泛的镶嵌方案。）然而，镶嵌方法不仅会导致空腔表面积和溶剂化能随核坐标变化出现不连续性，
而且其解析能量梯度也难以推导和实现。
为避免这些问题，**Q-Chem** 的 SwiG-PCM
实现[[753]](../bib_references/bib.md#bib786)
 采用 Lebedev 网格来离散化原子球。这些是以原子为中心、具有二十面体对称性的网格，
每个原子球可包含 26 至 5294 个网格点不等。**Q-Chem** 所用的默认值是基于大量数值测试选取的，[[754]](../bib_references/bib.md#bib787)
 并且对于 MM 原子（在 MM/PCM 或 QM/MM/PCM 计算中）比 QM 原子更为宽松，
这是因为与 MM 点电荷相比，QM 密度产生的静电势更为复杂。对于 QM 原子，默认对氢原子使用 $N=110$ 个点，对其他所有原子使用 $N=194$ 个点；
而对于 MM 原子，默认氢为 $N=50$，非氢为 $N=110$。这些默认值具有良好的旋转不变性
（分子旋转后 $\Delta G$ 的差异 $<0.1$ kcal/mol[[754]](../bib_references/bib.md#bib787)
），且绝对溶剂化能通常位于
$N\rightarrow\infty$ 极限值的 $<1$ kcal/mol 范围内，[[754]](../bib_references/bib.md#bib787)
 至少对于电中性溶质是如此。

请注意，**Q-Chem** 的早期版本默认使用更密集的网格。（在 **Q-Chem** v. 4.2 及之前的版本中，所有 QM 原子的默认值为 $N=590$，但从 v. 4.2.1 开始改为 $N=302$。上述默认值是自 v. 5.2 起的现行默认值。）不过，约 0.5 kcal/mol 的网格误差完全在这些模型 $\Delta G_{\textrm{solvation}}$ 的内在精度范围之内。激发能溶剂化变色位移（solvatochromatic shift）的网格误差通常约为 0.01–0.02 eV，这完全在几乎所有激发态方法的内在精度范围内。如果对网格精度存有疑问，我们建议将 $N=302$ 作为高质量选项，将 $N=590$ 作为基本收敛的选项。[[754]](../bib_references/bib.md#bib787)

对于大分子，可能需要减少网格点数目（*例如*减至 $N=86$），或使用线性标度求解器而非矩阵求逆，
如第 [11.2.5](subsec_linear-PCM.md) 节所述。

**注意： 

每个原子球可用的 Lebedev 点数目的允许取值为
$N=6$, 26, 38, 50, 86, 110, 146, 170, 194, 302, 350, 434, 590, 770, 974, 1202,
1454, 1730, 2030, 2354, 2702, 3074, 3470, 3890, 4334, 4802, 5294。
**

### `HeavyPoints`

> **在 QM 体系的非氢原子上放置的 Lebedev 网格点数。输入节：$pcm**
>
> * **类型**： `INTEGER`
> * **默认值**： `194`
> * **选项**：
>     * 可接受的取值已在上方列出。
> * **建议**：几何优化时使用默认值。若要计算绝对溶剂化能，用户可能需要考察其相对于 $N$ 的收敛性。

### `HPoints`

> **在 QM 体系的氢原子上放置的 Lebedev 网格点数。输入节：$pcm**
>
> * **类型**： `INTEGER`
> * **默认值**： `110`
> * **选项**：
>     * 可接受的取值已在上方列出。
> * **建议**：几何优化时使用默认值。若要计算绝对溶剂化能，用户可能需要考察其相对于 $N$ 的收敛性。

### `MMHeavyPoints`

> **在 MM 子体系的非氢原子上放置的 Lebedev 网格点数。输入节：$pcm**
>
> * **类型**： `INTEGER`
> * **默认值**： `110`
> * **选项**：
>     * 可接受的取值已在上方列出。
> * **建议**：几何优化时使用默认值。若要计算绝对溶剂化能，用户可能需要考察其相对于 $N$ 的收敛性。此选项仅适用于 MM/PCM 或 QM/MM/PCM 计算。

### `MMHPoints`

> **在 MM 子体系的氢原子上放置的 Lebedev 网格点数。输入节：$pcm**
>
> * **类型**： `INTEGER`
> * **默认值**： `50`
> * **选项**：
>     * 可接受的取值已在上方列出。
> * **建议**：几何优化时使用默认值。若要计算绝对溶剂化能，用户可能需要考察其相对于 $N$ 的收敛性。此选项仅适用于 MM/PCM 或 QM/MM/PCM 计算。

尤其是对于复杂的分子，用户可能希望将空腔表面可视化。这可以通过设置 **PrintLevel** $\geq 2$ 来实现，这将触发生成多个描述空腔表面的 `.PQR` 文件。（这些文件被写入 **Q-Chem** 输出文件中。）`.PQR` 格式与常见的 `.PDB`（Protein Data Bank，蛋白质数据库）格式类似，但同时包含每个原子的电荷和半径信息。其中一个输出的 `.PQR` 文件包含 PCM 计算中所得的电荷，以及每个表面网格点所代表表面积平方根的一半作为半径（单位为 Å）。因此，在查看该表面表示时，较大的离散化点对应于较大的表面积。第二个 `.PQR` 文件包含溶质的静电势（单位为原子单位）以取代电荷信息，并对网格点使用统一的半径。这些 `.PQR` 文件可以使用多种第三方软件进行可视化，包括免费提供的 Visual Molecular Dynamics (VMD) 程序，[[W. Humphrey, A. Dalke, and K. Schulten (1996)]](../bib_references/bib.md#bib627) 该程序特别适合根据电荷对 `.PQR` 表面网格点着色，并根据各点对分子表面积的贡献调整其大小。（此类可视化的示例见文献 [[753]](../bib_references/bib.md#bib786)
。）

### `PrintLevel`

> **控制 PCM 计算过程中的打印级别。输入节：$pcm**
>
> * **类型**： `INTEGER`
> * **默认值**： `0`
> * **选项**：
>     * 0
>     * 打印 PCM 能量和基本的表面网格信息。仅输出最少的附加信息。
>     * 1
>     * 在级别 0 的基础上，额外打印 PCM 溶剂-溶剂相互作用能分量和高斯定律误差。
>     * 2
>     * 在级别 1 的基础上，额外打印表面网格切换参数以及一个
>     * .PQR
>     * 文件，用于
>     * 空腔表观表面电荷的可视化。
>     * 3
>     * 在级别 2 的基础上，额外输出一个
>     * .PQR
>     * 文件，用于可视化由收敛溶质在表面网格处产生的静电势。
>     * 4
>     * 在级别 3 的基础上，额外打印表面网格的其他信息，以及每个自洽场（SCF）循环中的静电势
>     * 和表观表面电荷。
>     * 5
>     * 在级别 4 的基础上，额外输出大量的调试信息。
> * **建议**：如无需更多信息，请使用默认值。

最后需要注意的是，在 *$pcm* 输入节中将 **Method** 设置为 **Spherical**，会要求构建一个由单个固定球体组成的溶质空腔。这一般不推荐使用，但有时对于与文献中的 Born 模型结果、或第 [11.2.2](example_SCRF.md) 节中讨论的 Kirkwood-Onsager 模型进行对比很有用。在这种情况下，还必须在 *$pcm* 节中指定空腔半径及其中心。关键字 **HeavyPoints** 控制用于离散化该表面的 Lebedev 网格点数。

### `CavityRadius`

> **指定溶质空腔半径。输入区块：$pcm**
>
> * **类型**： `FLOAT`
> * **默认值**： `None`
> * **选项**：
>     * $R$
>     * 使用半径为
>     * $R$
>     * 的空腔，单位为埃（Ångstroms）。
> * **建议**： 无。

### `CavityCenter`

> **指定球形溶质空腔的中心。输入区块：$pcm**
>
> * **类型**： `FLOAT`
> * **默认值**： `0.0 0.0 0.0`
> * **选项**：
>     * $x$
>     * $y$
>     * $z$
>     * 空腔中心的坐标，单位为埃（Ångstroms）。
> * **建议**： 格式为三个由空格分隔的浮点数值。使用与 $molecule 区块相同的坐标系。

最后，HetPCM 方法（第 [11.2.3.5](topic_pcm-em.md#sec:HetPCM) 节）通过在 *$pcm* 区块中出现关键字 **Het-PCM** 来激活。此类计算需要一个 *$atomic_epsilon* 输入区块，用于为每个原子球指定所用 $\varepsilon$ 的值。其格式就是一个原子编号列表，并为每个原子配以一双精度 $\varepsilon$ 值：

> ```qchem
> $atomic_epsilon
> 1   epsilon_1
> 2   epsilon_2
> 3   epsilon_3
> ...
> $end
> ```

列表中可以省略某些原子，它们将被赋予 $\varepsilon=1$。

### `Het-PCM`

> **若存在此关键字，则激活非均相 PCM（HetPCM）。输入区块：$pcm**
>
> * **类型**： `STRING`
> * **默认值**： `None`
> * **选项**：
>     * 若存在此关键字，则开启 HetPCM
> * **建议**： 需要一个 $atomic_epsilon 区块，为每个原子提供用户指定的介电常数。在 $rem 中设置 PCM_PRINT $\geq 1$ 以确认各原子的 $\varepsilon$ 值已被采用。

## 11.2.4.2 示例

???+ example "示例 11.3：使用 PCM 的基础示例：在水溶剂中优化三氟乙醇。
溶剂介电常数在 $solvent 区块中指定，该区块将在下文描述。"
    ```qchem
    $comment
    2023/4/5 Add geom_opt_driver optimize per #2954, [39888/qchem]
    $end
    
    $molecule
       0 1
       C    -0.245826    -0.351674    -0.019873
       C     0.244003     0.376569     1.241371
       O     0.862012    -0.527016     2.143243
       F     0.776783    -0.909300    -0.666009
       F    -0.858739     0.511576    -0.827287
       F    -1.108290    -1.303001     0.339419
       H    -0.587975     0.878499     1.736246
       H     0.963047     1.147195     0.961639
       H     0.191283    -1.098089     2.489052
    $end
    
    $rem
       JOBTYPE         OPT
       BASIS           6-31G*
       METHOD          B3LYP
       SOLVENT_METHOD  PCM
       geom_opt_driver optimize
    $end
    
    $pcm
       Theory          CPCM
       Method          SWIG
       Solver          Inversion
       HeavyPoints     194
       HPoints         194
       Radii           Bondi
       vdwScale        1.2
    $end
    
    $solvent
       Dielectric 78.39
    $end
    ```

???+ example "示例 11.4：采用单一球形空腔的 PCM，应用于乙腈中的 H ${}_{2}$ O。
与 Kirkwood-Onsager 多极展开法的比较，见第 11.2.2 节示例（第 11.2.2 页）。"
    ```qchem
    $molecule
       0 1
       O       0.00000000     0.00000000     0.11722303
       H      -0.75908339     0.00000000    -0.46889211
       H       0.75908339     0.00000000    -0.46889211
    $end
    
    $rem
       METHOD            HF
       BASIS             6-31g**
       SOLVENT_METHOD    pcm
    $end
    
    $pcm
       method        spherical   ! single spherical cavity with 590 discretization points
       HeavyPoints   590
       CavityRadius  1.8         ! Solute Radius, in Angstrom
       CavityCenter  0.0 0.0 0.0 ! Will be at center of Standard Nuclear Orientation
       Theory        SSVPE
    $end
    
    $solvent
       Dielectric        35.9   !   Acetonitrile
    $end
    ```

最后，我们考虑一个联合原子（united-atom）空腔的示例。注意，此处仅为碳原子提供了用户自定义的范德华半径，因此氢原子的半径取为零，即氢原子不用于构造空腔表面。（如前所述，*$van_der_waals* 输入区块的格式将在第 [11.2.10](subsec_LD.md) 节中讨论）。

???+ example "示例 11.5：乙烯的联合原子空腔构造。"
    ```qchem
    $comment
       Benzene (in benzene), with a united-atom cavity construction
       R = 2.28 A for carbon, R = 0 for hydrogen
    $end
    
    $molecule
       0 1
       C    1.38620    0.000000   0.000000
       C    0.69310    1.200484   0.000000
       C   -0.69310    1.200484   0.000000
       C   -1.38620    0.000000   0.000000
       C   -0.69310   -1.200484   0.000000
       C    0.69310   -1.200484   0.000000
       H    2.46180    0.000000   0.000000
       H    1.23090    2.131981   0.000000
       H   -1.23090    2.131981   0.000000
       H   -2.46180    0.000000   0.000000
       H   -1.23090   -2.131981   0.000000
       H    1.23090   -2.131981   0.000000
    $end
    
    $rem
       EXCHANGE        hf
       BASIS           6-31G*
       SOLVENT_METHOD  pcm
    $end
    
    $pcm
       theory          iefpcm   ! this is a synonym for ssvpe
       method          swig
       printlevel      1
       radii           read
    $end
    
    $solvent
       dielectric 2.27
    $end
    
    $van_der_waals
    1
      6     2.28
      1     0.00
    $end
    ```

???+ example "示例 11.6：非均相（HetPCM）示例，由 $pcm 区块中的 Het-PCM 标志触发。
这是一个质子化组氨酸的截断模型，其中阳离子芳香部分所处的环境为 $\varepsilon=78.4$，而侧链中各原子的 $\varepsilon=10.0$。"
    ```qchem
    
    $molecule
    1 1
      H   -4.9076613   -1.9352798   -1.3335875
      C   -2.3500449   -0.5754970    0.0756697
      N   -3.3660526    0.0772627    0.6735620
      H   -3.3085727    0.8201166    1.4041665
      C   -4.4907166   -0.4318030    0.1363201
      H   -5.4902154   -0.1170220    0.4064538
      N   -4.2187491   -1.3840482   -0.7759280
      C   -2.8779889   -1.4836771   -0.8202360
      H   -2.3293638   -2.1655889   -1.4569339
      C   -0.4271237    1.0622789   -0.0051732
      C   -0.8883153   -0.3558429    0.3532960
      H   -0.6778182   -0.5663962    1.4234430
      H   -0.2980823   -1.0704793   -0.2605079
      N   -1.0842830    2.0665662    0.8255888
      H   -0.6455886    1.2632695   -1.0772303
      H   -0.7421259    3.0116763    0.5376181
      H   -0.8094259    1.9175321    1.8239106
      H    0.6740052    1.1315080    0.1435944
    $end
    
    $rem
    method            hf
    basis             sto-3g
    solvent_method    pcm
    pcm_print         1
    $end
    
    $pcm
    het-pcm
    theory     cpcm
    $end
    
    $atomic_epsilon
    1  78.4
    2  78.4
    3  78.4
    4  78.4
    5  78.4
    6  78.4
    7  78.4
    8  78.4
    9  78.4
    10 10.0
    11 10.0
    12 10.0
    13 10.0
    14 10.0
    15 10.0
    16 10.0
    17 10.0
    18 10.0
    $end
    ```

## 11.2.4.3 *$solvent* 输入段：静电作用选项

PCM 计算所用的溶剂通过 *$solvent* 输入段指定，如本节及下一节所述。注意，*$solvent* 输入段也用于指定 Kirkwood-Onsager SCRF 模型的参数（第 [11.2.2](example_SCRF.md) 节），并且 *$solvent* 输入段中可列出的具体选项取决于 *$rem* 输入段中 SOLVENT_METHOD 的取值。进行 PCM 计算的最低要求是：*$solvent* 输入段必须指定静态介电常数（$\varepsilon$）；对于非平衡激发态计算，还必须指定光频介电常数（$\varepsilon_{\text{opt}}\equiv\varepsilon_{\infty}$）。存在适用于水的默认值，但对于任何其他溶剂，这些常数都必须明确指定。这些常数既可以单独指定，即在 *$solvent* 输入段中使用变量 **Dielectric** 和 **OpticalDielectric**；也可以通过将 **SolventName** 设为表 [11.4](#table:PCM-solvents) 中所列的某种命名溶剂来采用其预定义值。

与同样使用命名溶剂（在 *$smx* 输入段中指定）的 SM$x$ 模型（第 [11.2.9](ex_SMx-User-Solvent.md) 节）不同，在 PCM 中使用 **SolventName** 仅用于指定这两个介电常数。非静电相互作用不会以自动方式被包含进来，但可以按第 [11.2.4.4](#subsubsec:PCM-solvent-NonElst) 节所述以临时（*ad hoc*）方式添加。表 [11.4](#table:PCM-solvents) 中列出的介电常数对应于 20${}^{\circ}$C 下的数值。对于水而言，这与 **Dielectric** 和 **OpticalDielectric** 的默认值略有不同，后者对应于 25${}^{\circ}$C。后两个值是完全可调的，而命名溶剂则仅限于表 [11.4](#table:PCM-solvents) 中所列的（$\varepsilon$、$\varepsilon_{\infty}$）数值对。

### `Dielectric`

> **指定 PCM 溶剂的静态介电常数。输入段：$solvent**
>
> * **类型**：`FLOAT`
> * **默认值**：`78.39`
> * **选项**：
>     * $\varepsilon$
>     * 使用某一介电常数
>     * $\varepsilon>0$
>     * .
> * **推荐**：静态（即零频率）介电常数就是通常所说的“介电常数”。默认值对应于 25 ${}^{\circ}$ C 下的水。

### `OpticalDielectric`

> **指定 PCM 溶剂的光频介电常数。输入段：$solvent**
>
> * **类型**：`FLOAT`
> * **默认值**：`1.78`
> * **选项**：
>     * $\varepsilon_{\infty}$
>     * 使用某一光频介电常数
>     * $\varepsilon_{\infty}>0$
>     * .
> * **推荐**：默认值对应于 25 ${}^{\circ}$ C 下的水。注意 $\varepsilon_{\infty}=n^{2}$ ，其中 $n$ 为溶剂的折射率。

### `SolventName`

> **通过命名溶剂来同时指定 PCM 计算的 $\varepsilon$ 和 $\varepsilon_{\infty}$。输入段：$solvent**
>
> * **类型**：`STRING`
> * **默认值**：`NONE`
> * **选项**：
>     * name
>     * 使用表 11.4 中溶剂 name 对应的
>     * $\varepsilon$
>     * 和
>     * $\varepsilon_{\infty}$
>     * 数值
>     * .
> * **推荐**：该选项与显式指定 Dielectric 或 OpticalDielectric 不兼容。

| SolventName | $\varepsilon$ | $\varepsilon_{\infty}$ | SolventName | $\varepsilon$ | $\varepsilon_{\infty}$ | SolventName | $\varepsilon$ | $\varepsilon_{\infty}$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| acetic_acid | 6.2 | 1.88 | dimethoxyethane | 7.3 | 1.90 | iodobenzene | 4.7 | 2.63 |
| acetone | 21.1 | 1.85 | 1-2-dimethoxyethane |  |  | isobutanol | 18.1 | 1.95 |
| acetonitrile | 36.6 | 1.81 | glyme |  |  | 2-methyl-1-propanol |  |  |
| acetylacetone | 26.5 | 2.11 | dimethylacetamide | 40.2 | 2.07 | isopropanol | 20.2 | 1.90 |
| pentane-2-4-dione |  |  | dimethylaminobenzene | 5.0 | 2.43 | 2-propanol |  |  |
| 2-4-pentanedione |  |  | n-n-dimethylaniline |  |  | mesitylene | 2.3 | 2.25 |
| aniline | 7.1 | 2.52 | dimethylformamide | 38.2 | 2.05 | 1-3-5-trimethylbenzene |  |  |
| benzenamine |  |  | N-N-dimethylformamide |  |  | methanol | 33.0 | 1.77 |
| anisole | 4.4 | 2.30 | dimethylsulfoxide | 47.2 | 2.18 | methyl_acetate | 6.8 | 1.85 |
| methoxybenzene |  |  | DMSO |  |  | acetic_acid_methyl_ester |  |  |
| benzaldehyde | 17.8 | 2.39 | dioxane | 2.2 | 2.02 | methyl_ethanoate |  |  |
| benzene | 2.3 | 2.25 | 1-4-dioxane |  |  | nitrobenzene | 35.6 | 2.41 |
| benzonitrile | 25.6 | 2.34 | ethanol | 25.3 | 1.85 | nonane | 2.0 | 1.98 |
| benzyl_alcohol | 13.7 | 2.38 | ethanolamine | 31.9 | 2.12 | n-nonane |  |  |
| phenyl_methanol |  |  | ethyl_acetate | 6.1 | 1.88 | octanol | 10.1 | 2.05 |
| bromobenzene | 5.5 | 2.43 | ethyl_ethanoate |  |  | 1-octanol |  |  |
| butanol | 18.1 | 1.96 | acetic_acid_ethyl_ester |  |  | p-xylene | 2.3 | 2.24 |
| 1-butanol |  |  | ethyl_acetoacetate | 14.0 | 2.02 | para-xylene |  |  |
| butanol | 17.1 | 1.95 | ethyl-3-oxobutanoate |  |  | 1-4-dimethylbenzene |  |  |
| 2-butanol |  |  | acetoacetic_acid_ethyl_ester |  |  | pentane | 1.8 | 1.84 |
| butanone | 18.6 | 1.90 | ethyl_benzoate | 6.2 | 2.27 | n-pentane |  |  |
| 2-butanone |  |  | benzoic_acid_ethyl_ester |  |  | 1-pentanol | 15.1 | 1.99 |
| butan-2-one |  |  | decane | 2.0 | 1.99 | 2-pentanol | 13.4 | 1.98 |
| methyl_ethyl_ketone |  |  | n-decane |  |  | 3-pentanol | 14.0 | 2.00 |
| carbon_tetrachloride | 2.2 | 2.13 | ethyl_formate | 8.7 | 1.85 | 2-pentanone | 15.4 | 1.94 |
| tetrachloromethane |  |  | ethyl_methanoate |  |  | pentan-2-one |  |  |
| chlorobenzene | 5.7 | 2.33 | formic_acid_methyl_ester |  |  | methyl_propyl_ketone |  |  |
| chloroform | 4.8 | 2.08 | ethylene_glycol | 42.8 | 2.05 | phenol | 13.4 | 2.37 |
| trichloromethane |  |  | 1-2-ethanediol |  |  | 1-propanol | 20.8 | 1.92 |
| cyclohexane | 2.0 | 2.03 | fluorobenzene | 5.5 | 2.23 | propanal | 17.4 | 1.86 |
| cyclohexanol | 16.4 | 2.15 | formamide | 111.8 | 2.10 | propionaldehyde |  |  |
| cyclohexanone | 16.1 | 2.11 | formic_acid | 51.1 | 1.88 | pyridine | 13.3 | 2.28 |
| 1-1-dichloroethane | 10.1 | 2.01 | heptane | 1.9 | 1.93 | t-butanol | 12.0 | 1.92 |
| 1-2-dichloroethane | 10.4 | 2.09 | n-heptane |  |  | tert-butanol |  |  |
| dichloromethane | 8.9 | 2.02 | heptanol | 11.9 | 2.03 | 2-methyl-2-propanol |  |  |
| methylene_chloride |  |  | 1-heptanol |  |  | tetrahydrofuran | 7.5 | 1.97 |
| diethylamine | 3.7 | 1.92 | hexane | 1.9 | 1.89 | THF |  |  |
| diethyl_ether | 4.3 | 1.83 | n-hexane |  |  | toluene | 2.4 | 2.24 |
| diethyl_ketone | 17.0 | 1.95 | hexanol | 13.6 | 2.01 | triethylamine | 2.4 | 1.96 |
| 3-pentanone |  |  | 1-hexanol |  |  | n-n-diethylethanamine |  |  |
| pentan-3-one |  |  |  |  |  | water | 80.2 | 1.78 |

表 11.4：
PCM 计算中可用的命名溶剂。（缩进的名称为同义词。）
$\varepsilon$ 的数值对应于 20${}^{\circ}$C 下的最新测量值（来自文献 

），
而 $\varepsilon_{\infty}=n^{2}$ 的数值对应于 20${}^{\circ}$C、$\lambda=589$ nm 条件下的最新测量值（来自文献 

）。
将 **SolventName** 设置为这些值之一仅指定了两个介电常数，并不包含任何非静电相互作用。

## 11.2.4.4 *$solvent* 部分：非静电选项

PCM 仅描述溶质的静电相互作用，其依据是静态介电常数（对于初始态），以及在非平衡激发或电离过程中可能用到的光介电常数。非静电相互作用项，例如描述空腔化（Pauli 排斥）和色散相互作用的项，[[569]](../bib_references/bib.md#bib580) 可以以*临时*（*ad hoc*）方式加入，但尚未针对 PCM 进行专门的参数化。（关于自动包含非静电项的溶剂化模型——这些项是获得绝对溶剂化能所必需的——请参见第 [11.2.9](ex_SMx-User-Solvent.md) 节中的 SM$x$ 模型，或第 [11.2.7](example_CMIRS-water.md) 节中的 CMIRS 方法。）

若要在 PCM 计算中加入非静电相互作用，请使用 *$solvent* 部分，其一般形式如下所示。

> ```qchem
> $solvent
>    NonEls  <Option>
>    NSolventAtoms <Number unique of solvent atoms>
>    SolventAtom <Number1> <Number2> <Number3> <SASradius>
>    SolventAtom <Number1> <Number2> <Number3> <SASradius>
>    . . .
>    <Keyword>  <parameter/option>
>    . . .
> $end
> ```

关键字 **SolventAtom** 需要多个参数，而其他所有关键字只需要一个参数，包括前面讨论过的 **Dielectric**、**OpticalDielectric** 和 **SolventName** 选项。关键字 **SolventAtom** 需要多个参数，而其他所有关键字只需要一个参数。介电常数对于任何 PCM 计算都是必需的（默认值代表水），而非静电参数是可选的，且很少被加入这些模型中。[[282]](../bib_references/bib.md#bib287)

**Q-Chem** 中目前可用的非静电相互作用基于 Cossi 等人的工作，[[274]](../bib_references/bib.md#bib272) 并且是在用于确定静电相互作用的 SCF 自洽场（SCF）过程之外计算的。非静电能量高度依赖于输入参数，并且对定义溶质空腔所选用的半径可能极其敏感。因此，纳入非静电相互作用具有很强的经验性，可能需要针对具体情况逐一考虑。依照文献 [[274]](../bib_references/bib.md#bib272)，空腔化能量使用与计算静电能量相同的溶质空腔来计算，而色散/排斥能量则使用溶剂可及表面（SAS）空腔定义来计算。

下列关键字（位于 *$solvent* 部分中）用于为 PCM 计算定义非静电参数。

### `NonEls`

> **指定要包含哪些类型的非静电贡献。输入部分：$solvent**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * Cav
>     * 空腔化能量
>     * Buck
>     * 由原子序数得到的 Buckingham 色散与排斥能量
>     * LJ
>     * 由力场得到的 Lennard-Jones 色散与排斥能量
>     * BuckCav
>     * Buck + Cav
>     * LJCav
>     * LJ + Cav
> * **建议**：目前 Buckingham 势的可用参数集非常有限。

### `NSolventAtoms`

> **不同类型原子的数目。输入部分：$solvent**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **选项**：
>     * $N$
>     * 指定存在
>     * $N$
>     * 种不同类型的原子。
> * **建议**：当 NonEls = Buck、LJ、BuckCav 或 LJCav 时，此关键字是必需的。例如，甲醇（ $\rm CH_{3}OH$ ）有三种类型的原子（C、H 和 O）。

### `SolventAtom`

> **指定一种唯一的溶剂原子。输入部分：$solvent**
>
> * **类型**：`Various`
> * **默认值**：`None.`
> * **选项**：
>     * 输入项 (TYPE)
>     * 描述
>     * Number1 (INTEGER)：
>     * 该原子的原子序数
>     * Number2 (INTEGER)：
>     * 一个溶剂分子中该原子的数目
>     * Number3 (INTEGER)：
>     * 力场原子类型
>     * SASradius (FLOAT)：
>     * 用于定义溶剂可及表面（SAS）的探针半径（单位为 Å）
> * **建议**：如果不使用 LJ 或 LJCav，则 Number3 应设为 0。当 NonEls = Buck、LJ、BuckCav 或 LJCav 时，此关键字是必需的。

### `Temperature`

> **指定溶剂温度。输入部分：$solvent**
>
> * **类型**：`FLOAT`
> * **默认值**：`300.0`
> * **选项**：
>     * $T$
>     * 使用温度
>     * $T$
>     * ，单位为开尔文（Kelvin）。
> * **建议**：仅用于空腔化能量。

### `Pressure`

> **指定溶剂压强。输入部分：$solvent**
>
> * **类型**：`FLOAT`
> * **默认值**：`1.0`
> * **选项**：
>     * $P$
>     * 使用压强为
>     * $P$
>     * ，单位为 bar。
> * **推荐**：仅用于空腔能（cavitation energy）的计算。

### `SolventRho`

> **指定溶剂的数密度。输入部分：$solvent**
>
> * **类型**：`FLOAT`
> * **默认值**：`Determined for water, based on temperature.`
> * **选项**：
>     * $\rho$
>     * 使用数密度为
>     * $\rho$
>     * ，单位为 分子/Å
>     * ${}^{3}$
>     * 。
> * **推荐**：仅用于空腔能（cavitation energy）的计算。

### `SolventRadius`

> **PCM 溶剂中溶剂分子的半径。输入部分：$solvent**
>
> * **类型**：`FLOAT`
> * **默认值**：`None`
> * **选项**：
>     * $r$
>     * 使用半径为
>     * $r$
>     * ，单位为 Å。
> * **推荐**：仅用于空腔能（cavitation energy）的计算。

下述示例展示了非静电相互作用的使用方法。

???+ example "示例 11.7：同时使用静电与非静电 PCM 相互作用，在水中优化三氟乙醇。在 Lennard-Jones 势中使用 OPLS-AA 参数描述色散与排斥作用。"
    ```qchem
    $molecule
       0 1
       C    -0.245826    -0.351674    -0.019873     23
       C     0.244003     0.376569     1.241371     22
       O     0.862012    -0.527016     2.143243     24
       F     0.776783    -0.909300    -0.666009     26
       F    -0.858739     0.511576    -0.827287     26
       F    -1.108290    -1.303001     0.339419     26
       H    -0.587975     0.878499     1.736246     27
       H     0.963047     1.147195     0.961639     27
       H     0.191283    -1.098089     2.489052     25
    $end
    
    $rem
       JOBTYPE        OPT
       BASIS          6-31G*
       METHOD         B3LYP
       SOLVENT_METHOD PCM
       FORCE_FIELD    OPLSAA
    $end
    
    $pcm
       Theory      CPCM
       Method      SWIG
       Solver      Inversion
       HeavyPoints 194
       HPoints     194
       Radii       Bondi
       vdwScale    1.2
    $end
    
    $solvent
       NonEls        LJCav
       NSolventAtoms 2
       SolventAtom   8 1 186 1.30
       SolventAtom   1 2 187 0.01
       SolventRadius 1.35
       Temperature   298.15
       Pressure      1.0
       SolventRho    0.03333
       Dielectric    78.39
    $end
    ```

## 11.2.4.5 非平衡溶剂化的作业控制与示例

在进行非平衡计算时，需要在 *$solvent* 部分中使用 **OpticalDielectric** 关键字，或者可以通过指定 **SolventName** 将其设置为预定义值。只要在 CIS/TDDFT 计算中配合 PCM 使用，LR-PCM 激发能就会自动计算，但在采用微扰方案时该功能会被关闭。

### `ChargeSeparation`

> **在溶剂平衡状态下划分快电荷与慢电荷。输入部分：$pcm**
>
> * **类型**：`STRING`
> * **默认值**：`No default.`
> * **选项**：
>     * Marcus
>     * 采用 Marcus 划分方式进行快慢电荷分离。
>     * Pekar
>     * 采用 Pekar 划分方式进行快慢电荷分离。
> * **推荐**：电荷分离需与 $pcm 中的 StateSpecific 关键字配合使用。

### `StateSpecific`

> **指定使用何种状态特定的 PCM。输入部分：$pcm**
>
> * **类型**：`Various`
> * **默认值**：`No default.`
> * **选项**：
>     * Perturb
>     * 对垂直激发执行 ptSS 和 ptLR 计算。
>     * External
>     * 对激发态执行自洽 EI-SS-PCM 计算（用于发射）。
>     * Internal
>     * 对激发态执行自洽 II-SS-PCM 计算（用于发射或激发）。
> * **推荐**：对于垂直激发能使用 ptSS-PCM；在强极性情形下使用非平衡 II-SS-PCM；对于长寿命激发态的发射能，使用平衡 EI-SS-PCM。

### `Td_CEq_NonEq`

> **基于非平衡溶剂化的约束平衡原理，指定自洽 SS-PCM/TDDFT 方法，以计算溶剂对溶液中垂直吸收与发射的影响。输入部分：$pcm**
>
> * **类型**：`INTEGER`
> * **默认值**：`NONE`
> * **选项**：
>     * 1
>     * 在基态几何下通过 RPA 计算，基于平衡基态反应场计算吸收过程中的非平衡激发态自由能。
>     * 2
>     * 在基态几何下通过 RPA 计算，基于非平衡激发态反应场计算吸收过程中的非平衡激发态自由能。
>     * 3
>     * 在激发态几何下通过 RPA 计算，基于平衡激发态反应场计算发射过程中的平衡激发态自由能。
>     * 4
>     * 在激发态几何下通过纯单点能计算，基于非平衡基态反应场计算发射过程中的非平衡基态自由能。
> * **推荐**：选项 2 和 3 需要迭代直至激发态反应场收敛。选项 1 是选项 2 的首次迭代。当选项 3 的平衡激发态反应场收敛后，执行选项 4。

???+ example "示例 11.8：LR-TDDFT/LR-C-PCM 低能垂直激发能"
    ```qchem
    $molecule
       0 1
       C    0  0  0.0
       O    0  0  1.21
    $end
    
    $rem
       EXCHANGE            B3LYP
       CIS_N_ROOTS         10
       CIS_SINGLETS        TRUE
       CIS_TRIPLETS        TRUE
       RPA                 TRUE
       BASIS               6-31+G*
       SOLVENT_METHOD      PCM
    $end
    
    $pcm
       Theory      CPCM
       Method      SWIG
       Solver      Inversion
       Radii       Bondi
    $end
    
    $solvent
       Dielectric         78.39
       OpticalDielectric  1.777849
    $end
    ```

???+ example "示例 11.9：使用 ptSS 和 ptLR 方法计算平面形 DMABN 垂直激发能的 PCM 溶剂化效应。"
    ```qchem
    $molecule
       0  1
       C     0.000046   -0.000398    1.904953
       C     1.210027    0.000379    1.186051
       C     1.214640   -0.000065   -0.194515
       C     0.000164   -0.000616   -0.933832
       C    -1.214349   -0.001557   -0.194687
       C    -1.209753   -0.001846    1.185775
       H     2.151949    0.001377    1.722018
       H     2.164371    0.000481   -0.709640
       H    -2.164082   -0.002008   -0.709781
       H    -2.151763   -0.002287    1.721615
       C    -0.000227    0.001061    3.325302
       N    -0.000475    0.002405    4.484321
       N     0.000053   -0.000156   -2.297372
       C    -1.258656    0.001284   -3.036994
       H    -1.041042    0.001615   -4.102376
       H    -1.860897   -0.885647   -2.811117
       H    -1.859247    0.889133   -2.810237
       C     1.258563   -0.000660   -3.037285
       H     1.860651    0.886208   -2.810755
       H     1.859362   -0.888604   -2.811461
       H     1.040664   -0.000097   -4.102609
    $end
    
    $rem
       EXCHANGE              LRC-wPBEPBE
       OMEGA                 260
       BASIS                 6-31G*
       CIS_N_ROOTS           10
       RPA                   2
       CIS_SINGLETS          1
       CIS_TRIPLETS          0
       CIS_RELAXED_DENSITY   TRUE
       SOLVENT_METHOD        PCM
    $end
    
    $pcm
       NonEquilibrium
       Theory                 IEFPCM
       StateSpecific          Perturb
    $end
    
    $solvent
       Dielectric             35.688000       ! Acetonitrile
       OpticalDielectric      1.806874
    $end
    ```

???+ example "示例 11.11.10：使用外迭代 SS-PCM 的 TDDFT 计算硝酸根离子在乙腈中的性质。"
    ```qchem
    $molecule
       -1 1
       N    -0.068642000000     -0.600693000000     -0.723424000000
       O     0.349666000000      0.711166000000      1.187490000000
       O    -0.948593000000      0.200668000000     -0.956940000000
       O     0.659040000000     -0.386002000000      0.402650000000
    $end
    
    $rem
       jobtype    ¯¯         sp
       method ¯¯             PBE0
       basis  ¯¯¯           3-21g
    point_group_symmetry False
       cis_n_roots             2           ! Number of excited states
       cis_singlets            true
       cis_triplets            false
       rpa                     false       ! Tamm-Dancoff approximation
       cis_moments             true        ! Excited state multipole moments
       cis_relaxed_density     true        ! Excited state density relaxation
       solvent_method        ¯ pcm
    $end
    
    $pcm
       StateSpecific           External    ! Keyword for External Iteration SS-PCM
       LinearResponse          false       ! Switch of LR-PCM
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       jobtype ¯¯             sp
       method ¯¯             PBE0
       basis ¯¯¯             3-21g
    point_group_symmetry False
       cis_n_roots             2
       cis_singlets            true
       cis_triplets            false
       rpa                     false
       cis_moments             true
       cis_relaxed_density     true
       solvent_method          pcm
    $end
    
    $pcm
       StateSpecific           External
       Eqsolv                  15          ! Max. Number of iterations
       Eqstate                 1           ! Ref. State to be equilibrated
       Eqs_Conv                4           ! Conv. criterion for SCF energy and surface charges
       EqState_Follow          true        ! State Following to remain on the same Ref. State
       LinearResponse          false
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    ```

???+ example "示例 11.11.11：使用内迭代 SS-PCM 的 TDDFT 以及额外的基态计算，计算硝酸根离子在乙腈中的垂直发射能。"
    ```qchem
    $molecule
       -1 1
       N    -0.068642000000     -0.600693000000     -0.723424000000
       O     0.349666000000      0.711166000000      1.187490000000
       O    -0.948593000000      0.200668000000     -0.956940000000
       O     0.659040000000     -0.386002000000      0.402650000000
    $end
    
    $rem
       jobtype ¯¯             sp
       method ¯¯             PBE0
       basis ¯¯¯             3-21g
    point_group_symmetry False
       cis_n_roots             4           ! Number of excited states
       cis_singlets            true
       cis_triplets            false
       rpa                     false       ! Tamm-Dancoff approximation
       cis_moments             true        ! Excited state multipole moments
       cis_relaxed_density     true        ! Excited state density relaxation
       solvent_method          pcm
    $end
    
    $pcm
       StateSpecific           Internal    ! Keyword for Internal Iteration SS-PCM
       ChargeSeparation        MARCUS      ! Keyword for the charge separation
       InternalIteration       AEM(f)      ! Procedure (VEM(f), VEM(d), AEM(f), or AEM(d)) + state sequence (add e.g.: -state 1 3 1 0)
       Eqsolv                  10          ! Max. Number of iterations
       Eqstate                 1           ! Ref. State to be equilibrated
       Eqs_Conv                4           ! Conv. criterion for SCF energy and surface charges
       EqState_Follow          true        ! State Following to remain on the same Ref. State
       theory                  iefpcm      ! PCM Theory (else CPCM)
       rf_ptss_save            true        ! Save the eq. reaction field of Ref. State
       LinearResponse          false       ! Switch of LR-PCM
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       jobtype                 sp
       method ¯¯             PBE0
       basis                   3-21g
    point_group_symmetry False
       solvent_method          pcm
    $end
    
    $pcm
       theory                  iefpcm
       rf_ptss_read            true        ! Flag to read the reaction field and do RF-ptSS calc
    $end
    
    $solvent
       Dielectric              35.68800    ! Acetonitrile
       OpticalDielectric       1.806874
    $end
    
    
    ```

???+ example "示例 11.11.12：基于约束平衡原理的 SS-PCM/TDDFT 低能垂直激发能计算。"
    ```qchem
    $molecule
      0 1
      C     0.00000000    0.00000000    0.00000000
      O     0.00000000    0.00000000    1.22027000
      C     1.28132052    0.00000000   -0.79367740
      H     2.14499626   -0.00083829   -0.12870724
      H     1.30455453   -0.88067608   -1.44302080
      H     1.30547296    0.88142003   -1.44198042
      C    -1.28127663    0.00458022   -0.79382239
      H    -2.14504139    0.00537545   -0.12895306
      H    -1.30703468   -0.87518579   -1.44430491
      H    -1.30295394    0.88686493   -1.44106115
    $end
    
    $rem
       METHOD              M062X
       BASIS               6-31+G*
       JOB_TYPE            sp
       RPA                 2
       DFT_D               D3
       cis_singlets        TRUE
       cis_triplets        FALSE
       cis_n_roots         5
       cis_state_deriv     1
       CIS_DYNAMIC_MEM     TRUE
       CIS_RELAXED_DENSITY TRUE
       CIS_MOMENTS         TRUE
       SOLVENT_METHOD      PCM
    $end
    
    $pcm
       Theory              SSVPE
       ChargeSeparation    Pekar
       StateSpecific       Perturb
       Td_CEq_NonEq        1
    $end
    
    $solvent
       Dielectric          32.613
       OpticalDielectric   1.766
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
       METHOD              M062X
       BASIS               6-31+G*
       JOB_TYPE            sp
       RPA                 2
       DFT_D               D3
       cis_singlets        TRUE
       cis_triplets        FALSE
       cis_n_roots         5
       cis_state_deriv     1
       CIS_DYNAMIC_MEM     TRUE
       CIS_RELAXED_DENSITY TRUE
       CIS_MOMENTS         TRUE
       SOLVENT_METHOD      PCM
    $end
    
    $pcm
       Theory              SSVPE
       ChargeSeparation    Pekar
       StateSpecific       Perturb
       Td_CEq_NonEq       2
    $end
    
    $solvent
       Dielectric          32.613
       OpticalDielectric   1.766
    $end
    ```

???+ example "示例 11.11.13：基于约束平衡原理的 SS-PCM/TDDFT 发射过程平衡激发态自由能计算。"
    ```qchem
    $molecule
      0 1
      C    0.00000000   -0.57624800    0.00000000
      H   -0.95773500   -1.10813200    0.00000000
      H    0.95773500   -1.10813200    0.00000000
      O    0.00000000    0.70921900    0.00000000
    $end
    
    $rem
      METHOD               M062X
      BASIS                6-31+G*
      CIS_N_ROOTS          5
      RPA                  2
      CIS_SINGLETS         1
      CIS_TRIPLETS         0
      CIS_DYNAMIC_MEM      TRUE
      CIS_RELAXED_DENSITY  TRUE
      SOLVENT_METHOD       PCM
      POP_MULLIKEN         -1
      CIS_MOMENTS          TRUE
      DFT_D                D3
      CIS_CONVERGENCE      5
      MAX_CIS_CYCLES       150
    $end
    
    $pcm
      Theory               SSVPE
      Method               SWIG
      ChargeSeparation     EXCITED
      StateSpecific        1
      Td_CEq_NonEq         3
    $end
    
    $solvent
      Dielectric           78.5
      OpticalDielectric    1.778
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
      METHOD                M062X
      BASIS                 6-31+G*
      SOLVENT_METHOD        PCM
      POP_MULLIKEN          -1
      DFT_D                 D3
      SCF_CONVERGENCE       8
    $end
    
    $pcm
      Theory                SSVPE
      Method                SWIG
      ChargeSeparation      Pekar
      StateSpecific         Pekar
      Td_CEq_NonEq          4
    $end
    
    $solvent
      Dielectric            78.5
      OpticalDielectric     1.778
    $end
    ```

???+ example "示例 11.14：基于约束平衡原理的 SS-PCM/TDDFT 发射过程非平衡基态自由能计算。"
    ```qchem
    $molecule
       0 1
       C    0.00000000   -0.57624800    0.00000000
       H   -0.95773500   -1.10813200    0.00000000
       H    0.95773500   -1.10813200    0.00000000
       O    0.00000000    0.70921900    0.00000000
    $end
    
    $rem
       METHOD           M062X
       BASIS            6-31+G(d)
       SOLVENT_METHOD   PCM
       POP_MULLIKEN     -1
       DFT_D            D3
    $end
    
    $pcm
       Theory            SSVPE
       Method            SWIG
       ChargeSeparation  Pekar
       StateSpecific     Pekar
       Td_CEq_NonEq      4
    $end
    
    $solvent
       Dielectric 78.5
       OpticalDielectric 1.778
    $end
    ```
