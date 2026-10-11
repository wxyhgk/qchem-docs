---
title: "5.2 Kohn-Sham 密度泛函理论"
---

# 5.2 Kohn-Sham 密度泛函理论

(July 4, 2026)

由 Hohenberg、Kohn 和 Sham 建立的密度泛函理论（Density Functional Theory, DFT）[[587]](../bib_references/bib.md#bib610)
 源于 Dirac 的早期工作,[[329]](../bib_references/bib.md#bib333)
 Dirac 证明了均匀电子气的交换能可以直接仅由电荷密度精确计算。然而,这种传统的*密度*泛函方法(如今称为"免轨道"(orbital-free) DFT)虽然直接与密度本身建立联系,但实际上很难为动能泛函获得像样的近似。
Kohn 和 Sham 通过一种间接方法回避了这一困难:在该方法中,动能由一个非相互作用的参考系统精确计算,这个参考系统就是 Kohn-Sham 行列式。[[701]](../bib_references/bib.md#bib732)

正是 Kohn-Sham 方法首次使 DFT 成为一种实用的计算工具。

在 Kohn-Sham 形式体系内,[[701]](../bib_references/bib.md#bib732)
 基态电子能量 $E$ 可以写为

<a id="eq:DFT_energy_components"></a>

$$
E=E_{\text{T}}+E_{\text{V}}+E_{\text{J}}+E_{\text{XC}} \tag{5.1}
$$

其中 $E_{\text{T}}$ 是动能,$E_{\mathrm{V}}$ 是电子–核相互作用能,$E_{\text{J}}$ 是电子密度 $\rho(\mathbf{r})$ 的库仑自相互作用能,而 $E_{\text{XC}}$ 是交换-关联能。采用非限制性(unrestricted)形式,$\alpha$ 和 $\beta$ 的总电子密度可以写为

<a id="eq429"></a>

$$
\displaystyle\rho_{\alpha}(\mathbf{r}) \tag{5.2a}
$$

其中 $n_{\alpha}$ 和 $n_{\beta}$ 分别是 $\alpha$ 电子和 $\beta$ 电子的数目,$\psi_{i}$ 是 Kohn-Sham 轨道。于是,总电子密度为

<a id="eq430"></a>

$$
\rho(\mathbf{r})=\rho_{\alpha}(\mathbf{r})+\rho_{\beta}(\mathbf{r}) \tag{5.3}
$$

在有限基组(basis set)中,密度表示为[[1112]](../bib_references/bib.md#bib1163)

<a id="eq431"></a>

$$
\rho(\mathbf{r})=\sum_{\mu\nu}P_{\mu\nu}\phi_{\mu}(\mathbf{r})\phi_{\nu}(\mathbf{r})\;, \tag{5.4}
$$

其中 $P_{\mu\nu}$ 是一电子密度矩阵的元素;参见 Hartree-Fock 理论讨论中的式 ([4.24](../ch04_scf/Ch4.S2.SS2.md#eq:P(mu,nu)))。式 ([5.1](#eq:DFT_energy_components)) 中的各项能量分量现在可以写为

<a id="A3.S8.EGx16"></a>

$$
\displaystyle E_{\mathrm{T}} \tag{5.5}
$$

对未知的 Kohn-Sham 轨道系数求 $E$ 的极小值,可得到一组与 UHF 情形的 Pople-Nesbet 方程(式 ([4.13](../ch04_scf/Ch4.S2.SS1.md#eq:Pople-Nesbet)))完全类似的矩阵方程,只是 Fock 矩阵元有所修改 [*cf*. 式 ([4.27](../ch04_scf/Ch4.S2.SS2.md#eq:F(mu,nu)))]

<a id="eq437"></a>

$$
\displaystyle F_{\mu\nu}^{\alpha} \tag{5.9a}
$$

这里,$\mathbf{F}^{\mathrm{XC}\alpha}$ 和 $\mathbf{F}^{\mathrm{XC}\beta}$ 是 Fock 矩阵的交换-关联部分,其形式取决于所使用的交换-关联泛函。只需取 $F_{\mu\nu}^{\mathrm{XC}\alpha}=K_{\mu\nu}^{\alpha}$(对 $\beta$ 同理),即可将 UHF 理论恢复为一个特例。
因此,密度和能量的求解方式与 HF 方法类似。先对分子轨道(MO)系数给出初始猜测,然后应用迭代过程直至达到自洽。
