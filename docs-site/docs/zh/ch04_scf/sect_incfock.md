---
title: "4.6.4 增量式与可变阈值 Fock 矩阵构建"
---

## 4.6.4 增量式与可变阈值 Fock 矩阵构建

(July 4, 2026)

在自洽场（SCF）的前几个循环中使用可变积分阈值，其合理性在于这些循环中的分子轨道（MO）系数通常质量较差。在 **Q-Chem** 中，第一次迭代的积分以 $10^{-6}$ 的阈值进行计算（针对预期最终积分阈值大于或等于 $10^{-6}$ 的情况），以确保第一次迭代的误差完全来源于较差的 MO 初猜。此后，所使用的积分阈值按下式计算

<a id="eq441"></a>
$$
t=10^{-\mathrm{VARTHRESH}}\times(\text{DIIS error}) \tag{4.48}
$$

其中 DIIS error 是由上一循环计算得到的误差，VARTHRESH 是由程序设置的（默认的）可变阈值，$t$ 是用于积分评估的临时阈值。每个循环都需要重新计算所有积分。可变积分阈值流程在早期 SCF 循环中影响最大。

在增量式 Fock 矩阵构建中，[[41]](../bib_references/bib.md#bib25)
$\mathbf{F}$ 按如下递归方式计算

<a id="eq442"></a>
$$
{\rm{\bf F}}^{\rm{\bf m}}={\rm{\bf F}}^{{\rm{\bf m}}-{\rm{\bf 1}}}+\Delta{\rm{\bf J}}^{{\rm{\bf m}}-{\rm{\bf 1}}}-\frac{1}{2}\Delta{\rm{\bf K}}^{{\rm{\bf m}}-{\rm{\bf 1}}} \tag{4.49}
$$

其中 $m$ 为 SCF 循环序号，而 $\Delta$**J${}^{m}$** 和 $\Delta$**K${}^{m}$** 使用差密度矩阵计算

<a id="eq443"></a>
$$
\Delta{\rm{\bf P}}^{\rm{\bf m}}={\rm{\bf P}}^{\rm{\bf m}}-{\rm{\bf P}}^{{\rm{\bf m}}-{\rm{\bf 1}}} \tag{4.50}
$$

利用 Schwartz 积分判别法和差密度矩阵的元素，**Q-Chem** 能够在每次迭代时确定哪些电子排斥积分（ERI）是必需的，并在必要时重新计算它们。随着 SCF 接近收敛，$\Delta\mathbf{P}^{m}$ 变得稀疏，需要重新计算的 ERI 数量急剧下降，从而为用户节省大量计算时间。

增量式 Fock 矩阵构建和可变阈值仅在使用直接 SCF（direct SCF）算法进行计算时才会启用，二者是相辅相成的算法。这些选项由以下输入参数控制，这些参数仅用于直接 SCF 计算。

INCFOCK

### `INCFOCK`

> **在此迭代次数之后启动增量式 Fock 矩阵算法**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **可选值**:
>     * 用户自定义（设为 0 则关闭 INCFOCK）
> * **建议**: 可能需要先允许进行若干次迭代后再开启 INCFOCK。

RESET_INCFOCK

### `RESET_INCFOCK`

> **在此迭代次数之后重置增量式 Fock 矩阵算法**
>
> * **类型**: `INTEGER`
> * **默认值**: `15`
> * **可选值**:
>     * 用户自定义（设为 0 则关闭 RESET_INCFOCK）

VARTHRESH

### `VARTHRESH`

> **控制临时积分截断阈值，$t=10^{-\mathrm{VARTHRESH}}\times(\text{DIIS error})$**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $n$
>     * 用户自定义阈值
> * **建议**: 3 被认为是一个实用的取值，可以略微加速 SCF 的评估。

???+ example "示例 4.20: 大型单点能计算的 Q-Chem 输入。该示例适用于中等大小的分子；但对于真正大规模的计算，CFMM 和 LinK 算法的效率要高得多。"
    ```qchem
    $comment
       HF/3-21G single point calculation on a large molecule
       read in the molecular coordinates from file
    $end
    
    $molecule
       read base_pair.inp
    $end
    
    $rem
       METHOD          HF      Hartree-Fock
       BASIS           3-21G   Basis set
       INCFOCK         5       Incremental Fock after 5 cycles
       VARTHRESH       3       1.0d-03 variable threshold
       MAX_SCF_CYCLES  100
    $end
    ```
