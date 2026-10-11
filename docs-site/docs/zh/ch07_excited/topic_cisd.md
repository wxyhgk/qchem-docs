---
title: "7.8.2 CIS(D) 理论"
---

## 7.8.2 CIS(D) 理论

(July 4, 2026)

CIS(D) 激发态计算方法是在单激发组态相互作用（CIS）参考态的基础上，对计算代价高昂的 CCSD 方法所作的二阶微扰近似。截断至单、双激发的耦合簇（coupled-cluster）波函数，是单替换与双替换算符的指数算符作用在 Hartree-Fock 行列式上的结果：

<a id="eq614"></a>

$$
\left|\Psi\right\rangle=\exp\left({T_{1}+T_{2}}\right)\left|{\Psi_{0}}\right\rangle \tag{7.82}
$$

求解单激发与双激发振幅需要解如下两个方程

<a id="eq615"></a>

$$
\left\langle{\Psi_{i}^{a}}\right|H-E\left|{\left({1+T_{1}+T_{2}+\frac{1}{2}T_{1}^{2}+T_{1}T_{2}+\frac{1}{3!}T_{1}^{3}}\right)\Psi_{0}}\right\rangle=0 \tag{7.83}
$$

以及

<a id="eq616"></a>

$$
\left\langle{\Psi_{ij}^{ab}}\right|H-E\left|{\left({1+T_{1}+T_{2}+\frac{1}{2}T_{1}^{2}+T_{1}T_{2}+\frac{1}{3!}T_{1}^{3}+\frac{1}{2}T_{2}^{2}+\frac{1}{2}T_{1}^{2}T_{2}+\frac{1}{4!}T_{1}^{4}}\right)\Psi_{0}}\right\rangle=0 \tag{7.84}
$$

由此得到 CCSD 激发态方程。这些方程可以写成

<a id="eq617"></a>

$$
\left\langle{\Psi_{i}^{a}}\right|H-E\left|{\left({U_{1}+U_{2}+T_{1}U_{1}+T_{1}U_{2}+U_{1}T_{2}+\frac{1}{2}T_{1}^{2}U_{1}}\right)\Psi_{0}}\right\rangle=\omega b_{i}^{a} \tag{7.85}
$$

以及

<a id="eq618"></a>

$$
\begin{array}[]{r}\left\langle{\Psi_{i}^{a}}\right|H-E\left|{\left({U_{1}+U_{2}+T_{1}U_{1}+T_{1}U_{2}+U_{1}T_{2}+\frac{1}{2}T_{1}^{2}U_{1}}\right.}\right.+T_{2}U_{2}\\
\left.{+\frac{1}{2}T_{1}^{2}U_{2}+T_{1}T_{2}U_{1}+\frac{1}{3!}T_{1}^{3}U_{1}}\right|\left.{\Psi_{0}}\right\rangle=\omega b_{ij}^{ab}\\
\end{array} \tag{7.86}
$$

这是一个关于跃迁振幅（$\mathbf{b}$ 向量）的本征方程 $\mathbf{A}\mathbf{b}=\omega\mathbf{b}$，这些跃迁振幅也包含在 $U$ 算符之中。

对 CCSD 本征方程作二阶近似，可得到激发能的二阶贡献，其形式可写为

<a id="eq619"></a>

$$
\omega^{(2)}=\mathbf{b}^{(0)^{\mathbf{t}}}{\rm{\bf A}}^{(1)}\mathbf{b}^{(1)}+\mathbf{b}^{(0)^{\mathbf{t}}}{\rm{\bf A}}^{(2)}\mathbf{b}^{(0)} \tag{7.87}
$$

或者写成另一种等价形式

<a id="eq620"></a>

$$
\omega^{(2)}=\omega^{\mathrm{CIS(D)}}=E^{\mathrm{CIS(D)}}-E^{\mathrm{MP2}} \tag{7.88}
$$

其中

<a id="eq621"></a>

$$
E^{\mathrm{CIS(D)}}=\left\langle{\Psi^{\mathrm{CIS}}}\right|V\left|{U_{2}\Psi^{\mathrm{HF}}}\right\rangle+\left\langle{\Psi^{\mathrm{CIS}}}\right|V\left|{T_{2}U_{1}\Psi^{\mathrm{{HF}}}}\right\rangle \tag{7.89}
$$

以及

<a id="eq622"></a>

$$
E^{\mathrm{MP2}}=\left\langle{\Psi^{\mathrm{HF}}}\right|V\left|{T_{2}\Psi^{\mathrm{HF}}}\right\rangle \tag{7.90}
$$

CIS(D) 计算的输出除了经过 CIS(D) 修正的激发能本身之外，还包含许多有用的信息。CIS(D) 能量的稳定性通过一个称为"theta 诊断量"（theta diagnostic）[[1031]](../bib_references/bib.md#bib1074)的指标来检验。该 theta 诊断量计算一个混合角，用以度量电子关联导致所计算的每两个 CIS 态之间发生耦合的程度。最极端的情形是混合角达到 $45^{\circ}$，这表明初始 CIS 态的有效性已被破坏，其后的任何修正也就失去了意义。反之，若混合角很小，仅在一度左右，则表明计算结果是可靠的。该程序可以报告每个态相对于所有其他已计算态的最大混合角。
