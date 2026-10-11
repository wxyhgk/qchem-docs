---
title: "5.3.7 用户自定义密度泛函（User-Defined Density Functionals）"
---

## 5.3.7 用户自定义密度泛函（User-Defined Density Functionals）

（2026 年 7 月 4 日）

用户还可以请求由 **Q-Chem** 中可用的任意交换与/或关联泛函线性组合构成的自定义密度泛函。这种“通用（general）”密度泛函通过设置 EXCHANGE = GEN 请求，并通过 *$xc_functional* 输入节指定，该输入节中每一行对应泛函的一个所需交换（X）或关联（C）组分，其格式如下所示。

> ```qchem
> $xc_functional
>    X   exchange_symbol   coefficient
>    X   exchange_symbol   coefficient
>    ...
>    C   correlation_symbol   coefficient
>    C   correlation_symbol   coefficient
>    ...
>    K   coefficient
> $end
> ```

每一行需要三个变量：X 或 C，用于指明该组分是交换组分还是关联组分；泛函的符号表示，即如上所述在 EXCHANGE 或 CORRELATION 关键字变量中所使用的名称；以及每个组分的实数系数。注意，Hartree-Fock 交换既可以表示为 “X”，也可以表示为 “K”。示例如下。

???+ example "示例 5.2: 使用 B3tLap 泛函计算 H ${}_{2}$ O 的 Q-Chem 输入。"
    ```qchem
    $molecule
       0  1
       O
       H1  O  oh
       H2  O  oh  H1  hoh
    
       oh  =   0.97
       hoh = 120.0
    $end
    
    $rem
       EXCHANGE     gen
       CORRELATION  none
       BASIS        g3large   ! recommended for high accuracy
       THRESH       14        ! and better convergence
    $end
    
    $xc_functional
       X    Becke     0.726
       X    S         0.0966
       C    PK06      1.0
       K    0.1713
    $end
    ```

???+ example "示例 5.3: 使用 BR89B94hyb 泛函计算 H ${}_{2}$ O 的 Q-Chem 输入。"
    ```qchem
    $molecule
       0  1
       O
       H1  O  oh
       H2  O  oh  H1  hoh
    
       oh  =   0.97
       hoh = 120.0
    $end
    
    $rem
       EXCHANGE     gen
       CORRELATION  none
       BASIS        g3large   ! recommended for high accuracy
       THRESH       14        ! and better convergence
    $end
    
    $xc_functional
       X    BR89      0.846
       C    B94hyb    1.0
       K              0.154
    $end
    ```
