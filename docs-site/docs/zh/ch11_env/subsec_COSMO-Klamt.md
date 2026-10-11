---
title: "11.2.8 COSMO"
---

## 11.2.8 COSMO

（2026 年 7 月 4 日）

根据表 [11.3](topic_pcm-em.md#table:K-matrix)，COSMO 与 C-PCM 似乎仅在介电屏蔽因子 $f_{\varepsilon}$ 上有所不同，见式 ([11.3](topic_pcm-em.md#eq:f_epsilon))。事实上，两种模型中的面电荷均按照下式计算

<a id="eq:C-PCM"></a>

$$
\mathbf{q}=-f_{\varepsilon}\mathbf{S}^{-1}\mathbf{v}\;. \tag{11.24}
$$

如第 [11.2.4](subsec_PCM_job_control.md) 节所讨论的，用户可以选择 $f_{\varepsilon}$ 的不同取值，包括 Klamt 及其合作者[[692]](../bib_references/bib.md#bib721)最初建议的取值
$f_{\varepsilon}=(\varepsilon-1)/(\varepsilon+1/2)$，

或在 C-PCM 计算中通常使用的[[1375]](../bib_references/bib.md#bib1436)
$f_{\varepsilon}=(\varepsilon-1)/\varepsilon$。然而更为重要的是，COSMO 与 C-PCM 的区别在于：前者包含一个针对溢出电荷（outlying charge）的 *ad hoc*（特殊约定）修正，该修正超出了式 ([11.24](#eq:C-PCM)) 的范畴；而 C-PCM 则仅仅由按式 ([11.24](#eq:C-PCM))（自洽地）计算所得的诱导面电荷构成。这一修正见于 COSMO 的许多实现方案[[569]](../bib_references/bib.md#bib580)
，其做法是使用两个独立的溶质空腔。值得注意的是，
后来有研究证明式 ([11.24](#eq:C-PCM)) *隐含地*包含了溢出电荷修正[[244]](../bib_references/bib.md#bib244)，
这是因为它可由 SS(V)PE 模型[[755]](../bib_references/bib.md#bib788)推导而来，而后者正是专门为处理溢出电荷而发展起来的。因此，尽管额外的*显式*溢出电荷修正在实践中取得了成功[[694]](../bib_references/bib.md#bib726)，其理论依据却十分有限。
有关这些问题的讨论，请参见文献 [[569]](../bib_references/bib.md#bib580)。

无论如何，这种*后验*（a posteriori）溢出电荷修正的具体做法如下。在求解式 ([11.24](#eq:C-PCM))之后，COSMO[[692]](../bib_references/bib.md#bib721)中的溢出电荷修正通过先定义一个更大的空腔来获得，该空腔基本上能够容纳溶质的全部电子密度；在实际操作中，这通常意味着采用 $1.95R$ 的原子半径，其中 $R$ 表示当初计算 $\mathbf{q}$ 时所使用的原始原子 van der Waals 半径。（请注意，与第 [11.2.3](topic_pcm-em.md) 和 [11.2.4](subsec_PCM_job_control.md) 节所描述的 PCM 不同——后者的原子半径有默认值但允许用户高度自定义——COSMO 的原子半径是专为该模型参数化并固定不变的。）随后在这个更大的空腔表面上计算一组新的电荷 $\mathbf{q}^{\prime}=-f_{\varepsilon}(\mathbf{S}^{\prime})^{-1}\mathbf{v}^{\prime}$，并将*原始*空腔表面上的电荷调整为新值 $\mathbf{q}^{\prime\prime}=\mathbf{q}+\mathbf{q}^{\prime}$。最后，按 $\mathbf{v}^{\prime\prime}=-f_{\varepsilon}\mathbf{S}\mathbf{q}^{\prime\prime}$在原始表面上计算修正后的静电势。正是利用这一电势来计算溶质–连续介质静电相互作用（极化能），
$G_{\rm pol}=\tfrac{1}{2}\sum_{i}q_{i}^{\prime\prime}v_{i}^{\prime\prime}$。（作为对比，当使用第 [11.2.3](topic_pcm-em.md) 节所描述的 C-PCM 方法时，静电极化能为 $G_{\rm pol}=\tfrac{1}{2}\sum_{i}q_{i}v_{i}$，
即使用原始面电荷 $\mathbf{q}$ 与表面静电势 $\mathbf{v}$ 计算。）借助这一溢出电荷修正，
**Q-Chem** 对 COSMO 的实现与 **Turbomole**[[1203]](../bib_references/bib.md#bib1257)中的实现相类似。

要请求 COSMO 计算，需在 *$rem* 段中设置 SOLVENT_METHOD =
COSMO，同时配合常规的作业控制（job control）变量。*$solvent* 段中的关键字 **Dielectric** 用于设定溶剂的静态介电常数，其用法如前文针对其他溶剂化模型所述。
