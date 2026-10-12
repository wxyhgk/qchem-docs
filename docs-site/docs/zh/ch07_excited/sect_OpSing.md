---
title: "7.7.3 近似自旋纯化"
---

## 7.7.3 近似自旋纯化

(July 4, 2026)

单重态双自由基（singlet biradicals）是一类重要的特殊情况，其在单行列式自洽场（SCF）框架下的描述通常以显著的自旋污染（spin contamination）为特征，$\langle\hat{S}^{2}\rangle\approx 1$（原子单位），这表明波函数近似为单重态（$\langle\hat{S}^{2}\rangle=0$）与三重态（$\langle\hat{S}^{2}\rangle=2$）的等比例混合。这一现象的根源在于：要对两个半占据轨道中的两个电子给出恰当的描述，至少需要两个行列式。一种简单的修正手段是使用近似自旋纯化（approximate spin-purification）公式，[[1580]](../bib_references/bib.md#bib1643)

<a id="eq:OpSing"></a>

$$
E_{\text{OSS}}\approx 2E_{\text{BS}}-E_{\text{trip}}\;, \tag{7.78}
$$

该公式用破缺对称性（broken-symmetry）解的能量（$E_{\text{BS}}$，即 $\langle\hat{S}^{2}\rangle\approx 1$ 的状态）与三重态能量（$E_{\text{trip}}$）来表示开壳层单重态（open-shell singlet）状态的能量（$E_{\text{OSS}}$）。此公式最初由 Ziegler、Rauk 和 Baerends 提出，[[1580]](../bib_references/bib.md#bib1643)
 但经由 Noodleman 将其应用于金属酶而广为流传。

对公式 ([7.78](#eq:OpSing)) 的求值需要两次独立的 SCF 计算，通过在 *$rem* 段中指定 SPIN_PROJ = NOODLEMAN，即可自动地完成这两次计算；参见示例 [7.7.2](ex_OpSing.md)。该近似自旋纯化方法已实现了解析梯度，同样需要两次独立的 SCF 梯度计算。（不过，即使采用有限差分法也无法获得 Hessian。）对于开壳层单重态这一特定情形，第 [7.7.4](ex_ESROKS.md) 节讨论的 ROKS 方法可以被理解为公式 ([7.78](#eq:OpSing)) 的完全自洽（self-consistent）或轨道优化（orbital-optimized）版本，

 因为其对公式 ([7.78](#eq:OpSing)) 中的两项采用同一组自洽轨道。
相比之下，Noodleman 的近似自旋纯化流程则执行两次独立的 SCF 计算，各自使用不同的轨道。

### `SPIN_PROJ`

> **控制是否执行近似自旋纯化。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不执行自旋纯化。
>     * `NOODLEMAN`: 使用 Noodleman 公式执行自旋纯化，即公式 ( 7.78 )。
> * **建议**: 若需要自旋纯化，请设置为 NOODLEMAN。务必确保 UNRESTRICTED 设置为 TRUE。梯度可用，但 Hessian 不可用。
