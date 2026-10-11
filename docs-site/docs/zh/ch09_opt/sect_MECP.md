---
title: "9.8.3 最小能量交叉点"
---

## 9.8.3 最小能量交叉点

(2026 年 7 月 4 日)

锥形相交（conical intersection）的接缝空间（seam space）实际上是一个维度为 $N_{\rm int}-2$ 的（超）曲面，尽管所讨论的两个电子态在该空间内的每一点都是简并的，但电子能量却随点的不同而变化。为了给出光化学反应路径的简单图像，人们常常希望在这个 $(N_{\rm int}-2)$ 维接缝内找到最小能量交叉点（minimum-energy crossing point, MECP）。随后进行两次独立的最小能量路径搜索：一次在激发态上，从基态几何出发，终止于 MECP；另一次在基态上，从 MECP 出发，终止于基态几何，如此便可得到一条光反应机理。（一个简单的例子可见文献 [[1546]](../bib_references/bib.md#bib1612)。）从某种意义上说，MECP 之于光化学，就如同过渡态（transition state）之于发生在单一玻恩-奥本海默（Born-Oppenheimer）势能面上的反应。不过不应把这一类比推得过远：尽管过渡态可以合理地被视为反应路径上的瓶颈点，但穿过锥形相交的路径可能是下坡的，因此更有可能在相交“附近”的某一点从一个势能面过渡到另一个势能面；此外，同一对电子态之间可能存在多个锥形相交，因而可能有不止一种光反应机理在起作用。若要探索这种复杂性，可以采用非绝热“面跳跃（surface hopping）”*ab initio* 分子动力学，如第 [9.9.7](sect_fssh.md) 节所述，但其计算代价会显著增加。本节我们介绍一种计算上更简单的程序，即沿锥形接缝寻找 MECP。

回顾一下，电子态 $J$ 与 $K$ 之间锥形相交周围的分支空间（branching space）由两个矢量张成：$\mathbf{g}_{JK}$ [式 ([9.49](subsec_NACMEs_and_CIs.md#eq:gJK))] 与 $\mathbf{h}_{JK}$ [式 ([9.50](subsec_NACMEs_and_CIs.md#eq:hJK))]。前者对于任何具有解析激发态梯度的电子结构方法都能容易地以解析形式获得，而非绝热耦合矢量（nonadiabatic coupling vector）$\mathbf{h}_{JK}$ 对大多数方法而言并*不*可用。因此，人们发展了若干种无需计算 $\mathbf{h}_{JK}$ 即可优化 MECP 的算法，**Q-Chem** 中提供了其中三种。

Martínez 及其合作者[[805]](../bib_references/bib.md#bib840)
 提出了一种罚函数约束（penalty-constrained）的 MECP 优化算法，其核心是最小化目标函数

<a id="Ch9.E52"></a>
$$
F_{\sigma}(\mathbf{R})=\tfrac{1}{2}\bigl{[}E_{I}(\mathbf{R})+E_{J}(\mathbf{R})\bigr{]}+\sigma\left(\frac{\bigl{[}E_{I}(\mathbf{R})-E_{J}(\mathbf{R})\bigr{]}^{2}}{E_{I}(\mathbf{R})-E_{J}(\mathbf{R})+\alpha}\right)\;, \tag{9.52}
$$

其中 $\alpha$ 是为避免奇点而设定的固定参数，$\sigma$ 则是罚函数的拉格朗日乘子（Lagrange multiplier），用于驱使能隙趋于零。对 $F_{\sigma}$ 的极小化是按迭代方式进行的，每次迭代使用逐渐增大的 $\sigma$ 值。

第二种 MECP 优化算法是对罚函数约束方法的一种简化，我们称之为“直接（direct）”方法。此时，目标函数的梯度为

<a id="eq:direct_MECP"></a>
$$
\mathbf{G}=\mathbf{P}\mathbf{G}_{\rm mean}+2(E_{K}-E_{J})\mathbf{G}_{\rm diff}\;, \tag{9.53}
$$

其中

<a id="Ch9.E54"></a>
$$
\mathbf{G}_{\rm mean}=\tfrac{1}{2}(\mathbf{G}_{J}+\mathbf{G}_{K}) \tag{9.54}
$$

是平均能量梯度，这里 $\mathbf{G}_{i}=\partial E_{i}/\partial\mathbf{R}$ 是态 $i$ 的核梯度；而

<a id="Ch9.E55"></a>
$$
\mathbf{G}_{\rm diff}=\frac{\mathbf{G}_{K}-\mathbf{G}_{J}}{||\mathbf{G}_{K}-\mathbf{G}_{J}||} \tag{9.55}
$$

是归一化的差值梯度。最后，

<a id="eq:MECP_projector1"></a>
$$
\mathbf{P}=\bm{1}-\mathbf{G}_{\rm diff}\mathbf{G}_{\rm diff}^{\top} \tag{9.56}
$$

的作用是把梯度差方向从式 ([9.53](#eq:direct_MECP)) 中的平均能量梯度里投影剔除。该算法随后就是沿梯度 $\mathbf{G}$ 进行极小化，而不必像对拉格朗日乘子那样做迭代循环，后者的收敛有时较为缓慢。

**Q-Chem** 中可用的第三种、也是最后一种 MECP 优化算法，是由 Morokuma 及其合作者[[871]](../bib_references/bib.md#bib906)
 发展、并由 Zhang 与 Herbert 在 **Q-Chem** 中实现的分支平面更新（branching-plane updating）方法[[1546]](../bib_references/bib.md#bib1612)
。该算法使用的梯度与式 ([9.53](#eq:direct_MECP)) 中的相似，但投影剔除的不仅是式 ([9.56](#eq:MECP_projector1)) 中的 $\mathbf{G}_{\rm diff}$，还有一个与之正交的第二矢量，它代表对分支空间的逐次更新近似。

上述三种方法都不需要计算非绝热耦合，并且三者都可以用于在 CIS、SF-CIS、TDDFT、SF-TDDFT 以及 SOS-CIS(D0) 级别上优化 MECP。直接算法还可用于 EOM-XX-CCSD 方法（XX = EE、IP 或 EA）。需要注意的是，由于 EOM-XX-CCSD 是一种线性响应方法，在处理涉及基态的锥形相交时，它会遇到与第 [9.8.1](subsec_NACMEs_and_CIs.md) 节中讨论的 TDDFT 相同的拓扑结构问题。而采用自旋翻转（spin-flip）方法则可获得正确的拓扑结构[[1547]](../bib_references/bib.md#bib1613)。

(SF-)CIS 与 (SF-)TDDFT 具备解析的导数耦合，因此对这些方法可以改用同时利用 $\mathbf{g}_{JK}$ 与 $\mathbf{h}_{JK}$ 的优化算法。Schlegel 及其合作者[[85]](../bib_references/bib.md#bib70)
 提出的这样一种算法在 **Q-Chem** 中也是可用的，它沿式 ([9.53](#eq:direct_MECP)) 给出的梯度进行优化，但使用投影算符

<a id="eq:MECP_projector2"></a>
$$
\mathbf{P}=\bm{1}-\mathbf{G}_{\rm diff}\mathbf{G}_{\rm diff}^{\top}-\mathbf{y}\mathbf{y}^{\top} \tag{9.57}
$$

其中

<a id="Ch9.E58"></a>
$$
\mathbf{y}=\frac{(\bm{1}-\mathbf{x}\mathbf{x}^{\top})\mathbf{h}_{JK}}{||(\bm{1}-\mathbf{x}\mathbf{x}^{\top})\mathbf{h}_{JK}||}\;, \tag{9.58}
$$

用以取代式 ([9.56](#eq:MECP_projector1)) 中的投影算符。式 ([9.57](#eq:MECP_projector2)) 的作用是把 $\mathbf{g}_{JK}$ 与 $\mathbf{h}_{JK}$ 所张成的空间（*即*分支空间）从式 ([9.53](#eq:direct_MECP)) 的态平均梯度中投影剔除。这通常会减少收敛 MECP 所需的迭代次数；而且由于计算（可选的）$\mathbf{h}_{JK}$ 矢量相对于（必需的）$\mathbf{g}_{JK}$ 矢量只带来很少的额外开销，最后这一算法相较于前三种方法往往能带来显著的速度提升[[1547]](../bib_references/bib.md#bib1613)。

因此，对于 (SF-)CIS 和 (SF-)TDDFT，它是被推荐的首选方案。

需要指出的是，虽然自旋翻转方法解决了涉及基态的锥形相交周围的拓扑结构问题，但相对于相应的自旋守恒方法，该方法往往会加剧自旋污染（spin contamination）[[1549]](../bib_references/bib.md#bib1615)。

尽管传统的自旋守恒 CIS 与 TDDFT 中当然也存在自旋污染，但自旋翻转方法带来了一个独特的难题。为明确起见，假设我们关注的是单重激发态。那么自旋翻转方法的参考态应当是高自旋的三重态。自旋翻转激发会产生 S${}_{0}$、S${}_{1}$、S${}_{2},\ldots$，但也会产生三重态参考态的 $M_{S}=0$ 分量，而该分量因此出现在表面上看起来是单重态流形的空间之中。**Q-Chem** 试图依据 $\langle\hat{S}^{2}\rangle$ 的阈值自动识别它，但严重的自旋污染有时会使这一算法失效[[1546]](../bib_references/bib.md#bib1612)，

从而妨碍 **Q-Chem** 区分（在此具体示例中的）单重态与三重态的能力。一个替代方案或许是第 [9.8.5](sec_state_following.md) 节所描述的态追踪（state-tracking）程序。自旋适配的自旋翻转（spin-adapted spin-flip, SA-SF）方法，无论在 CIS 还是 TDDFT 级别，都可以通过添加得到 $\hat{S}^{2}$ 本征态所需的最少行列式数目来消除自旋污染[[1549]](../bib_references/bib.md#bib1615)。

SA-SF 方法在第 [7.2.3.3](../ch07_excited/Ch7.S2.SS3.md#safs-sftddft) 节中描述。它目前尚缺解析梯度，但可用于对采用 SF-TDDFT 得到的轨迹或 MECP 优化路径进行抽查校验。
