---
title: "7.8.3 恒等式分解 CIS(D) 方法"
---

## 7.8.3 恒等式分解（Resolution of the Identity, RI）CIS(D) 方法

（2026 年 7 月 4 日）

由于在算法上与 MP2 计算相似，"恒等式分解"（resolution of the identity）近似也可以用于 CIS(D)。事实上，对于原子数多于寥寥数个的几乎所有分子，RI-CIS(D) 都比前文介绍的 CIS(D) 算法高效数个数量级。与 MP2 中的情况类似，这是通过降低计算量的前置因子（prefactor）来实现的。实际上，总体计算代价仍然随体系大小的五次方增长。

目前，在 **Q-Chem** 中，RI 近似支持闭壳层受限（restricted）CIS(D) 以及开壳层非受限（unrestricted）UCIS(D) 的能量计算。RI-CIS(D) 尚未实现 theta 诊断（theta diagnostic）。
