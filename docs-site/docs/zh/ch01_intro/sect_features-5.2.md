---
title: "1.3.10 Q-Chem 5.2 新特性"
---

## 1.3.10 **Q-Chem** 5.2 新特性

（2026 年 7 月 4 日）

- •

**默认设置的变更：**

- **–**

单节点共享内存并行成为默认设置，并推荐用于大多数作业。若需使用分布式内存 MPI 并行功能，需要新的命令行参数 *-mpi*（第 [2.2.1.1](../ch02_install/ssect_general-usage.md#sec:parallel) 节）。
- **–**

当 BASIS = GEN 时，默认使用纯（Pure）基函数。
- **–**

溶剂模型中 Lebedev 网格的默认网格点数由 302 点变更为：非氢（non-Hydrogen）原子 194 点，氢（Hydrogen）原子 110 点。
- **–**

SM$x$ 模型使用 SWIG 电荷。
- **–**

XPol、SAPT 与 XSAPT 以及 MBE 作业的输入格式已变更。
- **–**

使用 EDA2 作为 ALMO-EDA 的默认驱动程序。
- **–**

RAS-CI 计算中不再默认应用冻芯（Frozen core）近似。
- •

**通用改进：**

- **–**

基组可用性提升：大多数 SCF、RI-MP2、CC、EOM-CC、ADC 计算支持高角动量基函数（最高至 k 函数）。
- **–**

简化了 RI-SCF 计算的输入格式。
- **–**

为 SCF 及 post-SCF 计算新增了 def2- 系列的密度拟合（RI）基组（由 Florian Weigend 博士提供）。
- **–**

SCF 的原子密度叠加（superposition of atomic densities）初始猜测支持在线（on-the-fly）生成（Kevin Carter-Fenk、John Herbert）。
- **–**

重新引入未经拟合的旧版（legacy）有效核势（ECP）。
- **–**

可以便捷地在片段上指定基组，并支持从外部文件读取基组（Zheng Pei 与 Yihan Shao）。
- •

**密度泛函理论（DFT）功能的改进：**

- **–**

支持使用meta-GGA 密度泛函进行解析频率计算（仅在共享内存并行下可用）。
- **–**

支持使用 resolution-of-the-identity（密度拟合）库仑方法进行解析频率计算（仅在共享内存并行下可用）。
- **–**

提升了使用 DFT 进行解析部分 Hessian 计算的 performance。
- **–**

新增密度泛函：revM06、revM11（Pierpaolo Morgante 与 Roberto Peverati）。
- •

**隐式溶剂模型的改进：**

- **–**

改进的 PCM 剖分（tessellation）网格，性能更佳（John Herbert）。
- **–**

通用 SCF 程序在使用 SM$x$ 溶剂模型时性能提升（Yuezhi Mao）。
- •

**MP2 新特性：**

- **–**

新增正则化轨道优化二阶 Møller-Plesset 微扰理论（$\kappa$-OOMP2）
（Joonho Lee、Martin Head-Gordon；第 [6.6.6](../ch06_correlation/sec_oomp2.md) 节）。
- •

**耦合簇（Coupled-Cluster）程序的增强：**

- **–**

混合精度 CCSD 与 EOM-CCSD（Pavel Pokhilko、Evvgeny Epifanovsky、Anna Krylov，
另有 Ilya Kaliman、Kaushik Nanda、Marta Vidal 与 Sonia Coriani 的贡献；第 [6.18](../ch06_correlation/sec_SP_CC.md) 节与第 [7.9.15](../ch07_excited/sec_SP_EOM_CC.md) 节）。
- **–**

使用 EOM-CC 实现双电子吸收的阻尼响应（damped response）与动态极化率（Kaushik Nanda 与 Anna Krylov）。
- **–**

在 ADC 与 CC 方法中改进了对线性点群的处理。
- **–**

提升了基于磁盘的 ADC/CC 算法的性能。
- **–**

用于 CAP-EOM-CC/CC 计算的投影（Projected）CAP 与 Voronoi CAP（Ksenia Bravaya、Alexander Kunitsa；第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节）。
- **–**

CCSD 与 EOM-CCSD 的动态极化率（Kaushik Nanda、Anna Krylov；第 [7.9.21.8](../ch07_excited/sec_EOMGRAD.md#sec:EOMpol) 节）。
- **–**

改进了利用 EOM-CC 波函数计算自旋-轨道耦合常数的方法（Pavel Pokhilko 与 Anna Krylov）。
- **–**

自旋-轨道耦合（SOC）计算与分析的新功能（Pavel Pokhilko、Anna Krylov；第 [7.9.21.4](../ch07_excited/sec_EOMGRAD.md#sec:EOMSOC) 节）。
- **–**

用于 CVS-EOM-CCSD 的戴森轨道（Dyson orbitals）（Marta Vidal、Sonia Coriani、Anna Krylov；第 [7.9.9](../ch07_excited/sub_cvs_eom.md) 节）。
- •

**能量分解分析（EDA）方法的改进：**

- **–**

新增电子密度差（EDD）图及 ETS-NOCV 分析（Yuezhi Mao）。
- **–**

ALMO-EDA 新增对 PCM 与 SMD 溶剂模型的支持（Yuezhi Mao）。
- **–**

解决了导致 MP2-EDA 计算不稳定的若干问题（Yuezhi Mao）。
- •

**显式溶剂建模的新功能：**

- **–**

用于基态及 ADC 计算的极化嵌入（Polarizable Embedding, PE）模型
（Maximilian Scheurer；第 [11.8](../ch11_env/sect_PE_model.md) 节）。
- •

**其他新方法与新功能：**

- **–**

增量式全组态相互作用（Incremental FCI）方法（Paul Zimmerman）。
- **–**

用于核心-价层（core-valence）激发的跃迁势密度泛函理论（Transition potential DFT）。
- **–**

拉曼（Raman）强度的解析计算（Zheng Pei 与 Yihan Shao）。
