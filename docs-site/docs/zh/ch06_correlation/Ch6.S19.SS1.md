---
title: "6.19.1 引言"
---

## 6.19.1 引言

(July 4, 2026)

下文所述方法价键理论（Valence Bond Theory）相关，由 GVBMAN 模块负责处理。可用的模型如下：

CORRELATION

### `CORRELATION`

> **指定由 GVBMAN 处理的 GVB 模型中的关联级别。**
>
> * **类型**: `STRING`
> * **默认值**: `None`
> * **可选值**:
>     * PP
>     * CCVB
>     * GVB_IP
>     * GVB_SIP
>     * GVB_DIP
>     * OP
>     * NP
>     * 2P
> * **建议**: 作为粗略指导，对双自由基类（biradicaloid）分子使用 PP，对涉及强自旋关联的多自由基类（polyradicaloid）分子使用 CCVB。更多指导请查阅相关文献。

电子关联较强的分子，其名义占据轨道（例如构成 Hartree-Fock 波函数的那些轨道）与名义空轨道之间的能量差很小。典型例子包括所谓的双自由基类（diradicaloid）分子，[[655]](../bib_references/bib.md#bib679)
 或含有部分断裂化学键的分子（如某些过渡态结构）。由于能隙很小，除参考行列式之外的其他电子组态以相当可观的振幅对分子波函数有贡献，忽略它们会导致显著误差。

然而，纳入所有可能的组态是一种严重的过度处理。通常的做法是限制所生成的组态：不是由全部分子轨道构造，而仅由“芯（core）”轨道或“活性（active）”轨道构造。本节只讨论一种活性空间，它由每对电子对应两个轨道构成：一个名义占据（呈成键或孤对电子特征），另一个名义空轨道，即关联轨道（correlating orbital，通常呈反键特征）。这通常称为完美配对（perfect pairing）活性空间，它显然非常适合描述与断键相关的成键/反键关联。

在该活性空间（或任何其他活性空间）内的量子化学计算由完整活性空间自洽场（Complete Active Space SCF, CASSCF）给出，但其计算量随分子尺寸呈指数增长，对于活性轨道数超过约 14 个的体系而言代价高得令人却步。基于 CASSCF 的一个定义清晰的耦合簇（Coupled Cluster, CC）近似是只在价空间中纳入双替换，并对这些轨道加以优化。在常规 CC 理论框架下，这定义了价优化双替换（valence optimized doubles, VOD）模型，[[724]](../bib_references/bib.md#bib755)
 其标度为 ${\cal{O}}({N^{6}})$（见第 [6.14.2](topic_vod.md) 节）。该开销对于大分子仍然过于昂贵，难以直接应用。

本节所介绍的方法在精密但昂贵的耦合簇方法与廉价的 DFT、HF 及 MP2 方法之间架起桥梁——后者在描述呈现强电子关联的分子（如双自由基）时可能不足（而且事实上常常不足）。耦合簇完美配对（coupled cluster perfect pairing, PP）[[287]](../bib_references/bib.md#bib291)
、非完美配对（imperfect pairing, IP）[[1387]](../bib_references/bib.md#bib1449)
 以及受限耦合簇（restricted coupled cluster, RCC）[[1390]](../bib_references/bib.md#bib1452)
 模型都是 VOD 的局域近似，分别仅包含线性数量与二次数量级的双替换振幅。它们在思路上接近广义价键（generalized valence bond, GVB）型波函数，[[461]](../bib_references/bib.md#bib474)
 因为事实上它们都是针对 GVB 的耦合簇模型，共享同一完美配对活性空间。该系列中最强大的方法——耦合簇价键（Coupled Cluster Valence Bond, CCVB）方法，[[1274]](../bib_references/bib.md#bib1328)
——是一种价键途径，其能力远超 GVB-PP 及相关方法，详见下文第 [6.19.3](subsec_CCVB.md) 节。
