---
title: "6.8.1 引言"
---

## 6.8.1 引言

(July 4, 2026)

尽管二阶 Møller-Plesset 微扰理论（MP2）提供了最简单且最具性价比的 *ab initio*（从头算）关联能，但它需要为简并态单独建立形式体系，因为 MP2 能量在零能隙（zero-gap）极限下发散。二阶 Brillouin-Wigner 微扰理论（BW2）则无需这样的重新推导，因为其给出的二阶能量

<a id="Ch6.E33"></a>
$$
E_{\text{c}}^{(2)}=-\frac{1}{4}\sum\limits_{ijab}\frac{|\langle ij||ab\rangle|^{2}}{\Delta_{ij}^{ab}+E_{\text{c}}^{(2)}} \tag{6.33}
$$

由于分母中存在关联能项，当轨道能隙 $\Delta_{ij}^{ab}=\varepsilon_{a}+\varepsilon_{b}-\varepsilon_{i}-\varepsilon_{j}$ 为零时仍然有限。
然而，BW2 关联能并不具备尺寸一致性（size-consistency），即对于两个相距遥远、无相互作用的子系统 A 和 B，它不满足
$E(A\cup B)=E(A)+E(B)$，这严重限制了其在化学中的适用性。

最近，Carter-Fenk 和 Head-Gordon 提出了一种在二阶精度上保持尺寸一致性的 Brillouin-Wigner 微扰理论（BW-s2），它既保留了这一关键性质，又对零能隙体系保持有限值。[[195]](../bib_references/bib.md#bib196)

该理论基于对零阶哈密顿量的重新划分，得到了一个略微修正的振幅方程。而
MP2 振幅可以通过求解

<a id="Ch6.E34"></a>
$$
\Delta_{ijkl}^{abcd}\cdot t_{kl}^{cd}=-\langle ij||ab\rangle\;, \tag{6.34}
$$

求得，BW-s2 振幅方程则包含一个正则化张量，

<a id="Ch6.E35"></a>
$$
\big{(}\Delta_{ijkl}^{abcd}+R_{ijkl}^{abcd}\big{)}\cdot t_{kl}^{cd}=-\langle ij||ab\rangle \tag{6.35}
$$

在上述方程中，$\Delta_{ijkl}^{abcd}$ 由 Fock 矩阵元构成，并在使用正则轨道时约化为熟悉的
$\Delta_{ij}^{ab}$，而

<a id="eq:Rtensor"></a>
$$
R_{ijkl}^{abcd}=\frac{\alpha}{2}\big{(}W_{ik}\delta_{jl}+\delta_{ik}W_{jl}\big{)}\delta_{ac}\delta_{bd} \tag{6.36}
$$

其中，

<a id="Ch6.E37"></a>
$$
W_{ij}=\frac{1}{2}\sum\limits_{kab}\big{(}t_{ik}^{ab}\langle jk||ab\rangle+t_{jk}^{ab}\langle ik||ab\rangle\big{)} \tag{6.37}
$$

选择 $\mathbf{W}$ 的这种形式是因为它具备尺寸一致性，从而导出尺寸一致的 BW-s2 关联能。
从物理上看，$\mathbf{W}$ 代表 Koopmans（静态轨道）电离过程的关联能。因此，BW-s2 中的占据轨道被赋予了关联效应，使得占据/虚轨道能隙增大。
将占据轨道旋转到使 $\bm{\Delta}+\bm{R}$ 对角的基组后，BW-s2 的工作方程与 MP2 的形式相同，

<a id="Ch6.E38"></a>
$$
E_{\text{c}}^{(2)}=-\frac{1}{4}\sum\limits_{ijab}\frac{|\widetilde{\langle ij||ab\rangle}|^{2}}{\varepsilon_{a}+\varepsilon_{b}-\tilde{\varepsilon}_{i}-\tilde{\varepsilon}_{j}} \tag{6.38}
$$

只是轨道及相应的反对称化双电子积分已旋转到新的基组中。

在方程 [6.36](#eq:Rtensor) 中存在一个隐含参数 $\alpha$，
用于控制正则化的强度。
最初，该参数被设为 $\alpha=1$，以便在解离极限下对最小基组 H${}_{\text{2}}$ 的双电子双轨道体系得到精确结果，
但后来对 $\alpha$ 进行了调优，从而在从热化学性质到非共价相互作用能以及闭壳层过渡金属
反应能等一系列广泛的化学问题上获得了更加精确的结果。[[201]](../bib_references/bib.md#bib197)

所得 BW-s2($\alpha$) 方法的最优 $\alpha$ 值在不同化学问题之间略有差异，
但被发现比依赖于能隙的正则化参数（如 $\kappa$-、$\sigma$- 或 $\sigma^{2}$-MP2）更具灵活性。
作为一种折中，人们提出了 $\alpha=4$ 这一“普适”参数，以在广泛的化学
性质上取得最佳的综合表现。[[201]](../bib_references/bib.md#bib197)
