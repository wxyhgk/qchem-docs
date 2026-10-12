---
title: "9.8.2 作业控制与示例"
---

## 9.8.2 作业控制与示例

（2026 年 7 月 4 日）

为了执行非绝热耦合（nonadiabatic coupling）计算，必须给出 *$derivative_coupling* 段：

> ```qchem
> $derivative_coupling
> <one line comment>
> i, j, k, ...
> $end
> ```

随后将在所列状态 $i,j,k,\ldots$ 之间所有两两组合上计算非绝热耦合；使用 “0” 表示请求 HF 或 DFT 参考态，“1” 表示第一激发态，依此类推。注意，导数耦合（derivative coupling）的量纲为长度的倒数，并以原子单位（atomic unit）打印输出，*即*，bohr${}^{-1}$。

### `CALC_NAC`

> **决定是否计算非绝热耦合。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 计算非绝热耦合。
>     * FALSE
>     * 不计算非绝热耦合。
> * **建议**：无。

### `CIS_DER_NUMSTATE`

> **决定在多少个状态之间计算非绝热耦合。这些状态必须在 $derivative_coupling 段中指定。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 不计算非绝热耦合。
>     * $n$
>     * 计算
>     * $n(n-1)/2$
>     * 组非绝热耦合。
> * **建议**：无。

### `SET_QUADRATIC`

> **决定是否为含时密度泛函理论（TD-DFT）计算包含完整的二次响应（quadratic response）贡献。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 为 TD-DFT 包含完整的二次响应贡献。
>     * FALSE
>     * 采用伪波函数（pseudo-wave function）方法。
> * **建议**：伪波函数方法通常已具有足够的精度，并且不存在偶然奇点（accidental singularity）。更多指导请参阅文献 1548 Zhang X., Herbert J. M. J. Chem. Phys. (2015) , 142 , pp. 064109 . 链接 以及 1029 Ou Q. et al. J. Chem. Phys. (2015) , 142 , pp. 064114 . 链接。

???+ example "示例 9.26: 在 TD-B3LYP 层次上采用伪波函数方法计算乙烯最低五个单重态之间的非绝热耦合。"
    ```qchem
    $molecule
       0 1
       C    1.85082356   -1.78953123    0.00000000
       H    2.38603593   -2.71605577    0.00000000
       H    0.78082359   -1.78977646    0.00000000
       C    2.52815456   -0.61573833    0.00000000
       H    1.99294220    0.31078621    0.00000000
       H    3.59815453   -0.61549310    0.00000000
    $end
    
    $rem
       EXCHANGE           b3lyp
       BASIS              6-31G*
       CIS_N_ROOTS        4
       CIS_TRIPLETS       false
       MAX_CIS_CYCLES     50
       CIS_DER_NUMSTATE   5
       CALC_NAC           true
    $end
    
    $derivative_coupling
       0 is the reference state
       0 1 2 3 4
    $end
    ```

???+ example "示例 9.27: 使用 BH&HLYP 与自旋反转 TD-DFT（spin-flip TDDFT）计算乙烯 $S_{1}$ 与 $S_{3}$ 态之间的非绝热耦合。"
    ```qchem
    $molecule
       0 3
       C    1.85082356   -1.78953123    0.00000000
       H    2.38603593   -2.71605577    0.00000000
       H    0.78082359   -1.78977646    0.00000000
       C    2.52815456   -0.61573833    0.00000000
       H    1.99294220    0.31078621    0.00000000
       H    3.59815453   -0.61549310    0.00000000
    $end
    
    $rem
       EXCHANGE           bhhlyp
       BASIS              6-31G*
       SPIN_FLIP          true
       UNRESTRICTED       true
       CIS_N_ROOTS        4
       CIS_TRIPLETS       false
       MAX_CIS_CYCLES     50
       CIS_DER_NUMSTATE   2
       CALC_NAC           true
    $end
    
    $derivative_coupling
       comment
       1 3
    $end
    ```

???+ example "示例 9.28: 在 TD-B3LYP 层次上通过二次响应理论计算乙烯 $S_{1}$ 与 $S_{2}$ 态之间的非绝热耦合。"
    ```qchem
    $molecule
       0 1
       C    1.85082356   -1.78953123    0.00000000
       H    2.38603593   -2.71605577    0.00000000
       H    0.78082359   -1.78977646    0.00000000
       C    2.52815456   -0.61573833    0.00000000
       H    1.99294220    0.31078621    0.00000000
       H    3.59815453   -0.61549310    0.00000000
    $end
    
    $rem
       EXCHANGE          b3lyp
       BASIS             6-31G*
       CIS_N_ROOTS       4
       CIS_TRIPLETS      false
       RPA               true
       MAX_CIS_CYCLES    50
       CIS_DER_NUMSTATE  2
       CALC_NAC          true
       SET_QUADRATIC     true ! include full quadratic response
    $end
    
    $derivative_coupling
       comment
       1 2
    $end
    ```
