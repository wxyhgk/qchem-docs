---
title: "9.8.5 态跟踪算法（State-Tracking Algorithm）"
---

## 9.8.5 态跟踪算法（State-Tracking Algorithm）

(July 4, 2026)

对于激发态几何优化及其他应用，在几何结构变化过程中寻找并跟随具有特定特征的电子激发态可能非常重要。针对此类情况，人们提出了多种态跟踪（state-tracking）流程。[[527]](../bib_references/bib.md#bib541)

**Q-Chem** 中提供了一种基于相邻步骤间附着/分离密度（attachment/detachment densities）重叠度的算法（见第 [7.13.2 节](../ch07_excited/sect_AttachDetach.md)）。[[256]](../bib_references/bib.md#bib256) 使用密度可以避免由轨道或组态相互作用（configuration-interaction）系数符号变化所引入的任何问题。

有两个参数用于影响电子势能面的选择。一个参数（$\gamma_{E}$）控制参与搜索的态的能量窗口，另一个参数（$\gamma_{S}$）控制态之间必须达到的重叠程度，才能被认为具有相同特征。这些参数既可以由用户设定，也可以根据核位移的大小自动生成。能量窗口是相对于当前步骤的估计能量定义的（*即*，$E_{\rm est}\pm\gamma_{E}$），而该估计能量又基于先前步骤的能量、梯度和核位移。这一估计能量与计算类型相关（*例如*，几何优化）。

重叠度的相似性度量定义为

<a id="eq:similarity_metric"></a>

$$
\mathcal{S}=1-\tfrac{1}{2}\bigl{(}||\Delta\mathbf{A}||+||\Delta\mathbf{D}||\bigr{)} \tag{9.59}
$$

其中 $\Delta\mathbf{A}=\mathbf{A}_{t+1}-\mathbf{A}_{t}$ 是相邻步骤间附着密度矩阵之差（式 ([7.185](../ch07_excited/sect_AttachDetach.md#eq:attach_density_matrix)))，$\Delta\mathbf{D}=\mathbf{D}_{t+1}-\mathbf{D}_{t}$ 是分离密度矩阵之差（式 ([7.183](../ch07_excited/sect_AttachDetach.md#eq:detach_density_matrix)))。式 ([9.59](#eq:similarity_metric)) 使用矩阵谱范数，

<a id="Ch9.E60"></a>

$$
||\mathbf{M}||=\left(\lambda_{\rm max}\mathbf{M}^{\dagger}\mathbf{M}\right)^{1/2} \tag{9.60}
$$

其中 $\lambda_{\rm max}$ 是 $\mathbf{M}$ 的最大本征值。

所选态始终满足以下条件之一

1. 1.

它是 $\gamma_{E}$ 所定义窗口内唯一的态。
2. 2.

它是重叠度最大的态，前提是至少有一个态满足 $\mathcal{S}\geq\gamma_{S}$。
3. 3.

若窗口内所有态都满足 $\mathcal{S}<\gamma_{S}$，或能量窗口内没有任何态，则选择能量上最接近的态。

态跟随（state-following）目前可用于 CIS 或 TDDFT 激发态，通过 *$rem* 变量 STATE_FOLLOW 启用。它可以用于几何优化、*从头算（ab initio）*分子动力学，[[256]](../bib_references/bib.md#bib256)

或冻结/生长弦（freezing/growing-string）方法。目标态通过 CIS_STATE_DERIV（用于优化或动力学）指定，或通过 SET_STATE_REACTANT 和 SET_STATE_PRODUCT（用于冻结弦或生长弦方法）指定。几何优化的结果可能受步长（GEOM_OPT_DMAX）影响，使用比默认值更小的步长通常可以得到更好的结果。此外，冻结/生长弦计算中弦的收敛往往具有挑战性。

### `STATE_FOLLOW`

> **启用态跟随。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE
>     * 不使用态跟随。
>     * TRUE
>     * 使用态跟随。
> * **建议**：无。

### `FOLLOW_ENERGY`

> **调整近邻态的能量窗口**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 使用动态阈值，基于相邻步骤间的能量差。
>     * $n$
>     * 在所选态周围
>     * $E_{\rm est}\pm n\times 10^{-6}~{}E_{h}$
>     * 范围内进行搜索。
> * **建议**：若要非绝热地（diabatically）跟随某个态，使用较宽的能量窗口；若要在大多数情况下保持在绝动态上，使用较窄的窗口。

### `FOLLOW_OVERLAP`

> **调整具有相似特征之态的阈值。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 使用动态阈值，基于相邻步骤间的能量差。
>     * $n$
>     * 上一步与当前步之间的重叠百分比。
> * **建议**：使用较高值时，要求态之间具有更高的相似性才能被视为同一态（从而更常基于能量进行选择）。
