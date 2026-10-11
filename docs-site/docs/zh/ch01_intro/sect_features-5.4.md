---
title: "1.3.8 Q-Chem 5.4 的新特性"
---

## 1.3.8 **Q-Chem** 5.4 的新特性

（2026 年 7 月 4 日）

## 1.3.8.1 5.4.2 版本特性

- •

**默认行为变更：**

- **–**

使 EDA 和 BSSE 计算中超系统（supersystem）与碎片（fragment）作业的默认 SCF 收敛判据保持一致（Yuezhi Mao）
- •

**通用特性与改进：**

- **–**

为 AUTOSAD 初猜（guess）启用混合基组（mixed basis）（Kevin Carter-Fenk、Yuezhi Mao、John Herbert）
- **–**

启用与 NBO7 程序的兼容性（John Herbert）
- **–**

实现本征键轨道（Intrinsic Bond Orbital, IBO）分析（Alexander Zech、Christopher Stein、Abdulrahman Aldossary、Martin Head-Gordon）
- **–**

修复了以下问题：

- *

线程数为原子数三倍时频率（frequency）作业失败的问题
- *

CPSCF 分段数（segments）等于原子数时频率作业失败的问题
- *

使用新版 plots 章节格式时生成的 alpha 密度（alpha density）不正确的问题
- •

**密度泛函理论（Density Functional Theory, DFT）与自洽场（Self-Consistent Field, SCF）：**

- **–**

为 TPPS/TM/SCAN TDDFT 计算启用解析 Hessian（analytic Hessian）
- **–**

新增 TDDFT 内存需求信息的打印输出（John Herbert）
- **–**

新增相对论量子化学 X2C 方法的实验性实现（Diptarka Hait、Leonardo Cunha、Richard Kang、Martin Head-Gordon）
- **–**

改进 CIS/TDA/RPA 初猜，以避免遗漏根（missing roots）
- **–**

实现复基函数（complex basis functions）下的基于投影的嵌入（projection-based embedding）（Valentina Parravicini、Thomas Jagau）
- **–**

通过积分筛分（integral screening）提升 GOSTSHYP 方法的性能（Felix Zeller、Tim Neudecker、Eric Berquist）
- **–**

修复了以下问题：

- *

当较大碎片列在前面时 AIFDEM 崩溃的问题
- *

使用 VV10 泛函时 SCF 能量出现 NAN 的问题
- *

单重激发态（singlet excited state）的非限制 RPA TDDFT 解析 Hessian 问题
- *

使用纯 TDDFT 计算非绝热耦合（non-adiabatic couplings, NACs）失败的问题
- *

使用多线程时 FAST_XAS 给出错误 TDDFT 能量的问题
- *

以 LRC-DFT 作为低层理论时基于投影的嵌入给出错误结果的问题（Yuezhi Mao）
- *

RPA 计算中能量收敛不完全的问题
- *

TDDFT SOC 计算中自旋-轨道积分评估失败的问题
- *

使用 BrianQC 时非限制纯 DFT 梯度的 GPU 加速问题
- *

使用 BrianQC 时 ROHF 梯度不正确的问题
- •

**相关方法（Correlated methods）：**

- **–**

实现 CCSD 阻尼极化率（damped polarizability）与一阶超极化率（first hyperpolarizability）（Kaushik Nanda）
- **–**

修复了以下问题：

- *

EOM-IP-CCSD 错误激活 ECD 性质的问题（Josefine Andersen、Sonia Coriani）
- *

EOM-DIP 与 EOM-DEA 方法中的收敛问题
- *

v2RDM 的对称性检查问题（Rain Li、Eugene DePrince）
- *

无法将 ASCI 能量写入检查点（checkpoint）文件的问题
- •

**分子动力学（Molecular dynamics）：**

- **–**

在路径积分分子动力学（path integral MD）中启用新版 SCF 驱动模块（GEN_SCFMAN = TRUE）
- **–**

修复了以下问题：

- *

GEN_SCFMAN=TRUE 时 AIMD 缺失能量分量文件的问题
- •

**碎片与能量分解分析（Fragment and energy decomposition analysis）：**

- **–**

当 EDA2_MOM 与 EDA_BSSE 一同使用时，对含虚原子（ghost atoms）的 BSSE 计算施加 IMOM，以防止坍缩到较低能量态（Yuezhi Mao）
- **–**

允许 SCFMI_MOM 和 EDA2_MOM 保持冻结态（frozen state）的电子组态（Yuezhi Mao）
- **–**

