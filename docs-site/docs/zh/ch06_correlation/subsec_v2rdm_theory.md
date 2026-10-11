---
title: "6.23.2 理论"
---

## 6.23.2 理论

（2026 年 7 月 4 日）

电子能量是一-RDM（1-RDM）与二-RDM（2-RDM）的精确泛函

<a id="eq:v2rdm:energy"></a>
$$
E=\frac{1}{2}\sum_{pqrs}{}^{2}D^{pq}_{rs}(pr|qs)+\sum_{pq}{}^{1}D^{p}_{q}h_{pq}, \tag{6.106}
$$

其中一-RDM（${}^{1}\mathbf{D}$）与二-RDM（2-RDM）在由指标 $p$、$q$、$r$、$s$ 标记的给定自旋轨道基下表示。一空穴约化密度矩阵（one-hole RDM，${}^{1}\mathbf{Q}$）、二空穴约化密度矩阵（two-hole RDM，${}^{2}\mathbf{Q}$）、粒子-空穴约化密度矩阵（particle-hole RDM，${}^{2}\mathbf{G}$）、部分三粒子约化密度矩阵（$\mathbf{T1}$ 与 $\mathbf{T2}$）以及完整三粒子约化密度矩阵（${}^{3}\mathbf{D}$、${}^{3}\mathbf{Q}$、${}^{3}\mathbf{E}$、${}^{3}\mathbf{F}$）均为 ${}^{1}\mathbf{D}$ 与 ${}^{2}\mathbf{D}$ 的线性函数。[[399]](../bib_references/bib.md#bib408)
在强制施加这些约化密度矩阵（RDM）之间的线性关系、对 ${}^{2}\mathbf{D}$ 所施加的收缩（contraction）与自旋约束，以及所有 RDM 的半正定（positive semidefinite）性质的前提下，对 ${}^{2}\mathbf{D}$ 极小化电子能量构成一个半正定规划（semidefinite program，SDP）问题。当前的 v2RDM 实现使用边界点半正定规划（boundary-point SDP，BPSDP）算法来求解该 SDP 问题。[[1120]](../bib_references/bib.md#bib1167)

SDP 的原始（primal）形式为

<a id="A3.S8.EGx37"></a>
$$
\displaystyle E_{\rm primal} \tag{6.107}
$$

此处，$\mathbf{x}$ 表示原始解向量，向量 $\mathbf{c}$ 包含定义量子体系的所有信息（单电子与双电子积分），而映射 $M(\mathbf{x})$ 将原始解映射到一组半正定的 RDM 上：

<a id="eqn:vectormatrixmap"></a>
$$
M({\bf x})=\left(\begin{array}[]{cccc}{}^{1}{\mathbf{D}}&0&0&0\\
0&{}^{1}{\mathbf{Q}}&0&0\\
0&0&{}^{2}{\mathbf{D}}&0\\
0&0&0&{}\ddots\\
\end{array}\right)\succeq 0. \tag{6.108}
$$

根据所选 N-可表示性（N-representability）条件的不同，可以在 $M(\mathbf{x})$ 中包含更多其他 RDM。约束矩阵 ${\mathbf{A}}$ 作用于 ${\mathbf{x}}$ 是 N-可表示性条件的一种紧致表示。${\mathbf{A}}$ 维护 $M({\mathbf{x}})$ 各分块之间的适当映射关系，并强制施加适当的自旋条件与收缩条件。另一种做法是考虑半正定问题的对偶（dual）形式，表示为

<a id="A3.S8.EGx38"></a>
$$
\displaystyle E_{\rm dual} \tag{6.109}
$$

其中 ${\mathbf{y}}$ 与 ${\mathbf{z}}$ 为对偶解，且 $M({\mathbf{z}})$ 被约束为半正定。

BPSDP 算法包含一个迭代的二步流程：

1. 1.

用共轭梯度法（conjugate gradient methods）求解 $\mathbf{AA}^{T}\mathbf{y}=\mathbf{A}(\mathbf{c}-\mathbf{z})+\tau\mu(\mathbf{b}-\mathbf{A}\mathbf{x})$ 得到 $\mathbf{y}$。
2. 2.

通过对角化将 $\mathbf{U}=M(\mu\mathbf{x}+\mathbf{A}^{T}\mathbf{y}-\mathbf{c})$ 分解为正分量与负分量，从而更新 $\mathbf{x}$ 与 $\mathbf{z}$。更新后的原始解与对偶解 $\mathbf{x}$ 和 $\mathbf{z}$ 由 $M(\mathbf{x})=\mathbf{U}(+)/\mu$ 与 $M(\mathbf{z})=-\mathbf{U}(-)$ 给出。

这里，$\tau$ 是步长参数，取自区间 [1.0,1.6] [[930]](../bib_references/bib.md#bib968)
。惩罚参数 $\mu$ 控制原始约束或对偶约束被强制施加的严格程度，并按照文献 [[930]](../bib_references/bib.md#bib968)
 中所述的方案动态更新。$\mu$ 的更新频率由 *$rem* 关键字 RDM_MU_UPDATE_FREQUENCY 控制。当原始误差 $||\mathbf{A}\mathbf{x}-\mathbf{b}||$、对偶误差 $||\mathbf{A}^{T}\mathbf{y}-\mathbf{c}+\mathbf{z}||$ 以及原始/对偶能量间隙 $|E_{\rm primal}-E_{\rm dual}|$ 足够小时，即认为算法收敛。原始/对偶误差以及原始/对偶能量间隙的收敛判据分别由 *$rem* 关键字 RDM_EPS_CONVERGENCE 与 RDM_E_CONVERGENCE 控制。对于 DQG 条件，BPSDP 算法的计算标度为 $n^{6}$；对于 T1、T2 与 3POS 条件，标度为 $n^{9}$，其中 $n$ 是 v2RDM 计算中活性轨道的数目。

在 v2RDM-CASSCF 中，执行 BPSDP 算法以确定活性分子轨道子集的一-RDM 与二-RDM。在经过指定次数的 v2RDM 迭代（即上述步骤 1. 与 2.）之后，针对受限双占据/活性以及活性/外层（external）转动对这些轨道进行优化。该轨道优化的频率由 *$rem* 关键字 RDM_ORBOPT_FREQUENCY 控制。

给定 v2RDM-CASSCF 计算收敛后得到的一-RDM 与二-RDM，可以通过 MC-PDFT 的形式体系来估算剩余的关联效应。在 MC-PDFT 中，体系的总能量表示为

<a id="EQ:EMCPDFT"></a>
$$
E_{\rm MC-PDFT}=\sum_{i}h^{i}_{i}+\sum_{tu}h^{t}_{u}{}^{1}D^{t}_{u}+E_{\rm H}+E_{\rm XC}\left[\rho({\bf r}),\Pi({\bf r}),|\nabla\rho({\bf r})|,|\nabla\Pi({\bf r})|\right] \tag{6.110}
$$

其中 Hartree 能量 $E_{\rm H}$ 为经典的库仑排斥能

<a id="EQN:HARTREE_ENERGY"></a>
$$
E_{\rm H}=\frac{1}{2}\sum_{ij}(ii|jj)+\sum_{itu}(tu|ii){}^{1}D^{t}_{u}+\frac{1}{2}\sum_{tuvw}(tu|vw){}^{1}D^{t}_{u}{}^{1}D^{v}_{w} \tag{6.111}
$$

而 $E_{\rm xc}$ 表示一个在顶对密度（on-top pair density）泛函。在式 [6.111](#EQN:HARTREE_ENERGY) 中，标签 $i$ 与 $j$ 表示双占据自旋轨道，标签 $t$、$u$、$v$ 与 $w$ 表示活性自旋轨道。符号 $\rho({\bf r})$ 与 $\Pi({\bf r})$ 分别表示密度与在顶对密度，它们用分子轨道 $\{\phi\}$ 定义为

<a id="Ch6.E112"></a>
$$
\rho({\bf r})=\sum_{pq}\phi_{p}({\bf r})\phi_{q}({\bf r}){}^{1}D^{p}_{q} \tag{6.112}
$$

以及

<a id="Ch6.E113"></a>
$$
\Pi({\bf r})=\sum_{pqrs}\phi_{p}({\bf r})\phi_{q}({\bf r})\phi_{r}({\bf r})\phi_{s}({\bf r}){}^{2}D^{pq}_{rs} \tag{6.113}
$$

而 $\nabla\rho({\bf r})$ 与 $\nabla\Pi({\bf r})$ 表示这些量的梯度。在 Q-Chem 中，$E_{\rm xc}$ 选取为平移型（translated）[[886]](../bib_references/bib.md#bib920)
 在顶对密度泛函，它本质上等同于密度与自旋密度（及其梯度）的泛函，只是将自旋密度（及其梯度）重新表示为在顶对密度（及其梯度）的函数。在顶对密度泛函的具体选取通过 *$rem* 变量 PDFT_EXCHANGE 与 PDFT_CORRELATION 控制。
