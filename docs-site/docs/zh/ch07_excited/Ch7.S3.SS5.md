---
title: "7.3.5 电子亲和能（EA-）TDDFT"
---

## 7.3.5 电子亲和能（Electron-Affinity, EA-）TDDFT

（2026 年 7 月 4 日）

X 射线吸收光谱（X-ray Absorption Spectra, XAS）对含时密度泛函理论（Time-Dependent Density Functional Theory, TDDFT）而言是一项重大挑战。
小分子气相体系 K 边 XAS 峰位的误差通常超过
10 eV，而在凝聚相中，峰位与强度的误差会导致 K 边光谱出现严重畸变。
这些误差可追溯至两个来源：

1. 1.

轨道弛豫效应的缺失，而基于基态参考轨道、仅含单激发的线性响应理论很难对此加以补偿；
2. 2.

TDDFT 势中一类被称为粒子–空穴自相互作用误差（particle–hole self-interaction error）的激发态自相互作用误差。

这两者都可以通过为核心激发问题选取更合适的参考轨道集合（*e.g.*，一个核心电离参考行列式）来加以修正，正如第 [7.6.2](subsec_STEX.md) 节中静态交换（Static-Exchange, STEX）近似所做的那样。
将 STEX 推广以纳入密度泛函理论关联效应的做法，是通过两次独立的线性响应实现的。
首先，从一组初始的核心电离分子轨道出发，将缺失的核心电子重新附加回去（响应 #1），
随后进行第二次线性响应以激发该核心电子。
第二次线性响应是在一个非稳态的初始密度之上进行的，由于绝热近似（adiabatic approximation）的存在，这会带来问题。所幸，
针对绝热近似相关误差的一阶精确修正可以被推导出来，并且在
所有 EA-TDDFT 计算中都会自动施加。这一修正恰好呈现出类似激发态自相互作用误差的形式，因此 EA-TDDFT
方程天然地不含激发态自相互作用误差。正因如此，使用标准密度泛函，EA-TDDFT 的
统计误差（均方根偏差）可低至仅 0.5 eV。[[193]](../bib_references/bib.md#bib193)

EA-TDDFT 在参考轨道层面纳入轨道弛豫效应，相较于 TDDFT，也为
溶剂化分子的光谱带来了关键性的改进。[[194]](../bib_references/bib.md#bib194)

EA-TDDFT 仅对限制开壳层（restricted open-shell）轨道有定义，
并产生自旋纯（spin-pure）的光谱。

完整的 EA-TDDFT 方程具有熟悉的形式，

<a id="Ch7.E34"></a>
$$
\displaystyle A_{ia,ib} \tag{7.34a}
$$

其中 $E^{+}$ 是核心电离行列式经自洽优化的能量，$F_{ab}^{+}$ 是核心电离（core-ion）Fock 矩阵虚–虚块（virtual-virtual block）的矩阵元，
并且所有积分都在核心电离轨道下计算。
虽然完整的 EA-TDDFT 方程可以低成本求解
（在 *$nocis* 输入段中请求 **EA_RPA** 即可），
但对于 K 边 XAS，很少需要求解整个类似 RPA 的表达式。
取而代之的是，对于 K 边跃迁，可以在 *$nocis* 中设置 **EA_TDA**
来使用 Tamm-Dancoff 近似，而不会牺牲任何精度。[[194]](../bib_references/bib.md#bib194)

需要注意的是，EA-TDDFT 方程中只考虑一个占据轨道指标，
这意味着隐式地启用了核价分离近似（core-valence separation approximation）。
此外，由于 EA-TDDFT 基于线性响应理论，
因此不需要像 STEX 或 1C-NOCIS 那样构造基态
与单激发行列式之间的非正交矩阵元。
这意味着 EA-CIS（采用 Hartree-Fock 泛函的 EA-TDDFT）
会给出与 STEX 略有不同的结果，但二者差异
通常不超过 0.1 eV。[[193]](../bib_references/bib.md#bib193)

上述方程中 $E^{+}$ 的存在意味着，
必须针对每一个将要产生激发的核心轨道，优化相应核心电离参考轨道。
在 NOCIS 与 STEX 的实现中，这一过程一向完全依赖
第 [7.7.2](ex_OpSing.md) 节中的最大重叠法（Maximum Overlap Method, MOM）。
然而，**Q-Chem** 如今已具备若干优秀的算法，
可用于收敛非 *Aufbau*（non-*Aufbau*）的 SCF 解，
例如态靶向能量投影（State-Targeted Energy Projection, STEP）[[196]](../bib_references/bib.md#bib189)

以及平方梯度极小化（Square Gradient Minimization, SGM）；[[511]](../bib_references/bib.md#bib526)

分别参见第 [7.7.8](ex_ROSTEP.md) 节与第 [7.7.5](ex_BEDSCF.md) 节。
通过在 *$nocis* 输入段中设置 **DSCF_ALGORITHM**
或 **REF_SCF_ALGORITHM**，上述所有方法如今都可在 EA-TDDFT
代码中使用。由 STEP 与 MOM 构成的混合算法——在优化的初始若干循环中运行 STEP，
将解引导至一组条件良好的猜测轨道，随后再进行 MOM 优化——
在其他算法无法收敛时已被证明极为成功。该算法可通过设置
**DSCF_ALGORITHM** = **STEP_MOM**
来启用，并使用关键字 **STEP_MOM_START**
指定 STEP 关闭、MOM 启动的时间点。

在 EA-TDDFT 中，有两个环节可以利用局域化来改善结果
或使轨道选取更加便捷。
其一，当选取两个或更多参考轨道时，程序会自动对目标核心轨道执行 Boys 局域化，
以改善核心电离 SCF 收敛到正确极小点的表现。该
局域化流程也可手动控制（*e.g.*，局域化若干轨道但只计算其中某一个轨道的激发，
或完全关闭局域化），通过关键字 **LOCALIZE_ORBITALS** 实现。
在具有许多能量相近核心轨道的大型体系中（*e.g.*，
需要考察特定 O(1s) 轨道响应的水团簇），
可以使用子系统投影原子轨道分解（Subsystem Projected AO Decomposition, SPADE）轨道[[253]](../bib_references/bib.md#bib254)

在考虑 **ORB_OFFSET** 之前，将轨道局域化到某一特定原子子集上。
以上文给出的水团簇为例，
若关注的是 *$molecule* 段中的第一个水分子，
则应在 *$nocis* 段中设置 “**SUBSYSTEM_ATOMS** 1 2 3”，
如此该原子子集上的 O(1s) 轨道所对应的变量 **ORB_OFFSET**
将被设为 0。
