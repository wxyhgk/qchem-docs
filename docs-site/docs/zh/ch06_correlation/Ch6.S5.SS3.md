---
title: "6.5.3 基于数值稀疏性的实现"
---

## 6.5.3 基于数值稀疏性的实现

(2026 年 7 月 4 日)

近期于 2025 年，我们开发了一种新的基于数值稀疏性的局域相关形式体系（local correlation formalism）[[1431]](../bib_references/bib.md#bib1493)。
该新形式体系的目标是尽可能接近正则 RI-MP2，同时仅需要一个用于指定期望精度的用户输入参数。

**目前，该代码支持restricted 和 unrestricted SCF 参考下至氙（xenon）元素的体系。**

MP2 能量为

<a id="eq:lmp2_energy"></a>

$$
E^{(2)}=\sum_{iajb}{J_{ab}^{ij}\tau_{ab}^{ij}}\;, \tag{6.19}
$$

其中 $\mathbf{J}$（以及类交换张量 $\mathbf{K}$）是电子排斥积分（electron repulsion integral, ERI）张量

<a id="Ch6.E20"></a>

$$
J_{ab}^{ij}=K_{ba}^{ij}=(ia|jb)\;. \tag{6.20}
$$

$\boldsymbol{\tau}$ 是 MP2 方程的解

<a id="eq:lmp2_equation"></a>

$$
\mathbf{\Delta}\tau=-\left(2\mathbf{J}-\mathbf{K}\right)\;, \tag{6.21}
$$

这是一组线性方程，对于正交轨道，$\Delta$ 为

<a id="eq:Delta"></a>

$$
\Delta_{iajb,i^{\prime}a^{\prime}j^{\prime}b^{\prime}}=\delta_{ii^{\prime}}\delta_{aa^{\prime}}\delta_{jj^{\prime}}F^{\text{virt}}_{bb^{\prime}}-\delta_{ii^{\prime}}\delta_{aa^{\prime}}F^{\text{occ}}_{jj^{\prime}}\delta_{bb^{\prime}}+\delta_{ii^{\prime}}F^{\text{virt}}_{aa^{\prime}}\delta_{jj^{\prime}}\delta_{bb^{\prime}}-F^{\text{occ}}_{ii^{\prime}}\delta_{aa^{\prime}}\delta_{jj^{\prime}}\delta_{bb^{\prime}}\;. \tag{6.22}
$$

我们以数值稀疏性的方式计算并存储 $\mathbf{J}$ 张量，
即对于每个重要的 $i,j$ 对，我们存储两个"锯齿状列表（ragged lists）"，分别包含重要的
$a,b$ 指标及其积分值。我们所做的主要近似是"固定稀疏模式近似（fixed sparsity pattern approximation）"，
即我们强制解 $\mathbf{\tau}$ 具有相同的稀疏模式（相同的重要 $a,b$ 指标列表），参见图 [6.1](#fig:lmp2_fsp)。

![图 6.1：固定稀疏模式近似。](../assets/lmp2_fixed_sparsity_pattern.png)

*图 6.1：固定稀疏模式近似。*

通过将 CORRELATION 设置为 LMP2 选项来调用该代码。
必须在 LOCOOCCVIRT 中指定局域化方式。不同的局域化方案对 AO 线性相关性的处理方式不同。

### `LOCOOCCVIRT`

> **局域化分子轨道（MO）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * `2`: 当存在线性相关性时反复移除基函数。这会改变 SCF 结果，但可与 VV-HV 配合使用。
> * **建议**: 使用 2，因为推荐使用 VV-HV。之所以推荐非默认值，是因为它会导致不同的 SCF 能量。

可以选择不同的轨道局域化方法。占据空间推荐使用 $\lambda$-Boys 方法。
$\lambda$-Boys 试图同时最小化总轨道离域度（orbital spread）和总非对角 Fock 矩阵元。

<a id="Ch6.E23"></a>

$$
f^{\text{min}}_{\lambda\text{-Boys}}=\sum_{i}\left|\langle i|\mathbf{r}-\langle i|\mathbf{r}|i\rangle|i\rangle\right|^{2}+\lambda\sum_{i\neq j}\;.(F^{\text{occ}}_{ij})^{2}. \tag{6.23}
$$

当 $\lambda=0$ 时得到 Boys 轨道（最小化总轨道离域度），而当 $\lambda\to\infty$ 时得到正则轨道
（最小化 Fock 矩阵的非对角元）。推荐取值为 $\lambda=100$。

### `method`

> **定义占据空间的局域化方法。输入节：$localocc**
>
> * **类型**: `STRING`
> * **默认值**: `newboys`
> * **选项**:
>     * `newboys, cholesky, pipekmezey`
> * **建议**: 使用默认值，因为 $\lambda$-Boys 轨道已被证明非常有效。

### `lambda`

> **定义 $\lambda$。输入节：$localocc**
>
> * **类型**: `FLOAT`
> * **默认值**: `0`
> * **选项**:
>     * `100`: 推荐参数
> * **建议**: 使用更大的 $\lambda$ 会降低局域 MP2 代码的精度。

VV-HV 是虚拟空间推荐的局域化方法。

### `method`

> **定义虚拟空间的局域化方法。输入节：$localvirt**
>
> * **类型**: `STRING`
> * **默认值**: `VV-HV`
> * **选项**:
>     * VV-HV, NewBoys, PipekMezey, PAO
> * **建议**: 使用默认值。

阈值用于控制精度与效率之间的权衡。
通常，用户只需指定主阈值（$\epsilon$），
以控制 $\mathbf{J}$ 中保留哪些元素。

### `thresh`

> **定义主阈值 $\epsilon$。输入节：$localmp2**
>
> * **类型**: `INTEGER`
> * **默认值**: `60`
> * **选项**:
>     * `55 (`: $\epsilon=10^{-5.5}$，接近 DLPNO-MP2 中的 VeryTight), 50, 60, 65, 70
> * **建议**: 默认值通常可恢复 99.997% 的相关能，能量差误差为 0.1 kcal/mol。误差随 $\epsilon$ 线性变化，即使用 50 可将代码加速 3 到 5 倍，但误差也会增大 10 $\times$。

此处列出了所有其他内部预筛选阈值，它们可以类似地修改。
默认的 $i\rightarrow a$ 预筛选器阈值为

<a id="eq:lmp2_i_to_a"></a>

$$
\epsilon_{i\rightarrow a}=\left\{\begin{aligned} &\displaystyle 10^{-2.5}\epsilon&\displaystyle\epsilon\geq 10^{-6},\\
&\displaystyle 10^{3.5}\epsilon^{2}&\displaystyle\epsilon<10^{-6}.\end{aligned}\right. \tag{6.24}
$$

| 阈值 | 关键字 | 默认值 | 说明 |
| --- | --- | --- | --- |
| $\epsilon$ | thresh | $10^{-6}$ | 用户指定的主参数 |
| $\epsilon_{i\to j}$ | thresh $\_$ uFERF | $10^{-2}\epsilon$ |  |
| $\epsilon_{i\to a}$ | thresh $\_$ ia | 公式 6.24 |  |
| $\epsilon_{i\to P}$ | thresh $\_$ iP | $10^{2}\epsilon^{2}$ |  |
| $\epsilon_{i\to\mu}$ | thresh $\_$ coeff $\_$ occ | $\epsilon$ |  |
| $\epsilon_{a\to\nu}$ | thresh $\_$ coeff $\_$ virt | $10^{-4}$ | 固定默认值 |
| $\epsilon_{\text{solve}}$ | thresh $\_$ sol | $5\sqrt{\epsilon}$ | 线性方程求解器中的残差 |
| $\epsilon_{i\xrightarrow{p}a}$ | thresh $\_$ pre $\_$ ia | $\sqrt{10}\epsilon$ | 用于计算 $i\to a$ 预筛选器的预筛选器 |
| $\epsilon_{i\xrightarrow{p}P}$ | thresh $\_$ pre $\_$ iP | $\sqrt{10}\epsilon_{i\to P}$ |  |
| $\epsilon_{\mu\xrightarrow{p}P}$ | thresh $\_$ pre $\_$ muP | $10^{-3}\epsilon_{i\to a}$ |  |

表 6.2： 
基于数值稀疏性的局域 MP2 代码中的阈值。

$\kappa$-MP2 和二阶尺寸一致性 Brillouin-Wigner 理论（BWs2，第 [6.8](topic_bws2.md) 节）也受到支持，
但两者不能同时启用。

### `regularize`

> **定义 $\kappa$-MP2 中的 $1000\kappa$。输入节：$localmp2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `1450`: $\kappa=1.45$
> * **建议**: 非共价相互作用推荐使用 $\kappa=1.10$。

### `bw`

> **启用 BWs2 理论。输入节：$localmp2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `1`: 启用
> * **建议**: 如果需要 BW，请使用 1。

### `bw_alpha`

> **定义 BWs2 中的 $1000\alpha$ 参数。输入节：$localmp2**
>
> * **类型**: `INTEGER`
> * **默认值**: `1000`
> * **选项**:
>     * `4000`: $\alpha=4$。
> * **建议**: 为获得最佳的化学能量差，推荐使用 $\alpha=4$。与 $\gamma$ 配合使用时，推荐 $\alpha=\gamma=2$。

### `bw_gamma`

> **定义 BWs2 中的 $1000\gamma$ 参数。输入节：$localmp2**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `2000`: $\gamma=2$。
> * **建议**: 为获得最佳的化学效果，推荐 $\alpha=\gamma=2$。

???+ example "示例 6.3: 一个 $\epsilon=10^{-6}$ 的闭壳层示例。对于其他情况，请按需修改几何结构、基组和阈值。"
    ```qchem
    $molecule
    0 1
    C1
    H2    C1        1.09774
    H3    C1        1.09776    H2      107.23372
    H4    C1        1.09778    H2      107.22823    H3      114.89419
    H5    C1        1.09778    H2      107.22823    H4      114.89419
    $end

    $rem
    JOBTYPE¯¯¯SP
    UNRESTRICTED¯¯FALSE
    CORRELATION¯¯LMP2
    LOCOOCCVIRT¯¯2
    BASIS¯¯¯DEF2-SVP
    AUX_BASIS¯¯RIMP2-DEF2-SVP
    N_FROZEN_CORE¯FC
    SCF_CONVERGENCE 9
    THRESH¯¯¯14
    SYMMETRY¯¯FALSE
    SYM_IGNORE¯¯TRUE
    $end

    $localocc
    method newboys
    lambda 100
    $end
    $localvirt
    method vv-hv
    $end

    $localmp2
    thresh 60
    $end
    ```

