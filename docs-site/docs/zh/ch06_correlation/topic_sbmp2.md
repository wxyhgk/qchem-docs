---
title: "6.6.5 自旋偏向 MP2 方法（SCS-MP2、SOS-MP2 与 MOS-MP2）"
---

## 6.6.5 自旋偏向 MP2 方法（SCS-MP2、SOS-MP2 与 MOS-MP2）

（2026 年 7 月 4 日）

正如 Grimme 所示，[[491]](../bib_references/bib.md#bib499)
通过对异自旋（opposite-spin, OS）与同自旋（same-spin, SS）相关分量分别施加不同的标度因子进行半经验标度，可以显著提高二阶微扰理论（Second-Order Møller–Plesset Perturbation Theory, MP2）计算的精度。
对 OS 与 SS 分量分别采用 1.2 和 0.33 的标度因子即定义了 SCS-MP2 方法；但对于涉及分子间相互作用的体系，其他参数化方案更为合适，例如 SCS-MI-MP2 方法对 OS 和 SS 分量分别使用 0.40 和 1.29。[[330]](../bib_references/bib.md#bib337)

近期的研究证明，[[656]](../bib_references/bib.md#bib680)
仅保留异自旋相关项并对其施加 1.3 的标度，也能在热化学方面获得相当精度的结果。
此外，SOS-MP2 能量可以结合分辨率恒等（Resolution of the Identity, RI）近似与拉普拉斯变换（Laplace transform）技术来求值，从而使计算量仅随分子尺寸的四次方增长。
自 **Q-Chem** v. 3.0 起，该方法的高效能量[[656]](../bib_references/bib.md#bib680)
及解析梯度[[855]](../bib_references/bib.md#bib887)
算法均已可用，对于较大分子而言相比 MP2 在速度上具有优势，并且在精度上也有统计意义上的显著提升。

然而需要注意的是，SOS-MP2 方法确实会系统性地低估长程色散作用（对此合适的标度因子应为 2 而非 1.3），但可以通过使标度因子依赖于距离来加以修正，这即是近期提出并经过测试的修正异自旋标度变体（modified opposite spin, MOS-MP2）。[[853]](../bib_references/bib.md#bib886)
MOS-MP2 的能量与解析梯度同样在 **Q-Chem** 3.0 中可用，其计算代价与 SOS-MP2 基本相同。
计时测试表明，SOS-MP2 与 MOS-MP2 的四阶实现对于 40 个重原子及以上的分子相比 RI-MP2 可带来显著加速。
如有需要，还可以针对特定应用（例如弱相互作用）自定义标度因子。

将 CORRELATION 关键字设置为 SOSMP2 或 MOSMP2，即可调用四阶标度的 SOS-MP2/MOS-MP2 能量计算。MOS-MP2 还进一步需要指定 *$rem*
变量 OMEGA，用于调节 MOS 算符的衰减程度：[[853]](../bib_references/bib.md#bib886)

<a id="Ch6.E28"></a>
$$
g_{\omega}(r_{12})=\frac{1}{r_{12}}+c_{\mathrm{MOS}}\frac{\mathrm{erf}\left({\omega r_{12}}\right)}{r_{12}} \tag{6.28}
$$

推荐的 OMEGA 取值为 $\omega=0.6$ bohr${}^{-1}$。[[853]](../bib_references/bib.md#bib886)

快速算法使用了辅助基组展开，因此关键字 AUX_BASIS 应与用户对 BASIS
的选择保持一致。SOS-MP2 与 MOS-MP2 均有四阶标度的解析梯度可用，并在
JOBTYPE 设置为 OPT 或 FORCE 时自动调用。能量与解析梯度求值的最小内存需求均为 3$X^{2}$，其中 $X$ = 辅助基函数的数目。闭壳层计算的磁盘空间需求为：能量求值约 $\sim 2OVX$，解析梯度求值约 $\sim 4OVX$。

需要指定的关键 *$rem* 变量汇总：

| CORRELATION | RIMP2 |
| --- | --- |
|  | SOSMP2 |
|  | MOSMP2 |
| JOBTYPE | sp（默认）单点能量求值 |
|  | opt 带解析梯度的几何优化 |
|  | force 带解析梯度的力求值 |
| BASIS | 用户自选（标准基组或用户自定义：GENERAL 或 MIXED） |
| AUX_BASIS | 与之对应的辅助基组（标准或用户自定义： |
|  | AUX_GENERAL 或 AUX_MIXED |
| OMEGA | 无默认值 $n$；使用 $\omega=n/1000$。推荐值为 |
|  | $n=600$（$\omega=0.6$ bohr ${}^{-1}$） |
| N_FROZEN_CORE | 可选 |
| N_FROZEN_VIRTUAL | 可选 |
| SCS | 开启自旋分量标度，对应 SCS-MP2(1)、 |
|  | SOS-MP2(2) 以及任意 SCS-MP2(3) |

???+ example "示例 6.8：SCS-MP2 几何优化示例"
    ```qchem
    $molecule
       0 1
       C
       H  1  1.0986
       H  1  1.0986  2  109.5
       H  1  1.0986  2  109.5  3   120.0 0
       H  1  1.0986  2  109.5  3  -120.0 0
    $end
    
    $rem
       JOBTYPE             opt
       CORRELATION         rimp2
       BASIS               aug-cc-pvdz
       AUX_BASIS           rimp2-aug-cc-pvdz
       BASIS2              racc-pvdz   ! Optional Secondary basis
       SCS                 1           ! Turn on spin-component scaling
       DUAL_BASIS_ENERGY   true        ! Optional dual-basis approximation
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "示例 6.9：SCS-MI-MP2 能量计算示例"
    ```qchem
    $molecule
       0 1
       C       0.000000     -0.000140      1.859161
       H      -0.888551      0.513060      1.494685
       H       0.888551      0.513060      1.494685
       H       0.000000     -1.026339      1.494868
       H       0.000000      0.000089      2.948284
       C       0.000000      0.000140     -1.859161
       H       0.000000     -0.000089     -2.948284
       H      -0.888551     -0.513060     -1.494685
       H       0.888551     -0.513060     -1.494685
       H       0.000000      1.026339     -1.494868
    $end
    
    $rem
       CORRELATION         rimp2
       BASIS               aug-cc-pvtz
       AUX_BASIS           rimp2-aug-cc-pvtz
       BASIS2              racc-pvtz    Optional Secondary basis
       THRESH              12
       SCF_CONVERGENCE     8
       SCS                 3            Spin-component scale arbitrarily
       SOS_FACTOR          0400000      Specify OS parameter
       SSS_FACTOR          1290000      Specify SS parameter
       DUAL_BASIS_ENERGY   true         Optional dual-basis approximation
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "示例 6.10：SOS-MP2 几何优化示例"
    ```qchem
    $molecule
       0 3
       C1
       H1   C1   1.07726
       H2   C1   1.07726   H1  131.60824
    $end
    
    $rem
       JOBTYPE        opt
       METHOD         sosmp2
       BASIS          cc-pvdz
       AUX_BASIS      rimp2-cc-pvdz
       UNRESTRICTED   true
       INTEGRAL_SYMMETRY false
    $end
    ```

???+ example "示例 6.11：采用冻芯近似的 MOS-MP2 能量求值示例"
    ```qchem
    $molecule
       0 1
       Cl
       Cl 1 2.05
    $end
    
    $rem
       METHOD            mosmp2
       BASIS             cc-pVTZ
       AUX_BASIS         rimp2-cc-pVTZ
       N_FROZEN_CORE     fc
       OMEGA             600
       THRESH            12
       SCF_CONVERGENCE   8
    $end
    ```
