---
title: "4.2.2 Hartree-Fock 理论"
---

## 4.2.2 Hartree-Fock 理论

(July 4, 2026)

与现代量子化学的许多基础理论一样，Hartree-Fock（HF）近似是在薛定谔方程发表后不久发展起来的，但在计算机出现之前，它一直停留在定性理论阶段。尽管 HF 近似通常只能给出定性化学精度，而非定量信息，并且总体上不如许多可用的密度泛函理论（Density Functional Theory, DFT）方法，但它仍是量子化学家工具箱中的一种有用工具。特别地，对于有机化学，HF 对分子结构的预测非常有用。

再次考虑 Roothaan-Hall 方程，即式 ([4.11](Ch4.S2.SS1.md#eq:Roothaan-Hall))，或 Pople-Nesbet 方程，即式 ([4.13](Ch4.S2.SS1.md#eq:Pople-Nesbet))，它们均可追溯到式 ([4.8](Ch4.S2.SS1.md#eq407))，其中有效势 $\upsilon_{\rm eff}$ 取决于所采用的自洽场（Self-Consistent Field, SCF）方法。在限制型 HF（Restricted HF, RHF）形式体系中，有效势可以写为

<a id="eq413"></a>

$$
\upsilon_{\rm eff}=\sum_{a}^{N/2}\bigl{[}{2\hat{J}_{a}(1)-\hat{K}_{a}(1)}\bigr{]}-\sum_{A=1}^{M}{\frac{Z_{A}}{r_{1A}}} \tag{4.15}
$$

其中库仑（Coulomb）算符与交换（exchange）算符定义为

<a id="eq414"></a>

$$
\hat{J}_{a}(1)=\int{\psi_{a}^{\ast}(2)\frac{1}{r_{12}}\psi_{a}(2)\;d{\rm{\bf r}}_{2}} \tag{4.16}
$$

以及

<a id="eq415"></a>

$$
\hat{K}_{a}(1)\psi_{i}(1)=\left[{\int{\psi_{a}^{\ast}(2)\frac{1}{r_{12}}\psi_{i}(2)\;d{\rm{\bf r}}_{2}}}\right]\psi_{a}(1) \tag{4.17}
$$

分别。通过引入原子轨道（Atomic Orbital, AO）基组（Basis Set），我们得到 Fock 矩阵元

<a id="eq416"></a>

$$
F_{\mu\nu}=H_{\mu\nu}^{\mathrm{core}}+J_{\mu\nu}-K_{\mu\nu} \tag{4.18}
$$

其中核心哈密顿（core Hamiltonian）矩阵元

<a id="eq417"></a>

$$
H_{\mu\nu}^{\mathrm{core}}=T_{\mu\nu}+V_{\mu\nu} \tag{4.19}
$$

由动能矩阵元

<a id="eq418"></a>

$$
T_{\mu\nu}=\int{\phi_{\mu}({\rm{\bf r}})\left(-\frac{1}{2}\hat{\nabla}^{2}\right)\phi_{\nu}({\rm{\bf r}})\;d{\rm{\bf r}}} \tag{4.20}
$$

和核吸引矩阵元

<a id="eq419"></a>

$$
V_{\mu\nu}=\int{\phi_{\mu}({\rm{\bf r}})\left(-\sum_{A}\frac{Z_{A}}{\left|{{\rm{\bf R}}_{A}-{\rm{\bf r}}}\right|}\right)\phi_{\nu}({\rm{\bf r}})\;d{\rm{\bf r}}} \tag{4.21}
$$

组成。库仑矩阵元与交换矩阵元由下式给出

<a id="eq420"></a>

$$
J_{\mu\nu}=\sum\limits_{\lambda\sigma}{P_{\lambda\sigma}\left({\mu\nu|\lambda\sigma}\right)} \tag{4.22}
$$

以及

<a id="eq421"></a>

$$
K_{\mu\nu}=\frac{1}{2}\sum\limits_{\lambda\sigma}{P_{\lambda\sigma}\left({\mu\lambda|\nu\sigma}\right)} \tag{4.23}
$$

分别，其中密度矩阵（density matrix）元为

<a id="eq:P(mu,nu)"></a>

$$
P_{\mu\nu}=2\sum\limits_{a=1}^{N/2}{C_{\mu a}C_{\nu a}} \tag{4.24}
$$

双电子积分（two-electron integrals）为

<a id="eq423"></a>

$$
\left({\mu\nu|\lambda\sigma}\right)=\int\int{\phi_{\mu}({\rm{\bf r}}_{1})\phi_{\nu}({\rm{\bf r}}_{1})\left({\frac{1}{r_{12}}}\right)\phi_{\lambda}({\rm{\bf r}}_{2})\phi_{\sigma}({\rm{\bf r}}_{\rm{\bf 2}})\;d{\rm{\bf r}}_{1}\;d{\rm{\bf r}}_{2}}\;. \tag{4.25}
$$

!!! note "注意"
    双电子积分的构建与利用是整个 SCF 方法性能的核心议题。一款新型量子化学软件程序中 SCF 方法的性能，只需考察其原子轨道积分包的实现质量即可快速估算。有关 **Q-Chem** 的 **AOInts** 积分包的详细信息，参见附录 [A](../app_a_aoints/app_AOINTS.md)。


将式 ([4.18](#eq416)) 中的矩阵元代回 Roothaan-Hall 方程，即式 ([4.11](Ch4.S2.SS1.md#eq:Roothaan-Hall))，并迭代直至达到自洽，即可得到 RHF 能量与波函数。另一种做法是采用非限制型（unrestricted）波函数形式，分别定义 $\alpha$ 和 $\beta$ 密度矩阵：

<a id="A3.S8.EGx2"></a>

$$
\displaystyle\begin{aligned} \displaystyle P_{\mu\nu}^{\alpha}&\displaystyle=\sum\limits_{a=1}^{n_{\alpha}}{C_{\mu a}^{\alpha}C_{\nu a}^{\alpha}}\\
\displaystyle P_{\mu\nu}^{\beta}&\displaystyle=\sum\limits_{a=1}^{n_{\beta}}{C_{\mu a}^{\beta}C_{\nu a}^{\beta}}\end{aligned} \tag{4.26}
$$

总电子密度矩阵为 $\mathbf{P}=\mathbf{P}^{\alpha}+\mathbf{P}^{\beta}$。非限制型 $\alpha$ Fock 矩阵

<a id="eq:F(mu,nu)"></a>

$$
F_{\mu\nu}^{\alpha}=H_{\mu\nu}^{\mathrm{core}}+J_{\mu\nu}-K_{\mu\nu}^{\alpha}\;, \tag{4.27}
$$

与限制型矩阵的差别仅在于交换贡献部分，其中 $\alpha$ 交换矩阵元由下式给出

<a id="eq426"></a>

$$
K_{\mu\nu}^{\alpha}=\sum\limits_{\lambda}^{N}{\sum\limits_{\sigma}^{N}{P_{\lambda\sigma}^{\alpha}\left({\mu\lambda|\nu\sigma}\right)}} \tag{4.28}
$$
