---
title: "5.7.3 经验色散校正：DFT-D"
---

## 5.7.3 经验色散校正：DFT-D

（2026 年 7 月 4 日）

2000 年代中期密度泛函理论（Density Functional Theory, DFT）的一项重大进展是人们认识到：首先，半局域密度泛函无法正确描述色散（van der Waals）相互作用，而这一问题直到近期才通过第 [5.7.2](sect_VV10.md) 节讨论的非局域关联泛函得到处理；其次，解决该问题的一个廉价而简单的方案是引入形如 $-C_{6}/R^{6}$ 的经验势，其中 $C_{6}$ 系数为成对原子参数。这一方法作为使用非局域关联泛函的替代方案，被称为*色散校正 DFT*（dispersion-corrected DFT, DFT-D）。[[495]](../bib_references/bib.md#bib506)

目前 **Q-Chem** 中有三种独特的 DFT-D 方法。这些方法通过 *$rem* 变量 DFT_D 来请求，并在下文讨论。

### `DFT_D`

> **控制添加到 DFT 计算中的经验色散校正。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`None`
> * **选项**：
>     * FALSE
>     * （或 0）不应用 DFT-D2、DFT-CHG 或 DFT-D3 方案
>     * EMPIRICAL_GRIMME
>     * 来自 Grimme 的 DFT-D2 色散校正
>     * 494
>     * Grimme S.
>     * J. Comput. Chem.
>     * (2006)
>     * ,
>     * 27
>     * ,
>     * 第 1787 页
>     * .
>     * 链接
>     * EMPIRICAL_CHG
>     * 来自 Chai 和 Head-Gordon 的 DFT-CHG 色散校正
>     * 224
>     * Chai J.-D., Head-Gordon M.
>     * Phys. Chem. Chem. Phys.
>     * (2008)
>     * ,
>     * 10
>     * ,
>     * 第 6615 页
>     * .
>     * 链接
>     * EMPIRICAL_GRIMME3
>     * 来自 Grimme 的 DFT-D3(0) 色散校正（自 Q-Chem 5.0 起已弃用）
>     * D3_ZERO
>     * 来自 Grimme 等人的 DFT-D3(0) 色散校正
>     * et al.
>     * 486
>     * Grimme S. et al.
>     * J. Chem. Phys.
>     * (2010)
>     * ,
>     * 132
>     * ,
>     * 第 154104 页
>     * .
>     * 链接
>     * D3S_ZERO
>     * 来自 Tkachenko 和 Head-Gordon 的 DFT-D3S(0) 色散校正
>     * 1362
>     * Tkatchenko N. V., Head-Gordon M.
>     * J. Chem. Theory Comput.
>     * (2024)
>     * ,
>     * 20
>     * ,
>     * 第 9741 页
>     * .
>     * 链接
>     * D3_BJ
>     * 来自 Grimme 等人的 DFT-D3(BJ) 色散校正
>     * 488
>     * Grimme S., Ehrlich S., Goerigk L.
>     * J. Comput. Chem.
>     * (2011)
>     * ,
>     * 32
>     * ,
>     * 第 1456 页
>     * .
>     * 链接
>     * D3S_BJ
>     * 来自 Tkachenko 和 Head-Gordon 的 DFT-D3S(BJ) 色散校正
>     * 1362
>     * Tkatchenko N. V., Head-Gordon M.
>     * J. Chem. Theory Comput.
>     * (2024)
>     * ,
>     * 20
>     * ,
>     * 第 9741 页
>     * .
>     * 链接
>     * D3_CSO
>     * 来自 Schröder 等人的 DFT-D3(CSO) 色散校正
>     * 1218
>     * Schröder H., Creon A., Schwabe T.
>     * J. Chem. Theory Comput.
>     * (2015)
>     * ,
>     * 11
>     * ,
>     * 第 3163 页
>     * .
>     * 链接
>     * D3_ZEROM
>     * 来自 Smith 等人的 DFT-D3M(0) 色散校正
>     * 1278
>     * Smith D. G. et al.
>     * J. Phys. Chem. Lett.
>     * (2016)
>     * ,
>     * 7
>     * ,
>     * 第 2197 页
>     * .
>     * 链接
>     * D3_BJM
>     * 来自 Smith 等人的 DFT-D3M(BJ) 色散校正
>     * 1278
>     * Smith D. G. et al.
>     * J. Phys. Chem. Lett.
>     * (2016)
>     * ,
>     * 7
>     * ,
>     * 第 2197 页
>     * .
>     * 链接
>     * D3_OP
>     * 来自 Witte 等人的 DFT-D3(op) 色散校正
>     * 1481
>     * Witte J. et al.
>     * J. Chem. Theory Comput.
>     * (2017)
>     * ,
>     * 13
>     * ,
>     * 第 2043 页
>     * .
>     * 链接
>     * D3
>     * 自动选择"最佳"的可用 D3 色散校正
>     * D4
>     * 来自 Caldeweyher 等人的 DFT-D4 色散校正
>     * 178
>     * Caldeweyher E., Bannwarth C., Grimme S.
>     * J. Chem. Phys.
>     * (2017)
>     * ,
>     * 147
>     * ,
>     * 第 034112 页
>     * .
>     * 链接
>     * ,
>     * 179
>     * Caldeweyher E. et al.
>     * J. Chem. Phys.
>     * (2019)
>     * ,
>     * 150
>     * ,
>     * 第 154122 页
>     * .
>     * 链接
>     * ,
>     * 180
>     * Caldeweyher E. et al.
>     * Phys. Chem. Chem. Phys.
>     * (2020)
>     * ,
>     * 22
>     * ,
>     * 第 8499 页
>     * .
>     * 链接
> * **建议**：如果指定的泛函可用，则使用 D4。目前 DFT-D4 仅支持一部分泛函。其中包括 B3LYP、B97、B1LYP、PBE0、PW6B95、M06L、M06、WB97、WB97X、CAMB3LYP、PBE02、PBE0DH、MPW1K、MPWB1K、B1B95、B1PW91、B2GPPLYP、B2PLYP、B3P86、B3PW91、O3LYP、REVPBE、REVPBE0、REVTPSS、REVTPSSH、SCAN、TPSS0、TPSSH、X3LYP、TPSS、BP86、BLYP、BPBE、MPW1PW91、MPW1LYP、PBE、RPBE 和 PW91。

这些方法中最古老的是 DFT-D2，[[494]](../bib_references/bib.md#bib502)
 其经验色散势具有前述形式，即由成对原子的
$-C/R^{6}$ 项组成：

<a id="eqn:C6"></a>

$$
E^{\text{D2}}_{\text{disp}}=-s_{6}\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}\left(\frac{C_{6,AB}}{R_{AB}^{6}}\right)f^{\text{D2}}_{\text{damp}}(R_{AB})\;. \tag{5.25}
$$

该函数在短程（即 $R_{AB}^{-6}$ 发散的区域）通过下式进行阻尼：

<a id="Ch5.E26"></a>

$$
f^{\text{D2}}_{\text{damp}}(R_{AB})=\left[1+e^{-d(R_{AB}/R_{0,AB}-1)}\right]^{-1} \tag{5.26}
$$

这也有助于避免电子关联效应的重复计算，因为短程到中程的关联已通过密度泛函包含在内。（量 $R_{0,AB}$ 是原子 $A$ 和 $B$ 的 van der Waals 半径之和，$d$ 是一个附加参数。）式 ([5.25](#eqn:C6)) 中的主要参数是原子系数 $C_{6,A}$，式 ([5.25](#eqn:C6)) 中的成对参数由它们通过几何平均得到，这与经典力场中的常见做法一致：

<a id="eq:C_6AB"></a>

$$
C_{6,AB}=\bigl{(}C_{6,A}C_{6,B}\bigr{)}^{1/2} \tag{5.27}
$$

DFT-D2 中的总能量自然为 $E_{\text{DFT-D2}}=E_{\text{KS-DFT}}+E^{\text{D2}}_{\rm disp}$。

**Q-Chem** 提供了 DFT-D2，包括解析梯度和频率计算，这要归功于 David Sherrill 团队的贡献。D2 校正可与 **Q-Chem** 中提供的任何密度泛函一起使用，尽管将其与第 [5.7.2](sect_VV10.md) 节讨论的非局域关联泛函合用似乎是不一致的，因而不推荐使用。式 ([5.25](#eqn:C6)) 中的全局参数 $s_{6}$ 由 Grimme 针对四种不同的泛函进行了优化，[[494]](../bib_references/bib.md#bib502)
 并且 **Q-Chem** 使用这些作为默认值：
PBE 对应 $s_{6}=0.75$，BLYP 对应 $s_{6}=1.2$，BP86 对应 $s_{6}=1.05$，B3LYP 对应 $s_{6}=1.05$。对于所有其他泛函，默认 $s_{6}=1$。D2 参数（包括 $C_{6,A}$ 系数和原子 van der Waals 半径）可以通过 *$empirical_dispersion* 输入段进行修改。例如：

> ```qchem
> $empirical_dispersion
>    S6 1.1
>    D 10.0
>    C6 Ar 4.60 Ne 0.60
>    VDW_RADII Ar 1.60 Ne 1.20
> $end
> ```

未显式指定的值默认为 Grimme 优化得到的值。

**注意：**

1.

DFT-D2 仅对至 Xe 为止的元素有定义。

2.

B97-D 是一个交换-关联泛函，当通过 METHOD = B97-D 使用时，它会自动采用 DFT-D2 色散校正。

Grimme 的 DFT-D2 的一个替代方案是 Chai 和 Head-Gordon 的经验色散校正，[[224]](../bib_references/bib.md#bib219)
 它使用与式 ([5.25](#eqn:C6)) 相同的形状，但阻尼函数略有不同：

<a id="A3.S8.EGx18"></a>

$$
\displaystyle f^{\text{CHG}}_{\text{damp}}(R_{AB})=\bigl{[}1+a(R_{AB}/R_{0,AB})^{-12}\bigr{]}^{-1} \tag{5.28}
$$

该版本通过设置 DFT_D = EMPIRICAL_CHG 来激活，阻尼参数 $a$ 由关键字 DFT_D_A 控制。

### `DFT_D_A`

> **控制 Chai–Head-Gordon DFT-D 方案中式 ([5.28](#A3.S8.EGx18)) 的色散校正强度。**
>
> * **类型**：`INTEGER`
> * **默认值**：`600`
> * **选项**：
>     * $n$
>     * 对应于
>     * $a=n/100$
>     * 。
> * **建议**：使用默认值。

**注意：**

1.

DFT-CHG 仅对至 Xe 为止的元素有定义。

2.

$\omega$B97X-D 和 $\omega$M05-D 泛函在通过 METHOD = wB97X-D 或 wM05-D 使用时，会自动采用 DFT-CHG 色散校正。

Grimme 的 DFT-D3 方法[[486]](../bib_references/bib.md#bib504)
 是对其 D2 方案的改进，同样可与 **Q-Chem** 中提供的任何密度泛函一起使用，并附有一阶和二阶解析导数。D3 校正包含一个与 D2 中类似的势，但同时纳入了原子 $C_{8}$ 项：

<a id="eq:D3eqn"></a>

$$
E_{\text{D3,2-body}}=-\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}\left[s_{6}\left(\frac{C_{6,AB}}{R_{AB}^{6}}\right)f_{\text{damp,6}}(R_{AB})+s_{8}\left(\frac{C_{8,AB}}{R_{AB}^{8}}\right)f_{\text{damp,8}}(R_{AB})\right]\;. \tag{5.29}
$$

完整的 D3 色散校正由该项加上一个 Axilrod-Teller-Muto (ATM) 三偶极型三体项构成，因此总 D3 能量为 $E_{\text{DFT-D3}}=E_{\text{KS-DFT}}+E_{\text{D3,2-body}}+E_{\text{ATM,3-body}}$

自 **Q-Chem** 5.0 起，提供了若干 DFT-D3 版本，它们在两个阻尼函数的选择上有所不同。Grimme 的原始表述，[[486]](../bib_references/bib.md#bib504)
 即现被称为"零阻尼"版本 [DFT-D3(0)]，使用如下形式的阻尼函数：

<a id="eq:zero-damping"></a>

$$
f_{\text{damp},n}^{\text{D3(0)}}(R_{AB})=\left[1+6\left(\frac{R_{AB}}{s_{r,n}R_{0,AB}}\right)^{-\beta_{n}}\right]^{-1} \tag{5.30}
$$

其中 $n=6$ 或 8，$\beta_{6}=14$，且 $\beta_{8}=16$。[[486]](../bib_references/bib.md#bib504)
 参数 $R_{0,AB}$
来自原子 van der Waals 半径，$s_{r,6}$ 是与泛函相关的参数，且 $s_{r,8}=1$。通常 $s_{6}$ 被设为 1，而 $s_{8}$ 针对相应泛函进行优化。

较新的 DFT-D3 Becke–Johnson 阻尼版本，[[488]](../bib_references/bib.md#bib505)

即 DFT-D3(BJ)，被设计为当 $R_{AB}\rightarrow 0$ 时有限（但非零）。DFT-D3(BJ) 使用的阻尼函数为：

<a id="eq:bj-damping"></a>

$$
f_{\text{damp},n}^{\text{D3(BJ)}}(R_{AB})=\frac{R_{AB}^{n}}{R_{AB}^{n}+\left(\alpha_{1}R_{0,AB}+\alpha_{2}\right)^{n}} \tag{5.31}
$$

其中 $\alpha_{1}$ 和 $\alpha_{2}$ 是针对每个密度泛函拟合的可调参数。与 DFT-D3(0) 类似，$s_{6}$ 一般固定为 1，而 $s_{8}$ 针对每个泛函进行优化。DFT-D3(BJ) 通常优于原始的 DFT-D3(0) 版本。[[488]](../bib_references/bib.md#bib505)

除这些原始的 DFT-D3(BJ) 和 DFT-D3(0) 变体之外，还实现了改进的 DFT-D3S 版本。[[1362]](../bib_references/bib.md#bib1420)

D3S 方案通过引入依赖于原子对的 $k_{3}$ 重新定义了 C${}_{6}^{AB}$ 系数。原始 DFT-D3 中的 C${}_{6}^{AB}$ 系数通过下式给出：

<a id="eq:d3_c6"></a>

$$
C_{6}^{AB}(CN^{A},CN^{B})=\frac{\sum_{i=1}^{N_{A}}\sum_{j=1}^{N_{B}}C_{6,\text{ref}}^{AB}(CN_{i}^{A},CN_{j}^{B})L_{ij}}{\sum_{i=1}^{N_{A}}\sum_{j=1}^{N_{B}}L_{ij}} \tag{6}
$$

这里，$N_{A}$ 和 $N_{B}$ 分别是原子 A 和 B 的参考分子数目，$C_{6,\text{ref}}^{AB}(CN_{i}^{A},CN_{j}^{B})$ 是参考分子预先计算好的色散系数，而 $CN_{i}^{A}$、$CN_{j}^{B}$ 分别是原子 A 和 B 在各自参考分子中的配位数。项 $L_{ij}$ 根据配位数与其参考点的差异程度来调节权重，在原始 D3 方法中定义为：

<a id="eq:d3_k3"></a>

$$
L_{ij}^{D3}=e^{-k_{3}\left[(CN^{A}-CN_{i}^{A})^{2}+(CN^{B}-CN_{j}^{B})^{2}\right]} \tag{7}
$$

其中 $CN^{A}$ 和 $CN^{B}$ 是原子 A 和 B 在所研究体系中的配位数，$k_{3}$ 固定取值 4。然而，这个固定值可能导致势能面上出现非物理的局部极小点，尤其是在原子的配位数发生变化时。为解决这一问题，D3S 方案引入了依赖于原子对的参数 $k_{3}^{AB}$，得到表达式：

<a id="eq:d3s_k3ab"></a>

$$
L_{ij}^{D3S}=e^{-k_{3}^{AB}\left[(CN^{A}-CN_{i}^{A})^{2}+(CN^{B}-CN_{j}^{B})^{2}\right]} \tag{8}
$$

这里，$k_{3}^{AB}$ 不再是普适常数，而是对每个原子对单独优化，以降低 $C_{6}^{AB}(CN^{A},CN^{B})$ 函数的尖锐程度。这一优化缓解了原始 D3 表述即使在纯有机分子中也可能在势能面上产生的伪局部极小点。D3S 方案中这些成对 $k_{3}^{AB}$ 参数的引入提高了势能面的精度，尤其适用于原子配位数发生显著变化的过程。[[1362]](../bib_references/bib.md#bib1420)

Schröder *et al.*[[1218]](../bib_references/bib.md#bib1272)
 的仅含 $C_{6}$（CSO）方法舍弃了式 ([5.29](#eq:D3eqn)) 中的 $C_{8}$ 项，并使用只含一个参数 $\alpha_{1}$ 的阻尼函数：

<a id="eq:cso-damping"></a>

$$
f_{\text{damp},6}^{\text{D3(CSO)}}(R_{AB})=\frac{C_{AB}^{6}}{R_{AB}^{6}+(2.5\mbox{\AA})^{6}}\left(s_{6}+\frac{\alpha_{1}}{1+\exp[R_{AB}-(2.5\mbox{\AA})R_{0,AB}]}\right)\;. \tag{5.32}
$$

DFT-D3(BJ) 方法被 Smith *et al.*[[1278]](../bib_references/bib.md#bib1331)
 重新参数化，
得到"改进的"DFT-D3(BJ) 方法，即 DFT-D3M(BJ)，其参数化很大程度上依赖于非平衡几何构型。同一批作者还提出了对原始零阻尼校正的改进 DFT-D3M(0)，与 DFT-D3(0) 相比引入了一个额外参数（$\alpha_{1}$）：

<a id="eq:zero-m-damping"></a>

$$
f_{\text{damp},n}^{\text{D3M(0)}}(R_{AB})=\left[1+6\left(\frac{R_{AB}}{s_{r,n}R_{0,AB}}+\alpha_{1}R_{0,AB}\right)^{-\beta_{n}}\right]^{-1}. \tag{5.33}
$$

最后，Witte *et al.*[[1481]](../bib_references/bib.md#bib1543)
 的优化指数（optimized power）方法将指数 $\beta_{6}$ 视为可优化参数，其形式为：

<a id="eq:op-damping"></a>

$$
f_{\text{damp},n}^{\text{D3(op)}}(R_{AB})=\frac{R_{AB}^{\beta_{n}}}{R_{AB}^{\beta_{n}}+(\alpha_{1}R_{0,AB}+\alpha_{2})^{\beta_{n}}}\;. \tag{5.34}
$$

注意 $\beta_{8}=\beta_{6}+2$。

总结这一令人眼花缭乱的 D3 阻尼函数阵列：

- **DFT-D3(0)** 通过设置 DFT_D = D3_ZERO 请求。该模型依赖于四个缩放参数（$s_{6}$、$s_{r,6}$、$s_{8}$ 和 $s_{r,8}$），如式 ([5.30](#eq:zero-damping)) 所定义。
- **DFT-D3(BJ)** 通过设置 DFT_D = D3_BJ 请求。该模型依赖于四个缩放参数（$s_{6}$、$s_{8}$、$\alpha_{1}$ 和 $\alpha_{2}$），如式 ([5.31](#eq:bj-damping)) 所定义。
- **DFT-D3(CSO)** 通过设置 DFT_D = D3_CSO 请求。该模型依赖于两个缩放参数（$s_{6}$ 和 $\alpha_{1}$），如式 ([5.32](#eq:cso-damping)) 所定义。
- **DFT-D3M(0)** 通过设置 DFT_D = D3_ZEROM 请求。该模型依赖于五个缩放参数（$s_{6}$、$s_{8}$、$s_{r,6}$、$s_{r,8}$ 和 $\alpha_{1}$），如式 ([5.33](#eq:zero-m-damping)) 所定义。
- **DFT-D3M(BJ)** 通过设置 DFT_D = D3_BJM 请求。该模型依赖于四个缩放参数（$s_{6}$、$s_{8}$、$\alpha_{1}$ 和 $\alpha_{2}$），如式 ([5.31](#eq:bj-damping)) 所定义。
- **DFT-D3(op)** 通过设置 DFT_D = D3_OP 请求。该模型依赖于五个缩放参数（$s_{6}$、$s_{8}$、$\alpha_{1}$、$\alpha_{2}$ 和 $\beta_{6}$），如式 ([5.31](#eq:bj-damping)) 所定义。

这些阻尼函数中的缩放参数可以通过下文描述的 *$rem* 变量进行修改。或者，也可以简单地设置 DFT_D = D3，如果所选泛函有可用的 D3 色散校正，则会自动选择一个。

**注意：**

1.

DFT-D3(0) 对至 Pu（$Z=94$）为止的元素有定义。

2.

B97-D3(0)、$\omega$B97X-D3、$\omega$M06-D3 泛函在通过设置 METHOD 等于 B97-D3、wB97X-D3 或 wM06-D3 调用时，会自动采用 DFT-D3(0) 色散校正。

3.

调用 DFT-D3 的旧方式，即使用 EMPIRICAL_GRIMME3，仍然受到支持，但不建议使用，因为 D3_ZERO 可实现相同功能，且对相关参数提供额外的精度。

4.

当 DFT_D = D3 时，参数不可覆盖，DFT_D3_3BODY 除外；这是一个以用户友好为目标的选项。当对 **Q-Chem** 中已参数化的泛函使用 EMPIRICAL_GRIMME3 时情况亦如此。当选择 D3_ZERO、D3_BJ 等之一时，如果目标泛函有默认值，**Q-Chem** 会自动填入参数的默认值，但这些默认值仍可被用户覆盖。

### `DFT_D3_S6`

> **式 ([5.29](#eq:D3eqn)) 中的线性参数 $s_{6}$。用于所有形式的 DFT-D3。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100000`
> * **选项**：
>     * $n$
>     * 对应于
>     * $s_{6}=n/100000$
>     * 。
> * **建议**：无

### `DFT_D3_RS6`

> **式 ([5.30](#eq:zero-damping)) 和式 ([5.33](#eq:zero-m-damping)) 中的非线性参数 $s_{r,6}$。用于 DFT-D3(0) 和 DFT-D3M(0)。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100000`
> * **选项**：
>     * $n$
>     * 对应于
>     * $s_{r,6}=n/100000$
>     * 。
> * **建议**：无

### `DFT_D3_S8`

> **式 ([5.29](#eq:D3eqn)) 中的线性参数 $s_{8}$。用于 DFT-D3(0)、DFT-D3(BJ)、DFT-D3M(0)、DFT-D3M(BJ) 和 DFT-D3(op)。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100000`
> * **选项**：
>     * $n$
>     * 对应于
>     * $s_{8}=n/100000$
>     * 。
> * **建议**：无

### `DFT_D3_RS8`

> **式 ([5.30](#eq:zero-damping)) 和式 ([5.33](#eq:zero-m-damping)) 中的非线性参数 $s_{r,8}$。用于 DFT-D3(0) 和 DFT-D3M(0)。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100000`
> * **选项**：
>     * $n$
>     * 对应于
>     * $s_{r,8}=n/100000$
>     * 。
> * **建议**：无

### `DFT_D3_A1`

> **式 ([5.31](#eq:bj-damping))、([5.32](#eq:cso-damping))、([5.33](#eq:zero-m-damping)) 和 ([5.34](#eq:op-damping)) 中的非线性参数 $\alpha_{1}$。用于 DFT-D3(BJ)、DFT-D3(CSO)、DFT-D3M(0)、DFT-D3M(BJ) 和 DFT-D3(op)。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100000`
> * **选项**：
>     * $n$
>     * 对应于
>     * $\alpha_{1}=n/100000$
>     * 。
> * **建议**：无

### `DFT_D3_A2`

> **式 ([5.31](#eq:bj-damping)) 和 ([5.34](#eq:op-damping)) 中的非线性参数 $\alpha_{2}$。用于 DFT-D3(BJ)、DFT-D3M(BJ) 和 DFT-D3(op)。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100000`
> * **选项**：
>     * $n$
>     * 对应于
>     * $\alpha_{2}=n/100000$
>     * 。
> * **建议**：无

### `DFT_D3_POWER`

> **式 ([5.34](#eq:op-damping)) 中的非线性参数 $\beta_{6}$。用于 DFT-D3(op)。必须大于或等于 6 以避免发散。**
>
> * **类型**：`INTEGER`
> * **默认值**：`600000`
> * **选项**：
>     * $n$
>     * 对应于
>     * $\beta_{6}=n/100000$
>     * 。
> * **建议**：无

如需要，三体相互作用项 $E^{(3)}$[[486]](../bib_references/bib.md#bib504)
 必须显式开启。

### `DFT_D3_3BODY`

> **控制是否应用 Grimme 的 DFT-D3 方法中的三体相互作用（参见文献 486 Grimme S. et al. J. Chem. Phys. (2010) , 132 , 第 154104 页 . 链接 中的式 (14)）。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE（或 0）
>     * 不应用三体相互作用项
>     * TRUE
>     * 应用三体相互作用项
> * **建议**：无

近来，Grimme 发表了 D3 的扩展模型 D4。[[178]](../bib_references/bib.md#bib173)
 D4 的主要特征是通过动态原子极化率 $\alpha(i\omega)$ 的 Casimir-Polder 积分生成系数，其中借助原子部分电荷使用了电子密度信息。基准测试结果表明，所提出的 D4 模型显著降低了误差范围。与 D3 模型类似，DFT-D4 色散能量由下式给出：

<a id="eq:D4eqn"></a>

$$
E_{\text{D4,2-body}}=-\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}\left[s_{6}\left(\frac{C_{6,AB}}{R_{AB}^{6}}\right)f_{\text{BJ damp,6}}(R_{AB})+s_{8}\left(\frac{C_{8,AB}}{R_{AB}^{8}}\right)f_{\text{BJ damp,8}}(R_{AB})\right]\;. \tag{5.35}
$$

默认使用 Becke-Johnson 阻尼。依赖于配位数的 $C_{6}^{\text{AB}}$ 系数通过 Casimir-Polder 积分实时获得：

<a id="eq:D4C6"></a>

$$
C_{6}^{\text{AB}}=\sum^{\text{N}^{A,\mathrm{ref}}}_{A,\mathrm{ref}=1}\sum^{\text{N}^{B,\mathrm{ref}}}_{B,\mathrm{ref}=1}\frac{3}{\pi}\int_{0}^{\infty}d\omega\alpha^{A,\mathrm{ref}}(i\omega,z^{A})\times W_{A}^{A,\mathrm{ref}}\alpha^{B,\mathrm{ref}}(i\omega,z^{B})W_{B}^{B,\mathrm{ref}}\;, \tag{5.36}
$$

其中

<a id="eq:D4alpha"></a>

$$
\alpha^{A,\mathrm{ref}}(i\omega,z^{A})=\frac{1}{m}\left[\alpha^{A_{m}H_{n}}(i\omega)-\frac{n}{2}\alpha^{H_{2}}(i\omega)\times\zeta(z^{H_{A},\mathrm{ref}},z^{H_{2}})\right]\zeta(z^{A},z^{A,\mathrm{ref}})\; \tag{5.37}
$$

以及

<a id="eq:D4zeta"></a>

$$
\zeta(z^{A},z^{A,\mathrm{ref}})=ba^{[1.47\text{exp}(z^{A}/z^{A,\mathrm{ref}})\text{log}_{10}(z^{A,\mathrm{ref}}/z^{A})]}\;. \tag{5.38}
$$

$\alpha^{A_{m}H_{n}}$ 表示参考极化率，它代表对称氢化物体系 $A_{m}H_{n}$ 的分子极化率。$W_{A/B}^{A,\mathrm{ref}/B,\mathrm{ref}}$ 是决定所有元素特定参考体系 $N^{A,\mathrm{ref}/B,\mathrm{ref}}$ 贡献的权重因子。$z^{H_{A}}$ 描述参考体系 $A_{m}H_{n}$ 中与原子 A 相连的氢的有效电荷。有效电荷 $z^{A}$ 通过 Mulliken 电荷 $q^{A}$ 自洽地计算：

<a id="eq:D4za"></a>

$$
z^{A}=Z^{A}+q^{A}. \tag{5.39}
$$

系数 $a$ 和 $b$ 的参量化分别用于匹配阳离子的静态极化率和由含时 DFT（TD-DFT）导出的分子色散系数。

### `DFT_D4_S6`

> **线性参数 $s_{6}$。用于 DFT-D4。**
>
> * **类型**：`INTEGER`
> * **默认值**：`针对指定泛函优化的数值`
> * **选项**：
>     * $n$
>     * 对应于
>     * $s_{6}=n/100000000$
>     * 。
> * **建议**：无

### `DFT_D4_S8`

> **线性参数 $s_{8}$。用于 DFT-D4。**
>
> * **类型**：`INTEGER`
> * **默认值**：`针对指定泛函优化的数值`
> * **选项**：
>     * $n$
>     * 对应于
>     * $s_{8}=n/100000000$
>     * 。
> * **建议**：无

### `DFT_D4_S10`

> **线性参数 $s_{10}$。用于 DFT-D4。**
>
> * **类型**：`INTEGER`
> * **默认值**：`针对指定泛函优化的数值`
> * **选项**：
>     * $n$
>     * 对应于
>     * $s_{10}=n/100000000$
>     * 。
> * **建议**：无

### `DFT_D4_A1`

> **非线性参数 $\alpha_{1}$。用于 DFT-D4。**
>
> * **类型**：`INTEGER`
> * **默认值**：`针对指定泛函优化的数值`
> * **选项**：
>     * $n$
>     * 对应于
>     * $\alpha_{1}=n/100000000$
>     * 。
> * **建议**：无

### `DFT_D4_A2`

> **非线性参数 $\alpha_{2}$。用于 DFT-D4。**
>
> * **类型**：`INTEGER`
> * **默认值**：`针对指定泛函优化的数值`
> * **选项**：
>     * $n$
>     * 对应于
>     * $\alpha_{2}=n/100000000$
>     * 。
> * **建议**：无

### `DFT_D4_S9`

> **线性参数 $s_{9}$。用于 DFT-D4。**
>
> * **类型**：`INTEGER`
> * **默认值**：`针对指定泛函优化的数值`
> * **选项**：
>     * $n$
>     * 对应于
>     * $s_{9}=n/100000000$
>     * 。
> * **建议**：无

### `DFT_D4_WF`

> **高斯加权的权重因子。**
>
> * **类型**：`INTEGER`
> * **默认值**：`600000000`
> * **选项**：
>     * $n$
>     * 对应于
>     * $wf=n/100000000$
>     * 。
> * **建议**：使用默认值

### `DFT_D4_GA`

> **电荷缩放**
>
> * **类型**：`INTEGER`
> * **默认值**：`300000000`
> * **选项**：
>     * $n$
>     * 对应于
>     * $ga=n/100000000$
>     * 。
> * **建议**：使用默认值

### `DFT_D4_GC`

> **电荷缩放**
>
> * **类型**：`INTEGER`
> * **默认值**：`200000000`
> * **选项**：
>     * $n$
>     * 对应于
>     * $gc=n/100000000$
>     * 。
> * **建议**：使用默认值

???+ example "示例 5.13：使用自定义参数的 B3LYP-D3(0) 应用于甲烷二聚体。"
    ```qchem
    $comment
       Geometry optimization, followed by single-point calculations using a larger
       basis set.
    $end
    
    $molecule
       0 1
       C       0.000000    -0.000323     1.755803
       H      -0.887097     0.510784     1.390695
       H       0.887097     0.510784     1.390695
       H       0.000000    -1.024959     1.393014
       H       0.000000     0.001084     2.842908
       C       0.000000     0.000323    -1.755803
       H       0.000000    -0.001084    -2.842908
       H      -0.887097    -0.510784    -1.390695
       H       0.887097    -0.510784    -1.390695
       H       0.000000     1.024959    -1.393014
    $end
    
    $rem
       JOBTYPE         opt
       EXCHANGE        B3LYP
       BASIS           6-31G*
       DFT_D           D3_ZERO
       DFT_D3_S6       100000
       DFT_D3_RS6      126100
       DFT_D3_S8       170300
       DFT_D3_3BODY    FALSE
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE         sp
       EXCHANGE        B3LYP
       BASIS           6-311++G**
       DFT_D           D3_ZERO
       DFT_D3_S6       100000
       DFT_D3_RS6      126100
       DFT_D3_S8       170300
       DFT_D3_3BODY    FALSE
    $end
    ```
