---
title: "7.11.3 RAS-CI 的二阶微扰修正"
---

## 7.11.3 RAS-CI 的二阶微扰修正

（2026 年 7 月 4 日）

一般来说，在 $hole$ 与 $particle$ 近似下的 RAS-CI 方法族无法捕获以化学精度计算相对能量所需的动态相关能。缺失的相关能可以在 RAS-CI 波函数的基础上通过多参考微扰理论（Multi-Reference Perturbation Theory, MRPT）加以补充。[[210]](../bib_references/bib.md#bib204)
 二阶能量修正，*即* RASCI(2)，可以表示为：

<a id="eqRASCI2"></a>
$$
E^{(2)}=-\sum_{k}\frac{|\langle k|\hat{H}|0\rangle|^{2}}{E_{k}-E_{0}+\epsilon} \tag{7.165}
$$

其中 $0$ 表示零级空间，$\{|k\rangle\}$ 为其互补的行列式集合。在 MRPT 中，激发能 $\{E_{k}\}$ 并没有天然唯一的选择，RASCI(2) 方法提供了两种不同的模型，即 Davidson-Kapuy 分割或 Epstein-Nesbet 分割。与许多二阶 MRPT 修正中的常见做法一样，公式 ([7.165](#eqRASCI2)) 中的分母能量差可通过参数 $\epsilon$ 进行能级平移（level shift）。
