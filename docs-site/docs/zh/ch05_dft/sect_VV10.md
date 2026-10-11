---
title: "5.7.2 非局域相关（NLC）泛函"
---

## 5.7.2 非局域相关（NLC）泛函

(July 4, 2026)

从电子密度的角度来看，范德华（van der Waals, vdW）相互作用是一种非局域相互作用：即使是两个互不重叠、球对称的电荷密度（例如两个氩原子），在非共价 A$\cdots$B 复合物中，分子 B 的存在也会在 A 的电荷分布尾部激起"涟漪"，而这正是非共价相互作用的标志。[[265]](../bib_references/bib.md#bib266)
（这正是第 [10.5.6](../ch10_properties/NCI-plots.md) 节所描述的非共价相互作用（Non-Covalent Interaction, NCI）图背后的基本思想：vdW 相互作用表现为在密度本身很小的空间区域中出现较大的密度梯度。）仅依赖于密度及其梯度的半局域广义梯度近似（Generalized Gradient Approximation, GGA）泛函无法描述这种长程、由相关效应诱导的相互作用；而.meta-GGA 至多只能借助密度的拉普拉斯算子和/或动能密度在中程范围内对其进行描述。要对*长程*电子相关给出正确的描述，就需要一个非局域泛函，*即*，具有如下形式的交换-相关势

<a id="Ch5.E23"></a>

$$
v_{\rm c}^{\rm nl}(\mathbf{r})=\int f(\mathbf{r},\mathbf{r^{\prime}})\,d\mathbf{r^{\prime}}\;. \tag{5.23}
$$

这样一来，在某一点 $\mathbf{r^{\prime}}$ 处的微扰（比如由 B 引起）便会在（可能相距很远的）另一点 $\mathbf{r}$ 处（即在 A 上）诱导出交换-相关势。

**Q-Chem** 包含四个此类可描述色散相互作用的泛函：

- •

vdW-DF-04，由 Langreth、Lundqvist 及其合作者发展，[[327]](../bib_references/bib.md#bib331)
 实现方式见文献 [[1417]](../bib_references/bib.md#bib1474)
。
- •

vdW-DF-10（亦称 vdW-DF2），是 vdW-DF-04 的重新参数化版本。[[786]](../bib_references/bib.md#bib822)
- •

VV09，由 Vydrov 与 Van Voorhis 发展[[1414]](../bib_references/bib.md#bib1475)
 并实现[[1415]](../bib_references/bib.md#bib1476)。
- •

VV10，由 Vydrov 与 Van Voorhis 提出。[[1416]](../bib_references/bib.md#bib1477)
- •

rVV10，由 Sabatini 及其合作者提出。[[1192]](../bib_references/bib.md#bib1247)

上述每个泛函均以自洽（Self-Consistent Field, SCF）方式实现，并可提供对核位移的解析梯度。[[1417]](../bib_references/bib.md#bib1474)
 非局域相关由 *$rem* 变量 NL_CORRELATION 控制，其可取以下四个值之一：
vdW-DF-04、vdW-DF-10、VV09 或 VV10。
vdW-DF-04、vdW-DF-10 和 VV09 泛函需与局域自旋密度近似（Local Spin Density Approximation, LSDA）相关组合使用，且该 LSDA 相关必须显式指定。例如，vdW-DF-10 通过以下关键字组合调用：

> ```qchem
> $rem
>    CORRELATION        PW92
>    NL_CORRELATION     vdW-DF-10
>    ...
> $end
> ```

VV10 需与 PBE 相关组合使用，且该 PBE 相关必须显式添加。此外，VV10 还必须指定两个参数 $C$ 和 $b$ 的值（见文献 [[1417]](../bib_references/bib.md#bib1474)
）。这两个参数分别由 *$rem* 变量 NL_VV_C 和
NL_VV_B 控制。例如，若要以 $C=0.0093$ 和 $b=5.9$ 调用 VV10，可使用如下输入：

> ```qchem
> $rem
>    CORRELATION        PBE
>    NL_CORRELATION     VV10
>    NL_VV_C            93
>    NL_VV_B            590
>    ...
> $end
> ```

变量 NL_VV_C 也可用于 VV09，其含义相同。VV09 默认使用 $C=0.0089$（*即*
NL_VV_C 设为 89）。然而在 VV10 中，$C$ 与 $b$ 均无默认值，必须在输入中始终给出。

与局域（LSDA）及半局域（GGA 和 meta-GGA）泛函不同，非局域泛函在计算相关能时需要对空间变量做二重积分，而半局域泛函只需做如 [式 ([5.8](sec_Kohn-Sham.md#E_XC))] 所示的单重积分：

<a id="Ch5.E24"></a>

$$
E_{\rm c}^{\rm nl}=\int v_{\rm c}^{\rm nl}(\mathbf{r})\;d\mathbf{r}=\int f(\mathbf{r},\mathbf{r^{\prime}})\,\rho(\mathbf{r})\;d\mathbf{r}\;d\mathbf{r^{\prime}}. \tag{5.24}
$$

实际上，这一二重积分是在数值求积网格上完成的。[[1417]](../bib_references/bib.md#bib1474)
 默认情况下，$E_{\rm c}^{\rm nl}$ 采用 SG-1 求积网格（见下文第 [5.5.3](sect_standard-quad.md) 节）计算，但可以通过
*$rem* 变量 NL_GRID 请求使用其他网格。非局域能对网格精细程度相当不敏感，因此在大多数情况下使用 SG-1 甚至 SG-0 网格即可，但积分该泛函的其他成分时可能需要更精细的网格。这由第 [5.5.3](sect_standard-quad.md) 节讨论的
XC_GRID 变量控制。

由 Vydrov 与 Van Voorhis 最初发展的两个泛函可通过指定 METHOD = VV10 或
METHOD = LC-VV10 来调用。此外，Mardirossian 与 Head-Gordon 经组合优化得到的泛函（$\omega$B97X-V、B97M-V 和 $\omega$B97M-V）也使用了非局域相关，可通过将 METHOD 设为
wB97X-V、B97M-V 或 wB97M-V 来调用。目前，VV10 代码已经过重写，并新增了核磁共振（Nuclear Magnetic Resonance, NMR）化学屏蔽以及解析二阶导数功能。若希望使用旧代码，请将 USE_LIBNLQ 设为 false。

???+ example "示例 5.12: 使用 rPW86 交换与 VV10 对甲烷二聚体进行几何优化"
    ```qchem
    $molecule
       0 1
       C   0.000000  -0.000140   1.859161
       H  -0.888551   0.513060   1.494685
       H   0.888551   0.513060   1.494685
       H   0.000000  -1.026339   1.494868
       H   0.000000   0.000089   2.948284
       C   0.000000   0.000140  -1.859161
       H   0.000000  -0.000089  -2.948284
       H  -0.888551  -0.513060  -1.494685
       H   0.888551  -0.513060  -1.494685
       H   0.000000   1.026339  -1.494868
    $end
    
    $rem
       JOBTYPE            opt
       BASIS              aug-cc-pVTZ
       EXCHANGE           rPW86
       CORRELATION        PBE
       XC_GRID            2
       NL_CORRELATION     VV10
       NL_GRID            1
       NL_VV_C            93
       NL_VV_B            590
    $end
    ```

在上述示例中，SG-2 网格用于计算 rPW86 交换与 PBE 相关，而 VV10 的非局域部分则使用较粗的 SG-1 网格。此外，上述示例与指定 METHOD = VV10 完全等价。

NL_CORRELATION

### `NL_CORRELATION`

> **指定一个包含非经验色散项的非局域相关泛函。**
>
> * **类型**: `STRING`
> * **默认值**: `None`
> * **可选值**:
>     * None
>     * 不使用非局域相关
>     * vdW-DF-04
>     * vdW-DF-04 的非局域部分
>     * vdW-DF-10
>     * vdW-DF-10 的非局域部分（亦称 vdW-DF2）
>     * VV09
>     * VV09 的非局域部分
>     * VV10
>     * VV10 的非局域部分
> * **建议**: 使用 vdW-DF-04、vdW-DF-10 或 VV09 时，切勿忘记添加 LSDA 相关（推荐使用 PW92）。VV10 应与 PBE 相关配合使用。请谨慎选择交换泛函：HF、rPW86、revPBE 以及部分长程校正（Long-Range Corrected, LRC）交换泛函是推荐的选择之一。

NL_VV_C

### `NL_VV_C`

> **设置 VV09 和 VV10 中的参数 $C$。该参数通过对渐近范德华 $C_{6}$ 系数拟合得到。**
>
> * **类型**: `INTEGER`
> * **默认值**: `89`
> * **可选值**:
>     * $n$
>     * 对应于
>     * $C=n/10000$
> * **建议**: 当使用半局域交换泛函时，推荐 $C=0.0093$。当使用长程校正（LRC）杂化泛函时，推荐 $C=0.0089$。更多细节见文献 1416 Vydrov O. A., Van Voorhis T. J. Chem. Phys. (2010) , 133 , pp. 244103 . Link .

NL_VV_B

### `NL_VV_B`

> **设置 VV10 中的参数 $b$。该参数控制非局域相关能的短程行为。**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值`
> * **可选值**:
>     * $n$
>     * 对应于
>     * $b=n/100$
> * **建议**: 最优取值强烈依赖于所使用的交换泛函。对 rPW86，推荐 $b=5.9$。更多细节见文献 1416 Vydrov O. A., Van Voorhis T. J. Chem. Phys. (2010) , 133 , pp. 244103 . Link .

USE_RVV10

### `USE_RVV10`

> **用于开启 rVV10 非局域相关（NLC）泛函**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * False
>     * True

USE_LIBNLQ

### `USE_LIBNLQ`

> **用于选择是否使用重写后的 VV10 代码库。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
