---
title: "4.5.1 引言"
---

## 4.5.1 引言

（2026 年 7 月 4 日）

与任何数值优化过程一样，自洽场（SCF）过程的收敛速度取决于初始猜测（initial guess）以及用于向驻点迭代的算法。 **Q-Chem** 提供了多种 SCF 优化算法，可通过 *$rem* 变量 SCF_ALGORITHM 进行选择，包括：

基于外推或插值的方法：

- •

非常成功的 DIIS 过程。它们是默认方法（限制开壳层 SCF 计算除外），并且适用于所有轨道类型（见第 [4.5.3](sect_diis.md) 节）。
阻尼（damping）

 和能级移动（level-shifting）
技术[[578]](../bib_references/bib.md#bib599)

也可以与 DIIS 结合使用（仅限 R、U）。
- •

ADIIS：由 Hu 和 Yang 开发的增广 Roothaan-Hall（ARH）能量函数与 DIIS 的组合[[601]](../bib_references/bib.md#bib624)，
 仅适用于 R 和 U。

利用轨道梯度的方法：

- •

直接极小化（Direct Minimization, DM），已重新实现为带线搜索的简单最速下降法，适用于所有轨道类型。DM 可以在若干次 DIIS 迭代之后调用。
- •

有限内存 Broyden-Fletcher-Goldfarb-Shanno 算法（L_BFGS），
这是一种拟牛顿法，利用前几次迭代中的梯度和步长来构造近似的 Hessian 矩阵。
- •

几何直接极小化（Geometric Direct Minimization, GDM），它是 DM 的改进版且非常稳健，是 DIIS 失败时推荐使用的备选方法。与 DM 一样，它也可以在若干次 DIIS 迭代之后调用，以改进初始猜测。GDM 是限制开壳层 SCF 计算的默认算法，并适用于所有轨道类型（见第 [4.5.7](sect_gdm.md) 节）。GDM 有三种变体：

- **–**

GDM：默认实现。
- **–**

GDM_LS：在每次迭代中使用线搜索。
- **–**

GDM_QLS：采用二次能量模型在每次迭代中执行线搜索。
- •

平方梯度极小化（Square Gradient Minimization, SGM）系列：SGM 是一种受 GDM 启发、用于激发态轨道优化的方法。目前支持该方法的三种变体：SGM（适用于 RO 和 OS_RO）、SGM_LS（适用于 R、U、RO 和 OS_RO）以及 SGM_QLS（适用于 R 和 U），它们分别基于对应的 GDM 方法。更多细节见第 [4.5.15](sect_SGM-SCF.md) 节。

需要轨道 Hessian 的方法：

- •

NEWTON_CG/NEWTON_MINRES（使用 CG/MINRES 求解器求解 $\mathbf{Hd}=-\mathbf{g}$ 以获得更新方向）。
- •

SF_NEWTON_CG（NEWTON_CG 的“无鞍点（saddle-free）”版本）。

解析的轨道 Hessian 适用于 R/U/RO/G/CR，除非使用了特殊的密度泛函（*例如*，除 VV10 [[1416]](../bib_references/bib.md#bib1477)
 之外的非局域泛函）；而通过设置 FD_MAT_VEC_PROD = TRUE，所有轨道类型均可使用有限差分 Hessian。

除上述算法之外，还有最大重叠方法（maximum overlap method, MOM），它确保 DIIS 始终占据一组连续的轨道，而不会在不同占据方案之间振荡。MOM 还可用于求取 SCF 方程的高能量解（见第 [7.7.2](../ch07_excited/ex_OpSing.md) 节）。
松弛约束算法（relaxed constraint algorithm, RCA）能够保证能量在每一步都下降，它也可以通过旧版 SCF 代码使用（设置 GEN_SCFMAN = FALSE）。不过，
ADIIS [[601]](../bib_references/bib.md#bib624)
 算法的性能应与之相当。

由于 GEN_SCFMAN 中的代码高度模块化，不同 SCF 算法对不同 SCF（轨道）类型的适用性在总体上得到了极大扩展。例如，旧版 ROSCF 实现要求只能使用 GWH 猜测和 GDM 算法。这种限制在基于 GEN_SCFMAN 的 RO 计算中已被消除。
