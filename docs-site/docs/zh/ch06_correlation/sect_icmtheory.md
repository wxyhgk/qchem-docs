---
title: "6.21.2 理论"
---

## 6.21.2 理论

（2026 年 7 月 4 日）

iFCI 通过如下形式的 $n$ 体展开（$n$-body expansion）来获取电子能量：

<a id="eqn:mbe"></a>

$$
E=E_{\mathrm{ref}}+E_{C}=E_{\mathrm{ref}}+\sum_{i}\epsilon_{i}+\sum_{j<i}\epsilon_{ij}+\sum_{k<j<i}\epsilon_{ijk}+\cdots \tag{6.96}
$$

其中每个 $\epsilon_{X}$ 项表示一个关联能增量（increment of correlation energy），而 $i,j,k$ 指展开中的各个体（body）。增量关联能定义为

<a id="A3.S8.EGx35"></a>

$$
\displaystyle\epsilon_{i} \tag{6.97}
$$

其中 $n>1$ 的项会减去低阶增量以避免重复计数（double counting）。这些项表示在其余 $2(N-n)$ 个电子的平均场中，由 $2n$ 个电子对关联能作出的 $n$ 体贡献，其中每个 $\epsilon_{X}$ 值通过对 $N_{v}+n$ 个轨道中的 $2n$ 个电子求解 CAS-CI（活性空间组态相互作用）来计算。例如，$n=1$ 时执行 CAS($2,N_{v}+1$)-CI 以给出 $E_{C}(i)=E(\mathrm{CAS}(2,N_{v}+1))$ 的值。对更高的 $n$ 依此类推，CAS($2n,N_{v}+n$)-CI 给出每个 $E_{C}(X)$。

求解每个 CAS-CI 哈密顿量时采用热浴组态相互作用（Heat-bath CI, HBCI），按照与 CI 波函数耦合的行列式 $j$（形如 $|H_{ij}c_{i}|>\varepsilon_{i}$）执行选择性 CI（selected CI）计算，其中 $\varepsilon_{i}$ 是能量截断值，$c_{i}$ 是 HBCI 子空间中的行列式。

增量项的截断通过考虑自然轨道（natural orbital, NO）占据数截断 $\eta^{(m)}$ 来完成，其中

<a id="A3.S8.EGx36"></a>

$$
\displaystyle\epsilon_{i}^{(m)} \tag{6.100}
$$

这样只纳入具有足够大 NO 本征值的虚轨道，从而缩小虚空间（virtual space）的规模。当满足

<a id="eqn:ifcizeta"></a>

$$
\zeta>|\epsilon^{(m+1)}-\epsilon^{m}| \tag{6.102}
$$

时，每个 iFCI 增量即达到收敛，其单位为 $10^{-\zeta}$ E${}_{\mathrm{h}}$。对于 $n\geq 3$ 的项，还可以利用参数 $\zeta$ 与形如下的筛查截断（screening cutoff）$\mathcal{C}_{n}$ 进行进一步截断：

<a id="eqn:ifcicutoff"></a>

$$
\mathcal{C}_{n}=10^{-\zeta}\times\mathcal{S}_{n} \tag{6.103}
$$

其中 $\mathcal{C}_{n}$ 的单位为 E${}_{\mathrm{h}}$，$\mathcal{S}_{n}$ 为一个标量。该筛查通过选取高于 $\mathcal{C}_{n}$ 的 $n-1$ 体关联能贡献来实现。更多细节参见文献 [[1148]](../bib_references/bib.md#bib1200)。$\mathcal{S}_{n}$ 是输入中的一个参数。

iFCI 需要一个高自旋完美配对（high-spin perfect pairing, PP）参考态，其中自然轨道定域化为局域成键-反键轨道对，即双电子配对基（geminals）。
