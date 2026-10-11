---
title: "1.3.11 Q-Chem 5.1 新特性"
---

## 1.3.11 **Q-Chem** 5.1 新特性

(2026 年 7 月 4 日)

- •

改进了以下计算的 OpenMP 并行化:

- **–**

SCF 振动频率计算(Zhengting Gan)
- **–**

RIMP2 梯度(Fazle Rob, Joonho Lee, Xintian Feng, Evgeny Epifanovsky)
- •

完全活性空间自洽场(CASSCF)及自适应采样组态相互作用(adaptive sampling CI)(Daniel Levine, Martin Head-Gordon)
- •

Tkatchenko-Scheffler 范德华方法(第 [5.7.5](../ch05_dft/sect_TS.md) 节)和多体色散(many-body dispersion)方法(第 [5.7.6](../ch05_dft/sect_MBD.md) 节)
(Denis Barton, Ka Un Lao, & Rob DiStasio)
- •

耦合簇( coupled-cluster)程序包的增强功能:

- **–**

用于 EOM-CCSD 核心能级激发态与电离态的核/价分离(core/valence separation)
(Marta Vidal, Anna Krylov, Xintian Feng, Evgeny Epifanovsky, Sonia Coriani),第 [7.9.9](../ch07_excited/sub_cvs_eom.md) 节。
- **–**

双光子跃迁的自然跃迁轨道(NTO)分析(Kaushik Nanda, Anna Krylov),第 [7.9.21.6](../ch07_excited/sec_EOMGRAD.md#sec:2PA) 节。
- **–**

复值 EOM 波函数的 NTO 分析(Anna Krylov, Wojciech Skomorowski),第 [7.9.21](../ch07_excited/sec_EOMGRAD.md) 节。
- **–**

Cholesky 分解与 resolution-of-identity CCSD 及 EOM-CCSD 的解析梯度(Xintian Feng, Anna Krylov)。
- **–**

耦合簇方法的性能提升与磁盘占用减少(Evgeny Epifanovsky, Ilya Kaliman, Xintian Feng)。
- •

NTO 分析的新功能: NTO 能量(Anna Krylov),第 [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) 节。
- •

非线性性质的有限差分求值(Marc de Wergifosse, Anna Krylov),第 [10.13.3](../ch10_properties/sect_Romberg.md) 节。
- •

用于 SCF 计算的 Poisson 边界条件(Marc Coons, John Herbert),第 [11.2.11](../ch11_env/sect_PEQS.md) 节。

- **–**

支持在任意(各向异性且非均匀的)介电环境中进行量子化学计算。
- **–**

垂直电离能的非平衡溶剂校正。
- •

能量分解分析(EDA):

- **–**

基于对称适配微扰理论与约束 DFT 的能量分解分析(SAPT/cDFT-EDA),
第 [12.11](../ch12_frag/sect_SAPTEDA.md) 节(Ka Un Lao, Kevin Carter-Fenk, John Herbert)
- **–**

用于 CIS 及 TDDFT/TDA 激发态的 ALMO-EDA,第 [12.7.5](../ch12_frag/sect_ex_eda.md) 节
(Qinghui Ge, Yuezhi Mao, Martin Head-Gordon)
- **–**

EDA2 中的微扰式 ALMO-CTA 与 COVP 分析(Yuezhi Mao, Martin Head-Gordon)
- •

用于计算 *ab initio* Frenkel-Davydov 激子模型内激发/振动能量耦合的解析导数耦合项(Adrian Morrison, John Herbert),第 [12.14](../ch12_frag/sect_AIFDEM.md) 节。
- •

超精细耦合与核四极矩耦合,第 [10.11.4](../ch10_properties/sec_magnetman.md) 节(Eric Berquist, Daniel Lambrecht)
- •

变分双电子约化密度矩阵(v2RDM)方法以及 v2RDM 驱动的完全活性空间自洽场(v2RDM-CASSCF)
方法(Gergely Gidofalvi, Lauren Koulias, Wayne Mullinax, Eugene DePrince)
- •

冻结与受约束的势能面扫描(Yihan Shao),第 [9.6](../ch09_opt/sec_pes-scan.md) 节
- •

将扩展的 ESP 电荷拟合流程用于 RESP  charges 的计算(Yihan Shao)
