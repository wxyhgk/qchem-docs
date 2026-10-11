---
title: "12.7.1 面向 MP2 方法的 ALMO-EDA"
---

## 12.7.1 面向 MP2 方法的 ALMO-EDA

(July 4, 2026)

前述的 EDA 方法仅限于 HF 和 DFT 等 SCF 方法。然而对于许多体系而言，使用基于波函数的相关方法更为合适。因此，ALMO-EDA 已被推广至 MP2。[[1353]](../bib_references/bib.md#bib1413)
 MP2 ALMO-EDA 建立在第一代 ALMO-EDA 的基础之上。它为 ALMO-EDA 定义的 FRZ、POL 和 CT 各项提供 MP2 修正，并额外引入一个对应于伦敦色散力（London dispersion force）的项。其实现方式是为每一个 HF 中间态定义一个受约束的中间 MP2 波函数。

当前的实现仅限于 RI-MP2 而非完整的 MP2，并且只适用于闭壳层、自旋限制（spin restricted）的情形。冻结核（Frozen core）与自旋缩放（spin scaling）也尚不支持。若试图将该 EDA 与 RI-MP2 之外的其他相关方法一起使用，或使用非限制轨道（unrestricted orbitals），将导致程序崩溃。冻结核与自旋缩放的设置会被 EDA 忽略并给出警告，但不会被最终能量计算忽略，从而导致结果不一致。

尽管 MP2 EDA 基于第一代 ALMO-EDA，但其代码路径与 REM 设置与第二代 ALMO-EDA 共用。MP2 ALMO-EDA 本身并未定义任何新的 REM 变量。相反，在以 EDA2 和 GEN_SCFMAN 运行 EDA 任务时，若相关方法为 RI-MP2，便会触发 MP2 ALMO-EDA。该相关设置会使 EDA 的 SCF 部分切换回原始的格式，同时也会对相关能进行分解。多数为第二代 ALMO-EDA 设计的设置不受支持，但 EDA_NO_CT 和 EDA_BSSE 是例外。示例见下方。

???+ example "示例 12.27：水二聚体的 MP2 能量分解分析。"
    ```qchem
    $molecule
    0 1
    --
    0 1
    O  -0.031783  -0.057754   0.000000
    H  -0.415035   0.819269   0.000000
    H   0.919546   0.097478   0.000000
    --
    0 1
    O   2.960796   0.171800   0.000000
    H   3.290569  -0.313410  -0.758561
    H   3.290569  -0.313410   0.758561
    $end
    
    $rem
       JOBTYPE         EDA
       GEN_SCFMAN      TRUE
       EDA2            TRUE
       FRGM_METHOD     STOLL
       EXCHANGE        HF
       CORRELATION     RIMP2
       BASIS           aug-cc-pVTZ
       AUX_BASIS       rimp2-aug-cc-pVTZ
       THRESH          14
       SCF_CONVERGENCE 10
       N_FROZEN_CORE   0
       EDA_BSSE        TRUE
       USE_LIBQINTS    0
       INTEGRAL_SYMMETRY FALSE
    $end
    ```
