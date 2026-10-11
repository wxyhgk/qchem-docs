---
title: "10.8.6 共振拉曼强度"
---

## 10.8.6 共振拉曼强度

(July 4, 2026)

共振拉曼光谱的理论可由基于拉曼极化率张量的 Kramers-Heisenberg-Dirac 色散形式体系完整描述[[677]](../bib_references/bib.md#bib704)

<a id="eq:SOS"></a>

$$
\alpha_{\sigma\tau}(\omega_{\text{L}},\omega_{\text{S}})=\sum_{\upsilon}\left[\frac{\langle f|\hat{r}_{\sigma}|\upsilon\rangle\langle\upsilon|\hat{r}_{\tau}|i\rangle}{\hbar\omega_{\text{L}}-\hbar\omega_{\upsilon i}+i\Gamma_{i\upsilon}}+\frac{\langle f|\hat{r}_{\tau}|\upsilon\rangle\langle\upsilon|\hat{r}_{\sigma}|i\rangle}{\hbar\omega_{\upsilon i}+\hbar\omega_{\text{S}}+i\Gamma_{i\upsilon}}\right] \tag{10.74}
$$

其中涉及初态 $|i\rangle$ 与末态 $|f\rangle$。这里，$\omega_{\text{L}}$ 和 $\omega_{\text{S}}$ 分别是激光（入射光子）与散射光子的频率。由于式 ([10.74](#eq:SOS)) 需要对中间态 $\upsilon$（所有可达电子态上的振动能级）求和，使用上并不方便；通常的做法是将静态分子极化率按简正坐标展开为泰勒级数，[[35]](../bib_references/bib.md#bib18)
 从而将拉曼强度分解为 Franck–Condon（即“$A$ 项”）贡献与坐标相关的 Herzberg–Teller（“$B$ 项”和“$C$ 项”）贡献。[[35]](../bib_references/bib.md#bib18)

然而，每一项都包含对中间 vibrational（振动）态的求和，对于具有众多振动模式的大分子而言难以计算。

因此，在大多数情况下，计算共振拉曼（RR）光谱时只考虑能量最低的、具有拉曼活性的激发电子态。原则上应当考虑 Duschinsky 旋转效应，[[1246]](../bib_references/bib.md#bib1299)
*i.e.*,
即在每个电子态中简正模式各不相同这一事实。为简化起见忽略该效应、从而仅使用基态简正模式，即可得到“独立模式位移谐振子”（independent-mode, displaced harmonic oscillator, IMDHO）模型，[[1082]](../bib_references/bib.md#bib1127)

在该模型中，振动强度的共振增强（以模式 1 和 2 为例）表示为比值[[552]](../bib_references/bib.md#bib563)

<a id="eq:RR_intens"></a>

$$
\frac{I_{1}}{I_{2}}\approx\left(\frac{\omega^{\rm g}_{1}\Delta_{1}}{\omega^{\rm g}_{2}\Delta_{2}}\right)^{\!2}\;. \tag{10.75}
$$

在该方程中，$\omega_{1}^{\text{g}}$ 和 $\omega_{2}^{\text{g}}$ 分别表示简正模式 $Q_{1}$ 和 $Q_{2}$ 的基态振动频率，$\omega$ 为电子激发能。式 ([10.75](#eq:RR_intens)) 中的第一个等号在此写为近似形式，但在 IMDHO 模型内是精确成立的。物理量

<a id="eq:Delta_k"></a>

$$
\Delta_{k}=\left(\frac{\omega_{k}}{\hbar}\right)^{1/2}\Delta Q_{k} \tag{10.76}
$$

在基态几何构型（$\mathbf{Q}=\bm{0}$）处取值，它是激发态势能面沿模式 $k$ 方向的斜率。
由此得到式 ([10.75](#eq:RR_intens)) 中的第二个等号。

含时图像（time-dependent picture）为推导该表达式提供了途径。[[552]](../bib_references/bib.md#bib563)
 在这种方法中，涉及不同电子态的所需极化率张量元表示为初态与末态电子波函数之间随时间演化的重叠积分的傅里叶变换：

<a id="Ch10.E77"></a>

$$
\alpha(\omega_{\text{L}})\propto\int_{0}^{\infty}e^{i\omega_{\text{L}}t-\Gamma
t}\langle\psi_{f}|\psi_{i}(t)\rangle dt+\text{NRT}\;. \tag{10.77}
$$

这里，“NRT”表示在 RR 光谱中被忽略的非共振项。大分子在 Franck-Condon 区域停留的时间通常不超过 10–20 fs，重叠积分仅在该时间尺度上才显著。[[552]](../bib_references/bib.md#bib563)

在只考虑两个电子态的模型中，所得到的 RR 强度为

<a id="eq:functional"></a>

$$
I_{k}\propto\omega_{\text{L}}(\omega_{\text{L}}-\omega_{k})^{3}(\omega_{k}\Delta_{k})^{2}\; \tag{10.78}
$$

其中 $\mu_{k}$ 是第 $k$ 个简正模式的约化质量。

假设 $Q_{k}$ 在基态与激发态中具有相同的力常数，则可得该模式平衡位置的位移 $\Delta_{k}$（以简正坐标表示）与位移 $\widetilde{\Delta}_{i}$（以笛卡尔坐标表示）之间的线性变换关系：

<a id="Ch10.E79"></a>

$$
\widetilde{\Delta}_{i}=\sum_{k=1}^{3N-6}\left(\frac{L_{ik}}{m_{i}^{1/2}}\right)\Delta_{k}\;. \tag{10.79}
$$

其矩阵形式为

<a id="Ch10.E80"></a>

$$
\mathbf{\Delta}_{Q}=\lambda^{-1}\mathbf{L}^{\dagger}\mathbf{M}^{1/2}\mathbf{V}_{X} \tag{10.80}
$$

其中 $\lambda$ 是质量加权 Hessian 矩阵的本征值，M 定义原子质量矩阵，$V_{X}$ 是笛卡尔坐标下的能量梯度。
拉曼强度与无量纲位移相关

<a id="Ch10.E81"></a>

$$
\Delta_{k}=\left(\frac{\lambda_{k}}{m_{e}}\right)^{\!1/4}\Delta_{Qk}\;. \tag{10.81}
$$

设置 JOBTYPE = RRAMAN 即可调用共振拉曼强度的计算。

RR_NO_NORMALISE

### `RR_NO_NORMALISE`

> **控制频率计算任务是否计算共振拉曼强度**
>
> * **类型**: `LOGICAL`
> * **默认值**: `False`
> * **可选项**:
>     * False
>     * 归一化 RR 强度
>     * True
>     * 不归一化 RR 强度
> * **推荐设置**: False

???+ example "示例 10.44: 计算共振拉曼强度。"
    ```qchem
    $molecule
       0 1
       C     1.8288506578   -0.1219336002    0.0000000000
       C     0.6155951063    0.3987918905    0.0000000000
       C    -0.6155955606   -0.3987931260    0.0000000000
       C    -1.8288502653    0.1219348794    0.0000000000
       H     2.7085214046    0.4909328271    0.0000000000
       H     1.9881851899   -1.1843222290    0.0000000000
       H     0.4885913610    1.4671254626    0.0000000000
       H    -0.4885933454   -1.4671268234    0.0000000000
       H    -1.9881816088    1.1843239478    0.0000000000
       H    -2.7085226822   -0.4909289672    0.0000000000
    $end
    
    $rem
       JOBTYPE                RRAMAN
       METHOD                 hf
       BASIS                  3-21G
       CIS_N_ROOTS            1
       CIS_STATE_DERIVATIVE   1
    $end
    ```
