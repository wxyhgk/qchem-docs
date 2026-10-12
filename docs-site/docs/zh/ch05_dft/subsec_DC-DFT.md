---
title: "5.12.1 密度校正 DFT（Density-Corrected DFT）"
---

## 5.12.1 密度校正 DFT（Density-Corrected DFT）

（2026 年 7 月 4 日）

众所周知，DFT 中的自相互作用误差（self-interaction error, SIE）会导致开壳层分子中未配对自旋的过度离域。[[262]](../bib_references/bib.md#bib263)

这会带来多种有害影响，包括对三中心两电子“半键（hemibonds）”的过度稳定，[[1145]](../bib_references/bib.md#bib1195)

在充分分离的化学片段中出现分数电荷（*i.e.*，在解离时），[[1553]](../bib_references/bib.md#bib1607)

以及反应势垒过低——后者正是引入杂化密度泛函的主要动机。[[866]](../bib_references/bib.md#bib901)
 尽管多年来人们提出了各种*临时性（ad hoc）*的自相互作用校正方案，但没有一种能令人完全满意。[[630]](../bib_references/bib.md#bib653)

密度校正 DFT（DC-DFT）[[1412]](../bib_references/bib.md#bib1472)
 是对一个古老思想的复兴：[[1017]](../bib_references/bib.md#bib1058)
 通过使用无 SIE 的自洽 Hartree-Fock 密度以非自洽方式评估 DFT 泛函来规避 SIE。之所以避免在 DFT 层级进行自洽迭代，是因为这会将 SIE 重新引入密度。若 $E_{\text{DFT}}[\rho]$
表示用户选定的密度泛函，$E_{\text{HF}}[\rho]$ 表示 Hartree-Fock 泛函，则 DC-DFT 能量泛函为[[1143]](../bib_references/bib.md#bib1197)

<a id="Ch5.E75"></a>

$$
E_{\text{DC-DFT}}[\rho]=E_{\text{DFT}}\Big{[}\operatorname*{arg\,min}_{\rho}\big{(}E_{\text{HF}}[\rho]\big{)}\Big{]} \tag{5.75}
$$

即使 $E_{\text{DFT}}[\rho]$ 是一个半局域泛函，DC-DFT 所能给出的势垒高度在精度上也可与杂化泛函所得结果相媲美。[[629]](../bib_references/bib.md#bib652)
 这实际上并不能降低杂化 DFT 计算的成本，因为 Hartree-Fock 计算必须迭代至自洽；不过 DC-DFT 可作为一种有用的诊断工具。如果某一泛函的 DC-DFT 结果与该泛函的自洽 DFT 结果在定性上不同，那么密度驱动的 SIE 可能正在影响结果。例如，这种诊断能力已被用于检测金属氧化物中极化子（自旋）缺陷的不真实离域现象。[[1144]](../bib_references/bib.md#bib1196)

使用 **Q-Chem** 的 DC-DFT 实现的用户请引用文献 [[1144]](../bib_references/bib.md#bib1196)
。
DC-DFT 的解析能量梯度可用，[[1144]](../bib_references/bib.md#bib1196)
 但由于泛函 $E_{\text{DC-DFT}}$ 未被迭代至自洽，评估梯度 $dE_{\text{DC-DFT}}/dx$ 需要求解耦合微扰（$Z$-vector）方程，[[1399]](../bib_references/bib.md#bib1459)
 这使得梯度计算比传统 DFT 梯度略为昂贵。

**注意：

目前 DC-DFT 的耦合微扰方程以串行方式求解，也就是说，虽然 SCF 迭代是并行化的，
但 $Z$-vector 迭代并未并行化。
**

要执行 DC-DFT 计算，请在 *$rem* 段中设置 METHOD 以选择所需泛函，并设置
DC_DFT = TRUE。注意，由于 $E_{\text{DFT}}[\rho]$ 从不被对角化，因此在 SCF 流程末尾计算的任何后续性质均基于 Hartree-Fock 密度。
这包括单粒子能级、Mulliken 电荷、多极矩等。

### `DC_DFT`

> **控制是否使用 DC-DFT。**
>
> * **类型**: `Boolean`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `FALSE`: 不执行 DC-DFT。
>     * `TRUE`: 在 Hartree-Fock 层级将密度迭代至自洽，然后使用 METHOD 指定的泛函对 $E_{\text{DFT}}[\rho_{\text{HF}}]$ 求值。
> * **建议**: 按需使用。解析梯度可用，但在当前实现中是串行瓶颈。
