---
title: "7.9.4 EOM-XX-CC2"
---

## 7.9.4 EOM-XX-CC2

（2026 年 7 月 4 日）

运动方程耦合簇（EOM-CCSD）方法有一种更为经济的变体，即 CC2 线性响应理论（linear response theory）[[249]](../bib_references/bib.md#bib250)，
它也可以被理解为 EOM-CC2。参考态的双激发振幅通过 CC2 方程（见第 6.12.4 节 [6.12.4](../ch06_correlation/topic_cc2.md)）近似求得，
目标态相应的方程也随之作了修改。这意味着式 [7.97](sec_EOMEE.md#eq747) 至 [7.99](sec_EOMEE.md#eq749)对 EOM-XX-CC2 同样有效，
只是 $\bar{H}$ 的各个元素定义方式不同。CC2 计算可以像 CCSD 计算一样运行，只需将 METHOD 设置为 CC2 或 EOM-CC2。

**Q-Chem** 中提供了两种不同的 CC2 实现：一种位于耦合簇方法套件 CCMAN2 中，另一种位于广义多体微扰理论（general many-body perturbation theory）库 LIBGMBPT 中。在 CCMAN2 中，代码结构与 CCSD 相似；而 LIBGMBPT 则采用双激发方程的分块（partitioned）形式，从而避免存储双振幅[[532]](../bib_references/bib.md#bib546)。
结合分辨率恒等（resolution-of-the-identity, RI）近似，这将内存开销从 $\mathcal{O}\left(N^{4}\right)$降低至 $\mathcal{O}\left(N^{3}\right)$，并降低了计算成本。对于较小的分子，CCMAN2 可能提供更快的性能（尤其是具有对称性的体系），而对于较大的体系，我们推荐
使用 LIBGMBPT 实现。

在 CCMAN2 中，使用 RHF、UHF 或 ROHF 参考并借助点群对称性，可采用以下 CC2 功能：

- •

EOM-EE/SF/EA/IP-CC2 的能量[[1040]](../bib_references/bib.md#bib1085)；
- •

CC2 参考态以及 EOM-EE/SF-CC2 态的单电子性质，可选择是否包含振幅响应（amplitude response）；
- •

CC2 $\leftrightarrow$ EOM-EE-CC2、EOM-EE-CC2 $\leftrightarrow$ EOM-EE-CC2 以及 EOM-SF-CC2 $\leftrightarrow$ EOM-SF-CC2 类型跃迁的跃迁偶极矩；
- •

CC2 $\leftrightarrow$ EOM-EA/IP-CC2 以及 EOM-EE/SF-CC2 $\leftrightarrow$ EOM-EA/IP-CC2 类型跃迁的 Dyson 轨道（见第 [7.9.29](topic_dyson.md) 节）；
- •

使用 CAP、CS 或 CBFs 的 EOM-EE/EA-CC2 共振能[[1382]](../bib_references/bib.md#bib1443)
（见第 [7.9.10](sub_cc_cs_cap.md) 节）。

电子排斥积分（ERI）可以通过分辨率恒等近似或 Cholesky 分解来近似，也可以使用正则（canonical）ERI。
此外，还可以采用单精度执行以进一步降低计算成本。

CC2 的 LIBGMBPT 实现仅使用 RI 近似，不利用点群对称性，也不支持单精度执行。可用的功能包括：

- •

使用 RHF 或 UHF 参考的 EOM-EE-CC2 能量；
- •

使用 UHF 参考的 EOM-SF-CC2 能量[[1040]](../bib_references/bib.md#bib1085)；
- •

使用 RHF 参考的 EOM-EA/IP-CC2 能量[[1041]](../bib_references/bib.md#bib1086)；
- •

使用 RHF 参考并借助 CAP、CS 或 CBFs 的 EOM-EA-CC2 共振能[[1382]](../bib_references/bib.md#bib1443)
（见第 [7.9.10](sub_cc_cs_cap.md) 节）；
- •

自旋缩放（spin-scaling，见第 [6.6.5](../ch06_correlation/topic_sbmp2.md) 节）可用于单重激发态的实值 EOM-EE-CC2，以及实值和复值的 EOM-EA-CC2。

对于束缚态，LIBGMBPT 采用混合 Davidson/DIIS 求解器来求解 EOM 本征值问题[[532]](../bib_references/bib.md#bib546)。
对于共振态则仅使用 Davidson 求解器[[1382]](../bib_references/bib.md#bib1443)。
Davidson 算法的默认参数可以通过 EOM_DAVIDSON_CONVERGENCE、EOM_DAVIDSON_MAX_ITER 和 EOM_DAVIDSON_MAXVECTORS 修改（与 CCMAN2 相同），而 DIIS 参数可以通过 EOM_DIIS_CONVERGENCE、EOM_DIIS_MAX_ITER 和 EOM_DIIS_MAXVECTORS 修改（见第 [7.9.18](sub_ccjobcontol.md) 节）。

LIBGMBPT 实现通过将 CCMAN2 设置为 -1 来启用；目前 CC2 的默认设置仍为 CCMAN2。RI-CC2 的随机化（stochastic）版本同样可用
（见第 [6.12.5](../ch06_correlation/sec_Stochastic_CC2.md) 节）。
