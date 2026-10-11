---
title: "5.13.1 引言"
---

## 5.13.1 引言

（2026 年 7 月 4 日）

对亚稳态电子态（例如临时阴离子）进行建模，是自洽场（Self-Consistent Field, SCF）方法面临的一项挑战。
这类阴离子会发生自剥离（autodetachment）过程（AB${}^{-}\ \rightarrow\$AB $+$ e${}^{-}$），
而自剥离出来的未束缚电子往往被放置在一个非常弥散的分子轨道中。
这样，最终的 SCF 解描述的是中性分子加一个孤立电子，而非所期望的临时阴离子。
克服这一问题的一种方法是在分子哈密顿量 $\hat{H}$ 上引入复吸收势（Complex Absorbing Potential, CAP，另见第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节）：
$\hat{H}\rightarrow\hat{H}_{\eta}=\hat{H}-\text{i}\eta\hat{W}$。
其中，$\hat{W}$ 和 $\eta$ 分别决定 CAP 的形状和强度。

将 CAP 与密度泛函理论（Density Functional Theory, DFT）方法相结合（CAP-DFT），
可以对超出后 Hartree-Fock（post-Hartree-Fock）方法处理能力范围的大型临时阴离子进行建模，
并且相比 CAP-Hartree-Fock（CAP-HF）理论具有更高的精度。[[1359]](../bib_references/bib.md#bib1419)

在 Ernzerhof 和 Zhou 的理论工作基础上——他们报道了采用局域密度近似（Local Density Approximation）的 CAP-DFT 计算[[372]](../bib_references/bib.md#bib376)——
**Q-Chem** 当前的实现提供了来自局域密度近似（LDA）、广义梯度近似（Generalized Gradient Approximation, GGA）以及杂化泛函（Hybrid Functional）层级的一系列泛函供选择（见第 [5.13.3](sub_XCfuncs_CAP.md) 节）。
