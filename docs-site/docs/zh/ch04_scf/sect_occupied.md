---
title: "4.4.4 修改占据分子轨道"
---

## 4.4.4 修改占据分子轨道

（2026 年 7 月 4 日）

有时让初始猜测（guess）占据轨道不按最低的 $N_{\alpha}$（或 $N_{\beta}$）个轨道来排布是 useful 的。可能需要这样做的理由包括：

- -

用于收敛到不同对称性或不同轨道占据的态。
- -

用于破坏空间对称性。
- -

用于破坏自旋对称性，例如在电子数为偶数的分子上进行非限制（unrestricted）计算。

有两种机制可以修改一组猜测轨道：要么通过 SCF_GUESS_MIX，要么通过指明确定要占据的轨道。**Q-Chem**
用户可以借助 *$occupied* 或 *$swap_occupied_virtual* 关键字来定义占据的猜测轨道。在前者中，通过在第一行列出要占据的 $\alpha$ 轨道、第二行列出 $\beta$ 轨道来定义占据的猜测轨道。在后者中，只需指明需要交换（swap）的那一对轨道。

**注意：

(1) 为阻止 **Q-Chem** 在 SCF 过程中改变轨道占据，通常将 MOM_START 选项与
*$occupied* 或 *$swap_occupied_virtual* 关键字配合使用。
(2) 这些选项对轨道的需求使其与 SAD 猜测不相容。最常见的做法是将其与 SCF_GUESS = READ 一起使用。
**

修改占据猜测轨道的格式如下：

> ```qchem
> $occupied
>    1  2  3  4 ...  NAlpha
>    1  2  3  4 ...  NBeta
> $end
> ```

或者 alternatively 使用

> ```qchem
> $swap_occupied_virtual
>    <spin> <io1> <iv1>
>    <spin> <io2> <iv2>
> $end
> ```

占据轨道与虚轨道之间也可以进行交换

> ```qchem
> $swap_occupied_virtual
>    alpha  5  6
>    beta   6  7
> $end
> ```

这与下面的写法等价

> ```qchem
> $occupied
>    1 2 3 4 6 5 7
>    1 2 3 4 5 7 6
> $end
> ```

或者

> ```qchem
> $occupied
>    1:4 6 5 7
>    1:5 7 6
> $end
> ```

*$rem* 中其他与改变轨道占据相关的变量有：

### `SCF_GUESS_PRINT`

> **控制猜测分子轨道（MO）、Fock 矩阵与密度矩阵的打印输出。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * 0
>     * 不打印猜测结果。
>     * SAD
>     * 1
>     * 原子密度矩阵与分子矩阵。
>     * 2
>     * 在级别 1 的基础上增加密度矩阵。
>     * CORE 和 GWH
>     * 1
>     * 无额外输出。
>     * 2
>     * 在级别 1 的基础上增加 Fock 矩阵与密度矩阵，以及 MO 系数和本征值。
>     * READ
>     * 1
>     * 无额外输出
>     * 2
>     * 在级别 1 的基础上增加密度矩阵、MO 系数和本征值。
> * **建议**：无

### `SCF_GUESS_MIX`

> **控制将 LUMO 与 HOMO 混合以在初始猜测中破坏对称性。对于非限制（unrestricted）任务，仅对 alpha 轨道进行混合。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0 (FALSE)`
> * **可选值**：
>     * 0 (FALSE)
>     * 不在 SCF 猜测中混合 HOMO 与 LUMO。
>     * 1 (TRUE)
>     * 向 HOMO 中加入 10% 的 LUMO 以破坏对称性。
>     * $n$
>     * 向 HOMO 中加入
>     * $10n$
>     * % 的 LUMO（
>     * $0<n<10$
>     * ）。
> * **建议**：在对电子数为偶数的分子进行非限制计算时，通常需要用此选项，或在输入中指定 $occupied，来破坏初始猜测中的 alpha/beta 对称性。

???+ example "示例 4.6: H ${}_{2}$ 在解离极限下非限制 HF 计算的输入，
演示 SCF_GUESS_MIX = 2 的用法（相当于将 20% 的 alpha LUMO 混合进 alpha HOMO）。
使用带 DIIS 的几何直接极小化（geometric direct minimization）来收敛 SCF，同时设置
MAX_DIIS_CYCLES = 1（若使用 MAX_DIIS_CYCLES 的默认值，DIIS 过程只会来回振荡）。"
    ```qchem
    $molecule
       0  1
       H  0.000   0.000   0.0
       H  0.000   0.000 -10.0
    $end
    
    $rem
       METHOD           =  hf
       BASIS            =  6-31g**
       UNRESTRICTED     =  true
       SCF_ALGORITHM    =  diis_gdm
       MAX_DIIS_CYCLES  =  1
       SCF_GUESS        =  gwh
       SCF_GUESS_MIX    =  2
    $end
    ```
