---
title: "1.3.6 Q-Chem 6.1 新功能"
---

## 1.3.6 **Q-Chem** 6.1 新功能

(2026 年 7 月 4 日)

## 1.3.6.1 6.1.1 版新功能

- •

**默认行为变更:**

- **–**

在片段 REM 变量部分（*$rem_frgm*）中将 TDKS 设置为 FALSE(John Herbert)
- **–**

移除冗余的 CIS_ 和 SET_ 变量(John Herbert)
- **–**

更新 XDM 阻尼参数并添加供用户控制的变量(John Herbert)
- **–**

SCF 能量的格式化输出(John Herbert)
- •

**通用功能与改进:**

- **–**

新增打印 CHELPG 网格点及权重的功能(John Herbert)
- **–**

为 RI-JK 核（kernel）添加 Fock 矩阵修正(Xintian Feng)
- **–**

提高轨道能量输出的精度,使重元素可以获得 1s 能量(John Herbert)
- •

**密度泛函理论（Density Functional Theory, DFT）与自洽场（SCF）:**

- **–**

在可用方法列表中添加 XYG3、XYGJ-OS(Yuezhi Mao)
- **–**

在 CDFT 中禁用双杂化（double-hybrid）方法及后 HF 方法(Yuezhi Mao)
- **–**

改进 TRNSS LR-TDDFT 代码在处理核心层激发（core-level excitations）时的错误捕获(John Herbert)
- **–**

ROKS 计算中的最大重叠方法（Maximum Overlap Method）(Kevin Carter-Fenk, Martin Head-Gordon)
- **–**

修复了以下问题:

- *

XDM 用户界面中 NATOMS_MOL1 取值不明确的问题(John Herbert)
- *

XDM10 中 $\kappa$ 值的打印问题(John Herbert)
- •

**相关方法:**

- **–**

添加超精细耦合代码,用于计算单重态/三重态激发 CIS 态之间的耦合(Samuel May, Joseph Subotnik)
- **–**

改进 ccman2 中 Davidson 求解器的 MOM 功能(Florian Matz, Quyen Nguyen, Thomas-C. Jagau)
- **–**

支持 TDDFT/TDA-SOC 重叠及外磁场(Yanze Wu, Joseph Subotnik)
- **–**

加速 TDDFT/TDA-SOC 导数耦合（derivative coupling）计算,尤其是时间反演情形(Yanze Wu, Joseph Subotnik)
- **–**

为 CIS/TDDFT 重叠添加三重态支持(Yanze Wu, Joseph Subotnik)
- **–**

为 CAS-SCF 计算输出中的自然轨道占据数（NOON）添加正确的表头标签(John Herbert)
- **–**

针对基态与激发态能量计算,实现了随机化恒等分辨近似（stochastic resolution of identity approximation）的 CC2 模型(sRI-CC2)(Chongxiao Zhao, Wenjie Dou, and Joonho Lee)
- **–**

修复了以下问题:

- *

SOC 输出标签中的拼写错误("ms=1" 改为 "ms=-1")(Yanze Wu, Joseph Subotnik)
- *

RAS-FCD 与 RAS-FED 中的受体-给体顺序依赖问题(Aaditya Manjanath, Chao-Ping Hsu)
- •

**分子动力学、非绝热动力学、嵌入理论与溶剂化:**

- **–**

启用 SM$x$ 调试打印(John Herbert)
- **–**

改进对不正确 PCM 输入的错误捕获(John Herbert)
- **–**

修复了以下问题:

- *

SF-TDDFT 计算中 PCM 内 **Td_CEq_NonEq** 的错误处理(John Herbert)
- *

PCM 中的打印错误(Kuan-Yu Liu)
- •

**片段与能量分解分析:**

- **–**

将非微扰 PolA/CTA 中的片段索引约定改为从 1 开始(Yuezhi Mao)
- •

**杂项:**

- **–**

对 ROKS 任务禁用解析核 Hessian(Yuezhi Mao)
- **–**

对使用截断子空间的 TDDFT 进行格式化输出(John Herbert)
- **–**

在非微扰 PolA/CTA 中将术语 "Energy Transfer"（能量转移）替换为 "Polarization Energy"（极化能）(Yuezhi Mao)
- **–**

