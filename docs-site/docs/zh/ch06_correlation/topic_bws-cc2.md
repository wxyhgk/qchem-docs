---
title: "6.12.6 尺寸一致 Brillouin-Wigner 二阶近似耦合簇单激发与双激发（BWs-CC2）"
---

## 6.12.6 尺寸一致 Brillouin-Wigner 二阶近似耦合簇单激发与双激发（BWs-CC2）

（2026 年 7 月 4 日）

在 CCSD 方程中选用微扰无关的 Møller-Plesset 哈密顿量来近似哈密顿算符，是一种流行但并不唯一的选择。事实上，可以在求解双激发（Doubles）方程时改用微扰无关的尺寸一致 Brillouin-Wigner 哈密顿量[[195]](../bib_references/bib.md#bib196)

。关于该哈密顿量的定义，参见第 [6.8](topic_bws2.md) 节。

与常规的（MP-）CC2 相比，BWs-CC2 是一种*正则化（regular）*理论，即对于正的正规化（regularisation）强度，当 HOMO/LUMO 能隙趋于零时它不会发散。因此，它可以应用于解离键以及少数组态（few-reference）体系——这类体系的主导行列式之间通过双激发相耦合。[[337]](../bib_references/bib.md#bib340)

要启用该方法，需在 REM 段中设置 METHOD = RIBWS2，并在 *$bws2* 段中设置 EXC_METHOD = CC2。BWs-CC2 对所有分区（partition）方案均可用，推荐使用 BW-s2 或 MPR-BWs2。目前仅实现了电子基态。对于一般用途，建议在 BWs-CC2 计算中采用 $A_{0}=2$、$B_{0}=0$ 的 MPR-BWs2，尽管最优参数组取决于所研究的体系及关注的化学量。
