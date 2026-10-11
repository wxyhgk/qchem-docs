---
title: "6.19.4 完美配对的二阶微扰修正：PP(2)"
---

## 6.19.4 完美配对的二阶微扰修正：PP(2)

（2026 年 7 月 4 日）

PP 和 CCVB 模型有望取代 HF 理论，作为电子结构的零阶描述，并可用作微扰理论的起点。它们忽略了所有涉及组态中包含一个或多个活性空间之外轨道的电子关联。从物理上看，这意味着所谓的“动态关联”被忽略了，这类关联对应于涉及高角动量虚拟能级的原子状关联。因此，GVB 模型在描述对那些被忽略的关联能敏感的能量差（*e.g.*，原子化能）时可能不够准确。人们希望以类似于 HF 参考通过 MP2 微扰理论进行修正的方式，对这种被忽略的关联加以修正。

为此，已经推导并高效实现了 PP 模型的主导（二阶）修正——即 PP(2)，[[112]](../bib_references/bib.md#bib99)
 支持闭壳层与开壳层轨道（仅限能量）。PP(2) 改善了 MP2 理论（PP(2) 与其类似）的许多最严重的失效情形，例如开壳层自由基的情况。相对于 PP 本身，PP(2) 也显著改善了相对 energies。PP(2) 采用定域分辨率（resolution of the identity, RI）方法实现，以将计算成本控制在可接受的范围内。其计算量随分子尺寸的 scaling 与 RI-MP2 相同（五阶标度），但前置因子约大 5 倍。因此它比 CCSD 或 CCSD(T) 计算便宜得多，后两者的计算量分别随体系大小的六次方和七次方标度。通过设置 CORRELATION = PP(2) 来请求 PP(2) 计算。由于目前唯一可用的算法使用辅助基组（auxiliary basis set），因此必须同时为 AUX_BASIS 提供有效值，以构成完整的输入文件。

下面的示例展示了具有挑战性的拉伸键 N2 分子的 PP(2) 输入文件。为此，这里启用了第 [6.19.2](subsec_PP.md) 节和第 [6.19.5](subsec_GVBMAN_other.md) 节中讨论的若干关于轨道收敛的非标准选项。首先，该情形是对偶数电子分子进行的开壳层（unrestricted）计算，因此必须打破 alpha/beta 自旋对称性才能找到非限制性解。其次，我们选择让孤对电子不参与关联，这通过指定 GVB_N_PAIRS 来实现。

???+ example "示例 6.53: 一个非标准的 PP(2) 计算。仅关联 3 对电子的拉伸 N2 的 UPP(2) 计算，初始猜测尝试使用 Boys 定域方案。"
    ```qchem
    $molecule
       0 1
       N
       N   1   1.65
    $end
    
    $rem
       UNRESTRICTED    true
       CORRELATION     pp(2)
       EXCHANGE        hf
       BASIS           cc-pvdz
       AUX_BASIS       rimp2-cc-pvdz   must use RI with PP(2)
       SCF_GUESS_MIX   10              mix SCF guess 100{\%}
       GVB_GUESS_MIX   25              mix GVB guess 25{\%} also!
       GVB_N_PAIRS     3               correlate only 3 pairs
       GVB_ORB_CONV    6               tighter convergence
       GVB_LOCAL       1               use Boys initial guess
    $end
    ```
