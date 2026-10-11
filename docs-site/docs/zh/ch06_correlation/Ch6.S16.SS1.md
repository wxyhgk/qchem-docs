---
title: "6.16.1 概述"
---

## 6.16.1 概述

（2026 年 7 月 4 日）

CCSD、OO-CCD/VOD、CCD 以及 QCCD/VQCCD 方法的解析梯度（analytic gradients）已可用，适用于闭壳层和开壳层参考（仅限 UHF 和 RHF），
包括冻结核心（frozen core）和/或冻结虚轨道功能，以及电子排斥积分（electron-repulsion integrals）的 RI/Cholesky 表示。
CCVB-SD 的解析梯度仅适用于闭壳层参考（RHF）。
此外，部分选定的 GVB 模型的梯度也已可用。

对于 CCSD 和 OO-CCD 波函数，**Q-Chem** 还可以计算偶极矩、
$\langle r^{2}\rangle$（以及分开的 $\langle x^{2}\rangle$、$\langle y^{2}\rangle$
和 $\langle z^{2}\rangle$ 矩，这对于指认不同的里德堡（Rydberg）态很有用，*e.g.*，$3p_{x}$ 与 $3s$
*etc.*），以及 $\langle\hat{S}^{2}\rangle$ 值。
CCSD 和 (V)OO-CCD 程序与 NBO 5.0 软件包的接口也已可用。该程序与 EOM-CCSD
性质/梯度计算（第 [7.9.21](../ch07_excited/sec_EOMGRAD.md) 节）密切相关。
CCSD 可用的溶剂模型（solvent models）在第 [11.2](../ch11_env/topic_solvation.md) 章中描述。
对于 CCSD，g 张量（g-tensors）的解析计算也已可用（参见第 [7.9.21](../ch07_excited/sec_EOMGRAD.md) 节）。

局限性：目前尚不支持 ROHF 和非 HF（*e.g.*，B3LYP 或 FNO）轨道以及 RI 近似的梯度和完全弛豫性质。

**注意：**

**若使用冻结核心/虚轨道计算梯度或性质，算法会将冻结轨道替换为限制性（restricted）轨道。
这不会影响能量，但会改变 CCMAN 输出中的轨道编号。**

CC_REF_PROP

### `CC_REF_PROP`

> **是否计算非弛豫（期望值）或完整响应（包含轨道弛豫项）的单粒子 CCSD 性质。当前包含的性质有永久偶极矩、电子密度沿各方向的二阶矩（$\langle x^{2}\rangle$、$\langle y^{2}\rangle$ 和 $\langle z^{2}\rangle$）以及 $\langle r^{2}\rangle=\langle x^{2}\rangle+\langle y^{2}\rangle+\langle z^{2}\rangle$。此选项与 JOBTYPE = FORCE、OPT 或 FREQ 不兼容。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **可选值**：
>     * FALSE, TRUE
> * **建议**：计算性质需要求解额外的方程（$\lambda$-CCSD 方程），其开销与 CCSD 方程大致相同。如果不需要性质，请使用默认值。性质计算本身的开销较低。通过指定 NBO = TRUE、= TRUE 以及 JOBTYPE = FORCE，可以用 NBO 软件包分析 CCSD 单粒子密度。

CC_REF_PROP_TE

### `CC_REF_PROP_TE`

> **请求计算非弛豫的双粒子 CCSD 性质。目前包含的双粒子性质有 $\langle\hat{S}^{2}\rangle$。单粒子性质也将一并计算，因为与 $\langle\hat{S}^{2}\rangle$ 的开销相比，单粒子性质计算的额外开销很小。变量 CC_REF_PROP 也必须设置为 TRUE。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **可选值**：
>     * FALSE, TRUE
> * **建议**：双粒子性质的计算开销很大，因为需要计算并使用双粒子密度矩阵（开销大致相当于一次解析梯度计算的开销）。除非确实需要，否则请勿请求双粒子性质。

CC_FULLRESPONSE

### `CC_FULLRESPONSE`

> **计算完全弛豫性质（包含轨道弛豫项）。变量 CC_REF_PROP 也必须设置为 TRUE。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **可选值**：
>     * FALSE, TRUE
> * **建议**：不适用于非 UHF/RHF 参考，也不适用于没有解析梯度的方法（e.g.，QCISD）。

???+ example "示例 6.50：HHeF 的 CCSD 几何优化及后续性质计算"
    ```qchem
    $molecule
       0 1
       H    0.000000    0.000000   -1.886789
       He   0.000000    0.000000   -1.093834
       F    0.000000    0.000000    0.333122
    $end
    
    $rem
       JOBTYPE                     OPT
       METHOD                      CCSD
       BASIS                       aug-cc-pVDZ
       GEOM_OPT_TOL_GRADIENT       1
       GEOM_OPT_TOL_DISPLACEMENT   1
       GEOM_OPT_TOL_ENERGY         1
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE           SP
       METHOD            CCSD
       BASIS             aug-cc-pVDZ
       SCF_GUESS         READ
       CC_REF_PROP       1
       CC_FULLRESPONSE   1
    $end
    ```
