---
title: "5.12.2 导数间断性恢复"
---

## 5.12.2 导数间断性恢复（Derivative Discontinuity Restoration）

（2026 年 7 月 4 日）

Chai 和 Chen[[222]](../bib_references/bib.md#bib227)从微扰理论的角度出发，提出了一套系统化的程序，用于计算 Kohn-Sham 密度泛函理论（Kohn-Sham Density Functional Theory, KS-DFT）中交换-关联（exchange-correlation）能量泛函的导数间断性（derivative discontinuity），原则上通过将所有微扰修正项求和至无穷阶即可获得精确的导数间断性。将微扰级数在低阶截断，可得到一种高效计算近似导数间断性的方案。特别地，一阶修正项等价于冻结轨道近似（frozen-orbital approximation）方法。目前在 **Q-Chem** 中的实现仅支持局域泛函和广义梯度近似（Generalized Gradient Approximation, GGA）泛函，不支持/meta-GGA、杂化（hybrid）或非局域（non-local）泛函。作业控制变量及示例如下所示。

FOA_FUNDGAP

### `FOA_FUNDGAP`

> **计算基本能隙（fundamental gap）的冻结轨道近似值。**
>
> * **类型**: `Boolean`
> * **默认值**: `FALSE`
> * **可选值**:
>     * FALSE
>     * 不计算冻结轨道近似（FOA）的导数间断性与基本能隙。
>     * TRUE
>     * 计算并输出 FOA 基本能隙信息。隐含设置
>     * KS_GAP_PRINT
>     * 为真。
> * **建议**: 若设为真，请与 KS_GAP_UNIT 配合使用。

KS_GAP_PRINT

### `KS_GAP_PRINT`

> **控制（广义 Kohn-Sham, generalized Kohn-Sham）HOMO-LUMO 能隙信息的输出。**
>
> * **类型**: `Boolean`
> * **默认值**: `false`
> * **可选值**:
>     * false
>     * （默认）不输出能隙信息
>     * true
>     * 输出能隙信息
> * **建议**: 若设为真，请与 KS_GAP_UNIT 配合使用。

KS_GAP_UNIT

### `KS_GAP_UNIT`

> **KS_GAP_PRINT 和 FOA_FUNDGAP 所使用的单位（见 5.12.2 节）**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * 0
>     * （默认）Hartree（原子单位）
>     * 1
>     * eV（电子伏特）
> * **建议**: 无

???+ example "示例 5.29: 使用 PBE 和 LFAs-PBE 泛函对碳原子进行导数间断性的冻结轨道近似计算。"
    ```qchem
    $comment
        Frozen-orbital derivative discontinuity, C atom, PBE
    $end
    
    $molecule
       0 3
       C
    $end
    
    $rem
       BASIS         6-31G*
       METHOD        PBE
       FOA_FUNDGAP   true
       KS_GAP_UNIT   1    ! print gap info in eV
       THRESH        14
    $end
    
    @@@
    
    $comment
       with LFAs-PBE functional instead
    $end
    
    $molecule
       READ
    $end
    
    $rem
       BASIS         6-31G*
       SCF_GUESS     READ
       EXCHANGE      gen
       FOA_FUNDGAP   true
       KS_GAP_UNIT   1
       THRESH        14
    $end
    
    $xc_functional
       X   PBE    1.0
       X   LFAs   1.0
       C   PBE    1.0
    $end
    ```
