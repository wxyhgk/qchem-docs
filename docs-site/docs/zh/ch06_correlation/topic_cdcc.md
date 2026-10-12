---
title: "6.12.11 结合 Cholesky 分解的耦合簇方法（CD-CC）"
---

## 6.12.11 结合 Cholesky 分解的耦合簇方法（CD-CC）

（2026 年 7 月 4 日）

双电子积分可以通过 Cholesky 分解[[366]](../bib_references/bib.md#bib762)进行分解，
得到的表示形式与 RI（分辨身份，Resolution of Identity）方法相同，
并能显著降低积分变换的计算开销与磁盘存储需求，同时改善并行性能：

<a id="Ch6.E79"></a>

$$
(\mu\nu|\lambda\sigma)\approx\sum_{P=1}^{M}B_{\mu\nu}^{P}B_{\lambda\sigma}^{P}, \tag{6.79}
$$

Cholesky 分解的秩 $M$ 通常比基函数数目 $N$ 大 3 到 10 倍（参考文献 [[49]](../bib_references/bib.md#bib32)）；
它依赖于分解阈值 $\delta$，并且远小于矩阵的满秩
$N(N+1)/2$（参考文献 [[49]](../bib_references/bib.md#bib32)）。
Cholesky 分解消除了积密度 $(\mu\nu|$ 中的线性相关性[[49]](../bib_references/bib.md#bib32)，
因此原则上可以在达到机器精度的条件下，获得对原始矩阵的紧凑近似。

分解阈值 $\delta$ 是控制精度与分解秩的唯一参数。
通过指定 CHOLESKY_TOL 关键字来启用 Cholesky 分解，它定义了分解应达到的精度。
对于大多数计算，容差 $\delta=10^{-3}$ 能够在精度与秩的紧凑性之间取得良好平衡。
容差 $\delta=10^{-2}$ 可用于探索性计算，而 $\delta=10^{-4}$ 用于高精度计算。
与 RI 类似，Cholesky 分解后的积分可以借助 CC_DIRECT_RI 关键字变换回正则分子轨道（MO）形式。

默认执行采用新的两步分解算法[[1215]](../bib_references/bib.md#bib1265)。

旧算法[[366]](../bib_references/bib.md#bib762)可通过指定 CHOLESKY_TWOSTEP = FALSE 来启用。
两步算法使用一个附加参数 CD_TS_SPAN_FACTOR，其默认值为 2。
采用较大的取值可提高精度，如示例 [6.12.13](ex_CDCCSD.md) 所示。

!!! note "注意"
    Cholesky 分解可用于所有 CCMAN2 方法，包括能量、解析梯度以及性质计算。
    在适当的情况下，为获得最高的计算效率，可与 FNO（虚拟轨道冻结近似，见 [6.15.1](sec_FNOCC.md) 节和 [7.9.14](../ch07_excited/sec_FNO.md) 节）结合使用。


示例 [6.12.13](ex_CDCCSD.md)、[6.12.13](ex_CDCCSD.md) 和 [6.12.13](ex_CDCCSD.md) 演示了该功能的使用方法。
