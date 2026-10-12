---
title: "8.8.1 概述"
---

## 8.8.1 概述

（2026 年 7 月 4 日）

原子轨道（atomic orbital, AO）标准基组用于展开单电子函数（例如分子轨道），而*辅助基组（auxiliary basis sets）*则在许多 **Q-Chem** 任务中被用于高效地近似单电子函数的乘积，例如电子相关方法中出现的乘积形式。

对于固定尺寸的分子，增加*每个原子*的基函数数目 $n$ 会导致重要的四中心双电子积分数目以 ${\cal{O}}({n^{4}})$ 的规模增长，因为不可忽略的乘积电荷分布 $|\mu\nu\rangle$ 的数目以 ${\cal{O}}({n^{2}})$ 增长。因此，使用大型（高质量）基组展开在计算上代价高昂。或许克服这一“基组质量”瓶颈最实用的方式，就是采用辅助基组展开。[[387]](../bib_references/bib.md#bib395)

能够利用辅助基组来加速多种电子相关方法（包括能量和解析梯度）的计算，是 **Q-Chem** 的一项重要特性。

辅助基 $\{|K\rangle\}$ 用于近似高斯基函数的乘积：

<a id="Ch8.E2"></a>

$$
|\mu\nu\rangle\approx|\widetilde{\mu\nu}\rangle=\sum_{K}|K\rangle C_{\mu\nu}^{K} \tag{8.2}
$$

辅助基组展开早已提出，如今被广泛认可为一种有效且强大的方法，有时也被称为恒等分辨率（resolution of the identity, RI）或密度拟合（density fitting, DF）。使用辅助基组展开后，大规模电子结构计算的计算成本随 $n$ 的增长速率可降低至约 $n^{3}$。

若 $n$ 固定而分子尺寸增大，辅助基组展开可降低计算相关的预因子（pre-factor），但不改变标度关系。关键在于该预因子可降低 5 倍、10 倍甚至更多。之所以能实现如此巨大的加速，是因为已被证明：达到合理精度所需的辅助函数数目 $X$ 仅比 $N$ 大约 3 到 4 倍。

辅助基组展开系数 $\mathbf{C}$ 通过最小化拟合分布与真实分布之间的偏差 $\langle\mu\nu-\widetilde{\mu\nu}|{\mu\nu-\widetilde{\mu\nu}}\rangle$ 来确定，由此得到如下线性方程组：

<a id="Ch8.E3"></a>

$$
\sum_{L}{\left\langle{K\left|L\right.}\right\rangle}C_{\mu\nu}^{L}=\left\langle{K\left|{\mu\nu}\right.}\right\rangle \tag{8.3}
$$

显然，求解拟合方程只需要二中心和三中心积分，因此（四中心的）双电子积分可按如下表达式近似——对于给定的辅助基组选择，这是最优的近似形式：

<a id="eq:riapprox"></a>

$$
\langle\mu\nu|\lambda\sigma\rangle\approx\langle\widetilde{\mu\nu}|\widetilde{\lambda\sigma}\rangle=\sum_{K,L}C_{\mu\nu}^{L}\langle L|K\rangle C_{\lambda\sigma}^{K} \tag{8.4}
$$

在辅助基完备的极限情况下（*即*包含 AO 的所有乘积），上述拟合过程将是精确的。然而，辅助基总是不完备的（如前所述，$X\approx 3N)$，因为这正是获得更高计算效率的关键所在。

关于 **Q-Chem** 中使用 RI 方法的更多细节，请参见第 [6.6](../ch06_correlation/topic_rimp2.md) 节（RI-MP2 及相关方法）、第 [6.19](../ch06_correlation/sect_pairing.md) 节（配对方法，pairing methods）、第 [6.12.10](../ch06_correlation/topic_ricc.md) 节（耦合簇方法）、第 [4.6.6](../ch04_scf/sect_ri-DFT.md) 节（密度泛函理论（Density Functional Theory, DFT）方法）以及第 [7.11](../ch07_excited/topic_rasi.md) 节（限制活性空间方法，restricted active space methods）。本节余下部分我们将重点介绍与辅助基组本身相关的输入设置。

