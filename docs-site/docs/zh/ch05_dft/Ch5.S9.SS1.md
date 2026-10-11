---
title: "5.9.1 概述"
---

## 5.9.1 概述

(July 4, 2026)

双杂化密度泛函理论（Double-hybrid density functional theory, DH-DFT）[[493]](../bib_references/bib.md#bib501)

(DH-DFT) 已展现出巨大的潜力，能够在与二阶 Møller-Plesset 微扰理论（MP2）相当的计算成本下逼近化学精度。在 DH-DFT 中，首先执行一次 Kohn-Sham（KS）密度泛函理论（DFT）计算，然后在二阶 Møller-Plesset 微扰理论（MP2）级别处理非定域轨道相关能。[[957]](../bib_references/bib.md#bib998)
 该 MP2 相关能校正包含一个同自旋（same-spin, ss）分量 $E_{c}^{\mathrm{ss}}$ 以及一个反自旋（opposite-spin, os）分量 $E_{c}^{\mathrm{os}}$，它们被加到 KS-DFT 计算得到的总能量上。为避免对相关性能量的重复计入（double-counting），引入了两个缩放参数 $c_{\mathrm{ss}}$ 和 $c_{\mathrm{os}}$：

<a id="eq:dft2a"></a>

$$
E_{\text{DH-DFT}}=E_{\text{KS-DFT}}+c_{\mathrm{ss}}E_{c}^{\mathrm{ss}}+c_{\mathrm{os}}E_{c}^{\mathrm{os}} \tag{5.62}
$$

理解形如式 ([5.62](#eq:dft2a)) 的泛函形式来源的一个出发点，是可为双杂化泛函提供严格定义的绝热连接公式（adiabatic connection formula）。人们考虑在虚构的非相互作用 KS 参考体系（$\lambda=0$）与真实物理体系（$\lambda=1$）之间的一条绝热路径，同时对所有 $\lambda$ 将电子密度固定为其在真实体系中的取值。于是

<a id="sung1"></a>

$$
E_{\rm XC}\left[\rho\right]=\int_{0}^{1}U_{{\rm XC},\lambda}[\rho]\;d\lambda\,, \tag{5.63}
$$

其中 $U_{{\rm XC},\lambda}$ 是耦合强度为 $\lambda$ 时的交换-相关能，其含义是：若哈密顿量中的电子–电子项取 $\lambda/r_{ij}$ 而非 $1/r_{ij}$ 的形式，所对应的交换-相关能。对该量使用线性模型，

<a id="sung2"></a>

$$
U_{{\rm XC},\lambda}=a+b\lambda\;, \tag{5.64}
$$

即可得到包含 HF 交换（或占据轨道）的流行杂化泛函，例如 B3LYP。[[96]](../bib_references/bib.md#bib78)
 如果进一步使用 Görling-Levy 微扰理论（GL2）来定义 $\lambda=0$ 处的初始斜率，便可得到式 ([5.62](#eq:dft2a)) 中的双杂化泛函形式，其中包含涉及虚轨道的 MP2 型微扰项（PT2）：[[684]](../bib_references/bib.md#bib710)

<a id="sung3"></a>

$$
U_{{\rm XC},\lambda}=\left.\frac{\partial U_{{\rm XC},\lambda}}{\lambda}\right|_{\lambda=0}=2E_{\rm C}^{\rm GL2}\,. \tag{5.65}
$$

绝热连接公式已被用于发展诸如 XYG3 这样的双杂化泛函。[[1551]](../bib_references/bib.md#bib1610)
 需要注意的是，**Q-Chem** 中实现的 XYG3 使用 B3LYP 轨道来生成密度并计算 PT2 项。这与 B2PLYP 不同，后者是 Grimme 提出的更早的双杂化泛函。[[493]](../bib_references/bib.md#bib501)
 B2PLYP 使用截断的 KS 轨道，而 XYG3 使用收敛的 KS 轨道来计算 PT2 项。XYG3 的精度不仅可与 G2 或 G3 理论在热化学方面的表现相媲美，而且势垒高度和非共价相互作用（包括堆积相互作用）也能被 XYG3 非常好地描述。[[1551]](../bib_references/bib.md#bib1610)

**注意： 

XYG3 推荐的基组是 6-311+G(3df,2p)。
**

由于包含了 PT2 项，双杂化计算的形式计算标度为 ${\cal{O}}({N^{5}})$，与传统 MP2 相同，因此不适用于大体系，并且在一定程度上丧失了 DFT 的成本优势。不过，**Q-Chem** 中非常成功的 SOS-MP2 及局域 SOS-MP2 算法可以被加以利用，从而发展基于这些 ${\cal{O}}({N^{4}})$ 方法的双杂化泛函。使用 SOS-MP2 的 XYG3 版本即为 XYGJ-OS 泛函。[[1543]](../bib_references/bib.md#bib1611)
 该泛函含有 4 个参数，利用热化学数据进行优化。它不仅比 XYG3 更快，而且精度与 XYG3 相当（甚至可能略好）。若应用局域 SOS-MP2 算法，XYGJ-OS 的标度可进一步降低至 ${\cal{O}}({N^{3}})$。最近，XYGJ-OS 成为首个解析能量梯度被推导并实现的双杂化泛函。[[642]](../bib_references/bib.md#bib666)

其他更为经验化的双杂化泛函也已在 **Q-Chem** 中实现。在 $\omega$B97 系列泛函中，$\omega$B97X-2[[225]](../bib_references/bib.md#bib221)
 是一个长程校正的双杂化泛函，能够大幅减小自相互作用误差（因其具有很高的 HF 交换比例），并且已被证明对于同时包含成键与非键相互作用的体系显著优于其他泛函。由于 PT2 相关能对基组选择较为敏感，$\omega$B97X-2 使用两套不同的基组进行了参数化：$\omega$B97X-2(LP) 是为配合 6-311++G(3df,3pd) 使用而参数化的，而 $\omega$B97X-2(TQZ) 则是采用 T/Q（三重-$\zeta$/四重-$\zeta$）外推至基组极限进行参数化的。在使用这两个泛函中的任何一个之前，强烈建议仔细阅读文献 [[225]](../bib_references/bib.md#bib221)
。

双杂化 DFT 的任务控制变量（job control variables）如下所述。请注意，PT2 相关能也可以使用高效的分辨率恒等（resolution-of-identity, RI）方法计算。
自 **Q-Chem** 5.2 起，只需通过 AUX_BASIS_CORR 指定辅助基组即可调用 RIMP2。参见第 [6.6](../ch06_correlation/topic_rimp2.md) 节。

DH

### `DH`

> **控制是否应用 DH-DFT 方案。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **取值选项**:
>     * FALSE（或 0）
>     * 不应用 DH-DFT 方案
>     * TRUE（或 1）
>     * 应用 DH-DFT 方案
> * **建议**: 无（NONE）

以下 *$rem* 变量与 $\omega$B97X-2(LP) 和 $\omega$B97X-2(TQZ) 泛函相关。

SSS_FACTOR

### `SSS_FACTOR`

> **控制 PT2 相关能中同自旋（same-spin）分量的强度。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值选项**:
>     * $n$
>     * 对应于
>     * $c_{\mathrm{ss}}=n/10^{6}$
>     * （见式 (
>     * 5.62
>     * )）。
> * **建议**: 无（NONE）

SOS_FACTOR

### `SOS_FACTOR`

> **控制 PT2 相关能中反自旋（opposite-spin）分量的强度。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值选项**:
>     * $n$
>     * 对应于
>     * $c_{\mathrm{os}}=n/10^{6}$
>     * （见式 (
>     * 5.62
>     * )）。
> * **建议**: 无（NONE）

???+ example "示例 5.18: B2PLYP 泛函在 LiH 上的应用（使用与不使用 RI）"
    ```qchem
    $molecule
       0 1
       H
       Li H 1.6
    $end
    
    $rem
       EXCHANGE    B2PLYP
       BASIS       cc-pvtz
       AUX_BASIS_CORR   rimp2-cc-pvtz
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       EXCHANGE    B2PLYP
       BASIS       cc-pvtz
    $end
    ```

???+ example "示例 5.19: $\omega$B97X-2(TQZ) 泛函在 LiH 上的应用（使用与不使用 RI）"
    ```qchem
    $molecule
       0 1
       H
       Li H 1.6
    $end
    
    $rem
       EXCHANGE    omegaB97X-2(TQZ)
       BASIS       cc-pvqz
       AUX_BASIS_CORR   rimp2-cc-pvqz
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       EXCHANGE     omegaB97X-2(TQZ)
       BASIS        cc-pvqz
    $end
    ```

在下面 XYG3 的示例中，**Q-Chem** 会自动先执行一次 B3LYP 计算，然后利用所得轨道来计算 PT2 相关项。也可以将 XYG3 与 RI 近似结合使用；为此可设置 EXCHANGE = XYG3RI，并配合选择合适的辅助基组。

???+ example "示例 5.20: N ${}_{2}$ 的 XYG3 计算"
    ```qchem
    $molecule
       0 1
       N      0.000000   0.000000   0.547775
       N      0.000000   0.000000  -0.547775
    $end
    
    $rem
       EXCHANGE  xyg3
       BASIS     6-311+G(3df,2p)
    $end
    ```

下一个示例演示 XYGJ-OS。该泛函默认使用 RI 近似，因此必须指定辅助基组。

???+ example "示例 5.21: N ${}_{2}$ 的 XYGJ-OS 计算"
    ```qchem
    $molecule
       0 1
       N      0.000000   0.000000   0.547775
       N      0.000000   0.000000  -0.547775
    $end
    
    $rem
       EXCHANGE    xygjos
       BASIS       6-311+G(3df,2p)
       AUX_BASIS   rimp2-cc-pVTZ
       PURECART    1111
       TIME_MP2    true
    $end
    ```

最后一个示例使用 XYGJ-OS 的局域版本，它与原始 XYGJ-OS 相同，只是在求解 RI 系数时采用了衰减库仑度量（attenuated Coulomb metric）。这里，关键字 omega 决定度量的局域程度。

???+ example "示例 5.22: N ${}_{2}$ 的局域 XYGJ-OS 计算"
    ```qchem
    $molecule
       0 1
       N    0.000    0.000   0.54777500
       N    0.000    0.000  -0.54777500
    $end
    
    $rem
       EXCHANGE   lxygjos
       BASIS      6-311+G(3df,2p)
       AUX_BASIS  rimp2-cc-pVTZ
       OMEGA      200
       PURECART   1111
    $end
    ```
