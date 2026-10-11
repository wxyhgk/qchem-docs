---
title: "9.1.2 理论背景"
---

## 9.1.2 理论背景

（2026 年 7 月 4 日）

几何优化（Geometry Optimization）是指在分子势能面（Potential Energy Surface）上确定驻点（Stationary Point），主要是极小点和过渡态（Transition State）的过程。这是一个迭代过程，需要在每个优化循环中计算能量、梯度（Gradient）以及（可能的）Hessian 矩阵。能量、梯度和 Hessian 信息被用来计算一个优化步 $\mathbf{h}$，该步长使几何结构向目标驻点靠近。这一过程反复进行，直到达到收敛。几何优化的艺术在于如何计算步长 $\mathbf{h}$，以便用尽可能少的循环实现收敛。

考虑势面上某一点 $\mathbf{x}_{0}$ 处的能量 $E(\mathbf{x}_{0})$。我们可以借助 Taylor 级数将附近一点 $\mathbf{x}=\mathbf{x}_{0}+\mathbf{h}$ 处的能量表示为

<a id="eq:a1"></a>

$$
E(\mathbf{x}_{0}+\mathbf{h})=E(\mathbf{x}_{0})+\mathbf{h}^{t}\left(\frac{dE(\mathbf{x}_{0})}{d\mathbf{x}}\right)+\frac{1}{2}\mathbf{h}^{t}\left(\frac{d^{2}E(\mathbf{x}_{0})}{d\mathbf{x}_{1}d\mathbf{x}_{2}}\right)\mathbf{h}+\cdots \tag{9.1}
$$

如果我们知道能量泛函 $E(\mathbf{x})$ 的精确形式及其所有导数，就可以从当前点 $\mathbf{x}_{0}$ 直接移动到某个驻点（*即*，我们将确切知道步长 $\mathbf{h}$ 应当为何值）。由于我们通常充其量只知道 $E(\mathbf{x})$ 的低阶导数，因此可以对 Taylor 级数关于 $\mathbf{h}$ 求导，只保留右端的前几项，并将左端的 $dE(\mathbf{x}_{0}+\mathbf{h})/d\mathbf{h}$ 设为零（即在真正驻点处它所应取的值），从而得到

<a id="eq:a2"></a>

$$
\frac{dE(\mathbf{x}_{0}+\mathbf{h})}{d\mathbf{h}}=\frac{dE(\mathbf{x}_{0})}{d\mathbf{x}}+\left(\frac{d^{2}E(\mathbf{x}_{0})}{d\mathbf{x}_{1}d\mathbf{x}_{2}}\right)\mathbf{h}+\mbox{higher terms (ignored)} \tag{9.2}
$$

由此可得

<a id="eq:a3"></a>

$$
\mathbf{h}=-\mathbf{H}^{-1}\mathbf{g} \tag{9.3}
$$

其中

<a id="eq:a4"></a>

$$
\frac{dE}{d{\rm{\bf x}}}\equiv{\rm{\bf g}}\mbox{ (gradient vector),}\qquad\frac{d^{2}E}{d{\rm{\bf x}}_{\rm 1}d{\rm{\bf x}}_{\rm 2}}\equiv{\rm{\bf H}}\mbox{ (Hessian matrix)} \tag{9.4}
$$

