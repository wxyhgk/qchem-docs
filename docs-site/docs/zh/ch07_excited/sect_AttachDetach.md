---
title: "7.13.2 附件/脱附密度分析（Attachment/Detachment Density Analysis）"
---

## 7.13.2 附件/脱附密度分析（Attachment/Detachment Density Analysis）

（2026 年 7 月 4 日）

考虑所关心的初态与末态的单粒子密度矩阵，分别记为 $\mathbf{P}_{1}$ 与 $\mathbf{P}_{2}$。假设每个态都用自旋轨道的有限基组（例如分子轨道基）来表示，并且两个态具有相同的几何构型。将这两个矩阵相减即可得到差密度（difference density）

<a id="eq623"></a>

$$
\bm{\Delta}={\rm{\bf P}}_{1}-{\rm{\bf P}}_{2} \tag{7.180}
$$

在此需要注意，描述单个态的单粒子密度矩阵 $\mathbf{P}$ 的本征矢量称为自然轨道（natural orbitals），它能为该态提供可能的最佳轨道描述，因为以自然轨道作为单粒子基进行的 CI 展开是最紧凑的。附件/脱附分析（attachment/detachment analysis）的基础是考察所谓电子跃迁的自然轨道及其占据数（相应的本征值）。这些轨道定义为由下式给出的本征矢量 $\mathbf{U}$

<a id="eq624"></a>

$$
{\rm{\bf U}}^{\dagger}\bm{\Delta}{\rm{\bf U}}=\delta \tag{7.181}
$$

这些轨道的占据数 $\delta_{p}$ 之和为

<a id="eq625"></a>

$$
\mbox{tr}(\bm{\Delta})=\sum\limits_{p=1}^{N}{\delta_{p}}=n \tag{7.182}
$$

其中 $n$ 是跃迁过程中电子的净得失数。显然，对于不涉及电离或电子附着的电子跃迁，其净得失数等于零。

脱附密度（detachment density）

<a id="eq:detach_density_matrix"></a>

$$
\textbf{D}=\textbf{UdU}^{\dagger} \tag{7.183}
$$

定义为差密度的所有具有负占据数的自然轨道之和，并以其占据数的绝对值作为权重，其中 $\mathbf{d}$ 是对角矩阵，其元素为

<a id="eq627"></a>

$$
d_{p}=-\min(\delta_{p},0) \tag{7.184}
$$

脱附密度对应于电子跃迁中被腾空的单粒子能级所涉及电子密度，即空穴密度（hole density）。

附件密度（attachment density）

<a id="eq:attach_density_matrix"></a>

$$
\textbf{A}=\textbf{UaU}^{\dagger} \tag{7.185}
$$

定义为差密度的所有具有正占据数的自然轨道之和，其中 $\mathbf{a}$ 是对角矩阵，其元素为

<a id="eq629"></a>

$$
a_{p}=\max(\delta_{p},0)\;. \tag{7.186}
$$

附件密度对应于跃迁中被占据的单粒子能级所涉及电子密度，即粒子密度（particle density）。附件密度与脱附密度之差即得到原始的差密度矩阵

<a id="eq630"></a>

$$
\bm{\Delta}=\mathbf{A}-\mathbf{D}\;. \tag{7.187}
$$

在 CIS 或 TDDFT（含时密度泛函理论）计算中，由于跃迁严格来说是单电子性质的，矩阵 $\mathbf{A}$ 与 $\mathbf{D}$ 分别是非松弛（unrelaxed）差密度矩阵的粒子部分（虚-虚块，virtual-virtual）和空穴部分（占据-占据块，occupied-occupied）。
