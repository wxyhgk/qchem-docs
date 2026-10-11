---
title: "7.10.4 恒等分辨（Resolution of the Identity）ADC 方法"
---

## 7.10.4 恒等分辨（Resolution of the Identity）ADC 方法

（2026 年 7 月 4 日）

与 MP2 和 CIS(D) 类似，ADC 方程也可以借助恒等分辨（resolution-of-the-identity, RI）近似重新形式化。这一做法显著降低了积分变换的计算开销与存储需求。虽然相对于体系规模，RI 近似并不会改变 ADC(2)-s 的 $O(N^{5})$ 或 ADC(2)-x 的 $O(N^{6})$ 总体计算标度，但在计算较大体系时，采用 RI 近似仍能带来明显的加速效果。

RI 近似可与所有可用的 ADC 方法一同使用。只要通过 AUX_BASIS 指定了辅助基组（auxiliary basis set），该近似即会被自动启用。
