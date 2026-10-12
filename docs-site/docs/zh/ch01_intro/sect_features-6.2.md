---
title: "1.3.5 Q-Chem 6.2 新特性"
---

## 1.3.5 **Q-Chem** 6.2 新特性

(2026 年 7 月 4 日)

## 1.3.5.1 6.2.0 版本特性

- **默认行为变更：**

- 对于从前一作业读取初始猜测（guess）的频率计算作业，设置 POINT_GROUP_SYMMETRY = FALSE 以避免重新取向（reorientation）
- 将 NO_REORIENT = 1 和 POINT_GROUP_SYMMETRY = 0 设为谐振限制器（harmonic confiner）作业的默认值
- 将改进的初始猜测 Hessian 设为几何优化的默认选项（INITIAL_HESSIAN = MODEL）
- 对 occ-RI-K 频率计算作业默认启用 RI-K 虚轨道校正
- **通用功能与改进：**

- NEO 多态密度泛函理论（NEO Multistate DFT, NEO-MSDFT）（Joseph Dickinson、Qi Yu、Sharon Hammes-Schiffer）
- 新增基于实时核-电子轨道（real-time nuclear-electronic orbital, RT-NEO）的核-电子量子动力学模拟（Tao E. Li、Mathew Chow、Sharon Hammes-Schiffer）
- 为 NEO 方法及 RT-NEO 方法新增对 D3 经验色散校正（能量与梯度）以及有效核势（Effective Core Potential, ECP）（能量与梯度）的支持（Mathew Chow、Sharon Hammes-Schiffer）
- 针对单一 NEO 中心的约束 NEO（Constrained NEO, CNEO）（Eno Paenurk、Sharon Hammes-Schiffer）
- 在 NEO 方法中新增 SCS-RIMP2 和 SOS-OOMP2（Jonathan Fetherolf、Sharon Hammes-Schiffer）
- 通过同时 DIIS 优化加速 NEO-SCF（Mathew Chow、Sharon Hammes-Schiffer）
- 新增基于独立原子轨道（independent atomic orbitals, IAOs）的原子多极矩计算（Alexandra McIsaac、Abdulrahman Aldossary、Martin Head-Gordon）
- 更新原子（atomic）作业失败时不允许 AUTOSAD $\to$ CORE 回退的情形列表（Yuezhi Mao）
- 新语法支持外加电场沿化学键跟随（Tarek Scheele、Tim Neudecker）
- TAO-DFT 的实时扩展（RT-TAO）（Hung-Yi Tsai、Jeng-Da Chai）
- 当 SCF_FINAL_PRINT 设置为 TRUE 时，SCF 能量输出现将单电子项拆分为动能、核吸引及其余项
- 解决了以下问题：

- 使用 NEO 中的 EPC 泛函时氢同位素质量不正确（Mathew Chow、Zhen (Coraline) Tao、Sharon Hammes-Schiffer）
- NEO 中范围分离泛函的 Hessian 实现（Eno Paenurk 和 Sharon Hammes-Schiffer）
- 复数 RHF 的 READ_REAL 初始猜测失败（Yuezhi Mao）
- **Libopt3** 对接近零的本征值之结构类型误分类
- 少数几何优化情形中出现的 "SVD Failed" 无效步长错误
- **密度泛函理论与自洽场（Self-Consistent Field, SCF）：**

- 实现 DFT/CIS，包括针对 X 射线光谱学的新的参数化方案（Aniket Mandal、John Herbert）
- 在 QCAUX 中为 DFT/CIS 新增 TZVP 基组（Basis Set）（Aniket Mandal、John Herbert）
- 在 ROKS 计算中实现开壳层混合的抑制（Juanes Arias-Martinez、Martin Head-Gordon）
- 允许 Grimme D4 色散校正中 $s_{8}$ 取负值
- 为受限与非受限 TDKS 增加偶极矩过滤（dipole filtering）（John Herbert、Avik Kumar Ojha）
- 输出轨道的空间重叠（occ/virt 对之间的中间重叠）（John Herbert）
- 将 occ-RI-K 在 SCF 收敛后的虚轨道校正改为可选项
- 为 GEN_SCFMAN 启用 MakeMeSAD
- 为 cc-pV6Z 和 aug-cc-pV6Z 新增 SAD 初始猜测
- 为 CDFT-CI 禁用 AUTOSAD 初始猜测（John Herbert）
- 为 RPA 禁用自然轨道跃迁密度（NTO）（John Herbert）
- 解决了以下问题：

