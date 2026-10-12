---
title: "1.3.9 Q-Chem 5.3 新特性"
---

## 1.3.9 **Q-Chem** 5.3 新特性

（2026 年 7 月 4 日）

- **默认设置的变更：**

- 将 rem 变量 ADIABATIC_CTA 重命名为 VFB_CTA
- 针对限制性开壳层自洽场（ROHF）将 ROHF_DIAG_SPEC 默认值从 0 改为 2，并将 GEN_SCFMAN 设为默认的 ROHF 自洽场（ROSCF）引擎
- **通用改进：**

- 新增对 jun-cc-pVDZ 基组（Basis Set）的支持（Kevin Carter-Fenk）
- **密度泛函理论（Density Functional Theory, DFT）套件的新特性与改进：**

- 针对杂化广义梯度近似（meta-GGA）密度泛函的含时密度泛函理论（TD-DFT）解析力与频率计算
- 在直接迭代子空间最小二乘法（DIIS）中引入能级平移（level shifting），以改善困难情况下的自洽场（SCF）收敛性（第 [4.5](../ch04_scf/sect_convergence.md) 节）
- M06-SX 密度泛函（Pierpaolo Morgante，Roberto Peverati）
- HF-3c 方法（Bhaskar Rana，John Herbert）
- **耦合簇（CC）/运动方程耦合簇（EOM-CC）程序包的新特性与改进：**

- 共振非弹性 X 射线散射（RIXS）的计算以及 RIXS 跃迁矩的轨道分析（Kaushik Nanda，Anna Krylov；第 [7.9.9.1](../ch07_excited/sub_cvs_eom.md#sec:cvs_eom_rixs) 节）
- 核价分离近似运动方程耦合簇（CVS-EOM-CC）套件的新特性（Marta Vidal，Sonia Coriani）
- 偶极方程运动方程耦合簇（EOM-DEA-CCSD）的能量与性质计算（Sahil Gulania，Maxim Ivanov，Anna Krylov；第 [7.9.8](../ch07_excited/sec_eomdea.md) 节）
- 偶极移除方程运动方程耦合簇（EOM-DIP-CCSD）的跃迁性质与 $\langle\hat{S}^{2}\rangle$
（Sahil Gulania，Wojciech Skomorowski，Anna Krylov）
- EOM-CC 中新增的非线性光学（NLO）性质（超极化率）（Kaushik Nanda，Anna Krylov）
- 面向强关联与磁性体系的新工具：将冻结自然轨道（FNO）近似推广至开壳层参考态
（Pavel Pokhilko，Anna Krylov；第 [7.9.14](../ch07_excited/sec_FNO.md) 节）
- 由 EOM-CC 波函数构造有效哈密顿量（Pavel Pokhilko，Anna Krylov；第 [13.6](../ch13_specialized/sec_EffHam.md) 节）
- 自旋禁阻跃迁的自然跃迁轨道（NTO）分析（Pavel Pokhilko，Anna Krylov；第 [7.9.21.4](../ch07_excited/sec_EOMGRAD.md#sec:EOMSOC) 节）
- 在复吸收势能（CAP）EOM-CCSD 中搜索复势能面（PES）的特殊点（极小点、最小能量交叉点（MECP）以及例外点）（Zsuzsanna Koczor-Benda，Thomas Jagau）
- Voronoi 复吸收势（CAP）与投影复吸收势（CAP）方法（James Gayvert，Ksenia Bravaya；第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节）
- 用于计算俄歇（Auger）衰减速率与共振寿命的两体戴森（Dyson）轨道（Wojciech Skomorowski，Anna Krylov）
- EOM-CC 的数值稳定性改进（Pavel Pokhilko，Anna Krylov）
- **二阶微扰理论（MP2）方法的新特性与改进：**

- 采用正则化轨道优化二阶 Møller-Plesset 微扰理论（$\kappa$-OOMP2）进行几何优化
（Joonho Lee，Martin Head-Gordon；第 [6.6.6](../ch06_correlation/sec_oomp2.md) 节）
- **分子间相互作用的新功能：**

- XSAPT+MBD 方法的实现（Kevin Carter-Fenk，John Herbert）
- **量子力学/分子力学（QM/MM）改进：**

- 用于几何优化的有限内存 BFGS（L-BFGS）算法（Bhaskar Rana，John Herbert）
- 谐振约束势（Harmonic confining potentials）（Saswata Dasgupta，John Herbert）
- **新方法与新功能：**

- 核-电子轨道密度泛函理论（NEO-DFT）及其含时方法（TD-DFT）（Fabian Pavosevic，Zhen Tao，Sharon Hammes-Schiffer）
- 受限激活空间自旋翻转（RAS-SF）方法的新模块（Shannon Houck，Nick Mayhall）
- 一族组态相互作用（CI）方法：非正交组态相互作用单激发（NOCIS）、静态交换（STEX），以及单中心 NOCIS（Katherine Oosterbaan，Martin Head-Gordon）
- 针对复基函数的积分筛选与分辨率恒等（RI）近似功能（Thomas Jagau）
- 针对复基函数的 RI-MP2 方法（Mario Hernández Vera，Thomas Jagau；第 [6.6.10](../ch06_correlation/sec_cbf_rimp2.md) 节）
- 在基于投影子的嵌入理论中用于截断虚空间的新方法（同心局域化，concentric localization）（Yuezhi Mao）
- 用于激发态轨道优化的平方梯度最小化（square gradient minimization）方法（Diptarka Hait，Martin Head-Gordon）
- 共振拉曼（Resonance Raman）光谱模拟（Saswata Dasgupta，John Herbert）
- 反键轨道的布居分析（Abdulrahman Aldossary）
- 基于片段的二态化（diabatization）方案（Yuezhi Mao）
- 支持不携带基函数的虚原子（ghost atom）（Bushra Alam，John Herbert）
- 电子局域函数（Electron localization function）（Bushra Alam，John Herbert
- 波函数分析的新输入选项（Felix Plasser）
- **BrianQC GPU 模块的新特性：**

- 扩展对 GPU 加速 DFT 交换-关联泛函的支持，涵盖局域密度近似（LDA）、广义梯度近似（GGA）及 meta-GGA 泛函
- 部分 GPU 加速的 DFT 频率计算
