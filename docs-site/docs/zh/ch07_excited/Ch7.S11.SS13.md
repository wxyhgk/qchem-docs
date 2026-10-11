---
title: "7.11.13 casman 的作业控制选项"
---

## 7.11.13 **casman** 的作业控制选项

（2026 年 7 月 4 日）

在 **casman** 中，只需相应地设置 CORRELATION 的值，即可运行内置方法（built-in methods）：

CORRELATION

### `CORRELATION`

> **设置 casman 所使用的预定义方法。**
>
> * **类型（Type）**: `STRING`
> * **默认值（Default）**: `无（None）。`
> * **选项（Options）**:
>     * SF-CAS
>     * 不带微扰修正（perturbative corrections）的 CAS-SF（或自定义方法）
>     * SF-CAS(h,p)
>     * 对空穴（hole，h）与粒子（particle，p）激发引入微扰修正的 CAS-SF
>     * SF-CAS(S)
>     * 对单激发（single，h、p、hp）引入微扰修正的 CAS-SF
>     * SF-CAS(2x)
>     * 对 2x（h、p、hp、hh、pp）激发引入微扰修正的 CAS-SF
>     * SF-CAS(3x)
>     * 对 3x（h、p、hp、hh、pp、hhp、hpp）激发引入微扰修正的 CAS-SF
>     * SF-CAS(3x)+D
>     * 对（h、p、hp、hh、pp、hhp、hpp）激发引入微扰修正，并加上 MP2 处理 RAS1
> * $\rightarrow$
>     * RAS3 双激发
> * **建议（Recommendation）**: 无。

如果需要自定义的激发方案（excitation scheme），可以设置 CORRELATION = SF-CAS，
并手动设置下列变量。（若使用某个内置方法，则应避免手动设置这些变量，因为当 CORRELATION 不是 SF-CAS 时，
**Q-Chem** 会自动对其进行恰当的设置。）

RAS_N_SPIN_FLIP

### `RAS_N_SPIN_FLIP`

> **设置自旋翻转（spin-flip）的数目。**
>
> * **类型（Type）**: `INTEGER`
> * **默认值（Default）**: `自旋翻转的最大数目（`
> * **选项（Options）**:
>     * $n$
>     * 执行
>     * $n$
>     * 次自旋翻转
> * **建议（Recommendation）**: 无。

CAS_DO_NDPT

### `CAS_DO_NDPT`

> **是否使用非简并微扰理论（non-degenerate perturbation theory）？**
>
> * **类型（Type）**: `LOGICAL`
> * **默认值（Default）**: `FALSE`
> * **选项（Options）**:
>     * TRUE
>     * 使用非简并微扰理论。
>     * FALSE
>     * 不使用非简并微扰理论。
> * **建议（Recommendation）**: 无。

CAS_QDPT_ORDER

### `CAS_QDPT_ORDER`

> **准简并微扰理论（quasi-degenerate perturbation theory）分母展开中保留到几阶项。**
>
> * **类型（Type）**: `INTEGER`
> * **默认值（Default）**: `无（None）。`
> * **选项（Options）**:
>     * $n$
>     * 在分母展开中保留
>     * $n$
>     * 阶的项。
> * **建议（Recommendation）**: 无。

CAS_DO_1X

### `CAS_DO_1X`

> **是否执行空穴（h）与粒子（p）的微扰修正？**
>
> * **类型（Type）**: `LOGICAL`
> * **默认值（Default）**: `FALSE`
> * **选项（Options）**:
>     * TRUE
>     * 执行空穴（h）与粒子（p）的微扰修正
>     * FALSE
>     * 不执行空穴（h）与粒子（p）的微扰修正
> * **建议（Recommendation）**: 无。

CAS_DO_SINGLES

### `CAS_DO_SINGLES`

> **是否执行单激发（h、p、hp）的微扰修正？**
>
> * **类型（Type）**: `LOGICAL`
> * **默认值（Default）**: `FALSE`
> * **选项（Options）**:
>     * TRUE
>     * 执行单激发的微扰修正
>     * FALSE
>     * 不执行单激发的微扰修正
> * **建议（Recommendation）**: 无。

CAS_DO_2x

### `CAS_DO_2x`

> **是否执行 2x（h、p、hp、hh、pp）的微扰修正？**
>
> * **类型（Type）**: `LOGICAL`
> * **默认值（Default）**: `FALSE`
> * **选项（Options）**:
>     * TRUE
>     * 执行 2x 的微扰修正
>     * FALSE
>     * 不执行 2x 的微扰修正
> * **建议（Recommendation）**: 无。

CAS_DO_3x

### `CAS_DO_3x`

> **是否执行 3x（h、p、hp、hh、pp、hhp、hpp）的微扰修正？**
>
> * **类型（Type）**: `LOGICAL`
> * **默认值（Default）**: `FALSE`
> * **选项（Options）**:
>     * TRUE
>     * 执行 3x 的微扰修正
>     * FALSE
>     * 不执行 3x 的微扰修正
> * **建议（Recommendation）**: 无。

CAS_DO_DOUBLES

### `CAS_DO_DOUBLES`

> **是否执行（h、p、hp、hh、pp、hhp、hpp）的微扰修正 + MP2 处理的 RAS1 $\rightarrow$ RAS3 双激发修正？**
>
> * **类型（Type）**: `LOGICAL`
> * **默认值（Default）**: `FALSE`
> * **选项（Options）**:
>     * TRUE
>     * 执行（h、p、hp、hh、pp、hhp、hpp）微扰修正 + MP2 处理的 RAS1
>     * $\rightarrow$
>     * RAS3 双激发修正
>     * FALSE
>     * 不执行该修正
> * **建议（Recommendation）**: 无。

CAS_LEVEL_SHIFT

### `CAS_LEVEL_SHIFT`

> **是否对分母使用能级平移（level-shift）？**
>
> * **类型（Type）**: `LOGICAL`
> * **默认值（Default）**: `FALSE`
> * **选项（Options）**:
>     * TRUE
>     * 对分母使用能级平移
>     * FALSE
>     * 不对分母使用能级平移
> * **建议（Recommendation）**: 无。

CAS_SPARSE

### `CAS_SPARSE`

> **在构造有效哈密顿量（effective Hamiltonian）时是否使用稀疏矩阵乘法？**
>
> * **类型（Type）**: `LOGICAL`
> * **默认值（Default）**: `FALSE`
> * **选项（Options）**:
>     * TRUE
>     * 在构造有效哈密顿量时使用稀疏矩阵乘法
>     * FALSE
>     * 在构造有效哈密顿量时不使用稀疏矩阵乘法
> * **建议（Recommendation）**: 无。对于较大的自旋翻转数目，该选项可能很有用。
