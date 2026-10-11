---
title: "8.4.3 用户自定义基组（User-Defined Basis Sets）的格式"
---

## 8.4.3 用户自定义基组（User-Defined Basis Sets）的格式

（2026 年 7 月 4 日）

用户自定义基组（user-defined basis）段的格式如下：

> | $basis |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- |
> |  | $X$ | 0 |  |  |  |
> |  | $L$ | $K$ | $scale$ |  |  |
> |  | $\alpha_{1}$ | $C_{1}^{L_{\text{min}}}$ | $C_{1}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{1}^{L_{\text{max}}}$ |
> |  | $\alpha_{2}$ | $C_{2}^{L_{\text{min}}}$ | $C_{2}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{2}^{L_{\text{max}}}$ |
> |  | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ |
> |  | $\alpha_{K}$ | $C_{K}^{L_{\text{min}}}$ | $C_{K}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{K}^{L_{\text{max}}}$ |
> | **** |  |  |  |  |  |
> | $end |  |  |  |  |  |

其中

| $X$ | 原子的元素符号（不接受原子序数） |
| --- | --- |
| $L$ | 角动量符号（S、P、SP、D、F、G） |
| $K$ | 壳层（shell）的收缩阶数（整数） |
| $scale$ | 施加于指数（exponent）的缩放因子（默认值为 1.00） |
| $\alpha_{i}$ | 高斯原函数（Gaussian primitive）指数（正实数） |
| $C_{i}^{L}$ | 各角动量对应的收缩系数（contraction coefficient，非零实数）。 |

每个原子以 `****` 结束，整个基组则以 *$end* 关键字作为终止符。在通用基组（general basis set）输入中不得包含空行。请注意，对于 SP 这类复合壳层（compound shells），每行需要提供多个收缩系数。与 **Q-Chem** 输入文件（input deck）中的所有信息一样，全部输入均不区分大小写。

???+ example "示例 8.1: 添加一个用户自定义的非标准基组的示例。注意，由于引入了 $d$、$f$ 和 $g$ 函数，必须设置 $rem 变量 PURECART。同时注意使用 BASIS2 来提供初始猜测（initial guess）。"
    ```qchem
    $molecule
       0  1
       O
       H  O  oh
       H  O  oh  2  hoh
    
       oh  =   1.2
       hoh = 110.0
    $end
    
    $rem
       EXCHANGE   hf
       BASIS      gen      user-defined general basis
       BASIS2     sto-3g   sto-3g orbitals as initial guess
       PURECART   112      Cartesian d functions, pure f and g
    $end
    
    $basis
       H  0
       S  2  1.00
          1.30976    0.430129
          0.233136   0.678914
    ****
       O  0
       S  2  1.00
          49.9810    0.430129
          8.89659    0.678914
       SP 2  1.00
          1.94524    0.049472    0.511541
          0.49336    0.963782    0.612820
       D  1  1.00
          0.39000    1.000000
       F  1  1.00
          4.10000    1.000000
       G  1  1.00
          3.35000    1.000000
    ****
    $end
    ```
