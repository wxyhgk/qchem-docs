---
title: "5.10.3 局域 Fermi-Amaldi (LFA) 方案"
---

## 5.10.3 局域 Fermi-Amaldi (LFA) 方案

(July 4, 2026)

另一种由 Pan、Fang 和 Chai 提出的替代方案[[1037]](../bib_references/bib.md#bib226)，是使用 Fermi-Amaldi 交换关联泛函的*局域*版本。由此得到的交换密度泛函（其泛函导数具有正确的 $-1/r$ 渐近行为）可以直接添加到任何半局域密度泛函之上。文献 [[1037]](../bib_references/bib.md#bib226) 提出了该方法的三种变体。其中最简单的一种——严格局域 Fermi-Amaldi（LFAs）方案——已在 **Q-Chem** 中实现，适用于由 $Z\leq 55$ 的原子组成的分子。

???+ example "示例 5.24: 使用 LFAs-PBE 对水分子进行单点 TD-DFT 计算"
    ```qchem
    $comment
       Use LFAs-PBE potential for ground-state calculations, followed by
       TDDFT calculations with an adiabatic PBE XC kernel.
    $end
    
    $molecule
       0  1
       O
       H1  O  oh
       H2  O  oh  H1  hoh
    
       oh  =   1.0
       hoh = 110.0
    $end
    
    $rem
       EXCHANGE      gen
       BASIS         6-311(2+,2+)G**
       CIS_N_ROOTS   30
       RPA           true
    $end
    
    $xc_functional
       X   PBE   1.0
       C   PBE   1.0
       X   LFAs  1.0
    $end
    ```
