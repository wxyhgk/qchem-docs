---
title: "1.3.2 Q-Chem 7.0 新增功能"
---

## 1.3.2 **Q-Chem** 7.0 新增功能

(2026 年 7 月 4 日)

## 1.3.2.1 7.0.0 版本功能

- •

**默认设置与关键字变更：**

- **–**

更新了多参考自旋翻转含时密度泛函理论（MRSF-TDDFT）的关键字，以与自旋翻转含时密度泛函理论（SF-TDDFT）保持一致 (Arnab Chakraborty, Anna I. Krylov)

- *

移除了 MR_SPIN_FLIP 和 MRSF_DUMP
- *

现在使用 SPIN_FLIP = 2 来运行 MRSF-TDDFT 能量计算
- *

STS_MOM = TRUE 可启用态-态跃迁矩（state-to-state transition moment）计算
- **–**

将耦合簇（CC）作业默认改为使用阿贝尔子群（USE_ABELIAN_SUBGROUP = TRUE）(Tingting Zhao, Anna Krylov)
- **–**

将两步 Cholesky 分解设为 CC 作业的默认方式 (Tingting Zhao, Anna Krylov)
- **–**

将 CD_TS_SPAN_FACTOR 的默认值设为 $10^{-2}$ (Tingting Zhao, Anna Krylov)
- **–**

为清晰起见，将 OPSING 关键字更名为 SPIN_PROJ (John Herbert)
- **–**

更新了自然轨道/核轨道（NEO）计算中质子/电子质量比，采用 NIST CODATA 最新实验值（1836.152673426，而非 1836.15267389）(Jack Morgenstein, Sharon Hammes-Schiffer)
- **–**

在几何优化器中，将冗余内坐标的默认初始 Hessian 矩阵设为 SIMPLE (Kuan-Yu Liu)
- **–**

对于 SCF_CONVERGENCE>=8 的计算，将 MAX_SCF_CYCLES 的默认值改为 100 (Kaushik Nanda)
- **–**

将稳健自洽场（robust SCF）流程中 MAX_SCF_CYCLES 的默认值改为 100 (Kaushik Nanda)
- **–**

SF-1eX2C 的默认设置已从有限差分能量切换为解析能量 (Xiao Liu, Sahand Adibnia, Martin Head-Gordon)
- •

**通用功能与改进：**

- **–**

非限制态振动圆二色性（Unrestricted VCD）(Kaushik Nanda)
- **–**

MPI 改进 (Kaushik Nanda)
- **–**

wGDD：打印警告提示，说明在后续 TDDFT 作业中 omega 不会被重置 (John Herbert)
- **–**

在几何优化器中新增改进的 SIMPLE 初始 Hessian 矩阵 (Kuan-Yu Liu)
- **–**

UHF/RHF/ROHF 的 JK、J、K、RS_K、XC 对 Fock 矩阵构建的贡献（支持 DIIS、GDM 和 ROBUST 算法）现已启用 libhpc (Kaushik Nanda)
- •

**密度泛函理论（Density Functional Theory, DFT）与自洽场（SCF）：**

- **–**

扩展紧束缚 DFT（extended tight binding DFT, xtb）能量与梯度 (Rebecca Tomann, Siyavash Moradi, Lucas de Kam, Christopher Stein, Martin Head-Gordon)
- **–**

新增选项，允许用户为双杂化 DFT 泛函选择 PT2 引擎（MP2、RIMP2 或 LMP2）；LMP2 为双杂化 DFT 泛函提供与 DLPNO 相当甚至更优的标度 (Yao Shen, Martin Head-Gordon)
- **–**

针对 Hartree-Fock、 range-separated 泛函和全局杂化泛函的半数值 K（Hartree-Fock 交换）(Jesse David DiCenso, Henryk Laqua, Martin Head-Gordon)
- **–**

TDDFT 的电子圆二色性（Electronic Circular Dichroism, ECD）计算 (Xunkun Huang, Wan-Zhen Liang)
- **–**

以下 DFT 泛函现已可用：

- *

COACH (Jiashu Liang, Martin Head-Gordon)
- *

CF22D (Jiashu Liang, Martin Head-Gordon)
- *

wB97M(OS) (Yao Shen, Martin Head-Gordon)
- *

XYG-OS5 (Yao Shen, Martin Head-Gordon)
- **–**

采用复吸收势（complex absorbing potentials）的密度泛函理论，适用于局域密度近似（LDA）、广义梯度近似（GGA）及其衍生杂化泛函。(Charlotte Titeca, Yifan Jiang, Thomas-C. Jagau)
- **–**

以下复变量（complex-variable）泛函现已可用 (Charlotte Titeca, Yifan Jiang, Thomas-C. Jagau)

- *

LDA：Slater X、VWN5 C、VWN1RPA C
- *

GGA：B88 X、PBE X、PBE C、LYP C
- *

杂化：由上述 LDA 和 GGA 组合、并可加入精确 HF 交换的所有杂化泛函，其中包括（但不限于）PBE0、B3LYP 和 BH&HLYP。
- **–**

密度拟合（RI）改进：

- *

