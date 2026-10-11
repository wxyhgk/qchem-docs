---
title: "5.13.2 CAP-DFT 作业控制"
---

## 5.13.2 CAP-DFT 作业控制

（2026 年 7 月 4 日）

## 5.13.2.1 *$rem* 变量与关键字选项

在 *$rem* 中添加 CAP_SCF = TRUE 即可请求进行 CAP-DFT 计算。
目前，可与复变泛函（complex-variable functional）组合使用的泛函集合仍然有限，
有关如何指定期望泛函的说明请参见第 [5.13.3](sub_XCfuncs_CAP.md) 节。

CAP 参数应在 *$rem* 部分中指定。
其可用的关键字及取值与 CAP-CC 计算中所使用的相同：

- •

CAP_ETA，用于设置 CAP 强度 $\eta$。

$\eta$ 的最优值通常通过最小化 $\left|\eta dE/d\eta\right|$ 来确定。
- •

CAP_TYPE，用于指定 CAP 类型（cubic、spherical 或 Voronoi）。
- •

CAP_X/Y/Z，用于指定 CAP 的作用起始位置（onset）。

有关这些关键字的更多细节，请参见第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节。

用于 CAP 积分的网格可通过 CAP_GRID 关键字指定。
其可选取值（见下文）与 XC_GRID（第 [5.5](sect_quadrature.md) 节）相同。
CAP_GRID_SWITCH 和 CAP_NEW_GRID 关键字可用于在 SCF 迭代过程中
在另一个网格上重新计算 CAP。
有关这些关键字的详细信息见下文。

**注意：

此处所述方法同样适用于 CAP-HF 计算，只需将 METHOD = HF 而非某个复变泛函即可。
CAP-HF 也可以通过旧的实现方式来访问，
方法是在 *$complex_ccman* 中设置 CS_HF = 1（参见第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节）；
然而，该旧方式不能用于调用 CAP-DFT 计算，
并且关键字 CAP_GRID、CAP_GRID_SWITCH 和 CAP_NEW_GRID 将不被识别。
**

CAP_SCF

### `CAP_SCF`

> **调用一次 CAP-SCF 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 使用较新的实现方式调用 CAP-SCF 计算，该实现同时支持 CAP-DFT 计算。
>     * FALSE
>     * 不使用较新的实现方式调用 CAP-SCF 计算。
> * **建议**: 对于 CAP-DFT 计算，或者当希望在 SCF 迭代过程中在另一个网格上重新计算 CAP 时，设置为 'TRUE'（另见 CAP_GRID_SWITCH 和 CAP_NEW_GRID）。

CAP_GRID

### `CAP_GRID`

> **指定用于 CAP 积分的网格类型。其选项与 $rem 变量 XC_GRID 的选项相同。**
>
> * **类型**: `INTEGER`
> * **默认值**: `If`
> * **选项**:
>     * 0
>     * 对 H、C、N 和 O 使用 SG-0；对所有其他原子使用 SG-1。
>     * $n$
>     * 对所有原子使用 SG-
>     * $n$
>     *，其中
>     * $n=1,2,$
>     * 或
>     * $3$
>     *。
>     * $XY$
>     * 由两个六位整数组成的字符串
>     * $X$
>     * 和
>     * $Y$
>     *，其中
>     * $X$
>     * 是径向点数，
>     * $Y$
>     * 是角向点数，此处角向点数须为 Lebedev 角向点数
>     * 的允许值，取自第
>     * 5.5
>     * 节的表
>     * 5.2
>     *。
>     * $-XY$
>     * Gauss-Legendre 网格的类似格式，其中六位整数
>     * $X$
>     * 对应
>     * 径向点数，六位整数
>     * $Y$
>     * 给出
>     * Gauss-Legendre 角向点数，
>     * $Y=2N^{2}$
>     *。
> * **建议**: 在初始 SCF 迭代中使用较粗糙的 CAP 网格可能有助于找到共振态，而使用较精细的网格可能改善收敛行为。另见 CAP_GRID_SWITCH 和 CAP_NEW_GRID。

CAP_GRID_SWITCH

### `CAP_GRID_SWITCH`

> **指定从第几次 SCF 迭代开始在新网格上重新计算 CAP。另见 CAP_NEW_GRID。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * $n$
>     * 从第
>     * $n$
>     * 次 SCF 迭代开始在新网格上重新计算 CAP。
> * **建议**: 最优值取决于体系。应让初始 CAP 网格执行足够多次的迭代，以确保找到共振态。

CAP_NEW_GRID

### `CAP_NEW_GRID`

> **指定用于重新计算 CAP 的新网格。重新计算从 CAP_GRID_SWITCH 所指示的第 $n^{\text{th}}$ 次 SCF 迭代开始。**
>
> * **类型**: `INTEGER`
> * **默认值**: `99000590`
> * **选项**:
>     * 与
>     * CAP_GRID
>     * 的选项相同（见上文）。
> * **建议**: 使用比 CAP_GRID 更精细的网格。

## 5.13.2.2 使用 CAP-DFT 寻找临时阴离子的共振态

临时阴离子的共振态在电子组态空间中形式上表现为激发电子态。
因此，SCF 过程收敛到目标态并不总是 straightforward 的。
此外，已观察到 CAP-DFT 计算比 CAP-HF 计算更难收敛。[[1359]](../bib_references/bib.md#bib1419)

本节因此列出一些提高收敛可能性的技巧。

- •

提供高质量的 SCF 猜测密度矩阵（guess density matrix）至关重要。
示例包括但不限于：

- **–**

在相同 $\eta$ 值下收敛得到的 CAP-HF 密度矩阵。
- **–**

使用相同泛函、在相近 $\eta$ 值下收敛得到的 CAP-DFT 密度矩阵。
- **–**

使用相同泛函、并采用施加少量附加电荷的电荷稳定化（charge stabilization）方法收敛得到的 DFT 密度矩阵。
有关电荷稳定化使用的更多细节，请参见第 [7.9.13](../ch07_excited/sec_CAGE.md) 节。
- **–**

使用相同泛函、在相同 $\eta$ 值下、并采用施加少量附加电荷的电荷稳定化方法收敛得到的 CAP-DFT 密度矩阵。
- •

强烈推荐使用最大重叠方法（maximum overlap method, MOM，参见第 [7.7.2](../ch07_excited/ex_OpSing.md) 节）。
- •

已发现 CAP-DFT 计算需要非常精细的网格来进行交换-关联（XC）数值求积，
其精细程度高于常规（实变量）DFT 计算所需。
有关设置 XC 网格的详细信息，请参见第 [5.5](sect_quadrature.md) 节。
- •

在初始 SCF 迭代中使用较粗糙的 CAP 网格可能有助于找到共振态，
而使用较精细的网格可能改善收敛行为。
有关设置 CAP 网格的详细信息，请参见第 5.13.2 节。
