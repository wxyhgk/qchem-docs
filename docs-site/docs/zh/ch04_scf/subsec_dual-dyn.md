---
title: "4.7.3 双基组动力学"
---

## 4.7.3 双基组动力学

(July 4, 2026)

由于能够以降低的开销计算 SCF 与 MP2 的能量和受力，双基组（dual-basis）计算在*从头算*（*ab initio*）分子动力学模拟中颇具吸引力，相关内容见第 [9.9](../ch09_opt/topic_aimd.md) 节。双基组 BOMD 已展现出[[1301]](../bib_references/bib.md#bib1359)

58% 的节省，即便相对于采用 Fock 外推的最先进 BOMD 也是如此；对于双基组 RI-MP2 动力学，节省幅度进一步提升至

71%。值得注意的是，这些计时优于扩展拉格朗日（“Car-Parrinello”）动力学的估计值，且不存在后者有时出现的能量守恒劣化等不利伪影。[[558]](../bib_references/bib.md#bib572)

两项算法改进为双基组动力学带来了幅度不大但确有价值的提升。首先，

迭代式的小基组计算可从 Fock 矩阵外推中获益。[[558]](../bib_references/bib.md#bib572)

其次，对外推响应方程（“$Z$ 矢量”方程）以求核受力，可进一步提升效率。[[1304]](../bib_references/bib.md#bib1360)
（见第 [9.9](../ch09_opt/topic_aimd.md) 节。）
当启用 DUAL_BASIS_ENERGY 时，**Q-Chem** 会自动调整，在适当的基组中进行外推。
