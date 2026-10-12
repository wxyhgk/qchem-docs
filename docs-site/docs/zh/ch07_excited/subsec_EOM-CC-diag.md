---
title: "7.9.16 EOM-CC 初始猜测构建与迭代对角化"
---

## 7.9.16 EOM-CC 初始猜测构建与迭代对角化

(July 4, 2026)

EOM-CC 本征问题通过迭代对角化（iterative diagonalization）程序求解，该程序避免了完全对角化，仅寻找由 XX_STATES 关键字指定的若干个本征态。
默认程序基于改进的 Davidson 对角化算法。[[803]](../bib_references/bib.md#bib837)

除了若干用于控制算法收敛性、内存使用及其执行细节的关键字之外，还有一些重要关键字允许用户指定目标态的选取方式。

默认情况下，对角化程序寻找由 XX_STATES 指定的若干个最低本征态。初始猜测向量（guess vectors）由利用 Koopmans 定理选择的单激发行列式生成；猜测向量的数目等于目标态的数目。如有必要，用户可以增加单激发猜测向量的数目（EOM_NGUESS_SINGLES）并包含双激发猜测向量（EOM_NGUESS_DOUBLES）。

!!! note "注意"
    在 CCMAN2 中，如果单激发猜测向量不足，算法会添加双激发猜测向量。而在 CCMAN 中，只有当调用了 EOM_NGUESS_DOUBLES 时才会生成双激发猜测向量。


用户可以请求对 singles 进行预收敛（即仅在哈密顿量的 singles-only 块中求解方程），通过 EOM_PRECONV_SINGLES 实现。在 EOM-DEA/DIP 计算中，可以通过 EOM_PRECONV_DOUBLES 对 $2p$/$2h$ 振幅进行预收敛。在 CVS 方法系列中，该选项由 CVS_EOM_PRECONV_SINGLES 调用。

!!! note "注意"
    在 CCMAN 中，用户可以同时对 singles 和 doubles 块进行预收敛（EOM_PRECONV_SINGLES 和 EOM_PRECONV_DOUBLES）。


如果需要某个（或某几个）具有特定特征的态（*例如*，$\rm HOMO\rightarrow LUMO+10$ 激发或 $\rm HOMO-10$ 电离），用户可以通过 EOM_USER_GUESS 关键字和 *$eom_user_guess* 节来指定，如下例所示。算法将尝试寻找与该猜测向量具有最大重叠的本征态。该态的多重度与常规计算相同，由 XX_SINGLETS 和 EE_TRIPLETS 关键字决定。此选项对于寻找高位态（如核心电离态或核心激发态）非常有用。它仅在 CCMAN2 中可用。

下面的示例说明了如何在 EOM 计算中使用用户指定的猜测：

> ```qchem
> $eom_user_guess
>   4  Corresponds to 4(OCC)->5(VIRT) transition.
>   5
> $end
> ```

或者

> ```qchem
> $eom_user_guess
>   1  5   Ex. states corresponding to 1(OCC)->5(VIRT) and 1(OCC)->6(VIRT)
>   1  6
> $end
> ```

在 IP/EA 计算中，只需指定一组轨道：

> ```qchem
> $eom_user_guess
>   4 5 6
> $end
> ```

如果指定了 IP_STATES，则将计算对应于从第 4、5、6 个占据分子轨道（MO）电离的 EOM-IP 态。如果请求了 EA_STATES，则求解 EOM-EA 方程，寻找对应于电子附着到第 4、5、6 个空虚拟 MO 的根。

为使这些选项正确工作，用户应确保 XX_STATES 请求了足够数目的态。在存在对称性的情况下，可以在每个不可约表示（irrep）中请求若干个态，但算法只会计算与用户猜测轨道相一致的那些态。

另外，用户可以通过 EOM_SHIFT 指定一个能量平移。在这种情况下，求解器寻找最接近该能量的 XX_STATES 个本征态；猜测向量相应地利用 Koopmans 定理生成。当需要高度激发态（*即*，内部本征态）时，此选项非常有用。
