---
title: "9.8.1 非绝热耦合"
---

## 9.8.1 非绝热耦合

（2026 年 7 月 4 日）

锥形 intersections（conical intersections，CI）是 Born-Oppenheimer 势能面之间的简并点，它们促进了激发态之间的非绝热跃迁，*即*（*i.e.*）内转换（internal conversion）和系间窜越（intersystem crossing）过程，这两类过程都代表着 Born-Oppenheimer 近似的失效。[[916]](../bib_references/bib.md#bib952)

尽管两个以上电子态之间的同时相交也是可能的，[[916]](../bib_references/bib.md#bib952)
 但为简便起见，我们考虑两态情形，并令

<a id="eq:H_2x2"></a>

$$
\mathbf{H}=\left(\begin{array}[]{cc}H_{JJ}(\mathbf{R})&H_{JK}(\mathbf{R})\\
H_{JK}^{\ast}(\mathbf{R})&H_{KK}(\mathbf{R})\\
\end{array}\right)\;. \tag{9.48}
$$

表示振动（vibrational）＋电子（electronic）哈密顿量 [式 ([4.2](../ch04_scf/Ch4.S2.SS1.md#eq:Hamiltonian))] 在由两个电子态 $J$ 和 $K$ 构成的基组下的矩阵表示。（电子自由度在此表达式中已被积分掉，$\mathbf{R}$ 表示剩余的核坐标。）根据定义，Born-Oppenheimer 态就是在特定分子几何构型 $\mathbf{R}$ 下将 $\mathbf{H}$ 对角化所得的态，因此若要在 Born-Oppenheimer 表象中获得简并，必须同时满足两个条件：$H_{JJ}=H_{KK}$ 且 $H_{JK}=0$。由此，两个 Born-Oppenheimer 势能面之间的简并存在于维度为 $N_{\rm int}-2$ 的子空间中，其中 $N_{\rm int}=3N_{\rm atoms}-6$ 是内部（振动）自由度的数目（假设分子为非线性）。这个 ($N_{\rm int}-2$) 维子空间被称为*接缝空间（seam space）*，因为两个态在该空间内处处简并。在剩下的两个自由度（称为*分支空间（branching space）*）中，Born-Oppenheimer 势能面之间的简并会被无穷小位移所解除，在三维图像中该情形形似围绕交点的双锥，因此得名*锥形交叉（conical intersection）*。

分支空间由一对矢量 $\mathbf{g}_{JK}$ 和 $\mathbf{h}_{JK}$ 所张成的空间定义。前者 simply 是所讨论的两个态的梯度矢量之差，

<a id="eq:gJK"></a>

$$
\mathbf{g}_{JK}=\frac{\partial E_{J}}{\partial\textbf{R}}-\frac{\partial E_{K}}{\partial\textbf{R}}\;, \tag{9.49}
$$

在任何具备解析能量梯度（analytic energy gradients）的理论方法下都易于计算（若不具备，则可通过有限差分求得，只是不那么方便！）。而*非绝热耦合矢量（nonadiabatic coupling vector）* $\mathbf{h}_{JK}$ 的定义则更为复杂，且无法直接通过有限差分计算得到：

<a id="eq:hJK"></a>

$$
\mathbf{h}_{JK}=\left\langle\Psi_{J}\left|\left(\partial\hat{H}/\partial\mathbf{R}\right)\right|\Psi_{K}\right\rangle\;. \tag{9.50}
$$

它与*导数耦合（derivative coupling）*矢量密切相关

<a id="eq:dJK"></a>

$$
\mathbf{d}_{JK}=\bigl{\langle}\Psi_{J}\bigl{|}\bigl{(}\partial/\partial\mathbf{R}\bigr{)}\bigr{|}\Psi_{K}\bigr{\rangle}=\frac{\mathbf{h}_{JK}}{E_{J}-E_{K}}\;. \tag{9.51}
$$

$\mathbf{d}_{JK}$ 的后一表达式表明，在势能面上两个态接近简并的区域，态之间的耦合会变得很大。矢量 $\mathbf{g}_{JK}$ 和 $\mathbf{h}_{JK}$ 的相对取向与大小决定了交叉点附近的形貌（topography），*即*（*i.e.*）该交叉是“尖峰型（peaked）”还是“斜坡型（sloped）”；[[54]](../bib_references/bib.md#bib37)

可参阅文献 [[565]](../bib_references/bib.md#bib577)
 中的教学性综述。

计算非绝热耦合 $\mathbf{d}_{JK}$ 的算法在量子化学程序中并不普遍可用，但得益于 Herbert 与 Subotnik 课题组的努力，**Q-Chem** 已提供支持，前提是波函数 $\Psi_{J}$ 和 $\Psi_{K}$ 及相应的电子能量 $E_{J}$ 和 $E_{K}$ 是在 CIS 或含时密度泛函理论（Time-Dependent Density Functional Theory, TDDFT）级别[[378]](../bib_references/bib.md#bib383)
 或相应的自旋反转（spin-flip, SF）理论方法（SF-CIS 或 SF-TDDFT）级别下计算的。自旋反转方法的意义尤为重大。[[1547]](../bib_references/bib.md#bib1613)

只有该方法——而非传统的自旋守恒（spin-conserving）CIS 或 TDDFT——才能给出涉及基态的锥形交叉周围正确的形貌拓扑。

为理解其原因，假设式 ([9.48](#eq:H_2x2)) 中的 $J$ 表示基态；为明确起见记作 $J=0$。在线性响应理论（TDDFT）中，或者在 CIS 中（由于 Brillouin 定理），参考态（基态）与所有激发态之间的耦合矩阵元恒等地为零，因此 $H_{0K}(\mathbf{R})\equiv 0$。这意味着获得简并只需满足一个条件，于是对于任何涉及基态的锥形交叉，分支空间是一维而非二维的。[[806]](../bib_references/bib.md#bib839)

（对于两个激发态之间的交叉，其形貌拓扑应当是正确的。）然而在自旋反转方法中，参考态与目标态具有不同的自旋多重度；若目标态的自旋量子数为 $S$，则参考态的自旋为 $S+1$。其效果是：所关心的基态（自旋 $S$）被当作一种激发来处理，从而与相同自旋的激发态处于更为对等的地位，从根本上解决了锥形交叉周围的形貌拓扑问题。[[1547]](../bib_references/bib.md#bib1613)

这对向基态内转换的模拟会产生影响，例如在常规 TDDFT 中，S${}_{1}$/S${}_{0}$ 交叉周围势能面的畸变可能显著影响 S${}_{1}$ 的寿命。[[1550]](../bib_references/bib.md#bib1617)

CIS 和 TDDFT 均可获得非绝热（导数）耦合。CIS 的非绝热耦合可通过对波函数关于核位置直接求导得到。[[378]](../bib_references/bib.md#bib383)

对于 TDDFT，可采用同样的程序计算近似的非绝热耦合，此即所谓的“伪波函数（pseudo-wave function）”方法。[[1030]](../bib_references/bib.md#bib1071)

由二阶响应理论（quadratic response theory）导出的、在形式上更为严格的 TDDFT 非绝热耦合同样可用，但存在某些不受欢迎的偶然奇点：若式 ([9.50](#eq:hJK)) 中两个态 $J$ 和 $K$ 的能量差 $|E_{J}-E_{K}|$ 与某个第三态 $I$ 的激发能 $\omega_{I}=E_{I}-E_{0}$ 准简并（quasi-degenerate），就会出现这种奇点。[[1548]](../bib_references/bib.md#bib1614)
 因此，用 TDDFT 计算非绝热耦合时推荐使用伪波函数方法；而在自旋反转情形下，伪波函数方法与（原文如此）伪波函数方法是严格等价的，且不存在奇点。[[1548]](../bib_references/bib.md#bib1614)

最后需要指出，越来越多的证据表明，当使用含有约 50% Hartree-Fock 交换的泛函时，SF-TDDFT 计算最为准确，[[1239]](../bib_references/bib.md#bib1294)

许多采用该方法的研究都使用了 BH&HLYP 泛函；综述可参考文献 [[565]](../bib_references/bib.md#bib577)
 和 

。BH&H-LYP 泛函将 LYP 关联泛函与 Becke 的“半与半（half and half）”交换泛函相结合。[[484]](../bib_references/bib.md#bib496)

在 **Q-Chem** 中，通过设置 METHOD = BHHLYP 即可选用该泛函。
