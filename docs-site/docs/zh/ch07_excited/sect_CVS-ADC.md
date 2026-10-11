---
title: "7.10.7 核激发 ADC 方法（Core-Excitation ADC Methods）"
---

## 7.10.7 核激发 ADC 方法

（2026 年 7 月 4 日）

核激发电子态位于光谱中高能量的 X 射线区域。
因此，若使用标准的对角化程序来计算核激发态——这些程序通常
先求解能量最低的激发态——则需要计算大量激发态。
这在计算上极其昂贵，仅对很小的分子和很小的基组的计算才可行。

核-价分离（Core-Valence Separation, CVS）近似通过
先验地（*a priori*）忽略核激发态与价激发态之间的耦合来解决这一问题。[[218]](../bib_references/bib.md#bib215)

由此，ADC 矩阵呈现出特定的分块结构，使得求解时可以只针对核激发态。
CVS 近似的适用性是合理的，因为核激发态与价激发态在能量上分离良好，
且两类态之间的耦合非常小。为实现核激发态与价激发态的分离，
CVS 近似将以下类型的双电子积分强制置为零

<a id="A3.S8.EGx66"></a>
$$
\displaystyle\langle Ip|qr\rangle=\langle pI|qr\rangle=\langle pq|Ir\rangle=\langle pq|rI\rangle=0 \tag{7.151}
$$

其中大写字母 $I,J,K$ 指核轨道（core orbitals），而小写字母
$p,q,r$ 表示非核占据轨道或虚轨道。

核-价近似目前适用于最高到三阶的 ADC 模型（包括扩展变体）。[[1451]](../bib_references/bib.md#bib1512)

通过在 METHOD 关键字中设置为以 CVS 为前缀的相应 ADC 模型即可启用该近似。
除通用的 ADC 相关关键字外，* $rem* 块中还需要两个附加关键字来控制 CVS-ADC 计算：

- •

ADC_CVS = TRUE 开启 CVS-ADC 计算
- •

CC_REST_OCC = $n$ 控制包含在激发空间中的核轨道数目。
整数 $n$ 对应于能量最低的 $n$ 个核轨道。

*示例：* 分子式为 C${}_{4}$H${}_{5}$N${}_{3}$O 的胞嘧啶（cytosine）含有一个氧原子。
若要计算 O 1s 核激发态，必须将 CC_REST_OCC 设为 1，
因为氧原子的 1s 轨道在能量上最低。
若要获得 N 1s 核激发，则必须将该整数设为 4，
因为氧原子的 1s 轨道在能量上低于三个氮原子的 1s 轨道，所以它也被包含在内。
相应地，若要模拟胞嘧啶的 C(1s) XAS 谱，
必须将 CC_REST_OCC 设为 8。

为了与实验数据获得最佳吻合，应当使用 CVS-ADC(2)-x 方法，
并配合至少一个带弥散函数的三重 $\zeta$（triple-$\zeta$）基组。[[1451]](../bib_references/bib.md#bib1512)
