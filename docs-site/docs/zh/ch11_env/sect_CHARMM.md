---
title: "11.4 Q-Chem/Charmm 接口"
---

# 11.4 **Q-Chem**/**Charmm** 接口

（2026 年 7 月 4 日）

**Q-Chem** 可以作为使用 **Charmm** 软件包进行的 QM/MM（量子力学/分子力学）计算的 QM 后端。[[1492]](../bib_references/bib.md#bib1551)
在这种情况下，执行计算需要同时使用这两个软件包，但程序之间通信所需的全部代码
均已包含在发布版本中。独立的 QM/MM 计算在第 [11.3](sec_QMMM.md) 节中描述。

使用 **Charmm** 接口的 QM/MM 作业通过以下 *$rem* 关键字进行控制：

QM_MM

### `QM_MM`

> **开启 Q-Chem / Charmm 接口。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 通过
>     * Q-Chem
>     * /
>     * Charmm
>     * 接口执行 QM/MM 计算。
>     * FALSE
>     * 关闭此功能。
> * **建议**：除非使用 Charmm 运行计算，否则使用默认值。

QMMM_PRINT

### `QMMM_PRINT`

> **控制 QM/MM 作业输出信息的多少。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 限制分子、点电荷以及分析信息的打印。
>     * FALSE
>     * 正常打印。
> * **建议**：除非使用 Charmm 运行计算，否则使用默认值。

QMMM_CHARGES

### `QMMM_CHARGES`

> **控制是否将 QM 电荷打印到文件。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 写入一个 charges.dat 文件，其中包含来自 QM 区域的 Mulliken 电荷。
>     * FALSE
>     * 不写入文件。
> * **建议**：除非使用 Charmm 运行计算且需要保存 QM 区域上的电荷，否则使用默认值。

ESP_EFIELD

### `ESP_EFIELD`

> **触发在 MM 电荷位置上计算静电势（ESP）和/或电场。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 仅计算 ESP。
>     * 1
>     * 计算 ESP 和电场。
>     * 2
>     * 仅计算电场。
> * **建议**：无。

GEOM_PRINT

### `GEOM_PRINT`

> **控制在每一步打印的几何信息量。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 打印所有几何信息；键长、键角、二面角。
>     * FALSE
>     * 正常打印距离矩阵。
> * **建议**：如果你希望在优化的开始和结束阶段快速查看几何参数，则使用此项。在单点能计算中仅在开始时打印。

QMMM_FULL_HESSIAN

### `QMMM_FULL_HESSIAN`

> **触发对完整 QM/MM Hessian（黑塞矩阵）的求值。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 求值完整的 Hessian。
>     * FALSE
>     * 仅求值 QM-QM 分块的 Hessian。
> * **建议**：无

LINK_ATOM_PROJECTION

### `LINK_ATOM_PROJECTION`

> **控制是否执行连接原子（link atom）投影**
>
> * **类型**：`LOGICAL`
> * **默认值**：`TRUE`
> * **选项**：
>     * TRUE
>     * 执行投影
>     * FALSE
>     * 不执行投影
> * **建议**：在对含有连接原子的体系求值完整的 QM/MM Hessian 时是必需的

HESS_AND_GRAD

### `HESS_AND_GRAD`

> **在单个作业中同时启用解析梯度与 Hessian 的求值**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 同时求值梯度和 Hessian。
>     * FALSE
>     * 仅求值 Hessian。
> * **建议**：仅在频率计算（因而需要 Hessian）中使用。

GAUSSIAN_BLUR

### `GAUSSIAN_BLUR`

> **在 QM/MM 计算中启用高斯离域的外电荷。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 用高斯函数使外电荷离域。
>     * FALSE
>     * 点电荷
> * **建议**：无

SKIP_CHARGE_SELF_INTERACT

### `SKIP_CHARGE_SELF_INTERACT`

> **忽略 QM/MM 计算中各外电荷之间的静电相互作用。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 外电荷之间不存在静电相互作用。
>     * FALSE
>     * 计算外电荷之间的静电相互作用。
> * **建议**：无

???+ example "示例 11.27：对水二聚体进行基本的 QM/MM 优化。你需要 Charmm 才能完成此计算，
但这里是测试 QM/MM 功能所需的 Q-Chem 文件。这些是进行 Q-Chem / Charmm QM/MM 计算所必需的最少内容。"
    ```qchem
    $molecule
       0 1
       O    -0.91126   1.09227   1.02007
       H    -1.75684   1.51867   1.28260
       H    -0.55929   1.74495   0.36940
    $end
    
    $rem
       METHOD        hf        ! HF Exchange
       BASIS         cc-pvdz   ! Correlation Consistent Basis
       QM_MM         true      ! Turn on QM/MM calculation
       JOBTYPE       force     ! Need this for QM/MM optimizations
    $end
    
    $external_charges
       1.20426      -0.64330   0.79922  -0.83400
       1.01723      -1.36906   1.39217   0.41700
       0.43830      -0.06644   0.91277   0.41700
    $end
    ```

**Q-Chem**/**Charmm** 接口的独特之处在于：

- •

外点电荷可以被替换为具有有限宽度的高斯离域电荷。[[300]](../bib_references/bib.md#bib304)
这是一种经验性的方法，用于纳入 MM 区域中原子电子密度的离域特征。这对于 QM 区域
与 MM 区域中邻近原子之间的静电相互作用可能很重要。
- •

我们支持求值完整的 QM/MM Hessian。[[1491]](../bib_references/bib.md#bib1552)

当插入连接原子（link atoms）以饱和 QM 区域时，与连接原子相关的所有 Hessian 元素
都会自动投影到其 QM 与 MM 宿主原子上。
- •

对于含有大量 MM 原子的体系，可以定义由多个 MM 原子组成的块（*即*，移动块，mobile blocks），
并高效地求值相应的移动块 Hessian（MBH）以进行简正模式分析。