J 梯度与 Hessian 的多项性能改进 (Xintian Feng)
- *

通过基于分子轨道（MO）的算法提升 Fock XC 性能 (Xintian Feng)
- *

JK 梯度性能改进 (Xintian Feng)
- **–**

全新的 SCF 级别核磁共振（NMR）屏蔽各向异性计算功能，支持 RI 加速及 MPI+OpenMP 并行化 (Xiao Liu, Kaushik Nanda, Martin Head-Gordon)
- **–**

无自旋（spin-free）SF-1eX2C 解析实现，用于 SCF 级别的单点能计算 (Xiao Liu, Sahand Adibnia, Martin Head-Gordon)
- **–**

CAP/CBF RI-EA-CC2 实现 (Cansu Utku, Garrette Paran, Thomas Jagau)
- **–**

实现新的 Faddeeva 有限脉冲近似（FFPA）方法，用于光电离截面计算 (Jason Yi, Martin Head-Gordon, C. William McCurdy)
- **–**

用于占据数受限（OO-DFT）计算的新的 FRZ MO 初始猜测 (Nicola Bogo, Christopher J. Stein, Zeyi Zhang, Martin Head-Gordon)
- **–**

BWs-ADC 的实现 (Linus Dittmer, Adrian Dempwolff, Adrian Muller, Jonas Leitner, Andreas Dreuw)
- **–**

在 TAO-DFT 框架内用于激发能的 pTAO 方法 (Shaozhi Li, Jeng-Da Chai)
- **–**

range-separated 杂化泛函的 omega 有效调谐（effective tuning）(Aditi Singh, Subrata Jana, Szymon Smiga, Prasanjit Samal)
- **–**

打印多个 TDDFT 态的梯度 (Pavel Pokhilko)
- **–**

实现轨道与密度的二阶矩（second moments）(John Herbert)
- **–**

新版 DeltaSCF 驱动中改进了 HOMO-LUMO 交换检查 (Juanes Arias-Martinez)
- **–**

为 DeltaSCF 驱动添加双重态（阳离子）计算 (Juanes Arias-Martinez)
- **–**

支持在 DeltaSCF 驱动中使用不同的初始猜测 (Juanes Arias-Martinez)
- **–**

改进新版 DeltaSCF 驱动的打印输出 (Juanes Arias-Martinez)
- **–**

**已解决以下问题：**

- *

DeltaSCF 计算中的线性依赖问题 (Juanes Arias-Martinez)
- *

range-separated DFT 频率计算中与内存相关的缺陷 (Xintian Feng)
- *

基于 DFT 的 ROSCF 计算变慢的问题 (Xintian Feng)
- *

非限制 range-separated DFT 稳定性分析的性能缺陷 (Xintian Feng)
- *

请求使用 MBD 的频率计算未能执行 MBD 部分；现已通过有限差分正确纳入 MBD (John Herbert)
- *

新版 DeltaSCF 驱动中非限制混合态的 TDDFT NTO 初始猜测问题 (Juanes Arias-Martinez)
- *

新版 DeltaSCF 驱动中三重态 SOMO 的打印问题 (Juanes Arias-Martinez)
- *

当可用内存非常有限时，基于 libfock 的 JK 例程出现与内存相关的崩溃 (Xintian Feng)
- *

RI 与溶剂化模型不兼容的问题 (Xintian Feng)
- *

使用鬼原子（ghost atoms）时 DFT-D4 能量结果错误的问题 (Kuan-Yu Liu)
- *

激发态密度矩打印中的缺陷 (John Herbert)
- *

使用宽松阈值计算壳层半径时作业挂起的问题 (Xintian Feng)
- •

**相关方法：**

- **–**

基于数值稀疏性的局域 MP2 (Zhenling Wang)
- **–**

libgmbpt 中 RI-CC2 基态代码大幅提速 (Hrishikesh Ram and Martin Head-Gordon)
- **–**

RI-CC2 与 sRI-CC2 振子强度 (Chongxiao Zhao, Ruihao Bi, Qi Ou, Joohno Lee, Chenyang Li, Wenjie Dou)
- **–**

THC-sRI-CC2 性质 (Chongxiao Zhao, Ruihao Bi, Qi Ou, Joohno Lee, Chenyang Li, Wenjie Dou)
- **–**

THC-sRI-CCSD 基态与激发态能量 (Chongxiao Zhao, Ruihao Bi, Qi Ou, Joohno Lee, Chenyang Li, Wenjie Dou)
- **–**

为 MRSF-TDDFT 新增激发态分析功能，包括自然轨道（NOs）、自然跃迁轨道（NTOs）、自然差轨道（NDOs）及相关描述符，通过 libwfa 框架实现 (Arnab Chakraborty, Anna I. Krylov)
- **–**

新增基于推土机距离（Earth Mover's Distance）的激发态分析功能：一种精确但开销更大的传输单纯形（transportation-simplex）方法，以及一种更快但近似的水距离（Sinkhorn-distance）方法 (Zhe Wang, Martin Head-Gordon)
- **–**

