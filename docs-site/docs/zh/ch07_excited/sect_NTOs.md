---
title: "7.13.3 自然跃迁轨道（NTO）"
---

## 7.13.3 自然跃迁轨道（Natural Transition Orbitals, NTOs）

（2026 年 7 月 4 日）

在某些情况下，即使是附着/脱离密度（attachment/detachment densities）也可能难以分析。一类重要的例子是含有多个发色团（chromophores）的体系，这类体系可以支持由定域激发的线性组合所构成的激子态（exciton states）。对于这样的态，附着密度和脱离密度都是高度离域的，并且基本上占据相同的空间区域。[[752]](../bib_references/bib.md#bib785)
 由于缺乏位相（phase）信息，附着/脱离密度难以分析；而正则分子轨道（canonical MOs）之间的强烈混合又使得激子态同样难以用分子轨道（MOs）来刻画。[[572]](../bib_references/bib.md#bib586)

通过为激发态构造自然跃迁轨道（NTOs），这些态以及其他激发态的分析得以大大简化。[[572]](../bib_references/bib.md#bib586)

（NTOs 背后的基本思想其实相当古老，[[864]](../bib_references/bib.md#bib898)
 并已被多次重新发现。[[913]](../bib_references/bib.md#bib947)
 后来这些轨道被证明等价于 CIS 自然轨道（natural orbitals）。[[1331]](../bib_references/bib.md#bib1390)
）设 $\mathbf{T}$ 表示来自激发态计算的跃迁密度矩阵（transition density matrix）。该矩阵的维度为 $O\times V$，其中 $O$ 和 $V$
分别表示占据 MO 与虚 MO 的数目。NTOs 由矩阵 $\mathbf{T}$ 的奇异值分解（singular value decomposition, SVD）所得到的变换 $\mathbf{U}$ 与 $\mathbf{V}$
定义，*即*：[[925]](../bib_references/bib.md#bib962)

<a id="eq:NTO_SVD"></a>

$$
\mathbf{UTV}^{\dagger}=\bm{\Lambda} \tag{7.188}
$$

矩阵 $\mathbf{U}$ 和 $\mathbf{V}$ 是酉矩阵，$\bm{\Lambda}$ 是对角矩阵，后者最多包含 $O$
个非零元素。矩阵 $\mathbf{U}$ 是从正则占据 MO 到一组 NTOs 的酉变换，这组 NTOs 共同表示被激发电子留下的“空穴”（hole）轨道；而 $\mathbf{V}$
则将正则虚 MO 变换为一组表示激发电子的 NTOs。（等价地，“空穴”是 $O\times O$ 矩阵 $\mathbf{TT}^{\dagger}$
的本征矢，而“粒子”是 $V\times V$ 矩阵 $\mathbf{T}^{\dagger}\mathbf{T}$ 的本征矢。[[913]](../bib_references/bib.md#bib947)
）这些“空穴”与“粒子”NTOs 成对出现，而它们在描述激发时的相对重要性由 $\bm{\Lambda}$
的对角元素决定，这些对角元素即为 NTO 基下的激发振幅（excitation amplitudes）。凭借式 ([7.188](#eq:NTO_SVD))
中的 SVD，任何激发态都可以用最多 $O$ 个激发振幅及相应的空穴/粒子 NTO 对来表示。（此处的讨论假定 $V\geq O$，除极小基组（minimal basis
sets）外通常都是如此。虽然可以利用式 ([7.188](#eq:NTO_SVD))
的转置在 $V<O$ 时求得 NTOs，但由于其适用范围有限，**Q-Chem** 中尚未实现这一功能。）

SVD 将矩阵对角化的概念推广到矩形矩阵的情形，因此可以尽可能减少精确表示 $\mathbf{T}$
所需的非零外积（outer products）数目。就此意义而言，NTOs 代表了激发态的最佳可能的粒子/空穴图像。脱离密度可由“空穴”NTOs
的平方和恢复，而附着密度则恰好是“粒子”NTOs 的平方和。然而，与附着/脱离密度不同，NTOs 保留了位相信息，这在刻画复杂体系中激发态的非绝热（diabatic）特征（*e.g.*，$\pi\pi^{\ast}$
或 $n\pi^{\ast}$）时非常有用。当仅存在一对显著的 NTOs
时，这两个轨道的平方（$|\psi_{\text{hole}}(\mathbf{r})|^{2}$ 与 $|\psi_{\text{particle}}(\mathbf{r})|^{2}$）恰好等同于第 [7.13.2](sect_AttachDetach.md)
节中引入的脱离密度与附着密度。

即使存在多个显著的 NTO 振幅，与正则 MO 基相比，NTOs 仍然代表着信息的大幅压缩。

在 **Q-Chem** 中，CIS、RPA、TDDFT、ADC 和 EOM-CC 方法均可使用 NTOs。对于关联波函数方法（EOM-CC 与 ADC）以及 SF-DFT，可以利用 **libwfa** 模块计算 NTOs。可视化
NTOs 最简单的方式，是按照第 [10](../ch10_properties/chap_properties.md) 章所述，生成适合用免费可用的 **MolDen** 或 **MacMolPlt**
程序查看的格式。
