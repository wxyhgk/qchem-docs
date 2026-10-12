---
title: "4.5.13 黑盒鲁棒 SCF 流程"
---

## 4.5.13 黑盒鲁棒 SCF 流程

（2026 年 7 月 4 日）

秉承第 [4.5.12](sub_custom_algorithm.md) 节中用户自定义混合 SCF 算法（User-Customized Hybrid SCF Algorithm）的理念，自 v6.3.0 起，Q-Chem 提供了两条“黑盒”（black-box）流程，用于提升困难场景下自洽场（SCF）收敛的鲁棒性。
将 SCF_ALGORITHM 设置为 ROBUST 或 ROBUST_STABLE，并配合将 GEN_SCFMAN 设置为 true，即可使用这两条流程。
ROBUST 流程的概要如下：

- •

当 DIIS 误差或 RMS 梯度收敛至所请求的收敛阈值以下时，判定 SCF 收敛。
- •

双电子积分（2-electron integrals）的忽略截断值设置为 $10^{-12}$，或使用 THRESH 指定的更严格值。注意，默认情况下 THRESH = SCF_CONVERGENCE+4。
- •

重叠积分（overlap integrals）的忽略截断值设置为 $10^{-14}$，或使用 S2THRESH 指定的更严格值，以缓解基组（Basis Set）线性相关性问题。
- •

我们将 SCF 过程中的振荡行为（oscillatory behavior）定义为：在 DIIS 误差或 RMS 梯度对数值的一个窗口内出现 SCF_ROBUST_MIN_SIGN_CHANGES 次符号变化。
- •

我们将平台期检测（plateau detection）定义为：SCF_ROBUST_PLATEAU_WINDOWS 个 DIIS 误差或 RMS 梯度窗口的斜率均小于 SCF_ROBUST_SLOPE_THRESH。
- •

在整个流程中，MAX_SCF_CYCLES 表示 SCF 算法在不改变任何参数的情况下允许运行的最大迭代循环数。
- •

流程以 DIIS 算法开始。如果在第 #(2*SCF_ROBUST_WINDOW_SIZE+1) 次迭代之后检测到 DIIS 误差出现平台期或振荡行为，则增量 Fock（incremental Fock）算法（若已开启）将被永久关闭。
- •

此时，若 DIIS 误差小于 0.001，则算法切换为 ADIIS；否则，允许 DIIS 继续运行额外的 MAX_SCF_CYCLES 次迭代，除非再次检测到平台期或振荡趋势，届时算法将切换为 GDM。在 Q-Chem 7.0 中，若在 MPI+OMP 并行化下运行鲁棒 SCF，则会跳过向 ADIIS 的切换。
- •

允许 ADIIS 运行 MAX_SCF_CYCLES 次迭代，除非 DIIS 误差变得小于 0.001。
- •

ADIIS 之后再次运行 DIIS。若在第 #(2*SCF_ROBUST_WINDOW_SIZE+1) 次迭代之后再次检测到平台期或振荡趋势，则流程切换为 GDM。
- •

允许 GDM 一直运行，直至收敛或达到允许的最大迭代次数。

ROBUST_STABLE 流程在 ROBUST 流程的基础上额外执行稳定性分析（stability analysis），直到找到极小值点为止。
在使用 ROBUST 完成初始的宏迭代（macroiteration）之后，后续宏迭代中仅使用 GDM 进行稳定性分析。
作为该流程继续运行的必要条件，负本征值（negative eigenvalues）的数目需在每次宏迭代中递减。

下面介绍这些鲁棒流程内部的 *$rem* 参数。
这些参数的默认值目前设为实验性取值，未必对所有使用场景都是最优的；
因此，如果默认值无法让用户的场景收敛，我们鼓励用户将自己的设置反馈给 Q-Chem Office。

### `SCF_ROBUST_WINDOW_SIZE`

> **控制用于检测鲁棒 SCF 流程中振荡或平台期的 DIIS 误差或 RMS 梯度对数值窗口的大小。**
>
> * **类型**：`INTEGER`
> * **默认值**：`7`
> * **可选值**：
>     * n
>     * 自定义。
> * **建议**：无

### `SCF_ROBUST_MIN_SIGN_CHANGES`

> **控制用于检测鲁棒 SCF 流程中振荡时，DIIS 误差或 RMS 梯度对数值窗口内的符号变化次数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`3`
> * **可选值**：
>     * n
>     * 自定义。
> * **建议**：无

### `SCF_ROBUST_PLATEAU_WINDOWS`

> **控制用于检测鲁棒 SCF 流程中平台期时，所使用的 DIIS 误差或 RMS 梯度对数值窗口的数目。**
>
> * **类型**：`INTEGER`
> * **默认值**：`5`
> * **可选值**：
>     * n
>     * 自定义。
> * **建议**：无

### `SCF_ROBUST_SLOPE_THRESH`

> **控制用于检测鲁棒 SCF 流程中平台期时，DIIS 误差或 RMS 梯度对数值连续窗口的斜率阈值。**
>
> * **类型**：`INTEGER`
> * **默认值**：`3`
> * **可选值**：
>     * n
>     * 自定义为
>     * $10^{-n}$
>     * 。
> * **建议**：无
