---
title: "1.3.12 Q-Chem 5.0 的新特性"
---

## 1.3.12 **Q-Chem** 5.0 的新特性

(2026 年 7 月 4 日)

- 耦合簇（coupled-cluster）程序包的增强：

- Cholesky 分解 CCSD 与 EOM-CCSD 的解析梯度；
正则（canonical）CCSD 与 EOM-CCSD 梯度的效率提升（Xintian Feng、Evgeny Epifanovsky）。
- CAP-EOM-CCSD 解析梯度（Zsuzsanna Koczor-Benda、Thomas Jagau）以及亚稳态（metastable states）的 Dyson 轨道
（Thomas Jagau、Anna Krylov），参见第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节。
- CAP-EOM-MP2 方法（Alexander Kunitsa、Ksenia Bravaya）。
- 采用完整微分形式（full derivative formulation），利用 CCSD 与 EOM-CCSD（EE 和 SF）波函数计算极化率（Kaushik Nanda 和 Anna Krylov），参见第 [7.9.21.8](../ch07_excited/sec_EOMGRAD.md#sec:EOMpol) 节。
- EOM-CCSD 波函数的 $\langle\hat{S}^{2}\rangle$ 计算（Xintian Feng）。
- EOM-CCSD 波函数的非绝热耦合（NACs）计算（Shirin Faraji、Anna Krylov、Evgeny Epifanovsky、Xintian Feng），参见第 [7.9.21.5](../ch07_excited/sec_EOMGRAD.md#sec:EOMNAC) 节。
- (T) 校正的效率提升及新的多核并行代码（Ilya Kaliman）。
- 面向核心态（core states）的、基于耦合簇的新方法（Anna Krylov）。
- 隐式溶剂化建模的新功能：

- 用于在 EOM-CC 和 MP2 级别计算垂直激发能、电离能与电子附着能的平衡态 PCM 功能（参见第 [11.2](../ch11_env/topic_solvation.md) 节）。
- 针对 ADC 所有阶数与变体的态特定（state-specific）平衡及非平衡溶剂化（Jan Mewes、Andreas Dreuw），参见第 [7.10.11](../ch07_excited/topic_abs-adc.md) 节。
- 泊松方程边界条件，允许使用任意各向异性介电函数 $\varepsilon(\mathbf{r})$，并对体极化（volume polarization）进行完整处理（Marc Coons、John Herbert），参见第 [11.2.11](../ch11_env/sect_PEQS.md) 节。
- 溶剂隐式表示组合模型（Composite Model for Implicit Representation of Solvent, CMIRS），一种用于溶剂化自由能的高精度模型（Zhi-Qiang You、John Herbert），参见第 [11.2.7](../ch11_env/example_CMIRS-water.md) 节。
- 新的密度泛函（Narbe Mardirossian 和 Martin Head-Gordon），参见第 [5.3](../ch05_dft/sect_XCfuncs.md) 节：

- GGA 泛函：BEEF-vdW、HLE16、KT1、KT2、KT3、rVV10
- Meta-GGA 泛函：B97M-rV、BLOC、mBEEF、oTPSS、TM
- 杂化（Hybrids）泛函：CAM-QTP(00)、CAM-QTP(01)、HSE-HJS、LC-$\omega$PBE08、MN15、rCAM-B3LYP、WC04、WP04
- 双杂化（Double hybrids）泛函：B2GP-PLYP、DSD-PBEB95-D3、DSD-PBEP86-D3、
DSD-PBEPBE-D3、LS1DH-PBE、PBE-QIDH、PTPSS-D3、PWPB95-D3
- Grimme 的 PBEh-3c “低成本”组合方法
- rVV10 非局域关联泛函
- 额外的 DFT 进展：

- DFT-D3 的新形式（J. Witte；参见第 [5.7.3](../ch05_dft/subsec_DFT-D.md) 节）。
- 新的标准积分网格 SG-2 和 SG-3（Saswata Dasgupta、John Herbert），参见第 [5.5.3](../ch05_dft/sect_standard-quad.md) 节。
- 用于含时 Kohn-Sham 计算（亦称“实时”（real-time）TDDFT）的更高效的传播子算法（Ying Zhu、John Herbert），参见第 [7.4](../ch07_excited/sec_TDKS.md) 节。
- 用于计算有效核势（effective core potential, ECP）积分的新积分程序包（Simon McKenzie、Evgeny Epifanovsky），参见第 [8.10.2](../ch08_basis/sub_ECP-fit.md) 节。

- 用于能量及一阶导数的更高效的解析算法。
- 支持任意投影算符角动量（projector angular momentum）。
- 支持基组中最高至 $h$ 的角动量。
- *ab initio* Frenkel-Davydov 激发子（exciton）模型的解析导数耦合（Adrian Morrison、John Herbert）；参见第 [12.14](../ch12_frag/sect_AIFDEM.md) 节。
- 基于 ALMO 的新能量分解分析（energy decomposition analysis, EDA）方法：

- 面向 DFT 的第二代 ALMO-EDA 方法（Paul Horn、Yuezhi Mao、Martin Head-Gordon）；参见第 [12.6](../ch12_frag/sect_eda2.md) 节。
- 将 ALMO-EDA 扩展至 RIMP2 理论（Jonathan Thirman、Martin Head-Gordon）；参见第 [12.7.1](../ch12_frag/sect_mp2_eda.md) 节。
- 用于分解分子性质变化的“绝热”（adiabatic）EDA 方法（Yuezhi Mao、Paul Horn、Martin Head-Gordon）；参见第 [12.7.3](../ch12_frag/sect_adiabatic_eda.md) 节。
- 波函数关联计算能力：

- 用于描述具有强自旋关联的开壳层分子的耦合簇价键（coupled cluster valence bond, CCVB）方法（David Small、Martin Head-Gordon）；参见第 [6.19.3](../ch06_correlation/subsec_CCVB.md) 节。
- 面向闭壳层物种的含单激发与双激发的耦合簇价键（CCVB-SD）实现（Joonho Lee、David Small、Martin Head-Gordon）；参见第 [6.14.4](../ch06_correlation/topic_ccvb.md) 节。

!!! note "注意"
    自 4.4 版本以来，**Q-Chem** 的若干默认设置发生了重要变化。

    - 现在大多数后 Hartree-Fock 计算默认冻结核心电子；参见第 [6.2](../ch06_correlation/sec_core.md) 节。

    - 为保持不同方法之间的一致性，用于计算自旋-轨道耦合（SOCs）和非绝热耦合（NACs）的关键字已被重命名。

    - 某些较新的密度泛函现在默认使用 SG-2 或 SG-3 求积网格，而在 4.4 版本中所有泛函均默认使用 SG-1。表 [5.3](../ch05_dft/sect_standard-quad.md#table:SG) 列出了各类泛函的默认网格。

