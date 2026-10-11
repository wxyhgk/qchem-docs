---
title: "4.2.1 SCF 与 LCAO 近似"
---

## 4.2.1 SCF 与 LCAO 近似

（2026 年 7 月 4 日）

非相对论量子化学的基本方程是定态薛定谔方程（time-independent Schrödinger equation），

<a id="eq400"></a>

$$
\hat{H}({\rm{\bf R}},{\rm{\bf r}})\;\Psi({\rm{\bf R}},{\rm{\bf r}})=E({\rm{\bf
R}})\;\Psi({\rm{\bf R}},{\rm{\bf r}}). \tag{4.1}
$$

在量子化学中，该方程是针对固定的核坐标（$\mathbf{R}$）值、作为电子变量（$\mathbf{r}$）的函数来求解的。式 ([4.1](#eq400)) 中的哈密顿算符（Hamiltonian operator）为

<a id="eq:Hamiltonian"></a>

$$
\hat{H}=-\frac{1}{2}\sum_{i=1}^{N}\hat{\nabla}_{i}^{2}-\frac{1}{2}\sum_{A=1}^{M}\frac{1}{M_{A}}\hat{\nabla}_{A}^{2}-\sum_{i=1}^{N}\sum_{A=1}^{M}\frac{Z_{A}}{r_{iA}}+\sum_{i=1}^{N}\sum_{j>i}^{N}\frac{1}{r_{ij}}+\sum_{A=1}^{M}\sum_{B>A}^{M}\frac{Z_{A}Z_{B}}{R_{AB}} \tag{4.2}
$$

采用原子单位（atomic units），其中

<a id="eq402"></a>

$$
\hat{\nabla}^{2}=\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}\;. \tag{4.3}
$$

在式 ([4.2](#eq:Hamiltonian)) 中，$Z$ 是核电荷数，$M_{A}$ 是核 $A$ 的质量与电子质量之比，$R_{AB}=|\mathbf{R}_{A}-\mathbf{R}_{B}|$ 是核 $A$ 与核 $B$ 之间的距离，$r_{ij}=|\mathbf{r}_{i}-\mathbf{r}_{j}|$ 是第 $i$ 个与第 $j$ 个电子之间的距离，$r_{iA}=|\mathbf{r}_{i}-\mathbf{R}_{A}|$ 是第 $i$ 个电子与第 $A$ 个核之间的距离，$M$ 是核的数目，$N$ 是电子的数目。总能量 $E$ 是 $\hat{H}$ 的本征值（eigenvalue），其对应的本征函数（即波函数，wave function）为 $\Psi$。

将电子运动与核运动分离——这一思想最初源于 Born 和 Oppenheimer[[147]](../bib_references/bib.md#bib138)——可得到电子哈密顿算符

<a id="eq403"></a>

$$
\hat{H}_{\mathrm{elec}}=-\frac{1}{2}\sum_{i=1}^{N}\hat{\nabla}_{i}^{2}-\sum_{i=1}^{N}\sum_{A=1}^{M}\frac{Z_{A}}{r_{iA}}+\sum_{i=1}^{N}\sum_{j>i}^{N}\frac{1}{r_{ij}} \tag{4.4}
$$

求解相应的电子薛定谔方程，

<a id="eq404"></a>

$$
\hat{H}_{\mathrm{elec}}\Psi_{\mathrm{elec}}=E_{\mathrm{elec}}\Psi_{\mathrm{elec}}\;, \tag{4.5}
$$

可得到总电子能量 $E_{\mathrm{elec}}$ 以及电子波函数 $\Psi_{\mathrm{elec}}$，后者描述了核位置固定时电子的分布。总能量只需将核–核排斥能 [式 ([4.2](#eq:Hamiltonian)) 中的第五项] 加到总电子能量上即可求得：

<a id="eq405"></a>

$$
E_{\mathrm{tot}}=E_{\mathrm{elec}}+E_{\mathrm{nuc}}\;. \tag{4.6}
$$

求解式 ([4.5](#eq404)) 的本征值问题可得到一组本征函数（$\Psi_{0}$、$\Psi_{1}$、$\Psi_{2}\ldots$），其对应的本征值满足 $E_{0}\leq E_{1}\leq E_{2}\leq\ldots$。

我们感兴趣的是确定最低本征值及其 associated 本征函数，它们对应于分子的基态（ground state）能量和波函数。然而，除最简单的体系外，求解式 ([4.5](#eq404)) 极为困难，实践中我们所能做的只是寻找近似解。

求解式 ([4.5](#eq404)) 时采用的第一个近似是独立电子（平均场）近似（independent-electron (mean-field) approximation），其中波函数被近似为单电子函数（即分子轨道（Molecular Orbital, MO））的反对称化乘积。每个分子轨道的确定都是考虑电子在其他所有电子形成的平均场中运动。由此便得到著名的 Slater 行列式波函数[[1266]](../bib_references/bib.md#bib1315)

<a id="eq406"></a>

$$
\Psi=\frac{1}{\sqrt{n!}}\left|{{\begin{array}[]{cccc}\chi_{1}(1)&\chi_{2}(1)&\cdots&\chi_{n}(1)\\
\chi_{1}(2)&\chi_{2}(2)&\cdots&\chi_{n}(2)\\
\vdots&\vdots&\hfil&\vdots\\
\chi_{1}(n)&\chi_{2}(n)&\cdots&\chi_{n}(n)\\
\end{array}}}\right| \tag{4.7}
$$

其中 $\chi_{i}$ 是自旋轨道（spin orbital），它是分子轨道 $\psi_{i}$ 与自旋函数（$\alpha$ 或 $\beta$）的乘积。

通过在所谓的"自洽场"（self-consistent field, SCF）近似中对多电子问题的能量进行变分最小化，可得到最优的分子轨道集合。SCF 方法的原型是 Hartree-Fock（HF）近似，但这些 SCF 方法也包括 KS-DFT（第 [5 章](../ch05_dft/chap_DFT.md)）。所有 SCF 方法都导出如下形式的方程

<a id="eq407"></a>

$$
\hat{f}(i)\,\chi(\mathbf{x}_{i})=\varepsilon\,\chi(\mathbf{x}_{i})\;, \tag{4.8}
$$

其中第 $i$ 个电子的 Fock 算符（Fock operator）$\hat{f}(i)$ 为

<a id="eq408"></a>

$$
\hat{f}(i)=-\frac{1}{2}\hat{\nabla}_{i}^{2}+\upsilon_{\rm eff}(i)\;. \tag{4.9}
$$

这里 $\mathbf{x}_{i}$ 是第 $i$ 个电子的自旋与空间坐标，函数 $\chi$ 是自旋轨道，$\upsilon_{\rm eff}$ 是第 $i$ 个电子所"感受到"的有效势（effective potential），它取决于其他电子的自旋轨道。有效势 $\upsilon_{\rm eff}$ 的具体形式取决于所采用的 SCF 方法，*即*，取决于密度泛函近似的选择。

求解式 ([4.5](#eq404)) 时通常引入的第二个近似是引入原子轨道（Atomic Orbital, AO）基组 $\{\phi_{\mu}\}$，分子轨道将由这些原子轨道的线性组合（Linear Combination of Atomic Orbitals, LCAO）确定。存在许多标准化的、以原子为中心的高斯基组（Gaussian basis set），其细节在第 [8 章](../ch08_basis/chap_basis.md)中讨论。

在式 ([4.8](#eq407)) 中消去自旋分量并引入有限基组后，

<a id="eq409"></a>

$$
\psi_{i}=\sum_{\mu}{c_{\mu i}\phi_{\mu}}\;, \tag{4.10}
$$

式 ([4.8](#eq407)) 约化为 Roothaan-Hall 矩阵方程

<a id="eq:Roothaan-Hall"></a>

$$
\mathbf{FC}=\bm{\varepsilon}\mathbf{SC}\;. \tag{4.11}
$$

这里，$\mathbf{F}$ 是 Fock 矩阵，$\mathbf{C}$ 是分子轨道系数的方阵，$\mathbf{S}$ 是 AO 重叠矩阵（overlap matrix），其元素为

<a id="eq411"></a>

$$
S_{\mu\nu}=\int{\phi_{\mu}({\rm{\bf r}})}\phi_{\nu}({\rm{\bf r}})d{\rm{\bf r}} \tag{4.12}
$$

$\bm{\varepsilon}$ 是包含轨道能量的对角矩阵。若在式 ([4.7](#eq406)) 中为 $\alpha$ 与 $\beta$ 自旋引入各自独立的空间轨道，从而推广到非限制（unrestricted）形式，便得到 Pople-Nesbet 方程[[1116]](../bib_references/bib.md#bib1159)

<a id="A3.S8.EGx1"></a>

$$
\displaystyle\mathbf{F}^{\alpha}\mathbf{C}^{\alpha} \tag{4.13}
$$

在 SCF 方法中，首先确定一个关于分子轨道的初始猜测，由此可计算每个电子感受到的平均场。通过求解 Roothaan-Hall 或 Pople-Nesbet 本征值方程，可得到一组新的分子轨道，从而得到限制型或非限制型的有限基组 SCF 近似。重复此过程，直到新的分子轨道与上一次迭代的轨道差异可忽略不计为止。式 ([4.9](#eq408)) 中有效势的 Hartree-Fock 近似固有地忽略了瞬时电子–电子相关（electron-electron correlation）——这些相关在 SCF 过程中被平均化——尽管 HF 计算所得的化学结论往往能提供有价值的定性洞察，但其定量能量学结果常常较差。原则上，DFT 方法能够捕获全部相关能（correlation energy），*即*，HF 能量与真实能量之差。实践中，现有最好的密度泛函表现良好但并不完美，因此往往需要传统的后 Hartree-Fock（post-HF）方法来计算相关能（见第 [6 章](../ch06_correlation/chap_correlation.md)）。

尽管如此，由于 SCF 方法能以低到中等计算成本给出可接受精度的化学预测，自洽场方法构成了大多数量子化学程序与计算的基石。许多 SCF 算法的形式计算量为 ${\cal{O}}({N^{4}})$，*即*，其计算量随体系规模 $N$ 的四次方增长。这比最便宜的传统相关方法的增长速度更慢（后者标度为 ${\cal{O}}({N^{5}})$ 或更差）；**Q-Chem** 中可用的算法进展可以在有利情形下将 SCF 成本降至 ${\cal{O}}({N})$，这一改进使得 SCF 方法可以应用于过去被认为超出 *ab initio*（从头算）量子化学范畴的分子。

**Q-Chem** 中当前可用的基态能量计算类型汇总于表 [4.1](#tab:calculations)。

| 计算类型 | $rem 变量 JOBTYPE |  |
| --- | --- | --- |
| 单点能（默认） | SINGLE_POINT 或 SP |  |
| 力（能量 + 梯度） | FORCE |  |
| 平衡结构搜索 | OPTIMIZATION 或 OPT |（第 9 章）|
| 过渡态结构搜索 | TS |（第 9 章）|
| 内禀反应路径 | RPATH |（第 9.7 节）|
| 势能面扫描 | PES_SCAN |（第 9.6 节）|
| 振动频率计算 | FREQUENCY 或 FREQ |（第 10.8 节）|
| 极化率与弛豫偶极矩 | POLARIZABILITY , DIPOLE |（第 10.13.2 节）|
| NMR 化学位移 | NMR |（第 10.11.2 节）|
| 间接核自旋–自旋耦合 | ISSC |（第 10.11.2 节）|
| 从头算分子动力学 | AIMD |（第 9.9 节）|
| 从头算路径积分 | PIMD , PIMC |（第 9.10 节）|
| BSSE（基组重叠误差，counterpoise）校正 | BSSE |（第 12.4 节）|
| 能量分解分析 | EDA |（第 12.5.3 节与第 12.6 节）|
| 对称匹配微扰理论 | XSAPT |（第 12.9 节与第 12.10 节）|

表 4.1：
**Q-Chem** 所要运行的计算类型由 *$rem* 变量 JOBTYPE 控制。
