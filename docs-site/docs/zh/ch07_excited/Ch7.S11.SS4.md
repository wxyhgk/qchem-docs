---
title: "7.11.4 RAS-CI 中的短程密度泛函关联"
---

## 7.11.4 RAS-CI 中的短程密度泛函关联

（2026 年 7 月 4 日）

另一种途径是借助短程密度泛函关联能，在 RAS-CI 波函数中引入有效的动态关联。
这一思想依赖于波函数方法与密度泛函理论（Density Functional Theory, DFT）在处理非动态关联和动态关联方面能力的差异。
具体而言，RAS-CI-$sr$DFT（或 RAS-$sr$DFT）方法[[211]](../bib_references/bib.md#bib206)

基于电子-电子库仑算符（$\hat{V}_{ee}$）的范围分离，通过误差函数来描述长程相互作用，

<a id="A3.S8.EGx69"></a>
$$
\displaystyle\hat{V}_{\text{ee}}^{lr,\mu} \tag{7.166}
$$

其中 $r_{ij}$ 为电子间距离，参数 $\mu$ 控制短程与长程相互作用的范围。
对 $\hat{V}_{\text{ee}}$ 的这种拆分提供了一种将波函数理论（WFT）与 DFT 融合的明确途径：即对 RAS-CI 应用 $\hat{V}_{\text{ee}}^{lr,\mu}$，而对 DFT 应用 $V_{\text{ee}}^{lr,\mu}$。
在 RAS-$sr$DFT 方法中，电子态的能量可以表示为：

<a id="Ch7.E168"></a>
$$
E^{\text{RAS-}sr\text{DFT}}=\min_{\Psi^{\mu}}\left[\langle\Psi^{\mu}|\hat{T}+\hat{V}_{ne}+\hat{V}_{ee}^{lr,\mu}|\Psi^{\mu}\rangle+E_{\text{H}}^{sr,\mu}[\rho]+E_{\text{xc}}^{sr,\mu}[\rho]\right] \tag{7.168}
$$

其中 $\rho\equiv\rho[\Psi^{\mu}]$，而 $E_{\text{H}}^{sr,\mu}[\rho]$ 与 $E_{\text{xc}}^{sr,\mu}[\rho]$ 分别为短程 Hartree 能量泛函和交换-关联能量泛函。
RAS-CI 波函数可以与不同的短程交换与关联泛函相结合（第 5.3.3 节 [5.3.3](../ch05_dft/sect_DFTexchange.md) 和第 5.3.4 节 [5.3.4](../ch05_dft/sect_DFTcorrelation.md)）。
