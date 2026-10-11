---
title: "1.3.7 Q-Chem 6.0 新特性"
---

## 1.3.7 **Q-Chem** 6.0 新特性

(2026 年 7 月 4 日)

## 1.3.7.1 6.0.2 版本特性

- •

**通用功能与改进：**

- **–**

为新的默认几何优化器启用 Molden 支持
- **–**

改进反应路径（IRC）计算的输出（John Herbert）
- **–**

改进轨道回转半径（radii of gyration）输出的格式（John Herbert）
- **–**

改进输入区块的错误捕获（John Herbert）
- **–**

在 fchk 和 archive 文件中包含单电子矩阵
- **–**

解决核-电子轨道（nuclear-electronic orbital, NEO）基组的纯函数与 Cartesian 函数指定问题（Mathew Chow, Sharon Hammes-Schiffer）
- **–**

解决以下问题：

- *

高电荷过渡金属原子的 AUTOSAD/I-Hirshfeld 多重度问题（Kevin Carter-Fenk）
- *

惩罚函数（penalty function）优化的 molden 输出问题
- *

CIS Boys 绝热态（diabatic states）精确梯度与导数耦合的计算问题（Vishikh Athavale, Joseph Subotnik）
- *

SOS-CIS(D) 计算中 SOS_UFACTOR 不可变的问题
- *

DUAL_BASIS_ENERGY 计算中电荷和多极矩不一致的问题
- *

使用 SAD 初始猜测的 SCF_GUESS_MIX 计算问题（Yuezhi Mao）
- •

**密度泛函理论（Density Functional Theory, DFT）与自洽场（Self-Consistent Field, SCF）：**

- **–**

改进 RI-JK 导数算法
- •

**相关方法：**

- **–**

支持将 RAS-CI 性质绘制到 cube、**MolDen** 和 FChk 文件中（Abel Carreras, David Casanova）
- •

**分子动力学、非绝热动力学、嵌入与溶剂化：**

- **–**

为 PCM 任务增加单原子热力学信息的打印（John Herbert）
- •

**片段与能量分解分析改进：**

- **–**

解决片段使用混合基组时相互作用能错误的问题（Yihan Shao, Yuezhi Mao）
- •

**其他：**

- **–**

为 SCF_ALGORITHM 选项 NEWTON_CG 和 NEWTON_MINRES 添加示例任务（Yuezhi Mao）
- **–**

添加带外部电荷的 EDA2 计算示例任务（Yuezhi Mao, Yihan Shao）
- **–**

重命名基于 GEN_SCFMAN_EDA2 的变分 PA/CTA 示例任务（Yuezhi Mao, Hengyuan Shen）
- **–**

为 TDDDFT 和 SF-TDDFT 添加 SOC-NTO 分析（Saikiran Kotaru, Anna Krylov）

## 1.3.7.2 6.0.1 版本特性

- •

**通用功能与改进：**

- **–**

恢复对 IGDESP 的支持（供 CHARMM 使用）（John Herbert）
- **–**

实现内存高效的 GOSTSHYP 算法（Felix Zeller）
- **–**

针对 HF 和 MP2，实现使用规范无关原子轨道（gauge-independent atomic orbitals, GIAOs）的有限场化学屏蔽与磁化率计算（Jonathan Wong, Brad Ganoe, Tim Neudecker, Adam Rettig, Xiao Liu, Joonho Lee）
- **–**

解决以下问题：

- *

**Libopt3** 中优化的 molden 输出问题
- *

使用 PCM 的 **Libopt3** Hessian 计算问题
- *

将分子轨道（MO）系数和能量写入 qarchive 文件的问题
- *

清理拓扑检查的打印输出
- *

修复几何优化过程中步长均方根（RMS）的打印
- •

**分子动力学、非绝热动力学、嵌入与溶剂化改进：**

- **–**

实现结合 RAS-SF 的定态（state-specific）PCM（Bushra Alam, Hanjie Jiang, John Herbert, Paul Zimmerman）
- •

**片段与能量分解分析改进：**

- **–**

解决基于投影的嵌入（projection-based embedding）计算中冻结的环境占据轨道未按能量排序的问题（Yuezhi Mao）
- •

**其他：**

- **–**

为 DFT SOC 计算添加注释以标识任务进度（Saikiran Kotaru）
- **–**

为某些优化任务缺少解析 Hessian 添加警告
- **–**

添加打印以区分 CPCM1 与 CPCM2

## 1.3.7.3 6.0.0 版本特性

