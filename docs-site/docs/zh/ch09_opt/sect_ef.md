---
title: "9.1.3 特征矢量跟随（EF）算法"
---

## 9.1.3 特征矢量跟随（Eigenvector-Following, EF）算法

（2026 年 7 月 4 日）

Cerjan 和 Miller[[221]](../bib_references/bib.md#bib217)
 的工作，以及后来 Simons 及其合作者[[1256]](../bib_references/bib.md#bib1309)
 的研究表明，存在一种比直接沿某一条 Hessian 特征矢量行走更好的步长方案。对牛顿-拉夫森（Newton-Raphson）步长做一个简单的修正，就能够引导搜索偏离当前区域，走向具有所需特征（极大/极小性质）的驻点。该步长为

<a id="eq:a5t"></a>

$$
\mathbf{h}=-\sum_{i}\left(\frac{F_{i}}{b_{i}-\lambda}\right)\mathbf{u}_{i} \tag{9.6}
$$

其中 $\lambda$ 可以视为对 Hessian 本征值 $b_{i}$ 的平移参数（shift parameter）。以这种方式对牛顿-拉夫森步长进行缩放，能够有效地使该步长主要（但并非完全——这与 Poppinger 的算法[[1117]](../bib_references/bib.md#bib1164)
 不同）沿某一条局部本征模（eigenmode）方向行进，具体取决于 $\lambda$ 所选取的值。
参考文献 [[221]](../bib_references/bib.md#bib217)
 全部采用式 ([9.6](#eq:a5t)) 这一相同的基本思路，只是在确定 $\lambda$ 取值的方法上有所不同。

EF 算法[[64]](../bib_references/bib.md#bib46)
 采用参考文献 [[72]](../bib_references/bib.md#bib57)
 中提出的有理函数方法，得到形如下的本征值方程

<a id="eq:a6"></a>

$$
\left({{\begin{array}[]{*{2}c}{\rm{\bf H}}&{\rm{\bf g}}\\
{{\rm{\bf g}}^{t}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{\rm{\bf h}}\\
1\\
\end{array}}}\right)=\lambda\left({{\begin{array}[]{*{1}c}{\rm{\bf h}}\\
1\\
\end{array}}}\right) \tag{9.7}
$$

由此可以获得合适的 $\lambda$。将式 ([9.7](#eq:a6)) 展开可得

<a id="eq:a7a"></a>

$$
(\mathbf{H}-\lambda)\mathbf{h}+\mathbf{g}=0 \tag{9.8}
$$

以及

<a id="eq:a7b"></a>

$$
\mathbf{g}^{t}\mathbf{h}=\lambda \tag{9.9}
$$

在 Hessian 的对角表示下，式 ([9.8](#eq:a7a)) 可重新整理为式 ([9.6](#eq:a5t))；而将式 ([9.6](#eq:a5t)) 代入式 ([9.9](#eq:a7b)) 的对角形式，则得到

<a id="Ch9.E10"></a>

$$
\lambda=-\sum_{i}\left(\frac{-F_{i}^{2}}{b_{i}-\lambda}\right) \tag{9.10}
$$

该式可用于迭代求解 $\lambda$。

有理函数优化（Rational Function Optimization, RFO）方程即式 ([9.7](#eq:a6)) 的本征值 $\lambda$ 具有以下重要性质：[[72]](../bib_references/bib.md#bib57)

- •

$\lambda$ 的 $(n+1)$ 个取值将 Hessian 矩阵的 $n$ 个本征值"分隔包围"起来，即 $\lambda_{i}<b_{i}<\lambda_{i+1}$。
- •

在驻点处，式 ([9.7](#eq:a6)) 的某个本征值 $\lambda$ 为零，其余 $n$ 个本征值即为驻点处 Hessian 的本征值。
- •

对于一个 $m$ 阶鞍点（saddle point），那个零本征值恰好将 $m$ 个负 Hessian 本征值与 $(n-m)$ 个正 Hessian 本征值分隔开来。

最后这一性质——正、负 Hessian 本征值的可分隔性——使得可以使用两个平移参数：一个用于能量需要极大化的模式方向，另一个用于能量极小化的方向。对于过渡态（一阶鞍点），用 Hessian 本征模来表示，我们有两个矩阵方程

<a id="eq:a9a"></a>

$$
\left({{\begin{array}[]{*{2}c}{b_{1}}&{F_{1}}\\
{F_{1}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{h_{1}}\\
1\\
\end{array}}}\right)=\lambda_{p}\left({{\begin{array}[]{*{1}c}{h_{1}}\\
1\\
\end{array}}}\right) \tag{9.11}
$$

<a id="eq:a9b"></a>

$$
\left({{\begin{array}[]{*{4}c}{b_{2}}&&&{F_{2}}\\
&\ddots&{\rm{\bf 0}}&\vdots\\
&{\rm{\bf 0}}&{b_{n}}&{F_{n}}\\
{F_{2}}&\cdots&{F_{n}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{h_{2}}\\
\vdots\\
{h_{n}}\\
1\\
\end{array}}}\right)=\lambda_{n}\left({{\begin{array}[]{*{1}c}{h_{2}}\\
\vdots\\
{h_{n}}\\
1\\
\end{array}}}\right) \tag{9.12}
$$

这里假设我们沿最低的 Hessian 模式 $\mathbf{u}_{1}$ 进行极大化。注意，$\lambda_{p}$ 是式 ([9.11](#eq:a9a)) 的最大本征值，它始终为正，并在收敛时趋于零；$\lambda_{n}$ 是式 ([9.12](#eq:a9b)) 的最小本征值，它始终为负，同样在收敛时趋于零。

选取这些 $\lambda$ 值所得到的步长，会尝试沿最低的 Hessian 模式极大化，同时在所有其他模式上极小化。并且无论 Hessian 本征值的结构如何（不同于牛顿-拉夫森步长），它都能做到这一点。随后将这两个平移参数代入式 ([9.6](#eq:a5t))，得到最终的步长

<a id="Ch9.E13"></a>

$$
\mathbf{h}=-\left(\frac{F_{1}}{b_{1}-\lambda_{p}}\right)\mathbf{u}_{1}+\sum\limits_{i=2}^{n}\left(\frac{F_{i}}{b_{i}-\lambda_{n}}\right)\mathbf{u}_{i} \tag{9.13}
$$

若该步长超过允许的最大值，则将其缩小。对于纯极小化，只使用一个平移参数 $\lambda_{n}$，它作用于所有模式。

在式 ([9.11](#eq:a9a))) 和式 ([9.12](#eq:a9b)) 中，我们假设该步长沿最低的 Hessian 模式 $b_{1}$ 极大化，而在所有较高模式上极小化。然而，也可以沿非最低的其他模式进行极大化，这样一来，从同一个初始起点出发，就有可能定位到对应于不同重排/解离路径的过渡态。若改为沿第 $k$ 个模式（而非最低模式）极大化，则式 ([9.11](#eq:a9a)) 替换为

<a id="Ch9.E14"></a>

$$
\left({{\begin{array}[]{*{2}c}{b_{k}}&{F_{k}}\\
{F_{k}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{h_{k}}\\
1\\
\end{array}}}\right)=\lambda_{p}\left({{\begin{array}[]{*{1}c}{h_{k}}\\
1\\
\end{array}}}\right) \tag{9.14}
$$

而此时式 ([9.12](#eq:a9b)) 排除第 $k$ 个模式，但包含最低模式。由于原来的第 $k$ 个模式正是需要负本征值的那个模式，因此在优化过程的某个阶段，该模式最终会变成最低模式。为了保证从一开始所跟随的模式在相邻优化循环之间被平滑地追踪，实际跟随的模式是与上一循环所跟随模式重叠（overlap）最大的那个模式。这一做法称为*模式跟随（mode following）*。更多细节及示例可参见参考文献 [[64]](../bib_references/bib.md#bib46)
。
