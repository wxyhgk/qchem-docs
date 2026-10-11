---
title: "12.6.4 冻结能的进一步分解"
---

## 12.6.4 冻结能的进一步分解

（2026 年 7 月 4 日）

ALMO-EDA 中的冻结相互作用能（frozen interaction energy）定义为非弛豫冻结（Heitler-London）波函数与孤立碎片之间的能量差。在其他文献中，[[1408]](../bib_references/bib.md#bib1467)
 这种相互作用常被以经典方式分解为：

<a id="eq:cls_decomp"></a>
$$
\Delta E_{\mathrm{frz}}=\Delta E_{\mathrm{elec}}^{\mathrm{cls}}+\Delta E_{\mathrm{Pauli}}^{\mathrm{cls}}, \tag{12.8}
$$

其中永久静电（permanent electrostatics）贡献定义为孤立碎片电荷分布之间的库仑相互作用：

<a id="eq:cls_elec"></a>
$$
\Delta E_{\mathrm{elec}}^{\mathrm{cls}}=\sum_{A<B}\int_{r_{1}}\int_{r_{2}}\rho_{A}^{\mathrm{tot}}({\textbf{r}_{1}})\frac{1}{{\textbf{r}_{12}}}\rho_{B}^{\mathrm{tot}}({\textbf{r}_{2}})\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2} \tag{12.9}
$$

余项则构成泡利（Pauli，或交换）项。这样的分解（下文称为经典分解）存在两个问题：(i) 永久静电的计算使用的是“前分子”（promolecule）态（其密度仅为各单体密度的简单加和），而非经过正确反对称化的波函数；(ii) 当使用色散校正的密度泛函时，泡利项中会包含色散相互作用，从而失去其原始含义。

