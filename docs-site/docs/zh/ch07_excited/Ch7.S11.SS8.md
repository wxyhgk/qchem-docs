---
title: "7.11.8 直接 RAS-nSF-IP/EA（librassf）"
---

## 7.11.8 直接 RAS-nSF-IP/EA（**librassf**）

（2026 年 7 月 4 日）

**librassf** 模块支持使用 Fock 空间组态相互作用（Fock space CI）方法进行 RAS-$n$SF-IP/EA 计算。
CAS-$n$SF-IP/EA 方法将非粒子数守恒算符与非自旋守恒算符相结合，用于描述具有
自旋简并与空间简并体系的性质。例如，CAS-1SF-IP 算符定义如下：

<a id="Ch7.E171"></a>

$$
|\Psi\rangle=\sum_{ij\bar{a}}c_{ij}^{\bar{a}}\hat{a}_{ij}^{\bar{a}}|\Psi^{\text{Ref}}\rangle \tag{7.171}
$$

**librassf** 模块也可以执行传统的自旋翻转（spin-flip）以及 IP/EA 计算。
此外还可以加入外部空穴激子和粒子激发（分别记为 RAS(h) 和 RAS(p)）；由于电子数
发生变化，这种轨道弛豫（orbital relaxation）对于 IP/EA 计算尤为重要。

我们的实现针对 alpha 与 beta 电子数的唯一性变化采用了显式表达式。这些方法
通过直接张量收缩（direct tensor contractions）而非 alpha 和 beta 行列式串
（strings）的方式得到了高效实现。该代码还允许用户选择适当的自旋翻转次数，
从而在活性空间（active space）较大时限制所考虑的行列式数目。

目前已实现的方案包括：CAS-1SF、RAS(h)-1SF、
RAS(p)-1SF、RAS(h,p)-1SF、CAS-2SF、CAS-IP、RAS(h)-IP、CAS-EA、RAS(p)-EA、
CAS-1SF-IP、RAS(h)-1SF-IP、CAS-1SF-EA 以及 RAS(p)-1SF-EA。
