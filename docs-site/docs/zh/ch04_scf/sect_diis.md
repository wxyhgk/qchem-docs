---
title: "4.5.3 迭代子空间直接反演法（DIIS）"
---

## 4.5.3 迭代子空间直接反演法（Direct Inversion in the Iterative Subspace, DIIS）

（2026 年 7 月 4 日）

diis

迭代子空间直接反演法（Direct Inversion in the Iterative Subspace, DIIS）[[1136]](../bib_references/bib.md#bib1182)
 的自洽场（SCF）实现利用了 SCF 解的一个性质，即密度矩阵必须与 Fock 矩阵对易：

<a id="eq:DIIS-error"></a>
$$
\mathbf{SPF}-\mathbf{FPS}=\bm{0}\;. \tag{4.30}
$$

因此，在 SCF 迭代循环过程中，在达到自洽之前，可以定义一个误差矢量 **e${}_{i}$**，该矢量除在收敛点外均非零：

<a id="eq446"></a>
$$
{\rm{\bf SP}}_{i}{\rm{\bf F}}_{i}-{\rm{\bf F}}_{i}{\rm{\bf P}}_{i}{\rm{\bf S}}={\rm{\bf e}}_{i} \tag{4.31}
$$

其中 $\mathbf{P}_{i}$ 通过对 $\mathbf{F}_{i}$ 对角化得到，且

<a id="eq447"></a>
$$
\mathbf{F}_{k}=\sum\limits_{j=1}^{k-1}{c_{j}{\rm{\bf F}}_{j}} \tag{4.32}
$$

DIIS 系数 $c_{k}$ 通过对误差矢量进行带约束的最小二乘极小化得到，*即*

<a id="eq448"></a>
$$
Z=\left({\sum\limits_{k}{c_{k}{\rm{\bf e}}_{k}}}\right)\cdot\left({\sum\limits_{k}{c_{k}{\rm{\bf e}}_{k}}}\right) \tag{4.33}
$$

并施加约束 $\sum_{k}c_{k}=1$，从而得到一组维度为 $N+1$ 的线性方程组：

<a id="eq450"></a>
$$
\left({{\begin{array}[]{*{4}c}{{\rm{\bf e}}_{1}\cdot{\rm{\bf e}}_{1}}&\cdots&{{\rm{\bf e}}_{1}\cdot{\rm{\bf e}}_{N}}&1\\
\vdots&\ddots&\vdots&\vdots\\
{{\rm{\bf e}}_{N}\cdot{\rm{\bf e}}_{1}}&\cdots&{{\rm{\bf e}}_{N}\cdot{\rm{\bf e}}_{N}}&1\\
1&\cdots&1&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{c_{1}}\\
\vdots\\
{c_{N}}\\
\lambda\\
\end{array}}}\right)=\left({{\begin{array}[]{*{1}c}0\\
\vdots\\
0\\
1\\
\end{array}}}\right)\;. \tag{4.34}
$$

收敛判据要求第 $N$ 个误差矢量的最大元素低于截止阈值，单点能计算通常取 $10^{-5}$ a.u.，而在几何优化和频率计算中通常收紧至 $10^{-8}$ a.u.。

通过限制用于确定 DIIS 系数的先前 Fock 矩阵的数量，可以提高收敛速度，

<a id="eq451"></a>
$$
\mathbf{F}_{k}=\sum_{j=k-(L+1)}^{k-1}c_{j}\,\mathbf{F}_{j}\;. \tag{4.35}
$$

这里 $L$ 是 DIIS 子空间的大小，通过 *$rem* 变量 DIIS_SUBSPACE_SIZE 设置。当 Fock 矩阵接近自洽时，方程 ([4.34](#eq450)) 中的线性矩阵方程往往会变得严重病态，此时通常需要重置 DIIS 子空间（程序会自动完成这一操作）。

最后，从实践角度我们观察到，当 DIIS 用于 SCF 计算时，它倾向于收敛到全局极小点而非局部极小点。这似乎是因为只有在收敛时，DIIS 迭代中的密度矩阵才具有幂等性。在趋于收敛的过程中，体系并不处于真正的能量面上，这似乎使 DIIS 能够"穿越"波函数空间中的势垒。这通常是一个理想的性质，也正是某些选项的设计动机：在困难情况下，可以先执行若干次 DIIS 迭代，再切换到直接极小化（direct minimization）以收敛到极小点。

以下 *$rem* 变量允许对 DIIS 迭代进行一定程度的自定义：

DIIS_SUBSPACE_SIZE

### `DIIS_SUBSPACE_SIZE`

> **控制 SCF 过程中 DIIS 和/或 RCA 子空间的大小。**
>
> * **类型**: `INTEGER`
> * **默认值**: `15`
> * **可选值**:
>     * 用户自定义
> * **建议**: 无

DIIS_PRINT

### `DIIS_PRINT`

> **控制 DIIS SCF 优化的输出信息。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * 0
>     * 最少量打印输出。
>     * 1
>     * 所选方法以及 DIIS 系数和解。
>     * 2
>     * 在级别 1 基础上增加多极矩的变化。
>     * 3
>     * 在级别 2 基础上增加多极矩。
>     * 4
>     * 在级别 3 基础上增加外推后的 Fock 矩阵。
> * **建议**: 使用默认值

DIIS_ERR_RMS

### `DIIS_ERR_RMS`

> **决定用于衡量误差矢量 $\mathbf{SPF}-\mathbf{FPS}$ 大小的度量标准 [方程 ( 4.30 )]。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **可选值**:
>     * TRUE
>     * 使用误差矢量的均方根（RMS）值来衡量收敛。
>     * FALSE
>     * 改用
>     * $\mathbf{SPF}-\mathbf{FPS}$
>     * 的最大值来衡量。
> * **建议**: 使用默认值。

DIIS_SEPARATE_ERRVEC

### `DIIS_SEPARATE_ERRVEC`

> **控制非限制（unrestricted）计算中 DIIS 误差矢量的优化方式。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * FALSE
>     * 使用合并后的
>     * $\alpha$
>     * 和
>     * $\beta$
>     * 误差矢量。
>     * TRUE
>     * 对
>     * $\alpha$
>     * 和
>     * $\beta$
>     * 空间分别使用独立的误差矢量。
> * **建议**: 在 Q-Chem 中使用 DIIS 时，对于非限制计算有一种方便的优化方式，即将 $\alpha$ 和 $\beta$ 误差矢量求和为单个矢量用于外推。这种方法通常极为有效，但在某些存在对称性破缺的病态体系中，可能导致检测到虚假解：误差矢量的 $\alpha$ 和 $\beta$ 分量恰好相互抵消，给出零 DIIS 误差。这种情况极为罕见，但若有所怀疑，可将本选项设为 = TRUE 进行检查。
