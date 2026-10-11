---
title: "11.2.2 Kirkwood-Onsager 多极展开方法"
---

## 11.2.2 Kirkwood-Onsager 多极展开方法

(July 4, 2026)

**Q-Chem** 中最简单的隐式溶剂化模型是多极展开模型，[[690]](../bib_references/bib.md#bib716)

该模型也被称为 Kirkwood-Onsager 模型，有时称作广义 Kirkwood 模型。[[569]](../bib_references/bib.md#bib580)

在这种方法中，溶质被置于半径为 $a$ 的球形空腔内，空腔外围是介电常数为 $\varepsilon$ 的均匀介电介质，这两者构成了该模型的全部参数。*Onsager 模型*这一术语有时与溶质电荷密度的点偶极近似同义，但 **Q-Chem** 的版本使用对密度的单中心多极展开（可以推广到任意高阶），从而获得对溶质静电势的近乎精确的描述。该模型的核心是使用 Kirkwood 关于介电连续体内部球形空腔中各球谐函数溶剂化能的解析表达式。[[569]](../bib_references/bib.md#bib580)

关于空腔半径 $a$，Onsager 的原始建议基于纯溶质的摩尔体积 $V_{m}$，

<a id="eq:OnsagerRadius"></a>
$$
a=(3V_{m}/4\pi N_{A})^{1/3} \tag{11.1}
$$

其中 $N_{A}$ 为阿伏伽德罗常数。后来的研究表明，在现代量子化学计算的语境下，这是一个欠佳的选择。[[569]](../bib_references/bib.md#bib580)

也常见的做法是在式 ([11.1](#eq:OnsagerRadius)) 中 $a$ 的值上加 0.5 Å，
以考虑第一溶剂化壳层的影响，[[1490]](../bib_references/bib.md#bib1550)
或者将 $a$ 设置为溶质质心与溶质各原子之间的最大距离，再加上相关的范德华半径。第三种
选择是将 $2a$（空腔直径）设置为最大的溶质–溶剂核间距离，
再加上相关原子的范德华半径。
显然，这一选择带有相当大的任意性，且溶剂化能对 $a$ 的取值非常
敏感，[[569]](../bib_references/bib.md#bib580)
而第 [11.2.3](topic_pcm-em.md) 节所描述的 PCM 方法在很大程度上已使多极展开方法
过时，因为 PCM 采用精确的电子密度，并且（如有需要）也可使用球形空腔，
尽管更典型的选择是分子形状的范德华空腔。

Kirkwood-Onsager SCRF 通过在 *$rem* 部分设置 SOLVENT_METHOD =
KIRKWOOD 来请求使用。
 additional 一些额外选项可以在 *$solvent* 部分指定，
如下文所述，其中只有 **CavityRadius** 是必需的。
Kirkwood-Onsager 溶剂模型的能量与解析梯度
可用于 Hartree-Fock、DFT 以及 CCSD 计算。通常建议
先对溶质分子进行一次气相计算，其结果
可作为后续 Kirkwood-Onsager 隐式溶剂计算的初始猜测。
对于使用该模型的耦合簇计算，可以设置
CC_SAVEAMPL = TRUE 以保留气相计算中的 CC 振幅，
这将节省后续溶液相计算的一些时间。

**注意：

对于 CCSD 计算，Kirkwood-Onsager 模型只能与 CCMAN2 = FALSE 配合使用。
**

以下作业控制选项应放在 *$solvent* 部分，而不是 *$rem* 部分。
与 **Q-Chem** 输入文件的其他部分一样，此输入部分不区分大小写。

### `CavityRadius`

> **设置球形溶质空腔的半径。输入部分：$solvent**
>
> * **类型**: `FLOAT`
> * **默认值**: `无默认值。`
> * **选项**:
>     * $a$
>     * 空腔半径，单位为 Å。
> * **建议**: 无

### `Dielectric`

> **设置溶剂连续介质的介电常数。输入部分：$solvent**
>
> * **类型**: `FLOAT`
> * **默认值**: `78.39`
> * **选项**:
>     * $\varepsilon$
>     * 使用（无量纲的）值
>     * $\varepsilon$
>     * 。
> * **建议**: 默认值对应于 25 ${}^{\circ}$ C 下的水。

### `MultipoleOrder`

> **决定对溶质电荷密度的多极展开进行到哪一阶。输入部分：$solvent**
>
> * **类型**: `INTEGER`
> * **默认值**: `15`
> * **选项**:
>     * $\ell$
>     * 包含最高至
>     * $\ell$
>     * 阶的多极子。
> * **建议**: 使用默认值。多极展开通常在 $\ell$ = 15 阶即已收敛。

???+ example "示例 11.1: Hartree-Fock 级别的多极展开模型；乙腈中的 H ${}_{2}$ O"
    ```qchem
    $molecule
       0 1
       O       0.00000000     0.00000000     0.11722303
       H      -0.75908339     0.00000000    -0.46889211
       H       0.75908339     0.00000000    -0.46889211
    $end
    
    $rem
       METHOD            HF
       BASIS             6-31g**
       SOLVENT_METHOD    Kirkwood
    $end
    
    $solvent
       CavityRadius      1.8    !   1.8 Angstrom Solute Radius
       Dielectric        35.9   !   Acetonitrile
       MultipoleOrder    15     !   this is the default value
    $end
    ```

???+ example "示例 11.2: 将 Kirkwood-Onsager SCRF 应用于水中的氟化氢，先执行
气相计算。"
    ```qchem
    $molecule
       0 1
       H       0.000000     0.000000    -0.862674
       F       0.000000     0.000000     0.043813
     $end
    
    $rem
       METHOD          HF
       BASIS           6-31G*
    $end
    
    @@@
    
    $molecule
      read
    $end
    
    $rem
       JOBTYPE           FORCE
       METHOD            HF
       BASIS             6-31G*
       SOLVENT_METHOD    KIRKWOOD
       SCF_GUESS         READ  ! read vacuum solution as a guess
    $end
    
    $solvent
       CavityRadius    2.5
    $end
    ```
