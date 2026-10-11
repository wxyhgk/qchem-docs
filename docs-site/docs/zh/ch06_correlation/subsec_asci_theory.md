---
title: "6.22.2 理论"
---

## 6.22.2 理论

(July 4, 2026)

若波函数 $|\Psi\rangle=\displaystyle\sum\limits_{i}C_{i}|D_{i}\rangle$（其中 $|D_{i}\rangle$ 为系数为 $C_{i}$ 的 Slater 行列式）是哈密顿量的本征态，则有

<a id="Ch6.E104"></a>

$$
C_{i}=\frac{\sum_{j\neq i}H_{ij}C_{j}}{(H_{ii}-E)}\;, \tag{6.104}
$$

其中 $H_{ij}=\langle D_{i}|\mathbf{H}|D_{j}\rangle$ 是行列式 $i$ 与 $j$ 之间的哈密顿矩阵元，$E$ 是本征态 $|\Psi\rangle$ 的能量。这一精确关系可以推广为一个度量（metric），用于在组态相互作用（Configuration Interaction, CI）展开中，依据某个行列式 $|D_{i}\rangle$ 与近似试探波函数中其他行列式的连接方式，预测其预期权重。该度量同样被用于 Epstein-Nesbet 微扰理论（Perturbation theory, PT）中，作为一阶波函数里各行列式的系数。

在 ASCI 方法中，所有相对于试探波函数 $|\psi_{k}\rangle$ 中最重要行列式（按系数大小排序）为单激发或双激发的行列式 $|D_{i}\rangle$，都被赋予一个估计重要度 $A_{i}$，其定义为

<a id="Ch6.E105"></a>

$$
A_{i}=\frac{\sum_{|D_{j}\rangle\in|\psi_{k}\rangle}H_{ij}C_{j}}{(H_{ii}-E_{k})}\;, \tag{6.105}
$$

其中 $E_{k}$ 是试探波函数 $|\psi_{k}\rangle$ 的能量。搜索与筛选仅在 $|\psi_{k}\rangle$ 中前 $c$ 个行列式所连接的行列式张成的空间中进行，因为不重要的行列式不太可能成为某个高排名行列式的唯一生成源（sole generator），这种对搜索空间的剪枝可 greatly 加速算法。按 $A_{i}$ 大小排序、且与 $|\psi_{k}\rangle$ 相连的前 $t$ 个行列式被用于构造新的波函数 $|\psi^{k+1}\rangle$，方法是（在展开波函数基础上）通过在该 Hilbert 子空间内进行精确对角化得到。

完成若干轮 ASCI 循环后，波函数将包含完全组态相互作用（Full Configuration Interaction, FCI）波函数中所有（或几乎全部）权重最大的行列式，而未被包含的其余行列式权重应当很小。这些大量残余小权重行列式的效应，通过二阶 Epstein-Nesbet 微扰理论（PT2）进行估计。[[367]](../bib_references/bib.md#bib371)

这一最终的 PT2 修正可给出极为精确的结果——即使 ASCI 波函数仅包含 Hilbert 空间中极小的一部分，其能量也常常与绝对 FCI 能量相差不到 1 kcal/mol。[[1378]](../bib_references/bib.md#bib1439)

还可以将变分能量对 PT2 修正进行外推（外推至 PT2 修正为零的 FCI 极限），以生成更精确的估计值，并预测最终估计值的误差度量。事实上，已有研究表明，将选择组态相互作用（Selected Configuration Interaction, SCI）能量对 PT2 修正进行线性或二次拟合，可实现相当精确的外推。[[512]](../bib_references/bib.md#bib524)

在 ASCI 的情形下，我们观察到基本上是线性的行为。

ASCI 可以作为 CASSCF 计算中的 full-CI 求解器，从而将 CASSCF 推广到约 $\approx 50$ 个电子在 $\approx 50$ 个轨道中的活性空间。由此得到的方法称为 ASCI-SCF。[[807]](../bib_references/bib.md#bib844)

关于 CASSCF 作业控制的细节，参见第 [6.20](sec_casscf.md) 节。
