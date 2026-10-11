---
title: "10.2.13 推土机距离（Earth Mover's Distance）分析"
---

## 10.2.13 推土机距离（Earth Mover's Distance）分析

(July 4, 2026)

推土机距离（Earth Mover's Distance, EMD）为比较两个电荷分布提供了一种物理上直观的度量，它通过量化将一个分布转变为另一个分布所需的最小输运代价来实现这一点。[[1432]](../bib_references/bib.md#bib1494)
在激发态分析的语境下，
EMD 提供了一种电荷重排的真实空间（real-space）度量，因此能够对电荷转移与密度重新分布的传统描述符形成补充。EMD 的精确求值需要求解一个最优传输（optimal transport）问题，对于大型网格而言这可能计算开销巨大。为使该分析在常规应用中切实可行，**Q-Chem** 提供了一种基于 Sinkhorn–Knopp 算法的熵正则化（entropically regularized）表述，并结合电荷分布的约化网格（reduced-grid）表示，从而在保留其核心物理意义的同时，获得对精确 EMD 的高效近似。

## 10.2.13.1 理论

设 $\mathbf{r}$ 和 $\mathbf{c}$ 为定义在真实空间网格上的两个离散非负分布，且具有相等的总权重。
在 EMD 框架中，它们分别被解释为源分布和目标分布。对于一个距离矩阵 $\mathbf{M}$，
其元素 $M_{ij}$ 表示网格点 $i$ 与 $j$ 之间的距离，推土机距离定义为

<a id="Ch10.E37"></a>

$$
d_{\mathbf{M}}(\mathbf{r},\mathbf{c})=\min_{\mathbf{P}\in U(\mathbf{r},\mathbf{c})}\langle\mathbf{P},\mathbf{M}\rangle=\min_{\mathbf{P}\in U(\mathbf{r},\mathbf{c})}\sum_{ij}P_{ij}M_{ij}, \tag{10.37}
$$

其中 $\mathbf{P}$ 为输运方案（transport plan），且

<a id="Ch10.E38"></a>

$$
U(\mathbf{r},\mathbf{c})=\left\{\mathbf{P}\in\mathbb{R}_{+}^{d\times d}\;\middle|\;\mathbf{P}\mathbf{1}=\mathbf{r},\;\mathbf{P}^{T}\mathbf{1}=\mathbf{c}\right\}. \tag{10.38}
$$

因此，可行的输运方案被约束为须再现指定的源与目标边缘分布。换言之，
$\mathbf{P}$ 的每一行之和必须等于源分布，每一列之和必须等于目标分布。

在当前应用中，源分布和目标分布由与某一激发相关的真实空间密度差的正部和负部构造而来。令

<a id="Ch10.E39"></a>

$$
\Delta\rho(\mathbf{r})=\rho^{\mathrm{ES}}(\mathbf{r})-\rho^{\mathrm{GS}}(\mathbf{r}), \tag{10.39}
$$

其中 $\rho^{\mathrm{GS}}(\mathbf{r})$ 和 $\rho^{\mathrm{ES}}(\mathbf{r})$ 分别为基态密度和激发态密度。
密度差的正、负分量定义了两个待比较的电荷分布，

<a id="Ch10.E40"></a>

$$
\rho^{+}(\mathbf{r})=\max\!\bigl{(}\Delta\rho(\mathbf{r}),0\bigr{)},\qquad\rho^{-}(\mathbf{r})=\max\!\bigl{(}-\Delta\rho(\mathbf{r}),0\bigr{)}. \tag{10.40}
$$

在具有点 $\{\mathbf{r}_{i}\}$ 和求积权重 $\{w_{i}\}$ 的网格上进行离散化之后，每个网格点associated的有效电荷为

<a id="Ch10.E41"></a>

$$
q_{i}=w_{i}\rho(\mathbf{r}_{i}), \tag{10.41}
$$

而进入 EMD 问题的两个非负离散分布由密度差的正、负分量获得。于是转移的总电荷为

<a id="Ch10.E42"></a>

$$
q^{\mathrm{CT}}=\sum_{i}q_{i}^{+}=\sum_{j}q_{j}^{-}, \tag{10.42}
$$

相应的输运代价，

<a id="Ch10.E43"></a>

$$
\mu^{\mathrm{EMD}}=\min_{\mathbf{P}\in U(\mathbf{r},\mathbf{c})}\sum_{ij}P_{ij}M_{ij}, \tag{10.43}
$$

