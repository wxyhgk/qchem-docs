---
title: "1.3.18 Q-Chem 4.0 新特性"
---

## 1.3.18 **Q-Chem** 4.0 新特性

（2026 年 7 月 4 日）

- 新型交换关联泛函（第 [5.3](../ch05_dft/sect_XCfuncs.md) 节）：

- 采用 Becke 和 Johnson 提出的 XDM 模型的密度泛函色散校正，以高效、解析的形式实现（Z. Gan, E. I. Proynov 和 J. Kong；第 [5.7.4](../ch05_dft/sect_XDM.md) 节）。
- Langreth 及其合作者提出的范德华密度泛函 vdW-DF-04 与 vdW-DF-10（O. Vydrov；第 [5.7.2](../ch05_dft/sect_VV10.md) 节）。
- VV09 和 VV10，新型解析色散泛函（O. Vydrov, T. Van Voorhis；第 [5.7.2](../ch05_dft/sect_VV10.md) 节）
- 用于非共价相互作用的 DFT-D3 经验色散校正方法（S.-P. Mao 和 J.-D. Chai；第 [5.7.3](../ch05_dft/subsec_DFT-D.md) 节）。
- $\omega$B97X-2，一种基于长程校正 B97 泛函的双杂化泛函，对中等程与长程相互作用的描述有所改进（J.-D. Chai 和 M. Head-Gordon；第 [5.9](../ch05_dft/subsec_dhdft.md) 节）。
- XYGJ-OS，一种双杂化泛函，可在接近化学精度的水平上预测非键相互作用与热化学性质（X. Xu, W. A. Goddard 和 Y. Jung；第 [5.9](../ch05_dft/subsec_dhdft.md) 节）。
- 用于计算近边 X 射线吸收谱（NEXAFS）的短程校正泛函（N. A. Besley；第 [7.12.2](../ch07_excited/subsec_TDDFT-Xray.md) 节）。
- 用于含时密度泛函理论（TDDFT）的 LB94 渐近校正交换关联泛函（Y.-C. Su 和 J.-D. Chai；第 [5.10.2](../ch05_dft/sect_LB94.md) 节）。
- 在密度泛函理论（DFT）中引入非动力学关联，采用 Becke05 模型的高效 RI 实现，并具有完全的解析形式（E. I. Proynov, Y. Shao, F. Liu 和 J. Kong；第 [5.3](../ch05_dft/sect_XCfuncs.md) 节）。
- TPSS 及其杂化版本 TPSSh，以及 rPW86（F. Liu 和 O. Vydrov）。
- 双杂化泛函 B2PLYP-D（J.-D. Chai）。
- 来自 Mori-Sánchez、Cohen 和 Yang 的超广义梯度近似（Hyper-GGA）泛函 MCY2（F. Liu）。
- SOGGA、SOGGA11 及 SOGGA11-X 系列 GGA 泛函（R. Peverati, Y. Zhao 和 D. G. Truhlar）。
- M08-HX 与 M08-SO 系列高 HF 交换比例的元 GGA（meta-GGA）泛函（Y. Zhao 和 D. G. Truhlar）。
- M11-L 与 M11 系列元 GGA 泛函（R. Peverati, Y. Zhao, D. G. Truhlar）。
- 改进的 DFT 算法：

- 用于快速计算基于网格的 XC 求积的多分辨率交换关联（mrXC）方法（S. T. Brown, C.-M. Chang 和 J. Kong；第 [5.5.5](../ch05_dft/sect_mrXC.md) 节）。
- 对偶基组 DFT 中 XC 部分的高效计算（Z. Gan 和 J. Kong；第 [4.4.5](../ch04_scf/sect_projection.md) 节）。
- 采用在不同基组规模、网格规模以及不同泛函级别之间“三级跳”的快速 DFT 计算方法（J. Deng, A. T. B. Gilbert 和 P. M. W. Gill；第 [4.8](../ch04_scf/sect_HFPC.md) 节）。
- 采用原子分辨率恒等（resolution-of-identity）算法加速 DFT 与 HF 计算（A. Sodt 和 M. Head-Gordon；第 [4.6.6](../ch04_scf/sect_ri-DFT.md) 节）。
- 后 Hartree–Fock 方法：

