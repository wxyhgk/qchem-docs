---
title: "4.3.1 引言"
---

## 4.3.1 引言

（2026 年 7 月 4 日）

自 5.1 版本起，**Q-Chem** 启用了新的 SCF 程序包 GEN_SCFMAN，该程序包由 E. J. Sundstrom、P. R. Horn 及众多其他合作者开发。除了支持旧 SCF 程序包的基本功能（*例如*限制型、非限制型以及限制开壳层的 HF/KS-DFT 计算）之外，**Q-Chem** 现在还许多新功能，包括：

- •

新增了若干实用的 SCF 收敛算法，并支持用户自定义的混合算法（第 [4.5.12](sub_custom_algorithm.md) 节）。
- •

更为通用、用户友好的内部稳定性分析，以及针对能量极小点的自动修正（第 [4.5.17](sub_stability_analysis.md) 节）。

GEN_SCFMAN 还支持更广泛的轨道类型，包括复数轨道。所支持的轨道完整列表如下：

- •

限制型（Restricted, R）：通常适用于处于平衡几何构型的闭壳层分子，其中电子以成对方式占据轨道。
- •

非限制型（Unrestricted, U）：适用于具有奇数个电子的自由基，也适用于电子数为偶数但并非所有电子都配对的分子，*例如*拉伸的键和双自由基（diradicals）。
- •

限制开壳层（Restricted open-shell, RO）：适用于开壳层分子，其中 $\alpha$ 和 $\beta$ 轨道被约束为相同。
- •

正则限制开壳层（Canonical restricted open-shell, can. RO 或 “ROSCF-DODS”）：ROSCF 的正则形式，详见第 [4.5.18](sub_ROHF-DODS.md) 节。
- •

开壳层单重态 ROSCF（OS_RO）：参见第 [7.7.4](../ch07_excited/ex_ESROKS.md) 节中记录的 “ROKS" 方法。
- •

广义型（Generalized, G）：*即*每个分子轨道（MO）同时关联 $\alpha$ 和 $\beta$ 自旋分量。
- •

复数轨道的使用（仅限 Hartree-Fock）：限制型（CR）、非限制型（CU）以及广义型（CG）。

SCF 计算的某些方面，例如 SCF 初始猜测（guess），以及构建 Fock 矩阵时所使用的高效算法（如 occ-RI-K，见第 [4.6.8](subsec_occrik.md) 节），均不受 GEN_SCFMAN 的使用影响。同样地，使用 GEN_SCFMAN 也不会对 SCF 之后的流程产生任何影响，例如相关方法（correlated methods）、激发态计算以及分子性质的求值。

需要注意的是，基于 **Q-Chem** 旧 SCF 代码的许多特殊功能（*例如*双基组 SCF、CDFT 等）目前尚未在 GEN_SCFMAN 中得到支持。它们将在未来陆续推出。

自 Q-Chem v7.0 起，支持使用 DIIS（第 [4.5.3](sect_diis.md) 节）、GDM（第 [4.5.7](sect_gdm.md) 节）以及稳健 SCF 流程（robust SCF pipelines，第 [4.5.13](sub_scf_robust_pipelines.md) 节）进行 MPI+OMP 并行的非 RI SCF 计算，适用于 RHF、UHF 和 ROHF 波函数形式（ansätze）。
Q-Chem v7.0 采用复制式 Fock（replicated-Fock）方法，即每个 MPI 进程（rank）都为完整的 Fock 矩阵分配内存。由于在每次 SCF 迭代的 Fock 构建结束时都会构建完整的 Fock 矩阵，因此在同一物理节点上启动多个 MPI 进程时，必须考虑每个进程所带来的内存开销。
