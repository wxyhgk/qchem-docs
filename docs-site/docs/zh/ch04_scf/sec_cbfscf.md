---
title: "4.9.5 使用复基函数的非厄米 SCF"
---

## 4.9.5 使用复基函数的非厄米 SCF

(July 4, 2026)

亚稳态电子态可以用一个复的 Siegert 能量来表征，

<a id="Ch4.E74"></a>

$$
E=E_{r}-i\Gamma/2, \tag{4.74}
$$

其中宽度 $\Gamma$ 与该态寿命的倒数成正比：$\Gamma=\hbar/\tau$。复坐标方法（complex coordinate methods）旨在将该复能量作为有效非厄米哈密顿量的本征值来计算。其中一种方法是复基函数（complex basis functions, CBFs）方法，即使用具有复指数的高斯函数作为基组，并配合对称（而非复共轭）内积，从而有效地构造出非厄米算符的有限基组表示。[[931]](../bib_references/bib.md#bib970)
 在衰减通道具有单电子特征的情形下（例如临时阴离子），平均场理论可以为多电子体系提供近似的 Siegert 能量。

最简单的此类近似是静态交换（static-exchange）近似。在该近似中，($N+1$) 电子态的 Siegert 能量是通过对角化由 $N$ 电子态密度所构建的 Fock 算符来计算的。[[1457]](../bib_references/bib.md#bib1525)
 该近似忽略了轨道弛豫效应，而轨道弛豫效应可以通过非厄米自洽场（non-Hermitian self-consistent-field, NH-SCF）程序来纳入。[[931]](../bib_references/bib.md#bib970)
 实际上，NH-SCF 能量泛函与全纯 Hartree-Fock（Holomorphic Hartree-Fock）能量泛函（式 [4.70](sec_HoloHF.md#eq:HoloHFEnergy)）相同，只是用途不同。使用复基函数（CBFs）的静态交换理论和 NH-SCF 理论在 **Q-Chem** 中均可用。复基组的指定方法在第 [8.7](../ch08_basis/sect_zbas.md) 节中描述。

COMPLEX_EXPONENTS

### `COMPLEX_EXPONENTS`

> **启用使用 CBFs 的非厄米计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 执行使用 CBFs 的非厄米计算
> * **建议**: 若希望进行使用 CBFs 的非厄米计算，则设为 TRUE。

COMPLEX_SPIN_STATE

### `COMPLEX_SPIN_STATE`

> **非厄米计算的自旋态**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * $2S+1$
>     * 一个自旋态
>     * $S$
> * **建议**: 无

COMPLEX_N_ELECTRON

### `COMPLEX_N_ELECTRON`

> **为非厄米计算添加电子数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * 在
>     * $N+n$
>     * 电子体系上执行非厄米计算
> * **建议**: 无

COMPLEX_STATIC_EXCHANGE

### `COMPLEX_STATIC_EXCHANGE`

> **执行 CBF 静态交换计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 执行静态交换计算
>     * FALSE
>     * 不执行静态交换计算
> * **建议**: 若希望进行静态交换计算，则设为 TRUE。

COMPLEX_SCF

### `COMPLEX_SCF`

> **执行使用 CBFs 的非厄米 SCF 计算**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 不执行 NH-SCF 计算
>     * 1
>     * 执行限制性（restricted）NH-SCF 计算
>     * 2
>     * 执行非限制性（unrestricted）NH-SCF 计算
>     * 3
>     * 执行开壳层限制性（restricted, open-shell）NH-SCF 计算
> * **建议**: 无

COMPLEX_METSCF

### `COMPLEX_METSCF`

> **指定 NH-SCF 求解器**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * 0
>     * Roothaan 迭代
>     * 1
>     * DIIS
>     * 3
>     * ADIIS
>     * 21
>     * Newton-MINRES
> * **建议**: 使用默认值（DIIS）。

COMPLEX_SCF_GUESS

### `COMPLEX_SCF_GUESS`

> **指定 NH-SCF 初始猜测**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 使用来自静态交换计算的猜测
>     * 1
>     * 读取实基组的 MO 系数
>     * 2
>     * 读取实基组的密度矩阵
>     * 1000
>     * 从先前的计算读取猜测
> * **建议**: 使用来自静态交换计算的猜测。注意，对于临时阴离子，这需要指定 COMPLEX_TARGET。

COMPLEX_TARGET

### `COMPLEX_TARGET`

> **指定临时阴离子中要被占据的轨道索引**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $n$
>     * 附加电子的轨道索引（从零开始）
> * **建议**: $n$ 应始终大于 $N_{\text{occ}}-1$。
