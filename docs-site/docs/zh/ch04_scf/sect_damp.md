---
title: "4.5.4 阻尼"
---

## 4.5.4 阻尼（Damping）

(July 4, 2026)

damping

阻尼可能是最古老的 SCF 加速方案，最初由 Hartree 在用量子力学研究原子结构的早期阶段提出。

在这一简单的方案中，当前 SCF 迭代的密度矩阵（或 Fock 矩阵）与上一次迭代的密度矩阵进行线性混合，生成一个阻尼密度矩阵，作为下一次 SCF 迭代的输入：

<a id="Ch4.E36"></a>

$$
P_{n}^{\text{damped}}=(1-\alpha)P_{n}+\alpha P_{n-1}, \tag{4.36}
$$

其中 $\alpha$ 是混合因子，满足 $0\leqslant\alpha\leqslant 1$。在 SCF 计算过程中，如果密度矩阵在相邻迭代之间发生剧烈变化（通常发生在 SCF 过程的早期阶段），总能量和占据分子轨道也会强烈波动，这可能导致 SCF 收敛缓慢甚至发散。在这种情况下，将密度（或 Fock）矩阵与上一次迭代中的对应矩阵进行混合，可以减弱（阻尼）能量和分子轨道的波动，从而稳定 SCF 过程。另一方面，如果 SCF 过程平滑且快速地收敛，施加阻尼只会减慢其收敛速度。因此，阻尼很少在整个 SCF 过程中单独使用，通常只在 SCF 过程的早期阶段启用，之后再关闭。

在 **Q-Chem** 中，密度矩阵阻尼作为一种处理困难 SCF 案例的选项（DAMP 算法）提供（仅限 RHF 和 UHF）。在实际计算中，阻尼常常与 DIIS 和 GDM 结合使用（DP_DIIS 和 DP_GDM 算法）。要启用阻尼，需将 *$rem* 变量 SCF_ALGORITHM 设置为 DAMP、DP_DIIS 或 DP_GDM。其他相关的 *$rem* 变量如下所示：

### `NDAMP`

> **确定混合系数。$\alpha$ = /100。**
>
> * **类型**: `INTEGER`
> * **默认值**: `75`
> * **选项**:
>     * 用户自定义。0 到 100 之间的整数。
> * **建议**: 如果 SCF 过程中出现强烈波动，则增大该值。

### `MAX_DP_CYCLES`

> **当 SCF_ALGORITHM = DP_DIIS 和 DP_GDM 时，使用阻尼的 SCF 迭代的最大次数。另见 THRESH_DP_SWITCH 。**
>
> * **类型**: `INTEGER`
> * **默认值**: `3`
> * **选项**:
>     * `1`: 仅对单个 SCF 步施加阻尼，其余 SCF 步不使用阻尼。
>     * $n$
>     * $n$: 在关闭阻尼之前，使用阻尼的 SCF 迭代次数。
> * **建议**: 如果在关闭阻尼后仍然持续出现强烈波动，则增大该数值。

### `THRESH_DP_SWITCH`

> **当 SCF_ALGORITHM 设置为 DP_DIIS 或 DP_GDM 时，关闭阻尼的 SCF 迭代阈值是 $10^{-\mbox{{\small THRESH\_DP\_SWITCH}}}$。另见 MAX_DP_CYCLES 。**
>
> * **类型**: `INTEGER`
> * **默认值**: `2`
> * **选项**:
>     * 用户自定义。
> * **建议**: 无

???+ example "示例 4.8：水阳离子的 UKS 计算输入，在 SCF 过程早期阶段使用阻尼，之后使用 DIIS。"
    ```qchem
    $molecule
      1 2
       O    1.9158048   -5.3106212    3.9451654
       H    2.8858048   -5.3106212    3.9451654
       H    1.5924750   -5.6945720    3.1151415
    $end
    
    $rem
       METHOD             B3LYP
       BASIS              3-21G
       SCF_ALGORITHM      DP_DIIS
       THRESH_DP_SWITCH   3
       MAX_DP_CYCLES      20
       NDAMP              50
    $end
    ```