- •

**默认行为变更：**

- **–**

将默认积分阈值（THRESH）收紧为 SCF_CONVERGENCE + 4，并对 DIIS 和 GDM 使用相同阈值
- **–**

针对 VV10 泛函，将 FD_MAT_VEC_PROD 的默认值设为 FALSE（Yuezhi Mao）
- **–**

关闭在网格上自动计算静电势（Felix Plasser）
- **–**

将电场中能量导数的默认计算方法设为有限差分（Yuezhi Mao）
- •

**通用功能与改进：**

- **–**

Q-Chem 与外部工具的下一代接口（以 HDF5 格式生成 archive 文件）
- **–**

实现核-电子耦合簇 CCSD（NEO-CCSD）方法（Fabijan Pavosevic, Sharon Hammes-Schiffer）
- **–**

实现 NEO-TDDFT 解析梯度与 Hessian（Zhen (Coraline) Tao, Patrick E. Schneider, Sharon Hammes-Schiffer）
- **–**

在 NMR $J$-耦合计算（JOBTYPE = ISSC）中支持原子子集选择，
通过 *$spin-spin* 输入区块实现
- **–**

在含固定原子的几何优化中禁用最速下降法
- **–**

在新优化器中添加离域自然内坐标（delocalized natural internal coordinate）优化
- **–**

在有限差分优化的每一步中更新 **MolDen** 文件的几何结构（John Herbert）
- **–**

稳定 JK 和 MP2 的密度拟合（density fitting）
- **–**

将新优化器设为无约束优化的默认选项（GEOM_OPT_DRIVER = LIBOPT3）
- **–**

添加 Karlsruhe 基组的最小增强版（minimal-augmented）与重原子增强版（heavy-augmented）（John Herbert）
- **–**

移除 MPI 支持
- **–**

解决以下问题：

- *

基于分子输入顺序导致 Hirshfeld 电荷不正确的问题（Abdulrahman Aldossary）
- *

SOC 计算中出现非数字（NAN）错误的问题
- *

Fock 投影（BASIS2）计算中缺少核排斥能的问题
- *

移除随机搜索和盆地跳跃（basin hopping）可包含原子数（MAX_ATOM）的限制
- *

格式化检查点文件中局域化 MO 排序问题（Abdulrahman Aldossary）
- *

def2-SVPD 基组缺少有效核势（ECP）的问题
- *

使用线性相关基组时无法计算 NMR 性质的问题
- *

解析超过 10 万行输入文件的问题
- *

C3 点群的特征标表问题
- •

**密度泛函理论（DFT）与自洽场（SCF）：**

- **–**

加速 SCF 算法 ADIIS 的收敛，并添加新的组合算法选项 ADIIS_DIIS（Yuezhi Mao）
- **–**

在使用 GEN_SCFMAN 的 SCF 计算中启用规范无关原子轨道（GIAOs）（Brad Ganoe, Tim Neudecker, Joonho Lee, Adam Rettig, Jonathan Wong）
- **–**

若使用内置的 range 分离泛函（range-separated functionals），禁止用户设置系数（通过 HFK_LR_COEF 和 HFK_SR_COEF）
- **–**

实现 VV10 泛函的频率计算与解析 Hessian（Jiashu Liang）
- **–**

在 CIS/TDDFT 计算中（含冻结占据/虚轨道），通过 GUI = 2 支持生成格式化检查点文件（Yuezhi Mao）
- **–**

在新的绘图区块（PLOT = 1）中启用 STATE_ANALYSIS（Yuezhi Mao）
- **–**

基于 SCF 收敛阈值而非场振幅对 TDKS Fock 矩阵执行一致性检查（John Herbert）
- **–**

添加新的能量密度泛函：revSCAN、regSCAN、r++SCAN、r2SCAN、r4SCAN、TASK、mTASK、regTM、rregTM、revTM
- **–**

支持在 TDDFT（限制式与非限制式）以及自旋翻转 TDDFT（SF-TDDFT）中计算自旋-轨道耦合（SOC）（单电子与双电子平均场）（Saikiran Kotaru, Ana Krylov）
- **–**

为实现自相互作用校正（self-interaction correction）的密度校正 DFT（DC-DFT）解析梯度（Marc Coons, Bhaskar Rana, John Herbert）
- **–**

解决以下问题：

- *

使用 GEN_SCFMAN 的分数电子 SCF 计算结果不正确的问题（Yuezhi Mao）
- *