其单位为电荷乘以距离。类似地，可以定义一个具有长度量纲的量

<a id="Ch10.E44"></a>

$$
d^{\mathrm{EMD}}=\frac{\mu^{\mathrm{EMD}}}{q^{\mathrm{CT}}}. \tag{10.44}
$$

精确的 EMD 可以通过使用运输单纯形（transportation simplex）算法求解这一约束优化问题来获得。虽然这种方法能得到精确的最优输运代价，但其计算开销随网格规模迅速增长，对于大体系或稠密的真实空间网格可能高到难以承受。

## 10.2.13.2 用于高效 EMD 计算的网格选择

在 DFT 或 TDDFT 计算所使用的完整求积网格上直接进行 EMD 计算通常不可行，因为网格点数目可能非常庞大。
由于最优传输问题的计算规模随离散分布的尺寸呈不利增长，当前实现采用约化网格（reduced grid）来进行 EMD 求值。

在该流程中，首先电子波函数（结构）计算所用的底层求积网格上计算电子密度。随后为 EMD 分析引入一个更小的以原子为中心的（atom-centered）网格。
原始求积网格中的每个网格点根据空间邻近性被分配至较小 EMD 网格上的某个点，原始网格上的有效电荷被累加到所选的 EMD 网格点上。通过这种方式，细网格密度被投影到一个更小的离散表示上，
在保持整体分布特征的同时大幅减少了进入传输问题的点数目。

设 $\{\mathbf{r}_{k}^{\mathrm{big}},w_{k}^{\mathrm{big}},\rho_{k}^{\mathrm{big}}\}$ 表示原始求积网格上的网格点、权重与密度，
并设 $\{\mathbf{r}_{i}^{\mathrm{small}}\}$ 表示用于 EMD 求值的约化网格。分配给约化网格上点 $i$ 的有效电荷通过累加所有归属于该约化点的原始网格点的电荷来构造，

<a id="Ch10.E45"></a>

$$
q_{i}^{\mathrm{small}}=\sum_{k\in\Omega_{i}}w_{k}^{\mathrm{big}}\rho_{k}^{\mathrm{big}}, \tag{10.45}
$$

其中 $\Omega_{i}$ 表示被分配至约化网格点 $i$ 的原始网格点集合。随后，由此得到的约化网格电荷用于定义进入 EMD 计算的源分布和目标分布。

这一约化网格流程大幅降低了精确 EMD 与正则化 EMD 计算的开销，同时保留了密度差在物理上有意义的表示。约化网格选自 **Q-Chem** 中标准的以原子为中心的求积网格。
因此 EMD 结果的质量取决于密度差的约化网格表示质量；当需要较高的定量精度时，应当检查 EMD 网格的收敛性。

## 10.2.13.3 熵正则化最优传输

为进一步降低 EMD 求值的开销，可以用一个熵正则化问题来替代精确的最优传输问题，

<a id="Ch10.E46"></a>

$$
\mathbf{P}^{\lambda}=\arg\min_{\mathbf{P}\in U(\mathbf{r},\mathbf{c})}\left[\langle\mathbf{P},\mathbf{M}\rangle-\frac{1}{\lambda}h(\mathbf{P})\right], \tag{10.46}
$$

其中 $h(\mathbf{P})$ 是输运方案的熵，$\lambda$ 是正则化参数。相应的正则化输运代价为

<a id="Ch10.E47"></a>

$$
d_{\mathbf{M}}^{\lambda}(\mathbf{r},\mathbf{c})=\langle\mathbf{P}^{\lambda},\mathbf{M}\rangle. \tag{10.47}
$$

熵项有利于更平滑的输运方案，并且免去直接求解原始线性规划问题的需要。参数 $\lambda$ 控制平滑性与对精确 EMD 保真度之间的平衡。$\lambda$ 值越大，熵项的影响越小，解越接近
精确 EMD；而 $\lambda$ 值越小，输运方案越平滑，通常也能改善数值稳定性。

正则化问题允许最优输运方案写成因子化形式，

<a id="Ch10.E48"></a>

$$
\mathbf{P}^{\lambda}=\mathrm{diag}(\mathbf{u})\,\mathbf{K}\,\mathrm{diag}(\mathbf{v}), \tag{10.48}
$$

其中

<a id="eq:emd_kernel"></a>

$$
K_{ij}=e^{-\lambda M_{ij}}. \tag{10.49}
$$

向量 $\mathbf{u}$ 和 $\mathbf{v}$ 为正的缩放因子，其选取使得输运方案满足边缘约束，