在非微扰 PolA/CTA 中将术语 "Charge Transfer"（电荷转移）替换为 "On-Fragment Charge Shift"（片段内电荷偏移）(Yuezhi Mao)
- **–**

针对核心层激发的 TDDFT 格式化输出(John Herbert)

## 1.3.6.2 6.1.0 版新功能

- •

**默认行为变更:**

- **–**

将 SASF_RPA 重命名为 SASF_CIS
- **–**

将 TDDFT_PCM 重命名为 TDDFT_LR_PCM(John Herbert)
- **–**

将 SYMMETRY 重命名为 INTEGRAL_SYMMETRY,并令 INTEGRAL_SYMMETRY 默认值为 FALSE
- **–**

添加 POINT_GROUP_SYMMETRY
- **–**

添加 ENABLE_ARCHIVE 关键字以控制归档文件（archive files）的写入(Eric Berquist, Peter McLaughlin)
- •

**通用功能与改进:**

- **–**

为 SCF 计算实现规范无关原子轨道（gauge-independent atomic orbital, GIAO）基组(Jonathan Wong, Brad Ganoe, Tim Neudecker, Adam Rettig, Xiao Liu, Joonho Lee)
- **–**

为 DFT 任务实现 GIAO 复数计算(Jiashu Liang)
- **–**

使用受限 CIS 及 TDDFT/TDA 实现在线（on-the-fly）SQC 与 Ehrenfest 非绝热动力学算法(Justin Talbot, Stephen J. Cotton, Martin Head-Gordon)
- **–**

实现 Slater 跃迁方法与跃迁势方法,用于计算核心层结合能及 X 射线吸收谱(Subrata Jana, John Herbert)
- **–**

生成振动分解分析（vibronic decomposition analysis）数据(Kuan-Yu Liu, Peter McLaughlin, Andrew Gilbert)
- **–**

在 **Libopt3** 中启用态跟踪（state following）。
- **–**

将过渡态几何优化的默认设置更改为新优化器(Peter McLaughlin)
- **–**

为几何优化实现新的初始模型 Hessian(Peter McLaughlin)
- **–**

为 ESP cube 图启用新的 plots 部分格式(Yuezhi Mao)
- **–**

添加振动圆二色（vibrational circular dichroism, VCD）光谱(Yu Zhang, Kuan-Yu Liu, Eric Berquist, Evgeny Epifanovsky)
- **–**

添加 RRHO 输出(Abdul Aldossary, Alistair Sterling, Tim Schramm)
- **–**

添加在位移几何构型下计算分子轨道（MO）重叠的功能(John Herbert)
- **–**

解决了以下问题:

- *

B97M-V 梯度的性能
- *

NEO-epc19 中氘质量传递错误的问题(Zhen (Coraline) Tao, Mathew Chow, Sharon Hammes-Schiffer)
- *

NEO-epc19 梯度问题(Zhen (Coraline) Tao, Mathew Chow, Sharon Hammes-Schiffer)
- *

NEO-epc172 Hessian 及多质子 NEO Hessian 问题(Zhen (Coraline) Tao, Mathew Chow, Sharon Hammes-Schiffer)
- *

RHF 任务中缺失 STEP 约束的问题(Kevin Carter-Fenk)
- *

高斯模糊（Gaussian blur）与 ECP 配合使用失效的问题(John Herbert)
- *

四阶以上多体展开（many-body expansion）任务失败的问题
- •

**密度泛函理论（DFT）与自洽场（SCF）:**

- **–**

为 TDDFT 与 SF-TDDFT 启用自旋-轨道自然轨道（NTO）分析(Saikiran Kotaru)
- **–**

实现电子亲和能含时密度泛函理论（electron-affinity time-dependent density functional theory）(Kevin Carter-Fenk, Juan Arias-Martinez, Leonardo Cunha)
- **–**

在包含 ECP 的情况下启用基于投影的嵌入方法（projection-based embedding）(Valentina Parravicini, Thomas Jagau)
- **–**

在 DFT 任务的 SCF 之前添加内存检查
- **–**

改进 EA-TDDFT/STEX 任务控制(Kevin Carter-Fenk)
- **–**

在 EA-TDDFT/STEX 任务中添加 SPADE 定域化功能与初始猜测功能(Kevin Carter-Fenk)
- **–**

