---
title: "1.3.13 Q-Chem 4.4 新特性"
---

## 1.3.13 **Q-Chem** 4.4 新特性

(2026 年 7 月 4 日)

- 用于能量和力计算中精确交换（exact exchange）求值的 occ-RI-K 算法
(S. Manzer, F. Rob, M. Head-Gordon)；参见第 [4.6.8](../ch04_scf/subsec_occrik.md) 节。
- 组合优化交换-关联泛函（combinatorially-optimized exchange-correlation functionals）
(N. Mardirossian, M. Head-Gordon)；参见第 [5.3](../ch05_dft/sect_XCfuncs.md) 节：

- $\omega$B97M-V（带 VV10 非局域关联的 range-separated hybrid meta-GGA 泛函）
- B97M-V（带 VV10 非局域关联的 meta-GGA 泛函）
- $\omega$B97X-V（带 VV10 非局域关联的 range-separated hybrid 泛函）
- 实现来自文献的新型交换-关联泛函（N. Mardirossian 和 M. Head-Gordon；
参见第 [5.3](../ch05_dft/sect_XCfuncs.md) 节）。包括：

- MGGA_MS0, MGGA_MS1, MGGA_MS2, MGGA_MS2h, MGGA_MVS, MGGA_MVSh, PKZB, revTPSS, revTPSSh, SCAN, SCAN0,
PBEsol, revPBE, revPBE0
- N12, N12-SX, GAM, MN12-L, MN12-SX, MN15-L, dlDF
- VV10, LC-VV10
- B97-K, B97-D3(0), B97-3, $\tau$-HCTH, $\tau$-HCTHh
- SRC1-R1, SRC1-R2, SRC2-R1, SRC2-R2
- B1LYP, B1PW91, MPW1K, LRC-BOP, BHH, BB1K, PW6B95, PWB6K, B2PLYP
- 无 Hessian 极小点验证（Hessian-free minimum point verification）(S. Sharada, M. Head-Gordon)；参见第 [9.3.3](../ch09_opt/sect_approx_hess.md) 节。
- 基于激子（exciton）的激发态模型：

- 用于多生色团（multi-chromophore）体系耦合激发的 *ab initio* Frenkel-Davydov 模型
(A. F. Morrison, J. M. Herbert)；参见第 [12.14](../ch12_frag/sect_AIFDEM.md) 节。
- 分子间相互作用的 TDDFT [TDDFT(MI)]，一套用于多生色团体系高效 TDDFT 计算的局域激发近似方法，
也适用于含显式溶剂分子环境的单生色团体系
(J. Liu, J. M. Herbert)；参见第 [12.15](../ch12_frag/sec_TDDFT_MI.md) 节。
- 多体（many-body）及 XSAPT 方法的改进（K. U. Lao, J. M. Herbert）：

- MPI 并行的多体展开（many-body expansion）及解析梯度（参见第 [12.12](../ch12_frag/sec_MBE.md) 节）。
- XSAPT 的高效原子轨道实现，适用于闭壳层和开壳层体系
（参见第 [12.10.3](../ch12_frag/subsec_AO-XSAPT_KS_D.md) 节）。
- 用于 *ab initio* 分子动力学（molecular dynamics）的恒温器（thermostat）(R. P. Steele, J. M. Herbert)。
- QM/MM 计算中 Ewald 求和的解析能量梯度（analytic energy gradient）(Z. C. Holden, J. M. Herbert)。
- 沸石（zeolite）QM/MM 方法（J. Gomes, M. Head-Gordon）。
- 用于激发能、电离能及电子附着能的 EOM-MP2 方法
(A. Kunitsa, K. Bravaya)；参见第 [7.9.5.1](../ch07_excited/Ch7.S9.SS5.md#sec:EOMMP2) 节。
- 利用 CCSD 和 EOM-CCSD 波函数求值极化率（polarizabilities）
(K. Nanda, A. I. Krylov)；参见第 [7.9.21.8](../ch07_excited/sec_EOMGRAD.md#sec:EOMpol) 节。
- CC 和 EOM-CC 方法的分布式内存并行实现，以及基于磁盘算法的性能优化（E. Epifanovsky, I. Kaliman, A. I. Krylov）。
- SCF 计算中最大重叠方法（maximum overlap method, MOM）的改进（A. T. B. Gilbert）；参见第 [7.7.2](../ch07_excited/ex_OpSing.md) 节。
- 用于描述 ADC 激发态计算中溶剂效应的非平衡态（non-equilibrium）PCM 方法
(J.-M. Mewes, A. Dreuw)；参见第 [7.10.11](../ch07_excited/topic_abs-adc.md) 节。
- 自旋反转 ADC 方法（spin-flip ADC method）(D. Lefrancois, A. Dreuw)；参见第 [7.10.8](../ch07_excited/sect_SF-ADC.md) 节。
