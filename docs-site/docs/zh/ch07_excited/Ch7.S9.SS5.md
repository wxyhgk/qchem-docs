---
title: "7.9.5 更多近似 EOM-CC 方法"
---

## 7.9.5 更多近似 EOM-CC 方法

（2026 年 7 月 4 日）

## 7.9.5.1 EOM-MP2 与 EOM-MP2T

在 MP2 水平获得 $T$-振幅的近似 EOM-CCSD 模型与全 EOM-CCSD 相比计算量显著降低，因为计算中省去了耗时的 ${\cal{O}}({N^{6}})$ CCSD 步骤。**Q-Chem** 中实现了两种此类方法。第一种通过关键字 METHOD = EOM-MP2 调用。其理论形式与实现遵循 Stanton 及其合作者开发的原始 EOM-CCSD(2) 方法。[[1292]](../bib_references/bib.md#bib1347)
第二种方法可以通过 METHOD = EOM-MP2T 关键字指定，它与 EOM-MP2 类似，但计入了由于 MP2 $T$-振幅不满足 CCSD 方程而在 $\bar{H}$ 中出现的附加项。EOM-MP2 *ansatz* 适用于 IP/EA/EE/SF 能量、态性质以及态间性质（EOM-EOM，但不包括 REF-EOM）。EOM-MP2t 仅可用于 IP/EE/EA 能量计算。

## 7.9.5.2 EOM-CCSD-S(D) 与 EOM-MP2-S(D)

这些是非常轻量级的 EOM 方法，其中 EOM 问题在单激发块内求解，而双激发效应则通过微扰方法计算。与常规 EOM 计算类似，$\bar{H}$ 可以使用 CCSD 或 MP2 振幅来评估。EOM-MP2-S(D) 方法的相关处理水平与 SOS-CIS(D) 相当，速度极快。这些方法已实现用于 IP 和 EE 态。对于价层态，相对于常规 EOM-CCSD，其绝对电离能或激发能的误差约为 0.4 eV，且表现出系统性的蓝移；而 EOM-EOM 能隙的表现更佳。计算设置与常规 EOM-EE/IP 类似，只需指定 METHOD = EOM-CCSD-SD(D) 或 METHOD = EOM-MP2-SD(D)。这些方法可用于计算态性质以及 EOM-EOM 跃迁性质（基态-EOM 性质尚未实现）。这些方法专门设计用于处理芯能级态。[[1193]](../bib_references/bib.md#bib1248)

**注意：**

这些方法目前仍处于实验阶段。
