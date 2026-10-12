---
title: "10.3.1 NBO 程序包接口"
---

## 10.3.1 NBO 程序接口

（2026 年 7 月 4 日）

**Q-Chem** 内置了自然键轨道（Natural Bond Orbital, NBO）程序包的第 5 版（v. 5），用于分子性质与波函数分析[[459]](../bib_references/bib.md#bib471)，

并且也可以与 NBO 程序的第 6 版（v. 6）[[459]](../bib_references/bib.md#bib471)
 及第 7 版（v. 7）[[460]](../bib_references/bib.md#bib473)
 进行接口调用。
只需在 *$rem* 段中设置 NBO = TRUE 即可调用 NBO5 程序包，它会在求得自洽场（SCF）波函数之后启动。
若在几何优化过程中开启该选项，NBO5 程序只会在最后一个优化步结束后被调用一次。

若要使用 NBO6 或 NBO7，必须从 [nbo.chem.wisc.edu](https://nbo.chem.wisc.edu) 单独购买、下载并安装所需版本的 NBO 程序。
随后可通过以下方式让 **Q-Chem** 与外部版本的 NBO 程序进行接口调用：
(a) 正确设置 `NBOEXE` 环境变量，以及
(b) 在 **Q-Chem** 输入文件的 *$rem* 段中同时设置 NBO = TRUE 和 NBO_EXTERNAL = TRUE。
请注意，NBO6 程序的支持（以及新的下载服务）已于 2020 年停止。已有的副本仍应能与 **Q-Chem** 正常接口调用，
而较新的 NBO7 程序也应以相同的方式进行接口。较旧的 NBO5 程序仍然是 **Q-Chem** 的组成部分，
如果仅设置 NBO = TRUE 而未指定 NBO_EXTERNAL，则运行的就是 NBO5。

用户应查阅 NBO 用户手册（NBO User's Manual）以获取与 NBO 计算相关的选项和详细信息。
NBO 分析同样可用于采用构型相互作用单激发（CIS）或含时密度泛函理论（TDDFT）计算的激发态。
激发态的 NBO 分析发展尚不够完善，用户应当注意，激发态下 NBO 搜索过程的收敛性可能不如基态那样良好。
激发态可能需要在下文所述的 *$nbo* 段中指定额外的 NBO 参数。
详情请参阅参考文献

。

### `NBO`

> **控制是否使用 NBO 程序包。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * `0`: 不调用 NBO 程序包。
>     * `1`: 调用 NBO 程序包，针对基态进行分析。
>     * `2`: 对基态以及每一个 CIS、RPA 或 TDDFT 激发态调用 NBO 程序包。
> * **建议**: 无

### `NBOMEMORY`

> **控制为 Q-Chem 内部 NBO（v. 5）程序包分配多少内存。**
>
> * **类型**: `INTEGER`
> * **默认值**: `500000`
> * **选项**:
>     * $N$: 分配 $N$ 个双精度字（即 $8N$ 字节）。
> * **建议**: 这部分内存从 MEM_TOTAL 中扣除。

**Q-Chem** 向 NBO 程序传递选项的通用格式如下所示：

> ```qchem
> $nbo
>    {NBO program keywords, parameters and options}
> $end
> ```

几点使用说明：

1. 1.

在 *$nbo* 关键字被识别之前，*rem* 变量 NBO 必须先设置为 TRUE。
2. 2.

**Q-Chem** 不支持需要多次作业运行（multiple job runs）的 NBO 程序包功能。
3. 3.

可通过 PRINT_ORBITALS 和 MOLDEN_FORMAT 关键字触发 NBO 的输出。此时会向 *outfile* 写入两个 MOLDEN 段。
第一个对应常规分子轨道（MO），第二个对应自然键轨道（NBO）。
4. 4.

可通过在 $nbo 段中使用 PLOT 关键字触发输出完整的自然原子轨道（NAO）、自然杂化轨道（NHO）、自然键轨道（NBO）和自然定域分子轨道（NLMO）集合。
相关文件为 `$QCSCRATCH/savename` 中的 `FILE.31` – `FILE.39`。
这些文件可以由 **ChemCraft** 和 **JMol** 等程序打开。
5. 5.

**Q-Chem** 内部实现的 NBO v. 5 最多支持 300 个原子和 3,000 个基函数。

???+ example "示例 10.12: 甲醛（formaldehyde）NBO 计算的基本输入。
NBO 以 MolDen 格式打印到 outfile 中，完整的原生 NBO 格式文件写入 $QCSCRATCH/savename 。"
    ```qchem
    $molecule
       0 1
       C    0.000000    0.000000    0.523383
       O    0.000000    0.000000   -0.671856
       H    0.931138    0.000000    1.117280
       H   -0.931138    0.000000    1.117280
    $end
    
    $rem
       METHOD           pbe0
       BASIS            def2-sv(p)
       NBO              1
       PRINT_ORBITALS   true
       MOLDEN_FORMAT    true
    $end
    
    $nbo
       PLOT
    $end
    ```

???+ example "示例 10.13: 以自然原子轨道（NAO）基底给出正则分子轨道（canonical MOs）的 NBO 计算。
这是确定每个正则 MO 中原子轨道（AO）成分百分比的一种简便方法。"
    ```qchem
    $molecule
       0 1
       C    0.000000    0.000000    0.523383
       O    0.000000    0.000000   -0.671856
       H    0.931138    0.000000    1.117280
       H   -0.931138    0.000000    1.117280
    $end
    
    $rem
       METHOD           pbe0
       BASIS            def2-sv(p)
       NBO              true
    $end
    
    $nbo
       naomo
    $end
    ```