解决了以下问题:

- *

TDA 激发态频率计算崩溃
- *

VV10 计算中的重复计数（double counting）
- *

meta-GGA TDDFT 解析频率
- •

**相关方法:**

- **–**

新增对核心空穴态（core-vacant states）的 CCSD 计算获取部分宽度（partial widths）的功能(Florian Matz, Thomas Jagau)
- **–**

实现 RI-CC2-EOM-SF、EA 与 IP(Garrette Paran, Thomas Jagau, Cansu Utku)
- **–**

实现 CCSDT(Prashant Uday Manohar, Manisha)
- **–**

在 ADC 任务的激发态分析中启用新的 plots 部分格式(Yuezhi Mao)
- **–**

修正圆偏振光下 EOM-CC 双光子吸收（2PA）截面的系数(Kaushik Nanda)
- **–**

为阻尼 CC 方程添加 **Dalton** 求解器以加快收敛(Kaushik Nanda)
- **–**

允许在 fc-CVS-EOM-CC 计算中用户自定义活性与惰性冻芯轨道(Kaushik Nanda)
- **–**

解决了以下问题:

- *

使用 GEN_SCFMAN 时 iFCI 失败的问题
- *

当同时请求 CVS-EOM-EE-CCSD 与 CVS-EOM-IP-CCSD 态时,从初始 CCSD 态计算 CC 跃迁性质失败的问题(Kaushik Nanda)
- •

**分子动力学、非绝热动力学、嵌入理论与溶剂化:**

- **–**

为核-电子轨道（nuclear-electronic orbital, NEO）方法实现 PCM 贡献(NEO)(Mathew Chow, Sharon Hammes-Schiffer)
- **–**

禁用 $N=14$ 的 PCM 离散化网格(John Herbert)
- **–**

新的、改进的态特异（state-specific, SS）PCM-TDDFT(Thomas Froitzheim, John Herbert, Jan-Michael Mewes, Stefan Grimme)
- **–**

对不正确的 PEqS 输入格式打印更清晰的错误信息(John Herbert)
- **–**

解决了以下问题:

- *

结合 IEF-PCM 静电作用时的 SMD 梯度(John Herbert)
- *

NEO 计算中 SS(V)PE 与 IEF-PCM 梯度问题(Mathew Chow, Sharon Hammes-Schiffer)
- *

DACF 计算时 AIMD 崩溃的问题(J. A. Gyamfi, Thomas C. Jagau)
- *

隐式溶剂下当 IDERIV = 0 时冻结能梯度计算失败的问题(Yuezhi Mao)
- •

**片段与能量分解分析:**

- **–**

使用迭代 Hirshfeld 方案实现分子极化率的分解(Yihan Shao, Yuezhi Mao)
- **–**

实现力的分解分析（force decomposition analysis）(Abdulrahman Aldossary, Yuezhi Mao, Marti Gimferrer)
- **–**

为 EDA2 添加 POL 与 NOCV 分析(Hengyuan Shen)
- **–**

在 ALMO-EDA2 中启用非微扰 PolA/CTA 的计算(Hengyuan Shen, Yuezhi Mao)
- **–**

为 XSAPT 添加前处理与后处理脚本(Montgomery Gray, John Herbert)
- **–**

解决了以下问题:

- *

FSSH 任务中与 schema 相关的崩溃(Yuezhi Mao, Justin Talbot)
- *

MO SAPT 计算中 $E^{(1)}_{\text{elst}}$ 与 $E^{(1)}_{\text{exch}}$ 的错误(Montgomery Gary, John Herbert)
- •

**杂项:**

- **–**

在 MECP 中禁用 SMD(John Herbert)
- **–**

新增在 PCM 中通过溶剂名称定义溶剂介电常数的功能(John Herbert)
- **–**

当 GEN_SCFMAN = FALSE 且功能不受支持时,为 BrianQC 任务添加警告
- **–**

移除关于在高斯模糊中使用 ECP 的过时警告(John Herbert)
- **–**

在所有输入部分启用注释功能(John Herbert)
- **–**

修复使用 ROHF 轨道时 X2C 的内存泄漏(Kevin Carter-Fenk)
- **–**

允许输入解析器将 1 解释为 TRUE(Eric Berquist)
