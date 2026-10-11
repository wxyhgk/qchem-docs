---
title: "7.11.10 面向 RAS-SF 的态特定 PCM"
---

## 7.11.10 面向 RAS-SF 的态特定 PCM

（2026 年 7 月 4 日）

如[第 11.2.3 节](../ch11_env/topic_pcm-em.md)所述，极化连续介质模型（Polarizable Continuum Model, PCM）是一种将介电边界条件引入基态量子化学计算的高效方法，尽管在该理论框架内描述电子激发态时还存在一些额外的建模选择。[[569]](../bib_references/bib.md#bib580)
对于使用 RAS-SF 波函数计算的垂直跃迁能量，基于态特定的 PCM 溶剂化校正同时提供平衡（equilibrium）与非平衡（nonequilibrium）两种版本。[[32]](../bib_references/bib.md#bib17)
基态极化使用溶剂的静态介电常数来描述；而在非平衡溶剂化方法中，该极化会在垂直激发时利用溶剂的光学介电常数加以修正。

平衡形式的表述通过求解态特定的薛定谔（Schrödinger）方程实现

<a id="Ch7.E172"></a>

$$
(\hat{H}_{\text{vac}}+\hat{R}_{k})|\Psi_{k}\rangle=E_{k}|\Psi_{k}\rangle \tag{7.172}
$$

其中 $\hat{R}_{k}$ 是态 $k$ 的反应场算符。由于 $\hat{R}_{k}$ 依赖于 $|\Psi_{k}\rangle$，该方程必须迭代求解。完全弛豫（平衡）的激发自由能为

<a id="Ch7.E173"></a>

$$
\Delta G=G_{k}^{\text{eq}}-G_{0}=\Delta E_{k}^{\text{eq}}-W_{k}+W_{0}\;. \tag{7.173}
$$

（之所以称为*自由*能，是因为对溶剂的连续介质描述隐式地包含了对溶剂自由度的统计平均。）我们用 $G$ 表示自由能，用 $W$ 表示极化功，下标用于指明所涉及的电子态。

溶剂化模型的非平衡版本采用微扰框架来求解薛定谔方程。详细内容见[第 11.2.3.3 节](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM)。简而言之，该方法基于按如下方式划分的态特定哈密顿量

<a id="Ch7.E174"></a>

$$
\hat{H}_{k}^{\text{noneq}}=\underbrace{\hat{H}_{\text{vac}}+\hat{R}_{0}^{\text{s+f}}}_{\hat{H}_{0}}+\lambda(\hat{R}_{k}^{\text{f}}-\hat{R}_{0}^{\text{f}})\;. \tag{7.174}
$$

零阶哈密顿量（$\hat{H}_{0}$）包含基态平衡反应场算符 $\hat{R}_{0}\equiv R_{0}^{\text{s+f}}=\hat{R}_{0}^{\text{s}}+\hat{R}_{0}^{\text{f}}$。溶剂极化被划分为“慢”（核）分量与“快”（电子）分量，但在平衡溶剂化中两个分量都被包含在内。微扰项（由微扰参数 $\lambda$ 标示）用于修正激发 $|\Psi_{0}\rangle\rightarrow|\Psi_{k}\rangle$ 过程中的快极化。这一非平衡校正通过一阶微扰理论来描述，其结果是对激发能的微扰型、态特定（ptSS）校正：

<a id="Ch7.E175"></a>

$$
\Delta G_{k}^{\text{ptSS(1)}}=G_{k}-G_{0}=\Delta E_{k}^{\text{ptSS(1)}}-W^{\text{f}}_{k(0)}+W^{\text{f}}_{0}+W_{0,k(0)} \tag{7.175}
$$

更多细节参见文献 [[32]](../bib_references/bib.md#bib17)
。