ALMO-EDA 的多项稳定性改进（Yuezhi Mao）
- **–**

为 ALMO-EDA 实现非微扰的电荷转移（CT）分析（Hengyuan Shen、Srimukh Prasad、Martin Head-Gordon）
- **–**

修复了以下问题：

- *

使用 SMD 溶剂模型时，VFB CT 分析中单侧 CT 能量的最终打印错误地包含了 SMD 的 CDS（非静电）项贡献（Yuezhi Mao）
- *

在基于投影的嵌入中，默认 N_FROZEN_CORE 设置下环境冻结芯轨道（frozen core orbitals）被重复计数的问题（Yuezhi Mao）
- *

ALMO-EDA 制备能（preparation energy）的显示问题（Yuezhi Mao）
- *

多体展开（many-body expansion, MBE）几何优化问题（John Herbert）
- *

正交冻结分解（orthogonal frozen decomposition）线性求解器的收敛问题（Yuezhi Mao）
- *

非 *Aufbau* ALMO-EDA 中经典冻结分解的色散项问题（Yuezhi Mao）
- •

**其他：**

- **–**

禁用基于投影的嵌入的解析力计算（Yuezhi Mao）
- **–**

禁用碎片作业的复 SCF（complex SCF）（Yuezhi Mao）
- **–**

修复 QM/MM 计算中外部电荷设为零时 `efield` 文件打印 NAN 的问题
- **–**

新增警告：CDFT 不支持 DIIS 和 RCA 以外的算法（Yuezhi Mao）
- **–**

当使用 3c 方法却未使用推荐基组时新增警告（John Herbert）
- **–**

在输出中添加 NBO 版本号（John Herbert）
- **–**

修正 TDDFT 输出打印中的少量拼写错误（Bushra Alam、John Herbert）

## 1.3.8.2 5.4.1 版本特性

- •

**默认行为变更：**

- **–**

将 Onsanger 的 SOLVENT_METHOD 重命名为 Kirkwood（John Herbert）
- **–**

更新 SM8 溶剂化模型以使用笛卡尔高斯函数（PURCAR = 2222）（John Herbert）
- **–**

将自旋相关关键字重命名为 EA_ALPHA、EA_BETA、IP_ALPHA 和 IP_BETA（Wojtek Skomorowski）
- •

**通用特性与改进：**

- **–**

新增本征原子轨道（Intrinsic Atomic Orbitals, IAO）与本征键轨道（Intrinsic Bond Orbitals, IBO）（Abdulrahman Aldossary、Alexander Zech、Christopher Stein）
- **–**

新增一种定域化方法——氧化态定域轨道（Oxidation State Localized Orbitals, OSLO）（Abdulrahman Aldossary、Alexander Zech、Christopher Stein）
- **–**

安装中包含 Romberg 工具集
- •

**密度泛函理论（DFT）与自洽场（SCF）：**

- **–**

为 TAO-DFT 实现杂化泛函（Jeng-Da Chai）
- **–**

在共享内存与多线程并行运行时，提升范围分离 DFT（range-separated DFT）频率计算的效率
- **–**

新增选项，可关闭 TDDFT 的基态 PCM 计算（John Herbert）
- **–**

新增选项，可在态定向能量投影（state-targeted energy projection, STEP）的每个 SCF 循环中强制施加能级平移（level shifting）（Kevin Carter-Fenk）
- **–**

为非限制计算实现基于投影的嵌入（Yuezhi Mao）
- **–**

TDDFT 跃迁强度（transition strength）打印更多位数
- **–**

改进使用 BASIS2 的优化作业的 SCF 初猜
- **–**

修复了以下问题：

- *

使用 libqints 时 CIS 频率计算出现段错误（segmentation fault）的问题
- *

手册中 TDKS 示例出现索引越界错误（Hung-Yi Tsai、Jeng-Da Chai）
- *

非限制 TDDFT Hessian 计算中的错误
- *

RPA 激发能中的小误差
- *

基于 libqints 的 SRC-DFT 给出错误 SCF 能量的问题
- *

BASIS = GEN 时计算数值导数导致崩溃的问题
- *

大型频率作业因 CPSCF 内存不足而崩溃的问题
- *

迭代 Hirshfeld 电荷（iterative Hirshfeld charges）评估错误的问题（Abdulrahman Aldossary）
- •

**相关方法：**

- **–**

