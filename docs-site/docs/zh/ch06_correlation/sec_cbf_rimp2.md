---
title: "6.6.10 复数基函数的 RI-MP2 方法"
---

## 6.6.10 复数基函数的 RI-MP2 方法

(July 4, 2026)

基于 White、Head-Gordon 和 McCurdy 在 libqints 中对复数基函数（complex basis functions）的通用实现[[1457]](../bib_references/bib.md#bib1525)

（见第 [4.9.5](../ch04_scf/sec_cbfscf.md) 节），现已实现一种用于复数共振能的 RI-MP2 方法。[[1397]](../bib_references/bib.md#bib592)

该方法目前仅适用于闭壳层（closed-shell）体系。RI 近似既可以应用于复数 MP2 能量，也可以应用于复数 HF 能量的库仑（Coulomb）部分与交换（exchange）部分。对于电子共振而言，使用 RI 近似尤其具有优势，因为采用复标度（complex-scaled）方法处理这类问题需要使用包含大量弥散函数的大基组。在许多情况下，RI 可将计算时间缩短 10 倍甚至更多。此外，辅助基组（auxiliary basis set）中无需包含复标度函数，使用标准的辅助基组即可获得极好的结果。[[1398]](../bib_references/bib.md#bib593)

完整基组通过关键字 COMPLEX_BASIS 指定，而 BASIS 指定其中未标度的部分。这一流程在第 [8.7](../ch08_basis/sect_zbas.md) 节中有详细描述。与之完全类似地，辅助基组通过关键字 COMPLEX_AUX_BASIS 和 AUX_BASIS 指定。关键字 COMPLEX_RI_JK 用于控制 RI 近似是仅应用于 MP2 部分，还是同时应用于 HF 参考。

关于电子共振、**Q-Chem** 在此方面提供的功能以及相关关键字的更多信息，请参见第 [4.9.5](../ch04_scf/sec_cbfscf.md) 节和第 [7.9.10](../ch07_excited/sub_cc_cs_cap.md) 节。

???+ example "示例 6.20: 在强度为 0.1 a.u. 的静电场中，对 N ${}_{2}$ 的复数共振能（即 Stark 移动后的能量与隧穿电离速率）进行 RI-MP2 计算的 Q-Chem 输入"
    ```qchem
    $molecule
       0 1
       N  0.00  0.00  0.55
       N  0.00  0.00 -0.55
    $end
    
    $rem
       CORRELATION           RIMP2
       BASIS                 6-31G
       COMPLEX_BASIS         6-31G*
       AUX_BASIS             rimp2-aug-cc-pVDZ
       COMPLEX_AUX_BASIS     rimp2-aug-cc-pVDZ
       COMPLEX_RI_JK         true
       COMPLEX_CCMAN         true
       SCF_GUESS             gwh
       SCF_CONVERGENCE       10
       COMPLEX_EXPONENTS     1
       COMPLEX_THETA         80
       COMPLEX_SCF           1
       COMPLEX_SCF_GUESS     1
       COMPLEX_N_ELECTRONS   0
       COMPLEX_METSCF        1
       GEN_SCFMAN            true
       THRESH                14
       PURECART              1111
       INTEGRAL_SYMMETRY     false
       POINT_GROUP_SYMMETRY  false
    $end
    
    $complex_ccman
       stark_z   1000
       cs_alpha  1000
       cs_theta  0
    $end
    ```
