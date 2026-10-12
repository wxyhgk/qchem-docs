---
title: "9.1.7 GDIIS 算法"
---

## 9.1.7 GDIIS 算法

(July 4, 2026)

迭代子空间直接求逆（Direct Inversion in the Iterative Subspace, DIIS）最初由 Pulay 提出，用于加速自洽场（Self-Consistent Field, SCF）的收敛。[[1137]](../bib_references/bib.md#bib1183)
 随后，Császár 和 Pulay 将类似的格式用于几何优化，并将其称为 GDIIS。[[285]](../bib_references/bib.md#bib289)
 该方法与通常的拟牛顿（quasi-Newton）类型方法有所不同，在 **Optimize** 模块中作为 EF 算法的替代方案提供。测试表明，其性能与 EF 算法相当（至少对于小体系而言），不过与 EF 算法相比，使用 GDIIS 鲜有优势。

在 GDIIS 中，将此前优化循环中生成的几何结构 $\mathbf{x}_{i}$ 进行线性组合，以求出当前循环中“最佳”的几何结构

<a id="eq:a23"></a>

$$
\mathbf{x}_{n}=\sum\limits_{i=1}^{m}c_{i}\mathbf{x}_{i} \tag{9.33}
$$

其中问题的关键是找出系数 $c_{i}$ 的最佳值。

若用各个几何结构与所求最终几何结构 $\mathbf{x}_{f}$ 之间的偏差来表示该几何结构，*即* $\mathbf{x}_{f}=\mathbf{x}_{i}+\mathbf{e}_{i}$，其中 $\mathbf{e}_{i}$ 为误差向量，那么显然，当条件

<a id="eq:a24"></a>

$$
\mathbf{r}=\sum c_{i}\mathbf{e}_{i} \tag{9.34}
$$

以及

<a id="eq:a25"></a>

$$
\sum{c_{i}}=1 \tag{9.35}
$$

得到满足时，关系式

<a id="Ch9.E36"></a>

$$
\sum c_{i}\mathbf{x}_{i}=\mathbf{x}_{f} \tag{9.36}
$$

同样成立。

真实的误差向量 $\mathbf{e}_{i}$ 自然是未知的。不过，对于近似为二次型的能量函数，它们可以用下式近似：

<a id="Ch9.E37"></a>

$$
\mathbf{e}_{i}=-\mathbf{H}^{-1}\mathbf{g}_{i} \tag{9.37}
$$

其中 $\mathbf{g}_{i}$ 是与几何结构 $\mathbf{x}_{i}$ 对应的梯度向量，$\mathbf{H}$ 是 Hessian 矩阵的近似。对残差向量 $\mathbf{r}$ 的范数（式 ([9.34](#eq:a24))）进行最小化，并附加约束方程（式 ([9.35](#eq:a25))），可得到一个包含 $m+l$ 个线性方程的方程组

<a id="eq:a28"></a>

$$
\left({{\begin{array}[]{c c c c}{B_{11}}&\cdots&{B_{1m}}&1\\
\vdots&\ddots&\vdots&\vdots\\
{B_{m1}}&\cdots&{B_{mm}}&1\\
1&\cdots&1&0\\
\end{array}}}\right)\left({{\begin{array}[]{c}{c_{1}}\\
\vdots\\
{c_{m}}\\
{-\lambda}\\
\end{array}}}\right)=\left({{\begin{array}[]{c}0\\
\vdots\\
0\\
1\\
\end{array}}}\right) \tag{9.38}
$$

其中 $B_{ij}=\langle\mathbf{e}_{i}|\mathbf{e}_{j}\rangle$ 是误差向量 $\mathbf{e}_{i}$ 与 $\mathbf{e}_{j}$ 的内积，$\lambda$ 是拉格朗日乘子（Lagrange multiplier）。

由式 ([9.38](#eq:a28)) 确定的系数 $c_{i}$ 用于计算一个中间插值几何结构

<a id="Ch9.E39"></a>

$$
\mathbf{x}_{m+1}^{\prime}=\sum c_{i}\mathbf{x}_{i} \tag{9.39}
$$

及其对应的插值梯度

<a id="Ch9.E40"></a>

$$
\mathbf{g}_{m+1}^{\prime}=\sum c_{i}\mathbf{g}_{i} \tag{9.40}
$$

根据插值几何结构与插值梯度，按下式生成一个新的、独立的几何结构

<a id="Ch9.E41"></a>

$$
\mathbf{x}_{m+1}=\mathbf{x}_{m+1}^{\prime}-\mathbf{H}^{-1}\mathbf{g}_{m+1}^{\prime}\;. \tag{9.41}
$$

!!! note "注意"
    只要 Hessian 矩阵是正定的，无论其质量如何，理论上都能保证收敛。原始的 GDIIS
    算法使用静态 Hessian（*即*初始猜测的 Hessian），它常常只是一个简单的单位矩阵。
    在每个循环更新 Hessian 通常能带来更快的收敛，这也是 **Optimize** 中的默认设置。


对原始方法的其他改进包括：通过忽略较早的几何结构来限制式 ([9.33](#eq:a23)) 中所使用的先前几何结构数目，以及剔除与当前几何结构距离超过某一阈值的几何结构（默认值 = 0.3 a.u.）。
