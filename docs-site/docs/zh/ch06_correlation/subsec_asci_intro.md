---
title: "6.22.1 引言"
---

## 6.22.1 引言

（2026 年 7 月 4 日）

筛选组态相互作用（Selected CI）方法旨在通过仅纳入针对特定问题最重要的行列式（determinant），来逼近全组态相互作用（Full CI, FCI）能量，且可能是在活性空间（active space）内进行。筛选 CI 方法种类繁多，其历史可追溯至 20 世纪 70 年代。**Q-Chem** 包含了自适应采样组态相互作用（Adaptive Sampling Configuration Interaction, ASCI）方法。在 ASCI 方法中，通过纳入被认为重要的新行列式，对试探 CI 波函数 $\psi^{k}$ 进行迭代改进。其筛选规则源自精确 FCI 波函数在 CI 展开中各系数之间的一致性关系（consistency relationship）。
