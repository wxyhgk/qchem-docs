---
title: "7.10.3 IP- 与 EA-ADC"
---

## 7.10.3 IP- 与 EA-ADC

（2026 年 7 月 4 日）

与极化传播子（ADC）的 ADC 方案类似，该流程同样可以应用于电子传播子的 $(N-1)$ 与 $(N+1)$ 部分，电子传播子以其谱表示形式给出为

<a id="Ch7.E140"></a>

$$
G_{pq}(\omega)=\underbrace{\sum_{n}\frac{\bigl{\langle}\Psi_{0}^{N}\bigl{\lvert}c_{p}\bigr{\rvert}\Psi_{n}^{N+1}\bigr{\rangle}\bigl{\langle}\Psi_{n}^{N+1}\bigl{\lvert}c_{q}^{\dagger}\bigr{\rvert}\Psi_{0}^{N}\bigr{\rangle}}{\omega+E_{0}^{N}-E_{n}^{N+1}}}_{(N+1)\text{-electron (EA) part}}+\underbrace{\sum_{n}\frac{\bigl{\langle}\Psi_{0}^{N}\bigl{\lvert}c_{q}^{\dagger}\bigr{\rvert}\Psi_{n}^{N-1}\bigr{\rangle}\bigl{\langle}\Psi_{n}^{N-1}\bigl{\lvert}c_{p}\bigr{\rvert}\Psi_{0}^{N}\bigr{\rangle}}{\omega+E_{n}^{N-1}-E_{0}^{N}}}_{(N-1)\text{-electron (IP) part}}. \tag{7.140}
$$

据此，已推导出了微扰理论三阶以内的（非 Dyson）IP- 与 EA-ADC 方法。[[1208]](../bib_references/bib.md#bib1263)

与极化传播子的 ADC 方案情形相同，同样的工作方程也可通过 ISR 形式体系推导得出，与上一节 [7.10.2](sec_adc_pp_scheme.md) 所示流程的唯一区别在于激发算符

<a id="A3.S8.EGx63"></a>

$$
\displaystyle\left\{\hat{C}_{J}^{N-1}\right\} \tag{7.141}
$$

取代了方程 ([7.133](sec_adc_pp_scheme.md#eq:adc_pp_precursor_states)) 中守恒电子数的算符 $\hat{C}_{J}$。

对 IP- 与 EA-ADC 久期矩阵（secular matrix）$\mathbf{M}$ 进行对角化，分别可得到电子脱附能（即电离势，IPs）和电子附着能（即负电子亲和能，EAs）。
此外，$(N-1)$ 与 $(N+1)$ 跃迁的相对谱强度可通过极点强度（pole strength）$P_{n}$ 获得，其计算方式为

<a id="Ch7.E143"></a>

$$
P_{n}=\sum_{p}\left|x_{pn}\right|^{2}, \tag{7.143}
$$

其中 $x_{pn}$ 为谱因子（spectroscopic factor），利用 IP- 与 EA-ADC 的本征向量 $\mathbf{X}$ 以及有效跃迁振幅矩阵 $\mathbf{f}$，按下述关系式计算得到

<a id="A3.S8.EGx64"></a>

$$
\displaystyle x_{pn}^{N-1} \tag{7.144}
$$

当请求计算电子脱附态或电子附着态时，极点强度会被自动计算。对于 IP- 与 EA-ADC(2) 计算，采用二阶极点强度 [*即*，在计算中使用 IP- 与 EA-ADC(2) 的 $\mathbf{f}$ 矩阵]。如文献 [[1208]](../bib_references/bib.md#bib1263)
 所建议的，出于计算成本考虑，在严格的 IP- 与 EA-ADC(3) 计算中同样计算二阶极点强度，*即*，在整个 $\mathbf{M}$ 矩阵方程中始终使用二阶基态密度，即设置 ADC_DENSITY_ORDER = 2。当请求使用更高阶的基态密度时，*例如*，设置 ADC_DENSITY_ORDER = 3（对应 $\Sigma(4)$ 方案[[1372]](../bib_references/bib.md#bib1435)
）或 ADC_DENSITY_ORDER = 4（对应 $\Sigma(4+)$ 方案[[1372]](../bib_references/bib.md#bib1435)
，亦称为标准 IP- 与 EA-ADC(3) 方案），则使用相应的极点强度，*即*，在 $\Sigma(4)$ 情形下使用三阶极点强度，在 $\Sigma(4+)$ 情形下使用改进的三阶极点强度。

谱因子还可用于计算与电子脱附和附着过程相关的 Dyson 轨道 $|\phi_{n}\rangle$

<a id="Ch7.E146"></a>

$$
\left|\phi_{n}\right>=\sum_{p}x_{pn}\left|\varphi_{p}\right>, \tag{7.146}
$$

其中后一关系式中的 $\varphi_{p}$ 表示 HF 轨道。Dyson 轨道的输出通过设置
ADC_DO_DYSON = TRUE 并结合
STATE_ANALYSIS = TRUE 来触发。另见第 [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) 节了解更多细节。
