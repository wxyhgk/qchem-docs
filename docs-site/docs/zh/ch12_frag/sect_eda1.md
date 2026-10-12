---
title: "12.5.3 第一代 ALMO-EDA 与微扰电荷转移分析"
---

## 12.5.3 第一代 ALMO-EDA 与微扰电荷转移分析

（2026 年 7 月 4 日）

分子间结合的强度与分子间相互作用的本质密不可分。分子间复合物可以通过弱色散力、静电效应（*例如*，电荷–电荷、电荷–偶极以及电荷–诱导偶极相互作用）以及给体-受体型轨道相互作用（如分子间电子密度的正向给电子与反馒给电子）而稳定。根据这些相互作用程度的不同，分子间结合的强度可以从仅仅几 kJ/mol（范德华复合物）到几百 kJ/mol（金属复合物中的金属–配体键）不等。理解各种相互作用模式的贡献，有助于通过设计能够促进理想效应的材料，将分子间结合的强度调控到理想范围。现代第一性原理电子结构方法所提供的最强大的技术之一，就是将总分子结合能分解为具有物理意义的组分，例如色散（dispersion）、静电（electrostatic）、极化（polarization）、电荷转移（charge transfer）以及几何弛豫项，从而研究和剖析分子间相互作用的本质。

基于绝对局域分子轨道（absolutely-localized molecular orbitals, ALMO）的能量分解分析（Energy Decomposition Analysis, EDA）已在 **Q-Chem** 中实现，[[682]](../bib_references/bib.md#bib706)
 包括其开壳层推广形式。[[597]](../bib_references/bib.md#bib616)
 在 ALMO-EDA 中，总的分子间结合能被分解为“冻结密度”（frozen density）组分（FRZ）、极化（POL）项以及电荷转移（CT）项。“冻结密度”项定义为：将无限分离的片段彼此靠近时，其分子轨道（MO）不发生*任何*弛豫所对应的能量变化。FRZ 项计算为 FRAGMO 初始猜测能量与孤立片段上收敛的自洽场（SCF）能量之和的差值。极化（POL）能量项定义为片段上冻结的占据 MO 发生*片段内*（intrafragment）弛豫所带来的能量降低。POL 项计算为收敛的 SCF-MI 能量与 FRAGMO 初始猜测能量之差。最后，电荷转移（CT）能量项来源于 MO 进一步的*片段间*（interfragment）弛豫，计算为完全收敛的 SCF 能量与收敛的 SCF-MI 能量之差。

总电荷转移项包括如下能量降低：电子从一个分子上的占据轨道（更准确地说，是在收敛的 SCF-MI 态中的占据轨道）转移到另一个分子的虚轨道所带来的能量降低，以及伴随这种占据/虚轨道混合而产生的诱导效应所引起的进一步能量变化。占据-虚电子转移带来的能量降低可以通过从收敛的 SCF-MI 解出发的单次非迭代 Roothaan 步（Roothaan-step, RS）校正来描述。最为重要的是，SCF-MI(RS) 能量表达式的数学形式允许我们将占据-虚轨道混合项针对复合物中每一对分子分解为成键（bonding）与反馒（back-bonding）组分。剩余的电荷转移能量项（*即*，SCF-MI(RS) 能量与完全 SCF 能量之差）包含了伴随占据-虚电荷转移的所有诱导效应，通常数值很小。这最后一项被称为高阶（higher order, HO）弛豫。与 RS 贡献不同，高阶项无法自然地划分为正向给电子与反馒给电子项。每个电荷转移项（正向给电子、反馒以及高阶效应）相关的基组重叠误差（BSSE）都可以分别校正。

要执行能量分解分析，请在 *$molecule* 段中指定片段，并将 JOBTYPE 设置为 EDA。对于一个完整的 EDA 任务，**Q-Chem**

- 在孤立片段上执行 SCF 计算（若出现收敛问题可使用 *$rem_frgm* 段，但要确保该段中的关键字不会影响片段的最终能量），
- 生成 FRAGMO 初始猜测以获得 FRZ 项，
- 收敛 SCF-MI 方程以评估 POL 项，
- 执行微扰型（RS 或 ARS）变分校正的求值，以计算体系中每一对分子之间 CT 项的正向给电子与反馒组分，
- 收敛完整的 SCF 流程以评估 CT 项的高阶弛豫组分。

FRGM_LPCORR 关键字控制 EDA 任务中 CT 项的求值。若要评估上述所有 CT 组分，请将此关键字设置为 RS_EXACT_SCF 或 ARS_EXACT_SCF。如果 HO 项不重要，则可以通过将 FRGM_LPCORR 设置为 RS 或 ARS 来跳过最后一步（*即*，SCF 计算）。如果只需要总 CT 项，则将 FRGM_LPCORR 设置为 EXACT_SCF。

ALMO 电荷转移分析（ALMO-CTA）与 ALMO EDA 一同执行。[[680]](../bib_references/bib.md#bib707)
 ALMO 电荷转移尺度 $\Delta Q$ 提供了分子间键形成时电子云畸变程度的一种度量，并且使得所有 CT 项（*即*，正向给电子、反馒给电子以及高阶弛豫）都具有明确定义的能量效应（*即*，ALMO-CTA 与 ALMO-EDA 是自洽的）。

要从 CT 项中消除 BSSE（在能量尺度和电荷尺度上均如此），请将 EDA_BSSE 设置为 TRUE。**Q-Chem** 会为每个片段生成一个使用 MIXED 基组的输入文件以执行 BSSE 校正。与所有在具有 d 或更高角动量基函数的原子上使用 MIXED 基组的任务一样，需要设置 PURECART 关键字。如果 EDA_BSSE = TRUE，则在当前实现中不能使用广义基组（BASIS = GEN）。

请注意，片段的几何畸变能并未包含在 EDA 任务计算出的总结合能中。必须对孤立片段执行几何优化才能考虑这一项。

在 5.2 及之后的版本中，当设置 JOBTYPE = EDA 时将默认使用 “EDA2” 驱动（参见第 [12.6](sect_eda2.md) 节），它涵盖了第一代 ALMO-EDA/CTA 的几乎所有功能，同时包含许多新功能（例如对冻结项的进一步分解）。第一代 ALMO-EDA 的原始实现仍可通过设置 EDA2 = FALSE 来使用。

???+ example "示例 12.8：四聚体中水分子间结合能的能量分解分析，同时输出 ALMO-CTA 结果。"
    ```qchem
    $molecule
    0 1
    --
    0 1
    O          -0.106357    0.087598    0.127176
    H           0.851108    0.072355    0.136719
    H          -0.337031    1.005310    0.106947
    --
    0 1
    O           2.701100   -0.077292   -0.273980
    H           3.278147   -0.563291    0.297560
    H           2.693451   -0.568936   -1.095771
    --
    0 1
    O           2.271787   -1.668771   -2.587410
    H           1.328156   -1.800266   -2.490761
    H           2.384794   -1.339543   -3.467573
    --
    0 1
    O          -0.518887   -1.685783   -2.053795
    H          -0.969013   -2.442055   -1.705471
    H          -0.524180   -1.044938   -1.342263
    $end
    
    $rem
       JOBTYPE         EDA
       EDA2            FALSE
       METHOD          EDF1
       BASIS           6-31(+,+)g(d,p)
       PURECART        1112
       FRGM_METHOD     GIA
       FRGM_LPCORR     RS_EXACT_SCF
       EDA_BSSE        TRUE
    $end
    ```

???+ example "示例 12.9：Na ${}^{+}$ 与甲基自由基相互作用的开壳层 EDA 示例。"
    ```qchem
    $molecule
       1 2
    --
       0 2
       C       -1.447596  -0.000023   0.000019
       H       -1.562749   0.330361  -1.023835
       H       -1.561982   0.721445   0.798205
       H       -1.561187  -1.052067   0.225866
    --
       1 1
       Na       1.215591   0.000036  -0.000032
    $end
    
    $rem
       JOBTYPE              EDA
       EDA2                 FALSE
       METHOD               B3LYP
       BASIS                6-31G*
       UNRESTRICTED         TRUE
       SCF_GUESS            FRAGMO
       FRGM_METHOD          STOLL
       FRGM_LPCORR          RS_EXACT_SCF
       EDA_BSSE             TRUE
       DIIS_SEPARATE_ERRVEC 1
    $end
    ```
