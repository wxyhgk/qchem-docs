---
title: "9.3.3 无 Hessian 过渡态搜索"
---

## 9.3.3 无 Hessian 过渡态搜索

(July 4, 2026)

一旦获得过渡态的猜测结构，即可采用标准的本征矢跟随（eigenvector-following）方法，
例如 Baker 的分式有理函数优化（partitioned rational-function optimization, P-RFO）
算法[[64]](../bib_references/bib.md#bib46)，
将猜测结构精修到精确的过渡态。P-RFO 的可靠性依赖于 Hessian 输入的质量，
正是 Hessian 使得该方法能够区分反应坐标（以一个负本征值为特征）与其余自由度。
因此在常规计算中，会在 P-RFO 搜索之前通过频率计算求得精确的 Hessian。
由于计算精确 Hessian 的成本通常比能量或梯度多出一个体系规模的数量级，
这一步骤对于含有大量原子的体系而言变得不切实际。

通过基于 FSM 的输出构造近似的 Hessian，可以避免精确 Hessian 的计算。[[1243]](../bib_references/bib.md#bib1297)
在 FSM 柔性字符串（FSM string）上，过渡态猜测点处的切线方向是反应坐标所对应的
Hessian 本征矢的良好近似。因此利用该切线，通过变分地极小化 Rayleigh-Ritz
比[[739]](../bib_references/bib.md#bib1482)
来计算正确的本征值及对应的本征矢。随后将反应坐标信息并入一个猜测矩阵，
而该猜测矩阵本身则是通过将离域内坐标[[63]](../bib_references/bib.md#bib50)
下的对角矩阵变换到笛卡尔坐标而得到的。
如此得到的近似 Hessian 按其设计只含一个对应于反应坐标的负本征值。
然后以该矩阵取代精确 Hessian，作为 P-RFO 方法的输入。

???+ example "示例 9.10: 结合 FSM 与 P-RFO 方法的一步式（one-shot）无 Hessian 方案，从反应物与产物结构直接确定精确过渡态"
    ```qchem
    $molecule
       0  1
       Si   1.028032  -0.131573  -0.779689
       H    0.923921  -1.301934   0.201724
       H    1.294874   0.900609   0.318888
       H   -1.713989   0.300876  -0.226231
       H   -1.532839   0.232021   0.485307
    ****
       Si   0.000228  -0.000484  -0.000023
       H    0.644754  -1.336958  -0.064865
       H    1.047648   1.052717   0.062991
       H   -0.837028   0.205648  -1.211126
       H   -0.855603   0.079077   1.213023
    $end
    
    $rem
       JOBTYPE               fsm
       METHOD                b3lyp
       BASIS                 6-31g
       FSM_NGRAD             3
       FSM_NNODE             18
       FSM_MODE              2
       FSM_OPT_MODE          2
       INTEGRAL_SYMMETRY     false
       POINT_GROUP_SYMMETRY  false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       JOBTYPE               ts
       METHOD                b3lyp
       BASIS                 6-31g
       SCF_GUESS             read
       GEOM_OPT_HESSIAN      read
       MAX_SCF_CYCLES        250
       GEOM_OPT_DMAX         50
       GEOM_OPT_MAX_CYCLES   100
       INTEGRAL_SYMMETRY     false
       POINT_GROUP_SYMMETRY  false
    $end
    ```