**Q-Chem** 内置了多种辅助基组，可通过 *$rem* 关键字 AUX_BASIS 指定。这些辅助基组列于表 [8.9](#tab:auxbasis_corr) 中，并通过下文所列的任务控制变量在 *$rem* 输入段中指定。请注意，除内置辅助基组（表 [8.9](#tab:auxbasis_corr)）之外，还可以通过 *$aux_basis*（或 *$aux_basis_j*、*$aux_basis_k*、*$aux_basis_corr*）输入段来输入用户自定义的辅助基组，其语法总体上遵循前文第 [8.4](sect_userbasis.md) 节中所述的 *$basis* 输入段。

### `AUX_BASIS`

> **设置要使用的辅助基组**
>
> * **类型**: `STRING`
> * **默认值**: `无默认辅助基组`
> * **选项**:
>     * `General, Gen`: 用户自定义。与 BASIS 的用法相同
>     * `Symbol`: 使用下表中的标准辅助基组
>     * `Mixed`: 使用不同基组的组合
> * **建议**: 请参阅文献及 Basis Set Exchange 以辅助选择。

### `AUX_BASIS_J`

> **设置用于 RI-J 的辅助基组，或启用 RI-J**
>
> * **类型**: `STRING`
> * **默认值**: `无默认辅助基组`
> * **选项**:
>     * `General, Gen`: 用户自定义。与 BASIS 的用法相同
>     * `Symbol`: 使用下表中的标准辅助基组
>     * `Mixed`: 使用不同基组的组合
> * **建议**: 请参阅文献及 Basis Set Exchange 以辅助选择。

### `AUX_BASIS_K`

> **设置用于 RI-K 或 occ-RI-K 的辅助基组，或启用 occ-RI-K**
>
> * **类型**: `STRING`
> * **默认值**: `无默认辅助基组`
> * **选项**:
>     * `General, Gen`: 用户自定义。与 BASIS 的用法相同
>     * `Symbol`: 使用下表中的标准辅助基组
>     * `Mixed`: 使用不同基组的组合
> * **建议**: 请参阅文献及 Basis Set Exchange 以辅助选择。

### `AUX_BASIS_CORR`

> **设置用于 RI-MP2 的辅助基组，或在双杂化 DFT（double-hybrid DFT）或 MP2 的情况下启用 RI-MP2**
>
> * **类型**: `STRING`
> * **默认值**: `无默认辅助基组`
> * **选项**:
>     * `General, Gen`: 用户自定义。与 BASIS 的用法相同
>     * `Symbol`: 使用下表中的标准辅助基组
>     * `Mixed`: 使用不同基组的组合
> * **建议**: 请参阅文献及 Basis Set Exchange 以辅助选择。

| 符号名称 | 支持的原子 |
| --- | --- |
| RIJ-def2-XX ${}^{a}$ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Br, Rb $\rightarrow$ Xe, Cs $\rightarrow$ La, Hf $\rightarrow$ Rn |
| RIJK-def2-XX ${}^{a}$ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Br, Rb $\rightarrow$ Xe, Cs $\rightarrow$ La, Hf $\rightarrow$ Rn |
| RIMP2-def2-XX ${}^{b}$ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Br, Rb $\rightarrow$ Xe, Cs $\rightarrow$ La, Hf $\rightarrow$ Rn |
| RIMP2-def2-ma-XX ${}^{c}$ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Br, Rb $\rightarrow$ Xe, Cs $\rightarrow$ La, Hf $\rightarrow$ Rn |
| RIMP2-def2-ha-XX ${}^{c}$ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, K $\rightarrow$ Br, Rb $\rightarrow$ Xe, Cs $\rightarrow$ La, Hf $\rightarrow$ Rn |
| RIMP2-VDZ ${}^{d}$ | H, He, Li $\rightarrow$ F, Na $\rightarrow$ Cl, K $\rightarrow$ Br |
| RIMP2-TZVPP | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-cc-pVDZ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-cc-pVTZ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-cc-pVQZ | H, He, Li $\rightarrow$ Ne, Na $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2- cal -cc-pVDZ ${}^{e}$ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2- cal -cc-pVTZ ${}^{e}$ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2- cal -cc-pVQZ ${}^{e}$ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-aug-cc-pVDZ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-aug-cc-pVTZ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |
| RIMP2-aug-cc-pVQZ | H, He, B $\rightarrow$ Ne, Al $\rightarrow$ Ar, Ga $\rightarrow$ Kr |

- ${}^{a}$XX 包括 SV(P)、SVP、TZVP、TZVPP、QZVP 和 QZVPP。
${}^{b}$XX 包括 SV(P)、SVP、SVPD、TZVP、TZVPD、TZVPP、TZVPPD、QZVP 和 QZVPPD。
${}^{c}$XX 包括 SVP、TZVP、TZVPP 和 QZVPP，通过对弥散函数（diffuse functions）进行系统修剪（pruning）得到。
例如，RIMP2-def2-ma-SVP 由 RIMP2-def2-SVPD 修剪得到，其修剪方式与 def2-ma-SVP 由 def2-SVPD 修剪得到的方式相同。
${}^{d}$此为文献 [[1439]](../bib_references/bib.md#bib1501)
 中原始的 SVP 拟合基组。
${}^{e}$其中 *cal* = may、jun 或 jul。这些基组由相应的 RIMP2-aug-cc-pVDZ 系列构造而来。
