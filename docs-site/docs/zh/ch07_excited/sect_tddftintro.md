---
title: "7.3.1 简要介绍"
---

## 7.3.1 简要介绍

(July 4, 2026)

激发态可以通过密度泛函理论（Density Functional Theory, DFT）的线性响应
（linear response）[[351]](../bib_references/bib.md#bib357)
来获得，

出于历史原因，该方法被称为“含时”（time-dependent，TD-）DFT。

不要将其与第 [7.4](sec_TDKS.md) 节中所讨论的显式含时方法相混淆，
不过线性响应 DFT 几乎被普遍称为 TDDFT，我们也将采用这一术语。
该方法计算的是基态密度对随时间变化的外加电场的响应中的极点。
这些极点即为玻尔频率（Bohr frequencies），换言之也就是激发能。
从操作上看，这需要求解一个本征方程

<a id="eq:TDDFT"></a>

$$
\left(\begin{array}[]{cc}\mathbf{A}&\mathbf{B}\\
\mathbf{B}^{\dagger}&\mathbf{A}^{\dagger}\\
\end{array}\right)\left(\begin{array}[]{c}\mathbf{x}\\
\mathbf{y}\end{array}\right)=\omega\left(\begin{array}[]{cc}\mathbf{-1}&\mathbf{0}\\
\mathbf{0}&\mathbf{1}\\
\end{array}\right)\left(\begin{array}[]{c}\mathbf{x}\\
\mathbf{y}\end{array}\right) \tag{7.15}
$$

其中矩阵 $\mathbf{A}$ 的元素与 CIS 级别中所使用的元素类似（见式 ([7.11](subsec_CIS.md#eq:orbital-Hessian))），
但附加了交换-关联（exchange-correlation）修正。

矩阵 $\mathbf{B}$ 的元素与之类似。
式 ([7.15](#eq:TDDFT)) 通过迭代方式求解最低的若干激发能 $\omega$。
或者，也可以采用 Tamm-Dancoff 近似（TDA），
即忽略“退激发”（de-excitation）振幅 $\mathbf{Y}$。[[580]](../bib_references/bib.md#bib602)

在这种情况下，不需要 $\mathbf{B}$ 矩阵，
式 ([7.15](#eq:TDDFT)) 简化为一个类似于 CIS 的方程 $\mathbf{Ax}=\omega\mathbf{x}$。

TDDFT 之所以流行，是因为其计算开销与简单的 CIS 方法大致相当，
但该方法隐式地包含了差异电子关联（differential electron correlation）效应的描述。
建议仅将 TDDFT 用于低于分子第一电离势的低能价激发态，

或者更保守地说，用于低于第一里德堡（Rydberg）态的激发态；
在这类情形下，相对于 CIS，价激发能通常会有显著改善，
对许多泛函而言精度可达 $\sim 0.3$ eV。[[770]](../bib_references/bib.md#bib803)
完整 TDDFT 以及 TDA 框架下的核梯度计算均已实现。[[838]](../bib_references/bib.md#bib872)

标准 TDDFT 同样无法很好地描述静态关联（static correlation）效应
（参见第 [6.14](../ch06_correlation/sect_ccactive.md) 节），
因为它基于 Kohn-Sham 轨道的单一组态参考。
为解决这一问题，人们发展了一种称为自旋翻转（spin-flip，SF）TDDFT 的变体方法。[[1239]](../bib_references/bib.md#bib1294)

SF-TDDFT 与标准 TDDFT 的不同之处有两点：

- 对具有偶数（奇数）个电子的体系，参考态为高自旋三重态（四重态）；
- 在激发过程中，一个电子从 $\alpha$ Kohn–Sham 轨道自旋翻转至 $\beta$ 轨道。

SF-TDDFT 既能描述基态，也能描述若干低能激发态，
并已被应用于键断裂过程，以及具有简并或近简并前线轨道的双自由基与三自由基体系。
SF-DFT 的不同实现方式在第 [7.3.4](sect_sftddft.md) 节中描述。
