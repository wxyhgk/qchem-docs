---
title: "7.4.1 引言与理论"
---

## 7.4.1 引言与理论

(July 4, 2026)

尽管第 [7.3](sect_tddft.md) 节所讨论的理论被普遍称为“含时”密度泛函理论（Time-Dependent Density Functional Theory, TDDFT），
但事实上它是线性响应（Linear-Response, LR）DFT 在频率域中的变换形式，[[418]](../bib_references/bib.md#bib427)
有时会被额外冠以 LR-TDDFT 的名称，以便与本节所描述的“实时”（Real Time, RT）版本的 TDDFT 相区分。“实时含时密度泛函理论”
（real-time time-dependent DFT, RT-TDDFT）这一说法足够拗口，因此此处描述的理论也被称为*含时 Kohn-Sham*（Time-Dependent Kohn-Sham, TDKS）
理论，[[1578]](../bib_references/bib.md#bib1641)
 这一术语实际上与 Gross 及其合作者在发展基于含时 Kohn-Sham 方程的理论时
所使用的原始表述更为一致。[[498]](../bib_references/bib.md#bib511)

TDKS 方法是显式含时的，其本质是在基态密度受到微扰之后，对含时的 Kohn-Sham 分子轨道（Molecular Orbitals, MOs）进行传播。

当只需要求解少数几个低激发态时，LR-TDDFT 计算往往是预测共振电子响应频率和强度最高效的方式。
然而，若要获得宽带谱（例如在 X 射线区域），可能需要数百个激发态。
在这种情况下，实时方法可能更为可取，因为它可以通过对含时偶极矩函数进行傅里叶变换，获得整个吸收谱
（覆盖所有激发能），而无需逐态计算谱线。这正是*实时*
电子结构方法在理论上的通用基础。[[1124]](../bib_references/bib.md#bib1171)

微扰会产生所有（对称性允许的）激发的叠加态，随之而来的时间演化的傅里叶分量则包含了全部的激发能信息。下一节将对
该理论进行更详细的描述，随后第 [7.4.2](sec_TDKS_JobControl.md) 节将介绍 TDKS 的作业控制变量。
利用 TDKS 方法计算宽带吸收谱的内容在第 [7.4.3](sec_TDKS_Spectra.md) 节中讨论。

自 v. 5.3 版本起，**Q-Chem** 的 TDKS 模块经过大幅重写，新增了对高级传播子、[[1578]](../bib_references/bib.md#bib1641)
复吸收势（Complex Absorbing Potentials）[[1579]](../bib_references/bib.md#bib1642)
 以及 Padé 近似
的支撑，以加速傅里叶变换后偶极矩函数的收敛。[[566]](../bib_references/bib.md#bib585)

使用 TDKS/RT-TDDFT 代码的用户请引用文献 [[1579]](../bib_references/bib.md#bib1642)
 和 [[566]](../bib_references/bib.md#bib585)
。

在 $t=0$ 时刻对基态分子轨道 $\phi_{k}(\mathbf{r},0)$ 施加微扰之后，这些分子轨道按照含时薛定谔方程随时间演化。对于自洽场（Self-Consistent Field, SCF）级别的理论，
这是一个单电子方程

<a id="eq:TDKS"></a>

$$
\text{i}\hbar\frac{d\phi_{k}(\mathbf{r},t)}{dt}=\hat{F}(t)\phi_{k}(\mathbf{r},t)\;. \tag{7.58}
$$

这一时间演化可以等价地用密度 $\rho(\mathbf{r},t)$ 时间演化的 Liouville-von Neumann 方程来表示：

<a id="eq:LvN"></a>

$$
\text{i}\hbar\frac{d\rho(\mathbf{r},t)}{dt}=\bigl{[}\hat{F}(t),\;\rho(\mathbf{r},t)]\;. \tag{7.59}
$$

除了获得宽带谱之外，实时 SCF 方法还可用于模拟电子的阿秒（attosecond）动力学，例如在强场存在的情况下。需要注意
的是，通过积分方程 ([7.58](#eq:TDKS)) 或方程 ([7.59](#eq:LvN)) 所模拟的动力学是*电子*动力学，其基本时间
尺度为阿秒量级，这可以由时间原子单位的大小
（$\hbar/E_{h}\approx 2.4\times 10^{-17}$ s）估计得出。有限积分时间步长 $\Delta t$
必须远小于该值，**Q-Chem** 中的默认设置为 $\Delta t=0.02~{}\mbox{a.u.}=4.8\times 10^{-4}$ fs。
因此，可以合理模拟的最大时间尺度可能仅为皮秒量级，且目前这种时间传播仅在夹核近似（clamped-nuclei
approximation）内可用，*即*，无法模拟电子与核的耦合动力学。

由于 Fock 算符 $\hat{F}$ 依赖于其自身（随时间演化的）本征函数 $\phi_{i}(\mathbf{r},t)$，
支配方程 ([7.58](#eq:TDKS)) 或方程 ([7.59](#eq:LvN)) 中时间演化的算符 $\hat{F}(t)$ 是含时的，
这使这些方程的积分变得复杂。[[1578]](../bib_references/bib.md#bib1641)
 积分这些方程（在有限时间步长 $\Delta t$ 上）的最简单算法是*修正中点酉变换*（Modified Midpoint Unitary Transformation, MMUT）
方法，[[819]](../bib_references/bib.md#bib848)
 该方法对算符 $\hat{F}(t+\Delta t/2)$ 进行近似。当使用 MMUT 算法时，
单电子动力学一个时间步长的开销与基态 SCF 计算中单个 SCF 循环的开销相当，*即*，只需构造并
对角化一次 Fock 矩阵。内存占用约为基态计算的两倍，因为含时分子轨道是复数值的，但这通常
比线性响应（LR-）TDDFT 的内存占用小得多，尤其是在 LR-TDDFT 计算中请求的根数较多时（宽带谱所需），
或者态密度较高时（如半导体模型）。[[962]](../bib_references/bib.md#bib1004)

与一阶 MMUT 算法相比，还可使用更高阶的预测/校正（predictor/corrector）算法来积分动力学方程。[[1578]](../bib_references/bib.md#bib1641)

这些算法允许使用更大的时间步长 $\Delta t$，代价是每个时间步长需要几次 Fock 矩阵构造。
或许更重要的是，预测/校正算法在每个时间步长内将 Fock 算符 $\hat{F}(t)$ 和
$\hat{F}(t+\Delta t)$ 迭代至自洽，从而保证时间传播的稳定性（前提是自洽过程收敛）。MMUT 算法并
*不*保证动力学稳定，而总能量守恒只是轨迹被精确积分的必要而非充分条件。使用 MMUT 时，可以找到
这样的例子：能量虽然守恒，但由于使用了过大的 $\Delta t$ 值，谱线仍然发生偏移
（相对于使用极小时间步长获得的基准结果），而非自洽的 MMUT 算法无法检测和诊断这一问题。[[1578]](../bib_references/bib.md#bib1641)

电子动力学的传播只需要基态计算引擎（尽管使用的是复数值轨道），因此可在任何 SCF 级别的理论下使用，
包括 Hartree-Fock 理论或密度泛函理论（Density Functional Theory, DFT）。名称“TDKS”
（相对于笨拙的“RT-TDDFT”）强调方程 ([7.58](#eq:TDKS)) 是含时薛定谔方程的 Kohn-Sham 类似形式。
TDKS 计算每个时间步长的开销不应超过基态 SCF 循环开销的几倍。
**Q-Chem** 的实现利用了共享内存并行，强烈建议至少使用 8 个（也可以更多）处理器核心，
因为所需的时间步长数（从而 Fock 矩阵构造的次数）可能非常大。（使用多核心需通过 `-nt` 标志指定。）

通过在 *$rem* 输入段中设置 TDKS = TRUE 即可请求 TDKS 计算，其他作业控制选项在第 [7.4.2](sec_TDKS_JobControl.md) 节中讨论。
第 [7.4.3](sec_TDKS_Spectra.md) 节讨论如何从电子动力学的 TDKS 模拟中计算宽带谱。
第 [7.4.4](sec_TDKS_HHG_Spectra.md) 节讨论如何从电子动力学的 TDKS 模拟中计算高次谐波产生（High-Harmonic Generation, HHG）谱。

TDKS

### `TDKS`

> **用于开启 TDKS 计算的作业控制关键字**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 在基态 SCF 计算之后执行 TDKS 计算
>     * FALSE
>     * 不执行 TDKS 计算
> * **建议**: 无。
