---
title: "6.10.1 引言"
---

## 6.10.1 引言

（2026 年 7 月 4 日）

Q-Chem 提供了一种基于 RI 近似的、有用的 $\mathcal{O}(N^{4})$ 标度方法——直接随机相位近似（direct random phase approximation, dRPA）。该实现由 Joonho Lee 在与 Martin Head-Gordon 合作时添加。[[784]](../bib_references/bib.md#bib829)
 RI-dRPA 已被应用于热化学[[346]](../bib_references/bib.md#bib350)
 和非共价相互作用
问题[[991]](../bib_references/bib.md#bib1033)
，并经常展现出优于 RI-MP2 的性能。就计算成本而言，RI-dRPA 应与自旋对反式 MP2（scaled-opposite-spin MP2, SOS-MP2）进行比较；而在理论上，它涉及的图远超二阶，并且与耦合簇理论类似地包含了无穷阶图。事实上，可以将 dRPA 视为一种约化的含双激发耦合簇（coupled-cluster with doubles）方法。[[1225]](../bib_references/bib.md#bib1280)
 简而言之，我们将 dRPA 能量定义为

<a id="Ch6.E53"></a>

$$
E=E_{\text{HF}}+E_{\text{c}}^{\text{dRPA}} \tag{6.53}
$$

其中，利用等离激元（plasmon）公式计算[[373]](../bib_references/bib.md#bib377)

<a id="Ch6.E54"></a>

$$
E_{\text{c}}^{\text{dRPA}}=\int_{-\infty}^{\infty}\frac{\mathrm{d}\omega}{4\pi}\mathrm{tr}\left[\ln\left(\mathbf{I}+\mathbf{Q}(\omega)\right)-\mathbf{Q}(\omega)\right] \tag{6.54}
$$

其中

<a id="Ch6.E55"></a>

$$
\mathbf{Q}(\omega)=2\mathbf{B}^{T}\mathbf{D}(\mathbf{D}^{2}+\omega^{2}\mathbf{I})^{-1}\mathbf{B} \tag{6.55}
$$

且有

<a id="A3.S8.EGx21"></a>

$$
\displaystyle B_{ia,P} \tag{6.56}
$$

在这种形式下，计算 dRPA 关联能的成本为四次方标度，与 SOS-MP2 相当。要使用该方法，必须设置
METHOD = RIDRPA，并同时指定 AUXBASIS。
