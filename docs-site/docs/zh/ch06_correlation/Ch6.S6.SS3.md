---
title: "6.6.3 RI-MP2 的 OpenMP 实现"
---

## 6.6.3 RI-MP2 的 OpenMP 实现

(2026 年 7 月 4 日)

从 **Q-Chem** 4.1 版本开始，默认使用 OpenMP 的 RI-MP2 能量算法。
在较旧的版本中可以通过设置 CORR = PRIMP2 来调用该算法，但请注意
在 4.01 及更早版本中，仅支持 RHF/RI-MP2。现在已支持 UHF/RI-MP2 和 ROHF/RI-MP2，并且 ‘B’ 矩阵的构建以及
三中心积分均已实现并行化。该算法利用 MEM_TOTAL 分配中剩余的内存
完成全部计算，从而可以大幅减少构建 t-振幅（t-amplitudes）时的硬盘读取。
自 **Q-Chem** 5.2 起，可以通过设置 method=mp2 并使用
AUX_BASIS_CORR 指定合适的辅助基组来调用 RI-MP2。在双杂化（double-hybrid）方法的情况下，
添加 AUX_BASIS_CORR 将直接调用 RI-MP2。

???+ example "示例 6.5: OpenMP 并行 RI-MP2 作业示例。"
    ```qchem
    $molecule
       0 1
       C1
       H1  C1    1.077260
       H2  C1    1.077260
    $end
    
    $rem
       METHOD        mp2
       BASIS         cc-pVDZ
       AUX_BASIS_CORR cc-pVDZ / cc-pVDZ-RI
       MEMORY        2000
       SCF_CONV        12
       $end
    ```
