---
title: "10.8.2 同位素取代以及 $T$ 和 $P$ 的变化"
---

## 10.8.2 同位素取代以及 $T$ 和 $P$ 的变化

（2026 年 7 月 4 日）

默认情况下，**Q-Chem** 使用最丰富同位素的原子质量来计算振动频率。

可以通过 *$isotopes* 段并将 *$rem* 变量 ISOTOPES 设置为 TRUE 来指定其他同位素的质量。*$isotopes* 段的格式如下：

> ```qchem
> $isotopes
>    number_of_isotope_loops  tp_flag
>    number_of_atoms  [temp pressure] (loop 1)
>    atom_number1   mass1
>    atom_number2   mass2
>    ...
>    number_of_atoms  [temp pressure] (loop 2)
>    atom_number1   mass1
>    atom_number2   mass2
>    ...
> $end
> ```

**注意：**

**只需指定那些质量要偏离默认值而被更改的原子。在每个循环（loop）结束后，所有质量都会被重置为默认值。原子编号按照 *$molecule* 段中出现的顺序确定。**

程序总是先执行一个使用默认质量的初始循环。其后的循环则使用用户指定的原子质量。列表中只需包含那些质量需要更改的原子，其余原子都将采用默认质量。输出会为每个循环给出完整的频率分析。请注意，附加循环中振动频率的计算仅涉及对已计算得到的 Hessian（海塞矩阵）进行重新标度，因此几乎不增加额外的计算时间。

*$isotopes* 段的第一行指定取代循环的数目，并指明是否需要修改温度和压强。若使用默认的温度和压强（分别为 298.15 K 和 1 atm），*tp_flag* 应设置为 0；若要改变它们，则设置为 1。请注意，温度应以开尔文（Kelvin）为单位给出，压强应以大气压（atmospheres）为单位给出。参见示例 10.8.2。

ISOTOPES

### `ISOTOPES`

> **指定在频率计算中是否使用非默认质量。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 仅使用默认质量。
>     * TRUE
>     * 从
>     * $isotopes
>     * 段读取同位素质量。
> * **建议**: 无

???+ example "示例 10.39: 先进行 EDF1/6-31G* 几何优化，随后进行包含同位素取代的振动分析。只有在驻点上进行振动分析，结果才是有效的。"
    ```qchem
    $molecule
       0  1
       C   1.08900   0.00000   0.00000
       C  -1.08900   0.00000   0.00000
       H   2.08900   0.00000   0.00000
       H  -2.08900   0.00000   0.00000
    $end
    
    $rem
       BASIS    6-31G*
       JOBTYPE  opt
       METHOD   edf1
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       BASIS       6-31G*
       JOBTYPE     freq
       METHOD      edf1
       SCF_GUESS   read
       ISOTOPES    1
    $end
    
    $isotopes
       2   0           ! two loops, both at std temp and pressure
       4
         1   13.00336  ! All atoms are given non-default masses
         2   13.00336
         3   2.01410
         4   2.01410
       2
         3   2.01410   ! Hs replaced with Ds
         4   2.01410
    $end
    ```

???+ example "示例 10.40: 先进行 EDF1/6-31G* 几何优化，随后进行振动分析，并在不同的温度和压强下计算振动焓与振动熵。"
    ```qchem
    $molecule
       0 1
       O   0.000000   0.000000   0.106731
       H  -0.758095   0.000000  -0.528927
       H   0.758095   0.000000  -0.528927
    $end
    
    $rem
       JOBTYPE   opt
       METHOD    edf1
       BASIS     6-31G*
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE   freq
       METHOD    edf1
       BASIS     6-31G*
       ISOTOPES  true
    $end
    
    $isotopes
       3   1             ! "1" here means we will set T & P
       0   500.0   1.0   ! 500 K, 1 atm, standard masses
       0   298.0   10.0  ! 298 K, 10 atm, standard masses
       2   500.0   1.0   ! 500 K, 1 atm, subst. D for H
         2   2.0141018
         3   2.0141018
    $end
    ```
