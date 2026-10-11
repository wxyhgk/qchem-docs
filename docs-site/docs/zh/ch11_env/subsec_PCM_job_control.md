---
title: "11.2.4 PCM 任务控制"
---

## 11.2.4 PCM 任务控制

（2026 年 7 月 4 日）

通过在 *$rem* 区段中设置 SOLVENT_METHOD = PCM 即可请求进行 PCM 计算。如前所述，PCM 家族中包含多种不同的理论模型，因此可能需要进行额外的精细调整，具体说明如下。

## 11.2.4.1 *$pcm* 区段

大多数 PCM 任务控制是通过在 *$pcm* 输入区段中指定的选项来完成的，该区段允许用户指定所使用的 PCM 变体、求解 PCM 方程所用的算法以及其他选项。*$pcm* 区段的格式与 *$rem* 区段类似：

> ```qchem
> $pcm
>    <Keyword>  <parameter/option>
> $end
> ```

**注意：

以下任务控制变量*仅*属于 *$pcm* 区段。
请勿将其放置在 *$rem* 区段中。
**

### `Theory`

> **指定所使用的极化连续介质模型。输入区段：$pcm**
>
> * **类型**：`STRING`
> * **默认值**：`CPCM`
> * **可选值**：
>     * CPCM
>     * 类导体 PCM（Conductor-like PCM），见参考文献
>     * 275
>     * Cossi M. et al.
>     * J. Comput. Chem.
>     * (2003)
>     * ,
>     * 24
>     * ,
>     * pp. 669
>     * .
>     * 链接
>     * ，其中
>     * $f_{\varepsilon}=(\varepsilon-1)/\varepsilon$
>     * 。
>     * CPCM1
>     * 与 CPCM 等价。
>     * CPCM2
>     * 原始类导体屏蔽模型（conductor-like screening model），见参考文献
>     * ，其中
>     * $f_{\varepsilon}=(\varepsilon-1)/(\varepsilon+1/2)$
>     * 。
>     * IEFPCM
>     * 采用非对称 $\mathbf{K}$ 矩阵的 IEF-PCM。
>     * SSVPE
>     * SS(V)PE 模型，等价于采用对称 $\mathbf{K}$ 矩阵的 IEF-PCM。
> * **建议**：IEF-PCM/SS(V)PE 模型是比 C-PCM 更复杂的模型，对于低介电常数溶剂在形式上更为适用，但同时也更难使用。实践中，这些模型之间的差异往往很小；参见参考文献 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . 链接 。关于 C-PCM 的两个版本以及式 ( 11.3 ) 中 $f_{\varepsilon}$ 的选择，文献建议对于中性溶质取 $x=0$，对于离子取 $x=1/2$；同样可参见参考文献 569 Herbert J. M. Wiley Interdiscip. Rev.: Comput. Mol. Sci. (2021) , 11 , pp. e1519 . 链接 中对这些差异的讨论。

### `Method`

> **指定所使用的表面离散化方法。输入区段：$pcm**
>
> * **类型**：`STRING`
> * **默认值**：`SwiG`
> * **可选值**：
>     * SwiG
>     * 切换函数/高斯方法（Switching/Gaussian method）
>     * ISwiG
>     * 采用另一种切换函数的"改进型"（"Improved"）切换函数/高斯方法
>     * Spherical
>     * 对空腔表面使用单个固定球面。
>     * Fixed
>     * 使用离散点电荷代替平滑高斯函数。
> * **建议**：推荐仅使用 SwiG 的原因是它比 ISwiG 的切换函数略微高效。另一方面，ISwiG 提供了一些在概念上更具吸引力的特性，且在某些情况下可能更优。关于这些差异的讨论，请参考文献 754 Lange A. W., Herbert J. M. J. Chem. Phys. (2010) , 133 , pp. 244111 . 链接 、756 Lange A. W., Herbert J. M. Chem. Phys. Lett. (2011) , 509 , pp. 77 . 链接 。Fixed 选项使用 Li 和 Jensen 提出的可变面元数（Variable Tesserae Number, VTN）算法，812 Li H., Jensen J. H. J. Comput. Chem. (2004) , 25 , pp. 1449 . 链接 并结合 Lebedev 网格点。VTN 使用点电荷，不含切换函数或高斯模糊，因此容易受到不连续性的影响，可能导致解析梯度出错，并使几何优化收敛缓慢。753 Lange A. W., Herbert J. M. J. Phys. Chem. Lett. (2010) , 1 , pp. 556 . 链接 除非是为了与文献中的其他计算结果进行对接，否则不推荐使用该选项。

### `Solver`

> **指定求解 PCM 方程所使用的算法。输入区段：$pcm**
>
> * **类型**：`STRING`
> * **默认值**：`INVERSION`
> * **可选值**：
>     * INVERSION
>     * 直接矩阵求逆
>     * CG
>     * 迭代共轭梯度法（conjugate gradient）
> * **建议**：对于小溶质，矩阵求逆更快，因为在单点能计算中只需执行一次。然而，当离散化点数接近或超过 $\sim$ 10,000 时，推荐使用 CG 求解器（该求解器必须在每次自洽场（SCF）迭代中应用）。关于大规模 MM/PCM 和 QM/MM/PCM 计算的线性标度算法，将在第 11.2.5 节 中讨论。

