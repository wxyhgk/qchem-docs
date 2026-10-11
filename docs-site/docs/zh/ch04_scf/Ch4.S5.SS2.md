---
title: "4.5.2 基本收敛控制选项"
---

## 4.5.2 基本收敛控制选项

（2026 年 7 月 4 日）

另请参见后续章节中更详细的选项，并注意 SCF（自洽场）收敛判据与积分类阈值（integral threshold）必须以相互兼容的方式设置（这通常意味着 THRESH 的值应至少比 SCF_CONVERGENCE 高 3）。

MAX_SCF_CYCLES

### `MAX_SCF_CYCLES`

> **控制所允许的 SCF 迭代最大次数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`50`
> * **选项**：
>     * $n$
>     * $n>0$
>     * 由用户自行选择。
> * **建议**：对于收敛缓慢的体系（例如含有过渡金属的体系），应增大该值。

SCF_ALGORITHM

### `SCF_ALGORITHM`

> **用于驱动 SCF 收敛的算法。**
>
> * **类型**：`STRING`
> * **默认值**：`DIIS`
> * **选项**：
>     * DIIS
>     * Pulay DIIS（直接迭代子空间法，Direct Inversion in the Iterative Subspace）。
>     * ROOTHAAN
>     * Roothaan 重复对角化
>     * DM
>     * 直接极小化器（Direct minimizer）。
>     * L_BFGS
>     * 带线搜索的有限内存 BFGS（Limited memory BFGS）算法
>     * GDM
>     * 几何直接极小化（Geometric Direct Minimization）
>     * GDM_LS
>     * 与 GDM 类似，但在 L-BFGS 中采用线搜索
>     * GDM_QLS
>     * 与
>     * GDM_LS
>     * 类似，但在 L-BFGS 中使用二次线搜索
>     * RCA
>     * 松弛约束算法（Relaxed-constraint algorithm）
>     * ADIIS
>     * Hu 和 Yang 提出的 ARH 能量函数与 DIIS 的组合
>     * NEWTON_CG
>     * 求解
>     * $\mathbf{Hd}=-\mathbf{g}$
>     * 采用共轭梯度法确定牛顿步（Newton steps）
>     * （另见
>     * NEWTON_MINRES
>     * ，该选项使用 MINRES 算法
>     * 求解上述线性方程）
>     * DIIS_DM
>     * 初始阶段使用 DIIS，后续迭代切换为直接极小化器
>     * （参见
>     * THRESH_DIIS_SWITCH
>     * 、
>     * MAX_DIIS_CYCLES
>     * ）
>     * DIIS_GDM
>     * 先使用 DIIS，随后切换为几何直接极小化
>     * （参见
>     * THRESH_DIIS_SWITCH
>     * 、
>     * MAX_DIIS_CYCLES
>     * ）
>     * LS_DIIS
>     * 初始阶段使用能级移动（level shifting），后续迭代切换为 DIIS
>     * （参见
>     * THRESH_LS_SWITCH
>     * 、
>     * MAX_LS_CYCLES
>     * ）
>     * RCA_DIIS
>     * 初始阶段使用 RCA，后续迭代切换为 DIIS
>     * （参见
>     * THRESH_RCA_SWITCH
>     * 和
>     * MAX_RCA_CYCLES
>     * ）
>     * ADIIS_DIIS
>     * 初始阶段使用 ADIIS，后续迭代切换为 DIIS
>     * （参见
>     * THRESH_ADIIS_SWITCH
>     * 和
>     * MAX_ADIIS_CYCLES
>     * ）
>     * ROBUST
>     * 用于稳健收敛的新型黑箱（black-box）工作流，采用更严格的阈值
>     * 并结合多种算法（DIIS、ADIIS 和 GDM）。
>     * ROBUST_STABLE
>     * 在 ROBUST 流程的基础上额外进行稳定性分析。
> * **建议**：默认使用 DIIS；除非进行受限开壳层（restricted open-shell）计算，此时推荐使用 GDM。如果 DIIS 在初始迭代中无法找到合理的近似解，则推荐的备选方案是 RCA_DIIS 或 ADIIS_DIIS。如果 DIIS 已接近正确解但最终无法收敛，则推荐的备选方案是 DIIS_GDM。对于 HOMO/LUMO 能隙较小且 DIIS 无法收敛的体系，LS_DIIS 可能有所帮助。如果上述方法均无效，请尝试 ROBUST 或 ROBUST_STABLE。请将 SCF 收敛失败的情况反馈给 Q-Chem 办公室，以帮助完善这些工作流。

**注**：
关于 ROBUST 或 ROBUST_STABLE 算法的使用，参见第 [4.5.13](sub_scf_robust_pipelines.md) 节。
关于平方梯度极小化（Squared Gradient Minimization, SGM）及相关算法，参见第 [4.5.15](sect_SGM-SCF.md) 节。

SCF_CONVERGENCE

### `SCF_CONVERGENCE`

> **当波函数误差 $<10^{-\mathrm{SCF\_CONVERGENCE}}$ 时，即认为 SCF 已收敛。请同时调整 THRESH 的值。**
>
> * **类型**：`INTEGER`
> * **默认值**：`5`
> * **选项**：
>     * $n$
>     * 对应于
>     * $10^{-n}$
> * **建议**：几何优化和振动分析需要更严格的收敛判据。较大的值可提供更多有效数字，但计算代价也更高。

在某些情况下，除了 SCF 总能量之外，还需要其各个能量组分，例如动能、交换能、相关能等（*etc.*）。如果在输入中指定 SCF_PRINT = 1，则这些组分的数值将在每一轮 SCF 循环中被打印出来。
