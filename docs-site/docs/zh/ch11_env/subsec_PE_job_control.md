---
title: "11.8.2 作业控制"
---

## 11.8.2 作业控制

(July 4, 2026)

PE 的作业控制通过两个部分来实现，即 *$rem* 和 *$pe*。
要启用 PE-ADC，应在 *$rem* 部分中指定 ADC 方法以及其他 ADC
作业控制参数（阈值、最大迭代次数等）。PE-ADC 支持由 **libwfa** 模块执行的
激发态分析（STATE_ANALYSIS）。

PE

### `PE`

> **开启 PE。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `False`
> * **选项**:
>     * True
>     * 执行 PE 计算。
>     * False
>     * 不执行 PE 计算。
> * **建议**: 将 $rem 变量设置为 TRUE 以启动 PE 计算。

**注意：

开启 PE 会通过将 POINT_GROUP_SYMMETRY 设置为 FALSE 来禁用对称性。

**

**注意：

运行 PE 时，必须将 REM 变量 USE_LIBQINTS 和 GEN_SCFMAN
设置为 TRUE。
**

PE 专用的选项可以在 *$pe* 输入部分中设置。*$pe* 部分的格式
要求关键字与取值之间用空格分隔，形成键值对：

> ```qchem
> $pe
>    <keyword>  <parameter>
> $end
> ```

**注意：

以下作业控制变量*只能*放在 *$pe*
部分中。请勿将其放置在 *$rem* 部分。
**

### `POTFILE`

> **势文件（potential file）的路径。INPUT SECTION: $pe**
>
> * **类型**: `STRING`
> * **默认值**: `potfile.pot`
> * **选项**:
>     * 提供势文件的路径/名称。
> * **建议**: 无

### `DIIS`

> **使用 DIIS 加速以求解诱导矩。INPUT SECTION: $pe**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `TRUE`
> * **选项**:
>     * TRUE
>     * 开启 DIIS 加速。
>     * FALSE
>     * 关闭 DIIS 加速（使用常规的 Jacobi 求解器）。
> * **建议**: TRUE

### `CONVERGENCE_INDUCED`

> **诱导矩收敛阈值。将诱导矩收敛至残差范数 $10^{-\text{CONVERGENCE\_INDUCED}}$ 。INPUT SECTION: $pe**
>
> * **类型**: `INTEGER`
> * **默认值**: `8`
> * **选项**:
>     * $n\leq 12$
>     * 对应于
>     * $10^{-n}$
> * **建议**: 除非需要更高的精度，否则使用默认值。

### `MAXITER`

> **诱导矩的最大迭代次数。INPUT SECTION: $pe**
>
> * **类型**: `INTEGER`
> * **默认值**: `50`
> * **选项**:
>     * $n\geq 1$
> * **建议**: 使用默认值。如果需要更多迭代次数才能使诱导矩收敛，则体系设置中可能存在错误。

### `BORDER`

> **对靠近 QM/MM 边界区域的位点启用边界重分布/移除选项。INPUT SECTION: $pe**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 启用边界选项。
>     * FALSE
>     * 禁用边界选项。
> * **建议**: 无

### `BORDER_TYPE`

> **移除或重分布多极矩/极化率。INPUT SECTION: $pe**
>
> * **类型**: `STRING`
> * **默认值**: `REMOVE`
> * **选项**:
>     * REMOVE
>     * 移除多极矩/极化率。
>     * REDIST
>     * 重分布多极矩/极化率。
> * **建议**: 无

### `BORDER_RMIN`

> **在移除/重分布时需要考虑的 QM 原子与 MM 位点之间的最小距离 INPUT SECTION: $pe**
>
> * **类型**: `FLOAT`
> * **默认值**: `2.2`
> * **选项**:
>     * $r>0$
>     * （单位取决于 BORDER_RMIN_UNIT）
> * **建议**: 无

### `BORDER_RMIN_UNIT`

> **BORDER_RMIN 的单位，默认为原子单位（AU） INPUT SECTION: $pe**
>
> * **类型**: `STRING`
> * **默认值**: `AU`
> * **选项**:
>     * AU
>     * 使用原子单位。
>     * AA
>     * 使用埃（Angstrom）。
> * **建议**: 无

### `BORDER_REDIST_ORDER`

> **从此阶数开始的矩将被移除。例如，若设置为 1（默认值），则只重分布电荷，所有更高阶的矩均被移除。INPUT SECTION: $pe**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * $n=0,1,2,3,...$
> * **建议**: 无

### `BORDER_N_REDIST`

> **多极矩/极化率重分布的目标邻近位点数。默认值（-1）表示重分布到所有不处于边界区域的位点。INPUT SECTION: $pe**
>
> * **类型**: `INTEGER`
> * **默认值**: `-1`
> * **选项**:
>     * $n=-1,1,2,3,...,\text{number of MM sites}$
> * **建议**: 使用默认值。

### `BORDER_REDIST_POL`

> **是否重分布极化率？若设置为 FALSE，则移除极化率。INPUT SECTION: $pe**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 重分布极化率。
>     * FALSE
>     * 移除极化率。
> * **建议**: 无

???+ example "示例 11.52: 在六个水分子存在下对对硝基苯胺（4-Nitroaniline）进行 PE-HF 计算的输入"
    ```qchem
    $comment
    The potential file \texttt{gen\_scfman\_pe\_potfile.pot} can be
    found in the samples folder.
    $end
    
    $molecule
       0 1
       C      8.64800        1.07500       -1.71100
       C      9.48200        0.43000       -0.80800
       C      9.39600        0.75000        0.53800
       C      8.48200        1.71200        0.99500
       C      7.65300        2.34500        0.05500
       C      7.73200        2.03100       -1.29200
       H     10.18300       -0.30900       -1.16400
       H     10.04400        0.25200        1.24700
       H      6.94200        3.08900        0.38900
       H      7.09700        2.51500       -2.01800
       N      8.40100        2.02500        2.32500
       N      8.73400        0.74100       -3.12900
       O      7.98000        1.33100       -3.90100
       O      9.55600       -0.11000       -3.46600
       H      7.74900        2.71100        2.65200
       H      8.99100        1.57500        2.99500
    $end
    
    $rem
       METHOD               HF
       BASIS                STO-3G
       PE                   TRUE
    point_group_symmetry False
       USE_LIBQINTS         TRUE
    $end
    
    $pe
       potfile  gen_scfman_pe_potfile.pot
    $end
    ```
