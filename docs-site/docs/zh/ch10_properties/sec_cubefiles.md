---
title: "10.5.5 直接生成“Cube”文件"
---

## 10.5.5 直接生成“Cube”文件

（2026 年 7 月 4 日）

作为上文所讨论输出格式的一种替代方案，所有 *$plots* 数据都可以直接输出到作业暂存（scratch）目录中一个名为 `plots` 的子目录下，因此必须使用第 [2.2](../ch02_install/sect_running.md) 节中描述的 *–save* 选项来保存该目录。此子目录中的绘图数据并非以上文所述的 `plot.*` 格式写出，而是以所谓“cube”文件的形式写出，每个所请求的轨道或密度对应一个文件。cube 文件格式是体数据（volumetric data）的一种标准格式，由一个很小的文件头后跟每个网格点上的轨道或密度值组成，采用 ASCII 格式。（完整格式规范请参阅参考文献

。）由于网格坐标本身并不打印出来（其位置可由文件头中包含的信息隐含确定），因此每个单独的 cube 文件都比对应的 `plot.*` 文件小得多。许多标准且可免费获得的图形程序都能读取 cube 文件，包括
**MacMolPlt[[136]](../bib_references/bib.md#bib126)
[[12]](../bib_references/bib.md#bib16)
** 以及 **VMD**.[[604]](../bib_references/bib.md#bib627)
[[15]](../bib_references/bib.md#bib19)

特别推荐使用 VMD 来生成用于发表的高质量图像。按照第 [10.5.4](sect_plot.mo.md) 节所述指定 *$plots* 区段，并将 MAKE_CUBE_FILES 设置为 TRUE，即可为 *$plots* 区段中所请求的分子轨道（MO）与密度生成 cube 文件。

MAKE_CUBE_FILES

### `MAKE_CUBE_FILES`

> **请求为 MO、NTO 或 NBO 生成 cube 文件。**
>
> * **类型**: `LOGICAL/STRING`
> * **默认值**: `FALSE`
> * **可选值**:
>     * FALSE
>     * 不生成 cube 文件。
>     * TRUE
>     * 为 MO 和密度生成 cube 文件。
>     * NTOS
>     * 为自然跃迁轨道（Natural Transition Orbitals, NTO）生成 cube 文件。
>     * NBOS
>     * 为自然键轨道（Natural Bond Orbitals, NBO）生成 cube 文件。
> * **建议**: 无

PLOT_SPIN_DENSITY

### `PLOT_SPIN_DENSITY`

> **请求生成自旋密度 $\rho_{\alpha}$ 和 $\rho_{\beta}$。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * FALSE
>     * 不生成自旋密度 cube 文件。
>     * TRUE
>     * 生成自旋密度 cube 文件。
> * **建议**: 若在总密度之外还需要自旋密度，则将其设置为 TRUE。这要求同时把 MAKE_CUBE_FILES 设置为 TRUE，并且在 $plots 输入区段中请求了一个或多个总密度。相应的自旋密度随后也会被一并生成。

下面的示例演示了如何为基态密度和激发态密度生成 cube 文件，其中包括相应的自旋密度。在本例中，作业暂存目录下的 `plots` 子目录应包含名为 `dens.N.cube`（第 $N$ 个态的总密度，其中 $N=0$ 或 1 分别代表基态与第一激发态）、`dens_alpha.N.cube` 和 `dens_beta.N.cube`（每个态的 $\rho_{\alpha}$ 与 $\rho_{\beta}$），以及 `dens_spin.N.cube`（每个态的 $\rho_{\alpha}-\rho_{\beta}$。）

???+ example "示例 10.27: 为 HOO 自由基的基态与第一激发态生成密度及自旋密度 cube 文件。"
    ```qchem
    $molecule
       0 2
       H     1.004123   -0.180454    0.000000
       O    -0.246002    0.596152    0.000000
       O    -1.312366   -0.230256    0.000000
    $end
    
    $rem
       PLOT_SPIN_DENSITY  true
       MAKE_CUBE_FILES    true
       SCF_CONVERGENCE    8
       METHOD             b3lyp
       BASIS              6-31+G*
       CIS_N_ROOTS        1
    $end
    
    $plots
    grid information and request to plot 2 densities
       20  -5.0  5.0
       20  -5.0  5.0
       20  -5.0  5.0
       0  2  0  0
       0  1
    $end
    ```

将 MAKE_CUBE_FILES 设置为 NTOS，同样可以为自然跃迁轨道（NTO）生成 cube 文件（第 [7.13.3](../ch07_excited/sect_NTOs.md) 节与第 [10.5.3](sect_visualize_NTOs.md) 节），不过在这种情况下过程略显复杂，因为这些量具有态特定（state-specific）的性质。NTO 的 cube 文件只会为单个激发态生成，该态由 CUBEFILE_STATE 指定。若要获取其他态的 cube 文件，只需串联运行若干个 **Q-Chem** 作业即可，其中第二个（及后续）作业通过 SCF_GUESS 和 SKIP_CIS_RPA 读入已收敛的基态与激发态信息。

CUBEFILE_STATE

### `CUBEFILE_STATE`

> **决定使用哪一个激发态来生成 cube 文件**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **可选值**:
>     * $n$
>     * 为第
>     * $n$
>     * 个激发态生成 cube 文件
> * **建议**: 无

另一个需要注意的复杂之处在于指定哪些 NTO 将作为 cube 文件输出。当 MAKE_CUBE_FILES 设置为 TRUE 时，这在 *$plots* 区段中指定，与指定待绘制的 MO 的方式相同。但必须理解 NTO 的存储顺序。对于一个具有 $N_{\alpha}$ 个 $\alpha$ 自旋 MO 的体系，占据 NTO $1,2,\ldots,N_{\alpha}$ 按振幅递增的顺序存储，因此第 $N_{\alpha}$ 个占据 NTO 是最重要的。虚 NTO 紧随其后存储，并按*递减*的重要性排序。按照这一约定，对于任意特定激发态，主要（principle）NTO 对由最后一个占据轨道和第一个虚轨道组成。因此，轨道 $N_{\alpha}$ 和 $N_{\alpha}+1$ 代表最重要的 NTO 对，而轨道 $N_{\alpha}-1$ 和 $N_{\alpha}+2$ 代表第二重要的 NTO 对，依此类推。

???+ example "示例 10.28: 为尿嘧啶（uracil）第二单重激发态的主要占据 NTO 与虚 NTO 之间的跃迁生成 cube 文件。注意尿嘧啶的 $N_{\alpha}=29$。"
    ```qchem
    $molecule
       0 1
       N    -2.181263     0.068208     0.000000
       C    -2.927088    -1.059037     0.000000
       N    -4.320029    -0.911094     0.000000
       C    -4.926706     0.301204     0.000000
       C    -4.185901     1.435062     0.000000
       C    -2.754591     1.274555     0.000000
       N    -1.954845     2.338369     0.000000
       H    -0.923072     2.224557     0.000000
       H    -2.343008     3.268581     0.000000
       H    -4.649401     2.414197     0.000000
       H    -6.012020     0.301371     0.000000
       H    -4.855603    -1.768832     0.000000
       O    -2.458932    -2.200499     0.000000
    $end
    
    $plots
    Plot the dominant NTO pair, N --&gt; N+1
       25  -5.0  5.0
       25  -5.0  5.0
       25  -5.0  5.0
       2  0  0  0
       29  30
    $end
    
    $rem
       METHOD           B3LYP
       BASIS            6-31+G*
       CIS_N_ROOTS      2
       CIS_TRIPLETS     FALSE
       NTO_PAIRS        TRUE    ! calculate the NTOs
       MAKE_CUBE_FILES  NTOS    ! generate NTO cube files...
       CUBEFILE_STATE   2       ! ...for the 2nd excited state
    $end
    ```

自然键轨道（NBO，可以是基态或任意 CIS、RPA 或 TDDFT 激发态）的 cube 文件也可以用几乎相同的方式生成，只需将 MAKE_CUBE_FILES 设置为 NBOS，并使用 CUBEFILE_STATE 选择所需的电子态。CUBEFILE_STATE = 0 选择基态 NBO。待绘制的具體 NBO 通过 *$plots* 区段来选取，但需认识到 **Q-Chem** 按占据数递减的顺序存储 NBO，并且在非限制（unrestricted）SCF 计算中，所有 $\alpha$ 自旋 NBO 都排在任何 $\beta$ 自旋 NBO 之前。（对于基态，通常每个电子对应一个强占据 NBO。）NBO cube 文件保存在作业暂存目录下的 `plots` 子目录中。最后一点注意事项：要获得 NBO cube 文件，用户必须在 *$nbo* 区段中指定 AONBO 选项，如下例所示。

???+ example "示例 10.29: 为 $\rm H_{2}O$ 第一激发态的 NBO 生成 cube 文件。"
    ```qchem
    $rem
       METHOD           CIS
       BASIS            CC-PVTZ
       CIS_N_ROOTS      1
       CIS_TRIPLETS     FALSE
       NBO              2      ! ground- and excited-state NBO
       MAKE_CUBE_FILES  NBOS   ! generate NBO cube files...
       CUBEFILE_STATE   1      ! ...for the first excited state
    $end
    
    $nbo
      AONBO
    $end
    
    $molecule
       0 1
       O
       H  1  0.95
       H  1  0.95  2  104.5
    $end
    
    $plots
    Plot the 5 high-occupancy NBOs, one for each alpha electron
       40  -8.0  8.0
       40  -8.0  8.0
       40  -8.0  8.0
       5  0  0  0
       1  2  3  4  5
    $end
    ```

???+ example "示例 10.30: 使用 *$plots* 区段的新格式绘制 NTO 与 NBO 图：
绘制第一激发态的 NTO（两对）以及基态和第一激发态各自的五个 NBO。
下方 nbo 区段中的 aonbo 关键字是必需的。"
    ```qchem
    $molecule
      0 1
       O
       H 1 0.95
       H 1 0.95 2 104.5
    $end
    
    $rem
       METHOD¯¯     cis
       BASIS¯¯     cc-pvtz
       CIS_N_ROOTS       1
       CIS_TRIPLETS      false
       nbo               2  ! ground- and excited-state NBO
       NTO_PAIRS         2  ! triggers NTO analysis
       MAKE_CUBE_FILES   true
       PLOTS             true
    $end
    
    $nbo
       aonbo
    $end
    
    $plots
       grid_points 50 50 50
       nbo_state   0-1
       natural_bond_orbital 1-5
       natural_transition_orbital 1
    $end
    ```

此外，还可以从复数吸收势 Hartree-Fock（Complex-Absorbing-Potential Hartree-Fock, CAP-HF）或复数吸收势密度泛函理论（Complex-Absorbing-Potential Density Functional Theory, CAP-DFT）计算中获得分子轨道（MO）或基态电子密度的 cube 文件。此时 *$plots* 区段无需做任何调整，但用户应当留意加以区分识别。
