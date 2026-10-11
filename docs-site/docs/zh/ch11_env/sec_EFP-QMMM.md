---
title: "11.5.6 EFP 框架下的 QM/MM 模型"
---

## 11.5.6 EFP 框架下的 QM/MM 模型

（2026 年 7 月 4 日）

**libefp** 的接口提供了执行简单 QM/MM 计算以及受约束的 QM 区域几何优化的方法。在这种情况下，片段势（fragment potentials）应包含 MM_CHARGE 和 MM_LJ 节，
详见 `https://libefp2.github.io/parameters.html#additional-efp-parameters`。
关键字 EFP_QMMM 用于指定 QM 区域与 MM 区域之间以及 MM（EFP）片段之间的相互作用类型，
可选项包括机械嵌入（mechanical embedding）、静电嵌入（electrostatic embedding）以及混合模型
（mixed model），在混合模型中，可极化的 QM/EFP 计算通过 QM 区域与 EFP 区域之间的
Lennard-Jones 相互作用得到增强。

QM 区域的几何优化仅在静电嵌入方案（EFP_QMMM = 2）下启用。MM 区域保持刚性；
只有 QM 原子在笛卡尔坐标下接受优化。
