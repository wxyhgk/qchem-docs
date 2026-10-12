---
title: "5.6.4 调优型 RSH 泛函"
---

## 5.6.4 调优型 RSH 泛函

（2026 年 7 月 4 日）

对于 [5.6.2](subsec_wb97series.md) 节所描述的泛函，其 range-separation（程分离）参数完全属于经验性质，不应加以调整；而对于 [5.6.3](ex_ks-wb97xd4.md) 节所描述的泛函，则确实*建议*进行一定程度的调整，尤其是在含时密度泛函理论（Time-Dependent Density Functional Theory, TDDFT）计算中，以及任何需要解读轨道能量的性质（例如 HOMO/LUMO 能隙）。这种调整可以以一种非经验（但依赖于具体体系）的方式来完成，[[60]](../bib_references/bib.md#bib45)

即通过“调优”（tuning）$\omega$ 的取值，使其满足类 Koopmans 电离能判据

<a id="eq:IP-tuning"></a>

$$
-\epsilon_{\rm HOMO}(\omega)=\mbox{IE}(\omega) \tag{5.18}
$$

其中 $\mbox{IE}=E(N-1)-E(N)$ 是所关注的 $N$ 电子体系电离能（Ionization Energy, IE）的 $\Delta$SCF 值。条件 $\epsilon_{\rm HOMO}=-\mbox{IE}$ 在精确的密度泛函理论（Density Functional Theory, DFT）中是一条定理，[[1065]](../bib_references/bib.md#bib1113)
 但近似泛函往往严重违背该条件。当使用 range-separated hybrid（RSH，程分离杂化）泛函时，Eq. ([5.18](#eq-IP-tuning)) 的两侧都依赖于 $\omega$，于是需要不断调整该参数，直到 Eq. ([5.18](#eq:IP-tuning)) 中的条件得到满足为止；这就需要对中性物种和电离物种分别使用不同的 $\omega$ 值进行一系列自洽场（Self-Consistent Field, SCF）计算。如此获得的取值通常被称为 $\omega$ 的“最优调优”（optimally tuned）值。
严格来说，并不能保证某个近似密度泛函对任意给定分子都能满足 Eq. ([5.18](#eq:IP-tuning))，因此最优调优值未必存在。
实践中通常能够找到这样一个值，但需要注意的是，$\omega$ 的最优调优值依赖于体系大小，因而这一调优过程在形式上破坏了尺寸一致性（size-consistency）。[[667]](../bib_references/bib.md#bib692)

在 Eq. ([5.18](#eq:IP-tuning)) 这一简单的“IE 调优”判据基础上，还可以有若干变体。
为了正确描述电荷转移（charge-transfer）激发态，Baer 及其合作者[[60]](../bib_references/bib.md#bib45)
 建议寻找这样的 $\omega$ 值，使其（在尽可能大的程度上）同时对中性供体分子以及（另行计算的）受体物种的*阴离子*满足 Eq. ([5.18](#eq:IP-tuning))。沿类似思路，为了同时设定 HOMO 与 LUMO 的能级，使基本能隙（fundamental gap，即 $\mbox{IE}-\mbox{EA}$）等于 HOMO/LUMO 能隙，Kronik 等人[[720]](../bib_references/bib.md#bib751)
 建议最小化如下函数

<a id="eq:J(w)"></a>

$$
J(\omega)=\big{[}\epsilon_{\rm HOMO}(\omega)+\mbox{IE}(\omega)\big{]}^{2}+\big{[}\epsilon_{\rm LUMO}(\omega)+\mbox{EA}(\omega)\big{]}^{2} \tag{5.19}
$$

其中相对于 $\omega$ 进行最小化，且 $\mbox{EA}=E(N+1)-E(N)$。最小化 $J(\omega)$ 代表了一种尝试：在假定 ($N+1$) 电子阴离子是束缚态的前提下，同时对 $N$ 电子分子及其阴离子满足 Eq. ([5.18](#eq:IP-tuning)) 中的 IE 定理。
已发表的基准测试表明，这些依赖于具体体系的方法能够给出最准确的 IE 值和 TDDFT 激发能。[[851]](../bib_references/bib.md#bib885)

有一个用于优化 $\omega$ 的脚本，名为 `OptOmegaIPEA.pl`，位于
`$QC/bin/tools` 目录中。该脚本在 0.1–0.8 bohr${}^{-1}$ 的范围内扫描 $\omega$，
对应于 *$rem* 变量 OMEGA 在 100–800 范围内的取值。有关如何修改脚本以在更宽范围内扫描的说明，请参阅脚本本身。
运行该脚本之前，用户需要为 RSH 单点能计算创建三个输入文件，使用相同的几何结构和基组（Basis Set）：
一个用于中性分子（`N.in`），一个用于其阴离子（`M.in`），一个用于其阳离子（`P.in`）。然后用户应运行命令

> ```qchem
> OptOmegaIPEA.pl >& optomega
> ```

该命令既生成输入文件（`N_*`、`P_*`、`M_*`），也对这些输入文件运行 **Q-Chem**，并将优化输出写入 `optomega`。
该脚本对中性分子及其阴离子同时施加 IE 条件，最小化 Eq. ([5.19](#eq:J(w))) 中的 $J(\omega)$。
另有一个类似的脚本 `OptOmegaIP.pl`，仅对中性分子使用 Eq. ([5.18](#eq:IP-tuning))。

**注意：**

1.

若体系不具有正的电子亲和能（Electron Affinity, EA），则应仅按照 IP 条件进行调优。
在这种情况下，IP/EA 脚本会给出错误的 $\omega$ 值。

2.

为了使脚本正常工作，必须在输入文件中指定
SCF_FINAL_PRINT = 1。脚本会查找特定的正则表达式，
缺少该关键字将无法正确运行。

**

尽管调优过程最初由 Baer 及其合作者基于 BNL 泛函开发，[[851]](../bib_references/bib.md#bib885)
 但它同样适用于任何 RSH 泛函，例如 LRC-$\omega$PBE（参见
Ref. [[1380]](../bib_references/bib.md#bib1441)
）。上述脚本也可以与这些其他 RSH 泛函配合使用。

遗憾的是，通过满足 Eq. ([5.18](#eq:IP-tuning)) 中的判据所获得的最优调优值“$\omega_{\text{IE}}$”
对体系大小表现出令人不安的依赖性，[[710]](../bib_references/bib.md#bib742)

从而导致尺寸可加性（size-extensivity）的丧失。[[667]](../bib_references/bib.md#bib692)
例如，团簇阴离子 (H${}_{2}$O)${}^{-}_{6}$ 的最优调优值与针对 (H${}_{2}$O)${}^{-}_{70}$ 调优所得的值差异很大，[[1380]](../bib_references/bib.md#bib1441)

而且对于 $\pi$ 共轭体系，最优调优值还会随共轭长度而变化。[[710]](../bib_references/bib.md#bib742)
作为基于 IE 的 Eq. ([5.18](#eq:IP-tuning)) 判据的一种替代方案，
有所谓的全局密度依赖（Global Density-Dependent, GDD）调优程序，[[956]](../bib_references/bib.md#bib997)
其中最优值

<a id="eq:wgdd"></a>

$$
\omega_{\text{GDD}}=C\langle d^{2}_{\text{x}}\rangle^{-1/2} \tag{5.20}
$$

与距离 $d_{\text{x}}$ 的平均值相关联，该距离指分子外围区域中的电子与局域化价轨道区域的交换空穴（exchange hole）之间的距离。量 $C$ 是针对给定 LRC 泛函的经验参数，
已针对 LRC-$\omega$PBE（$C=0.90$）和
LRC-$\omega$PBEh（$C=0.75$）确定，[[956]](../bib_references/bib.md#bib997)
 目的是在小分子中确保 $\omega_{\text{GDD}}\approx\omega_{\text{IE}}$。
（对于 **Q-Chem** 实现的 LRC-$\omega$PBE，确定了一个略有不同的值，$C=0.885$。[[764]](../bib_references/bib.md#bib798)
）
对于小分子的 TD-DFT 计算，选择 $\omega_{\text{GDD}}$ 还是 $\omega_{\text{IE}}$ 基本上没有差别，
而与前者的计算相比，搜索 $\omega_{\text{IE}}$ 值要昂贵得多（也不那么方便）。[[880]](../bib_references/bib.md#bib915)

由于与 $\omega_{\text{IE}}$ 相比，LRC-$\omega_{\text{GDD}}$PBE 对聚乙炔的极化率给出了更好的描述，[[526]](../bib_references/bib.md#bib540)
 因此可以预期，用 $\omega_{\text{GDD}}$ 代替 $\omega_{\text{IE}}$
可能会给出更准确的分子性质，尤其是在共轭体系中——在这些体系里 IE 调优有时会遇到 HOMO/LUMO 能隙趋于零的问题。[[480]](../bib_references/bib.md#bib491)

通过将 *$rem* 变量 OMEGA_GDD = TRUE 进行设置，即可对 RSH 泛函实施 GDD 调优。
计算 Eq. ([5.20](#eq:wgdd)) 中的 $\omega_{\text{GDD}}$ 需要电子密度，
这是通过使用由 *$rem* 变量 OMEGA 所给定 $\omega$ 值的 RSH 泛函计算得到的收敛 SCF 密度来实现的。
因此，原则上 $\omega_{\text{GDD}}$ 的取值依赖于 OMEGA 的设定值，尽管实际上它对该值并不十分敏感，
以此方式获得的结果与完全自洽的 $\omega_{\text{GDD}}$ 值相近。[[956]](../bib_references/bib.md#bib997)

### `OMEGA_GDD`

> **控制对长程校正 DFT 应用 $\omega_{\text{GDD}}$ 调优**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`（或 `0`）: 不应用 GDD 调优。
>     * `TRUE`（或 `1`）: 使用 GDD 调优。
> * **建议**: 还必须指定 $rem 变量 OMEGA，以设定初始的 range-separation 参数。

### `OMEGA_GDD_SCALING`

> **设定 GDD 调优程序中的经验常数 $C$。**
>
> * **类型**: `INTEGER`
> * **默认值**: `885`
> * **选项**:
>     * $n$: 对应于 $C=n/1000$。
> * **建议**: 量 $C=0.885$（即 $n=885$）是在 Ref. 764 Lao K. U., Herbert J. M. J. Chem. Theory Comput. (2018) , 14 , pp. 2955 . 中基于 LRC-$\omega$PBE/hpTZVPP 计算确定的。

???+ example "示例 5.9: 示例输入，演示基于 GDD 调优程序确定 LRC-$\omega$PBE 所用 $\omega$ 值的计算。"
    ```qchem
    $comment
       The initial omega value has to set.
    $end
    
    $molecule
       0 1
       O   -0.042500   0.091700   0.110000
       H    0.749000   0.556800   0.438700
       H   -0.825800   0.574700   0.432500
    $end
    
    
    $rem
       EXCHANGE          gen
       BASIS             aug-cc-pvdz
       LRC_DFT           true
       OMEGA             300
       OMEGA_GDD         true
    $end
    
    $xc_functional
       X   wPBE   1.0
       C    PBE   1.0
    $end
    ```

无论调优是如何实现的，这些经过调优的泛函通常被认为之所以有效，是因为它们减少了近似 DFT 中的自相互作用误差（self-interaction error）。
量化——或至少直观呈现——该误差的一种便捷方式，是将 DFT 能量作为（分数）电子数 $N$ 的函数绘制出来，
因为原则上 $E(N)$ 应由一系列线段组成，并在 $N$ 取整数值处出现斜率的突变（即所谓的导数不连续性（derivative discontinuity）[[261]](../bib_references/bib.md#bib262)
），
但实际绘出的 $E(N)$ 曲线会偏离直线段而向外弯曲。[[261]](../bib_references/bib.md#bib262)
有人建议通过检查这类图来调整 RSH 泛函中短程交换的成分比例，[[58]](../bib_references/bib.md#bib41)
 而 $\omega$ 参数则由调优来确定。

### `FRACTIONAL_ELECTRON`

> **增加或减少分数个电子。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 使用整数个电子。
>     * $n$: 向体系添加 $n/1000$ 个电子。
> * **建议**: 仅在试图生成 $E(N)$ 图时使用。若 $n<0$，则从体系中移除相应分数的电子。

???+ example "示例 5.10: 具有分数电子数的 DFT 作业示例。此处通过从 F${}^{2-}$ 的 HOMO 中减去分数个电子，构造氟的 $-1.x$ 价阴离子。"
    ```qchem
    $comment
       Subtracting a whole electron recovers the energy of F-.
       Adding electrons to the LUMO is possible as well.
    $end
    
    $molecule
       -2 2
       F
    $end
    
    $rem
       EXCHANGE              b3lyp
       BASIS                 6-31+G*
       FRACTIONAL_ELECTRON  -500   ! divide by 1000 to get the fraction, -0.5 here.
       GEN_SCFMAN            FALSE ! not yet available in new scf code
    $end
    ```

IE 调优的另一种替代方案是有效（Effective, EFF）调优程序 [[1257]](../bib_references/bib.md#bib1312)
，其中 range-separation 参数的最优值由下式给出

<a id="mu-eff"></a>

$$
\omega=\frac{a_{1}}{\langle r_{s}\rangle}+\frac{a_{2}\langle r_{s}\rangle}{1+a_{3}\langle r_{s}\rangle^{2}}~{}, \tag{5.21}
$$

其中 $a_{1}=1.91718$，$a_{2}=-0.02817$，$a_{3}=0.14954$。局域 Seitz 半径定义为
$r_{s}=\left(\frac{3}{4\pi n}\right)^{1/3}$，其中 $n=n_{\uparrow}+n_{\downarrow}$。量 $\langle r_{s}\rangle$ 表示按体积平均的 Seitz 半径。

虽然对于体相固体而言 $\langle r_{s}\rangle$ 的计算很直接，但对于原子和分子这类有限体系则需要特别小心，因为在低密度尾部 $r_{s}$ 会发散。
为解决这一问题，采用了 $r_{s}$ 的加权平均：

<a id="eq:rs-average"></a>

$$
\langle r_{s}\rangle=\frac{\int w(\mathbf{r})\,r_{s}(\mathbf{r})\,d^{3}r}{\int
w(\mathbf{r})\,d^{3}r}\;. \tag{5.22}
$$

此处，权重函数 $w(\mathbf{r})$ 的构造旨在突出电子密度显著的区域（即芯层和价层区域）。
关于权重函数的构造及其推导的更多细节，请参见 Ref. [[1257]](../bib_references/bib.md#bib1312)
。

已证明 LRC-$\omega_{\text{EFF}}$PBE 泛函能够更好地描述电荷转移激发、HOMO-LUMO 能隙以及激子（excitonic）性质。

实践中，通过将 *$rem* 变量 OMEGA_EFF = TRUE 进行设置，即可对 RSH 泛函实施 EFF 调优。
Eq. ([5.21](#mu-eff)) 中 $\omega_{\text{EFF}}$ 的求值需要电子密度，这是从收敛的 SCF 计算中获得的。
使用 RSH 泛函时，必须通过 *$rem* 变量 OMEGA 指定 $\omega$ 的初始值。相比之下，对于半局域泛函或全局杂化泛函（例如 PBE 或 B3LYP），则无需指定 OMEGA。

### `OMEGA_EFF`

> **控制对长程校正 DFT 应用 $\omega_{\text{EFF}}$ 调优**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`（或 `0`）: 不应用 EFF 调优。
>     * `TRUE`（或 `1`）: 应用 EFF 调优。
> * **建议**: 还必须指定 $rem 变量 OMEGA，为 range-separation 参数提供初始值。

???+ example "示例 5.11: 示例输入，演示使用 EFF 调优程序确定 $\omega$ 值的计算。"
    ```qchem
    $comment
    w_EFF tuning for anthracene molecule
    Effective (eff) tunning of the range-separation parameter, w
    J. Phys. Chem. Lett. 2025, 16, 32, 8198–8208
    $end
    
    
    $molecule
    0 1
      Ne  0 0 0
    $end
    
    $rem
    METHOD           PBE
    BASIS            cc-pVDZ
    OMEGA_EFF       true
    SCF_CONVERGENCE  7
    MAX_SCF_CYCLES   100
    XC_GRID          000099000590
    THRESH           14
    SYM_IGNORE       TRUE
    $end
    ```