式 ([9.3](#eq:a3)) 称为 Newton-Raphson 步。它是量子化学中几乎所有几何优化算法的核心组成部分。

上述推导假设了一阶导数（梯度）和二阶导数（Hessian）信息都是精确的。**Q-Chem** 支持的大部分方法都提供解析梯度，但解析二阶导数的可用性较差，参见表 [9.2](topic_ts_Overview.md#table:grad_and_hess)。此外，即使可以得到解析二阶导数，使用它们也未必有利，因为其计算代价高昂，而没有精确 Hessian 同样可以进行高效的优化。实践中一个极佳的折衷方案是从一个近似的 Hessian 矩阵出发，并利用优化过程中生成的梯度和位移信息对其进行更新。这样几乎不花额外代价就能“改进”初始 Hessian。将式 ([9.3](#eq:a3)) 与近似 Hessian 结合使用，称为拟 Newton-Raphson（Quasi Newton-Raphson）步。

Hessian 矩阵的性质（尤其是其特征值结构）在优化的成功与否中起着关键作用。势面上所有驻点的梯度矢量都为零，然而驻点的特征（*即*它对应何种类型的结构）是由 Hessian 矩阵决定的。对 Hessian 进行对角化可得到能量面上一组相互正交的方向（特征矢量）以及沿这些方向的曲率（特征值）。在局部极小点（对应势能面上的势阱）处，沿所有这些方向的曲率都必须为正，这表明沿其中任一方向施加微小位移都会使能量升高。而在过渡态处，沿某一个方向的曲率为负（*即*能量取极大值），但沿所有其他方向的曲率为正。因此，一个驻点若要成为过渡态，该点处的 Hessian 矩阵必须具有一个且仅有一个负特征值；而对于极小点，Hessian 必须具有全部正特征值。在后一种情况下，该 Hessian 被称为*正定（positive definite）*的。在搜索极小点时，保证 Hessian 矩阵正定非常重要；事实上，除非 Hessian 正定，否则无法保证由式 ([9.3](#eq:a3)) 预测的步长真的会降低能量。类似地，在过渡态搜索中，Hessian 必须有一个负特征值。在极小化过程中保持正确的 Hessian 特征值结构并不困难，但在过渡态搜索时却可能成为问题。

在对角化的 Hessian 表示下，Newton-Raphson 步可以写成

<a id="eq:a5"></a>

$$
\mathbf{h}=-\sum_{i}\left(\frac{F_{i}}{b_{i}}\right){\mathbf{u}_{i}} \tag{9.5}
$$

其中 $\mathbf{u}_{i}$ 和 $b_{i}$ 是 Hessian 矩阵 $\mathbf{H}$ 的特征矢量和特征值，$F_{i}=\mathbf{u}_{i}^{t}\mathbf{g}$ 是 $\mathbf{g}$ 沿局域方向（本征模式）$\mathbf{u}_{i}$ 的分量。正如 Simons 等人[[1256]](../bib_references/bib.md#bib1309)所讨论的，

Newton-Raphson 步可以看作是在具有正特征值的方向 $\mathbf{u}_{i}$ 上做极小化，而在具有负特征值的方向上做极大化。因此，如果用户在搜索极小点且 Hessian 矩阵正定，那么 Newton-Raphson 步是合适的，因为它试图同时在所有方向上进行极小化。然而，如果 Hessian 有一个或多个负特征值，那么基本的 Newton-Raphson 步就不适合极小点搜索，因为它将在一个或多个方向上做极大化而非极小化。同样的论证也完全适用于过渡态搜索，只不过此时 Hessian 必须有一个负特征值，因为用户需要在某一个方向上做极大化。但必须*只有*一个负特征值。正定的 Hessian 对过渡态搜索来说是灾难性的，因为 Newton-Raphson 步会朝着极小点前进。

如果确实处于势面上具有正确 Hessian 特征的区域，那么基于 Newton-Raphson 步的谨慎搜索几乎总能引导至正确类型的驻点。然而，这只有在 Hessian 精确时才成立。如果 Hessian 只是近似更新的，那么除非在更新过程中非常小心，否则无法保证 Hessian 的特征值结构能从一个循环保持到下一个循环。确实存在一些“保证”保持 Hessian 正定性的更新程序（或者至少在更新可能引入负特征值时警告用户）。这在极小点搜索期间非常有用；但对于过渡态所需的 Hessian 特征保持，尚无此类保证。

除了保持正确 Hessian 特征的困难之外，还有如何在第一步就获得“正确”Hessian 的问题。这一问题在过渡态搜索中尤为突出。对于极小点搜索，可以“猜测”一个合理的正定初始 Hessian（例如，先做一次分子力学（Molecular Mechanics）极小化，并在该极小点处同样用分子力学计算 Hessian），但这一选择对过渡态通常不可行。即使用户在初始几何结构处精确计算了 Hessian，结构的猜测也可能不够准确，昂贵的精确 Hessian 未必具有所需的特征值结构。

因此，尤其是在过渡态搜索中，显然需要一种可以替代基本 Newton-Raphson 步的方法，特别是当 Hessian 矩阵不适用于所寻找的驻点时。

最早能够在过渡态搜索过程中针对 Hessian 特征值结构错误采取纠正措施的算法之一由 Poppinger[[1117]](../bib_references/bib.md#bib1164) 提出，他建议：当 Hessian 全部为正特征值时，不走 Newton-Raphson 步，而是沿最低的 Hessian 模式向上（爬升）行进；而当存在两个或更多负特征值时，则沿对应最小负值（least negative，即绝对值最小的负特征值）的模式向下行进。虽然这一步应当能把用户引导回能量面上正确的区域，但其缺点是用户只沿单一模式做极大化或极小化，这与同时在所有模式上做极大化/极小化的 Newton-Raphson 步不同。另一个缺点是，连续的此类步长往往趋于线性相关，从而降低大多数常用 Hessian 更新的效果。
