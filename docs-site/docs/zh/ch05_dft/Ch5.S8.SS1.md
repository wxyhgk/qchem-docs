---
title: "5.8.1 概述"
---

## 5.8.1 概述

(2026年7月4日)

本节介绍 DFT-C,[[1482]](../bib_references/bib.md#bib1542)
 这是一种针对密度泛函理论（Density Functional Theory, DFT）计算中基组重叠误差（Basis Set Superposition Error, BSSE）的经验校正方法，
它是对 Grimme 的几何反基组（geometrical counterpoise, gCP）校正的改进。[[722]](../bib_references/bib.md#bib754)
 与传统的 Boys-Bernardi 反基组校正（第 [8.9](../ch08_basis/sec_BSSE.md) 节）不同，[[151]](../bib_references/bib.md#bib148)
 DFT-C 校正的计算开销几乎为零（相对于一次 DFT 计算的量级而言），并且它可以同时估计分子间和*分子内*的 BSSE。该校正的形式为

<a id="Ch5.E56"></a>

$$
E_{\text{DFT-C}}=\sigma\sum^{\text{atoms}}_{A}c_{A}\sum^{\text{atoms}}_{B\neq A}g_{AB^{\ast}}^{\text{DFT-C}}(R_{AB})\;h_{AB^{\ast}}(\{A,B,\ldots\}) \tag{5.56}
$$

其中 $g_{AB^{\ast}}^{\text{DFT-C}}$ 是一个带阻尼的两体 BSSE 校正项，

<a id="Ch5.E57"></a>

$$
g_{AB^{\ast}}^{\text{DFT-C}}(R_{AB})=d(R_{AB})\;f_{AB^{\ast}}^{\text{DFT-C}}(R_{AB})+\bigl{[}1-d(R_{AB})\bigr{]}f_{AB^{\ast}}^{\text{DFT-C}}(R_{\text{cov},AB})\;. \tag{5.57}
$$

量

<a id="Ch5.E58"></a>

$$
f_{AB^{\ast}}^{\text{DFT-C}}(R_{AB})=c_{AB}\exp\bigl{(}-\alpha_{AB}R_{AB}^{2}+\beta_{AB}R_{AB}\bigr{)} \tag{5.58}
$$

是未加阻尼的两体 BSSE，而

<a id="Ch5.E59"></a>

$$
d(R_{AB})=\frac{1}{1+k_{1,AB}(R_{AB}/R_{0,AB})^{-k_{2,AB}}} \tag{5.59}
$$

是一个阻尼函数。量 $h_{AB^{\ast}}(\{A,B,...\})$ 是对两体 BSSE 校正的多体校正项，其表达式为

<a id="3b"></a>

$$
h_{AB^{\ast}}(\{A,B,...\})=\left[1+\sum_{C\neq A,B}\frac{N_{C}^{\text{virt}}}{N_{B}^{\text{virt}}}\operatorname{terfc}\left(R_{AC},R_{AB}\right)\operatorname{terfc}\left(R_{BC},R_{AB}\right)\right]^{-1} \tag{5.60}
$$

其中

<a id="terfc"></a>

$$
\operatorname{terfc}(x,y)=1-\frac{1}{2}\big{[}\mathrm{erf}(x+y)+\mathrm{erf}(x-y)\bigr{]}\;. \tag{5.61}
$$

参数 $c_{A}$、$c_{AB}$、$\alpha_{AB}$ 和 $\beta_{AB}$ 依赖于基组，而总体缩放参数 $\sigma$ 则与方法 loosely 相关（即对方法的选择仅有较弱的依赖）。所有这些参数都根据 *$rem* 中指定的方法和基组在内部自动设定。

**注意：

目前 DFT-C 仅支持 def2-SVPD 基组。
**

DFT-C 校正由以下 *$rem* 变量控制：

DFT_C

### `DFT_C`

> **控制是否添加 DFT-C 经验 BSSE 校正。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **可选值**：
>     * FALSE
>     * (或 0) 不应用 DFT-C 校正
>     * TRUE
>     * (或 1) 应用 DFT-C 校正
> * **建议值**：NONE

DFT-C 方法可以应用于任何局域泛函、广义梯度近似（Generalized Gradient Approximation, GGA）或meta-GGA 密度泛函，如下例所示。

???+ example "示例 5.17: 使用 B97M-V-C/def2-SVPD（即在 def2-SVPD 基组下采用带 DFT-C BSSE 校正的 B97M-V 泛函）对甲烷二聚体进行几何优化。"
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
       BASIS              def2-SVPD
       METHOD             b97m-v
       DFT_C              true
    $end
    ```