- 非谐频率计算中通过 FDIFF_DER 进行的作业控制（Yuezhi Mao）
- DFT 非谐频率计算失败（Yuezhi Mao）
- 非受限 TDKS 的重启动初始化（Hung-Yi Tsai、Jeng-Da Chai）
- 与使用多重壳层（multishells）基组相关的 RI 缺陷（注意：除非使用辅助多重壳层基组，否则不影响大多数 RI 计算）
- **相关方法：**

- 新增超精细耦合代码，用于计算单重态/三重态激发 CIS 态之间的耦合（Samuel May、Joseph Subotnik）
- 将 1C-NOCIS 推广至双电子开壳层单重态（Juanes Arias-Martinez、Hamlin Wu、Martin Head-Gordon）
- 实现 ACP-EOMIP-CCSD 方法以计算部分俄歇（Auger）衰变宽度（Florian Matz、Thomas Jagau）
- 内置基于 Dyson 轨道计算截面和角分布的功能（Madhubani Mukherjee、Sarai Folkestad、Anna Krylov）
- 为 CVS-EOM 方法针对俄歇衰变、ICD 及相关过程引入自然俄歇轨道（Natural Auger Orbitals）（Nayanthara K. Jayadev、Anna I. Krylov）
- 新增 BW-s2 方法（Kevin Carter-Fenk、Martin Head-Gordon）
- 将随机分辨率恒等（stochastic resolution of identity）方法应用于 CC2（sRI-CC2），用于激发态能量计算（Chongxiao Zhao、Wenjie Dou、Joonho Lee）
- 针对 EE 和 SF 态的 EOM-CCSDT（Manisha、Prashant Uday Manohar）
- 解决了以下问题：

- 当 MEM_STATIC 值过大时，旧版 RI-MP2 代码崩溃（Yuezhi Mao）
- CCSD 中单粒子密度矩阵可分离部分计算的错误（Yongbin Kim、Madhubani Mukherjee、Anna Krylov）
- 共振俄歇衰变计算中自然俄歇轨道的 Molden 文件被覆盖（Nayanthara Karippara Jayadev、Anna Krylov）
- **分子动力学、非绝热动力学、嵌入与溶剂化改进：**

- 外部/嵌入势读取（Huseyin Aksu、Barry Dunietz）
- 当 SCF_GUESS = READ 时，在第一次 SCF 迭代即开启 PCM，
从而加快收敛（Yuezhi Mao）
- 对 FRAGMO 和 AUTOSAD，在第二次几何优化循环的首次 SCF 迭代即开启 PCM（Yuezhi Mao）
- 澄清 COSMO 中含义模糊的输出（John Herbert）
- 新增解析的 X-HCFF Hessian（Rahel Weiss、Felix Zeller、Tim Neudecker）
- 解决了以下问题：

- SMX 与虚原子（ghost atoms）联用时的越界访问错误
- SOLVENT_METHOD = TRUE 触发 Kirkwood 模型的不当行为（John Herbert）
- 为 QM/MM 计算补充缺失的 qarchive 文件（Xiaoliang Pan、Yihan Shao）
- 在多次 SMD 计算作业中，I 和 At 原子的范德华半径被错误地增大（Zheng Pei）
- **片段与能量分解分析改进：**

- 为 libwfa 新增关于离子态/共价态的额外输出（Felix Plasser）
- 解决了以下问题：

- 非微扰 CTA 中偶发的崩溃（Yuezhi Mao）
- **后处理功能：**

- 使用 ezMagnet 计算 g 张量（Sven Kähler、Antonio Cebreiro-Gallardo、Pavel Pokhilko、David Casanova 和 Anna I. Krylov）
