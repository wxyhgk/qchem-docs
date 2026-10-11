---
title: "9.12.1 引言"
---

## 9.12.1 引言

(July 4, 2026)

原子与分子团簇的势能面景观可能极为复杂，存在许多能量相近的极小值点，并且随着团簇尺寸的增大，这种复杂性会迅速加剧。确定这些团簇的全局极小值是一项颇具挑战性的任务，因为它需要在势能面（potential energy surface, PES）上进行大范围搜索。寻找这类团簇低能结构的一种方法是从不同的初始坐标出发执行多次几何优化。**Q-Chem** 能够对最多包含两种分子类型的分子团簇执行此类随机搜索。在这类搜索中，通过对分子结构施加平移和旋转来生成新的起始结构。这些搜索由 JOBTYPE = RAND 启动，并且需要指定不同种类分子的数量以及各类分子中的原子数。对于原子团簇的优化，可设置 SEARCH_ATOMIC = TRUE，并指定在结构生成过程中执行的原子交换次数（N_SWOP）。在 *$molecule* 段中指定输入结构时需要特别注意：分子类型 1 的所有原子必须排在分子类型 2 的原子之前；此外，同一分子中的原子应当相邻排列。相关研究的示例请参见参考文献 [[338]](../bib_references/bib.md#bib343) 。

???+ example "示例 9.52：NO ${}^{+}$ .H ${}_{2}$ O 团簇的随机搜索几何优化。"
    ```qchem
    $molecule
       1 1
       N    0.5682008336    0.1585044954   -0.9009280260
       O   -0.3450383302   -0.5598328271   -0.4634299478
       O    1.7303273568    0.3403569345    0.4364171165
       H    2.5236300547   -0.2494576134    0.1485689942
       H    2.1020812302    1.2823911654    0.2570156558
    $end
    
    $rem
       JOBTYPE                     RAND
       METHOD                      B3LYP
       BASIS                       STO-3G
       SCF_CONVERGENCE             6
       MAX_SCF_CYCLES              100
       NSEARCH                     10
       N_MOL_TYPE                  2
       NMOL1                       1
       N_ATOM_TYPE_1               2
       NMOL2                       1
       N_ATOM_TYPE_2               3
       N_MOVES                     20
       MAXBOX                      10000
       MIN_SEPARATION              25
       MAX_DISPLACE                25
       SCF_NOCRASH                 TRUE
       TIGHTEN_CONVERG             TRUE
       GEOM_OPT_MAX_CYCLES         200
       GEOM_OPT_COORDS             0
       GEOM_OPT_TOL_DISPLACEMENT   1000
       GEOM_OPT_TOL_GRADIENT       300
       GEOM_OPT_TOL_ENERGY         100
    $end
    ```

???+ example "示例 9.53：He ${}_{3}$ Ne ${}_{3}$ 团簇的随机搜索几何优化。"
    ```qchem
    $molecule
       0 1
       He   -1.3590894    3.0177788   -0.1662522
       He   -2.9853158    1.1444488    0.1036005
       He    0.5068109    1.3795209   -0.2168151
       Ne   -1.1002149   -0.5693061    0.0381894
       Ne    0.5981676    1.8697812    1.4685618
       Ne   -1.2376457    1.2597811   -0.0756066
    $end
    
    $rem
       JOBTYPE                     RAND
       METHOD                      B3LYP
       DFT_D                       EMPIRICAL_GRIMME
       BASIS                       STO-3G
       SCF_CONVERGENCE             6
       MAX_SCF_CYCLES              100
    
       NSEARCH                     10
       SEARCH_ATOMIC               TRUE
       N_SWOP                      4
       N_MOL_TYPE                  2
       NMOL1                       3
       N_ATOM_TYPE_1               1
       NMOL2                       3
       N_ATOM_TYPE_2               1
       N_MOVES                     20
       MAXBOX                      10000
       MIN_SEPARATION              25
       MAX_DISPLACE                25
       SCF_NOCRASH                 TRUE
       TIGHTEN_CONVERG             TRUE
       USE_INITIAL                 TRUE
    
       GEOM_OPT_MAX_CYCLES         200
       GEOM_OPT_COORDS             0
       GEOM_OPT_TOL_DISPLACEMENT   1000
       GEOM_OPT_TOL_GRADIENT       3000
       GEOM_OPT_TOL_ENERGY         1000
    $end
    ```

盆地跳跃（basin hopping, BH）是一种更为先进的技术，用于在复杂势能面上定位全局极小值。[[1421]](../bib_references/bib.md#bib1481)

BH 算法本质上是 Metropolis 采样技术与基于梯度的局部搜索方法的结合。其效果是对能量盆地（energy basin）进行采样，而不是对构型空间进行采样；所谓能量盆地，是指势能面上某个极小值周围的一定构型空间区域，其中包含的所有构型经 downhill 弛豫后都会收敛到该极小值。为提高方法效率，可采用带偶发跳跃的 BH（BH with occasional jumping），[[616]](../bib_references/bib.md#bib639) 它在标准蒙特卡洛（Monte Carlo, MC）移动之外引入了一种跳跃移动。跳跃是在无限温度下、不做局部极小化的 MC 移动，因此总是被接受。当常规 MC 移动被连续拒绝多次时，即判定系统被捕获在该局部极小值处。此时将温度升高至 $T=\infty$，并执行若干次 MC 跳跃移动，以使系统得以逃离该局部极小值。这为逃离局部极小值、并在山谷中下一个盆地被高能垒隔开时对其加以探索提供了一种高效途径。根据所研究体系的规模与复杂程度，需要设置大量的 MC_STEPS 和/或 MC_CYCLES，以确保找到全局极小值。

???+ example "示例 9.54：NO ${}^{+}$ (H ${}_{2}$ O) 团簇的盆地跳跃搜索。"
    ```qchem
    $molecule
       1 1
       N     0.5682008336    0.1585044954   -0.9009280260
       O    -0.3450383302   -0.5598328271   -0.4634299478
       O     1.7303273568    0.3403569345    0.4364171165
       H     2.5236300547   -0.2494576134    0.1485689942
       H     2.1020812302    1.2823911654    0.2570156558
    $end
    
    $rem
      JOBTYPE          BH
      METHOD           B3LYP
      BASIS            STO-3G
      SCF_CONVERGENCE  6
      MAX_SCF_CYCLES   100
    
      MC_CYCLES             4
      MC_STEPS              5
      MC_TEMP               300
      MAX_DISPLACE          25
      MIN_SEPARATION        25
      MAXBOX                5000
      N_MOVES               20
    
      N_MOL_TYPE       2
      NMOL1            1
      N_ATOM_TYPE_1    2
      NMOL2            1
      N_ATOM_TYPE_2    3
      N_MOVES          20
      MAXBOX           10000
      MIN_SEPARATION   25
      MAX_DISPLACE     25
      SCF_NOCRASH      TRUE
    
      GEOM_OPT_MAX_CYCLES       200
      GEOM_OPT_COORDS           0
      GEOM_OPT_TOL_DISPLACEMENT 2000
      GEOM_OPT_TOL_GRADIENT     4000
      GEOM_OPT_TOL_ENERGY       400
    $end
    ```
