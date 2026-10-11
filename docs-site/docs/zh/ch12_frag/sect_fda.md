---
title: "12.7.4 ALMO 受力分解分析"
---

## 12.7.4 ALMO 受力分解分析

（2026 年 7 月 4 日）

在绝热能量分解分析（EDA）（第 [12.7.3](sect_adiabatic_eda.md) 节）取得成功的基础上，可以引入一种类似的扩展方法，对任意几何结构下的受力进行分解。与绝热 EDA 中追踪受力以生成几何结构并在该几何结构下评估能量不同，受力分解分析直接在给定几何结构下对受力本身进行分解和分析。这种方法带来了一个重要的特性，即能够对冻结（frozen）受力进行分解，从而揭示与几何变化相关的冻结分量。这种分解在绝热 EDA 中是没有意义的，因为例如单纯沿着吸引力的方向追踪会导致分子相互坍缩。

Aldossary *等* 的工作实现了经典静电能的解析导数 [[36]](../bib_references/bib.md#bib21)
，使得冻结受力可以被拆分为经典静电作用力和范德华（vdW，包括泡利与色散）力：

<a id="eq:Ffrz_decomp"></a>

$$
\Delta\mathbf{F}_{\text{frz}}=\Delta\mathbf{F}_{\text{cls-elec}}+\Delta\mathbf{F}_{\text{vdw}}. \tag{12.32}
$$

此外，现在对冻结受力的定义会减去几何畸变受力（由几何畸变能产生的力）。冻结受力项现在为：

<a id="eq:Ffrz"></a>

$$
\Delta\textbf{F}_{\text{frz}}=\textbf{F}_{\text{frz}}[\mathbf{P}_{\text{frz}}]-\sum_{A}\textbf{F}_{A}[\textbf{P}_{A}], \tag{12.33}
$$

其中等式右侧的第二项即为几何畸变受力。与几何畸变能类似，几何畸变受力是从孤立片段几何结构的受力中减去的，而对于几何极小点，这些孤立几何结构的受力为零。换句话说，几何畸变受力正是孤立片段在复合物几何结构下的受力。几何畸变受力会被单独打印出来以便分析。

通过将分子间受力分解为几何畸变、静电作用、范德华作用、极化和电荷转移五部分，我们现在生成了比普通受力计算多 5 倍的受力。这些 $5(3N)$ 个力可能难以人工分析，因此我们使用内坐标来对这些受力作出化学意义上的解读。Wilson 的 B 矩阵由新的 opt3 库生成，我们采用通常的变换。随后用户可以聚焦于感兴趣的键、键角或二面角，分析哪些受力分量与拉伸或压缩相关。尽管冗余内坐标非常有用，但它们并不是唯一的，并且输入文件中原子的排列顺序可能会影响结果。

FDA

### `FDA`

> **分解分子间受力**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 执行普通的受力计算。
>     * TRUE
>     * 调用受力分解分析方法
> * **建议**: 将其设为 TRUE 并配合 jobtype=force 以分解受力。

???+ example "示例 12.34: 使用内坐标对 H ${}_{2}$ O $\cdots$ F ${}^{-}$ 体系进行受力分解分析计算"
    ```qchem
    $molecule
    -1 1
    --
    0 1
    O       0.0144306160     0.0000000000     0.0991268524
    H      -0.0433242925     0.0000000000     1.2143531865
    H       0.9756708294     0.0000000000    -0.0327279220
    --
    -1 1
    F      -0.0237828221    -0.0000000000     2.5253092017
    $end
    
    $rem
    JOBTYPE      FORCE
    FDA          TRUE
    GEN_SCFMAN   TRUE
    METHOD       PBE
    BASIS        def2-svp
    MEM_TOTAL    2000
    MEM_STATIC   500
    SCF_GUESS    FRAGMO
    BASIS_LIN_DEP_THRESH  6
    SCFMI_MODE            0
    SCF_PRINT_FRGM        TRUE
    SCF_CONVERGENCE       10
    THRESH                14
    INTEGRAL_SYMMETRY     FALSE
    POINT_GROUP_SYMMETRY  FALSE
    $end
    
    ```