MRSF-TDDFT 现支持用于可视化的检查点文件输出（GUI = 2）及 MOLDEN 文件生成 (Arnab Chakraborty, Anna I. Krylov)
- **–**

使用 EOM-CCSD 波函数计算 K 壳层俄歇（Auger）宽度的单中心近似（One-Center Approximation）方法 (Wojtek Skomorowski, Sonia Coriani)
- **–**

优化 lambda 方程，提升 RI-CCSD 及 RI-EOM-EE/EA/IP-CCSD 的性能 (Tingting Zhao, Anna Krylov)
- **–**

libwfa 中的电荷位移（charge-displacement）度量指标 (John Herbert)
- **–**

CC2 与 RI-CC2 的电子亲和能（EA）、电离能（IP）、EE-EA 和 EE-IP Dyson 轨道 (3755, Mauro Gascon, Robin Moorby, Simen Camps, Tianyi Gao, Thomas Jagau)
- **–**

MRSF-TDDFT 的自旋-轨道耦合（SOC）实现 (Arnab Chakraborty, Anna I. Krylov)
- **–**

EOMEE/SF-CC2 的偶极矩与跃迁偶极矩 (Simen Camps, Tianyi Gao, Mauro Gascón Navas, Thomas Jagau)
- **–**

**已解决以下问题：**

- *

使用旧版 SCF 驱动时 CAS 计算跳过了 CAS (John Herbert)
- *

NOCIS/STEX 中非正交矩阵元计算的错误 (Rachel Patterson, Martin Head-Gordon)
- *

使用冻结芯（frozen core）时 Cholesky 分解出错 (Tingting Zhao, Anna Krylov)
- *

CCMAN2 中单精度 RI-CC2 计算作业失败的问题 (Simen Camps, Thomas Jagau)
- •

**量子核效应纳入（NEO 套件）：**

- **–**

为 NEO-SCF 的单点能（SPE）计算添加电子密度拟合（RI-JK）(Rowan Goudy, Sharon Hammes-Schiffer)
- **–**

添加 NEO-AIMD 方法，适用于 NEO-HF 和 NEO-DFT，包括 NEO Born-Oppenheimer 分子动力学（NEO-BOMD）与约束 NEO 分子动力学（CNEO-MD）(Joseph Dickinson, Sharon Hammes-Schiffer)
- **–**

通过更新 NEO-TDDFT 的初始猜测，改进了 v_pp 关闭时 RPA 的收敛性 (Rowan Goudy, Scott M. Garner, Sharon Hammes-Schiffer)
- **–**

**已解决以下问题：**

- *

NEO-MRCI/NEO-CASSCF 忽略了输入文件中设置的 NEO_ISOTOPE，导致含氘和氚体系的结果错误 (Jack Morgenstein, Sharon Hammes-Schiffer)
- *

使用 NEO_ISOTOPE 定义的含氘和氚体系结果错误 (Jack Morgenstein, Sharon Hammes-Schiffer)
- *

当 NEO 基组中使用角动量大于等于 2 的球函数时，部分 NEO 计算出现段错误（segmentation fault）(Rowan Goudy, Eno Paenurk, Sharon Hammes-Schiffer)
- *

当核基组存在线性依赖时，使用核 Hartree 乘积表示的 NEO Hessian 计算结果错误 (Eno Paenurk, Sharon Hammes-Schiffer)
- *

在低内存条件下运行时，某些情况下 NEO-SCF 结果错误 (Rowan Goudy, Jack Morgenstein, Sharon Hammes-Schiffer)
- •

**分子动力学、非绝热动力学、嵌入与溶剂化改进：**

- **–**

实现成对简谐约束器（pairwise harmonic confiner），用于内坐标下的优化 (Chance Brandt, John Herbert)
- **–**

在基于投影的嵌入（projection-based embedding）中，新增在超系统 SCF 之后更改非交换相关泛函的能力 (Elena Kolodzeiski, Christopher Stein)
- **–**

通用的、基于文件的外部嵌入接口，可与 CP2K 等外部软件包对接 (Arnelle Fonlon, Kay Carter-Fenk, Dustin R. Broderick, Elena Kolodzeiski, John M. Herbert, Christopher J. Mundy)
- **–**

QM/EFP 作业中单电子积分的显著加速与并行化，使大型作业的总体提速达一个数量级 (Lyudmila Slipchenko)
- **–**

改进 QM/EFP 的打印输出，为调试收敛问题提供关键信息 (Lyudmila Slipchenko)
- **–**

改进 QM/MM 功能，包括用于 QM/MM 几何优化的有效约束 (Lyudmila Slipchenko)
- **–**

解决简谐约束作业在 IQmol 中无法正确打开的问题 (Yuezhi Mao)
- •

**片段与能量分解分析：**

- **–**

能量分解分析（EDA）OVOCV 分析及 OODFT OVOCV 分析 (Hengyuan Shen, Martin Head-Gordon)
- **–**

为对称适配扰动理论（SAPT）添加修订后的多体色散（MBD）参数（MBDrev）(Ka Un Lao, Corentin Villot)
- **–**

用于 XSAPT+MBD 的新 MBD 色散模型 (Keegan Paice, John Herbert)