### `SwitchThresh`

> **丢弃空腔表面网格点的阈值。INPUT SECTION: $pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `8`
> * **选项**:
>     * $n$
>     * 当开关函数（switching function）小于
>     * $10^{-n}$
>     * 时丢弃网格点
>     * 。
> * **建议**: 使用默认值，经验证该值可在机器精度范围内避免不连续性。增大 $n$ 会降低 PCM 计算的成本，但可能在势能面中引入不连续性。如果 PCM 部分的计算开销过大，更好的做法是减少离散化点的数量（ HeavyPoints 和 HPoints ，见下文介绍），或使用 Solver = CG ，而不是调整  。

溶质空腔的构建是该模型的重要组成部分，用户应当参阅相关文献，尤其是关于原子球所采用半径的内容。**Q-Chem** 提供的默认值对应于数十年来形成的共识选择，即使用范德华（vdW）半径 $\{R_{\text{vdW},A}\}$ 并乘以缩放因子 $\alpha_{\text{vdW}}=1.2$；参见公式 ([11.4](topic_pcm-em.md#eq:PCM_atomic_radii))。应用最广泛的 vdW 半径集合是 Bondi 依据晶体学数据确定的[[146]](../bib_references/bib.md#bib136)，
 尽管氢的半径后来被调整为
1.1 Å[[1186]](../bib_references/bib.md#bib1240)，
 并且 Bondi 未涵盖的主族元素半径也在后续工作中得到补充[[889]](../bib_references/bib.md#bib923)。
 **Q-Chem** 默认使用这一扩展的 vdW 半径集合，为简便起见，无论其来源于 Bondi 的原始论文还是后续工作，我们一律称之为“Bondi 半径”。另外，也可选用通用力场（Universal Force Field, UFF）的原子半径[[1146]](../bib_references/bib.md#bib1198)。
 UFF 半径的主要吸引力在于其对元素周期表中的所有原子都有定义，不过这些半径用于 PCM 应用时的质量尚不明确。

### `Radii`

> **指定用于定义溶质空腔的原子范德华半径集合。INPUT SECTION: $pcm**
>
> * **类型**: `STRING`
> * **默认值**: `Bondi`
> * **选项**:
>     * Bondi
>     * 使用（扩展的）Bondi 半径集合（参考文献
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
>     * 使用来自分子力学（MM）力场的 Lennard-Jones 半径。
>     * UFF
>     * 使用通用力场（UFF）的半径（参考文献
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
>     * 输入段中读取原子半径。
> * **建议**: Bondi 半径的应用十分广泛。FF 选项要求用户通过 $rem 段中的 FORCE_FIELD 变量指定一个 MM 力场，并在 $molecule 段中定义原子类型（见第 11.3 节 ）。UFF 半径则不需要这些操作。若需使用用户自定义半径，有关 $van_der_waals 输入段的格式请参见第 11.2.10 节 。

从 **Radii** 关键字的说明中可以看出，
用户可以使用 *$van_der_waals* 输入段为空的构建自行指定半径。
若要为给定分子指定全部半径，请采用第 [11.2.10](subsec_LD.md) 节中所述的 *$van_der_waals* 段格式。
或者，如果只需补充某个半径集合中缺失的半径（例如 Bondi 集合并未覆盖整个元素周期表），则无需设置 **Radii** = **Read**。
只需保持
**Radii** = **Bondi**（或其他选择），同时包含一个格式如下的 *$van_der_waals* 段即可

> ```qchem
> $van_der_waals
> atomic_number   vdW_radius
> $end
> ```

用户自定义的半径不会应用任何缩放因子。
需要注意的是，某个原子的半径允许取 $R=0$，
此时该原子不参与空腔表面的构建。
这一特性便于构建“ united atom（统一原子）”
空腔[[78]](../bib_references/bib.md#bib60)，
 即氢原子不单独占据球体，而是增大重原子半径以作补偿。
作为对 vdW 半径 $\{R_{\text{vdW},A}\}$ 进行缩放的替代方案，
用户也可以选择给每个半径加上一个探针半径 $R_{\text{probe}}$
[参见公式 ([11.4](topic_pcm-em.md#eq:PCM_atomic_radii))]，以获得 SAS 空腔。

从历史上看，空腔表面的离散化采用的是“镶嵌（tessellation）”方法，
即将空腔表面积划分为有限的多边形“镶嵌块（tesserae）”。（GEPOL 算法[[1044]](../bib_references/bib.md#bib1089)
 或许是应用最广泛的镶嵌方案。）然而，镶嵌方法不仅存在空腔表面积和溶剂化能
随核坐标变化而产生的不连续性问题，而且其导出的解析能量梯度
也复杂难推、难以实现。
为避免这些问题，**Q-Chem** 的 SwiG-PCM
实现[[753]](../bib_references/bib.md#bib786)
 使用 Lebedev 网格对原子球进行离散化。
这些是以原子为中心、具有二十面体对称性的网格，每个原子球的网格点数
可在 26 到 5294 之间选取。**Q-Chem** 所用的默认值
基于大量数值测试选定[[754]](../bib_references/bib.md#bib787)，
并且对于 MM 原子（在 MM/PCM 或 QM/MM/PCM 计算中）所用的网格比 QM 原子更稀疏（点数更少），
这是因为与 MM 点电荷相比，QM 密度产生的静电势更为复杂。对于 QM 原子，
默认对氢原子使用 $N=110$ 个点，对其余所有原子使用 $N=194$ 个点；
而对于 MM 原子，默认对氢原子使用 $N=50$、对非氢原子使用 $N=110$。这些默认值
表现出良好的旋转不变性（分子旋转时
$\Delta G$ 的差异 $<0.1$ kcal/mol[[754]](../bib_references/bib.md#bib787)
），且绝对溶剂化能通常位于 $N\rightarrow\infty$
极限的 $<1$ kcal/mol 范围之内[[754]](../bib_references/bib.md#bib787)，
至少对电中性溶质而言是如此。

请注意，早期版本的 **Q-Chem** 默认使用更密集的网格。（在
**Q-Chem** v. 4.2 及更早版本中，所有 QM 原子的默认值为 $N=590$，自 v. 4.2.1 起改为 $N=302$。上述默认值是从 v. 5.2 开始的当前默认值。）然而，$\sim$0.5 kcal/mol 量级的网格误差完全在这些模型 $\Delta G_{\textrm{solvation}}$ 的固有精度范围之内。激发能溶剂致变色位移中的
网格误差通常为 $\sim$0.01–0.02 eV，这远低于几乎所有激发态方法的固有精度。如果
对网格精度存有疑问，我们建议将 $N=302$ 作为高质量选项，将 $N=590$ 作为基本收敛的选项[[754]](../bib_references/bib.md#bib787)。

对于大分子，可能有必要减少网格点数
（*e.g.*，减至 $N=86$），或采用线性标度求解器代替矩阵求逆，
详见第 [11.2.5](subsec_linear-PCM.md) 节。

**注意：**

每个球允许的 Lebedev 点数为
$N=6$、26、38、50、86、110、146、170、194、302、350、434、590、770、974、1202、
1454、1730、2030、2354、2702、3074、3470、3890、4334、4802、5294。

### `HeavyPoints`

> **放置在 QM 系统中非氢原子上的 Lebedev 网格点数目。输入节：$pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `194`
> * **选项**:
>     * 可接受的取值见上文列表。
> * **建议**: 几何优化时使用默认值。对于绝对溶剂化能，用户可能希望考察结果关于 $N$ 的收敛性。

### `HPoints`

> **放置在 QM 系统中氢原子上的 Lebedev 网格点数目。输入节：$pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `110`
> * **选项**:
>     * 可接受的取值见上文列表。
> * **建议**: 几何优化时使用默认值。对于绝对溶剂化能，用户可能希望考察结果关于 $N$ 的收敛性。

### `MMHeavyPoints`

> **放置在 MM 子系统中非氢原子上的 Lebedev 网格点数目。输入节：$pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `110`
> * **选项**:
>     * 可接受的取值见上文列表。
> * **建议**: 几何优化时使用默认值。对于绝对溶剂化能，用户可能希望考察结果关于 $N$ 的收敛性。此选项仅适用于 MM/PCM 或 QM/MM/PCM 计算。

### `MMHPoints`

> **放置在 MM 子系统中氢原子上的 Lebedev 网格点数目。输入节：$pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `50`
> * **选项**:
>     * 可接受的取值见上文列表。
> * **建议**: 几何优化时使用默认值。对于绝对溶剂化能，用户可能希望考察结果关于 $N$ 的收敛性。此选项仅适用于 MM/PCM 或 QM/MM/PCM 计算。

尤其是对于复杂的分子，用户可能希望可视化空腔表面。这可以通过设置 **PrintLevel** $\geq 2$ 来实现，
该设置将触发若干描述空腔表面的 `.PQR` 文件的生成。（这些文件会写入 **Q-Chem** 输出文件中。）
`.PQR` 格式类似于常见的 `.PDB`（蛋白质数据库，Protein Data Bank）格式，
但 additionally 还为每个原子包含电荷与半径信息。其中一个输出的 `.PQR`
文件包含在 PCM 计算中求得的电荷，以及半径（单位为 Å），其值等于每个表面网格点所代表表面积一半的平方根。
因此，在检查这种表面表示形式时，较大的离散点对应较大的表面积。第二个 `.PQR`
文件以溶质的静电势（以原子单位计）代替电荷信息，并对网格点使用统一的半径。这些 `.PQR`
文件可以使用多种第三方软件进行可视化，包括免费提供的可视化分子动力学（Visual Molecular Dynamics, VMD）程序，[[W. Humphrey, A. Dalke, and K. Schulten (1996)]](../bib_references/bib.md#bib627)
该程序尤其适合根据电荷对 `.PQR` 表面网格点进行着色，并根据其对分子表面积的贡献来调整其大小。（此类可视化的示例可见参考文献 [[753]](../bib_references/bib.md#bib786) 。）

### `PrintLevel`

> **控制 PCM 计算过程中的输出详细程度。输入节：$pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 输出 PCM 能量和基本表面网格信息。附加输出最少。
>     * 1
>     * 在级别 0 基础上增加 PCM 溶质-溶剂相互作用能分量及高斯定律（Gauss' Law）误差。
>     * 2
>     * 在级别 1 基础上增加表面网格切换参数，以及用于
>     * 可视化空腔表面表观电荷（apparent surface charges）的
>     * .PQR
>     * 文件。
>     * 3
>     * 在级别 2 基础上增加用于可视化收敛后溶质在表面网格处所产生静电势的
>     * .PQR
>     * 文件。
>     * 4
>     * 在级别 3 基础上增加更多表面网格信息，以及每个 SCF 循环中的静电势与表观电荷。
>     * 5
>     * 在级别 4 基础上增加大量调试信息。
> * **建议**: 除非需要更多信息，否则使用默认值。

最后请注意，在 *$pcm* 输入节中将 **Method** 设置为 **Spherical**，会请求构造一个由单个固定球体组成的溶质空腔。
这通常不被推荐，但对于与文献中 Born 模型的结果建立联系，或与[第 11.2.2 节](example_SCRF.md)中讨论的 Kirkwood-Onsager 模型建立联系，偶尔会有用处。
在这种情况下，还必须在 *$pcm* 节中指定空腔半径及其中心。关键字 **HeavyPoints** 用于控制对表面进行离散化时所使用的 Lebedev 网格点数目。

### `CavityRadius`

> **指定溶质空腔半径。输入节：$pcm**
>
> * **类型**：`FLOAT`
> * **默认值**：`None`
> * **选项**：
>     * $R$
>     * 使用半径
>     * $R$
>     * ，单位为埃（Ångstroms）。
> * **建议**：无。

### `CavityCenter`

> **指定球形溶质空腔的中心。输入节：$pcm**
>
> * **类型**：`FLOAT`
> * **默认值**：`0.0 0.0 0.0`
> * **选项**：
>     * $x$
>     * $y$
>     * $z$
>     * 空腔中心的坐标，单位为埃（Ångstroms）。
> * **建议**：格式后跟三个以空格分隔的浮点数值。使用与 $molecule 节相同的坐标系。

最后，HetPCM 方法（第 [11.2.3.5](topic_pcm-em.md#sec:HetPCM) 节）通过在 *$pcm* 节中出现关键字
**Het-PCM** 来激活。此类计算需要一个 *$atomic_epsilon* 输入节，用于指定
每个原子球所采用的 $\varepsilon$ 值。其格式就是一个原子编号列表，
每个编号对应一个双精度的 $\varepsilon$ 值：

> ```qchem
> $atomic_epsilon
> 1   epsilon_1
> 2   epsilon_2
> 3   epsilon_3
> ...
> $end
> ```

原子可以从该列表中省略，其 $\varepsilon$ 将被赋值为 $1$。

### `Het-PCM`

> **若存在，则激活非均相 PCM（heterogeneous PCM）。输入节：$pcm**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * 若该关键字存在，则开启 HetPCM
> * **建议**：需要一个 $atomic_epsilon 节来为每个原子提供用户指定的介电常数。可在 $rem 中设置 PCM_PRINT $\geq 1$，以确认原子级的 $\varepsilon$ 值正在被使用。

## 11.2.4.2 示例

???+ example "示例 11.3: 使用 PCM 的一个基本示例：在水中对三氟乙醇进行结构优化。
溶剂介电常数在 $solvent 节中指定，该节将在下文描述。"
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

???+ example "示例 11.4: 在乙腈中对 H ${}_{2}$ O 使用具有单个球形空腔的 PCM。
与 Kirkwood-Onsager 多极展开方法相比，参见第 11.2.2 页的示例 11.2.2。"
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

最后，我们考虑一个 united-atom（ united-atom，合并原子）空腔的示例。请注意，
用户仅对碳定义了自定义的范德华（vdW）半径，因此氢半径被取为零，
从而氢原子不参与空腔表面的构建。（如上所述，*$van_der_waals*
输入节的格式在第 [11.2.10](subsec_LD.md) 节中讨论。）

???+ example "示例 11.5: 乙烯的 united-atom 空腔构建。"
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

???+ example "示例 11.6: 非均相 PCM（HetPCM）示例，由 $pcm 节中的 Het-PCM 标志触发。
这是一个质子化组氨酸的截断模型，其中带正电的芳香部分暴露于 $\varepsilon=78.4$ 的环境中，
而侧链中原子的 $\varepsilon=10.0$。"
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

## 11.2.4.3 *$solvent* 部分：静电学选项

用于 PCM（极化连续介质模型）计算的溶剂通过 *$solvent* 部分进行指定，具体说明见本小节及下一小节。请注意，*$solvent* 部分也用于指定 Kirkwood-Onsager SCRF（自洽反应场）模型（第 [11.2.2](example_SCRF.md) 节）的参数，而 *$solvent* 部分中可以列出的具体选项取决于 *$rem* 部分中 SOLVENT_METHOD 的取值。进行 PCM 计算的最低要求是：*$solvent* 部分必须指定静态介电常数（$\varepsilon$），并且对于非平衡激发态计算，还必须指定光学介电常数（$\varepsilon_{\text{opt}}\equiv\varepsilon_{\infty}$）。存在一组适用于水的默认值，但对于任何其他溶剂，这些常数都必须显式指定。这些常数既可以使用 *$solvent* 部分中的变量 **Dielectric** 和 **OpticalDielectric** 逐一指定，也可以通过将 **SolventName** 设置为表 [11.4](#table:PCM-solvents) 中给出的某个命名溶剂，从而采用其预定义的值。

与 SM$x$ 模型（第 [11.2.9](ex_SMx-User-Solvent.md) 节）不同——后者同样使用命名溶剂（在 *$smx* 部分中指定）——在 PCM 中使用 **SolventName** 仅用于指定两个介电常数。非静电相互作用不会被自动纳入，尽管可以按第 [11.2.4.4](#subsubsec:PCM-solvent-NonElst) 节所述以特设（*ad hoc*）方式添加。表 [11.4](#table:PCM-solvents) 中列出的介电常数对应 20${}^{\circ}$C 下的数值。对于水，这与 **Dielectric** 和 **OpticalDielectric** 的默认值略有不同，后者对应 25${}^{\circ}$C。后两个值可以完全自由调节，而命名溶剂则仅限于表 [11.4](#table:PCM-solvents) 中列出的 ($\varepsilon$, $\varepsilon_{\infty}$) 数值对。

### `Dielectric`

> **为 PCM 溶剂指定静态介电常数。输入部分：$solvent**
>
> * **类型**: `FLOAT`
> * **默认值**: `78.39`
> * **选项**:
>     * $\varepsilon$
>     * 使用的介电常数
>     * $\varepsilon>0$
>     * 。
> * **建议**: 静态（即零频率）介电常数就是通常所称的"该"介电常数。默认值对应 25 ${}^{\circ}$ C 下的水。

### `OpticalDielectric`

> **为 PCM 溶剂指定光学介电常数。输入部分：$solvent**
>
> * **类型**: `FLOAT`
> * **默认值**: `1.78`
> * **选项**:
>     * $\varepsilon_{\infty}$
>     * 使用的光学介电常数
>     * $\varepsilon_{\infty}>0$
>     * 。
> * **建议**: 默认值对应 25 ${}^{\circ}$ C 下的水。注意 $\varepsilon_{\infty}=n^{2}$ ，其中 $n$ 为溶剂的折射率。

### `SolventName`

> **通过命名溶剂的方式，为 PCM 计算同时指定 $\varepsilon$ 和 $\varepsilon_{\infty}$。输入部分：$solvent**
>
> * **类型**: `STRING`
> * **默认值**: `NONE`
> * **选项**:
>     * name
>     * 使用
>     * 对应于溶剂
>     * name
>     * 的
>     * $\varepsilon$
>     * 和
>     * $\varepsilon_{\infty}$
>     * 数值（见
>     * 表
>     * 11.4
>     * ）。
> * **建议**: 使用该选项与显式指定 Dielectric 或 OpticalDielectric 中的任一项是不兼容的。

| SolventName | $\varepsilon$ | $\varepsilon_{\infty}$ | SolventName | $\varepsilon$ | $\varepsilon_{\infty}$ | SolventName | $\varepsilon$ | $\varepsilon_{\infty}$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| acetic_acid（乙酸） | 6.2 | 1.88 | dimethoxyethane | 7.3 | 1.90 | iodobenzene（碘苯） | 4.7 | 2.63 |
| acetone（丙酮） | 21.1 | 1.85 | 1-2-dimethoxyethane |  |  | isobutanol（异丁醇） | 18.1 | 1.95 |
| acetonitrile（乙腈） | 36.6 | 1.81 | glyme |  |  | 2-methyl-1-propanol |  |  |
| acetylacetone（乙酰丙酮） | 26.5 | 2.11 | dimethylacetamide（N,N-二甲基乙酰胺） | 40.2 | 2.07 | isopropanol（异丙醇） | 20.2 | 1.90 |
| pentane-2-4-dione |  |  | dimethylaminobenzene | 5.0 | 2.43 | 2-propanol |  |  |
| 2-4-pentanedione |  |  | n-n-dimethylaniline（N,N-二甲基苯胺） |  |  | mesitylene（均三甲苯） | 2.3 | 2.25 |
| aniline（苯胺） | 7.1 | 2.52 | dimethylformamide（N,N-二甲基甲酰胺） | 38.2 | 2.05 | 1-3-5-trimethylbenzene |  |  |
| benzenamine |  |  | N-N-dimethylformamide |  |  | methanol（甲醇） | 33.0 | 1.77 |
| anisole（苯甲醚） | 4.4 | 2.30 | dimethylsulfoxide（二甲基亚砜） | 47.2 | 2.18 | methyl_acetate（乙酸甲酯） | 6.8 | 1.85 |
| methoxybenzene |  |  | DMSO |  |  | acetic_acid_methyl_ester |  |  |
| benzaldehyde（苯甲醛） | 17.8 | 2.39 | dioxane（二噁烷） | 2.2 | 2.02 | methyl_ethanoate |  |  |
| benzene（苯） | 2.3 | 2.25 | 1-4-dioxane |  |  | nitrobenzene（硝基苯） | 35.6 | 2.41 |
| benzonitrile（苯甲腈） | 25.6 | 2.34 | ethanol（乙醇） | 25.3 | 1.85 | nonane（壬烷） | 2.0 | 1.98 |
| benzyl_alcohol（苯甲醇） | 13.7 | 2.38 | ethanolamine（乙醇胺） | 31.9 | 2.12 | n-nonane |  |  |
| phenyl_methanol |  |  | ethyl_acetate（乙酸乙酯） | 6.1 | 1.88 | octanol（辛醇） | 10.1 | 2.05 |
| bromobenzene（溴苯） | 5.5 | 2.43 | ethyl_ethanoate |  |  | 1-octanol |  |  |
| butanol（丁醇） | 18.1 | 1.96 | acetic_acid_ethyl_ester |  |  | p-xylene（对二甲苯） | 2.3 | 2.24 |
| 1-butanol |  |  | ethyl_acetoacetate（乙酰乙酸乙酯） | 14.0 | 2.02 | para-xylene |  |  |
| butanol | 17.1 | 1.95 | ethyl-3-oxobutanoate |  |  | 1-4-dimethylbenzene |  |  |
| 2-butanol |  |  | acetoacetic_acid_ethyl_ester |  |  | pentane（戊烷） | 1.8 | 1.84 |
| butanone（丁酮） | 18.6 | 1.90 | ethyl_benzoate（苯甲酸乙酯） | 6.2 | 2.27 | n-pentane |  |  |
| 2-butanone |  |  | benzoic_acid_ethyl_ester |  |  | 1-pentanol（1-戊醇） | 15.1 | 1.99 |
| butan-2-one |  |  | decane（癸烷） | 2.0 | 1.99 | 2-pentanol | 13.4 | 1.98 |
| methyl_ethyl_ketone（甲乙酮） |  |  | n-decane |  |  | 3-pentanol | 14.0 | 2.00 |
| carbon_tetrachloride（四氯化碳） | 2.2 | 2.13 | ethyl_formate（甲酸乙酯） | 8.7 | 1.85 | 2-pentanone（2-戊酮） | 15.4 | 1.94 |
| tetrachloromethane |  |  | ethyl_methanoate |  |  | pentan-2-one |  |  |
| chlorobenzene（氯苯） | 5.7 | 2.33 | formic_acid_methyl_ester |  |  | methyl_propyl_ketone |  |  |
| chloroform（氯仿） | 4.8 | 2.08 | ethylene_glycol（乙二醇） | 42.8 | 2.05 | phenol（苯酚） | 13.4 | 2.37 |
| trichloromethane |  |  | 1-2-ethanediol |  |  | 1-propanol（1-丙醇） | 20.8 | 1.92 |
| cyclohexane（环己烷） | 2.0 | 2.03 | fluorobenzene（氟苯） | 5.5 | 2.23 | propanal（丙醛） | 17.4 | 1.86 |
| cyclohexanol（环己醇） | 16.4 | 2.15 | formamide（甲酰胺） | 111.8 | 2.10 | propionaldehyde（丙醛） |  |  |
| cyclohexanone（环己酮） | 16.1 | 2.11 | formic_acid（甲酸） | 51.1 | 1.88 | pyridine（吡啶） | 13.3 | 2.28 |
| 1-1-dichloroethane（1,1-二氯乙烷） | 10.1 | 2.01 | heptane（庚烷） | 1.9 | 1.93 | t-butanol（叔丁醇） | 12.0 | 1.92 |
| 1-2-dichloroethane（1,2-二氯乙烷） | 10.4 | 2.09 | n-heptane |  |  | tert-butanol |  |  |
| dichloromethane（二氯甲烷） | 8.9 | 2.02 | heptanol（庚醇） | 11.9 | 2.03 | 2-methyl-2-propanol |  |  |
| methylene_chloride |  |  | 1-heptanol |  |  | tetrahydrofuran（四氢呋喃） | 7.5 | 1.97 |
| diethylamine（二乙胺） | 3.7 | 1.92 | hexane（己烷） | 1.9 | 1.89 | THF |  |  |
| diethyl_ether（乙醚） | 4.3 | 1.83 | n-hexane |  |  | toluene（甲苯） | 2.4 | 2.24 |
| diethyl_ketone（3-戊酮） | 17.0 | 1.95 | hexanol（己醇） | 13.6 | 2.01 | triethylamine（三乙胺） | 2.4 | 1.96 |
| 3-pentanone |  |  | 1-hexanol |  |  | n-n-diethylethanamine |  |  |
| pentan-3-one |  |  |  |  |  | water（水） | 80.2 | 1.78 |

表 11.4: 
PCM 计算可用的命名溶剂。（缩进的名称为同义词。）
$\varepsilon$ 的数值对应
于 20${}^{\circ}$C 下的最新测量值（来自参考文献

），
而 $\varepsilon_{\infty}=n^{2}$ 的数值对应 20${}^{\circ}$C、$\lambda=589$ nm 下的最新测量值（来自参考文献

）。

## 11.2.4.4 *$solvent* 部分：非静电选项

PCM 仅描述与溶质之间的静电相互作用，其依据是静态介电常数（针对初始态），以及在非平衡激发或电离过程中可能用到的光学介电常数。描述空化（泡化，cavitation，即 Pauli 排斥）和色散相互作用等的非静电相互作用项[[569]](../bib_references/bib.md#bib580)可以用一种 *ad hoc*（特设）的方式添加，但并未针对 PCM 进行专门的参数化。（关于能够自动纳入非静电项的溶剂化模型——获得绝对溶剂化能需要这些项——参见第 [11.2.9](ex_SMx-User-Solvent.md) 节的 SM$x$ 模型，或第 [11.2.7](example_CMIRS-water.md) 节的 CMIRS 方法。

要在 PCM 计算中添加非静电相互作用，请使用 *$solvent* 部分，其一般形式如下所示。

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

关键字 **SolventAtom** 需要多个参数，而所有其他关键字仅需要单个参数，包括上文讨论过的 **Dielectric**、**OpticalDielectric** 和 **SolventName** 选项。关键字 **SolventAtom** 需要多个参数，而所有其他关键字仅需要单个参数。任何 PCM 计算都需要介电常数（其默认值对应水），而非静电参数则是可选的，且很少被添加到这些模型中。[[282]](../bib_references/bib.md#bib287)

**Q-Chem** 中目前可用的非静电相互作用基于 Cossi *et al.* 的工作，[[274]](../bib_references/bib.md#bib272)
 并在用于确定静电相互作用的自洽场（SCF）流程之外进行计算。
非静电能高度依赖于输入参数，并且可能对用于定义溶质空腔的半径选择极为敏感。
因此，纳入非静电相互作用具有很强的经验性，可能需要逐例（case-by-case）加以考虑。
依照文献 [[274]](../bib_references/bib.md#bib272)，
空化能使用与计算静电能相同的溶质空腔来计算，
而色散/排斥能则使用溶剂可及表面（SAS）空腔定义来计算。

以下关键字（位于 *$solvent* 部分中）用于为 PCM 计算定义非静电参数。

### `NonEls`

> **指定要纳入哪类非静电贡献。输入部分（INPUT SECTION）：$solvent**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * Cav
>     * 空化能
>     * Buck
>     * 基于原子序数的 Buckingham 色散与排斥能
>     * LJ
>     * 基于力场的 Lennard-Jones 色散与排斥能
>     * BuckCav
>     * Buck + Cav
>     * LJCav
>     * LJ + Cav
> * **建议**：目前可供使用的 Buckingham 势参数集合非常有限。

### `NSolventAtoms`

> **不同种类原子的数目。输入部分（INPUT SECTION）：$solvent**
>
> * **类型**：`INTEGER`
> * **默认值**：`None`
> * **选项**：
>     * $N$
>     * 指明存在
>     * $N$
>     * 种不同类型的原子。
> * **建议**：当 NonEls = Buck 、 LJ 、 BuckCav 或 LJCav 时，该关键字是必需的。例如甲醇（ $\rm CH_{3}OH$ ）有三类原子（C、H 和 O）。

### `SolventAtom`

> **指定一种唯一的溶剂原子。输入部分（INPUT SECTION）：$solvent**
>
> * **类型**：`Various`
> * **默认值**：`None.`
> * **选项**：
>     * 输入（类型）
>     * 描述
>     * Number1 (INTEGER)：
>     * 该原子的原子序数
>     * Number2 (INTEGER)：
>     * 每个溶剂分子中该类原子的数目
>     * Number3 (INTEGER)：
>     * 力场原子类型
>     * SASradius (FLOAT)：
>     * 用于定义溶剂可及表面的探针半径（以 Å 计）
> * **建议**：若不使用 LJ 或 LJCav ，则应将 Number3 设为 0。当 NonEls = Buck 、 LJ 、 BuckCav 或 LJCav 时，该关键字是必需的。

### `Temperature`

> **指定溶剂温度。输入部分（INPUT SECTION）：$solvent**
>
> * **类型**：`FLOAT`
> * **默认值**：`300.0`
> * **选项**：
>     * $T$
>     * 使用温度为
>     * $T$
>     * ，单位为开尔文（Kelvin）。
> * **建议**：仅用于空化能。

### `Pressure`

> **指定溶剂压力。输入节：$solvent**
>
> * **类型**: `FLOAT`
> * **默认值**: `1.0`
> * **选项**:
>     * $P$
>     * 使用压力
>     * $P$
>     * ，单位为 bar。
> * **建议**: 仅用于空化（cavitation）能。

### `SolventRho`

> **指定溶剂的数密度 输入节：$solvent**
>
> * **类型**: `FLOAT`
> * **默认值**: `Determined for water, based on temperature.`
> * **选项**:
>     * $\rho$
>     * 使用密度
>     * $\rho$
>     * ，单位为 molecules/Å
>     * ${}^{3}$
>     * 。
> * **建议**: 仅用于空化能。

### `SolventRadius`

> **PCM 溶剂中溶剂分子的半径。输入节：$solvent**
>
> * **类型**: `FLOAT`
> * **默认值**: `None`
> * **选项**:
>     * $r$
>     * 使用半径
>     * $r$
>     * ，单位为 Å。
> * **建议**: 仅用于空化能。

下面的示例演示了非静电相互作用的使用。

???+ example "示例 11.7: 同时使用静电与非静电 PCM 相互作用在水中优化三氟乙醇。Lennard-Jones 势中的色散与排斥采用 OPLS-AA 参数。"
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

## 11.2.4.5 非平衡溶剂化的任务控制与示例

非平衡计算需要 *$solvent* 节中的 **OpticalDielectric** 关键字，或者也可以通过指定 **SolventName** 来设置一个预定义值。当在 PCM 下执行 CIS/TDDFT 计算时，LR-PCM 激发能会自动计算，但一旦采用微扰（perturbation）方案则会被关闭。

### `ChargeSeparation`

> **在溶剂平衡态下划分快电荷与慢电荷 输入节：$pcm**
>
> * **类型**: `STRING`
> * **默认值**: `No default.`
> * **选项**:
>     * Marcus
>     * 使用 Marcus 划分方案进行慢-快电荷分离。
>     * Pekar
>     * 使用 Pekar 划分方案进行慢-快电荷分离。
> * **建议**: 电荷分离需与 $pcm 中的 StateSpecific 关键字配合使用。

### `StateSpecific`

> **指定将使用的态特异性（state-specific）PCM。 输入节：$pcm**
>
> * **类型**: `Various`
> * **默认值**: `No default.`
> * **选项**:
>     * Perturb
>     * 对垂直激发执行 ptSS 和 ptLR。
>     * External
>     * 对激发态执行自洽的 EI-SS-PCM（用于发射）。
>     * Internal
>     * 对激发态执行自洽的 II-SS-PCM（用于发射或激发）。
> * **建议**: 垂直激发能使用 ptSS-PCM，或在强极性情形下使用非平衡 II-SS-PCM；长寿命激发态的发射能则使用平衡 EI-SS-PCM。

### `Td_CEq_NonEq`

> **基于非平衡溶剂化的约束平衡原理（constrained equilibrium principle），指定用于计算溶液中垂直吸收与发射的溶剂效应的自洽 SS-PCM/TDDFT 方法。 输入节：$pcm**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * 1
>     * 在平衡基态反应场的基础上，通过在基态几何结构上进行 RPA 计算，求出吸收过程中基于非平衡的激发态自由能。
>     * 2
>     * 在非平衡激发态反应场的基础上，通过在基态几何结构上进行 RPA 计算，求出吸收过程中基于非平衡的激发态自由能。
>     * 3
>     * 在平衡激发态反应场的基础上，通过在激发态几何结构上进行 RPA 计算，求出发射过程中基于平衡的激发态自由能。
>     * 4
>     * 在非平衡基态反应场的基础上，通过在激发态几何结构上进行纯单点能计算，求出发射过程中基于非平衡的基态自由能。
> * **建议**: 选项 2 和 3 需要迭代直到激发态反应场收敛。选项 1 即选项 2 的第一次迭代。当选项 3 的平衡激发态反应场收敛后，执行选项 4。

???+ example "示例 11.8: LR-TDDFT/LR-C-PCM 低能垂直激发能"
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

???+ example "示例 11.9: 使用 ptSS 和 ptLR 方法计算平面型 DMABN 垂直激发能的 PCM 溶剂化效应。"
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

???+ example "示例 11.11.10: 采用外迭代（External Iteration）SS-PCM 的硝酸根在乙腈中的 TDDFT 计算。"
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

???+ example "示例 11.11.11: 采用内迭代（Internal Iteration）SS-PCM 及额外基态计算求硝酸根在乙腈中的垂直发射能。"
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
       jobtype ¯¯             sp
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

???+ example "示例 11.11.12: 基于约束平衡原理的 SS-PCM/TDDFT 低能垂直激发能。"
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

???+ example "示例 11.11.13: 基于约束平衡原理的 SS-PCM/TDDFT 发射过程中平衡激发态自由能。"
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

???+ example "示例 11.11.14: 基于约束平衡原理的 SS-PCM/TDDFT 发射过程中非平衡基态自由能。"
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
