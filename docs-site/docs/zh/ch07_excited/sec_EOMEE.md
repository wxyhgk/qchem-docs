---
title: "7.9.3 EOM-XX-CCSD 与 CI 方法系列"
---

## 7.9.3 EOM-XX-CCSD 与 CI 方法系列

（2026 年 7 月 4 日）

**Q-Chem** 提供了最为完整的 EOM-CCSD 模型集合，[[729]](../bib_references/bib.md#bib760)

从而能够对电子激发态（EOM-EE-CCSD 或 EOM-EE-OD）进行精确、稳健且高效的计算；
[[1228]](../bib_references/bib.md#bib1283)
；
双自由基与三自由基的基态和激发态（EOM-SF-CCSD 与
EOM-SF-OD）；[[726]](../bib_references/bib.md#bib757)
 电离势与电子附着能，以及难以处理的双基（doublet）自由基和阳离子或阴离子自由基
（EOM-IP/EA-CCSD）。[[1260]](../bib_references/bib.md#bib1313)
 EOM-DIP-CCSD、EOM-2SF-CCSD 和 EOM-DEA-CCSD
方法同样可用。在概念上，EOM 与组态相互作用（Configuration Interaction, CI）非常相似：目标 EOM 态通过对相似变换后的哈密顿量 $\bar{H}=e^{-T}He^{T}$ 进行对角化来求得，

<a id="eq747"></a>

$$
\bar{H}R=ER, \tag{7.97}
$$

其中 $T$ 和 $R$ 是相对于参考行列式 $|\Phi_{0}\rangle$ 的一般激发算符。在 EOM-CCSD 模型中，$T$ 和 $R$ 均在单、双激发处截断，且振幅 $T$ 满足参考态 $|\Phi_{0}\rangle$ 的耦合簇（Coupled Cluster, CC）方程：

<a id="A3.S8.EGx55"></a>

$$
\displaystyle\langle\Phi_{i}^{a}|\bar{H}|\Phi_{0}\rangle \tag{7.98}
$$

EOM-CCSD 与 CISD 方法的计算标度完全相同，*即*，
${\cal{O}}({N^{6}})$，然而 EOM-CCSD 在数值上优于 CISD，因为关联效应已被“折叠”进变换后的哈密顿量之中，并且因为 EOM-CCSD 严格满足尺寸强度性（size-intensive）。

通过组合不同类型的激发算符和参考态
$|\Phi_{0}\rangle$，可以触及不同的目标态组，如图 [7.2](Ch7.S9.SS2.md#fig:EOM) 所述。例如，当参考态 $|\Phi_{0}\rangle$ 对应于基态波函数，且算符 $\hat{R}$ 保持电子数与总自旋不变时，即可描述电子激发态。[[1289]](../bib_references/bib.md#bib1345)
 在电离/电子附着 EOM
模型中，[[1291]](../bib_references/bib.md#bib1346)
 算符 $R$ 不保持电子数不变（*即*，产生算符与湮灭算符的数目不同）——这些模型能够精确处理双基自由基及某些其他开壳层体系的基态与激发态。例如，单电离 EOM 方法，*即*，EOM-IP-CCSD 和 EOM-EA-CCSD，对于理论处理常受对称性破缺困扰的双基自由基非常有用。EOM-SF 方法[[726]](../bib_references/bib.md#bib757)
 的激发算符包含自旋翻转（spin-flip），因而可以处理双自由基、三自由基以及化学键断裂问题。

最后，EOM-DIP 和 EOM-DEA 方法同样提供了访问类似这类强关联体系的途径。

**Q-Chem** 针对闭壳层与开壳层参考（RHF/UHF/ROHF）均提供了 EOM-EE/SF/IP/EA/DIP/DEA/DSF-CCSD
方法，并包含冻结核/冻结核外轨道（frozen core/virtual）选项。对于 EE、SF、IP 和 EA，还提供更经济的 EOM-CCSD 变体（EOM-MP2 方法系列）。所有 EOM
模型都充分利用了分子点群对称性。解析梯度可用于 RHF 和 UHF
参考，适用于完整轨道空间，也支持冻结核/冻结核外轨道。[[804]](../bib_references/bib.md#bib838)

性质计算（永久偶极矩与跃迁偶极矩、角动量投影、自旋-轨道耦合（SOC）与非绝热耦合（NAC）、$\langle\hat{S}^{2}\rangle$、$\langle\hat{R}^{2}\rangle$ 等）同样可用。EOM-XX-CCSD
方法的当前实现可支持中等尺寸分子的计算，*e.g.*，最多约 15–25
个重原子。使用 RI 近似（第 [6.12.10](../ch06_correlation/topic_ricc.md) 节）或 Cholesky
分解（第 [6.12.11](../ch06_correlation/topic_cdcc.md) 节）有助于减少积分变换时间和磁盘占用，从而能够对大得多的体系进行计算。EOM-MP2 和 EOM-MP2t
变体的计算需求也更低。RI-CC2（第 [7.9.4](sec_eomcc2.md)
节）则提供了更为稳健且计算高效的选项。通过使用 FNO
方案截断核外轨道空间（见第 [7.9.14](sec_FNO.md) 节），可以显著降低
EOM-IP/SF 计算的开销（且精度损失可忽略不计）。

## 7.9.3.1 EOM-CC 与基于投影的嵌入方法

由于该方法计算成本高昂，将 EOM-CCSD 应用于大体系在计算时间和资源方面均存在困难。克服这一问题的一种策略是将 EOM-CC 与基于投影的嵌入（projection-based embedding）相结合[[878]](../bib_references/bib.md#bib913)
。该方法在电离能、核电子激发（core-ionized）能级以及价激发能的计算中表现优异。对于里德堡（Rydberg）态也能给出足够精确的描述，但不建议将基于投影的嵌入与 EOM-EA-CCSD 结合使用。
基于投影的嵌入的理论与作业命令详见第 [11.6](../ch11_env/sect_den_emb.md) 节。

## 7.9.3.2 CCMAN 中提供的遗留功能

**Q-Chem** 的 CCMAN 模块包含 EOM-IP-CCSD 的两种实现。默认使用的正确实现[[1092]](../bib_references/bib.md#bib1137)
 更为高效和稳健。关键字 EOM_FAKE_IPEA
所调用的是一种试验性实现，其做法是在所选基组中加入一个非常扩散的轨道，并针对包含电子向该扩散轨道激发的目标态求解 EOM-EE-CCSD 方程，从而搭建 EOM-IP-CCSD
计算。CCMAN 中 EOM-EA-CCSD 的实现也使用了这一技巧。假（Fake）IP/EA 计算仅推荐用于戴森（Dyson）轨道计算和调试目的。CCMAN2 提供了 EOM-IP 和 EOM-EA 的正确实现（包括戴森轨道）。

CCMAN 中还提供 EOM-IP-CCSD 的一种更为经济的 CI 变体，即 IP-CISD。这是 IP-CCSD 的 ${\cal{O}}({N^{5}})$ 近似，可用于棘手的双基态的几何优化。[[470]](../bib_references/bib.md#bib483)
