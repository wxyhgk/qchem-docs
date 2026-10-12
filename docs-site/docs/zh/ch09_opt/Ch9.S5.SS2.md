---
title: "9.5.2 压强的施加"
---

## 9.5.2 压强的施加

(July 4, 2026)

**Q-Chem** 提供了多种方法，可在几何优化或 AIMD（从头算分子动力学）模拟过程中对化学体系施加压强。[[1298]](../bib_references/bib.md#bib1354)
 目前已实现的方法如下：

| 流体静压压缩力场（Hydrostatic Compression Force Field, HCFF）[[1295]](../bib_references/bib.md#bib1352) | 第 9.5.2.1 节 |
| --- | --- |
| 扩展流体静压压缩力场（eXtended Hydrostatic Compression Force Field, X-HCFF）[[1297]](../bib_references/bib.md#bib1353) | 第 9.5.2.2 节 |
| 压强乘体积项（Pressure times Volume term, PV）[[1540]](../bib_references/bib.md#bib1604) | 第 9.5.2.3 节 |
| 表面面元上的高斯模拟流体静压（Gaussians on Surface Tesserae Simulate HYdrostatic Pressure, GOSTSHYP）[[1206]](../bib_references/bib.md#bib1261) | 第 9.5.2.4 节 |

要调用上述方法之一，需在 *$rem* 段中设置 DISTORT = TRUE。
通过将 *$rem* 变量设置为 SCF_FINAL_PRINT = 1，
可在输出中打印由压强引起的能量贡献。

### `DISTORT`

> **指定是否对化学体系施加压强或外力**
>
> * **类型**: `LOGICAL`
> * **默认值**: `False`
> * **选项**:
>     * `False`: 不使用压强或力
>     * `True`: 使用压强或力
> * **建议**: 若需施加压强或力，请设置为 true。

作业的相关参数通过 *$distort* 输入段中指定的选项来设置。*$distort* 段的格式与 *$rem* 段类似：

> ```qchem
> $distort
>   <Keyword>  <parameter/option>
> $end
> ```

**注意：

以下作业控制变量*仅*属于 *$distort* 段。请勿将其放入 *$rem* 段中。
**

### `Model`

> **指定用于使分子畸变的模型。输入段：$distort**
>
> * **类型**: `STRING`
> * **默认值**: `None`
> * **选项**:
>     * `HCFF`: Hydrostatic Compression Force Field（流体静压压缩力场）
>     * `1295`: Stauch T., Chakraborty R., Head-Gordon M. ChemPhysChem (2019) ,
>     * `20`: , pp. 2742 . Link
>     * `XHCFF`: eXtended Hydrostatic Compression Force Field（扩展流体静压压缩力场）
>     * `1297`: Stauch T. J. Chem. Phys. (2020) ,
>     * `153`: , pp. 134503 . Link
>     * `PV`: 通过计算 vDW 体积添加 PV 项
>     * `1540`: Zeller F., Pracht P., Neudecker T. J. Phys. Chem. A (2025) ,
>     * `129`: , pp. 2108 . Link
>     * `GOSTSHYP`: Gaussians On Surface Tesserae Simulate HYdrostatic Pressure（表面面元上的高斯模拟流体静压）
>     * `1206`: Scheurer M. et al. J. Chem. Theory Comput. (2021) ,
>     * `17`: , pp. 583 . Link
>     * `EFEI`: 显式包含外力（External Force is Explicitly Included，第 9.5.1 节）
> * **建议**: 关于模型选择的具体建议，请参阅以下各小节。

### `Pressure`

> **指定用于压缩分子的压强（单位为 MPa）。输入段：$distort**
>
> * **类型**: `DOUBLE`
> * **默认值**: `None`
> * **选项**:
>     * 用户自定义
> * **建议**: 无

### `NPoints_Heavy`

> **指定每个非氢原子的面元剖分点数。输入段：$distort**
>
> * **类型**: `INTEGER`
> * **默认值**: `110`
> * **选项**:
>     * 用户自定义
> * **建议**: 使用默认值。

### `NPoints_Hydrogen`

> **指定每个氢原子的面元剖分点数。输入段：$distort**
>
> * **类型**: `INTEGER`
> * **默认值**: `110`
> * **选项**:
>     * 用户自定义
> * **建议**: 使用默认值。

### `Scaling`

> **指定用于分子表面剖分的原子范德华（van der Waals, vDW）半径的缩放因子，该剖分用于各压强模型。输入段：$distort**
>
> * **类型**: `DOUBLE`
> * **默认值**: `1.2`
> * **选项**:
>     * 用户自定义
> * **建议**: 在模拟化学复合物时增大该值，以确保复合物被置于单一空腔之内。 1206 Scheurer M. et al. J. Chem. Theory Comput. (2021) , 17 , pp. 583 . Link X-HCFF 模型中建议使用 1.0 的取值。 1297 Stauch T. J. Chem. Phys. (2020) , 153 , pp. 134503 . Link

### `tess_method`

> **选择面元剖分方法。输入段：$distort**
>
> * **类型**: `STRING`
> * **默认值**: `scrf`
> * **选项**:
>     * `scrf`: 使用与隐式溶剂化模型相同的剖分代码
>     * `distort`: 使用 libdistort 剖分例程
>     * `occ`: 使用外空腔校正（outer cavity correction）
> * **建议**: 若要在同一计算中与隐式溶剂化模型保持兼容，请使用 distort 选项。Scrf 选项支持更多空腔选项。OCC 可减少负振幅的出现量——建议用于 SCF 收敛不佳的 GOSTSHYP 计算。

### `proberad`

> **在 vDW 半径上叠加探针半径（proberad），以模拟溶剂可及表面（solvent accessible surface, SAS）。输入段：$distort**
>
> * **类型**: `DOUBLE`
> * **默认值**: `0.0`
> * **选项**:
>     * 用户自定义
### `occrad`

> **OCC GOSTSHYP 计算中外空腔的距离。输入段：$distort**
>
> * **类型**: `DOUBLE`
> * **默认值**: `0.25`
> * **选项**:
>     * 用户自定义
> * **建议**: 取值越小，出现负振幅的概率越高；取值越大，则会舍弃大量剖分点。

## 9.5.2.1 流体静压压缩力场（HCFF）

流体静压压缩力场（Hydrostatic Compression Force Field, HCFF）模型由 Stauch、Chakraborty 和 Head-Gordon 提出。[[1295]](../bib_references/bib.md#bib1352)
 在 HCFF 中，使用指向非质量加权分子质心的机械力来压缩分子。由于在极高
压强下 HCFF 倾向于生成球形几何结构，因此在模拟延展型分子时需要谨慎。[[1298]](../bib_references/bib.md#bib1354)
 此外，用户输入的压强只是对实际施加于分子上压强的一个猜测值。
后者是根据生成的几何结构和分子表面*事后*（*a posteriori*）计算得出的，并以 *HCFF Macroscopic Pressure*（HCFF 宏观压强）的形式输出。
通常，实际施加的压强低于输入的压强。需要注意的是，由于对核梯度的依赖，
HCFF 无法对单个原子施加压强。而且，由于压强仅作用于原子核，
并未直接模拟电子密度的压缩，因此在压缩分子时 HCFF 通常会低估电子能量的增加量。
HCFF 可与任何可获得核梯度的电子结构方法配合使用。

???+ example "示例 9.16: 使用 HCFF 模型在输入压强为 3808 MPa 条件下对乙硼烷进行几何优化"
    ```qchem
    $molecule
       0 1
       B     0.0000000000    0.0000000000    0.8917854534
       B     0.0000000000    0.0000000000   -0.8917854534
       H    -0.5244343500    0.9105724300    1.4720415209
       H     0.5244343500   -0.9105724300    1.4720415209
       H    -0.5244343500    0.9105724300   -1.4720415209
       H     0.5244343500   -0.9105724300   -1.4720415209
       H     0.8561835151    0.4929549655    0.0000000000
       H    -0.8561835151   -0.4929549655    0.0000000000
    $end
    
    $rem
       JOBTYPE            opt
       METHOD             m06-2x
       BASIS              6-311++G(d,p)
       DISTORT            true
    $end
    
    $distort
       model              hcff
       pressure           3808
       scaling            1.0
       npoints_heavy      590
       npoints_hydrogen   590
    $end
    ```

## 9.5.2.2 扩展流体静压压缩力场（X-HCFF）

扩展流体静压压缩力场（eXtended Hydrostatic Compression Force Field, X-HCFF）方法由 Stauch 提出，
用于解决 HCFF 存在的问题。[[1297]](../bib_references/bib.md#bib1353)
 与 HCFF 类似，X-HCFF 同样使用机械力来压缩分子，但与 HCFF 不同的是，
这些力严格垂直于剖分后的分子表面，从而模拟真正的流体静压条件。因此，
即使在高压力下也能保持化学上合理的几何结构。此外，用户可以
输入模拟过程中实际施加于分子的精确压强。建议在剖分例程中
使用未经缩放的原子范德华半径。[[1297]](../bib_references/bib.md#bib1353)
 X-HCFF 可与任何可获得核梯度的电子结构方法配合使用。
也可以通过设置 JOBTYPE = FREQ，在 X-HCFF 下进行解析 Hessian 计算，
从而获得相关的结构性质，如红外（IR）和拉曼（Raman）频率。[[1447]](../bib_references/bib.md#bib1509)

需要指出的是，X-HCFF 模型中所构造的力并非由某项能量对几何求导得到，
而是直接构造并加到梯度上。因此，电子能量中不会加入相应的能量项，
由此压强引起的电子能量增加通常偏低。
X-HCFF 的力可以理解为对 vDW 体积梯度的一个近似。[[1540]](../bib_references/bib.md#bib1604)

???+ example "示例 9.17: 使用 X-HCFF 模型在 100 GPa 压强下对 CO ${}_{2}$ 二聚体进行几何优化"
    ```qchem
    $molecule
       0 1
       O    2.6192991230   -0.0571311942    0.0000000000
       C    1.6782610262    0.6502025480    0.0000000000
       O    0.7413912820    1.3674070371    0.0000000000
       C   -1.6782610262   -0.6502025480    0.0000000000
       O   -2.6192991230    0.0571311942    0.0000000000
       O   -0.7413912820   -1.3674070371    0.0000000000
    $end
    
    $rem
       JOBTYPE            opt
       METHOD             pbe
       BASIS              cc-pvdz
       DISTORT            true
    $end
    
    $distort
       model              xhcff
       pressure           100000
       scaling            1.0
       npoints_heavy      302
       npoints_hydrogen   302
    $end
    ```

## 9.5.2.3 PV 项

处于任意施压介质中的分子体系的焓 $H$ 可表示为电子能量 $E_{el}$ 与
压强 $P$ 乘以分子所占据体积 $V$ 之和。

<a id="Ch9.E44"></a>

$$
H=E_{el}+PV \tag{9.44}
$$

对分子体积最简单的近似大概是 vDW 体积，本文即采用该近似。
它可以通过对分子 vDW 表面进行数值积分来计算（见 [11.2.3.2](../ch11_env/topic_pcm-em.md#subsubsec:pcm_cavity)），
并会为分子梯度提供一个定义明确的贡献。[[1540]](../bib_references/bib.md#bib1604)
 这种方法产生的压强致形变与 X-HCFF 模型类似，但它为能量提供了远更真实的校正。

该方法提供了 Hessian，可通过频率计算获得红外和拉曼频率。

## 9.5.2.4 表面面元上的高斯模拟流体静压（GOSTSHYP）

由 Scheurer 及其合作者提出的表面面元上的高斯模拟流体静压
（Gaussians On Surface Tesserae Simulate HYdrostatic Pressure, GOSTSHYP）方法[[1206]](../bib_references/bib.md#bib1261)
克服了与压强的机械化学模型（*i.e.* HCFF 和 X-HCFF）相关的问题。
GOSTSHYP 在剖分后的分子表面放置一个均匀的势场（由一系列高斯势组成），用以压缩
电子密度。每个高斯势 G${}_{j}$ 的形式为

<a id="Ch9.E45"></a>

$$
G_{j}=p_{j}\cdot\exp\left(-w_{j}(\textbf{r}-\textbf{r}_{0})^{2}\right) \tag{9.45}
$$

在 GOSTSHYP 例程运行过程中，高斯势的参数 $p_{j}$ 和
$w_{j}$ 会被调整，以施加用户指定的压强。该方法既可处理原子也可处理分子，
且压强引起的电子能量增加在物理上是合理的。在 SCF 过程中，能量表达式具有以下形式

<a id="A3.S8.EGx72"></a>

$$
\displaystyle E_{\text{GOSTSHYP}} \tag{9.46}
$$

由于可以获取核梯度，因此可以使用 GOSTSHYP 模型在压强下进行几何优化。
目前，GOSTSHYP 仅在 SCF 层级实现，可用于 Hartree-Fock（HF）和密度泛函理论（Density Functional Theory, DFT）计算。

为了获得良好的性能，GOSTSHYP 需要相对较大的可用内存（RAM）。如果检测到
可用内存不足，GOSTSHYP 将切换到内存效率更高但以性能为代价的算法，
并在输出中打印包含最佳性能所需内存量的警告信息。

我们发现，在两个原子的剖分球面交界处可能出现"负振幅"
$p_{j}$。由于它们会导致非物理的吸引性压强势，因此在 GOSTSHYP 计算中通常会被屏蔽（blacklist）。
然而这会导致 SCF 计算中的不稳定性。我们发现，当 VDW 缩放因子大于 $1.5$ 时，
负振幅极少出现，但缩放因子越小则越容易出现。
另一种做法是通过定义探针半径来使用溶剂可及表面（SAS）（见 [11.2.3.2](../ch11_env/topic_pcm-em.md#subsubsec:pcm_cavity)），其效果类似。
我们近期提出了外空腔校正（outer cavity correction, OCC）[[1048]](../bib_references/bib.md#bib1093)
，它应能显著改善收敛性。
要使用该校正，请将 tess_method 设置为 occ。

???+ example "示例 9.18: 使用 GOSTSHYP 模型在 40 GPa 压强下对环戊二烯与乙烯进行几何优化"
    ```qchem
    $molecule
       0 1
       C    1.1148422354   -0.6418674001    0.7279292386
       C    1.1148422354   -0.6418674001   -0.7279292386
       C    0.5936432126    0.5363396649    1.1772168767
       C   -2.0464511598   -0.6129291257    0.6711240568
       C   -2.0464511598   -0.6129291257   -0.6711240568
       C    0.5936432126    0.5363396649   -1.1772168767
       C    0.2915208637    1.4128825196    0.0000000000
       H    0.9756522868    2.2894492537    0.0000000000
       H   -0.7374232239    1.8214336422    0.0000000000
       H    1.4681344173   -1.4690333337   -1.3527755131
       H    1.4681344173   -1.4690333337    1.3527755131
       H   -2.3879086093    0.2541525765    1.2531118994
       H   -1.7231567891   -1.4887031107    1.2461940178
       H   -1.7231567891   -1.4887031107   -1.2461940178
       H   -2.3879086093    0.2541525765   -1.2531118994
       H    0.4773764265    0.8454441265    2.2200767812
       H    0.4773764265    0.8454441265   -2.2200767812
    $end
    
    $rem
       JOBTYPE               opt
       METHOD                pbe
       BASIS                 cc-pvdz
       GEOM_OPT_MAX_CYCLES   150
       SCF_ALGORITHM         diis_gdm
       MAX_SCF_CYCLES        150
       USE_LIBQINTS          1
       GEN_SCFMAN            1
       DISTORT               1
    $end
    
    $distort
       model                 gostshyp
       pressure              40000
       npoints_heavy         302
       npoints_hydrogen      302
       scaling               1.8
    $end
    ```
