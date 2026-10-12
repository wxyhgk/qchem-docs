---
title: "1.3.4 Q-Chem 6.3 新特性"
---

## 1.3.4 **Q-Chem** 6.3 新特性

（2026 年 7 月 4 日）

## 1.3.4.1 6.3.0 版本特性

- **关键字与默认行为变更：**

- 将 MDQ-uFERF 设为 EDA2 任务的默认方法（EDA_UFERF = TRUE）（Hengyuan Shen, Abdulrahman Aldossary, Martin Head-Gordon）
- 新增 REM 控制选项，用于设置片段 CPSCF 最大迭代次数（FRAG_CPSCF_MAXITER）（Yuezhi Mao）
- 在 BW-s2 任务中，将 alpha 参数由 n/100 改为 n/1000（Linus Dittmer, Nikolay V. Tkachenko, Martin Head-Gordon）
- 将 O-V 投影设为 basis2 计算的默认方式（BASISPROJTYPE = OVPROJECTION）（Kuan-Yu Liu）
- 所有 NEO 任务现默认使用紧密的初始猜测（Mathew Chow, Sharon Hammes-Schiffer）
- 对含幽灵原子的 NEO 任务默认使用核库仑猜测（nuclear core guess）（Mathew Chow, Sharon Hammes-Schiffer）
- NEO 计算默认使用联立 SCF（NEO_SIMULTANEOUS_SCF = TRUE）（Mathew Chow, Sharon Hammes-Schiffer）
- **通用特性与改进：**

- 为有限差分及多体展开（many-body expansion）计算新增 MPI 并行化支持
- 为几何优化新增压迫（restraint）势：扭转势与平底势（flat-bottom potential）（Chance W. Lander, Yihan Shao）
- 在可用的约束势能面（PES）扫描选项中新增：键拉伸、r12pr34、键角、原子 1 到两原子中点、原子 1 到质心（COM）、二面角约束（Chance W. Lander, Yihan Shao）
- 重新启用自然轨道跃迁密度矩阵（NATural Transition Orbitals, NTOs）用于随机相位近似（RPA）计算，并修正为使用正确的电子（particle）与空穴（hole）密度矩阵（John Herbert）
- 新的力化学（mechanochemical）压力模型，采用 PV 项能量修正（Felix Zeller）
- **已解决的问题：**

- 在 **Libopt3** 中设置 GEOM_OPT_HESSIAN = READ 时海森矩阵（Hessian）被不必要地重新计算（Yuezhi Mao）
- 移除 libneo 与 librtneo 中电子 JK 梯度计算的瓶颈（Mathew Chow, Sharon Hammes-Schiffer）
- 消除大弥散基组下 Feshbach-Fano 计算中的 NaN 值（Saikat Roy, Wojciech Skomorowski）
- 修复轨道未输出到 **IQmol** 所使用的 .fchk 文件的问题（Kuan-Yu Liu）
- 允许在 STATE_ANALYSIS = TRUE 或 GUI = 2 时对 FAST_XAS 进行报错终止（Kaushik Nanda）
- 修复 SCF_FINAL_PRINT 与 DC-DFT 不兼容的问题（John Herbert）
- 修复 **Libopt3** 中分子点群对称性未被保持的问题（Andrew Gilbert）
- 修复计算 TS-VDW 力时的文件错误（John Herbert）
- **密度泛函理论（Density Functional Theory, DFT）与自洽场（SCF）：**

- 新增“Robust SCF”流程，通过自动选择算法与默认设置提供更可靠的 SCF 收敛（Kaushik Nanda）
- 针对中大规模 DFT 计算的性能提升（Xintian Feng）
- 正则化的限制开壳层 HF/SCF（Canonical ROHF/ROSCF）（Adrian L. Dempwolff）
- 为含时密度泛函理论（Time-Dependent DFT, TDDFT）新充电荷转移度量（charge-transfer metrics）（John Herbert）
- TDDFT-1D 提供改进的 TDDFT/TDA，使 S1/S0 态的交叉更加平滑（Vishikh Athavale, Hung-Hsuan Teh, Joseph Subotnik）
- **已解决的问题：**

- ALMO-CIS/TDA 在大基组下崩溃（Yuezhi Mao）
- DFT 数值积分一致性检查并非总能执行（Xintian Feng）
- **相关方法：**

