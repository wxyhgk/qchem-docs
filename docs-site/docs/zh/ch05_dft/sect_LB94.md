---
title: "5.10.2 LB94 方案"
---

## 5.10.2 LB94 方案

(July 4, 2026)

van Leeuwen 和 Baerends 提出了一种渐近修正（asymptotically corrected，AC）交换势[[1386]](../bib_references/bib.md#bib1445)

<a id="eq:vx_LB"></a>

$$
v_{x}^{\text{LB}}=-\beta\left(\frac{x^{2}}{1+3\beta\mbox{sinh}^{-1}(x)}\right) \tag{5.66}
$$

其中 $x=\|\hat{\bm{\nabla}}\rho\|/\rho^{4/3}$ 为约化密度梯度。对于指数衰减的密度，该势在分子体系的渐近区域还原为 $-1/r$。LB94 xc 势由 LDA XC 势与 LB 交换势的线性组合构成：[[1386]](../bib_references/bib.md#bib1445)

<a id="Ch5.E67"></a>

$$
v_{xc}^{\text{LB94}}=v_{xc}^{\text{LDA}}+v_{x}^{\text{LB}}\;. \tag{5.67}
$$

式 ([5.66](#eq:vx_LB)) 中的参数 $\beta$ 是通过对 Be 原子的精确 XC 势进行拟合确定的。如文献 [[213]](../bib_references/bib.md#bib210) 和 [[580]](../bib_references/bib.md#bib602) 所述，对于 TDDFT 计算，只需在基态计算中包含 AC XC 势，随后使用绝热 LDA XC 核进行 TDDFT 计算即可。**Q-Chem** 中 LB94 XC 势的实现采用了这一方法：先使用 LB94 XC 势进行基态计算，然后使用绝热 LDA XC 核进行 TDDFT 计算。这种 TDLDA/LB94 方法已被广泛应用于研究大分子的激发态性质。

由于式 ([5.66](#eq:vx_LB)) 中的 LB 交换势并非来源于某个交换能量泛函的泛函导数，因此改用 Levy-Perdew 位力关系[[811]](../bib_references/bib.md#bib845) 来获取交换能量：

<a id="Ch5.E68"></a>

$$
E_{x}^{\text{LB}}=-\int v_{x}^{\text{LB}}[\rho]\,(\textbf{r})\bigl{[}3\rho(\mathbf{r})+\mathbf{r}\bm{\cdot}\hat{\bm{\nabla}}\rho(\mathbf{r})\bigr{]}\;d\mathbf{r} \tag{5.68}
$$

在 *$rem* 区段中设置 EXCHANGE = LB94 即可请求 LB94 计算。更多的作业控制选项及示例见下文。

### `LB94_BETA`

> **设置 LB94 XC 势的 $\beta$ 参数**
>
> * **类型**：`INTEGER`
> * **默认值**：`500`
> * **可选值**：
>     * $n$
>     * 对应于
>     * $\beta=n/10000$
>     * 。
> * **建议**：使用默认值。

???+ example "示例 5.23: LB94 XC 势在 N ${}_{2}$ 分子中的应用。"
    ```qchem
    $comment
       TDLDA/LB94 calculation is performed for excitation energies.
    $end
    
    $molecule
       0 1
       N    0.0000    0.0000    0.0000
       N    1.0977    0.0000    0.0000
    $end
    
    $rem
       EXCHANGE      lb94
       BASIS         6-311(2+,2+)G**
       CIS_N_ROOTS   30
       RPA           true
    $end
    ```
