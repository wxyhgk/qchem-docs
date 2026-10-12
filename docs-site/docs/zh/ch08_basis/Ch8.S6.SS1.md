---
title: "8.6.1 概述"
---

## 8.6.1 概述

（2026 年 7 月 4 日）

在 **Q-Chem** 中有若干类型的计算可以使用*两*套原子轨道基组（atomic orbital basis set）来完成，而不是本章到目前为止所假设的仅使用一套。这类计算被称为涉及*双*基组（dual basis sets）。迭代通常在较小的主基组（primary basis）中进行，该基组由 *$rem* 关键字 BASIS2 指定。可以使用双基组执行的计算示例包括：

- •

为大基组中的自洽场（SCF）计算提供更好的初始猜测。参见第 [4.4.5](../ch04_scf/sect_projection.md) 节。
- •

双基组自洽场计算（Hartree-Fock 与密度泛函理论（Density Functional Theory, DFT））。相关讨论参见第 [4.7](../ch04_scf/sect_dualbasis.md) 节。
- •

通过 “triple jumping”（三重跳跃）方式进行密度泛函的微扰修正。参见第 [4.8](../ch04_scf/sect_HFPC.md) 节。
- •

双基组 MP2 计算。相关讨论参见第 [6.6.2](../ch06_correlation/sect_rimp2.md) 节。

### `BASIS2`

> **定义（较小的）第二套基组。**
>
> * **类型**：`STRING`
> * **默认值**：`第二基组没有默认值。`
> * **选项**：
>     * 符号
>     * 与 BASIS
>     * 一样使用标准基组
>     * 。
>     * BASIS2_GEN
>     * 通用
>     * BASIS2_MIXED
>     * 混合
> * **建议**：应当比 BASIS 指定的基组更小。当仅用于提供初始猜测时，使用比极小基组（minimal basis）更大的基组几乎没有优势。双基组计算可使用更大的标准化选项，如第 4.7 节所述，并在表 4.2 中总结。

除了 BASIS2 内置的基组之外，还可以通过额外的 *$basis2* 输入节（input section）来输入用户自定义的第二套基组，其语法一般遵循上文第 [8.4](sect_userbasis.md) 节中记录的 *$basis* 输入节的规范。