- 支持激发能（EE）、自旋翻转（SF）、电离势（IP）、电子亲和能（EA）、双电离（DIP）与双电子附着（DEA）的 EOM-CCSDT（Manisha, Prashant Uday Manohar）
- 为 EOM-CCSDT 新增并行性能（Manisha）
- EOM-DEA/DIP-CCSD 方法的解析梯度（Tingting Zhao, Anna Krylov）
- EOM-DEA/DIP-CCSD 方法的自旋-轨道耦合（SOC）与 $<S^{2}>$ 计算（Tingting Zhao, Sai Kotaru, Sahil Gulania, Pavel Pokhilko, Anna Krylov）
- 在 Feshbach–Fano 框架内自动计算库仑波（Coulomb wave），用于俄歇（Auger）速率计算（Saikat Roi, Wojciech Skomorowski）
- 支持冻结芯与开壳层参考的俄歇通道投影（Auger Channel Projection）EOMIP-CCSD（Robin Moorby, Florian Matz, Thomas Jagau）
- 复数值 RI-EOM-CCSD（Simen Camps, Cansu Utku, Thomas Jagau）
- EOM-(EE/SF)-CCSD 在虚频率下的动态极化率（Kaushik Nanda）
- 改进的 EOM-CC 各向异性极化率公式（Kaushik Nanda）
- 采用尺寸一致（size-consistent）Brillouin–Wigner _partitioning_ 的 CC2（Linus Dittmer, Nikolay V. Tkachenko, Martin Head-Gordon）
- 尺寸一致 Brillouin-Wigner 理论的最大物理正则化（Maximum Physical Regularization）（Linus Dittmer, Nikolay V. Tkachenko, Martin Head-Gordon）
- BW-S2 性能提升（Zhenling Wang, Martin Head-Gordon）
- 将 1eX2C 扩展以计算自旋-轨道耦合分量（Richard Kang, Martin Head-Gordon）
- 新算法利用广义非正交 Slater-Condon 规则加速 1C-NOCIS 计算（Rachel Lynn Patterson, Martin Head-Gordon）
- 实现 Dyson 轨道与连续态（平面波）之间的耦合（Madhubani Mukherjee, Anna I. Krylov）
- 新增开关以控制 DO/PW 耦合计算中的平均化（Madhubani Mukherjee, Anna I. Krylov）
- **已解决的问题：**

- 耦合簇势能面（PES）扫描错误地报告 SCF 能量（Kaushik Nanda）
- DIP-EOM-CCSDT 的收敛困难（Manisha）
- 某些基组下俄歇衰变宽度计算因内存分配问题而崩溃（Saikat Roy, Wojciech Skomorowski）
- **分子动力学、非绝热动力学、嵌入方法与溶剂化：**

- SAPT+PCM，为 (X)SAPT 计算提供介电边界（John Herbert）
- 非均匀 PCM（Heterogeneous PCM）允许用户逐个原子修改 PCM 中的介电常数（John Herbert）
- 为 SMD 溶剂化模型新增半数值频率支持（Seminumerical frequency support）（John Herbert）
- 基于能量的广义多体展开（generalized many-body expansion, GMBE）实现（Jake A. Tan, Francisco Ballesteros, Ka Un Lao）
- 基于密度矩阵的广义多体展开（GMBE）实现（Jake A. Tan, Francisco Ballesteros, Ka Un Lao）
- 允许为泊松方程求解器 PEqS 自定义范德华（vdW）半径（John Herbert）
- 允许用户在 EFP 中显式设置极化屏蔽因子（Kaushik Nanda）
- **已解决的问题：**

- 带梯度的多体计算因 FILE_MO_COEFS 错误而失败（Kaushik Nanda, Ryan Steele）
- 当 USE_LIBQINTS = TRUE 时，每一步 SCF 中缺失 EFP 极化能（Xintian Feng）
- 禁用 SMD 下的非绝热耦合（NAC）计算（John Herbert）
- 输出占据-虚轨道对的空间重叠，SPATIAL_OVERLAP_ANALYSIS（John Herbert）
- **片段分析与能量分解分析（Energy Decomposition Analysis, EDA）：**

- 断键轨道（Broken bond orbitals, BBOs）（Alistair J. Sterling, Daniel S. Levine, Abdul Aldossary, Martin Head-Gordon）
- 支持涉及 $\Delta$SCF 激发态的 ALMO(MSDFT) 非绝热耦合（diabatic coupling）计算（Yuezhi Mao）
- 非耦合 FERF（Uncoupled FERF）（Hengyuan Shen, Abdul Aldossary, Martin Head-Gordon）
- **量子核效应整合（NEO 套件）：**

