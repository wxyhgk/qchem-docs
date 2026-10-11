---
title: "6.20.1 简介与理论"
---

## 6.20.1 简介与理论

(July 4, 2026)

完全活性空间（Complete Active Space, CAS）方法是一族用于处理强关联体系的方法。在这类方法中，体系的一部分轨道和电子被标记为*活性（active）*空间，并在这个较小的活性空间内精确求解完整组态相互作用（Full Configuration Interaction, FCI）问题。其余的占据轨道被标记为*非活性（inactive）*，以平均场（mean-field）方式处理，而其余的空轨道则被标记为*虚（virtual）*轨道。在 CAS-CI 中，处理到此为止。而在 CASSCF 中，跨越这三个空间（非活性、活性和虚空间）的轨道会被进一步优化，以获得尽可能低的能量。换言之，CASSCF 问题就是要找到轨道希尔伯特空间（Hilbert space）的最优（按能量而言）划分。由于活性空间内所有可能组态对应的 Slater 行列式数目呈组合式增长，只要活性空间相对较小，该方法就可以用于研究中等规模的体系。事实上，对于含有 $M$ 个*空间（spatial）*轨道、$N_{\uparrow}$ 个上旋电子和 $N_{\downarrow}$ 个下旋电子的活性空间，可能的 Slater 行列式总数为：

<a id="A3.S8.EGx28"></a>
$$
\displaystyle N_{\text{total}} \tag{6.87}
$$

现代计算架构可以处理约 18 个电子处于 18 个轨道（$\approx 2\times 10^{9}$ 个行列式）的活性空间，但我们不建议在常规计算中使用如此大的活性空间。

**Q-Chem** 同样提供 CASSCF 计算的核梯度（nuclear gradients）。除了完整的 CAS 计算之外，还可以在指定的活性空间中进行任意阶截断的组态相互作用（CIS、CISD、CISDT 等）计算，并对轨道进行优化。

电子能量是 1-RDM（一阶约化密度矩阵，1-particle reduced density matrix）和 2-RDM 的精确泛函

<a id="eq:casscf:energy"></a>
$$
E=\frac{1}{2}\sum_{pqrs}\Gamma_{pqrs}g_{pqrs}+\sum_{pq}D_{pq}h_{pq}, \tag{6.88}
$$

给定 1-PDM 和 2-PDM，即可为该多组态自洽场（Multi-Configuration Self-Consistent Field, MCSCF）生成广义 Fock 矩阵。其推导及更多细节在 Helgaker、Jorgensen 和 Olsen 的著作中有清晰的描述，

 但这里对关键结果进行概要总结。在下文中，$m,n,p,q,\ldots$ 为一般指标，$i,j,k,\ldots$ 为非活性指标，$t,u,v,w,\ldots$ 为活性指标，$a,b,c,\ldots$ 为虚指标。

广义 Fock 矩阵定义为

<a id="A3.S8.EGx29"></a>
$$
\displaystyle F_{mn}=\sum_{q}D_{pq}h_{pq}+\sum_{qrs}\Gamma_{mqrs}g_{nqrs} \tag{6.89}
$$

其中 $h_{pq}$ 为单电子积分，$g_{nqrs}$ 为双电子积分，且所有指标遍历全部轨道类别（非活性、活性和虚轨道）。这个通常非对称的矩阵可以利用如下事实加以简化：当某些指标为非活性或虚指标时，密度矩阵的形式比指标为活性时要简单得多。当广义 Fock 矩阵的第一个指标为非活性、第二个指标为一般指标时：

<a id="A3.S8.EGx30"></a>
$$
\displaystyle F_{in}=2({}^{I}F_{ni}+{}^{A}F_{ni}) \tag{6.90}
$$

其中*非活性 Fock 矩阵*与*活性 Fock 矩阵*为

<a id="A3.S8.EGx31"></a>
$$
\displaystyle{}^{I}F_{mn} \tag{6.91}
$$

换言之，非活性 Fock 矩阵是仅使用非活性密度构造的 Fock 矩阵，而活性 Fock 矩阵则是由活性空间 1-PDM 构造的 J 矩阵与 K 矩阵之和。当第一个指标为活性、第二个指标为一般指标时，有

<a id="A3.S8.EGx32"></a>
$$
\displaystyle F_{tn}=\sum_{u}{}^{I}F_{nu}D_{vu}+Q_{tn} \tag{6.93}
$$

其中辅助的 Q 矩阵为

<a id="A3.S8.EGx33"></a>
$$
\displaystyle Q_{tm}=\sum_{u,v,w}\Gamma_{tuvw}g_{muvw} \tag{6.94}
$$

最后，若第一个指标为虚指标，则 $F_{an}=0$。广义 Fock 矩阵的这种表达形式非常有用，因为它只需要所有指标均为活性的密度矩阵，以及在分子轨道（MO）基下具有三个活性指标和一个一般指标的双电子积分，从而大大降低了 MO 积分变换的存储与计算开销。轨道梯度（orbital gradient）随由下式给出

<a id="A3.S8.EGx34"></a>
$$
\displaystyle\frac{\partial E}{\partial\Delta_{pq}}=2(F_{pq}-F_{qp}) \tag{6.95}
$$