- 为提升多核架构性能而重写的、显著增强的耦合簇（coupled-cluster）代码，包括 CCSD 的能量与梯度计算、EOM-EE/SF/IP/EA-CCSD 的能量计算以及 CCSD(T) 能量计算（E. Epifanovsky, M. Wormit, T. Kús, A. Landau, D. Zuev, K. Khistyaev, I. Kaliman, A. I. Krylov 和 A. Dreuw；第 [6](../ch06_correlation/chap_correlation.md)、[7](../ch07_excited/chap_excited.md) 章）。
- 采用冻结自然轨道（frozen natural orbitals）的快速、高精度耦合簇计算（A. Landau, D. Zuev 和 A. I. Krylov；第 [6.15.1](../ch06_correlation/sec_FNOCC.md) 节）。
- 基于微扰理论、满足尺寸一致性（size-consistent）的 ADC 方案处理关联激发态（M. Wormit 和 A. Dreuw；第 [7.10](../ch07_excited/sect_exadc.md) 节）。
- 用于多组态基态与多电子激发态的限制活性空间自旋翻转（spin-flip）方法（P. M. Zimmerman, F. Bell, D. Casanova 和 M. Head-Gordon；第 [7.2.3.2](../ch07_excited/Ch7.S2.SS3.md#topic:sf) 节）。
- 用于描述强关联的后 Hartree–Fock 方法：

- 面向强关联问题的“perfect quadruples（完美四激发）”与“perfect hextuples（完美六激发）”方法（J. A. Parkhill 和 M. Head-Gordon；第 [6.14.5](../ch06_correlation/topic_lpcc.md) 节）。
- 用于多重键断裂研究的耦合簇价键（CCVB）方法（D. W. Small, K. V. Lawler 和 M. Head-Gordon；第 [6.19](../ch06_correlation/sect_pairing.md) 节）。
- 用于激发态的 TDDFT：

- TDDFT 的核梯度（Z. Gan, C.-P. Hsu, A. Dreuw, M. Head-Gordon 和 J. Kong；第 [7.3.1](../ch07_excited/sect_tddftintro.md) 节）。
- 用于研究电荷转移反应的带电态直接耦合方法（Z.-Q. You 和 C.-P. Hsu；第 [10.15.2](../ch10_properties/topic_dc.md) 节）。
- Tamm-Dancoff 近似（TDA）下 TDDFT 激发态解析 Hessian（J. Liu 和 W. Liang；第 [7.3.8](../ch07_excited/subsec_tddft-hessian.md) 节）。
- 采用最大重叠方法（MOM）自洽地求解激发态（A. T. B. Gilbert, N. A. Besley 和 P. M. W. Gill；第 [7.7.2](../ch07_excited/ex_OpSing.md) 节）。
- 通过约束 DFT 计算带电荷约束的组态，再利用其组态相互作用计算化学反应（Q. Wu, B. Kaduk 和 T. Van Voorhis；第 [5.11](../ch05_dft/topic_cdft.md) 节）。
- TDDFT 激发态中电荷转移的重叠分析（N. A. Besley；第 [7.3.3](../ch07_excited/subsec_TRNSS.md) 节）。
- 针对电荷或能量转移，采用 Boys 或 Edmiston-Ruedenberg 局域化方法将非绝热态局域化（J. E Subotnik, R. P. Steele, N. Shenvi 和 A. Sodt；第 [10.15.1.3](../ch10_properties/Ch10.S15.SS1.md#subsec:diabatic) 节）。
- 自旋翻转 TDDFT 的非共线形式体系（Y. Shao, Y. A. Bernard 和 A. I. Krylov；第 [7.3](../ch07_excited/sect_tddft.md) 节）
- 溶剂化与凝聚相建模

- 通过 SWIG-PCM 为溶剂化分子构建平滑的自由能面，适用于 QM 及 QM/MM 计算，并包含线性标度的 QM/MM/PCM 算法（A. W. Lange 和 J. M. Herbert；第 [11.2.3](../ch11_env/topic_pcm-em.md)、[11.2.5](../ch11_env/subsec_linear-PCM.md) 节）。
- Klamt 提出的 COSMO 溶剂化模型，支持 DFT 能量与梯度计算（Y. Shao；第 [11.2.8](../ch11_env/subsec_COSMO-Klamt.md) 节）。
- 通过 EFP 实现可极化的显式溶剂，支持基态与激发态计算，涵盖 DFT/TDDFT、CCSD/EOM-CCSD 以及 CIS 和 CIS(D) 级别；同时提供常见溶剂的有效碎片库，并支持 EFP–EFP 计算的能量与梯度（V. Vanovschi, D. Ghosh, I. Kaliman, D. Kosenkov, C. F. Williams, J. M. Herbert, M. S. Gordon, M. W. Schmidt, Y. Shao, L. V. Slipchenko 和 A. I. Krylov；第 [11.5](../ch11_env/sect_efp.md) 节）。
- 结构优化、振动与动力学：

- 用于高效自动化反应路径搜索的“freezing（冻结）”与“growing（生长）”字符串方法（A. Behn, P. M. Zimmerman, A. T. Bell 和 M. Head-Gordon；第 [9.3.2](../ch09_opt/sect_fstring.md) 节）。
- 跟随内禀反应坐标（IRC）代码的稳健性得到改进（M. Head-Gordon）。
- 在平衡态下通过路径积分对核运动进行量子力学处理（R. P. Steele；第 [9.10](../ch09_opt/sec_PIMC.md) 节）。
- 利用部分 Hessian 振动分析计算所关注的局域振动模式（N. A. Besley；第 [10.8.4](../ch10_properties/partial-hess.md) 节）。
- 基于 $Z$ 矢量外推的、加速的 MP2 和/或对偶基组 *ab initio* 分子动力学方法（R. P. Steele；第 [4.7.3](../ch04_scf/subsec_dual-dyn.md) 节）。
- 准经典 *ab initio* 分子动力学（D. S. Lambrecht 和 M. Head-Gordon；第 [9.9.6](../ch09_opt/subsec_QCT.md) 节）。
- 基于片段的方法：

- 用于计算和分析二聚体相互作用能的对称适配微扰理论（SAPT）（L. D. Jacobson, M. A. Rohrdanz 和 J. M. Herbert；第 [12.9](../ch12_frag/topic_sapt.md) 节）。
- SAPT 的多体推广（“XSAPT”），结合经验色散校正，可在大型团簇上以低成本实现高精度（L. D. Jacobson, K. U. Lao 和 J. M. Herbert；第 [12.10](../ch12_frag/sect_XSAPT.md) 节）。
- 基于截断多体展开的方法，包括片段分子轨道（FMO）方法（K. U. Lao 和 J. M. Herbert；第 [12.12](../ch12_frag/sec_MBE.md) 节）。
- 性质计算与波函数分析：

- 通过局域轨道成键分析（LOBA）研究金属氧化态（A. J. W. Thom, E. J. Sundstrom 和 M. Head-Gordon；第 [10.2.6](../ch10_properties/sect_LOBA.md) 节）。
- Hirshfeld 布居分析（S. Yeganeh；第 [10.2.2](../ch10_properties/subsec_pop_anal.md) 节）。
- 采用 Johnson 和 Yang 提出的 NCI 算法对非共价相互作用进行可视化（Y. Shao；第 [10.5.6](../ch10_properties/NCI-plots.md) 节）。
- 在网格上计算跃迁密度的静电势（Y. Shao；第 [10.5.8](../ch10_properties/sec_ESP.md) 节）。
- 对现代计算平台的支持

- CC、EOM 与 ADC 方法具备高效的多线程并行性能。
- 共享内存并行 DFT 与 Hartree-Fock（Z. Gan, Y. Shao 和 J. Kong）以及 RI-MP2（M. Goldey 和 M. Head-Gordon；第 [6.17](../ch06_correlation/CCparallel.md) 节）在多核系统上的性能得到提升。
- 在 GPU 上加速的 RI-MP2 计算（R. Olivares-Amaya, M. Watson, R. Edgar, L. Vogt, Y. Shao 和 A. Aspuru-Guzik；第 [6.6.4](../ch06_correlation/sect_gpu-rimp2.md) 节）。
- 图形用户界面（GUI）：

- 输入文件生成、**Q-Chem** 作业提交与可视化由 **IQmol** 支持，这是由 Andrew Gilbert 开发的全集成 GUI。**IQmol** 是一款免费软件。
