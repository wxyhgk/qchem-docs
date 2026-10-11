---
title: "7.9.17 使用投影算符计算高激发能的 EOM-CC 态"
---

## 7.9.17 使用投影算符计算高激发能的 EOM-CC 态

（2026 年 7 月 4 日）

**Q-Chem** 提供了一种简单的投影（projection）技术，用于计算高激发能的
EOM-CCSD 态，例如以内层价轨道（inner-valence orbitals）电子移除为主的激发态或电离态。

该技术为第 [7.9.16 节](subsec_EOM-CC-diag.md)中所述基于重叠（overlap-based）的算法
提供了更为稳健的替代方案：它允许在单次计算中定位多个属于给定类别的态，
并且通过在每一次迭代中施加投影算符，保证收敛到稳定的解。

该功能由关键字 EOM_EE_IV_PROJ 和
EOM_IP_IV_PROJ 控制，这两个关键字会激活一个在 Davidson 求解器每次迭代中施加的投影算符。
内层价投影算符通过纳入指定数量的最低能级活性占据轨道（active occupied orbitals）来构造。
若存在冻结轨道（frozen orbitals），则不将其计入该数目。

所施加的投影算符强制收敛至这样的态：至少有一个电子从由所选轨道定义的内层价子空间中被移除。
这使得与更深层轨道相关的激发态或电离态能够实现稳定收敛。内层价子空间基于轨道能量自动定义。
与基于重叠的 Davidson 算法不同，该功能不需要用户指定初始猜测（initial guess）。
该功能也可视为 CVS 类核心空穴态（core-hole states）计算[[269]](../bib_references/bib.md#bib270)
的一种替代方案，且无需冻结核心轨道。

示例 [7.9.19](ex_CAPlibwfa.md)和 [7.9.19](ex_CAPlibwfa.md)演示了这一功能。
