---
title: "1.3.19 Q-Chem 3.$\,$*x* 版本功能汇总"
---

## 1.3.19 **Q-Chem** 3.$\,$*x* 版本功能汇总

(2026 年 7 月 4 日)

- 密度泛函理论（DFT）泛函与算法：

- 长程校正（Long-Ranged Corrected, LRC）泛函，亦称 range-separated 杂化泛函（M. A. Rohrdanz 和 J. M. Herbert）
- 约束密度泛函理论（Constrained DFT）（Q. Wu 和 T. Van Voorhis）
- Grimme 的 "DFT-D" 经验色散校正（C.-D. Sherrill）
- "增量式"（Incremental）DFT 方法，可显著加速后续自洽场（SCF）循环中的交换-关联求积（S. T. Brown）
- 高效的 SG-0 求积网格，其网格点数约为 SG-1 的一半（S.-H. Chien）
- 溶剂化模型：

- SM8 模型
（A. V. Marenich, R. M. Olson, C. P. Kelly, C. J. Cramer 和 D. G. Truhlar）
- Kirkwood-Onsager 反应场模型
（C.-L. Cheng, T. Van Voorhis, K. Thanthiriwatte 和 S. R. Gwaltney）
- Chipman 的 SS(V)PE 模型（S. T. Brown）
- 基态与激发态的二阶微扰理论算法：

- 双基组 RIMP2 能量与解析梯度（R. P. Steele, R. A. DiStasio Jr. 和 M. Head-Gordon）
- O2 能量与梯度（R. C. Lochan 和 M. Head-Gordon）
- 用于激发态的 SOS-CIS(D)、SOS-CIS(D${}_{0}$) 和 RI-CIS(D)（D. Casanova, Y. M. Rhee 和 M. Head-Gordon）
- MP2 与 SOS-MP2 的高效分解恒等（Resolution-of-Identity, RI）实现（包括能量与梯度），
以及 RI-TRIM 与 RI-CIS(D) 能量的实现（Y. Jung, R. A. DiStasio, Jr., R. C. Lochan 和 Y. M. Rhee）
- 耦合簇（Coupled-Cluster, CC）方法（P. A. Pieniazek, E. Epifanovsky, A. I. Krylov）：

- IP-CISD 与 EOM-IP-CCSD 能量及梯度
- 多线程（OpenMP）并行耦合簇计算
- 采用 CCSD 与 EOM-CCSD 方法的势能面交叉最小化（E. Epifanovsky）
- 在 CCSD 与 EOM-CCSD 方法中用于基态及激发态电离的戴森轨道（Dyson Orbitals）（M. Oana）
- 量子力学/分子力学（QM/MM）方法（H. L. Woodcock, A. Ghysels, Y. Shao, J. Kong 和 H. B. Brooks）

- **Q-Chem**/**Charmm** 接口（H. L. Woodcock）
- 完整的 QM/MM 黑塞矩阵（Hessian）求值及近似移动块黑塞矩阵（mobile-block-Hessian）求值
- 两层 ONIOM 模型（Y. Shao）。
- 与 **Molaris** 模拟程序包的集成（E. Rosta）。
- 改进的双电子积分程序包

- 针对现代计算机体系结构重写 Head-Gordon–Pople 算法（Y. Shao）
- 傅里叶变换库仑（Fourier Transform Coulomb, FTC）方法，可线性标度地构建库仑矩阵，即使对于高角动量
及含弥散函数的基组同样适用（L. Fusti-Molnar）
- 双基组自洽场（SCF）计算，可将大基组 DFT 计算的成本降低一个数量级（J. Kong 和 R. P. Steele）
- 关联（correlation）程序包的增强，包括：

- 提供最为齐全的 EOM-CCSD 方法族，包括
EOM-SF-CCSD、EOM-EE-CCSD、EOM-DIP-CCSD、EOM-IP/EA-CCSD（A. I. Krylov）。
- 可用于 RHF、UHF 及 ROHF 参考态。
- 解析梯度与性质计算（永久偶极矩、跃迁偶极矩*等*）。
- 充分利用阿贝尔点群对称性（Abelian point-group symmetry）。
- 耦合簇完美配对（perfect-pairing）方法，适用于活性电子数 $>100$ 的体系（M. Head-Gordon）
- 采用"生长字符串"（growing string）算法进行过渡态结构搜索（A. Heyden 和 B. Peters）：
- *从头算*（*Ab initio*）分子动力学（J. M. Herbert）
- 适用于大体系的线性标度性质计算（J. Kussmann, C. Ochsenfeld）：

- 核磁共振（NMR）化学位移
- 静态与动态极化率
- 静态超极化率、光整流（optical rectification）及电光普克尔斯效应（electro-optical Pockels effect）
- 非谐频率（C. Y. Lin）
- 波函数分析工具：

- 采用自适应局域分子轨道能量分解分析（ALMO-EDA）进行分子间相互作用分析（R. Z. Khaliullin 和 M. Head-Gordon）
- 电子转移分析（Z.-Q. You 和 C.-P. Hsu）
- 原子核处自旋密度（V. A. Rassolov）
- 位置、动量及 Wigner 内函数（intracules）（N. A. Besley 和 D. P. O’Neill）
- 图形用户界面（GUI）选项：

- **IQmol**，一个完全集成的 GUI。**IQmol** 包含输入文件生成器与上下文帮助、分子构建器、
任务提交工具以及可视化套件（分子轨道与电子密度查看器、频率等）。
如需获取最新版本及下载/安装说明，请访问 **IQmol** 主页
（`http://www.iqmol.org`）。
- 与 **Spartan** 程序包的无缝集成
（参见 `www.wavefun.com`）。
- 支持多个其他公有领域的可视化程序：

- **WebMO**

`https://www.webmo.net`
- **Avogadro**

`https://avogadro.cc`
- **MolDen**

`http://www.cmbi.ru.nl/molden`
- **MacMolPlt**（通过 **MolDen** 格式的输入文件）

`https://brettbode.github.io/wxmacmolplt`
- **JMol**

`http://jmol.sourceforge.net/`
