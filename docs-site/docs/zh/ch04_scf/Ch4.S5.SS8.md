---
title: "4.5.8 直接极小化（DM）"
---

## 4.5.8 直接极小化（Direct Minimization, DM）

（2026 年 7 月 4 日）

直接极小化（Direct Minimization, DM）是上一节所讨论的几何直接极小化（Geometric Direct Minimization, GDM）方法的一种较为原始、不够精细的前身。DM 并不能在轨道旋转所构成的超球面空间（hyper-spherical space）中沿大圆（great circle）正确地走步，因此一般而言，其收敛速度和稳健程度都不如 GDM。**Q-Chem** 保留 DM 仅仅是出于历史兼容（legacy）目的的考虑。总体上，其输入选项与 GDM 相同，只是 SCF_ALGORITHM 的取值有所不同，它可以是 DIIS_DM（推荐）或 DM。

### `PSEUDO_CANONICAL`
