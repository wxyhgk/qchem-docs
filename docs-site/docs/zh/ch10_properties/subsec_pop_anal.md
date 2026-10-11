---
title: "10.2.2 原子部分电荷"
---

## 10.2.2 原子部分电荷

(July 4, 2026)

## 10.2.2.1 Mulliken 电荷与 Löwdin 电荷

单电子电荷密度，

<a id="eq1001"></a>
$$
\rho({\rm{\bf r}})=\sum\limits_{\mu\nu}{P_{\mu\nu}\,\phi_{\mu}({\rm{\bf r}})\,\phi_{\nu}({\rm{\bf r}})}\;, \tag{10.1}
$$

表示在点 $\mathbf{r}$ 处找到电子的概率，但对于分子中与给定原子核相关联的电子数目几乎没有给出任何信息。然而，由于电子数 $N$ 与占据轨道 $\psi_{i}$ 的关系为

<a id="eq1002"></a>
$$
N=2\sum_{a}^{N/2}\bigl{|}\psi_{a}(\mathbf{r})\bigr{|}^{2} \tag{10.2}
$$

我们可以将 $\psi_{a}$ 的原子轨道（atomic orbital, AO）基组展开代入式 ([10.2](#eq1002))，得到

<a id="eq1003"></a>
$$
N=\sum_{\mu\nu}P_{\mu\nu}S_{\mu\nu}=\sum_{\mu}\left(\mathbf{PS}\right)_{\mu\mu}=\mathrm{tr}(\mathbf{PS}) \tag{10.3}
$$

其中我们将 $(\mathbf{PS})_{\mu\mu}$ 解释为与 $\phi_{\mu}$ 相关联的电子数。如果基函数是以原子为中心的，则通过对某个原子的所有基函数求和，即可获得与该原子相关联的电子数。由此得到原子 $A$ 净电荷的 Mulliken 公式：

<a id="eq1004"></a>
$$
q_{A}=Z_{A}-\sum_{\mu\in A}\left(\mathbf{PS}\right)_{\mu\mu} \tag{10.4}
$$

其中 $Z_{A}$ 是该原子的核电荷。这被称为 *Mulliken 布居分析*（Mulliken population analysis），

 且默认情况下即会执行该分析。

尽管概念上很简单，Mulliken 布居分析严重依赖于所用基组，并且可能产生非物理的负电子数。另一种选择是 *Löwdin 布居分析*（Löwdin population analysis），[[861]](../bib_references/bib.md#bib896)
 它使用 Löwdin 对称正交化基组（该基组仍带有原子标记）来分配电子密度。这种方法表现出较小的基组依赖性，但保持了相同的基本特征。

虽然 Mulliken 和 Löwdin 布居分析被广泛使用，并且可用于提供电子密度变化以及局域自旋极化的信息，但不应将其解释为体系中原子的氧化态。对于这类信息，我们建议使用成键分析技术（LOBA 或 NBO）。

POP_MULLIKEN

### `POP_MULLIKEN`

> **控制是否运行 Mulliken 布居分析。**
>
> * **类型**: `LOGICAL/INTEGER`
> * **默认值**: `TRUE (or 1)`
> * **选项**:
>     * FALSE (or 0)
>     * 不计算 Mulliken 布居。
>     * TRUE (or 1)
>     * 计算 Mulliken 布居。
>     * 2
>     * 同时计算每个占据轨道的各壳层布居。
>     * 3
>     * 输出与 2 相同，并额外给出核中心处的轨道密度。
>     * $-1$
>     * 计算基态以及任意 CIS、RPA 或 TDDFT 激发态的 Mulliken 电荷。
> * **建议**: 保持为 TRUE，除非需要激发态电荷。Mulliken 分析只是微不足道的额外计算，无论对基态还是激发态均如此。

LOWDIN_POPULATION

### `LOWDIN_POPULATION`

> **运行 Löwdin 布居分析。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不计算 Löwdin 布居。
>     * TRUE
>     * 运行 Löwdin 布居分析。
> * **建议**: 无

## 10.2.2.2 由静电势导出的电荷

比 Mulliken 或 Löwdin 电荷更稳定的替代方案是由静电势（electrostatic potential, ESP）导出的电荷，

 其中有若干不同的类型。所谓“ChElPG”电荷，[[159]](../bib_references/bib.md#bib152)

其名称是“Charges from the Electrostatic Potential on a Grid”（由网格上静电势导出的电荷）的首字母缩略词，在各种基于 ESP 的电荷方案中可能是概念上最直接的。根据定义，ChElPG 原子电荷是能够对范德华区域之外的实空间网格上评估的分子静电势提供最佳拟合的电荷，且须满足 ChElPG 电荷之和等于分子电荷这一约束条件。**Q-Chem** 对 ChElPG 算法的实现与 Breneman 和 Wiberg 最初描述的算法[[159]](../bib_references/bib.md#bib152)
 略有不同，**Q-Chem** 使用平滑函数对网格点进行加权，以确保 ChElPG 电荷随原子核位移而连续变化。[[560]](../bib_references/bib.md#bib574)
（但对于特定几何构型，电荷的数值与使用原始算法所得结果非常接近。）另需注意，Breneman-Wiberg 方法使用笛卡尔网格，对于大体系开销昂贵，尤其是当 ChElPG 电荷用于 QM/MM-Ewald 计算时。[[590]](../bib_references/bib.md#bib612)

因此，还提供了一种基于原子中心 Lebedev 网格的替代程序，[[590]](../bib_references/bib.md#bib612)
 它用少得多的网格点即可给出非常相似的电荷。若要使用 Lebedev 网格实现，必须设置 *$rem* 变量 CHELPG_H 和 CHELPG_HA，分别指定氢原子和重原子的 Lebedev 网格点数。

CHELPG

### `CHELPG`

> **控制是否计算 CHELPG 电荷。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不计算 ChElPG 电荷。
>     * TRUE
>     * 计算 ChElPG 电荷。
> * **建议**: 如需要则设为 TRUE。对于大分子，计算 ChElPG 电荷会带来一定开销，尤其当网格点数很大时。注意，若要获得 ChElPG 电荷，POP_MULLIKEN 也必须设为 TRUE（即默认值）。

CHELPG_HEAD

### `CHELPG_HEAD`

> **设置 ChElPG 网格的“头部空间”（head space）（径向范围）。159 Breneman C. M., Wiberg K. B. J. Comput. Chem. (1990) , 11 , pp. 361 . Link**
>
> * **类型**: `INTEGER`
> * **默认值**: `28`
> * **选项**:
>     * $N$
>     * 对应于
>     * $N/10$
>     * 的头部空间，单位为 Å。
> * **建议**: 使用默认值，即 Breneman 和 Wiberg 推荐的值。159 Breneman C. M., Wiberg K. B. J. Comput. Chem. (1990) , 11 , pp. 361 . Link

CHELPG_DX

### `CHELPG_DX`

> **设置传统笛卡尔 ChElPG 网格的矩形网格间距，或同心 Lebedev 壳层之间的间距（当同时指定变量 CHELPG_HA 和 CHELPG_H 时）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `6`
> * **选项**:
>     * $N$
>     * 对应于
>     * $N/20$
>     * 的网格间距，单位为 Å。
> * **建议**: 使用默认值，它对应于 Breneman 和 Wiberg 的“稠密网格”（dense grid），159 Breneman C. M., Wiberg K. B. J. Comput. Chem. (1990) , 11 , pp. 361 . Link ，除非代价过高，此时可选择更大的值。注意，此默认值是针对笛卡尔网格而非 Lebedev 网格设定的。对于 Lebedev 网格，通常可以使用更大的值。

CHELPG_HA

### `CHELPG_HA`

> **设置重原子（非氢原子）所使用的 Lebedev 网格。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $N$
>     * 每个原子使用
>     * $N$
>     * 个 Lebedev 点。
> * **建议**: $N$ 必须是 Lebedev 网格已定义的取值之一；参见 Table 5.2 。

CHELPG_H

### `CHELPG_H`

> **设置氢原子所使用的 Lebedev 网格。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $N$
>     * 每个原子使用
>     * $N$
>     * 个 Lebedev 点。
> * **建议**: $N$ 必须是 Lebedev 网格已定义的取值之一；参见 Table 5.2 。此外，它必须始终小于或等于 CHELPG_HA 。若更大，将自动设置为 CHELPG_HA 的值。

另一组与之密切相关的基于 ESP 的电荷是所谓“Merz-Kollman”电荷，[[1258]](../bib_references/bib.md#bib1310)

在该方法中，以原子为中心的电荷通过拟合来再现少量同心原子球面（或分子的范德华表面）上的 ESP，就此而言，Merz-Kollman 算法与 **Q-Chem** 基于 Lebedev 网格的 ChElPG 电荷实现类似。**Q-Chem** 计算 Merz-Kollman 电荷的算法使用由原子球构成的表面，其半径分别为原子范德华半径的 1.4$\times$、1.6$\times$、1.8$\times$ 和 2.0$\times$。
在每个表面上布置 Lebedev 网格点或球谐函数网格点，这些网格点之间的默认间距为 0.5 Å。
这些电荷可以被约束以满足“化学对称性”，即化学等价的原子具有相同的原子电荷值，从而得到所谓“RESP”电荷。[[270]](../bib_references/bib.md#bib271)

**注意：

1.

当 ESP_CHARGES 和 RESP_CHARGES 同时开启时，仅计算 RESP 电荷

2.

ESP_CHARGES 和 RESP_CHARGES 均可用于从 CIS 或 TDDFT 计算（RPA 或 TDA）中计算任意单重激发态的原子电荷。对于激发态布居分析，建议开启 CIS_RELAXED_DENSITY。
从物理上看，外部静电环境感受到的应当是弛豫后的激发态密度，而非未弛豫的密度。

**

ESP_CHARGES

### `ESP_CHARGES`

> **控制是否计算基于 Merz-Kollman ESP 导出的电荷。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * 1
>     * 在每个原子周围使用 Lebedev 网格点。
>     * 2
>     * 在每个原子周围使用球谐函数网格点。
> * **建议**: NONE

RESP_CHARGES

### `RESP_CHARGES`

> **控制是否计算 RESP 电荷，其中化学等价的原子被约束为具有相同的原子电荷值。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * 1
>     * 在每个原子周围使用 Lebedev 网格点。
>     * 2
>     * 在每个原子周围使用球谐函数网格点。
> * **建议**: NONE

ESP_SURFACE_DENSITY

### `ESP_SURFACE_DENSITY`

> **控制范德华（vdW）表面上网格点之间的间距。**
>
> * **类型**: `INTEGER`
> * **默认值**: `500`
> * **选项**:
>     * $n$
>     * 间距为
>     * $0.001\times n$
>     * （单位为 Å）
> * **建议**: 默认值对应 0.5 Å 间距。

## 10.2.2.3 Hirshfeld 电荷

Hirshfeld 布居分析[[583]](../bib_references/bib.md#bib606)
 为分子中的原子电荷提供了另一种定义：

<a id="eq:hirshfeld"></a>
$$
q_{A}=Z_{A}-\int d{\bf r}\left(\frac{\rho^{0}_{A}({\bf r})}{\sum_{B}\rho^{0}_{B}({\bf r})}\right)\rho({\bf r}), \tag{10.5}
$$

其中 $Z_{A}$ 是 $A$ 的核电荷，$\rho^{0}_{B}$ 是原子 $B$ 的孤立基态原子密度，$\rho$ 是分子密度。求和遍历分子中的所有原子。因此，计算 Hirshfeld 电荷需要对孤立原子密度（promolecule，预分子）以及整个分子进行自洽计算。在 SCF 计算之前，先构造 Hirshfeld 原子密度矩阵。SCF 收敛后，使用数值求积来评估式 ([10.5](#eq:hirshfeld)) 中的积分。由于对带电分子而言合适参考态的选择具有歧义（此类任务将会崩溃），故使用电中性基态原子。由于采用数值积分（默认求积网格），电荷之和可能不严格为零。可以使用更大的 XC_GRID 来提高积分精度，但 Hirshfeld 电荷的大小应在很大程度上与网格选择无关。

与其他电荷方案或实验数据相比，使用 Hirshfeld 电荷得到的电荷（及相应的分子偶极矩）通常被低估。为纠正这一点，Marenich *et al.* 提出了“电荷模型 5”（Charge Model 5, CM5），[[911]](../bib_references/bib.md#bib945)
 它采用一组参数将 Hirshfeld 电荷映射为对静电势更合理的表征。与原始 Hirshfeld 电荷相比，CM5 电荷通常给出更准确的偶极矩，而额外代价可以忽略。CM5 适用于由 H–Ca、Zn、Ge–Br 和 I 元素组成的分子。

在 Hirshfeld 方案中使用电中性基态原子来定义预分子密度并没有严格的理论基础，而且构造预分子密度也没有唯一的方法。例如，Li${}^{0}$F${}^{0}$、Li${}^{+}$F${}^{-}$ 或 Li${}^{-}$F${}^{+}$ 都可以用来构造 LiF 的预分子密度。
此外，对带电分子而言合适参考态的选择具有歧义，因此 **Q-Chem** 对任何带净电荷的分子都禁用了 Hirshfeld 分析。针对带电分子的一种解决方案是使用 Bultinck *et al.* 提出的迭代式“Hirshfeld-I”划分方案，[[170]](../bib_references/bib.md#bib164)
 其中参考态不是预先定义的，而是通过自洽方式确定，从而消除了任意性。Hirshfeld-I 划分最终的自洽参考态通常由非整数的原子布居组成。

在第一次迭代中，Hirshfeld-I 方法使用中性原子密度（与原始 Hirshfeld 方案相同），即 $\rho_{i}^{0}(\mathbf{r})$，其电子布居为 $N_{i}^{0}=\int d\mathbf{r}\,\rho_{i}^{0}(\mathbf{r})=Z_{i}$。
由此得到

<a id="eq:hirshc"></a>
$$
q_{i}^{1}=Z_{i}-\int d\mathbf{r}\left(\frac{\rho_{i}^{0}(\mathbf{r})}{\sum_{i}^{A}\rho_{i}^{0}(\mathbf{r})}\right)\rho(\mathbf{r})=Z_{i}-N_{i}^{1} \tag{10.6}
$$

为第一次迭代上的电荷。原子 $i$ 的新电子布居（电子数）为 $N_{i}^{1}$，由预分子布居 $N_{i}^{0}$ 导出。
然后计算满足 $N_{i}^{1}=\int d\mathbf{r}\,\rho_{i}^{1}(\mathbf{r}_{1})$ 的新孤立原子密度，并在下一次迭代中用它们构造预分子密度。一般地，第 $k$ 次迭代中原子 $i$ 的新权重函数为

<a id="eq:weight2"></a>
$$
w_{i,\rm{HI}}^{k}(\mathbf{r})=\frac{\rho_{i}^{k-1}(\mathbf{r})}{\sum\limits_{i\in A}\rho_{i}^{k-1}(\mathbf{r})}\;. \tag{10.7}
$$

具有相应分数电子数 $N_{i}^{k}$ 的原子密度 $\rho_{i}^{k}(\mathbf{r})$ 通过对同一原子的 $\rho_{i}^{0,\lfloor N_{i}^{k}\rfloor}(\mathbf{r})$ 与 $\rho_{i}^{0,\lceil N_{i}^{k}\rceil}(\mathbf{r})$ 进行线性插值得到：[[170]](../bib_references/bib.md#bib164)

<a id="eq:interpolate"></a>
$$
\rho_{i}^{k}(\mathbf{r})=\left(\lceil N_{i}^{k}\rceil-N_{i}^{k}\right)\,\rho_{i}^{0,\lfloor N_{i}^{k}\rfloor}(\mathbf{r})+\left(N_{i}^{k}-\lfloor N_{i}^{k}\rfloor\right)\,\rho_{i}^{0,\lceil N_{i}^{k}\rceil}(\mathbf{r})\;, \tag{10.8}
$$

其中 $\lfloor N_{i}^{k}\rfloor$ 和 $\lceil N_{i}^{k}\rceil$ 表示夹住 $N_{i}^{k}$ 的两个整数。式 ([10.8](#eq:interpolate)) 右侧的两个原子密度由预先计算的密度 $\rho_{i}^{0,Z_{A}-2},\rho_{i}^{0,Z_{A}-1},\ldots,\rho_{i}^{0,Z_{A}+2}$ 获得。（也就是说，该方法在方程中使用中性原子密度，以及该元素单电荷与双电荷阳离子和阴离子的密度。）当原子布居在相邻迭代之间的变化不显著时，例如 $|N_{i}^{k}-N_{i}^{k-1}|<0.0005e$，Hirshfeld-I 迭代即达到收敛。[[170]](../bib_references/bib.md#bib164)

与原始 Hirshfeld 方案相比，迭代式 Hirshfeld 方案通常给出更合理的电荷。以 LiF 为例，原始 Hirshfeld 方案预测的原子电荷为 $\pm$0.57，而迭代方案将这些电荷增大至 $\pm$0.93。式 ([10.6](#eq:hirshc)) 中的积分通过数值求积评估，每次 Hirshfeld-I 迭代的代价与计算原始 Hirshfeld 电荷的代价相等。进行 Hirshfeld-I 分析时，必须将 *$rem* 变量 POINT_GROUP_SYMMETRY 设为 FALSE。

HIRSHFELD

### `HIRSHFELD`

> **控制是否运行 Hirshfeld 布居分析。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 计算 Hirshfeld 布居。
>     * FALSE
>     * 不计算 Hirshfeld 布居。
> * **建议**: 无

HIRSHFELD_READ

### `HIRSHFELD_READ`

> **强制从磁盘读入孤立原子密度的开关。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 从磁盘读入先前 Hirshfeld 计算产生的孤立原子密度。
>     * FALSE
>     * 生成新的孤立原子密度。
> * **建议**: 除非体系很大，否则使用默认值。注意，原子的顺序及所用基组应与先前的 Hirshfeld 计算保持一致（坐标可以改变）。先前的计算应使用 -save 选项运行。

HIRSHFELD_SPHAVG

### `HIRSHFELD_SPHAVG`

> **控制预分子（pro-molecule）中的原子密度是否应进行球平均。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **选项**:
>     * TRUE
>     * 对原子密度进行球平均。
>     * FALSE
>     * 不进行球平均。
> * **建议**: 使用默认值。

CM5

### `CM5`

> **控制是否运行 CM5 布居分析。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 计算 CM5 布居。
>     * FALSE
>     * 不计算 CM5 布居。
> * **建议**: 无

HIRSHITER

### `HIRSHITER`

> **控制是否运行迭代式 Hirshfeld 布居分析。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 计算迭代式 Hirshfeld 布居。
>     * FALSE
>     * 不计算迭代式 Hirshfeld 布居。
> * **建议**: 无

HIRSHITER_THRESH

### `HIRSHITER_THRESH`

> **控制迭代式 Hirshfeld 布居分析的收敛判据。**
>
> * **类型**: `INTEGER`
> * **默认值**: `5`
> * **选项**:
>     * $N$
>     * 对应于
>     * $N/10000$
>     * 的收敛判据，单位为
>     * $e$
>     * 。
> * **建议**: 使用默认值，即文献 170 Bultinck P. et al. J. Chem. Phys. (2007) , 126 , pp. 144111 . Link 中推荐的值。

???+ example "示例 10.1: $\rm F^{-}(H_{2}O)$ 的迭代式 Hirshfeld 布居分析"
    ```qchem
    $molecule
     -1  1
      O     1.197566    -0.108087     0.000000
      H     1.415397     0.827014     0.000000
      H     0.134830    -0.084378     0.000000
      F    -1.236389     0.012239     0.000000
    $end
    
    $rem
    point_group_symmetry False
       METHOD      B3LYP
       BASIS       6-31G*
       HIRSHITER   true
    $end
    ```