为复基函数计算新增自定义缩放（custom scaling）选项（Florian Matz、Thomas Jagau）
- **–**

改进投影 CAP-EOM-CC（James Gayvert）
- **–**

实现 EOM-DEA-CCSD 双光子吸收（two-photon absorption）（Kaushik Nanda、Sahil Gulania、Anna Krylov）
- **–**

实现复值 CC2 与 RI-CCSD（Cansu Utku、Garrette Pauley Paran、Thomas Jagau）
- **–**

实现使用 EOM 计算 SOC 的有效核电荷近似（effective nuclear charge approximation）（Saikiran Kotaru、Anna Krylov）
- **–**

修复了以下问题：

- *

冻结弦方法（freezing string method, FSM）读取的是 SCF 能量而非相关能量的问题
- *

ccman2 中 EOM 计算缺失三重激发修正（triples corrections）的问题（Pavel Pokhilko）
- *

在基于投影子的嵌入计算中使用冻结芯轨道与虚轨道的问题（Yuezhi Mao）
- •

**大体系、QM/MM 与溶剂化：**

- **–**

为泊松方程求解器（PEqS）实现用户定义的介电常数网格（permittivity grid）（Suranjan Kumar Paul）
- **–**

为基于 GEN_SCFMAN 的 ROHF/ROKS 计算启用 SCRF（Yuezhi Mao）
- **–**

基于约束平衡理论（constrained equilibrium theory）实现态特定 PCM/TDDFT（SS-PCM/TDDFT）方法（Haisheng Ren、Fan Wang、Xiangyuan Li、Yingli Su）
- **–**

改进 GROMACS QM/MM 接口（Vale Cofer-Shabica）
- **–**

提升 SM8 溶剂化模型的梯度计算性能（John Herbert）
- **–**

优化 SM8 溶剂化模型的内存使用（John Herbert）
- **–**

新增 TDDFT_LR_PCM 关键字以控制线性响应溶剂修正（linear-response solvent correction）（John Herbert）
- •

**碎片与能量分解分析：**

- **–**

在基于投影的嵌入中启用线性化近似（linearized approximation）（Yuezhi Mao）
- **–**

为投影算符非绝热化（projection operator diabatization, POD）实现 POD2L 与 POD2GS（Yuezhi Mao）
- **–**

为 POD 启用多对非绝热轨道（diabatic orbitals）之间耦合的计算（Yuezhi Mao）
- **–**

在 SAPT 输出中新增各分离能量分量的打印（John Herbert）

## 1.3.8.3 5.4.0 版本特性

- •

**默认行为变更：**

- **–**

对自定义基组使用自动生成的原子密度叠加（superposition of atomic densities）SCF 初猜（Yuezhi Mao、Kevin Carter-Fenk）
- **–**

为 CDFT 使用原子尺寸修正的 Becke 权重（atomic size-corrected Becke weights）（Kevin Carter-Fenk）
- •

**通用特性与改进：**

- **–**

新增利用力与压强使分子畸变的新方法：HCFF、X-HCFF、GOSTSHYP（Tim Stauch、Maximilian Scheurer）
- **–**

全面修订标准基组库，与 Basis Set Exchange 保持一致，并将支持扩展至 118 号元素
- **–**

提升 ECP 拟合的稳定性并更新已拟合 ECP 的定义（CRENBS、CRENBL、HWMB、LACVP、LANL2DZ、SBKJC）
- **–**

计算原子核处的电场（electric field at nuclei）（Yuezhi Mao）
- **–**

支持刚性固定原子约束（rigid fixed-atom constraints）的频率计算（Saswata Dasgupta）
- **–**

将额外的计算输出文件保存到唯一文件夹中
- **–**

修复了以下问题：

- *

四极场（quupole field）在消除轨道简并时应用不一致的问题
- *

jun-cc-pVDZ 基组的定义问题（John Herbert）
- *

某些作业因 FILE_SET_SYM_REP 读取错误而崩溃的问题
- *

Windows 上 PES 扫描作业的清理问题
- *

冻结 PES 扫描中每个点都进行不必要的梯度计算的问题
- •

**密度泛函理论与自洽场的特性与改进：**

- **–**

面向全局杂化 GGA 的 TAO-DFT（Jeng-Da Chai）
- **–**

振动耦合（vibronic）与共振拉曼光谱（resonance Raman spectroscopy）（Xunkun Huang、Huili Ma、WanZhen Liang）
- **–**

