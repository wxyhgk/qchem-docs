---
title: "7.7.1 引言"
---

## 7.7.1 引言

(July 4, 2026)

当基态与激发态之间的电子密度存在显著差异时（例如电荷转移、里德堡（Rydberg）激发或核心电子激发），标准的含时密度泛函理论（Time-Dependent Density Functional Theory, TDDFT）容易出现灾难性的失效。[[351]](../bib_references/bib.md#bib357)
 通过在线性响应之外引入轨道弛豫、显式地优化激发态轨道（其方式类似于基态自洽场（Self-Consistent Field, SCF）计算），这一问题可以得到极大改善，本节将介绍若干实现这一目标的方法。其中一些方法认识到，任何单重激发态的单一行列式描述都无法保持自旋纯净（spin pure），而开壳层单重态的最小描述需要两个行列式。这一问题可以通过受限开壳层 Kohn-Sham（Restricted Open-Shell Kohn-Sham, ROKS）计算以计算上可行的方式加以处理，详见第 [7.7.4](ex_ESROKS.md) 节。对于开壳层单重态（*即*，双自由基，biradicals），该方法的简化版本即为近似自旋纯化（approximate spin purification），详见第 [7.7.3](sect_OpSing.md) 节。

与基态 SCF 问题相比，激发态轨道优化通常更具挑战性，因为 SCF 方程的激发态解在轨道旋转空间中一般并非局部极小点，而是通常是鞍点。传统的优化器（如 DIIS 或梯度下降法 GDM）往往无法找到 SCF 方程的这些激发态、非构造原理（non-aufbau）解，反而会坍缩到能量更低的解（通常是基态）。这种"变分坍缩"（variational collapse）问题限制了解发态轨道优化方法的实用性。最大重叠法（Maximum Overlap Method, MOM，见第 [7.7.2](ex_OpSing.md) 节）在许多情况下可以避免这一问题，但仍受限于底层 SCF 算法本身的收敛问题。**Q-Chem** 包含两种备用流程，与 MOM 相比往往更为稳健，可用于寻找 SCF 方程的激发态解：平方梯度最小化（squared-gradient minimization，见第 [7.7.5](ex_BEDSCF.md) 节）[[511]](../bib_references/bib.md#bib526)
，以及态靶向能量投影（state-targeted energy projection，见第 [7.7.8](ex_ROSTEP.md) 节）[[196]](../bib_references/bib.md#bib189)
。这两种方法既可以独立使用，借助基态计算流程给出激发能的单行列式"$\Delta$SCF"估计，

 也可以与 ROKS 流程相结合，以规避 $\Delta$SCF 方法所伴随的自旋污染问题。
