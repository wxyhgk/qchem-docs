---
title: "9.1.5 约束优化"
---

## 9.1.5 约束优化

（2026 年 7 月 4 日）

约束优化是指在固定某些参数（*例如*，键长、键角或二面角）的情况下对分子结构进行优化。在量子化学计算中，这传统上是通过 *Z*-矩阵坐标（*Z*-matrix coordinates）实现的，即将所需的参数集写入 *Z*-矩阵中，并简单地从优化空间中省略。1992 年，Baker 提出了一种直接在笛卡尔坐标中进行约束优化的算法。[[65]](../bib_references/bib.md#bib48)
Baker 的算法同时使用了惩罚函数（penalty functions）和经典的拉格朗日乘子（Lagrange multipliers）方法，

其开发初衷是对从图形化模型构建器以笛卡尔坐标集形式获得的分子施加约束。1993 年又进行了一些改进，扩大了可处理约束的范围。[[61]](../bib_references/bib.md#bib49)
**Q-Chem** 包含了该算法的最新版本，并已修改为可直接在离域内坐标（delocalized internal coordinates）中处理约束。[[66]](../bib_references/bib.md#bib51)

约束优化的核心问题是在满足 $m$ 个形如 $C_{i}(\mathbf{x})=0$（$i=\ell,\ldots,m$）的约束条件下，最小化含 $n$ 个变量的函数 $F(\mathbf{x})$。假设 $m<n$，那么也许最好的求解方式（如果实践中可行的话）是利用这 $m$ 个约束方程消去 $m$ 个变量，然后针对剩余的 $n-m$ 个独立变量求解相应的无约束问题。这正是 *Z*-矩阵优化中所发生的过程。这种方法无法用于笛卡尔坐标，因为标准的距离和角度约束是关于相应坐标的非线性函数。例如，在笛卡尔坐标中，原子 $i$ 和 $j$ 之间的距离约束表示为 $(R_{ij}-R_{0})=0$，其中

<a id="Ch9.E17"></a>

$$
R_{ij}=\bigl{[}(x_{i}-x_{j})^{2}+(y_{i}-y_{j})^{2}+(z_{i}-z_{j})^{2}\bigr{]}^{1/2} \tag{9.17}
$$

而 $R_{0}$ 是被约束的距离。显然这无法通过消元来满足。在笛卡尔坐标中能够消去的是各个 $x$、$y$ 和 $z$ 坐标本身，通过这种方式可以将单个原子完全或部分冻结。

内禀约束可以通过引入拉格朗日函数（Lagrangian function）在笛卡尔坐标中处理

<a id="eq:a15"></a>

$$
L(\mathbf{x},\lambda)=F(\mathbf{x})-\sum\limits_{i=1}^{m}{\lambda_{i}C_{i}(\mathbf{x})} \tag{9.18}
$$

该函数取代了无约束情形下的函数 $F(\mathbf{x})$。这里，$\lambda_{i}$ 即所谓的拉格朗日乘子，每个约束 $C_{i}(\mathbf{x})$ 对应一个。对式 ([9.18](#eq:a15)) 分别关于 $\mathbf{x}$ 和 $\lambda$ 求导，可得

<a id="A3.S8.EGx70"></a>

$$
\displaystyle\frac{dL(\mathbf{x},\lambda)}{dx_{j}} \tag{9.19}
$$

在拉格朗日函数的驻点处，有 $\hat{\bm{\nabla}}\mathbf{L}=\bm{0}$，*即*所有 $dL/dx_{j}=0$ 且所有 $dL/d\lambda_{i}=0$。后一个条件意味着所有 $C_{i}(\mathbf{x})=0$，从而所有约束均被满足。因此，找到一组使 $\hat{\bm{\nabla}}\mathbf{L}=\bm{0}$ 成立的取值（$\mathbf{x}$，$\lambda$），即可得到约束优化问题的一个可能解，其方式与找到使 $\mathbf{g}=\hat{\bm{\nabla}}\mathbf{F}=\bm{0}$ 成立的 $\mathbf{x}$ 从而得到相应无约束问题的解完全相同。

拉格朗日函数二阶导数矩阵是无约束优化中海森（Hessian）矩阵的对应物，其表达式为

<a id="eq:a17"></a>

$$
\hat{\nabla}^{2}\mathbf{L}=\left(\begin{array}[]{cc}\displaystyle\frac{d^{2}L(\mathbf{x},\lambda)}{dx_{j}dx_{k}}&\displaystyle\frac{d^{2}L(\mathbf{x},\lambda)}{dx_{j}d\lambda_{i}}\\
\displaystyle\frac{d^{2}L(\mathbf{x},\lambda)}{dx_{j}d\lambda_{i}}&\displaystyle\frac{d^{2}L(\mathbf{x},\lambda)}{d\lambda_{j}d\lambda_{i}}\end{array}\right) \tag{9.21}
$$

其中

<a id="A3.S8.EGx71"></a>

$$
\displaystyle\frac{d^{2}L(\mathbf{x},\lambda)}{dx_{j}dx_{k}} \tag{9.22}
$$

因此，除了无约束函数 $F(\mathbf{x})$ 的标准梯度向量与海森矩阵之外，我们还需要约束函数关于坐标位移的一阶和二阶导数。一旦得到这些量，就可以构造相应的拉格朗日梯度（式 ([9.19](#eq:a16a))）和拉格朗日二阶导数矩阵（式 ([9.21](#eq:a17))），并以类似于标准无约束优化的方式计算优化步长。[[65]](../bib_references/bib.md#bib48)

在拉格朗日乘子方法中，未知乘子 $\lambda_{i}$ 是参数集的固有组成部分。这意味着优化空间由全部 $n$ 个变量 $\mathbf{x}$ 加上全部 $m$ 个拉格朗日乘子 $\lambda$（每个约束对应一个）构成。因此，与相应的无约束情形相比，约束优化问题的总维数 $n+m$ 增加了 $m$。拉格朗日海森矩阵 $\hat{\nabla}^{2}\mathbf{L}$ 比标准（无约束）海森矩阵 $\hat{\nabla}^{2}\mathbf{F}$ 多出 $m$ 个模式。通常发生的情况是，这些附加模式由约束所主导（*即*，它们的最大分量对应于约束的拉格朗日乘子），并且具有负曲率（负的海森本征值）。当我们认识到参数空间中任何破坏约束的运动都可能降低能量时，这一点或许并不令人惊讶。

与寻求海森矩阵本征值全为正的驻点的标准无约束最小化相比，在约束问题中我们要寻找的是拉格朗日函数的一个驻点，在该点拉格朗日海森矩阵具有与约束数目一样多的负本征值（*即*，我们正在寻找一个 $m$ 阶鞍点）。关于在笛卡尔坐标中使用拉格朗日乘子进行约束优化的更多细节和实际应用，参见文献 [[65]](../bib_references/bib.md#bib48)
。

本征向量跟随（eigenvector following）可以在约束优化中以类似于无约束情形的方式实现。考虑一个带有 $m$ 个约束的约束最小化，则式 ([9.11](sect_ef.md#eq:a9a)) 被替换为

<a id="eq:a18a"></a>

$$
\left({{\begin{array}[]{*{4}c}{b_{1}}&&&{F_{1}}\\
&\ddots&{\rm{\bf 0}}&\vdots\\
&{\rm{\bf 0}}&{b_{m}}&{F_{m}}\\
{F_{1}}&\cdots&{F_{m}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{h_{1}}\\
\vdots\\
{h_{m}}\\
1\\
\end{array}}}\right)=\lambda_{p}\left({{\begin{array}[]{*{1}c}{h_{1}}\\
\vdots\\
{h_{m}}\\
1\\
\end{array}}}\right) \tag{9.25}
$$

式 ([9.12](sect_ef.md#eq:a9b)) 被替换为

<a id="eq:a18b"></a>

$$
\left({{\begin{array}[]{*{4}c}{b_{m+1}}&&&{F_{m+1}}\\
&\ddots&{\rm{\bf 0}}&\vdots\\
&{\rm{\bf 0}}&{b_{m+n}}&{F_{m+n}}\\
{F_{m+1}}&\cdots&{F_{m+n}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{h_{m+1}}\\
\vdots\\
{h_{m+n}}\\
1\\
\end{array}}}\right)=\lambda_{n}\left({{\begin{array}[]{*{1}c}{h_{m+1}}\\
\vdots\\
{h_{m+n}}\\
1\\
\end{array}}}\right) \tag{9.26}
$$

其中 $b_{i}$ 现在是 $\hat{\nabla}^{2}\mathbf{L}$ 的本征值，对应的本征向量为 $\mathbf{u}_{i}$，且 $F_{i}=\mathbf{u}_{i}^{t}\hat{\nabla}\mathbf{L}$。这里式 ([9.25](#eq:a18a)) 包含了要求拉格朗日海森本征值为负的 $m$ 个约束模式，而式 ([9.26](#eq:a18b)) 包含了所有其他模式。

式 ([9.25](#eq:a18a)) 和式 ([9.26](#eq:a18b)) 实现了约束最小化的本征向量跟随。约束过渡态搜索可以通过在 $m$ 个约束模式之外再选择一个需要最大化的模式来进行，*即*，搜索拉格朗日函数的 $m+\ell$ 阶鞍点。

应当认识到，在拉格朗日乘子方法中，期望的约束仅在其收敛时才被满足，而在中间几何结构处未必如此。拉格朗日乘子是优化空间的一部分，它们像其他几何参数一样变化，因此约束被满足的程度逐循环变化，在接近收敛时趋近于 100% 满足。这样做带来的一个优点是，与标准 *Z*-矩阵方法不同，约束在初始几何结构中不必被满足。

所施加的约束通常可以被满足到非常高的精度，即 $10^{-6}$ 或更好。然而，在 $0^{\circ}$ 和 $180^{\circ}$ 附近的键约束和二面角约束可能会出现问题，此时与其试图施加单个约束，不如将该角度约束拆分为多个约束。