集成 DFT-D4 经验色散模型（Kuan-Yu Liu、Romit Chakraborty）
- **–**

含时 Kohn-Sham 方程直接传播（real-time TDKS）的新实现，支持非限制 SCF 与隐式溶剂化（Ying Zhu、John Herbert）
- **–**

态定向能量投影方法（state-targeted energy projection method）（Kevin Carter-Fenk、John Herbert）
- **–**

冻结密度嵌入（frozen-density embedding）方法的多项改进（Cristina Gonzalez-Espinoza、Alexander Zech、Tomasz A. Wesolowski）
- **–**

更快的 $\omega$GDD 参数调节（tuning）算法（John Herbert）
- **–**

更快的 $\omega$EFF 参数调节算法（Aditi Singh、Subrata Jana 和 Szymon Śmiga）
- **–**

改进长程修正（long range corrected）泛函的 IP/EA omega 调节脚本（John Herbert）
- **–**

支持 DFT 频率计算中的高角动量（high angular momentum）
- **–**

用于 SCF 的原子势叠加（Superposition of Atomic Potentials, SAP）初猜（Yu Zhang、Susi Lehtola）
- **–**

扩展可用于 NMR 化学位移计算的密度泛函（Jiashu Liang、Khadiza Begam、Barry Dunietz、Yihan Shao）
- **–**

VV10 泛函的核梯度与解析二阶泛函导数（Jiashu Liang）
- **–**

提升 DFT-D3 核 Hessian 贡献计算的绩效
- **–**

约束 DFT（constrained DFT）与 SCF 收敛判据保持一致（Kevin Carter-Fenk）
- **–**

通过 BrianQC 接口改进 NVIDIA GPU 计算：

- *

加速范围分离泛函的力与振动频率计算
- *

加速 DFT 振动频率作业中 Fock 导数的计算
- **–**

修复了以下问题：

- *

超大 DFT 作业特殊情况下的缓冲区溢出（buffer overflow）问题
- *

非限制 CIS 导数耦合计算在特殊情况下崩溃的问题
- *

非局域关联轨道 Hessian 的有限差分评估问题（Yuezhi Mao）
- *

通用响应模块（general response module）中原子轨道（AO）积分的使用问题
- *

Linux 与 macOS 之间 DFT 求积（quadrature）差异的问题
- *

在 MBD-vdW 计算中使用虚原子的问题（Kevin Carter-Fenk、Evgeny Epifanovsky）
- *

为 MBD-vdW 与 TS-vdW 使用任意密度泛函的问题
- *

大型 CIS 态跟随（state following）计算崩溃的问题
- *

非限制 TDDFT 的 SOC 常数问题
- *

RI-J/RI-K 梯度问题
- *

DFT 超极化率（hyperpolarizabilities）问题
- •

**相关方法的特性与改进：**

- **–**

使用 CCSD 计算电子 $g$ 张量（electronic $g$-tensors）（Sven Kähler、Anna Krylov）；
- **–**

使用 EOM-CC 计算电子圆二色性（electronic circular dichroism, ECD）（Josefine Andersen、Sonia Coriani）
- **–**

使用 CVS-EOM 方法评估自旋-轨道耦合（spin-orbit couplings），并进行 L 边 XAS/XES 光谱计算（Marta Vidal、Pavel Pokhilko、Sonia Coriani）
- **–**

将 Feshbach 方法与 EOM-CC 态相结合，并用平面波展开的高斯型轨道（plane wave Gaussian type orbitals）表示 Coulomb 波（Wojciech Skomorowski）
- **–**

通过核内计算（in-core computations）提升中小型 CC/EOM 作业的绩效
- **–**

改进投影 CAP EOM-CC（James Gayvert）
- **–**

IP/EA-ADC 方法及中间态表示（intermediate state representation, ISR）性质（Adrian Dempwolff、Matthias Schneider、Alexander Paul）
- **–**

ADC(3) 的大幅加速（Adrian Dempwolff）
- **–**

改进所有 ADC 变体（PP (EE)、IP、EA）的四阶静态自能（fourth-order static self-energy）（Adrian Dempwolff）
- **–**

面向所有 ADC 变体（PP (EE)、IP、EA）的子空间投影 CAP-ADC（subspace-projected CAP-ADC）（Adrian Dempwolff）
- **–**

使用 RAS-CI 与 RAS2-SF 方法评估自旋-轨道耦合（Abel Carreras、Anna Krylov、David Casanova、Hanjie Jiang、Pavel Pokhilko、Paul M. Zimmerman）
- **–**

