---
title: "4.2.2 Hartree-Fock Theory"
---

## 4.2.2 Hartree-Fock Theory

(July 4, 2026)

As with much of the theory underlying modern quantum chemistry, the
HF approximation was developed shortly after publication of the
Schrödinger equation, but remained a qualitative theory until the advent of
the computer. Although the HF approximation tends to yield qualitative chemical
accuracy, rather than quantitative information, and is generally inferior to
many of the DFT approaches available, it remains as a useful tool in the
quantum chemist’s toolkit. In particular, for organic chemistry, HF predictions
of molecular structure are very useful.

Consider once more the Roothaan-Hall equations, Eq. ([4.11](Ch4.S2.SS1.md#eq:Roothaan-Hall)), or the
Pople-Nesbet equations, Eq. ([4.13](Ch4.S2.SS1.md#eq:Pople-Nesbet)), which can be traced back to
Eq. ([4.8](Ch4.S2.SS1.md#eq407)), in which the effective potential
$\upsilon_{\rm eff}$ depends on the SCF methodology. In a restricted HF (RHF)
formalism, the effective potential can be written as

<a id="eq413"></a>
$$
\upsilon_{\rm eff}=\sum_{a}^{N/2}\bigl{[}{2\hat{J}_{a}(1)-\hat{K}_{a}(1)}\bigr{]}-\sum_{A=1}^{M}{\frac{Z_{A}}{r_{1A}}} \tag{4.15}
$$

where the Coulomb and exchange operators are defined as

<a id="eq414"></a>
$$
\hat{J}_{a}(1)=\int{\psi_{a}^{\ast}(2)\frac{1}{r_{12}}\psi_{a}(2)\;d{\rm{\bf r}}_{2}} \tag{4.16}
$$

and

<a id="eq415"></a>
$$
\hat{K}_{a}(1)\psi_{i}(1)=\left[{\int{\psi_{a}^{\ast}(2)\frac{1}{r_{12}}\psi_{i}(2)\;d{\rm{\bf r}}_{2}}}\right]\psi_{a}(1) \tag{4.17}
$$

respectively. By introducing an atomic orbital basis, we obtain Fock matrix elements

<a id="eq416"></a>
$$
F_{\mu\nu}=H_{\mu\nu}^{\mathrm{core}}+J_{\mu\nu}-K_{\mu\nu} \tag{4.18}
$$

where the core Hamiltonian matrix elements

<a id="eq417"></a>
$$
H_{\mu\nu}^{\mathrm{core}}=T_{\mu\nu}+V_{\mu\nu} \tag{4.19}
$$

consist of kinetic energy elements

<a id="eq418"></a>
$$
T_{\mu\nu}=\int{\phi_{\mu}({\rm{\bf r}})\left(-\frac{1}{2}\hat{\nabla}^{2}\right)\phi_{\nu}({\rm{\bf r}})\;d{\rm{\bf r}}} \tag{4.20}
$$

and nuclear attraction elements

<a id="eq419"></a>
$$
V_{\mu\nu}=\int{\phi_{\mu}({\rm{\bf r}})\left(-\sum_{A}\frac{Z_{A}}{\left|{{\rm{\bf R}}_{A}-{\rm{\bf r}}}\right|}\right)\phi_{\nu}({\rm{\bf r}})\;d{\rm{\bf r}}} \tag{4.21}
$$

The Coulomb and exchange elements are given by

<a id="eq420"></a>
$$
J_{\mu\nu}=\sum\limits_{\lambda\sigma}{P_{\lambda\sigma}\left({\mu\nu|\lambda\sigma}\right)} \tag{4.22}
$$

and

<a id="eq421"></a>
$$
K_{\mu\nu}=\frac{1}{2}\sum\limits_{\lambda\sigma}{P_{\lambda\sigma}\left({\mu\lambda|\nu\sigma}\right)} \tag{4.23}
$$

respectively, where the density matrix elements are

<a id="eq:P(mu,nu)"></a>
$$
P_{\mu\nu}=2\sum\limits_{a=1}^{N/2}{C_{\mu a}C_{\nu a}} \tag{4.24}
$$

and the two electron integrals are

<a id="eq423"></a>
$$
\left({\mu\nu|\lambda\sigma}\right)=\int\int{\phi_{\mu}({\rm{\bf r}}_{1})\phi_{\nu}({\rm{\bf r}}_{1})\left({\frac{1}{r_{12}}}\right)\phi_{\lambda}({\rm{\bf r}}_{2})\phi_{\sigma}({\rm{\bf r}}_{\rm{\bf 2}})\;d{\rm{\bf r}}_{1}\;d{\rm{\bf r}}_{2}}\;. \tag{4.25}
$$

**Note: 

The formation and utilization of two-electron integrals is a topic
central to the overall performance of SCF methodologies. The performance of the
SCF methods in new quantum chemistry software programs can be quickly estimated
simply by considering the quality of their atomic orbital integrals packages.
See Appendix [A](../app_a_aoints/app_AOINTS.md) for details of **Q-Chem**’s **AOInts** package.
**

Substituting the matrix element in Eq. ([4.18](#eq416)) back into the
Roothaan-Hall equations, Eq. ([4.11](Ch4.S2.SS1.md#eq:Roothaan-Hall)), and iterating until
self-consistency is achieved will yield the RHF energy and wave function.
Alternatively, one could have adopted the unrestricted form of the wave
function by defining separate $\alpha$ and $\beta$ density matrices:

<a id="A3.S8.EGx2"></a>
$$
\displaystyle\begin{aligned} \displaystyle P_{\mu\nu}^{\alpha}&\displaystyle=\sum\limits_{a=1}^{n_{\alpha}}{C_{\mu a}^{\alpha}C_{\nu a}^{\alpha}}\\
\displaystyle P_{\mu\nu}^{\beta}&\displaystyle=\sum\limits_{a=1}^{n_{\beta}}{C_{\mu a}^{\beta}C_{\nu a}^{\beta}}\end{aligned} \tag{4.26}
$$

The total electron density matrix $\mathbf{P}=\mathbf{P}^{\alpha}+\mathbf{P}^{\beta}$. The
unrestricted $\alpha$ Fock matrix,

<a id="eq:F(mu,nu)"></a>
$$
F_{\mu\nu}^{\alpha}=H_{\mu\nu}^{\mathrm{core}}+J_{\mu\nu}-K_{\mu\nu}^{\alpha}\;, \tag{4.27}
$$

differs from the restricted one only in the exchange contributions, where the
$\alpha$ exchange matrix elements are given by

<a id="eq426"></a>
$$
K_{\mu\nu}^{\alpha}=\sum\limits_{\lambda}^{N}{\sum\limits_{\sigma}^{N}{P_{\lambda\sigma}^{\alpha}\left({\mu\lambda|\nu\sigma}\right)}} \tag{4.28}
$$
