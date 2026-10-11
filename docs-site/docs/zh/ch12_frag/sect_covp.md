---
title: "12.5.4 使用互补占据/虚轨道对的微扰电荷转移分析"
---

## 12.5.4 使用互补占据/虚轨道对（Complementary Occupied/Virtual Pairs, COVPs）的微扰电荷转移分析

(July 4, 2026)

除了定量描述分子间电荷转移的量与能量贡献之外,对分子间复合物中的轨道相互作用给出简单的描述通常也很有用。由 SCF-MI  procedure 得到的极化局域分子轨道(Asserted Localized Molecular Orbitals, ALMOs)在分解分析(decomposition analysis)中被用作参考基组,但它并不能直接指出哪些占据-虚轨道对（occupied-virtual orbital pairs）在形成分子间键合中最为重要。通过在分子内部对极化 ALMOs 进行旋转,可以找到一套"化学家基组（chemist's basis set）",它仅用少数几个称为互补占据-虚轨道对（COVPs）的定域轨道来表示分子间的键合。这一轨道相互作用模型验证了现有的关于分子间键合的概念性描述。例如,在修正后的 ALMO 基组中,水二聚体的氢键被描述为定域在氧原子上的一对电子向另一分子上的 O–H $\sigma$ 反键轨道给予电子,[[681]](../bib_references/bib.md#bib708) 而金属配合物中协同键合（synergic bonding）的描述也与简单的 Dewar-Chatt-Duncanson 模型高度吻合。[[257]](../bib_references/bib.md#bib258)

在能量分解分析（Energy Decomposition Analysis, EDA）计算中,将 EDA_COVP 设置为 TRUE 即可对电荷转移（Charge Transfer, CT）项执行 COVP 分析。目前 COVP 分析仅支持两个片段（fragment）的体系。将 EDA_PRINT_COVP 设置为 TRUE 可打印形成占据-虚轨道对的定域轨道。在这种情况下,运行结束时得到的分子轨道(MOs)（SCF-MI 轨道、SCF-MI(RA) 轨道、收敛的 SCF 轨道）将被 COVP 的轨道所取代。每个轨道都会连同相应的 CT 能量项(以 kJ/mol 为单位,而不是以 hartree 为单位的轨道本征值)一起打印。这些能量标签便于找出一个分子上的占据轨道与另一个分子上的虚轨道之间的对应关系。下面的示例展示了如何打印 COVP 轨道。一种方法是设置 *$rem* 变量 PRINT_ORBITALS,另一种方法是将 IANLTY 设置为 200 并在 **Q-Chem** 输入中使用 *$plots* 段。在前一种情况下,可以使用 MOLDEN 对轨道进行可视化(将 MOLDEN_FORMAT 设置为 TRUE)。在后一种情况下,可使用 Visual Molecular Dynamics (VMD)[[W. Humphrey, A. Dalke, and K. Schulten (1996)]](../bib_references/bib.md#bib627) 或类似的能够绘制三维图像的第三方程序。

???+ example "示例 12.10: CT 项的 COVP 分析。COVP 轨道以 Q-Chem 和 MOLDEN 格式打印。"
    ```qchem
    $molecule
    0 1
    --
    0 1
    O          -1.521720    0.129941    0.000000
    H          -1.924536   -0.737533    0.000000
    H          -0.571766   -0.039961    0.000000
    --
    0 1
    O           1.362840   -0.099704    0.000000
    H           1.727645    0.357101   -0.759281
    H           1.727645    0.357101    0.759281
    $end
    
    $rem
       JOBTYPE         EDA
       EDA2            FALSE
       BASIS           6-31G
       PURECART        1112
       METHOD          B3LYP
       FRGM_METHOD     GIA
       FRGM_LPCORR     RS_EXACT_SCF
       EDA_COVP        TRUE
       EDA_PRINT_COVP  TRUE
       PRINT_ORBITALS  16
       MOLDEN_FORMAT   TRUE
    $end
    ```

???+ example "示例 12.11: CT 项的 COVP 分析。注意,无需运行完整的 EDA 计算。
只需将 FRGM_LPCORR 设置为 RS 或 ARS 并将 EDA_COVP 设置为 TRUE,即可执行 COVP 分析。最重要的占据-虚轨道对的轨道会被输出到名为 plot.mo 的 ASCII 文件中,该文件可以转换为 cube 文件并在 VMD 中进行可视化。"
    ```qchem
    $molecule
    0 1
    --
    0 1
    O          -1.521720    0.129941    0.000000
    H          -1.924536   -0.737533    0.000000
    H          -0.571766   -0.039961    0.000000
    --
    0 1
    O           1.362840   -0.099704    0.000000
    H           1.727645    0.357101   -0.759281
    H           1.727645    0.357101    0.759281
    $end
    
    $rem
       BASIS           6-31G
       PURECART        1112
       METHOD          B3LYP
       FRGM_METHOD     GIA
       FRGM_LPCORR     RS
       IANLTY          200
       EDA_COVP        TRUE
       EDA_PRINT_COVP  TRUE
    $end
    
    $plots
    MOs
       80  -4.0  4.0
       60  -3.0  3.0
       60  -3.0  3.0
       2   0  0  0
       6  11
    $end
    ```
