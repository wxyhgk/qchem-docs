---
title: "5.7.5 Tkatchenko-Scheffler van der Waals 模型（TS-vdW）"
---

## 5.7.5 Tkatchenko-Scheffler van der Waals 模型（TS-vdW）

（2026 年 7 月 4 日）

Tkatchenko 和 Scheffler[[1361]](../bib_references/bib.md#bib1421)
 针对 van der Waals（vdW，*即*，色散）相互作用开发了一种成对（pairwise）方法，该方法基于一种缩放（scaling）方案，可得到能够反映局域电子环境的*原位*（*in situ*）原子极化率（$\alpha$）、色散系数（$C_{6}$）以及 vdW 半径（$R_{\text{vdW}}$）。这些参数是通过对自由原子值进行缩放得到的，以体现给定原子的体积如何被其分子环境所改变。分子中原子的尺寸利用电子密度的 Hirshfeld 划分（partition）来确定。（Hirshfeld 或"stockholder"划分法——它同时也可以给出分子中原子电荷的一种度量——在第 [10.2.2](../ch10_properties/subsec_pop_anal.md) 节中描述。）
在由此得到的"TS-vdW"方法中，只需要一个经验性的范围分离参数（$s_{R}$），它依赖于所采用的交换-关联泛函。

!!! note "注意"
    目前参数 $s_{R}$ 仅对 PBE、PBE0、BLYP、B3LYP、revPBE、M06L 和 M06 泛函实现了。


TS-vdW 的能量表达式基于色散能量的成对加和模型，

<a id="eq:ts_energy"></a>

$$
E_{\text{vdW}}^{\text{TS}}=-\frac{1}{2}\sum^{\text{atoms}}_{A}\sum^{\text{A}}_{B\neq A}\left(\frac{C_{6,AB}^{\text{eff}}}{R_{AB}^{6}}\right)f_{\text{damp}}(R_{AB})\;. \tag{5.46}
$$

与 DFT-D 类似，式 ([5.46](#eq:ts_energy)) 中的 $R^{-6}$ 势必须在短程加以阻尼（damp），TS-vdW 模型使用的阻尼函数为

<a id="eq:fdamp_TS-vdW"></a>

$$
f_{\text{damp}}(R_{AB})=\frac{1}{1+\exp\bigl{[}-d(R_{AB}/s_{R}R_{\mathrm{vdW,}AB}^{\text{eff}}-1)\bigr{]}} \tag{5.47}
$$

其中 $d=20$，而经验参数 $s_{R}$ 以依赖于具体泛函的方式优化，用于重现分子间相互作用能[[1361]](../bib_references/bib.md#bib1421)
。若干不同泛函对应的优化值列于表 [5.4](#table:sR_TS-vdW-1)。

|  | PBE | PBE0 | BLYP | B3LYP | revPBE | M06L | M06 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| $s_{R}$ | 0.94 | 0.96 | 0.62 | 0.84 | 0.60 | 1.26 | 1.16 |

表 5.4： 
TS-vdW 模型的优化阻尼参数 [式 ([5.46](#eq:ts_energy))]，取自文献 [[1361]](../bib_references/bib.md#bib1421)
。

式 ([5.46](#eq:ts_energy)) 中的成对系数 $C_{6,AB}^{\text{eff}}$ 由相应的原子参数 $C_{6,A}^{\text{eff}}$ 通过下式构造：

<a id="Ch5.E48"></a>

$$
C_{6,AB}^{\text{eff}}=\frac{2C_{6,A}^{\text{eff}}C_{6,B}^{\text{eff}}}{\bigl{(}\alpha_{B}^{\text{0,eff}}/\alpha_{A}^{\text{0,eff}}\bigr{)}\,C_{6,A}^{\text{eff}}+\bigl{(}\alpha_{A}^{\text{0,eff}}/\alpha_{B}^{\text{0,eff}}\bigr{)}\,C_{6,B}^{\text{eff}}}\;, \tag{5.48}
$$

这与经验性 DFT-D 方法中对 $C_{6,AB}$ 参数所采用的简单几何平均[式 ([5.27](subsec_DFT-D.md#eq:C_6AB))]不同。这些 $C_{6}$ 系数之所以称为"有效"（effective）系数，是因为它们考虑了局域电子环境。如前所述，这是通过对相应的自由原子值进行缩放实现的，*即*，

<a id="Ch5.E49"></a>

$$
C_{6,A}^{\text{eff}}=C_{6,A}^{\text{free}}\left(\frac{V_{A,\text{eff}}}{V_{A,\text{free}}}\right)^{\!2} \tag{5.49}
$$

其中 $V_{A,\text{eff}}$ 是利用 Hirshfeld 划分确定的原子 $A$ 在分子中的有效体积。有效原子极化率和 vdW 半径以类似方式获得：

<a id="Ch5.E50"></a>

$$
\alpha^{\text{0,eff}}_{A}=\alpha_{A}^{\text{0,free}}\left(\frac{V_{A,\text{eff}}}{V_{A,\text{free}}}\right) \tag{5.50}
$$

<a id="Ch5.E51"></a>

$$
R_{\text{vdW,}A}^{\text{eff}}=R_{\text{vdW,}A}^{\text{free}}\left(\frac{V_{A,\text{eff}}}{V_{A,\text{free}}}\right)^{\!1/3}\;. \tag{5.51}
$$

因此，这三个原子特异性参数都是电子密度的泛函。

与 DFT-D 一样，计算式 ([5.46](#eq:ts_energy)) 中色散校正的费用与 DFT 计算本身的费用相比几乎可以忽略。最近的一篇综述[[574]](../bib_references/bib.md#bib590)
 表明，TS-vdW 模型的表演与其他成对色散校正方法相当。例如，对于 S66 数据集[[1161]](../bib_references/bib.md#bib1213)
中的分子间相互作用能，

在 PBE 基础上加入 TS-vdW 校正后，平均绝对误差为 0.4 kcal/mol，最大误差为 1.5 kcal/mol；而单独使用 PBE 时的相应误差为 2.2 kcal/mol（平均值）和 7.2 kcal/mol（最大值）。

在 **Q-Chem** 中实现 TS-vdW 方案的过程中，人们注意到自由原子体积的评估结果与 **FHI-aims** 和 **Quantum Espresso** 程序中的实现存在显著差异，例如，对使用 PBE 泛函的氢原子，$V_{\text{H,free}}$ = 8.68 a.u.（**Q-Chem**）、10.32 a.u.（**FHI-aims**）以及 10.39 a.u.（**Quantum Espresso**）。

这些差异可归因于 Hirshfeld 划分的不同实现方式。在 **Q-Chem** 中，自由原子体积由非限制性（unrestricted）原子 SCF 计算得出，然后进行球平均（spherically averaged）以获得球对称的原子密度。而在 **FHI-aims** 和 **Quantum Espresso** 中，它们是通过求解一维径向 Schrödinger 方程获得的，该方法自动给出球对称的原子密度，但对于开壳层原子必须使用分数占据数。若针对使用 **Q-Chem** 自洽计算的原子体积重新参数化式 ([5.47](#eq:fdamp_TS-vdW)) 中的阻尼函数，这些差异或许可以得到改善，因为其电子结构的表示方式与 **FHI-aims** 或 **Quantum Espresso** 中的相当不同。
然而目前尚未这样做，参数只是简单地取自先前的实现[[1361]](../bib_references/bib.md#bib1421)。

若要在 **Q-Chem** 中复现用 **FHI-aims** 或 **Quantum Espresso** 得到的 TS-vdW 色散能，可以在 **Q-Chem** 中使用本代码并对原子 Hirshfeld 体积施加缩放因子，其推荐值通过将 **Q-Chem** 的原子体积与 **FHI-aims** 所得体积进行线性回归而获得。然而，为了完全的自洽性，不应使用这些缩放因子。

通过设置 TSVDW = TRUE 可请求计算 TS-vdW 色散能。可提供能量及解析梯度。

### `TSVDW`

> **用于开启 TS-vdW 方法的开关**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 不应用 TS-vdW。
>     * `1`: 应用 TS-vdW 方法以获得 TS-vdW 能量。
>     * `2`: 应用 TS-vdW 方法以获得 TS-vdW 能量及相应的梯度。
> * **建议**: 由于 TS-vdW 本身就是一种色散校正形式，因此不应与第 5.7.3 节中描述的任何色散校正联合使用。

### `TSVDW_SR`

> **设置自定义的 $s_{R}$ 阻尼参数值**
>
> * **类型**: `INTEGER`
> * **默认值**: `no default value defined`
> * **选项**:
>     * $n$: 对应于 $n\cdot 10^{-4}$
> * **建议**: 对受支持的泛函使用预定义值，否则请查阅文献 1361 Tkatchenko A., Scheffler M. Phys. Rev. Lett. (2009) , 102 , pp. 073005 。链接及其他相关文献。

### `HIRSHFELD_CONV`

> **为单原子 Hirshfeld 计算设置不同的 SCF 收敛判据**
>
> * **类型**: `INTEGER`
> * **默认值**: `same as SCF_CONVERGENCE`
> * **选项**:
>     * $n$: 对应于 $10^{-n}$
> * **建议**: 5

### `HIRSHMOD`

> **对用于计算缩放 TS-vdW 参数的自由原子体积施加修正因子**
>
> * **类型**: `INTEGER`
> * **默认值**: `4`
> * **选项**:
>     * `0`: 不对 Hirshfeld 体积施加修正因子。
>     * `1`: 对 H 施加内置修正因子。
>     * `2`: 对 H 和 C 施加内置修正因子。
>     * `3`: 对 H、C 和 N 施加内置修正因子。
>     * `4`: 对 H、C、N 和 O 施加内置修正因子。
> * **建议**: 使用默认值

???+ example "示例 5.15: 演示水分子的计算（包含 TS-vdW 能量）的示例输入。"
    ```qchem
    $molecule
       0 1
       O
       H 1 0.95
       H 1 0.95 2 104.5
    $end

    $rem
       BASIS            6-31G*
       METHOD           PBE
       TSVDW            TRUE  !vdw settings
       HIRSHFELD_CONV   6 ! sets SCF_CONVERGENCE for single atom calculations
       HIRSHMOD         4 ! Apply modifiers to the free-atom volumes for H, C, N, and O
    $end
    ```

