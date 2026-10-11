---
title: "7.9.5 其他近似的 EOM-CC 方法"
---

## 7.9.5 其他近似的 EOM-CC 方法

（2026 年 7 月 4 日）

## 7.9.5.1 EOM-MP2 与 EOM-MP2T

以 MP2 级别获得 $T$ 振幅的近似 EOM-CCSD 模型，由于从计算中消除了计算量大的 ${\cal{O}}({N^{6}})$ CCSD 步骤，因此相比完整的 EOM-CCSD 具有更低的计算成本。**Q-Chem** 中实现了两种此类方法。第一种通过关键字 METHOD = EOM-MP2 调用，其公式化和实现遵循 Stanton 及其合作者提出的原始 EOM-CCSD(2) 方法。[[1292]](../bib_references/bib.md#bib1347)
 第二种方法可通过 METHOD = EOM-MP2T 关键字请求，与 EOM-MP2 类似，但它考虑了 $\bar{H}$ 中由于 MP2 的 $T$ 振幅不满足 CCSD 方程而出现的附加项。EOM-MP2 *ansatz*（拟设）已实现用于 IP/EA/EE/SF 能量、态性质以及态间性质（EOM-EOM，但不包括 REF-EOM）。EOM-MP2t 仅可用于 IP/EE/EA 能量计算。

## 7.9.5.2 EOM-CCSD-S(D) 与 EOM-MP2-S(D)

这些是计算量非常轻的 EOM 方法，其中 EOM 问题在单激发（singles）块中求解，而双激发的影响通过微扰方式评估。$\bar{H}$ 通过使用 CCSD 或 MP2 振幅来求值，与常规 EOM 计算相同。EOM-MP2-S(D) 方法在关联处理的级别上与 SOS-CIS(D) 类似，因此尤其快速。这些方法的设置方式与常规 EOM 计算相同，通过关键字 METHOD = EOM-CCSD-S(D) 或 METHOD = EOM-MP2-S(D) 调用。其性质计算与常规 EOM 方法完全相同。

???+ note "注意事项"

    注意 EOM-CCSD-S(D) / EOM-MP2-S(D) 仅支持单重态。
