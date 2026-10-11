---
title: "4.5.15 平方梯度最小化（SGM）"
---

## 4.5.15 平方梯度最小化（Square Gradient Minimization, SGM）

（2026 年 7 月 4 日）

GDM 方法（第 [4.5.7](sect_gdm.md) 节）是一种极其有效的能量最小化方法，但它无法可靠地用于优化激发态轨道，因为这类态在轨道旋转空间中通常是不稳定的驻点。因此，基于能量最小化的方法往往会从这些鞍点‘滑落’到某些局部极小点（通常是基态，这一现象常被描述为‘变分坍缩’（variational collapse））。

Diptarka Hait 和 Martin Head-Gordon 提出了一种优化激发态轨道的替代方法，即最小化能量梯度相对于轨道自由度的平方。[[511]](../bib_references/bib.md#bib526)
对于所有能量驻点，该能量梯度应当为零，因此所有此类驻点都是平方能量梯度 $\Delta$ 的全局极小点。
因此，拟牛顿（Quasi-Newton）方法通过最小化 $\Delta$，可以可靠地收敛到最接近初始猜测轨道的驻点，而不存在变分坍缩的风险。
所得到的 SGM 方法本质上是 GDM 的扩展，它收敛到最接近初始猜测的态（*即*，轨道空间中的驻点），而不是最接近的能量极小点。
因此，SGM 可以在直接最小化框架内用于可靠的激发态优化，类似于第 [4.5.14](topic_mom.md) 节的 MOM 算法可以与 DIIS 等迭代对角化方法结合使用的方式。
关于 SGM 应用于激发态轨道优化的更多细节，请参阅第 [7.7.5](../ch07_excited/ex_BEDSCF.md) 节。
SGM 算法的完整细节见参考文献 [[511]](../bib_references/bib.md#bib526)。

SGM 的使用由 *$rem* 部分的 SCF_ALGORITHM 变量控制：

SCF_ALGORITHM

### `SCF_ALGORITHM`

> **用于收敛 SCF 的算法。**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * SGM
>     * SGM_LS
>     * SGM_QLS
>     * 仅适用于 R 和 U 轨道
> * **建议**：SGM 应仅用于 RO 或 OS_RO 轨道。对于 R 或 U 轨道，推荐使用 SGM_LS，但它也可用于 RO 和 OS_RO 轨道。SGM_QLS 是一种速度较慢但更稳健的选择，适用于 R 和 U 计算。

DELTA_GRADIENT_SCALE

### `DELTA_GRADIENT_SCALE`

> **将 $\Delta$ 的梯度按 $N$ /100 进行缩放，这对于收敛困难的体系可以通过减小步长来提供帮助。**
>
> * **类型**：`INTEGER`
> * **默认值**：`100`
> * **选项**：
>     * $N$
> * **建议**：使用默认值。对于问题体系，50、25、10 甚至 1 可能有用。
