---
title: "4.6.7 PARI-K 快速交换算法"
---

## 4.6.7 PARI-K 快速交换算法

(2026年7月4日)

PARI-K[[891]](../bib_references/bib.md#bib925)
 是一种能够显著加速
在具有大基组的 Hartree-Fock（哈特里-福克）方法与杂化密度泛函理论（Hybrid Density Functional Theory, DFT）计算中交换矩阵（exchange matrix）构建的算法。这一加速之所以成为可能，是因为它仅利用位于各自原子上的辅助基函数（auxiliary basis functions）来拟合原子轨道（atomic orbital）的乘积。
**Q-Chem** 中的 PARI-K 实现是一种高效的分子轨道基（MO-basis）表述形式，类似于 Merlot *et al.*[[938]](../bib_references/bib.md#bib978)
 提出的原子轨道基（AO-basis）表述形式。对于使用 aug（增强）三重-ζ（triple-zeta）或更大基组的计算，强烈推荐使用 PARI-K，并且应将其与用于构建库仑矩阵（Coulomb matrix）的标准 RI-J 算法结合使用。[[1442]](../bib_references/bib.md#bib1502)
 推荐将与 Weigend[[1442]](../bib_references/bib.md#bib1502)
 开发的交换拟合基组（cc-pVTZ-JK 和 cc-pVQZ-JK）与 PARI-K 配合使用。与 PARI-K 近似相关的误差看起来仅比标准 RI-HF 略高。[[938]](../bib_references/bib.md#bib978)

### `PARI_K`

> **控制在交换矩阵的构建中是否使用 PARI-K 近似**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `TRUE`: 使用 PARI-K。
> * **建议**: 用于 aug-cc-pVTZ 及更大的基组。
