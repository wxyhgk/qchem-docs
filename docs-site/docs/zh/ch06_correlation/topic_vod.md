---
title: "6.14.2 VOD 与 VOD(2) 方法"
---

## 6.14.2 VOD 与 VOD(2) 方法

（2026 年 7 月 4 日）

VOD 方法是前文第 [6.12.8 节](topic_odcc.md) 中所描述的 OD（轨道优化二阶密度矩阵，Orbital-Optimized Double）方法的活性空间版本。VOD 既可以计算能量，也可以计算梯度，因此可以进行结构优化。关于 VOD 的适用性，有几点重要说明。首先，该方法能够精确处理那些在分子某个局域区域内本质上涉及 2 个活性电子的问题。因此，它是描述单键断裂、双键扭转（异构化）或某些类别双自由基的一个良好选择。然而，对于在同一局域区域内存在多个键被断裂的问题，VOD 的表现往往不佳，并且很可能得到非变分的解。针对此类问题，较新的 VQCCD 方法要可靠得多。

在假设 VOD 是电子结构的合理零阶描述的前提下，可以进一步计算仅针对能量的二阶修正，即 VOD(2)。VOD(2) 是 OD(2) 推广到手性（价层）活性空间后的版本。它通过计入动力学相关能，使得相对能量的计算更加精确。

???+ example "示例 6.45：使用 VOD 耦合簇活性空间方法计算部分拉伸键的水分子的关联能。这是一个相对“容易”收敛的任务，可与下一个不易收敛的示例形成对照。轨道采用限制性（restricted）方式。"
    ```qchem
    $molecule
      0  1
      O
      H  1  r
      H  1  r  2  a
    
      r =   1.5
      a = 104.5
    $end
    
    $rem
       METHOD        vod
       BASIS         6-31G
    $end
    ```

???+ example "示例 6.46：使用 VOD 耦合簇活性空间方法计算高度拉伸键的水分子。这是一个“困难”的、不易收敛的任务。经过若干次试验后，所示的收敛选项使该任务得以收敛（感谢 Ed Byrd！）。该任务的收敛难度应与前一个键拉伸程度较小的示例形成对照。"
    ```qchem
    $molecule
       0  1
       O
       H  1  r
       H  1  r  2  a
    
       r =   3.0
       a = 104.5
    $end
    
    $rem
       METHOD                vod
       BASIS                 6-31G
       SCF_CONVERGENCE       9
       THRESH                12
       CC_PRECONV_T2Z        50
       CC_PRECONV_T2Z_EACH   50
       CC_DOV_THRESH         7500
       CC_THETA_STEPSIZE     3200
       CC_DIIS_START         75
    $end
    ```
