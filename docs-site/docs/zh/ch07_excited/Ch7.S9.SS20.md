---
title: "7.9.20 EOM 计算中的非 Hartree–Fock 轨道"
---

## 7.9.20 EOM 计算中的非 Hartree–Fock 轨道

（2026 年 7 月 4 日）

在开壳层参考态存在问题的情形下，*例如*，自旋污染严重的双重态、三重态或四重态，可以选择使用 DFT 轨道。具体做法是先进行 DFT 计算，然后读取轨道并关闭 Hartree–Fock（在 CCMAN 或 CCMAN2 作业中设置 SCF_GUESS = READ 和 MAX_SCF_CYCLES = 0）。
在 CCMAN 中，更便捷的方式是直接指定 EXCHANGE，*例如*，若 EXCHANGE = B3LYP，则会计算并使用 B3LYP 轨道。有关关联波函数计算中替代轨道选择的更多讨论，请参见第 [6.15 节](../ch06_correlation/sec_AltOrbs.md)。

**注意：**

在 CCMAN2 中无法使用非 HF 交换。
**
