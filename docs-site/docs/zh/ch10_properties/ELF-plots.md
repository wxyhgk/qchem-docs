---
title: "10.5.7 电子定域函数"
---

## 10.5.7 电子定域函数

(July 4, 2026)

由 Becke 和 Edgecombe 提出的[[86]](../bib_references/bib.md#bib76)电子定域函数（Electron Localization Function, ELF），

<a id="Ch10.E63"></a>
$$
\text{ELF}=\Bigg{[}1+\Bigg{(}\frac{\tau_{\sigma}-\|\hat{\nabla}\rho_{\sigma}\|^{2}/(4\rho_{\sigma})}{\frac{3}{5}(6\pi^{2})^{2/3}(\rho_{\sigma}^{5/3})}\Bigg{)}^{\!2}\Bigg{]}^{-1} \tag{10.63}
$$

是衡量电子定域化程度的指标。
它源自 Hartree-Fock 条件对概率（conditional pair probability），能够揭示成键和壳层结构的相关信息。

函数 $\text{ELF}(\mathbf{r})$ 的取值介于 0 和 1 之间，其中 $\text{ELF}=1$
表示完全定域，$\text{ELF}=1/2$
表示类似电子气的对概率。若要使用 **Q-Chem** 生成 ELF 图像，请将 *$rem* 变量 PLOT_ELF 设置为 TRUE。
对于闭壳层体系，仅计算 $\alpha$ 自旋 ELF；对于开壳层体系
（自旋非限制计算），则同时计算 $\alpha$ 和 $\beta$ 自旋 ELF。[[702]](../bib_references/bib.md#bib734)

以下示例演示了水分子 ELF 的计算。

???+ example "示例 10.31：在 $50\times 50\times 50$ 网格上计算 H ${}_{2}$ O 的 ELF，输出为名为 elf_alpha.0.cube 的 cube 文件。"
    ```qchem
    $molecule
       0 1
       O    -4.5320698567   0.2524215916      0.0130780103
       H    -3.5641829319   0.2173288989     -0.0173259969
       H    -4.8109190521  -0.4489616171     -0.5945943692
    $end
    
    $rem
       JOBTYPE           opt
       METHOD            b3lyp
       BASIS             6-31g*
       PLOT_ELF          true
       MAKE_CUBE_FILES   true
       geom_opt_driver optimize
    $end
    
    $plots
    water
    50 -7 7
    50 -4 4
    50 -4 4
    0 1 0 0
    0
    $end
    ```

另请参阅 `$QC/samples` 目录中的 `elf_methane.in`，该示例使用了较新的 *$plots* 格式。
