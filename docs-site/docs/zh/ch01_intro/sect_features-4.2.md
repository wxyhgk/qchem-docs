---
title: "1.3.15 Q-Chem 4.2 新特性"
---

## 1.3.15 **Q-Chem** 4.2 新特性

(2026 年 7 月 4 日)

- 输入文件更改：

- 新关键字 METHOD 在大多数情况下取代了 EXCHANGE 与 CORRELATION 这一对关键字，从而简化了输入（见第 [4](../ch04_scf/chap_scf.md) 章）。
- 用于请求激发态计算的关键字已做修改与简化（详见第 [7](../ch07_excited/chap_excited.md) 章）。
- 用于溶剂化模型的关键字已做修改与简化（详见第 [11.2](../ch11_env/topic_solvation.md) 节）。
- 核磁共振（NMR）计算的新特性，包括自旋-自旋耦合（J. Kussmann、A. Luenser 和 C. Ochsenfeld；第 [10.11.2](../ch10_properties/sec_magnetic_NMR.md) 节）。
- 新的内置基组（Basis Set）（见第 [8](../ch08_basis/chap_basis.md) 章）。
- EOM-CC 的新特性与性能改进：

- EOM-CC 方法得到扩展，通过复标度（complex scaling）与复吸收势（complex absorbing potentials）来处理亚稳电子态（共振态）（D. Zuev、T.-C. Jagau、Y. Shao 和 A. I. Krylov；第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节）。
- 为 EOM-CC 迭代求解器添加了新特性，例如用于求解内部本征值的方法以及用户指定的初始猜测（D. Zuev；第 [7.9.16](../ch07_excited/subsec_EOM-CC-diag.md) 节）
- 针对 (EOM-)CC 梯度的多线程并行代码，以及改进的 CCSD(T) 性能。
- ADC 方法的新特性与性能改进（M. Wormit、A. Dreuw）：

- RI-ADC 能够以更低成本处理更大的体系（第 [7.10.4](../ch07_excited/sec_ADC_RI.md) 节）。
- SOS-ADC 方法（第 [7.10.5](../ch07_excited/sect_SOS-ADC.md) 节）。
- ADC 的态-态（state-to-state）性质（第 [7.10.10](../ch07_excited/sect_ADC_prop.md) 节）。
- SM12 隐式溶剂化模型（A. V. Marenich、D. G. Truhlar 和 Y. Shao；第 [11.2.9.1](../ch11_env/ex_SMx-User-Solvent.md#subsubsec:SM8) 节）。
- 与 NBO v. 6 的接口（第 [10.3.1](../ch10_properties/sect_NBO.md) 节）。
- 在 SOS-CIS(D) 与 TDDFT 级别上优化电子态之间的最小能量交叉点（MECP）（X. Zhang 和 J. M. Herbert；第 [9.8.3](../ch09_opt/sect_MECP.md) 节）。
- 用于激发态 $\Delta$SCF 计算的 ROKS 方法（T. Kowalczyk 和 T. Van Voorhis；第 [7.7.4](../ch07_excited/ex_ESROKS.md) 节）。
- 用于 SCF 方法的基于片段的初始猜测（第 [12.3](../ch12_frag/sect_FRAGMOguess.md) 节）。
- 用于改善小能隙体系 SCF 收敛的伪分数占据数方法（D. S. Lambrecht；第 [4.5.6](../ch04_scf/sect_pFNO.md) 节）。
- 密度嵌入（density embedding）方案（B. J. Albrecht、E. Berquist 和 D. S. Lambrecht；第 [11.6](../ch11_env/sect_den_emb.md) 节）。
- 基于片段的多个体展开（many-body expansion）方法的新特性与增强（K. U. Lao 和 J. M. Herbert）：

- XSAPT(KS)+D：
对称匹配微扰理论（symmetry-adapted perturbation theory）的色散校正版本，可快速、准确地计算非共价团簇的相互作用能（第 [12.10](../ch12_frag/sect_XSAPT.md) 节）。
- 用于团簇的多个体展开与片段分子轨道（fragment molecular orbital, FMO）方法（第 [12.12](../ch12_frag/sec_MBE.md) 节）。
- 具有正确 Ewald 求和的周期性边界条件，仅适用于能量计算（Z. C. Holden 和 J. M. Herbert；第 [11.3](../ch11_env/sec_QMMM.md) 节）。
