---
title: "5.3.6 专用泛函"
---

## 5.3.6 专用泛函

（2026 年 7 月 4 日）

- SRC1-R1：TDDFT 短程校正（short-range corrected）泛函
[Ref. [[123]](../bib_references/bib.md#bib112) 中的式 (1)，第一行原子]
- SRC1-R2：TDDFT 短程校正泛函
[Ref. [[123]](../bib_references/bib.md#bib112) 中的式 (1)，第二行原子]
- SRC2-R1：TDDFT 短程校正泛函
[Ref. [[123]](../bib_references/bib.md#bib112) 中的式 (2)，第一行原子]
- SRC2-R2：TDDFT 短程校正泛函
[Ref. [[123]](../bib_references/bib.md#bib112) 中的式 (2)，第二行原子]
- BR89：Becke-Roussel 元广义梯度近似（meta-GGA）交换泛函，仿照氢原子建模[[91]](../bib_references/bib.md#bib75)
- B94：Becke 提出的 meta-GGA 关联泛函，利用 BR89 交换泛函计算库仑势[[97]](../bib_references/bib.md#bib79)
- B94hyb：B94 关联泛函的改进版本，与 BR89B94hyb 交换-关联泛函配合使用[[97]](../bib_references/bib.md#bib79)
- BR89B94h：15.4% HF 交换 + 84.6% BR89 meta-GGA 交换 + BR89hyb meta-GGA 关联[[97]](../bib_references/bib.md#bib79)
- BRSC：原始 B05 交换-关联泛函的交换组分[[101]](../bib_references/bib.md#bib85)
- MB05：改进版 B05（BM05）交换-关联泛函的交换组分[[1128]](../bib_references/bib.md#bib1179)
- B05：Becke 提出的完整精确交换 Kohn-Sham 方案，使用精确交换能量密度（RI）并考虑静态关联[[101]](../bib_references/bib.md#bib85)
- BM05 (XC)：改进的 B05 超广义梯度近似（hyper-GGA）方案，采用 MB05 取代 BRSC 作为交换泛函[[1128]](../bib_references/bib.md#bib1179)
- PSTS：Perdew、Staroverov、Tao 和 Scuseria 提出的 hyper-GGA（100% HF 交换）交换-关联泛函[[1072]](../bib_references/bib.md#bib1119)
- MCY2：基于绝热连接（adiabatic connection）的 Mori-Sánchez-Cohen-Yang hyper-GGA 交换-关联泛函[[960]](../bib_references/bib.md#bib1001)

本示例演示 RI-B05 与 RI-PSTS 泛函的用法。目前这些泛函仅可用于单点能计算，并且先通过（*例如*）LDA 或 HF 计算获得收敛的 SCF 轨道可以极大地促进收敛（下面的示例使用了 LDA，也可以替换为 HF）。使用 RI 近似（第 [6.6](../ch06_correlation/topic_rimp2.md) 节）需要指定辅助基组（auxiliary basis set）。

???+ example "示例 5.1：使用 RI-B05 计算 H ${}_{2}$ 的 Q-Chem 输入"
    ```qchem
    $comment
       H2, example of SP RI-B05.  First do a well-converged LSD, G3LARGE is the
       basis of choice for good accuracy.
    $end
    
    $molecule
       0 1
       H   0.  0.   0.0
       H   0.  0.   0.7414
    $end
    
    $rem
       METHOD           lda
       BASIS            g3large
       SCF_GUESS        core     ! required
       PURECART         2222     ! required
       THRESH           14
       INCDFT           false
       SCF_CONVERGENCE  9
       POINT_GROUP_SYMMETRY false
       INTEGRAL_SYMMETRY    false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       EXCHANGE        b05            ! or set to psts for ri-psts
       BASIS           g3large
       AUX_BASIS       rib05-cc-pvtz  ! the aux basis for both RI-B05 and RI-PSTS
       SCF_GUESS       read
       PURECART        2222           ! required
       THRESH          4
       PRINT_INPUT     true
       INCDFT          false
       MAX_SCF_CYCLES  0              ! required
       DFT_CUTOFFS     0              ! required
       POINT_GROUP_SYMMETRY false
       INTEGRAL_SYMMETRY    false
    $end
    ```
