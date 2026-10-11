---
title: "7.6.3 单中心 NOCIS（1C-NOCIS）"
---

## 7.6.3 单中心 NOCIS（1C-NOCIS）

（2026 年 7 月 4 日）

## 7.6.3.1 单电子 M${}_{S}$ = 1/2 双重态与两电子 M${}_{S}$ = 1 三重态参考态

除此之外，还有一种近似方法，即单中心 NOCIS（1C-NOCIS），[[1023]](../bib_references/bib.md#bib1068)

它是介于 NOCIS 与 STEX 之间的一种折中方案。开壳层行列式像 NOCIS 那样被分别优化，但忽略了不同中心上具有空穴的非正交行列式之间的耦合，而剩余的、非正交行列式之间的矩阵元则用 NOCI 来计算。1C-NOCIS 先构造矩阵的正交 Slater-Condon 分量，然后执行 NOCI 以获得相应的非正交分量。之后，对角块会相对于基态进行投影。对于闭壳层单重态 NOCIS，由于不存在开壳层基态轨道，1C-NOCIS 与 STEX 是等价的。

1C-NOCIS 主要有两个优势。第一，其计算代价远低于 NOCIS，因此能够处理更大的分子。第二，与 STEX 不同，它允许开壳层态各自独立弛豫，这对精度可能有显著影响。

## 7.6.3.2 两电子 M${}_{S}$ = 0 单重态与三重态参考态

受 1C-NOCIS 模型的启发，人们发展了一套针对 M${}_{S}$ = 0、两电子开壳层（2eOS）参考态（单重态或三重态）的核心激发态理论。[[51]](../bib_references/bib.md#bib34)
 该理论适用于例如先用超快紫外（UV）泵浦、再用极紫外（XUV）或 X 射线探测的实验。对于可用单个自然跃迁轨道（NTO）对描述的 2eOS 态——即占据轨道 $o$ 上的一个电子被激发到目标虚轨道 $t$——其激发态波函数具有如下形式

<a id="Ch7.E74"></a>
$$
\big{|}^{1,\;3}\Psi_{i}\big{\rangle}=(2)^{1/2}\left(\big{|}\Phi_{o}^{t}\big{\rangle}\pm\big{|}\Phi_{\bar{o}}^{\bar{t}}\big{\rangle}\right) \tag{7.74}
$$

其中加号对应单重态，减号对应三重态。随后，在保持处于 M${}_{s}$ = 0 流形的前提下，将一个核心电子 $c$ 激发到任意粒子能级 $y$，可得到八种可能的组态

<a id="Ch7.E75"></a>
$$
\big{|}\Phi_{oc}^{to}\big{\rangle},\;\big{|}\Phi_{\bar{o}\bar{c}}^{\bar{t}\bar{o}}\big{\rangle},\;\big{|}\Phi_{oc}^{ty}\big{\rangle},\;\big{|}\Phi_{\bar{o}\bar{c}}^{\bar{t}\bar{y}}\big{\rangle},\;\big{|}\Phi_{\bar{o}c}^{\bar{t}y}\big{\rangle},\;\big{|}\Phi_{o\bar{c}}^{t\bar{y}}\big{\rangle},\;\big{|}\Phi_{\bar{o}c}^{\bar{y}t}\big{\rangle},\;\big{|}\Phi_{o\bar{c}}^{y\bar{t}}\big{\rangle} \tag{7.75}
$$

在这些组态所张成的空间内对角化 S${}^{2}$ 算符，可得到若干可能的组态态函数（Configuration State Function, CSF）。其中有一类特殊的 CSF，即与核心电子 $c$ 和那个在闭壳层态中原本满占据的单占据分子轨道（SOMO）$o$ 上的电子重新配对相对应的 2eOS 单重态或三重态 CSF。

<a id="Ch7.E76"></a>
$$
\big{|}^{1,\;3}\Phi_{o}^{t}\big{\rangle}=(2)^{-1/2}\left(\big{|}\Phi_{c}^{t}\big{\rangle}\pm\big{|}\Phi_{\bar{c}}^{\bar{t}}\big{\rangle}\right) \tag{7.76}
$$

当核心电子被激发到（相对于闭壳层组态而言的）任意虚轨道时，这些态可以用其余的 4eOS 单重态、三重态和五重态 CSF 来描述。

<a id="Ch7.E77"></a>
$$
\displaystyle\big{|}^{1_{A}}\Phi_{oc}^{ty}\big{\rangle} \tag{7.77a}
$$

请注意，与核心电子和粒子 SOMO $t$ 重新配对相对应的特殊 2eOS CSF，已包含在上述 4eOS CSF 之中，即 $y=t$ 的情形。与原始的 1C-NOCIS 和 STEX 方法一样，M${}_{S}$ = 0 的 2eOS 参考态变体是在上述所有 CSF 构成的子空间中对角化哈密顿量。然而，与原始的双重态和三重态 1C-NOCIS 实现不同，2eOS 变体提供了三组可能的参考轨道：

- •

1eOS、M${}_{S}$ = 1/2 双重态核心离子轨道，其中虚空间旋转到标准闭壳层 STEX 计算的 NTO 基下
- •

针对 $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ 组态、采用 ROKS 优化的 2eOS、M${}_{S}$ = 0 轨道
- •

针对 $\big{|}^{4}\Phi_{oc}^{t}\big{\rangle}$ 组态、采用 ROHF 优化的 3eOS、M${}_{S}$ = 3/2 四重态核心离子轨道

关键在于，所有这些参考态都纳入了由核心空穴存在所导致的弛豫，并期望提供一个定义明确的粒子态 $t$。由于 STEX 与 1C-NOCIS 模型本质上是针对开壳层体系的截断组态相互作用（Configuration Interaction, CI）形式体系，最终构造出的激发态对底层轨道的选择十分敏感。[[712]](../bib_references/bib.md#bib744)
 由于轨道 $t$ 在描述泵浦-探测态所采用的所有 CSF 中均被占据，这个通常为空轨道的 $t$ 的质量至关重要。目前，我们建议在以单重态为目标时使用 $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ 轨道，在以三重态为目标时使用 $\big{|}^{4}\Phi_{oc}^{t}\big{\rangle}$ 轨道。

价层激发态轨道可用作 $\big{|}^{1}\Phi_{o}^{t}\big{\rangle}$ ROKS 或 $\big{|}^{4}\Phi_{oc}^{t}\big{\rangle}$ ROHF 优化的初始猜测。或者，代码也可以将 1eOS、M${}_{S}$ = 1/2 双重态核心离子轨道用作猜测。由于 Hartree-Fock（HF）提供的虚轨道质量较差，双重态核心离子的计算可以用密度泛函理论（Density Functional Theory, DFT）来执行，从而为后续计算提供更好的猜测。所用的 DFT 方法通过 ENV_METHOD rem 变量指定。

1C-NOCIS 2eOS 实现比针对双重态和三重态的原始 1C-NOCIS 实现更灵活。它可以利用 CIS 或 ROKS 获得的任意 M${}_{S}$ = 0 单重态或三重态作为目标，并允许对初态的底层计算以及参考轨道的 SCF 优化进行控制。相应地，仅用于 2eOS 参考态 1C-NOCIS 计算的 $rem 变量数量也更多。
