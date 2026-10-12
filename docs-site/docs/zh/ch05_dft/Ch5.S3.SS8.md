---
title: "5.3.8 半经验泛函"
---

## 5.3.8 半经验泛函

（2026 年 7 月 4 日）

## 5.3.8.1 Grimme "3c" 方法

**Q-Chem** 中提供以下方法：

- •

**HF-3c**：这是一种基于 HF（Hartree-Fock，哈特里-福克）的半经验方法，配合名为 MINIX 的最小基组（Minimal Basis Set）使用。支持从 H 到 Xe 的所有元素。对于从 Rb（$Z=37$）到 Xe（$Z=54$）的元素，必须使用 def2-ECP。[[1329]](../bib_references/bib.md#bib1388)
- •

**PBEh-3c**：这是一种基于 DFT（Density Functional Theory，密度泛函理论）的方法，配合 def2-mSVP 基组使用。支持从 H 到 Rn 的所有元素。对于从 Rb（$Z=37$）到 Rn（$Z=86$）的元素，必须使用 def2-ECP。由于该方法包含电子相关效应，[[487]](../bib_references/bib.md#bib508)

其精度高于 HF-3c，但双-$\zeta$（double-$\zeta$）基组使其在处理大分子时计算代价更高。

**注意：

•

HF-3c 和 PBEh-3c 方法是针对上述基组进行参数化的。虽然 **Q-Chem** 并不强制这一限制，但除非有充分理由，否则不应使用其他基组；即便如此也应谨慎使用，因为结果可能无法达到文献报道的精度。

•

这些 DFT-3c 方法支持解析频率计算，

其中"3c"项的导数采用数值方法计算。在大多数情况下，用户无需关心此细节；有关半数值 Hessian（Hessian matrix，黑塞矩阵）计算的任务控制设置，请参见第 [5.3.8.2](#sec:3c-JobControl) 节。

**

## 5.3.8.2 DFT-3c 的任务控制与示例

### `FDIFF_STENCIL_3C`

> **指定是否对 DFT-3c 中"3c"部分的导数使用 5 点差分模板（5-point stencil）。**
>
> * **类型**：`STRING`
> * **默认值**：`无默认值`
> * **选项**：
>     * 5
>     * 使用 5 点差分模板
> * **建议**：若未指定此变量，Q-Chem 将使用 3 点差分模板，此前的测试已证明其精度足够。仅当对半数值频率的精度存有疑问时，才使用 5 点差分模板。

???+ example "示例 5.4：I ${}^{-}$ (H ${}_{2}$ O) 复合物的 HF-3c 计算。"
    ```qchem
    $rem
     method  hf-3c
     basis   minix
     ecp     def2-ecp
    $end
    
    $molecule
    -1 1
            I         0.6539056222    0.0300979939    0.0000000000
            O        -2.8593081518    0.0835488510    0.0000000000
            H        -1.8947008157    0.2596704547    0.0000000000
            H        -2.8641221666   -0.8778240298    0.0000000000
    $end
    
    ```

???+ example "示例 5.5：(H ${}_{2}$ O) ${}_{2}$ 的 PBEh-3c 计算。"
    ```qchem
    $molecule
       0 1
       O  -1.551007  -0.114520   0.000000
       H  -1.934259   0.762503   0.000000
       H  -0.599677   0.040712   0.000000
       O   1.350625   0.111469   0.000000
       H   1.680398  -0.373741  -0.758561
       H   1.680398  -0.373741   0.758561
    $end
    
    $rem
       METHOD           PBEh-3c
       BASIS            def2-mSVP
       XC_GRID          000099000590
       INCDFT           0
       INCFOCK          0
       SCF_CONVERGENCE  8
       THRESH           14
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