Horn *et al.*[[595]](../bib_references/bib.md#bib619)
 提出了一种新方案，将冻结项进一步分解为永久静电（ELEC）、泡利排斥（PAULI）和色散（DISP）三部分贡献：

<a id="eq:new_decomp"></a>
$$
\Delta E_{\mathrm{frz}}=\Delta E_{\mathrm{elec}}+\Delta E_{\mathrm{Pauli}}+\Delta E_{\mathrm{disp}} \tag{12.10}
$$

该方法与除双杂化泛函之外的所有密度泛函均兼容，并且 FRZ 项的三个分量都使用反对称化的冻结波函数来计算。此方法的关键步骤是将与冻结波函数相关的一阶密度矩阵（1PDM）正交分解为各碎片的贡献：
$\mathbf{P}_{\mathrm{frz}}=\sum_{A}\tilde{\mathbf{P}}_{A}$。这一分解通过最小化如下目标函数来实现：

<a id="eq:kep_obj"></a>
$$
\Omega=\sum_{A}E_{A}[\tilde{\mathbf{P}}_{A}]-E_{A}[\mathbf{P}_{A}] \tag{12.11}
$$

同时在碎片密度矩阵 $\tilde{\mathbf{P}}_{A}$ 之间强制施加碎片间正交性；见参考文献 [[595]](../bib_references/bib.md#bib619)
。

ELEC 项随后定义为畸变（distorted）碎片密度（$\tilde{\rho}_{A}(\mathbf{r})$）之间的库仑相互作用：

<a id="eq:eda_elec"></a>
$$
\Delta E_{\mathrm{elec}}=\sum_{A<B}\int_{r_{1}}\int_{r_{2}}\tilde{\rho}_{A}^{\mathrm{tot}}({\textbf{r}_{1}})\frac{1}{{\textbf{r}_{12}}}\tilde{\rho}_{B}^{\mathrm{tot}}({\textbf{r}_{2}})\mathrm{d}\mathbf{r}_{1}\mathrm{d}\mathbf{r}_{2}. \tag{12.12}
$$

DISP 项通过从总交换-关联（XC）相互作用中减去其无色散（dispersion-free）部分来求得，其中需在使用主（目标）XC 泛函的同时配合使用一个辅助的“无色散”（dispersion-free）XC（DFXC）泛函：

<a id="eq:eda_disp"></a>
$$
\Delta E_{\mathrm{disp}}=\left(E_{\mathrm{xc}}[\mathbf{P}_{\mathrm{frz}}]-\sum_{A}E_{\mathrm{xc}}[\tilde{\mathbf{P}}_{A}]\right)-\left(E_{\mathrm{xc}}^{\mathrm{DF}}[\mathbf{P}_{\mathrm{frz}}]-\sum_{A}E_{\mathrm{xc}}^{\mathrm{DF}}[\tilde{\mathbf{P}}_{A}]\right). \tag{12.13}
$$

已有研究建议[[896]](../bib_references/bib.md#bib933)
，对于包含色散或经色散校正的杂化泛函（如 $\omega$B97M-V 或 B3LYP-D3），HF 是合适的 DFXC；而对于半局域泛函（如 B97M-V），revPBE 更为合适。

冻结相互作用中的剩余部分归入 PAULI 项，其包含由式 ([12.11](#eq:kep_obj)) 给出的净排斥相互作用，以及 XC 相互作用的“无色散”部分：

<a id="eq:eda_pauli"></a>
$$
\Delta E_{\mathrm{Pauli}}=\sum_{A}(E_{A}[\tilde{\mathbf{P}}_{A}]-E_{A}[\mathbf{P}_{A}])+\left(E_{\mathrm{xc}}^{\mathrm{DF}}[\mathbf{P}_{\mathrm{frz}}]-\sum_{A}E_{\mathrm{xc}}^{\mathrm{DF}}[\tilde{\mathbf{P}}_{A}]\right). \tag{12.14}
$$

如有需要，PAULI 项与 ELEC 项也可以合并，作为无色散冻结（dispersion-free frozen，DFFRZ）项报告。

在 **Q-Chem** 的 “EDA2” 实现中，经典冻结分解以及由式 ([12.12](#eq:eda_elec))–([12.14](#eq:eda_pauli)) 定义的新方案默认都会计算。经典的 ELEC 项仅依赖于单体性质和碎片间距离，因此在力场开发等场景中特别有用（可作为永久静电的参考值）。当新方案计算出的 DISP 项可用时，程序还会报告一个修正的经典泡利项[[893]](../bib_references/bib.md#bib927)
，其定义非常简单：

<a id="Ch12.E15"></a>
$$
\Delta E_{\mathrm{Pauli}}^{\mathrm{mod}}=\Delta E_{\mathrm{Pauli}}^{\mathrm{cls}}-\Delta E_{\mathrm{disp}}\;. \tag{12.15}
$$

也就是说，从按原始定义计算的经典泡利项中扣除色散贡献。采用经典方案时，冻结能的整体分解为：

<a id="Ch12.E16"></a>
$$
\Delta E_{\mathrm{frz}}=\Delta E^{\mathrm{cls}}_{\mathrm{elec}}+\Delta E^{\mathrm{mod}}_{\mathrm{Pauli}}+\Delta E_{\mathrm{disp}}\;. \tag{12.16}
$$

或者，也可以通过将 EDA_CLS_DISP 设为 TRUE，在不执行正交分解的情况下实现这一点。
此时同样使用式 ([12.13](#eq:eda_disp)) 计算 DISP 项，只不过使用的是未畸变的单体密度
（$\{\mathbf{P}_{A}\}$）而非其畸变后的对应量（$\{\tilde{\mathbf{P}}_{A}\}$）：

<a id="Ch12.E17"></a>
$$
\Delta E_{\mathrm{disp}}=\left(E_{\mathrm{xc}}[\mathbf{P}_{\mathrm{frz}}]-\sum_{A}E_{\mathrm{xc}}[\mathbf{P}_{A}]\right)-\left(E_{\mathrm{xc}}^{\mathrm{DF}}[\mathbf{P}_{\mathrm{frz}}]-\sum_{A}E_{\mathrm{xc}}^{\mathrm{DF}}[\mathbf{P}_{A}]\right). \tag{12.17}
$$

FRZ_ORTHO_DECOMP

### `FRZ_ORTHO_DECOMP`

> **基于与冻结波函数关联的一阶密度矩阵（1PDM）的正交分解，执行冻结相互作用能的分解。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE (automatically set to`
> * **选项**:
>     * FALSE
>     * 不执行正交分解。
>     * TRUE
>     * 使用正交碎片密度执行冻结能分解。
> * **建议**: 使用由 "EDA2" 自动设置的默认值。注意，用户可以通过将其设置为 $-1$ 来关闭正交分解。此外，对于涉及有效核势（ECP）的计算，该值会被自动设置为 FALSE，否则会产生不合理的结果。

FRZ_ORTHO_DECOMP_CONV

### `FRZ_ORTHO_DECOMP_CONV`

> **用于求解正交碎片密度的最小化问题的收敛判据。**
>
> * **类型**: `INTEGER`
> * **默认值**: `6`
> * **选项**:
>     * $n$
>     * $10^{-n}$
> * **建议**: 除非需要更严格的收敛标准，否则使用默认值。

EDA_CLS_ELEC

### `EDA_CLS_ELEC`

> **对冻结项执行经典分解。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE (automatically set to`
> * **选项**:
>     * FALSE
>     * 不计算经典的 ELEC 项和 PAULI 项。
>     * TRUE
>     * 执行经典分解。
> * **建议**: TRUE

EDA_CLS_DISP

### `EDA_CLS_DISP`

> **在不执行正交分解的情况下计算 DISP 贡献，随后将其从经典 PAULI 项中扣除。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 使用通过正交分解计算得到的 DISP 项（如果可用）。
>     * TRUE
>     * 使用基于未畸变单体密度（undistorted monomer densities）计算得到的 DISP 项。
> * **建议**: 当不执行正交分解时，将其设置为 TRUE。

DISP_FREE_X

### `DISP_FREE_X`

> **指定所采用的"无色散"（dispersion-free）交换泛函。**
>
> * **类型**: `STRING`
> * **默认值**: `HF`
> * **选项**:
>     * Q-Chem 所支持的交换泛函（
>     * 例如
>     * revPBE）或交换-关联泛函（
>     * 例如
>     * B3LYP）。
> * **建议**: 对于杂化（主）泛函（例如 $\omega$ B97X-V）推荐使用 HF，对于半局域泛函（例如 B97M-V）推荐使用 revPBE。其他合理选项（例如对 B3LYP-D3 使用 B3LYP）亦可采用。

DISP_FREE_C

### `DISP_FREE_C`

> **指定所采用的"无色散"（dispersion-free）关联泛函。**
>
> * **类型**: `STRING`
> * **默认值**: `NONE`
> * **选项**:
>     * Q-Chem 所支持的关联泛函。
> * **建议**: 填入与所选交换泛函相匹配的关联泛函（例如，若 DISP_FREE_X 设为 revPBE，则填入 PBE）；若 DISP_FREE_X 设为某个交换-关联泛函，则填入 NONE。
