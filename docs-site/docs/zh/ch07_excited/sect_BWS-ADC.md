---
title: "7.10.6 正则化激发态与 BWs-ADC"
---

## 7.10.6 正则化激发态与 BWs-ADC

（2026 年 7 月 4 日）

## 7.10.6.1 引言与理论

标准的、基于 Møller-Plesset 分拆（Møller-Plesset，MP）的 ADC 方案存在一个缺点：当 HOMO/LUMO 能隙趋近于零时，激发能和性质开始发散。这是由进入久期矩阵（secular matrix）的一阶 $t_{2}$-振幅发散所引起的。
通过在极化传播子（polarisation propagator）的微扰展开中选择*正则*（regular）的哈密顿量分拆，可以避免这一问题。
这里，我们采用 Carter-Fenk 和 Head-Gordon 提出的尺寸一致的 Brillouin-Wigner 分拆[[195]](../bib_references/bib.md#bib196)。
虽然它最初是作为一种重新分拆方案提出的，目的是使二阶 Brillouin-Wigner 理论具有尺寸一致性和尺寸广延性，但更好的理解方式是将 BWs-$n$ 视为一种正则化的 Rayleigh-Schrödinger 微扰理论，其零级哈密顿量和微扰项为：

<a id="A3.S8.EGx65"></a>

$$
\displaystyle\hat{H}^{(0)} \tag{7.147}
$$

其中，$\hat{W}$ 是一个分块对角的一电子算符，其性质在文献 [[335]](../bib_references/bib.md#bib339) 中得到了广泛探讨。

在 BWs-ADC 的框架下，我们推荐使用 MPR-BWs2 的 $A_{0}$ 和 $B_{0}$ 参数（另见 [6.9](../ch06_correlation/topic_mpr-bws2.md)）：

<a id="Ch7.E149"></a>

$$
\hat{W}=\frac{A_{0}}{8}\sum_{ijkab}\left(\langle ik||ab\rangle{t^{ab}_{jk}}^{(1)}\right)\left(\hat{a}^{\dagger}_{i}\hat{a}_{j}+\hat{a}^{\dagger}_{j}\hat{a}_{i}\right)+\frac{B_{0}}{8}\sum_{ijabc}\left(\langle ij||ac\rangle{t^{bc}_{ij}}^{(1)}\right)\left(\hat{a}^{\dagger}_{a}\hat{a}_{b}+\hat{a}^{\dagger}_{b}\hat{a}_{a}\right) \tag{7.149}
$$

BW-s2 理论的一个关键特点是，组合后的零级哈密顿量仍然构成一个单粒子算符，因此可以自洽地对角化，从而得到* dressed（重整化）* 轨道 $\phi_{p}^{\prime}(r,\sigma)$ 及相应的轨道能 $\varepsilon_{p}^{\prime}$：

<a id="Ch7.E150"></a>

$$
(\hat{F}+\hat{W})\phi_{p}^{\prime}(r,\sigma)=\varepsilon_{p}^{\prime}\phi_{p}^{\prime}(r,\sigma) \tag{7.150}
$$

如果 BWs-ADC 方程（包括久期矩阵-向量乘积，以及 ISR 性质计算所需的密度）用 dressed 轨道来表示，那么 BWs-ADC 方程的代数结构与相应的 MP-ADC 表达式几乎完全等价。这意味着 BWs-ADC 计算的 computational cost（计算成本）与其 MP-ADC 对应方法*几乎完全相同*。两个额外必需的步骤会略微增加成本：首先，BW-s2 基态是迭代求解的。其次，二阶基态双振幅（${t^{ab}_{ij}}^{(2)}$）由于 $\hat{H}^{(1)}$ 中存在 $\hat{W}$，需要一次成本为 $\mathcal{O}(N^{5})$ 的校正。

实际上，在同一台机器上，一次 BWs-ADC(2) 计算仅比等效的 MP-ADC(2) 计算多花 $1-5\%$ 的时间。对于 BWs-ADC(3) 计算，这一差异通常更小，因为所有计算复杂度为 $\mathcal{O}(N^{6})$ 的张量收缩在 BWs-ADC(3) 与 MP-ADC(3) 之间是完全相同的。

## 7.10.6.2 已实现的 BWs-ADC 方法概览

到目前为止，BWs-ADC 仅对粒子数守恒的激发态（即通过关键字 EE_STATES 访问的那些态）实现了。下面我们对每种已实现的 BWs-ADC 方法的性质进行概览。

- -

**BWs-ADC(0)** 仅为完整性而实现。由于所有零阶 ADC 方案都以自旋适配的 Koopman 激发作为激发向量、以（dressed）轨道能差作为相应的激发能，因此无论参数如何选择，都不推荐将该方法用于实际计算。
- -

**BWs-ADC(1)** 在激发能上与 MP-ADC(1) 完全相等。如果尝试进行 BWs-ADC(1) 计算，Q-Chem 会崩溃并转而指向常规的 ADC(1) 计算。
- -

**BWs-ADC(2)-s** 被发现始终优于 MP-ADC(2) 以及 CC2、CIS(D) 和 CIS(D${}_{\infty}$)。请注意，当 $A_{0}=3.8$、$B_{0}=0$ 时表现最佳，且对 $A_{0}$ 的依赖极小，这非常接近基态的最优参数选择（$A_{0}=4$，$B_{0}=0$）。另请注意，任何 $B_{0}\neq 0$ 的选择都会严重降低激发能的质量。
- -

**BWs-ADC(2)-x** 仅为完整性而实现，尚未进行基准测试。由于在久期矩阵的 *2p2h-2p2h* 分块中.ad hoc（临时性地）加入了一阶项，只有 *ph-ph* 分块的二阶贡献携带对正则化参数的依赖。因此预期其表现与 MP-ADC(2)-x 相仿。
- -

**BWs-ADC(3)** 被发现当 $A_{0}=-1$、$B_{0}=0$ 时表现最佳，不过满足约束 $A_{0}-B_{0}=-1$ 的相似参数选择几乎给出相同的误差。请注意，这一参数选择是*去正则化（deregularising）*的，即它无法描述 HOMO/LUMO 能隙消失或很小的体系。对于弱静态关联且双激发特征较小的态，BWs-ADC(3) 显著优于 BWs-ADC(2)。与此同时，那些正确描述需要三激发、且表现出显著静态关联的激发态则被描述得相对较差，导致在各基准测试中整体 MAE 与 BWs-ADC(2) 相近。

各方法以及推荐参数和设置的概览见表 [7.4](#table:bwsadc_overview)。

| 方法 | 计算标度 | 推荐 ( $A_{0}$ , $B_{0}$ ) | MAE [eV] | 适用场景 |
| --- | --- | --- | --- | --- |
| BWs-ADC(0) | $\mathcal{O}(N^{5})$ | - | - | 永不使用 |
| BWs-ADC(2)-s | $\mathcal{O}(N^{5})$ | (4, 0) | 0.16 | 单参考或少参考体系 |
| BWs-ADC(2)-x | $\mathcal{O}(N^{6})$ | - | - | 若基准测试表明其有效时使用 |
| BWs-ADC(3) | $\mathcal{O}(N^{6})$ | (-1, 0) | 0.16 | 单参考体系 |

表 7.4：BWs-ADC($n$) 方法的使用建议。Rec. ($A_{0}$, $B_{0}$) 指的是在小分子体系 122 个单激发基准测试中发现的最优参数[[859]](../bib_references/bib.md#bib895)。
MAE 表示在该基准上使用推荐参数所确定的最低平均绝对激发能误差。注意 MP-ADC(2) 的 MAE 分别为 0.21 eV 和 0.24 eV

。若要了解方法性能的更详细分析，请参见文献

## 7.10.6.3 在 Q-Chem 中使用 BWs-ADC

BWs-ADC 计算在单个 Q-Chem 作业中以两步流程执行。首先，在 `libgmbpt` 模块中运行一次 RI-BW-s2 计算。然后，将收敛后的 dressed 轨道和轨道能传递给 `adcman` 进行后续的 ADC 计算。正因如此，BWs-ADC *仅*可在分辨率恒等（Resolution of Identity, RI）近似下使用。

要运行 BWs-ADC 计算，请在输入文件中包含以下内容：

- •

在 REM 段中，将 METHOD 设置为 RIBWS2。
- •

在 REM 段中，同时指定 BASIS 以及 AUX_BASIS 或 AUX_BASIS_CORR 其中之一。
- •

在 *$bws2* 段中使用 METHOD 关键字选择一种分拆方案。我们推荐：

- **–**

在 *$bws2* 段中将 METHOD 设置为 MPR-BWS2。
- **–**

在 *$bws2* 段中将 MPR_A0 设置为目标 $A_{0}$ 值。
- **–**

在 *$bws2* 段中将 MPR_B0 设置为目标 $B_{0}$ 值。
- •

在 *$bws2* 段中，使用 EXC_METHOD 关键字确定 BWs-ADC 的变体：

- **–**

对于 BWs-ADC(0)，将 EXC_METHOD 设置为 ADC(0) 或 ADC0。
- **–**

对于 BWs-ADC(2)-s，将 EXC_METHOD 设置为 ADC(2)、ADC2、ADC(2)-S 或 ADC2-S 中的任意一个。
- **–**

对于 BWs-ADC(2)-x，将 EXC_METHOD 设置为 ADC(2)-X 或 ADC2-X。
- **–**

对于 BWs-ADC(3)，将 EXC_METHOD 设置为 ADC(3) 或 ADC3。
- •

对于限制（restricted）参考，使用 REM 段中的 EE_STATES 或 EE_SINGLETS 和 EE_TRIPLETS 关键字指定激发态数目。
- •

对于非限制（unrestricted）参考，仅使用 EE_STATES 关键字。

用于 RI-BW-s2 计算作业控制（Job Control）的所有关键字（见第 [6.8.2](../ch06_correlation/sect_bws2_jobcontrol.md) 节）均可用于指定 BWs-ADC 计算中基态计算的细节。
此外，用于 ADC 作业控制的所有关键字（见第 [7.10.13](sect_adc_jobcontrol.md) 节）均可用于调整 BWs-ADC 计算中 ADC 部分的设置。
