---
title: "7.12.1 面向核激发态的多体方法"
---

## 7.12.1 面向核激发态的多体方法

(July 4, 2026)

一种高度稳健且精确的策略是结合使用多体方法（例如 EOM 或 ADC）与核-价分离（core-valence separation，CVS）格式。[[218]](../bib_references/bib.md#bib215)

在该方法中，涉及核电子的激发与其余组态空间解耦。这使得人们能够降低计算开销，并将高度激发的核态与连续态分离开来。这些方法在第 [7.9.9](sub_cvs_eom.md) 节和第 [7.10.7](sect_CVS-ADC.md) 节中描述；CVS 也可以按照第 [7.12.2](subsec_TDDFT-Xray.md) 节所述部署于 TDDFT 之中。对于 K 边（1s $\rightarrow$ 虚拟轨道）激发，CVS 近似引入的误差可以忽略不计，[[573]](../bib_references/bib.md#bib589)
尽管其对其他类型 X 射线激发的精确性尚不确定。

对于闭壳层分子，另一种获得核激发能的高精度方法是使用受限开壳层 Kohn-Sham（restricted open-shell Kohn-Sham，ROKS）方法，详见第 [7.7.4](ex_ESROKS.md) 节。与 EOM 或 ADC 方法不同，ROKS 并不具备系统可改进性（systematically improvable），但依然相当精确，现代密度泛函能够将激发能的预测误差控制在 $<0.5$ eV 以内。[[510]](../bib_references/bib.md#bib525)
ROKS 方法的最大优势在于其计算效率：可以在与基态 meta-GGA 相同的 ${\cal{O}}({N^{3}})$ 标度下获得高精度结果，而 EOM-CCSD 的标度为 ${\cal{O}}({N^{6}})$，ADC(2) 的标度为 ${\cal{O}}({N^{5}})$。ROKS 对基组的要求也远比波函数理论温和，实践中混合基组（mixed basis）策略十分有效。关于将 ROKS 用于核能级激发的细节，请见第 [7.12.4](ex_COCOREIP.md) 节。

在 EOM-CC 形式框架内，还可以使用近似的 EOM-EE/IP 方法，其中目标态由单激发描述，双激发则以微扰方式处理；这些方法在第 [7.9.5.2](Ch7.S9.SS5.md#sec:EOM-S-D) 节中描述。这些方法虽有一定实用价值，但不如 CVS-EOM 各变体精确。[[1193]](../bib_references/bib.md#bib1248)

此外，还可以使用 $\Delta E$ 方法，即简单的能量差计算——核电离能由中性态与核电离态的能量差求得。该流程由下面的示例 7.12.1 演示。

???+ example "示例 7.204: 用于计算甲烷（CH ${}_{\text{4}}$ ）1s 能级化学位移的 Q-Chem 输入。第一个作业仅是一次 SCF 计算，用于获得中性分子的轨道与 CCSD 能量。第二个作业求解核电离态的 HF 与 CCSD 方程。"
    ```qchem
    $molecule
       0,1
       C      0.000000    0.000000    0.000000
       H      0.631339    0.631339    0.631339
       H     -0.631339   -0.631339    0.631339
       H     -0.631339    0.631339   -0.631339
       H      0.631339   -0.631339   -0.631339
    $end
    
    $rem
       EXCHANGE        = HF
       CORRELATION     = CCSD
       BASIS           = 6-31G*
       MAX_CIS_CYCLES  = 100
    $end
    
    @@@
    
    $molecule
       +1,2
       C      0.000000    0.000000    0.000000
       H      0.631339    0.631339    0.631339
       H     -0.631339   -0.631339    0.631339
       H     -0.631339    0.631339   -0.631339
       H      0.631339   -0.631339   -0.631339
    $end
    
    $rem
       UNRESTRICTED    = TRUE
       EXCHANGE        = HF
       BASIS           = 6-31G*
       MAX_CIS_CYCLES  = 100
       SCF_GUESS       = read  Read MOs from previous job and use occupied as specified below
       CORRELATION     = CCSD
       MOM_START       = 1 Do not reorder orbitals in SCF procedure!
    $end
    
    $occupied
       1 2 3 4 5
       2 3 4 5
    $end
    ```

在本作业中，我们首先计算中性 CH${}_{\text{4}}$ 的 HF 与 CCSD 能量：
$E_{\text{SCF}}=-40.1949062375~{}E_{h}$ 与 $E_{\text{CCSD}}=-40.35748087~{}E_{h}$（中性分子的 HF 轨道能量给出 Koopmans 电离能，即 11.210 hartree = 305.03 eV）。在第二个作业中，我们对核电离的 CH${}_{\text{4}}$ 做同样的计算。为了得到所需的 SCF 解，使用了 MOM_START 选项和 *$occupied* 关键字。所得能量为 $E_{\text{SCF}}=-29.4656758483~{}E_{h}$（$\langle\hat{S}^{2}\rangle$ =
0.7730）以及 $E_{\text{CCSD}}=-29.64793957~{}E_{h}$。因此，
$\Delta E_{\text{CCSD}}=10.709~{}E_{h}=291.42$ eV。

该方法还可以进一步扩展，通过执行 CIS、TDDFT 或 EOM-EE 计算来获得多个涉及核电子的激发态。

!!! note "注意"
    该方法在关联计算中常常导致收敛问题。


人们还可以使用示例 7.12.1 所演示的如下技巧。

???+ example "示例 7.205: 使用 EOM-IP 计算甲烷 1s 能级化学位移的 Q-Chem 输入。这里我们先按常规求解 SCF，然后重排分子轨道（MO），使核轨道成为“HOMO”，接着在所有价轨道冻结、核轨道保持活化的情况下求解 CCSD 与 EOM-IP 方程。"
    ```qchem
    $molecule
       0,1
       C      0.000000    0.000000    0.000000
       H      0.631339    0.631339    0.631339
       H     -0.631339   -0.631339    0.631339
       H     -0.631339    0.631339   -0.631339
       H      0.631339   -0.631339   -0.631339
    $end
    
    $rem
       EXCHANGE        = HF
       BASIS           = 6-31G*
       MAX_CIS_CYCLES  = 100
       CORRELATION     = CCSD
       CCMAN2          = false
       N_FROZEN_CORE   = 4 Freeze all valence orbitals
       IP_STATES       = [1,0,0,0] Find one EOM_IP state
    $end
    
    $reorder_mo
       5 2 3 4 1
       5 2 3 4 1
    $end
    ```

这里我们使用 EOM-IP 来计算核电离态。由于核态能量非常高，我们使用“冻结核（frozen core）”技巧，将价电离态从计算中剔除。也就是说，我们重排 MO，使核轨道成为最后一个占据轨道，然后冻结其余所有轨道。如此计算得到的 EOM-IP 能量为 245.57 eV。从 EOM-IP 振幅可以看出，该态具有 Koopmans 特征（以单重核电离为主）；因此，正则 HF MO 能很好地表示关联的 Dyson 轨道。同样的策略可用于计算核激发态。

!!! note "注意"
    该方法的精确性相当差，与 Koopmans 近似相当。


---

已同时保存为 `translated_7_12_1_many_body_core_excited.md`。