大量 OpenMP 线程下 qints（USE_LIBQINTS = TRUE）任务挂起的问题
- *

ADIIS 非变分初始 SCF 猜测问题（Yuezhi Mao）
- *

TDDFT/TDA 计算中内存估计不正确的问题
- *

TDA 激发态频率计算任务崩溃问题
- *

含固定原子的几何优化崩溃问题
- *

使用 g 或更高角动量基函数的频率计算问题
- *

TDDFT 自旋-轨道耦合计算中的符号错误（Nicole Bellonzi）
- *

基于投影的嵌入计算崩溃问题（Yuezhi Mao）
- *

使用非 Pople 基组时 RPA TDDFT 频率结果不正确的问题
- *

使用 meta-GGA 泛函进行 NMR 计算时内存分配不足的问题
- *

使用大基组的杂化泛函进行 DC-DFT 计算时结果错误的问题（Marc Coons, Bhaskar Rana, John Herbert）
- *

CIS/TDDFT 激发态势能面扫描崩溃问题（John Herbert）
- •

**相关方法：**

- **–**

实现速度规范与混合规范下的 EOM 振子强度（Josefine Andersen, Sonia Coriani）
- **–**

实现 CCSD 光学旋光（optical rotation）计算（Josefine Andersen, Kaushik Nanda）
- **–**

在 RASMAN2 中实现片段电荷差（fragment charge difference, FCD）方案（Chou-Hsun (Jeff) Yang, Aaditya Manjanath, Chao-Ping (Cherri) Hsu）
- **–**

实现复数值的 CC2、RI-CC2 和 RI-CCSD（Cansu Utku, Garrette Paran, Thomas Jagau）
- **–**

在 AIMD 计算中实现复吸收势（complex absorption potential, CAP）方法（Jerryman A. Gyamfi, Thomas Jagau）
- **–**

实现使用密度拟合基组的 v2RDM-CASSCF-PDFT 方法（Mohammad Mostafanejad, Run Li, A. Eugene DePrince III）
- **–**

修复 RAS-CI 方法 SOC 计算输出中的格式错误（Abel Carreras, David Casanova）
- •

**分子动力学、非绝热动力学、嵌入与溶剂化：**

- **–**

实现基于复基函数的投影嵌入（projection-based embedding）（Valentina Parravicini, Thomas Jagau）
- **–**

支持为泊松方程求解器（PEqS）自定义介电常数网格（Suranjan Paul）
- **–**

改进 PCM 打印输出（John Herbert）
- **–**

实现 CIS 和 TDDFT 波函数重叠（含其自旋翻转变体）用于 (A)FSSH（Theta Chen, Junhan Chen, Zuxin Jin, Vishikh Athavale, Vale Cofer-Shabica, Joe Subotnik）
- **–**

解决 QM/MM 优化未将上一轮 MO 作为下一轮初始猜测读取的问题
- •

**片段与能量分解分析：**

- **–**

在 QM/EFP 计算中实现成对片段激发能分解分析（EDA）（Lyudmila Slipchenko）
- **–**

将 XSAPT 计算中基函数的最大角动量提高到 5
- **–**

实现基于 SPADE 和 ALMO 的电场计算划分方案（Yuezhi Mao）
- **–**

实现新的 MP2 EDA 方案，并为 DFT EDA 添加非微扰极化分析（Kevin Ikeda, Hengyuan Shen）
- **–**

支持激发振幅局域在单一片段上的 ALMO-CIS/TDA 计算（Yuezhi Mao）
- **–**

支持从一个片段的占据轨道激发到体系中所有虚轨道的 ALMO-CIS/TDA 计算（Yuezhi Mao）
- **–**

支持从一个片段的占据轨道激发到另一片段虚轨道的 ALMO-CIS/TDA 计算（Yuezhi Mao）
- **–**

支持在 ALMO-CIS/TDA 计算中自定义占据-虚轨道对（Yuezhi Mao）
- **–**

解决 ALMO-CIS 与激发态 ALMO-EDA 计算中的各种问题（Yuezhi Mao）
- •

**其他：**

- **–**

使用 SCF_PRINT = 3 打印轨道动能
- **–**

支持在外部文件中指定 EXTERNAL_CHARGES（Vale Cofer-Shabica, Joseph Subotnik）
- **–**

为多体色散（many-body dispersion）计算添加参数检查（John Herbert）
- **–**

恢复 $\omega$B97M-2 和 XYG 系列泛函的有限差分方法
- **–**

恢复 SA-SF-RPA 的有限差分提示横幅