- NEO-MCSCF（Christopher Malbon, Sharon Hammes-Schiffer）
- NEO-MRCI（Christopher Malbon, Sharon Hammes-Schiffer）
- NEO-PCM 解析海森矩阵，用于溶液相频率分析与简正模式分析（Mathew Chow, Sharon Hammes-Schiffer）
- NEO 静电嵌入计算现已支持外部点电荷（Mathew Chow, Sharon Hammes-Schiffer）
- 允许在 NEO-DFT 中使用内嵌额外色散校正的交换-相关泛函（如 wB97X-D、wB97X-D3、B3LYP-D3(BJ) 等）（Mathew Chow, Sharon Hammes-Schiffer）
- 为 NEO（能量、梯度、海森矩阵）及 RT-NEO（实时动力学与实时-Ehrenfest）计算新增完整的 DFT-D 支持（Mathew Chow, Sharon Hammes-Schiffer）
- NEO 现已完整支持赝势（包括能量、梯度与海森矩阵）（Mathew Chow, Sharon Hammes-Schiffer）
- NEO 联立求解器现已支持 DIIS_GDM（Mathew Chow, Sharon Hammes-Schiffer）
- **通过以下方式提升性能：**

- NEO-HF 与 NEO-DFT 方法的联立 GDM 优化（Mathew Chow, Sharon Hammes-Schiffer）
- 核 SCF 初始猜测（Mathew Chow, Sharon Hammes-Schiffer）
- 推广联立 DIIS 与 GDM 优化以处理任意“N”个量子质子，从而加速 NEO Hartree 积计算（Mathew Chow, Sharon Hammes-Schiffer）
- 对联立 NEO-PCM 计算的多项改进，包括支持 Hartree 积以及多质子 CNEO 海森矩阵计算（Mathew Chow, Sharon Hammes-Schiffer）
- 通用轨道优化器库的更新与改进（Christopher Malbon, Sharon Hammes-Schiffer）
- 通过增加预条件子（preconditioner）提升 CNEO 海森矩阵计算性能（Eno Paenurk, Sharon Hammes-Schiffer）
- 提升 NEO 海森矩阵与 CNEO 海森矩阵代码的稳定性与性能（Mathew Chow, Sharon Hammes-Schiffer）
- **已解决的问题：**

- 修复核 AUTOSAD 不会为子任务指令读取 NEO_PURECART 的问题（Mathew Chow, Sharon Hammes-Schiffer）
- 修复 MAX_SCF_CYCLES 对联立 NEO-SCF 求解器无效的问题（Mathew Chow, Sharon Hammes-Schiffer）
- 修复 NEO 联立 SCF 与 NEO Hartree 积组合使用时的内存问题（Mathew Chow, Sharon Hammes-Schiffer）

## 1.3.4.2 6.3.1 版本特性

- **关键字与默认行为变更：**

- 移除 rel2e 区块
- 为与 STATE_ANALYSIS 冲突的 TD-DFT 分析工具添加兜底保护（backstop）（John Herbert）
- **通用特性与改进：**

- 将 DFT-D4 升级至 3.7.0 版本
- 在谐振子约束（harmonic confiner）计算的每一步中输出能量与梯度（John Herbert）
- 改进输出格式（John Herbert, Yuezhi Mao）
- 解决 HF-3c 与 PBEh-3c 解析频率存在的问题（John Herbert）
- **密度泛函理论（DFT）与自洽场（SCF）：**

- 为 GOSTSHYP（表面面元上高斯函数模拟静水压力）计算添加外腔校正（outer cavity correction）（Felix Zeller, Nico Kissing, Tim Neudecker）
- 允许在 CIS-1D 计算中设置可调的最大迭代次数（John Herbert）
- 为双杂化（double hybrids）功能提供清晰、一致的能量组分输出
- **已解决的问题：**

- 双杂化泛函结果错误
- sr-PBE 相关泛函的数值问题（Abel Carreras, David Casanova）
- **相关方法：**

- 改进格林函数（Green functions）积分与 Feshbach 计算（Saikat Roy, Wojciech Skomorowski）
- **已解决的问题：**

- 某些 CASSCF 计算中的段错误（segmentation fault）
- RAS-CI 计算（Abel Carreras, David Casanova）
- EOM-DEA/DIP-CCSD 中三重态猜测向量（guess vector）的问题（Tingting Zhao, Anna Krylov）
- **片段分析与能量分解分析：**

- （本节内容见 6.3.0 版本特性中的相应条目）
