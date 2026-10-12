---
title: "5.7.6 多体色散（Many-Body Dispersion, MBD）方法"
---

## 5.7.6 多体色散（Many-Body Dispersion, MBD）方法

（2026 年 7 月 4 日）

与早期严格采用（原子）对可加形式的 DFT-D 方法不同，DFT-D3 包含了三体（三原子）修正项。对于由大单体组装而成的非共价复合物[[764]](../bib_references/bib.md#bib798)，尤其是那些包含大量可极化中心的体系[[345]](../bib_references/bib.md#bib346)，这些修正项非常重要。Tkatchenko *et al.*[[1360]](../bib_references/bib.md#bib1422)提出的*多体色散*（many-body dispersion, MBD）方法代表了一种更普适、更少经验性的途径，超越了色散的对可加处理。该方法通过纳入直至原子数数目的 $n$ 体色散能贡献，以及任意阶的极化屏蔽（polarization screening）贡献来实现这一点。即使在苯二聚体这样的小体系中，MBD 方法也始终优于其他流行的 vdW 方法[[133]](../bib_references/bib.md#bib123)。

MBD 的核心思想是用偶极耦合的量子谐振子（quantum harmonic oscillator, QHO）来近似体系的动态响应，每个谐振子代表目标体系的一个片段。此类体系的关联能可以通过对对应的哈密顿量进行对角化而精确求得[[574]](../bib_references/bib.md#bib590)：

<a id="eq:mbdhamil"></a>

$$
\hat{H}_{\text{MBD}}=\frac{1}{2}\sum^{\text{atoms}}_{A}\hat{\nabla}^{2}_{\xi_{A}}+\frac{1}{2}\sum^{\text{atoms}}_{A}\omega^{2}_{A}\xi^{2}_{A}+\frac{1}{2}\sum^{\text{atoms}}_{A,B}\omega_{A}\omega_{B}(\alpha_{A}^{0}\alpha_{B}^{0})^{1/2}\xi_{A}T_{AB}\xi_{B}. \tag{5.52}
$$

其中，$\xi_{A}=m_{A}^{1/2}|\mathbf{r}_{A}-\mathbf{R}_{A}|$ 是振子 $A$ 相对于其中心
$\mathbf{R}_{A}$ 的质量加权位移，$\omega_{A}$ 是特征频率，$\alpha_{A}^{0}$ 是静态极化率。$T_{AB}$
是振子 $A$ 与 $B$ 之间的偶极势。MBD 哈密顿量是通过对长程关联进行粗粒化（经由长程偶极张量 $\mathbf{T}_{\mathrm{lr}}$）并利用绝热连接-涨落耗散（adiabatic connection fluctuation-dissipation）公式近似短程极化率而得到的：

<a id="eq:lrmbdcorr"></a>

$$
E^{\mathrm{MBD}}_{c,\text{lr}}=-\sum_{n=2}^{\infty}\frac{(-1)^{n}}{n}\int_{0}^{\infty}\frac{\mathrm{d}u}{2\pi}\sum_{AB}\mbox{tr}\Bigl{[}\bigl{\langle}(\mathbf{\alpha}_{\mathrm{eff}}\mathbf{T}_{\mathrm{lr}})^{n}\bigl{\rangle}_{\!AB}(iu)\Bigr{]}\;. \tag{5.53}
$$

这一近似将（给定片段的）动态极化率
$\mathbf{\alpha}_{\mathrm{eff}}$ 用相应 QHO 的极化率来表示，

<a id="Ch5.E54"></a>

$$
\alpha_{A}^{\mathrm{QHO}}(u)=\frac{q_{A}^{2}}{m_{A}(\omega_{A}^{2}-u^{2}-i\delta u)} \tag{5.54}
$$

其中 $q_{A}$ 是电荷，$m_{A}$ 是质量，$\omega_{A}$ 是振子的特征频率。式 ([5.53](#eq:lrmbdcorr))
中频率域的积分可以解析地完成，从而得到所谓关联能的等离激元极点（plasmon pole）公式，

<a id="eq:mbdplasmon"></a>

$$
E_{c}=\frac{1}{2}\sum_{p=1}^{3N}(\bar{\omega}_{p}-\omega_{p}) \tag{5.55}
$$

其中 $N$ 是片段数目，$\bar{\omega}_{p}$ 是相互作用（偶极耦合）体系的频率，$\omega_{p}$ 是无相互作用体系的频率（*即*，一组独立 QHO 的频率）。
该求和遍历体系的全部 $3N$ 个特征频率。

MBD 框架内的某一具体方法由以下模型定义：静态极化率（$\alpha_{\text{eff},A}^{0}$）的模型、无相互作用特征频率（$\omega_{A}$）的模型，以及用于定义 $\mathbf{T}_{\text{lr}}$ 的阻尼函数 [$f(R)$]。在 **Q-Chem** 中，MBD 方法按照 “MBD@rsSCS” 方案实现，其中 “rsSCS” 代表
范围分离自洽屏蔽（range-separated self-consistent screening）[[43]](../bib_references/bib.md#bib27)。
在该方案中，$\alpha_{\text{eff},A}^{0}$ 通过两步过程获得：

1. 1.

将自由体积缩放（free-volume scaling）方法应用于自由原子极化率，使用 Hirshfeld 划分的分子电子密度。这与第 [5.7.5](sect_TS.md)
节所述 TS-vdW 方法中采用的程序相同。
2. 2.

短程原子极化率
$\mathrm{\alpha}_{\mathrm{sr},AB}(iu)$ 是仅对极化率的短程部分施加类 Dyson（Dyson-like）屏蔽而得到的。
同样的范围分离稍后也将用于定义
$\mathbf{T}_{\mathrm{lr}}$。

将短程原子极化率沿一个片段坐标求和，得到局域有效动态极化率，*即*，
$\mathrm{\alpha}_{\mathrm{eff},A}^{0}=\sum_{B}\mathrm{\alpha}_{\mathrm{sr},AB}$，
然后进行球平均。用于构造 $\mathrm{\alpha}_{\mathrm{sr},AB}(iu)$ 和
$\mathbf{T}_{\mathrm{lr}}$ 的范围分离（阻尼）函数
$f(R)$ 与式 ([5.47](sect_TS.md#eq:fdamp_TS-vdW)) 中的相同，
只不过 $d=6$ 而非 $d=20$，并且给定泛函的 $s_{R}$ 同样是通过拟合非键复合物的相互作用能得到的。随后通过对哈密顿量式 ([5.52](#eq:mbdhamil)) 进行对角化，并使用等离激元极点公式式 ([5.55](#eq:mbdplasmon)) 来计算 MBD 能。

|  | BOP | B97-3 | B97 | BPW91 | revPBE | TPSS | BP86 | mPW91 | PBE | PBE0 | PW91 | SVWN |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $s_{R}$ | 0.42 | 0.45 | 0.50 | 0.53 | 0.54 | 0.56 | 0.64 | 0.68 | 0.83 | 0.85 | 0.91 | 1.19 |

表 5.5： 
MBD-vdW 模型中无量纲范围分离参数 $s_{R}$
[式 ([5.47](sect_TS.md#eq:fdamp_TS-vdW))] 的最优化取值，
取自文献 [[43]](../bib_references/bib.md#bib27)
。（该参数在文献 [[43]](../bib_references/bib.md#bib27)
中称为 $\beta$。）

MBD-vdW 方法显著提高了 S66[[1161]](../bib_references/bib.md#bib1213)
测试集相互作用能的精度，即使使用像 PBE 这样简单的泛函，其平均绝对误差为 0.3 kcal/mol、最大误差为 1.3 kcal/mol，而原始 PBE 的相应值分别为 2.3 kcal/mol（平均）和 7.2 kcal/mol（最大）。总体而言，MBD-vdW 方法优于对可加的后验（*a posteriori*）色散修正[[574]](../bib_references/bib.md#bib590)。

如前文在 TS-vdW 方法（第 [5.7.5](sect_TS.md) 节）背景下所述，
**FHI-aims** 或 **Quantum Espresso** 程序无法对原子执行精确的非限制 SCF 计算，这导致其自由原子体积与 **Q-Chem** 中计算的球对称体积不一致，从而使得 vdW 修正的取值也不一致。由于 TS-vdW 和 MBD-vdW 模型的参数是针对 **FHI-aims** 和 **Quantum Espresso** 拟合的，使用这些程序得到的结果与 S66 基准值略微更接近，因此 **Q-Chem** 为内部计算的 Hirshfeld 体积比提供了标量修正因子（scalar modifiers）。对于 S66，使用这些修正因子后，三种程序所得结果之间的差异可以忽略不计。

MBD-vdW 修正通过在 *$rem* 段中设置 MBDVDM = TRUE
来请求。其他作业控制变量，包括前述用于自由原子体积比的修正因子，均与 TS-vdW 方法相同，并在第 [5.7.5](sect_TS.md) 节中描述。

Q-Chem 中 MBD 的当前实现基于 LibMBD[[575]](../bib_references/bib.md#bib591)，

这是一个可移植的 Fortran 库，已与众多量子化学程序对接，其中请求 SCF 梯度的计算由 **Q-Chem** 专用代码完成。

### `MBDVDW`

> **开启 MBD-vdW 方法的开关标志**
>
> * **类型**：`STRING`
> * **默认值**：`0`
> * **可选值**：
>     * 0
>     * 不计算 MBD。
>     * MBD_SP
>     * 计算 MBD-vdW 对能量的贡献。
>     * MBD_FORCES
>     * 计算 MBD-vdW 对能量和核梯度的贡献。
>     * MBD_SCF
>     * 计算 MBD-vdW 对能量、核梯度以及 SCF 梯度的贡献。
> * **建议**：NONE

### `MBDVDW_BETA`

> **设置自定义的 $s_{R}$（$\beta$）阻尼参数值**
>
> * **类型**：`INTEGER`
> * **默认值**：`未定义默认值`
> * **可选值**：
>     * $n$
>     * 对应于
>     * $n\cdot 10^{-4}$
> * **建议**：对受支持的泛函使用预定义值，否则请查阅文献 43 Ambrosetti A. et al. J. Chem. Phys. (2014) , 140 , pp. 18A508 . 链接及其他相关文献。

???+ example "示例 5.16: 示例输入，演示包含 MBD-vdW 能量的水分子计算。"
    ```qchem
    $molecule
       0 1
       O
       H 1 0.95
       H 1 0.95 2 104.5
    $end
    
    $rem
       BASIS            6-31G*
       METHOD           PBE
       MBDVDW           MBD_SP !vdw settings, single point MBD correction
       HIRSHFELD_CONV   6 ! sets SCF_CONVERGENCE for single atom calculations
       HIRSHMOD         4 ! Apply modifiers to the free-atom volumes for H, C, N, and O
    $end
    ```