<a id="Ch10.E50"></a>

$$
\mathbf{P}^{\lambda}\mathbf{1}=\mathbf{r},\qquad(\mathbf{P}^{\lambda})^{T}\mathbf{1}=\mathbf{c}. \tag{10.50}
$$

将因子化形式代入这些约束，得到耦合的不动点方程

<a id="Ch10.E51"></a>

$$
u_{i}=\frac{r_{i}}{(\mathbf{K}\mathbf{v})_{i}},\qquad v_{j}=\frac{c_{j}}{(\mathbf{K}^{T}\mathbf{u})_{j}}. \tag{10.51}
$$

这些方程构成了 Sinkhorn–Knopp 算法的基础，

 该算法交替更新 $\mathbf{u}$ 和 $\mathbf{v}$，直到边缘约束
在指定阈值内得到满足。

因此该方法的具体计算步骤如下。第一，在底层求积网格上计算密度差。
第二，将相应电荷投影到更小的 EMD 网格上。第三，在该约化网格上构造距离矩阵 $\mathbf{M}$，
并按照式 ([10.49](#eq:emd_kernel)) 形成核矩阵 $\mathbf{K}$。最后，执行 Sinkhorn 迭代以得到
正则化输运方案及相应的输运代价。正则化方法的主要计算开销在于涉及 $\mathbf{K}$ 和 $\mathbf{K}^{T}$ 的重复矩阵-向量
乘积，这比针对大网格求解精确运输单纯形问题的代价要低得多。

在实践中，主要的数值参数是正则化强度 $\lambda$。该参数必须取得足够大，使正则化输运代价保持接近精确 EMD，
但又不能大到使核矩阵严重病态。若 $\lambda M_{ij}$ 过大，
指数核可能下溢，导致缩放向量不稳定和收敛行为变差。因此当前实现开放了用户可调的正则化与收敛参数，其中用户指定的正则化参数按距离矩阵的最大元素进行缩放。
换言之，计算中使用的有效正则化强度为 $\lambda_{\mathrm{eff}}=\frac{\lambda_{\mathrm{in}}}{M_{ij}^{\max}}$，其中
$M_{ij}^{\max}=\max_{ij}M_{ij}$。一般而言，增大 $\lambda_{\mathrm{eff}}$ 可改善与精确 EMD 的一致性，而减小
$\lambda_{\mathrm{eff}}$ 则可改善数值稳定性与收敛行为。

综上所述，该特性可在真实空间网格上对两个离散电荷分布之间的推土机距离（EMD）进行求值，既可使用精确传输算法，也可使用由 Sinkhorn–Knopp 算法求解的熵正则化最优
传输表述，并且 EMD 计算采用约化的以原子为中心的网格，而非底层电子结构计算所使用的完整求积网格。因此结果的质量同时取决于 EMD 网格与正则化参数。主要的用户可控选项包括：
EMD 分析本身的开关 EMD_ANALYSIS、用于构造约化真实空间电荷分布的网格 EMD_FIT_GRID、是否使用 Sinkhorn
求解器 SINKHORN、Sinkhorn 求解器的正则化强度 SINKHORN_REG、Sinkhorn 求解器的收敛阈值 SINKHORN_THRESHOLD，以及最大迭代
循环数 MAX_SINKHORN_CYCLES。较大的正则化参数通常能改善与精确 EMD 的一致性，但若核矩阵变得过于尖锐，则可能导致数值不稳定。较小的正则化参数能改善数值鲁棒性，
但相对于精确 EMD 会引入更大的近似误差。

EMD_ANALYSIS

### `EMD_ANALYSIS`

> **控制是否执行推土机距离（EMD）分析。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不执行 EMD 分析。
>     * TRUE
>     * 执行 EMD 分析。
> * **建议**: 该关键字激活对真实空间密度差的正、负两部分之间推土机距离（EMD）的求值。相应的电荷分布构建于 EMD_FIT_GRID 所指定的网格上。

EMD_FIT_GRID

### `EMD_FIT_GRID`

> **指定用于构造推土机距离（EMD）分析约化真实空间电荷分布的以原子为中心的网格。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $N$
>     * 网格规格
>     * $N$
>     * 的格式与
>     * XC_GRID
>     * 相同。
> * **建议**: 该关键字定义用于进入 EMD 计算的密度差约化网格表示的网格。输入格式与 XC_GRID 相同，但其取值应不大于 XC_GRID。推荐的选取是 19000026；对于较大分子，可以使用更小的网格，精度损失甚微。更稠密的网格通常能改善 EMD 结果的质量，但同时也会增加传输问题的计算开销。

SINKHORN

### `SINKHORN`

> **控制 EMD 计算是否使用熵正则化的 Sinkhorn–Knopp 算法。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 使用精确的运输单纯形算法。
>     * TRUE
>     * 使用熵正则化的 Sinkhorn–Knopp 算法。
> * **建议**: Sinkhorn–Knopp 算法为精确推土机距离提供高效的近似，对于大网格通常更为可取。相应的正则化强度由 SINKHORN_REG 控制。

MAX_SINKHORN_CYCLES

### `MAX_SINKHORN_CYCLES`

> **控制 EMD 计算中使用的 Sinkhorn–Knopp 迭代的最大次数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `50`
> * **选项**:
>     * $N$
>     * 最多执行
>     * $N$
>     * 次 Sinkhorn 迭代。
> * **建议**: 若 Sinkhorn 迭代在默认循环次数内不收敛，可增大此值。仅当 SINKHORN 设为 1 时该关键字才有效。

SINKHORN_THRESHOLD

### `SINKHORN_THRESHOLD`

> **控制 Sinkhorn–Knopp 迭代的收敛阈值。**
>
> * **类型**: `INTEGER`
> * **默认值**: `3`
> * **选项**:
>     * $N$
>     * 将 Sinkhorn 迭代收敛至阈值
>     * $10^{-N}$
>     * 。
> * **建议**: $N$ 值较小对应较宽松的收敛判据，而较大的值对应更严格的收敛要求。仅当 SINKHORN 设为 1 时该关键字才有效。

SINKHORN_REG

### `SINKHORN_REG`

> **控制熵正则化 Sinkhorn EMD 计算中使用的正则化强度。**
>
> * **类型**: `INTEGER`
> * **默认值**: `100`
> * **选项**:
>     * $N$
>     * 对 Sinkhorn 核使用正则化参数
>     * $N$
>     * 。
> * **建议**: 该关键字控制 EMD 问题 Sinkhorn 表述中熵正则化的强度。较大的值通常给出更接近精确 EMD 的结果，但也可能导致数值不稳定或收敛变慢。较小的值数值上更稳健，但与精确最优传输解的偏差更大。在当前实现中，用户指定的正则化参数在构造 Sinkhorn 核之前会按距离矩阵的最大元素进行内部缩放。仅当 SINKHORN 设为 1 时该关键字才有效。

???+ example "示例 10.10: 使用 PBE 泛函对水分子进行基础 TDDFT 计算，并采用精确的运输单纯形算法对前三个激发单重态和三重态进行 EMD 分析。"
    ```qchem
    $molecule
    0 1
    O   0.000000   0.000000   0.000000
    H   0.758602   0.000000   0.504284
    H  -0.758602   0.000000   0.504284
    $end
    
    $rem
    METHOD PBE
    BASIS aug-cc-pVDZ
    CIS_N_ROOTS 3
    CIS_SINGLETS TRUE
    CIS_TRIPLETS TRUE
    STATE_ANALYSIS TRUE
    XC_GRID 50000194
    EMD_ANALYSIS TRUE
    EMD_FIT_GRID 19000026
    SINKHORN FALSE
    SCF_CONVERGENCE 8
    THRESH 13
    N_FROZEN_CORE 0
    $end
    
    ```

???+ example "示例 10.11: 使用 PBE 泛函对水分子进行基础 TDDFT 计算，并采用近似的 Sinkhorn–Knopp 算法对前三个激发单重态和三重态进行 EMD 分析。"
    ```qchem
    $molecule
    0 1
    O   0.000000   0.000000   0.000000
    H   0.758602   0.000000   0.504284
    H  -0.758602   0.000000   0.504284
    $end
    
    $rem
    METHOD PBE
    BASIS aug-cc-pVDZ
    CIS_N_ROOTS 3
    CIS_SINGLETS TRUE
    CIS_TRIPLETS TRUE
    STATE_ANALYSIS TRUE
    XC_GRID 50000194
    EMD_ANALYSIS TRUE
    EMD_FIT_GRID 19000026
    SINKHORN TRUE
    SINKHORN_THRESHOLD 3
    MAX_SINKHORN_CYCLES 30
    SINKHORN_REG 200
    SCF_CONVERGENCE 8
    THRESH 13
    N_FROZEN_CORE 0
    $end
    
    ```
