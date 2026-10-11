---
title: "10.5.8 静电势"
---

## 10.5.8 静电势

(July 4, 2026)

**Q-Chem** 可以在一组网格点上计算静电势。静电势（Electrostatic Potential, ESP）的求值由 *$rem* 变量 ESP_GRID 控制。

**注意：

为了与 **Q-Chem**/**Charmm** 接口保持向后兼容，名称 IGDESP 与 ESP_GRID 等价。
**

ESP_GRID

### `ESP_GRID`

> **控制在网格点上静电势的求值。若启用，输出将以 $x,y,z,\phi(x,y,z)$ 的形式（对每一个点）写入 ASCII 文件 plot.esp，其中 $\phi$ 为静电势。**
>
> * **类型**: `INTEGER`
> * **默认值**: `-4`
> * **选项**:
>     * $-1$
>     * 通过输入文件的
>     * $plots
>     * 部分读取网格输入
>     * $-2$
>     * 与选项
>     * $-1$
>     * 相同，此外还计算
>     * $external_charges
>     * 的静电势
>     * $-3$
>     * 与选项
>     * $-1$
>     * 相同，但需配合
>     * STATE_ANALYSIS
>     * =
>     * TRUE
>     * 使用。
>     * 该选项会为所有激发态密度、跃迁密度以及电子/空穴密度计算静电势。
>     * $-4$
>     * 不进行静电势求值
>     * $0$
>     * 在所有核位置处生成静电势值
>     * +
>     * $n$
>     * 从 ASCII 文件
>     * ESPGrid
>     * 中读取 $n$ 个以 bohr 为单位的网格点
> * **建议**: 对于 $+n$ 选项，用户还应指定 NO_REORIENT = TRUE 。这会强制 **Q-Chem** 使用用户的坐标系（在 $molecule 部分中确立），该坐标系应当与 ESPGrid 文件中所使用的坐标系一致。

下面的示例演示了在网格上求值静电势。注意 IANLTY 也必须设置为 200。

???+ example "示例 10.32: 一个沿键轴方向在 1×1×15 网格上计算 H ${}_{2}$ 静电势的作业。输出写入名为 plot.esp 的 ASCII 文件，其中对每个网格点列出 $x$ 、 $y$ 、 $z$ 以及静电势。"
    ```qchem
    $molecule
       0  1
       H   0.0   0.0   0.35
       H   0.0   0.0  -0.35
    $end
    
    $rem
       METHOD     hf
       BASIS      6-31g**
       IANLTY     200
       ESP_GRID     -1
    $end
    
    $plots
       plot the electrostatic potential on a line
       1   0.0   0.0
       1   0.0   0.0
      15  -3.0   3.0
       0  0  0  0
       0
    $end
    ```

下面的示例在绘图网格上计算静电势并生成一个 cube 文件，该文件可被 IQmol 加载，用于可视化分子表面（*例如* vdW 表面或电子密度等值面）上的静电势。

???+ example "示例 10.33: 在用户指定的网格上计算乙酰氯的静电势，并生成 cube 文件作为结果；此处使用 $plots 部分的新格式"
    ```qchem
    $molecule
     0 1
     C       0.00000     1.18959     1.29360
     H       0.00000     1.01580     2.37206
     H       0.88291     1.76694     1.00084
     H      -0.88291     1.76694     1.00084
     C       0.00000    -0.13357     0.57945
     O       0.00000    -1.22212     1.05977
     Cl      0.00000     0.06441    -1.23718
    $end
    
    $rem
     jobtype  sp
     method   b3lyp
     basis    6-31g(d)
     point_group_symmetry False
     scf_convergence  8
     esp_grid  -1
     make_cube_files  true
     plots    true
     gui      2
    $end
    
    $plots
     grid_points 50 50 50
     grid_range (-4,4) (-5,5) (-5,5)
    $end
    ```

我们还可以计算跃迁密度的静电势，例如可用于计算激发能量转移（excitation energy transfer）中的库仑耦合（Coulomb coupling）。

ESP_TRANS

### `ESP_TRANS`

> **控制跃迁密度静电势的计算**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 计算激发态跃迁密度的静电势
>     * FALSE
>     * 计算激发态电子密度的静电势
> * **建议**: 无（NONE）

静电势是一个复杂的对象，通常使用基于原子电荷的简化表示来对其进行建模。为此，人们早已知道 Mulliken 电荷的表现非常差。文献中给出了多种由静电势导出（ESP-derived）原子电荷的定义，然而其中大多数依赖于在选定的一组网格点上对静电势进行最小二乘拟合。尽管这些网格点通常都被精心挑选，以使静电势在“化学上重要的”区域得到良好建模，但计算得到的电荷仍会随分子的旋转而改变。近期提出了一种高效的旋转不变算法，它不是通过直接拟合来建模静电势，而是通过对多极矩（multipole moments）进行拟合来实现。[[1255]](../bib_references/bib.md#bib1308)
 通过这种方式，人们发现对静电势的拟合效果优于那些依赖直接拟合静电势的方法。
该计算需要采用无迹（traceless）形式的多极矩，这些多极矩在计算过程中也会被打印出来。若要求解这些由多极矩导出的电荷（multipole-derived charges, MDCs），请在 *$rem* 部分设置 MM_CHARGES = TRUE 。

MM_CHARGES

### `MM_CHARGES`

> **请求计算多极矩导出电荷（MDCs）。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 计算 MDCs，同时计算多极矩的无迹形式
> * **建议**: 若需要 MDCs 或多极矩的无迹形式，请设置为 TRUE 。该计算耗时不长。
