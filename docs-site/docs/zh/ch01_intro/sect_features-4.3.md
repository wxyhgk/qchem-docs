---
title: "1.3.14 Q-Chem 4.3 新特性"
---

## 1.3.14 **Q-Chem** 4.3 新特性

(2026 年 7 月 4 日)

- 电子态之间的解析导数耦合（analytic derivative coupling），即非绝热耦合（nonadiabatic coupling），可在 CIS、自旋翻转 CIS（spin-flip CIS）、TDDFT 以及自旋翻转 TDDFT 级别下计算（S. Fatehi, Q. Ou, J. E. Subotnik, X. Zhang, J. M. Herbert）；第 [9.8](../ch09_opt/topic_namd.md) 节。
- 用于 XSAPT 的第三代（“+D3”）色散势（K. U. Lao, J. M. Herbert）；第 [12.10](../ch12_frag/sect_XSAPT.md) 节。
- 非平衡态 PCM（Non-equilibrium PCM），可用于计算溶液中的垂直激发能（TDDFT 级别）与电离能（Z.-Q. You, J. M. Herbert）；第 [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM) 节。
- 针对 CC 与 EOM-CC 波函数的电子态自旋-轨道耦合（spin-orbit coupling）（E. Epifanovsky, J. Gauss, A. I. Krylov）；第 [7.9.21.4](../ch07_excited/sec_EOMGRAD.md#sec:EOMSOC) 节。
- 用于精确交换（exact exchange）计算的 PARI-K 方法，在杂化 DFT（hybrid DFT）计算中，对于三-$\zeta$ 及更大的基组（basis set）可带来显著的速度提升（S. Manzer, M. Head-Gordon）。
- 利用 EOM-CC 波函数计算双光子吸收（two-photon absorption）的跃迁矩（transition moment）与截面（cross section）（K. Nanda, A. I. Krylov）；第 [7.9.21.6](../ch07_excited/sec_EOMGRAD.md#sec:2PA) 节。
- 针对 ADC 与 CC/EOM-CC 方法的新型激发态分析（excited-state analysis）（M. Wormit）；第 [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md)) 节。
- 针对 EOM-IP-CCSD 与 EOM-EA-CCSD 的新型 Dyson 轨道（Dyson orbital）代码（A. Gunina 与 A. I. Krylov；第 [7.9.29](../ch07_excited/topic_dyson.md) 节）。
- 针对 CAP-EOM-CCSD 的跃迁矩、态偶极矩（state dipole moment）与 Dyson 轨道（T.-C. Jagau 与 A. I. Krylov；第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节及第 [7.9.29](../ch07_excited/topic_dyson.md) 节）。
- TAO-DFT：热辅助占据密度泛函理论（Thermally-assisted-occupation density functional theory）（J.-D. Chai；第 [5.12.3](../ch05_dft/ex_ptao.md) 节）。
- MP2[V]，一种近似 MP2 能量的双基组（dual basis）方法（J. Deng 与 A. Gilbert）。
- 针对带电体系的迭代式 Hirshfeld 布居分析（iterative Hirshfeld population analysis），以及 CM5 半经验电荷格式（semi-empirical charge scheme）（K. U. Lao 与 J. M. Herbert；第 [10.2.2](../ch10_properties/subsec_pop_anal.md) 节）。
- 新型 DFT 泛函（第 [5.3](../ch05_dft/sect_XCfuncs.md) 节）：

- 含经验色散校正的长程校正（long-range corrected）泛函：$\omega$M05-D、$\omega$B97X-D3 与 $\omega$M06-D3（Y.-S. Lin, K. Hui 与 J.-D. Chai。
- PBE0_DH 与 PBE0_2 双杂化（double-hybrid）泛函（K. Hui 与 J.-D. Chai；第 [5.9](../ch05_dft/subsec_dhdft.md) 节）。
- AK13（K. Hui 与 J.-D. Chai）。
- LFA 渐近校正（asymptotic correction）格式（P.-T. Fang 与 J.-D. Chai）。
- 采用冻结轨道近似（frozen-orbital approximation）计算 LDA/GGA 基本能隙（fundamental gap）（K. Hui 与 J.-D. Chai；第 [5.12.2](../ch05_dft/sect_foaDD.md) 节）。
