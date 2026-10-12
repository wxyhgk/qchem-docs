---
title: "1.3.16 Q-Chem 4.1 新特性"
---

## 1.3.16 **Q-Chem** 4.1 新特性

(2026 年 7 月 4 日)

- 基础算法：

- 各层级的并行性能均得到提升，包括为 Hartree-Fock、密度泛函理论（Density Functional Theory, DFT）、二阶微扰理论（MP2）以及耦合簇（coupled cluster）理论新增的 OpenMP 能力（Z. Gan, E. Epifanovsky, M. Goldey, 和 Y. Shao；第 [2.2.1.1](../ch02_install/ssect_general-usage.md#sec:parallel) 节）。
- 显著增强了有效核心势（Effective Core Potential, ECP）能力，在所有可计算能量的基组（Basis Set）中均支持梯度和频率计算（Y. Shao 和 M. Head-Gordon；第 [8.10.7](../ch08_basis/sect_ECP_derivs.md) 节）。
- 自洽场（SCF）与 DFT 能力：

- 支持 M06、M08 和 M11 系列泛函的含时密度泛函理论（TDDFT）能量计算。
- XYGJ-OS 解析能量梯度。
- TDDFT/C-PCM 的激发能、梯度与 Hessian 矩阵（J. Liu 和 W. Liang；第 [7.3.7](../ch07_excited/subsec_tddft-cPCM.md) 节）。
- 在最重叠方法（maximum overlap method, MOM）中新增附加功能，用于收敛困难的 SCF 计算（N. A. Besley；第 [4.5.14](../ch04_scf/topic_mom.md) 节）。
- 波函数相关方法能力：

- 为所有耦合簇（CC）及 EOM-CC 方法实现了 Resolution of Identity（RI）与 Cholesky 分解，从而可将应用扩展至更大体系，同时降低磁盘与内存需求并提升性能（E. Epifanovsky, X. Feng, D. Zuev, Y. Shao, 和 A. I. Krylov；第 [6.12.10](../ch06_correlation/topic_ricc.md) 节与第 [6.12.11](../ch06_correlation/topic_cdcc.md) 节）。
- 在 aug-cc-pVDZ 与 aug-cc-pVTZ 基组中提供衰减（attenuated）MP2 理论，通过对双电子积分进行截断来抵消基组重叠误差（basis set superposition error），在相同基组下所得分子间相互作用结果的精度远高于标准 MP2（M. Goldey 和 M. Head-Gordon；第 [6.7](../ch06_correlation/topic_attmp2.md) 节）。
- 扩展了 RAS-$n$SF 方法学，适用于涉及强非动态相关的基态与激发态（P. M. Zimmerman, D. Casanova, 和 M. Head-Gordon；第 [7.11](../ch07_excited/topic_rasi.md) 节）。
- 耦合簇价键（coupled cluster valence bond, CCVB）方法，用于描述具有强自旋关联的分子（D. W. Small 和 M. Head-Gordon；第 [6.19.3](../ch06_correlation/subsec_CCVB.md) 节）。
- 势能面搜索与扫描：

- 势能面（potential energy surface）扫描（Y. Shao；第 [9.6](../ch09_opt/sec_pes-scan.md) 节）。
- 通过“自由字符串（freezing string）”方法改进了自动过渡态搜索，包括无需进行 Hessian 矩阵计算即可完成此类计算的能力（S. M. Sharada 和 M. Head-Gordon；第 [9.3.3](../ch09_opt/sect_approx_hess.md) 节）。
- 对偏 Hessian 振动分析（partial Hessian vibrational analysis）进行了增强（N. A. Besley；第 [10.8.4](../ch10_properties/partial-hess.md) 节）。
- 分子间与分子内相互作用的计算与表征

- 将有效片段势（Effective Fragment Potential, EFP）方法扩展至大分子体系：fEFP 方法（A. Laurent, D. Ghosh, A. I. Krylov, 和 L. V. Slipchenko；第 [11.5.5](../ch11_env/sec_fefp.md) 节）。
- 对称适配微扰理论（symmetry-adapted perturbation theory, SAPT）的“SAPT0”级别，可将分子间相互作用能分解为静电、诱导、色散与交换等有物理意义的成分。同时提供 RI 版本（L. D. Jacobson, J. M. Herbert；第 [12.9](../ch12_frag/topic_sapt.md) 节）。
- “显极化（explicit polarization, XPol）”基于单体的 SCF 计算，通过电荷嵌入以线性标度时间计算多体极化效应（第 [12.8](../ch12_frag/sect_xpol.md) 节），既可经验势（*e.g.*，Lennard-Jones）与非极化部分的分子间相互作用相结合，也可更好地与 SAPT 结合，形成名为 XSAPT 的 *ab initio* 方法，将 SAPT 推广至包含两个以上单体的体系（L. D. Jacobson 和 J. M. Herbert；第 [12.10](../ch12_frag/sect_XSAPT.md) 节）。
- 将基于完全定域分子轨道（absolutely-localized molecular orbital, ALMO）的能量分解分析（energy decomposition analysis）扩展至非限制（unrestricted）情形（P. R. Horn 和 M. Head-Gordon；第 [12.5.3](../ch12_frag/sect_eda1.md) 节）。
- 利用 DFT 计算低自旋态下“有效未成对电子（effectively unpaired electrons）”的布居数；一种在 Kohn-Sham 框架内无需对称性破缺即可评估定域原子磁矩的新方法；以及包含静态相关效应的 Mayer 型键级分析（E. I. Proynov；第 [10.2.4](../ch10_properties/sect_odd_electron.md) 节）。
- 量子输运计算，包括电子透射函数以及外加偏压下的电子隧穿电流（B. D. Dunietz 和 N. Sergueev；第 [13.4](../ch13_specialized/sect_transport.md) 节）。
- 提供可检索的在线版 **Q-Chem** PDF 手册（J. M. Herbert 和 E. Epifanovsky）。
