---
title: "8.10.5 用户自定义 ECP"
---

## 8.10.5 用户定义的有效核势（ECP）

(2026 年 7 月 4 日)

许多用户会发现内置的 ECP 库已能满足其需求。不过，如果您需要使用 **Q-Chem** 中未内置的 ECP，可以按照与定义用户自定义轨道基组（orbital basis set）类似的方式输入；参见第 [8](chap_basis.md) 章。

要应用用户自定义的 ECP，必须将 *$rem* 中的 ECP 与 BASIS 关键字设置为 GEN。随后添加一个逐元素定义 ECP 的 *$ecp* 块，以及一个定义轨道基组的 *$basis* 块，各元素之间用星号分隔。

*$basis* 块中的语法在第 [8](chap_basis.md) 章中描述。*$ecp* 块中每条记录的语法如下：

*$ecp*

对于每个施加 ECP 的原子：

      该原子的化学符号

      ECP 名称；ECP 的 $L$ 值；被移除的芯电子（core electrons）数目

      对于每个 ECP 分量（按 unprojected、$\hat{P}_{0}$、$\hat{P}_{1}$、…、$\hat{P}_{L-1}$ 的顺序）：

            该分量的名称

            该分量中高斯函数（Gaussian）的数目

            对于该分量中的每个高斯函数

                  $r$ 的幂次；指数；收缩系数

一串四个星号（*即* `****`）

*$end*

**注意：

1.

*$ecp* 块中的所有信息均不区分大小写。

2.

$r$ 的幂次（其中已包含雅可比（Jacobian）因子 $r^{2}$）必须为 0、1 或 2。

3.

若包含 $r^{0}$ 或 $r^{1}$ 项，则必须加入 rem 关键字 “ECP_FIT = TRUE”。

**

???+ example "示例 8.10: 在 Al 上使用用户自定义的 ECP 与基组、在 H 上使用 3-21G 基组，优化 AlH ${}_{3}$ 的 HF 几何结构"
    ```qchem
    $molecule
       0  1
       Al
       H1  Al  r
       H2  Al  r  H1  120.0
       H3  Al  r  H1  120.0  H2  180.0
    
       r = 1.6
    $end
    
    $rem
       JOBTYPE    opt   Geometry optimization
       METHOD     hf    Hartree-Fock theory
       ECP        gen   User-defined ECP
       BASIS      gen   User-defined basis
       ECP_FIT    true
       geom_opt_driver optimize
    $end
    
    $ecp
       Al
       Stevens_ECP  2  10
       d potential
         1
         1   1.95559  -3.03055
       s-d potential
         2
         0   7.78858   6.04650
         2   1.99025  18.87509
       p-d potential
         2
         0   2.83146   3.29465
         2   1.38479   6.87029
    ****
    $end
    
    $basis
       Al
       SP 3  1.00
          0.90110  -0.30377  -0.07929
          0.44950   0.13382   0.16540
          0.14050   0.76037   0.53015
       SP 1  1.00
          0.04874   0.32232   0.47724
    ****
       H
       3-21G
    ****
    $end
    ```