在基于 LibRASSF 的 RAS-SF 实现中使用分辨率恒等（resolution-of-the-identity）积分（Shannon Houck）
- **–**

在基于 LibRASSF 的 RAS-SF 中实现 Bloch 有效哈密顿量（Bloch effective Hamiltonian）方法（Shannon Houck）
- **–**

CC2 与 RI-CC2 方法的实验性实现（Garrette Paran、Thomas Jagau）
- **–**

实现 Brueckner CC2 方法（Adam Rettig）
- **–**

实现用于基态关联能的直接 RPA（direct RPA）（Joonho Lee）
- **–**

三次方存储（cubic storage）RI-MP3 以及 Laplace 变换的 RI-MP2 与 RI-MP3（Joonho Lee）
- **–**

新增通过 METHOD = KOOMP2 访问 $\kappa$ 正则化的轨道优化 MP2（orbital optimized MP2）
- **–**

v2RDM 与 v2RDM-CASSCF 求解器的新实现（Rain Li、Wayne Mullinax、Eugene DePrince、Marcus Liebenthal）
- **–**

改进增量式 FCI（incremental FCI）的默认设置（Alan Rask）
- **–**

张量超收缩（tensor hypercontraction）方法的实验性实现（Joonho Lee）
- **–**

修复了以下问题：

- *

Windows 上 CC/EOM/ADC 计算临时文件 2 GB 上限的问题
- *

$\kappa$ 正则化 OO-MP2 解析梯度评估的问题
- *

碎片激发差（fragment excitation difference, FED）计算因内存不足而崩溃的问题（Aaditya Manjanath）
- *

大型 RI-MP2 计算崩溃的问题
- *

EOM-DIP-CCSD 计算中的初猜问题
- *

大型 RI-CCSD 计算崩溃的问题
- •

**分子动力学的特性与改进：**

- **–**

新增 AIMD 变量（AIMD_INIT_VELOC_NANO_RANDOM）以获得更好的随机种子（Tarek Scheele）
- **–**

修复了以下问题：

- *

特殊情况下振动光谱计算激活的问题
- •

**大体系、QM/MM 与溶剂化的特性与改进：**

- **–**

AIRBED：一种用于表面物理吸附（physisorption）的简化密度泛函理论模型（Nick Besley、Stephen Mason）
- **–**

修复了以下问题：

- *

SM12 在通用基组下崩溃的问题（Yuezhi Mao）
- *

MM 有限差分力计算问题
- *

EFG 主成分（principal components）的打印问题
- *

SM12 梯度问题
- *

SCF 与 DFT 响应性质计算中的隐式溶剂化问题
- *

IEF-PCM 频率计算要求显式设置导数级别的问题（John Herbert）
- *

RI-MP2 + PCM 作业问题
- *

大型 SMD 作业中的内存溢出（out-of-memory）错误
- •

**碎片与能量分解分析方法的特性与改进：**

- **–**

在存在溶剂的情况下，启用 POL 与 VFB-CT 势能面上的几何优化（Yuezhi Mao）
- **–**

为具有非 *Aufbau* 电子组态的体系启用 ALMO-EDA（Yuezhi Mao）
- **–**

在 SMD 溶剂化能中启用静电项与非静电项的分离（Yuezhi Mao）
- **–**

改进尝试基于 ROHF 的 SCFMI 与 EDA 时的错误信息
- **–**

改进尝试在 SCFMI 与 EDA 中使用不受支持溶剂模型时的错误信息
- **–**

在 SAPT CPSCF 中控制子空间向量数与收敛阈值（Kevin Carter-Fenk）
- **–**

改进 SAPT+aiD$x$ 与 SAPT+MBD 关键字（Kevin Carter-Fenk）
- **–**

修复了以下问题：

- *

大型基于投影的嵌入计算过程中崩溃的问题（Yuezhi Mao）
- *

绝热 EDA 几何与频率计算要求显式设置导数级别的问题（Yuezhi Mao）
- *

SAPT 特性与各种 SAPT 基组之间互操作性的问题（Kevin Carter-Fenk）
- *

使用基于碎片的 Hirshfeld 布居（fragment-based Hirshfeld populations）时 SAPT + cDFT 崩溃的问题（Kevin Carter-Fenk）
- *

XSAPT 中的内存使用问题（Kevin Carter-Fenk、John Herbert）
