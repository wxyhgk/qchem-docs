---
title: "4.5.17 内部稳定性分析与能量极小点的自动修正"
---

## 4.5.17 内部稳定性分析与能量极小点的自动修正

(2026 年 7 月 4 日)

在收敛时，自洽场（SCF）能量相对于分子轨道（MO）系数的变化将处于平稳点。然而，该平稳点并不保证是能量极小点，若并非极小点，则称该波函数是不稳定的。即使波函数处于极小点，该极小点也可能是对波函数形式施加约束所带来的伪象（artifact）。例如，非限制性（Unrestricted）计算通常会给比相应限制性（Restricted）计算更低的能量，这就可能导致 RHF $\rightarrow$ UHF 不稳定性。

根据我们的经验，即使对于像 G2 原子化能这样非常简单的数据集，[[293]](../bib_references/bib.md#bib298)
 使用默认算法（DIIS）也会对若干物种（在某些密度泛函下甚至对单个原子）产生不稳定的解。在这些情况下，若不检查 SCF 解的内部稳定性，就可能导致有缺陷的基准测试结果。虽然一般而言，使用基于梯度的算法（如 GDM）更有可能找到真正的极小点，但它仍然不能完全排除找到不稳定解的可能性。

为了理解可能出现哪些不稳定性，考虑自旋轨道所能具有的最一般形式是很有帮助的：

<a id="eq427"></a>

$$
\chi_{i}({\rm{\bf r}},\zeta)=\psi_{i}^{\alpha}({\rm{\bf r}})\alpha(\zeta)+\psi_{i}^{\beta}({\rm{\bf r}})\beta(\zeta)\;. \tag{4.45}
$$

其中，$\psi_{i}^{\alpha}$ 和 $\psi_{i}^{\beta}$ 是关于笛卡尔坐标 $\mathbf{r}$ 的复值函数，$\alpha$ 和 $\beta$ 是自旋变量 $\zeta$ 的自旋本征函数。几乎普遍采用的第一个约束是假设自旋轨道仅依赖于自旋函数 $\alpha$ 或 $\beta$ 中的一个。于是自旋函数取如下形式

<a id="Ch4.E46"></a>

$$
\chi_{i}(\mathbf{r},\zeta)=\psi_{i}^{\alpha}(\mathbf{r})\alpha(\zeta)\quad\mathrm{or}\quad\chi_{i}(\mathbf{r},\zeta)=\psi_{i}^{\beta}(\mathbf{r})\beta(\zeta)\;. \tag{4.46}
$$

此外，大多数 SCF 计算使用实函数，这对波函数形式施加了额外的约束。如果 SCF 方程存在能量更低的复数解，则波函数表现出实 $\rightarrow$ 复（real $\rightarrow$ complex）不稳定性。通常对自旋函数施加的最后一个约束是 $\psi_{i}^{\alpha}=\psi_{i}^{\beta}$，*i.e.*，自旋向上和自旋向下轨道的空间部分相同。这就得到了人们熟悉的限制性形式体系，如上所述，它可能导致 RHF $\rightarrow$ UHF 不稳定性。关于各种可能不稳定性的更多细节，可参阅文献 [[1227]](../bib_references/bib.md#bib1282)
。

波函数不稳定性可能由多种原因引起，但通常在以下情况下频繁出现

- •

存在能量低于闭壳层单重态的重单双自由基（singlet diradical）态。
- •

存在能量低于最低单重态的三重态。
- •

SCF 方程存在多个解，而计算未能找到能量最低的解。

**Q-Chem**
 以前的稳定性分析程序包存在以下局限：

- •

它仅适用于限制性（闭壳层）和非限制性 SCF 计算。
- •

它需要波函数能量的解析轨道 Hessian 矩阵。
- •

计算在生成修正后的 MO 之后即终止，需要运行第二个作业读入这些轨道并再进行一次 SCF 计算。

GEN_SCFMAN 中内部稳定性分析的实现几乎克服了所有这些缺点。其适用范围已扩展到所有已实现的轨道类型。与旧代码一样，当给定轨道类型和方法（*e.g.* RO/B3LYP）的解析 Hessian 可用时，它以解析方式计算 Davidson 算法[[307]](../bib_references/bib.md#bib311)
 所需的矩阵-向量乘积。若解析 Hessian 不可用，用户仍然可以使用 Sharada *et al.*[[1244]](../bib_references/bib.md#bib1298)
 开发的有限差分矩阵-向量乘积技术进行稳定性分析，该技术只需要梯度（与 Fock 矩阵相关）：

<a id="eq:fd_mat_vec"></a>

$$
\mathbf{Hb}_{1}=\frac{\hat{\bm{\nabla}}E(\mathbf{X}_{0}+\xi\mathbf{b}_{1})-\hat{\bm{\nabla}}E(\mathbf{X}_{0}-\xi\mathbf{b}_{1})}{2\xi} \tag{4.47}
$$

其中 $\mathbf{H}$ 是 Hessian 矩阵，$\mathbf{b}_{1}$ 是试探向量，$\mathbf{X}_{0}$ 表示当前的平稳点，$\xi$ 是有限步长。采用该方法，GEN_SCFMAN 中所有已实现的轨道类型均可进行内部稳定性分析。需要指出的是，由于 **Q-Chem**
 中非局部相关（NLC）泛函（VV10 除外）的二阶导数不可用，默认将使用这种有限差分方法来计算 Hessian-向量乘积。

GEN_SCFMAN 允许在单个作业中执行多次 SCF 计算和稳定性分析，从而能够利用修正后的 MO 自动定位真正的极小点。如果某个 SCF 解被判定为不稳定，则沿能量最低本征向量的方向对 MO 进行位移（并配合线搜索）。若 INTERNAL_STABILITY_ITER > 0，将自动启动一个新的 SCF 计算，以这些修正后的 MO 作为初始猜测。这样的宏循环将持续进行，直到得到稳定的解为止。

**注意：

稳定性分析程序包可用于分析 HF 和 DFT 波函数。
**

## 4.5.17.1 作业控制（Job Control）

### `INTERNAL_STABILITY`

> **在 GEN_SCFMAN 中执行内部稳定性分析。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 收敛后不执行内部稳定性分析。
>     * `TRUE`: 执行内部稳定性分析并生成修正后的 MO。
> * **建议**: 当 SCF 解容易出现不稳定解时开启此项，尤其是对开壳层物种。

### `FD_MAT_VEC_PROD`

> **使用有限差分技术计算 Hessian-向量乘积。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE (当所用泛函包含非局部相关（VV10 除外）时为 TRUE)`
> * **选项**:
>     * `FALSE`: 以解析方式计算 Hessian-向量乘积。
>     * `TRUE`: 使用有限差分计算 Hessian-向量乘积。
> * **建议**: 当解析 Hessian 不可用时设置为 TRUE。注意：对于简单的 R 和 USCF 计算，此项始终可以设置为 FALSE，这表示只有 NLC 部分会用有限差分计算（前提是其解析轨道 Hessian 不可用）。

### `INTERNAL_STABILITY_ITER`

> **在首次稳定性分析之后允许进行的新 SCF 计算的最大次数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0 (若 INTERNAL_STABILITY = TRUE，则自动设为 1)`
> * **选项**:
>     * $n$: 允许进行 $n$ 次新的 SCF 计算。
> * **建议**: 如果 1 次不够（结果仍不稳定），请给出更大的数值。

### `INTERNAL_STABILITY_DAVIDSON_ITER`

> **单次稳定性分析中允许的 Davidson 迭代最大次数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `50`
> * **选项**:
>     * $n$: 最多执行
>     * $n$: 次 Davidson 迭代。
> * **建议**: 使用默认值。

### `INTERNAL_STABILITY_CONV`

> **Davidson 求解器（用于求解最低本征值）的收敛判据。**
>
> * **类型**: `INTEGER`
> * **默认值**: `4 (当 FD_MAT_VEC_PROD = TRUE 时为 3)`
> * **选项**:
>     * $n$: 当残差向量的范数低于 10 ${}^{-n}$ 时终止 Davidson 迭代。
> * **建议**: 使用默认值。

### `INTERNAL_STABILITY_ROOTS`

> **需求解的最低 Hessian 本征值的数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `2`
> * **选项**:
>     * $n$: 求解
>     * $n$: 个最低本征值。
> * **建议**: 使用默认值。

???+ example "示例 4.18: 使用 B97M-V/6-31g 和 GDM 算法对三重态 B ${}_{2}$ 进行非限制性 SCF 计算。当第一个解被判定为鞍点时执行位移，第二次 SCF 计算得到稳定的解。"
    ```qchem
    $molecule
       0 3
       b
       b 1 R
    
       R = 1.587553
    $end
    
    $rem
       METHOD               b97m-v
       BASIS                6-31g
       UNRESTRICTED         true
       THRESH               14
       SCF_FINAL_PRINT      1
       SCF_ALGORITHM        gdm
       SCF_CONVERGENCE      8
       INTERNAL_STABILITY   true  ! turn on internal stability analysis
       FD_MAT_VEC_PROD      false ! use finite-diff for the vv10 part only
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
