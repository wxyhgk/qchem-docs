---
title: "7.3.8 TDDFT 中的解析激发态 Hessian"
---

## 7.3.8 TDDFT 中的解析激发态 Hessian

（2026 年 7 月 4 日）

若要对某个激发态使用 TDDFT[[842]](../bib_references/bib.md#bib873) 进行振动频率分析，
首先必须对该激发态的几何结构进行优化。与基态的振动频率分析类似，
激发态的频率分析同样应当在激发态势能面上的驻点处进行。除了激发能
计算所需的 *$rem* 关键字之外，还需将 *$rem* 变量
CIS_STATE_DERIV 设置为需要进行几何优化和频率分析的激发态。

与数值微分方法相比，激发能几何二阶导数的解析计算所需时间大大减少，
但需要更多的内存。计算开销主要消耗在以下这些步骤上：求解用于分子轨道
系数导数 C${}^{\mathrm{x}}$ 的 CPSCF 方程、求解用于跃迁矢量导数的
CP-TDDFT 方程，以及构建 Hessian 矩阵。这些步骤的内存使用量
按 ${\cal{O}}({3mN^{2}})$ 的规模增长，其中 $N$ 是基函数数目，m 是原子数目。因此对于
大体系，分段（in segments）求解所有耦合微扰方程至关重要。
在这种情况下，必须始终设置 *$rem* 变量 CPSCF_NSEG。

在解析 TDDFT 激发态 Hessian 的计算中，需要求值大量能量泛函导数：
即关于密度变量的一阶至四阶泛函导数，以及它们对核坐标的导数。因此，
应当采用非常精细的 DFT 计算积分网格，以保证结果的精度。

解析 TDDFT/C-PCM Hessian 已在 **Q-Chem** 中实现。
可以使用 TDDFT/C-PCM 方法的频率计算，对溶液中的体系进行
正则模式分析。上述垂直激发能示例中，TDDFT/C-PCM 激发态计算
所需的 *$rem* 和 *$pcm* 变量同样需要设置。当计算大体系的性质时，
必须注意内存限制。

???+ example "示例 7.18: 在气相中进行 B3LYP/6-31G* 几何优化，随后对过氧自由基的第一激发态进行频率分析。"
    ```qchem
    $molecule
       0 2
       C  1.004123  -0.180454   0.000000
       O -0.246002   0.596152   0.000000
       O -1.312366  -0.230256   0.000000
       H  1.810765   0.567203   0.000000
       H  1.036648  -0.805445  -0.904798
       H  1.036648  -0.805445   0.904798
    $end
    
    $rem
       JOBTYPE           opt
       EXCHANGE          b3lyp
       CIS_STATE_DERIV   1
       BASIS             6-31G*
       CIS_N_ROOTS       10
       CIS_SINGLETS      true
       CIS_TRIPLETS      false
       XC_GRID           000075000302
       RPA               0
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE           freq
       EXCHANGE          b3lyp
       CIS_STATE_DERIV   1
       BASIS             6-31G*
       CIS_N_ROOTS       10
       CIS_SINGLETS      true
       CIS_TRIPLETS      false
       XC_GRID           000075000302
       RPA               0
    $end
    ```

???+ example "示例 7.19: 使用 TDDFT/C-PCM 在甲醇中对环戊二烯酮的低能激发态进行几何优化"
    ```qchem
    $molecule
       0 1
      C   -0.0000000    0.6920860    1.4656691
      C   -0.0000000   -0.6920860    1.4656691
      C   -0.0000000   -1.1528931    0.1065000
      C    0.0000000   -0.0000000   -0.7957576
      C    0.0000000    1.1528931    0.1065000
      O    0.0000000   -0.0000000   -2.0301721
      H   -0.0000000    1.3254423    2.3427356
      H   -0.0000000   -1.3254423    2.3427356
      H   -0.0000000   -2.1834532   -0.2231979
      H    0.0000000    2.1834532   -0.2231979
    $end
    
    $rem
       JOBTYPE             opt
       EXCHANGE            b3lyp
       CIS_N_ROOTS         5
       CIS_SINGLETS        true
       CIS_TRIPLETS        true
       CIS_STATE_DERIV     1   Lowest TDDFT state
       BASIS               6-311G*
       XC_GRID             3
       SOLVENT_METHOD      pcm
       THRESH              12
    $end
    
    $pcm
       Theory      CPCM
       Method      SWIG
       Solver      Inversion
       Radii       Bondi
    $end
    
    $solvent
       Dielectric 32.613
    $end
    
    ```

???+ example "示例 7.20: Hessian 计算，使用上一个示例中优化后的几何结构。"
    ```qchem
    $molecule
       0 1
       C     0.0000000000    0.6940558365    1.4635362645
       C     0.0000000000   -0.6940558367    1.4635362652
       C     0.0000000000   -1.1539902580    0.1063088532
       C     0.0000000000    0.0000000000   -0.7890068343
       C     0.0000000000    1.1539902569    0.1063088524
       O     0.0000000000    0.0000000000   -2.0333287471
       H     0.0000000000    1.3287019844    2.3394236351
       H     0.0000000000   -1.3287019837    2.3394236361
       H     0.0000000000   -2.1861329696   -0.2193590119
       H     0.0000000000    2.1861329678   -0.2193590131
    $end
    
    $rem
       JOBTYPE           freq
       EXCHANGE          b3lyp
       CIS_N_ROOTS       5
       CIS_SINGLETS      true
       CIS_TRIPLETS      true
       CIS_STATE_DERIV   1   Lowest TDDFT state
       BASIS             6-311G*
       XC_GRID           3
       SOLVENT_METHOD    pcm
       MEM_STATIC        4000
       MEM_TOTAL         24000
       CPSCF_NSEG        3
       THRESH            12
    $end
    
    $pcm
       Theory      CPCM
       Method      SWIG
       Solver      Inversion
       Radii       Bondi
    $end
    
    $solvent
       Dielectric  32.613
    $end
    ```
