---
title: "6.13.4 作业控制选项"
---

## 6.13.4 作业控制选项

(July 4, 2026)

在耦合 cluster 单双激发级别计算（CCSD、QCISD 或 OD 均可）之后评估非迭代 (T) 或 (2) 校正，由 `correlation` 关键字控制，而冻结轨道的指定则通过 `N_FROZEN_CORE`（以及可能的 `N_FROZEN_VIRTUAL`）来完成。

对于 (2) 校正，可以在参考耦合 cluster 计算中采用冻结核（frozen core）近似，然后在 (2) 校正中关联所有轨道。该行为由下文描述的 `CC_INCL_CORE_CORR` 控制。

默认情况下，如果参考 CCSD 或 OD 计算使用了冻结核轨道，则 CCSD(2) 或 OD(2) 校正会自动包含核关联及核-价关联。作出这一选择的原因是：通过该方法包含核关联的代价较低（主要计算成本的增加仅与核轨道数成线性关系），而且在精确计算中这些效应非常重要。若希望获得明确冻结核轨道的计算结果，则应将此选项设为 false。在校正中对核轨道进行冻结的一个合理理由是基组在物理上不适合描述核关联（*例如*，标准 Pople 基组和 Dunning cc-pV$x$Z 基组是专为描述仅价层关联效应而设计的）。另一个合理理由是希望与另一种方法（如 CCSD(T)）进行直接比较，而 CCSD(T) 总是使用与 CCSD 参考相同的轨道窗口。

**Q-Chem** 中提供了多种非迭代三激励（non-iterative triples）的实现。在原始的 CCMAN 套件中，可以计算 (T)、(2) 以及 (dT)/(fT) 校正。该代码的并行扩展性非常有限（最多 4 个核心）。CCMAN2 目前仅允许对 CCSD 波函数计算 (T) 和 (fT) 校正。默认使用 CCMAN2 代码来计算 (T)；若要使用 CCMAN 代码，请将 `CCMAN2` 设为 false。CCMAN2 中有两个版本的 (T)：默认版本（原生 CCMAN2）和使用 **libpt** 的新版本。基于 **libpt** 的实现是内存内（in-core）的 OpenMP 并行代码。在大多数实际计算中它显著更快，但它不使用点群对称性，因此对于高对称性的小体系作业，其性能可能反而较慢。通过设置 USE_LIBPT=TRUE 可启用 **libpt** 代码。CCSD(T) 计算可以利用 CCSD(T) 计算过程中打印的 *$ccsd_pt_restart* 数据进行重启。要重启作业，只需将最后一次打印的 *$ccsd_pt_restart* 复制到 **Q-Chem** 输入文件中即可。

**注意：

为获得 **libpt** (T) 代码的最佳性能，应请求并行执行，参见第 [2.2.1.1](../ch02_install/ssect_general-usage.md#sec:parallel) 节。
**

### `USE_LIBPT`

> **在 CCMAN2 中为 CCSD(T) 计算启用 libpt。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `TRUE`
>     * `FALSE`
> * **建议**: 现在所有实数（real-valued）CC/EOM-CC 计算均默认使用 libpt

### `CC_INCL_CORE_CORR`

> **是否在非迭代 (2) 校正（如 OD(2) 和 CCSD(2)）中包含来自冻结核轨道的关联贡献。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **选项**:
>     * `TRUE`
>     * `FALSE`
> * **建议**: 使用默认值，除非不希望包含核-价关联或核关联（*例如*，为了与其他方法比较，或所用地基组无法描述核关联）。
