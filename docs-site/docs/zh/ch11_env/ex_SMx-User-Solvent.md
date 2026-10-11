---
title: "11.2.9 SM$x$ 模型"
---

## 11.2.9 SM$x$ 模型

(2026 年 7 月 4 日)

SM$x$ 模型由明尼苏达大学的 Cramer、Truhlar 及其合作者开发。SM8[[912]](../bib_references/bib.md#bib942)、
SM12[[910]](../bib_references/bib.md#bib946)
 和 SMD[[909]](../bib_references/bib.md#bib943)

版本在 **Q-Chem** 中均可使用。其中推荐使用 SMD，因为它适用于任意基组（与 SM8 不同），
并且同时实现了解析梯度与 Hessian（与 SM8 和 SM12 均不同）。

这些 SM$x$ 方法中的每一种都被设计为"通用"溶剂化模型，[[281]](../bib_references/bib.md#bib286)

其含义是：只要已知某种溶剂的少量描述符（descriptors），该模型就可以应用于该溶剂。
溶剂描述符包括：

- •

介电常数
- •

折射率
- •

宏观表面张力
- •

Abraham 标度下的酸度
- •

Abraham 标度下的碱度
- •

碳芳香性（carbon aromaticity），即非氢溶剂原子中芳香碳原子所占的比例
- •

电负性卤素性（electronegative halogenicity），即非氢溶剂原子中
F、Cl 或 Br 所占的比例）。

这些模型由对连续介质静电相互作用的广义 Born（generalized Born）处理，以及以原子表面张力进行参数化的
非静电相互作用组成。非静电相互作用包括空穴化（cavitation）、色散（dispersion）
以及溶剂结构变化，对这些非静电效应的正确处理是获得准确溶剂化（自由）能的关键。

通过设置 SOLVENT_METHOD = SM8、SM12 或 SMD 来请求 SM$x$ 计算。
其中某些模型需要在 *$smx* 输入节中指定方法专用的关键字，这些关键字在后文各节中讨论。
至少需要在这类模型的 *$smx* 节中指定溶剂，除非所用溶剂为水。可用溶剂列于表 [11.7](#table:SMx-solvents) 中。
这些名称在 *$smx* 节中给出时不应包含空格或连字符，因此表 [11.7](#table:SMx-solvents) 中的 propanoic acid 应写作 `propanoicacid`，1-hexanol 应写作 `1hexanol`。

表 11.7：可用于 SM$x$ 计算的溶剂。${}^{a}$

<table class="ltx_tabular">
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_tt">1,1,1-trichloroethane</td>
<td class="ltx_td ltx_align_left ltx_border_tt">bromoethane</td>
<td class="ltx_td ltx_align_left ltx_border_tt">
$m$-ethylbenzoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1,1,2-trichloroethane</td>
<td class="ltx_td ltx_align_left">bromooctane</td>
<td class="ltx_td ltx_align_left">
$m$-ethylethanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1,1-dichloroethane</td>
<td class="ltx_td ltx_align_left">butanal</td>
<td class="ltx_td ltx_align_left">
$m$-ethylmethanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1,2,4-trimethylbenzene</td>
<td class="ltx_td ltx_align_left">butanoicacid</td>
<td class="ltx_td ltx_align_left">
$m$-ethylphenylketone</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1,4-dioxane</td>
<td class="ltx_td ltx_align_left">butanone</td>
<td class="ltx_td ltx_align_left">
$m$-ethylpropanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-bromo-2-methylpropane</td>
<td class="ltx_td ltx_align_left">butanonitrile</td>
<td class="ltx_td ltx_align_left">
$m$-ethylbutanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-bromopentane</td>
<td class="ltx_td ltx_align_left">butylethanoate</td>
<td class="ltx_td ltx_align_left">
$m$-ethylcyclohexane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-bromopropane</td>
<td class="ltx_td ltx_align_left">butylamine</td>
<td class="ltx_td ltx_align_left">
$m$-ethylformamide</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-butanol</td>
<td class="ltx_td ltx_align_left">butylbenzene</td>
<td class="ltx_td ltx_align_left">
$m$-xylene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-chloropentane</td>
<td class="ltx_td ltx_align_left">carbon disulfide</td>
<td class="ltx_td ltx_align_left">heptane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-chloropropane</td>
<td class="ltx_td ltx_align_left">carbon tetrachloride</td>
<td class="ltx_td ltx_align_left">hexadecane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-decanol</td>
<td class="ltx_td ltx_align_left">chlorobenzene</td>
<td class="ltx_td ltx_align_left">hexane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-fluorooctane</td>
<td class="ltx_td ltx_align_left">chlorotoluene</td>
<td class="ltx_td ltx_align_left">nitrobenzene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-heptanol</td>
<td class="ltx_td ltx_align_left">
<span class="ltx_text ltx_font_italic">cis</span>-1,2-dimethylcyclohexane</td>
<td class="ltx_td ltx_align_left">nitroethane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-hexanol</td>
<td class="ltx_td ltx_align_left">decalin</td>
<td class="ltx_td ltx_align_left">nitromethane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-hexene</td>
<td class="ltx_td ltx_align_left">cyclohexane</td>
<td class="ltx_td ltx_align_left">methylaniline</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-hexyne</td>
<td class="ltx_td ltx_align_left">cyclohexanone</td>
<td class="ltx_td ltx_align_left">nonane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-iodobutane</td>
<td class="ltx_td ltx_align_left">cyclopentane</td>
<td class="ltx_td ltx_align_left">octane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-iodopentene</td>
<td class="ltx_td ltx_align_left">cyclopentanol</td>
<td class="ltx_td ltx_align_left">pentane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-iodopropane</td>
<td class="ltx_td ltx_align_left">cyclopentanone</td>
<td class="ltx_td ltx_align_left">
$o$-chlorotoluene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-nitropropane</td>
<td class="ltx_td ltx_align_left">decane</td>
<td class="ltx_td ltx_align_left">
$o$-cresol</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-nonanol</td>
<td class="ltx_td ltx_align_left">dibromomethane</td>
<td class="ltx_td ltx_align_left">
$o$-dichlorobenzene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-octanol</td>
<td class="ltx_td ltx_align_left">dibutyl ether</td>
<td class="ltx_td ltx_align_left">
$o$-nitrotoluene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-pentanol</td>
<td class="ltx_td ltx_align_left">dichloromethane</td>
<td class="ltx_td ltx_align_left">
$o$-xylene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-pentene</td>
<td class="ltx_td ltx_align_left">diethyl ether</td>
<td class="ltx_td ltx_align_left">pentadecane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-pentyne</td>
<td class="ltx_td ltx_align_left">diethylsulfide</td>
<td class="ltx_td ltx_align_left">pentanal</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">1-propanol</td>
<td class="ltx_td ltx_align_left">diethylamine</td>
<td class="ltx_td ltx_align_left">pentanoic acid</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2,2,2-trifluoroethanol</td>
<td class="ltx_td ltx_align_left">diiodomethane</td>
<td class="ltx_td ltx_align_left">pentylethanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2,2,4-trimethylpentane</td>
<td class="ltx_td ltx_align_left">dimethyldisulfide</td>
<td class="ltx_td ltx_align_left">pentylamine</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2,4-dimethylpentane</td>
<td class="ltx_td ltx_align_left">dimethylacetamide</td>
<td class="ltx_td ltx_align_left">perfluorobenzene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2,4-dimethylpyridine</td>
<td class="ltx_td ltx_align_left">dimethylformamide</td>
<td class="ltx_td ltx_align_left">phenyl ether</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2,6-dimethylpyridine</td>
<td class="ltx_td ltx_align_left">dimethylpyridine</td>
<td class="ltx_td ltx_align_left">propanal</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-bromopropane</td>
<td class="ltx_td ltx_align_left">DMSO</td>
<td class="ltx_td ltx_align_left">propanoic acid</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-chlorobutane</td>
<td class="ltx_td ltx_align_left">dipropylamine</td>
<td class="ltx_td ltx_align_left">propanonitrile</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-heptanone</td>
<td class="ltx_td ltx_align_left">dodecane</td>
<td class="ltx_td ltx_align_left">propylethanoate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-hexanone</td>
<td class="ltx_td ltx_align_left">
$E$-1,2-dichloroethene</td>
<td class="ltx_td ltx_align_left">propylamine</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-methylpentane</td>
<td class="ltx_td ltx_align_left">
$E$-2-pentene</td>
<td class="ltx_td ltx_align_left">
$p$-xylene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-methylpyridine</td>
<td class="ltx_td ltx_align_left">ethanethiol</td>
<td class="ltx_td ltx_align_left">pyridine</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-nitropropane</td>
<td class="ltx_td ltx_align_left">ethanol</td>
<td class="ltx_td ltx_align_left">pyrrolidine</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-octanone</td>
<td class="ltx_td ltx_align_left">ethylethanoate</td>
<td class="ltx_td ltx_align_left">
<span class="ltx_text ltx_font_italic">sec</span>-butanol</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-pentanone</td>
<td class="ltx_td ltx_align_left">ethylmethanoate</td>
<td class="ltx_td ltx_align_left">
$t$-butanol</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-propanol</td>
<td class="ltx_td ltx_align_left">ethylphenyl ether</td>
<td class="ltx_td ltx_align_left">
$t$-butylbenzene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">2-propen-1-ol</td>
<td class="ltx_td ltx_align_left">ethylbenzene</td>
<td class="ltx_td ltx_align_left">tetrachloroethene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">3-methylpyridine</td>
<td class="ltx_td ltx_align_left">ethylene glycol</td>
<td class="ltx_td ltx_align_left">tetrahydrofuran</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">3-pentanone</td>
<td class="ltx_td ltx_align_left">fluorobenzene</td>
<td class="ltx_td ltx_align_left">tetrahyrothiophenedioxide</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">4-heptanone</td>
<td class="ltx_td ltx_align_left">formamide</td>
<td class="ltx_td ltx_align_left">tetralin</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">4-methyl-2-pentanone</td>
<td class="ltx_td ltx_align_left">formic acid</td>
<td class="ltx_td ltx_align_left">thiophene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">4-methylpyridine</td>
<td class="ltx_td ltx_align_left">hexadecyliodide</td>
<td class="ltx_td ltx_align_left">thiophenol</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">5-nonanone</td>
<td class="ltx_td ltx_align_left">hexanoic acid</td>
<td class="ltx_td ltx_align_left">toluene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">acetic acid</td>
<td class="ltx_td ltx_align_left">iodobenzene</td>
<td class="ltx_td ltx_align_left">
<span class="ltx_text ltx_font_italic">trans</span>-decalin</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">acetone</td>
<td class="ltx_td ltx_align_left">iodoethane</td>
<td class="ltx_td ltx_align_left">tribromomethane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">acetonitrile</td>
<td class="ltx_td ltx_align_left">iodomethane</td>
<td class="ltx_td ltx_align_left">tributylphosphate</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">aniline</td>
<td class="ltx_td ltx_align_left">isobutanol</td>
<td class="ltx_td ltx_align_left">trichloroethene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">anisole</td>
<td class="ltx_td ltx_align_left">isopropyl ether</td>
<td class="ltx_td ltx_align_left">trichloromethane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">benzaldehyde</td>
<td class="ltx_td ltx_align_left">isopropylbenzene</td>
<td class="ltx_td ltx_align_left">triethylamine</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">benzene</td>
<td class="ltx_td ltx_align_left">isopropyltoluene</td>
<td class="ltx_td ltx_align_left">undecane</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">benzonitrile</td>
<td class="ltx_td ltx_align_left">
$m$-cresol</td>
<td class="ltx_td ltx_align_left">water</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">benzyl alcohol</td>
<td class="ltx_td ltx_align_left">mesitylene</td>
<td class="ltx_td ltx_align_left">
$Z$-1,2-dichloroethene</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left">bromobenzene</td>
<td class="ltx_td ltx_align_left">methanol</td>
<td class="ltx_td ltx_align_left">other</td>
</tr>
<tr class="ltx_tr">
<td class="ltx_td ltx_align_left ltx_border_tt" colspan="3">
${}^{a}$<span class="ltx_text" style="font-size:80%;">溶剂名称在指定时不应包含连字符或空格。</span>
</td>
</tr>
</table>

通过设置 **solvent** = **other**，用户可以指定自定义溶剂。这需要提供
以下溶剂描述符：

- •

**Dielec**，溶剂的介电常数 $\varepsilon$
- •

**SolN**，293 K 下光频折射率 $n_{20}^{D}$
- •

**SolA**，Abraham 氢键酸度 $\sum{\alpha}_{2}^{\text{H}}$
- •

**SolB**，Abraham 氢键碱度 $\sum{\beta}_{2}^{\text{H}}$
- •

**SolG**，$\gamma=\gamma_{m}/\gamma^{0}$
其中 $\gamma_{m}$ 是 298 K 下空气/溶剂界面的宏观表面张力，$\gamma^{0}$ 为 1 cal mol${}^{-1}$ Å${}^{-2}$
（1 dyne/cm = 1.43932 cal mol${}^{-1}$ Å${}^{-2}$）
- •

**SolC**，芳香性（$\phi$），即非氢溶剂原子中芳香碳原子所占的比例
- •

**SolH**，电负性"卤素性"（$\psi$），即非氢溶剂原子中 F、Cl 或 Br 所占的比例

这些参数在 *$smx* 输入节中按示例 11.2.9 所示的方式指定。
（*​$smx* 节中省略的任何溶剂描述符默认为零。）
其数值可来自实验，或通过对其他溶剂已有数据进行内插或外推获得。常见有机溶剂的
溶剂参数收录于 Minnesota 溶剂描述符数据库（Minnesota Solvent
Descriptor Database）。该数据库的最新版本可通过以下地址获取：

`http://comp.chem.umn.edu/solvation/mnsddb.pdf`

*$smx* 节中对 SM8、SM12 和 SMD 通用的作业控制变量如下所述。

### `Solvent`

> **设置 SM $x$ 溶剂 输入节：$smx**
>
> * **类型**: `STRING`
> * **默认值**: `water`
> * **可选值**:
>     * 表
>     * 11.7
>     * 所列溶剂列表中的任意名称
>     * 。
> * **建议**: 无

### `Print`

> **控制 SM $x$ 计算的额外输出 输入节：$smx**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * 0
>     * 最简输出
>     * 1
>     * 能量分项的详细分解（在 SCF 收敛时）
>     * 2
>     * 附加信息，取决于具体的 SM
>     * $x$
>     * 模型
> * **建议**: print = 1 得到的能量分项可能有用，尽管默认情况下已输出摘要。print = 2 的值可能仅用于诊断问题。

???+ example "示例 11.16: 使用用户自定义溶剂的 SMD 模型。"
    ```qchem
    $comment
    User-defined specification of pentane.
    (Result should be equivalent to SOLVENT = PENTANE)
    $end
    
    $molecule
       0 1
       C    -0.361658    -0.986967     0.222366
       C    -1.331098     0.144597    -0.108363
       O    -0.592574     1.354183     0.036738
       C     0.798089     1.070899     0.136509
       C     0.964682    -0.396154    -0.256319
       H    -0.625676    -1.925862    -0.267011
       H    -0.333229    -1.158101     1.302753
       H    -1.697529     0.068518    -1.140448
       H    -2.193412     0.181620     0.562129
       H     1.130199     1.238399     1.169839
       H     1.348524     1.754318    -0.514697
       H     1.050613    -0.489646    -1.343151
       H     1.843065    -0.855802     0.199659
    $end
    
    $rem
       METHOD           b3lyp
       BASIS            6-31G*
       SOLVENT_METHOD   smd
    $end
    
    $smx
    solvent other
    epsilon 1.840
    SolN    1.357
    SolA    0.000  ! could be omitted
    SolB    0.000  ! could be omitted
    SolG   22.300
    SolC    0.000  ! could be omitted
    SolH    0.000  ! could be omitted
    $end
    
    ```

## 11.2.9.1 SM8 模型

SM8 模型在文献 [[912]](../bib_references/bib.md#bib942)
 中有详细描述。
它可与密度泛函理论（**Q-Chem** 中可用的任意密度泛函）或 Hartree-Fock 理论
配合使用，但出于下文所述原因，仅 intended 与 6-31G*、6-31+G* 和 6-31+G**
基组配合使用。

SM8 中的宏观（连续介质）静电相互作用采用广义 Born（GB）SCRF 描述，[[569]](../bib_references/bib.md#bib580)

并使用由原子中心球构造的溶质空穴。对于 H、C、N、O、F、Si、P、S、Cl 和 Br 原子，
其原子半径是专为 SM8 优化过的，而对于其他原子则使用 Bondi 半径，[[146]](../bib_references/bib.md#bib136)
若原子未收录在 Bondi 的论文中，则取值为 2.0 Å。
几何相关的半径通过这些"内禀"库仑半径经去屏蔽（de-screening）近似计算得到。[[912]](../bib_references/bib.md#bib942)

除 GB 静电项外，SM8 标准态溶剂化自由能还包括若干其他贡献。其一是
电子-核-极化（electronic-nuclear-polarization, ENP）能，它是通常所称静电溶剂化能的
更贴切（且更精确）的名称。[[569]](../bib_references/bib.md#bib580)

溶剂化自由能的另一贡献来自与第一溶剂化层中溶剂分子的短程相互作用，
有时称为空穴化-色散-溶剂结构（cavitation–dispersion–solvent-structure, CDS）项。
各种 CDS 相互作用总体代表溶剂化能中的非静电贡献。

在 SM$x$ 模型中，这一非静电贡献被建模为与每个溶质原子的溶剂可及表面积
（solvent-accessible surface area, SASA）成正比的若干项之和。
这些比例常数是模型的参数，其单位为能量/(面积)${}^{2}$，
因此有时称为原子表面张力参数。溶质分子的 SASA 是由一个球形有效溶剂分子的球心
在溶质分子的 van der Waals 表面上滚动所产生的曲面面积，类似于 [11.2.3](topic_pcm-em.md) 节中提到的
溶剂可及表面。SASA 使用文献 [[835]](../bib_references/bib.md#bib868)
 中描述的算法，并配合 Bondi 的
van der Waals 半径值[[146]](../bib_references/bib.md#bib136)
 计算；若无可用的 Bondi 半径，则取
2.0 Å。（与 PCM 中非静电相互作用的情况一样，这意味着
宏观静电计算与非静电相互作用计算使用了不同的分子表面。）
用于生成 SASA 的溶剂探针半径对所有溶剂均设为 0.40 Å。注意，CDS 项中的
溶剂结构部分包含了诸多未被宏观静电学描述的溶剂结构效应，例如氢键、交换排斥，
以及第一溶剂化层中有效介电常数相对于其体相值的变化。CDS 项的经验性质
同时也弥补了以下因素引起的误差：($i$）假设内禀库仑半径取固定且依赖于模型的值，以及
($ii$）使用 GB 近似描述溶质–溶剂静电相互作用时产生的任何系统误差。

SM8 溶剂化自由能的最后一部分是浓度项。若溶质在气相与溶液相中的标准态浓度
相同（*e.g.*，在气相与溶液相中均为 1 mol/L），则该项为零。
否则，此校正可按理想气体公式计算，详见下文。

SM8 不要求用户为原子或基团指定分子力学原子类型；理论中的所有原子表面张力
都是溶质几何的唯一且连续函数，由模型定义并在 **Q-Chem** 内部计算。
原则上，只要能计算准确的partial charges，SM8 可与任意电子结构理论层次配合使用，
但 **Q-Chem** 对 SM8 的实现专门使用了自洽极化的 Charge Model 4 (CM4) 类 IV 电荷。[[678]](../bib_references/bib.md#bib702)

CM4 电荷由 Löwdin 布居分析电荷通过映射获得，映射参数取决于基组
（且仅取决于基组，与密度泛函或其他因素无关）。
**Q-Chem** 支持的基组为 6-31G*、6-31+G* 和 6-31+G**；
其他基组不应在 SM8 计算中使用。
电荷映射参数见文献 [[678]](../bib_references/bib.md#bib702)
。

SM8 溶剂化自由能按 $T=298$ K、气相与溶液相标准态浓度均为 1 M 输出。
然而，文献中的溶剂化自由能常采用气相 $P=1$ atm 的标准态。若要将 298 K 下
1 M→1 M 的溶剂化自由能转换为气相 $P=1$ atm、溶液相浓度 1 M 的标准态，
需在计算得到的溶剂化自由能上加上 $+1.89$ kcal/mol。

可以进行溶液相几何优化，但不支持使用球谐 $d$ 函数或角动量高于 $d$
（$f$、$g$、*etc.*）的基组。由于按定义 6-31G*、6-31+G* 和 6-31+G**
基组均采用笛卡尔 $d$ 壳层，因此它们是可配合 SM8 进行几何优化的基组示例。
溶液相 Hessian 计算可通过对解析能量梯度进行数值微分，或通过对能量进行二次微分来完成，
不过前一种方法既更稳定又更经济。SM8 的解析梯度基于极化自由能的解析导数
以及文献 [[1577]](../bib_references/bib.md#bib1640)
 中导出的 CDS 项解析导数。

SM8 测试套件包含以下代表性示例：

- •

2,2-dichloroethenyl dimethyl phosphate 在水中的单点溶剂化能与解析梯度计算，
方法为 M06-2X/6-31G*；
- •

2,2-dichloroethenyl dimethyl phosphate 在苯中的单点溶剂化能计算，
方法为 M06-2X/6-31G*；
- •

2,2-dichloroethenyl dimethyl phosphate 在乙醇中的单点溶剂化能计算，
方法为 M06-2X/6-31G*；
- •

5-fluorouracil 在水中的单点溶剂化能计算，方法为 M06/6-31+G*；
- •

5-fluorouracil 在辛醇中的单点溶剂化能计算，方法为 M06-L/6-31+G*；
- •

5-fluorouracil 在氟苯中的单点溶剂化能与解析梯度计算，方法为 M06-HF/6-31+G**；
- •

质子化甲醇 $\rm CH_{3}OH_{2}^{+}$ 在水中的几何优化，方法为 B3LYP/6-31G*；
- •

质子化甲醇 $\rm CH_{3}OH_{2}^{+}$ 在水中的有限差分频率计算（含解析梯度），方法为 B3LYP/6-31G*。

希望计算溶解度的用户可以根据溶剂化自由能，采用文献 [[1358]](../bib_references/bib.md#bib1418)
 中描述的方法进行计算。
本模型也可放心地用于计算分配系数（*e.g.*，亨利定律常数、
正辛醇/水分配系数等），方法见文献

。

用户应注意，当前版本 **Q-Chem** 中 SM8 模型计算的溶剂化自由能均为
所谓平衡溶剂化自由能。用于垂直激发能的非平衡算法[[813]](../bib_references/bib.md#bib846)

尚未在 **Q-Chem** 中实现。（PCM 提供了相应的非平衡版本，见 [11.2.3.3](topic_pcm-em.md#subsubsec:noneq-PCM) 节。）

## 11.2.9.2 SM12 模型

SM12 模型[[910]](../bib_references/bib.md#bib946)
 在 **Q-Chem** 中同样可用。与
SM8 类似，它采用（a）广义 Born 近似处理溶剂化自由能的宏观静电贡献，
以及（b）相同形式的 CDS 贡献公式（参数经过重新优化）。SM12 相较于 SM8
具有若干优势，其中最重要的可能是它在宏观静电项中使用了 CM5 电荷，[[911]](../bib_references/bib.md#bib945)
CM5 电荷基于 Hirshfeld 布居分析，或使用由静电势导出的电荷，[[1258]](../bib_references/bib.md#bib1310)
这些电荷对基组的扩展是稳定的，因此 SM12 可以使用更大的基组，而 SM8 由于
Löwdin 电荷在较大基组中的不稳定性，仅限于 6-31G*、6-31+G* 和 6-31+G**。
此外，与 SM8 相比，SM12 使用更多样化的训练集进行参数化，并且覆盖整个元素周期表。
然而，**Q-Chem** 目前尚不提供 SM12 的解析梯度。

通过在 *$rem* 节中设置 SOLVENT_METHOD = SM12 来请求 SM12 计算。
静电项的计算方式由 *$smx* 输入节中的 **Charges** 关键字控制。

### `Charges`

> **设置 SM12 静电项所用原子电荷的类型。输入节：$smx**
>
> * **类型**: `STRING`
> * **默认值**: `CM5`
> * **可选值**:
>     * CM5
>     * Charge Model 5 电荷，
>     * 参见 911
>     * Marenich A. V. 等，
>     * J. Chem. Theory Comput.
>     * (2012)
>     * ，
>     * 第 8
>     * 卷，
>     * 第 527 页
>     * 。链接
>     * MK
>     * Merz-Singh-Kollman 电荷，
>     * 参见 1258
>     * Singh U. C.、Kollman P. A.，
>     * J. Comput. Chem.
>     * (1984)
>     * ，
>     * 第 5
>     * 卷，
>     * 第 129 页
>     * 。链接
>     * CHELPG
>     * ChElPG 电荷，
>     * 参见 159
>     * Breneman C. M.、Wiberg K. B.，
>     * J. Comput. Chem.
>     * (1990)
>     * ，
>     * 第 11
>     * 卷，
>     * 第 361 页
>     * 。链接
> * **建议**: 无。Merz-Singh-Kollman 电荷和 ChElPG 电荷分别通过拟合以重现 van der Waals 表面上或立方网格上的分子静电势获得，而 CM5 是基于 Hirshfeld 布居分析的经验模型。

???+ example "示例 11.17: 使用 SM12CM5 计算水在 1-octanol 溶剂中的溶剂化自由能。"
    ```qchem
    $molecule
       0 1
       O    0.000000    0.125787   0.000000
       H    0.758502   -0.503148   0.000000
       H   -0.758502   -0.503148   0.000000
    $end
    
    $rem
       METHOD               b3lyp
       BASIS                6-31G*
       SCF_GUESS            core
       SOLVENT_METHOD       sm12
       POINT_GROUP_SYMMETRY false
    $end
    
    $smx
       solvent 1octanol
       charges chelpg
    $end
    ```

## 11.2.9.3 SMD 模型

SMD 模型[[909]](../bib_references/bib.md#bib943)
 在 **Q-Chem** 中同样可用。在该模型的
原始版本中，溶剂化自由能的静电贡献通过 IEF-PCM 模型描述，而 CDS 贡献遵循与 SM8
和 SM12 相同的公式，只是参数经过重新优化以与 IEF-PCM 静电学相容。相对于
静电相互作用以依赖于基组选择的原子点电荷定义的 SM8 或 SM12（因此这两个模型
仅支持特定的基组），SMD 可与任意基组配合使用。

**Q-Chem** 对 SMD 模型的实现默认使用更简单的 C-PCM 模型，与 SOLVENT_METHOD = PCM
相同。基于文献 [[569]](../bib_references/bib.md#bib580)
 表 4 中给出的基准测试结果，
C-PCM 的结果在精度上与 IEF-PCM 的结果基本没有差别。
通过在 *$rem* 节中设置 SOLVENT_METHOD = SMD 可请求 SMD 的能量、
梯度或 Hessian 计算。虽然 **Q-Chem** 用户可以修改 SMD 计算中 C-PCM 或 IEF-PCM
部分的参数，但不推荐这样做，因为此类修改可能与 CDS 参数不够相容，
从而导致结果精度下降。对于 SMD 计算，C-PCM 是首选的静电学模型。
从 **Q-Chem** v. 6.3 开始，提供了半数值 SMD Hessian，
其使用 C-PCM 解析 Hessian[[844]](../bib_references/bib.md#bib876)
 并结合 CDS 贡献的有限差分求值。

在 **Q-Chem** v. 5.2 及更高版本中，默认的表面离散化方法由 VTN 改为 SwiG，
以保证势能面的光滑性。此外，在 SM$x$ 计算之前进行的气相 SCF 计算默认关闭。
若需要获得溶剂化自由能，则仍需要进行气相计算，可通过设置 SMX_GAS_PHASE = TRUE
来开启。若直接使用 SM$x$ 模型收敛 SCF 存在困难，将该 *$rem*
变量设为 TRUE 也可能有所帮助。

SMX_GAS_PHASE

### `SMX_GAS_PHASE`

> **在使用 SM $x$ 模型进行计算之前先收敛气相 SCF**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * FALSE
>     * 直接运行 SMx 计算
>     * TRUE
>     * 先运行气相计算
> * **建议**: 除非需要溶剂化自由能，否则使用默认值。若 SCF 计算否则无法收敛，则将其设为 TRUE。

???+ example "示例 11.18: 四氢呋喃（THF）在戊烷溶剂中的 SMD 力计算。"
    ```qchem
    $molecule
       0 1
       C    -0.361658    -0.986967     0.222366
       C    -1.331098     0.144597    -0.108363
       O    -0.592574     1.354183     0.036738
       C     0.798089     1.070899     0.136509
       C     0.964682    -0.396154    -0.256319
       H    -0.625676    -1.925862    -0.267011
       H    -0.333229    -1.158101     1.302753
       H    -1.697529     0.068518    -1.140448
       H    -2.193412     0.181620     0.562129
       H     1.130199     1.238399     1.169839
       H     1.348524     1.754318    -0.514697
       H     1.050613    -0.489646    -1.343151
       H     1.843065    -0.855802     0.199659
    $end
    
    $rem
       JOBTYPE          force
       METHOD           b3lyp
       BASIS            6-31G*
       SOLVENT_METHOD   smd
    $end
    
    $smx
       solvent pentane
    $end
    ```
