---
title: "4.7.1 引言"
---

## 4.7.1 引言

(2026 年 7 月 4 日)

对自洽场（Self-Consistent Field, SCF）能量（HF 或 DFT）而言，双基组（dual-basis）近似[[825]](../bib_references/bib.md#bib859)
提供了一种高效的方法，能够以远低于在大基组中进行完整 SCF 计算的成本，获得大基组效应。首先，在选定的小基组（由 BASIS2 指定）中执行一次完整的 SCF 计算。然后，在较大的目标基组（照例由 BASIS 指定）中执行一步类 SCF（SCF-like）计算，以微扰方式近似大基组能量。该修正相当于在单步大基组计算之后，对密度矩阵变化量的一阶近似：

<a id="Ch4.E64"></a>
$$
E_{\text{total}}=E_{\text{small basis}}+\mbox{tr}[(\Delta\mathbf{P})\mathbf{F}]_{\text{large basis}}\;. \tag{4.64}
$$

这里的 $\mathbf{F}$（在大基组中）由已收敛的（小基组）密度矩阵构建。因此，在大基组中只需要构建一次 Fock 矩阵。目前可用的是 HF 与 DFT 能量（SP）以及解析一阶导数（FORCE 或 OPT）。

**注意：

自 4.0 版起，非限制（unrestricted）双基组 DFT 能量的一阶导数虽然结果正确，但代码效率上尚需改进。在该改进完成之前，我们不建议使用这些导数。
**

在包含 223 个分子的 G3 集[[296]](../bib_references/bib.md#bib297)
上，使用 cc-pVQZ 时，B3LYP 的双基组误差为 0.04 kcal/mol（能量）和 0.03 kcal/mol（梯度）。
