---
title: "4.5.10 增强型 Roothaan-Hall 能量 DIIS（ADIIS）"
---

## 4.5.10 增强型 Roothaan-Hall 能量 DIIS（ADIIS）

（2026 年 7 月 4 日）

与 RCA/EDIIS 类似，[[186]](../bib_references/bib.md#bib182)

Hu 和 Yang 提出的 [[601]](../bib_references/bib.md#bib624) ADIIS 算法同样旨在
DIIS 初始迭代表现不佳的情况下加速 SCF 收敛。该算法同样涉及一种 Fock 矩阵外推格式：

<a id="eq:adiis_fock"></a>

$$
\tilde{\mathbf{F}}_{n+1}=\sum_{i=1}^{n}c_{i}\mathbf{F}_{i} \tag{4.42}
$$

其中 $\tilde{\mathbf{F}}_{n+1}$ 是待对角化以生成更新分子轨道（MO）与电子密度的外推 Fock 矩阵，$\mathbf{F}_{i}=\mathbf{F}[\mathbf{P}_{i}]$ 是由第 $i$ 次迭代的密度矩阵构造的 Fock 矩阵，而 $\{c_{i}\}$ 是外推系数，其通过对如下外推密度
$\tilde{\mathbf{P}}_{i+1}=\sum_{i=1}^{n}\mathbf{P}_{i}$ 的增强型 Roothaan-Hall（ARH）能量函数进行极小化而得到

<a id="A3.S8.EGx3"></a>

$$
\displaystyle f^{\mathrm{ADIIS}}(c_{1},\dots,c_{n})=E[\mathbf{P}_{n}]+\sum_{i=1}^{n}c_{i}(\mathbf{P}_{i}-\mathbf{P}_{n})\cdot\mathbf{F}_{n} \tag{4.43}
$$

同时需满足约束 $\sum_{i=1}^{n}c_{i}=1,c_{i}\geq 0$（对所有 $i$）。如原始文献所建议的，[[601]](../bib_references/bib.md#bib624)
 通过变量替换
（$c_{i}=t_{i}^{2}/\sum_{i}t_{i}^{2}$）将带约束优化转化为标准的无约束优化问题（后者可用 L-BFGS 等优化器求解）。
注意，虽然式 [4.42](#eq:adiis_fock) 和式 [4.43](#eq:adiis_obj) 中的求和从 1 到 $n$，但实际计算中
没有必要使用此前 SCF 循环中得到的所有 $\mathbf{P}_{i}$ 和 $\mathbf{F}_{i}$ 来进行外推。在 **Q-Chem** 的 ADIIS 实现中，
外推所使用的 $\mathbf{P}_{i}$ 与 $\mathbf{F}_{i}$ 数量最多为 6。

已知 ADIIS 算法在接近 SCF 收敛的区域效率会有所下降。因此，使用“ADIIS+DIIS”算法更为理想：当 SCF 误差低于某一阈值，或 ADIIS 迭代次数达到某个设定值时，即切换为 DIIS。这种混合算法可通过在 **Q-Chem** 中设置 “SCF_ALGORITHM
= ADIIS_DIIS” 来调用。已有结果表明，在单独使用 DIIS 无法收敛或收敛耗时过长的情况下，该算法能够显著加速收敛。[[601]](../bib_references/bib.md#bib624)

### `ADIIS_INNER_CONV`

> **ADIIS 内层循环（式 4.43 的 L-BFGS 优化）的收敛判据**
>
> * **类型**：`INTEGER`
> * **默认值**：`12`
> * **选项**：
>     * $n$
>     * 以 10
>     * ${}^{-n}$
>     * 作为 ADIIS 内层循环的收敛判据
> * **建议**：使用默认值

### `THRESH_ADIIS_SWITCH`

> **在 ADIIS-DIIS 计算中从 ADIIS 切换到 DIIS 的阈值**
>
> * **类型**：`INTEGER`
> * **默认值**：`3`
> * **选项**：
>     * $n$
>     * 当 SCF 误差低于
>     * $10^{-n}$
>     * 时，从 ADIIS 切换到 DIIS
> * **建议**：3 或 4 较为合适

### `MAX_ADIIS_CYCLES`

> **在 ADIIS-DIIS 计算中，切换到 DIIS 之前 ADIIS 循环的最大次数**
>
> * **类型**：`INTEGER`
> * **默认值**：`30`
> * **选项**：
>     * $N$
>     * 在切换到 DIIS 之前最多执行
>     * $N$
>     * 次 ADIIS 迭代
> * **建议**：使用默认值；通常而言，ADIIS 迭代次数过多并无益处

???+ example "示例 4.14：使用 ADIIS_DIIS 算法对 Cd(II)-咪唑配合物进行 B3LYP/3-21G 计算（当误差低于 10 ${}^{-3}$ 时
切换至 DIIS）。采用 SADMO 初猜。"
    ```qchem
    $molecule
    2 1
    Cd     0.000000     0.000000     0.000000
     N     0.000000     0.000000    -2.260001
     N    -0.685444     0.000000    -4.348035
     C     0.676053     0.000000    -4.385069
     C     1.085240     0.000000    -3.091231
     C    -1.044752     0.000000    -3.060220
     H     1.231530     0.000000    -5.300759
     H     2.088641     0.000000    -2.711077
     H    -2.068750     0.000000    -2.726515
     H    -1.313170     0.000000    -5.174718
    $end
    
    $rem
    METHOD          B3LYP
    BASIS           3-21G
    THRESH          14
    SCF_GUESS       SADMO
    SCF_ALGORITHM   ADIIS_DIIS
    SCF_CONVERGENCE 8
    INTEGRAL_SYMMETRY    FALSE
    POINT_GROUP_SYMMETRY FALSE
    $end
    ```
