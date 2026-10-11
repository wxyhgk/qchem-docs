---
title: "12.10.4 运行 XSAPT+MBD 计算任务"
---

## 12.10.4 运行 XSAPT+MBD 计算任务

(2026 年 7 月 4 日)

为了运行 XSAPT 计算任务，至少必须运行两个独立的作业，第三个作业是可选的，并且在诱导能被认为很重要时建议使用。第一个必须运行的作业是在整个体系上进行的、不带电荷嵌入（charge embedding）的二阶 SAPT 作业。该作业提供静电项、交换项和色散项的数值。（对于 XSAPT+MBD 方法[[200]](../bib_references/bib.md#bib188)作业，色散值将取自 MBD 计算得到的色散值）。第二个需要运行的作业是在整个体系上进行的、带电荷嵌入的 SAPT 作业。这个带电荷嵌入的 SAPT 作业起到对诱导能的校正作用，并且必须在每一对单体（monomer）上运行。因此，XSAPT 计算的最终诱导能等于不带电荷嵌入的 SAPT 作业的诱导能，加上带电荷嵌入的 SAPT 总能量与不带电荷嵌入的 SAPT 总能量之差。用公式表示，XSAPT 对诱导能的贡献为：

<a id="eq:xsapt_pol"></a>

$$
E_{\text{pol}}=\sum_{A}\sum_{B>A}\left[E_{AB}^{\text{XSAPT}}(AB)-E_{AB}^{\text{SAPT}}\right] \tag{12.69}
$$

这里方括号中的项是 $AB$ 二聚体（dimer）的电荷嵌入能量与不带电荷嵌入计算得到的 SAPT 能量之差。
因此，静电能、交换能和色散能将等同于从常规 SAPT 计算中得到的相同项，在 XSAPT 计算中发生变化的是诱导能。
还可以执行额外的计算以进一步校正诱导能，即 $\delta$HF 计算，它考虑了高于二阶的诱导能。
由此得到的 delta(SCF) 能量项随后被加到按上述方式计算得到的诱导能项上。

上述流程是在二聚体复合物上执行 XSAPT（$+\delta$HF）计算所要求的流程。
若要在 n 聚体复合物上执行 XSAPT（$+\delta$HF）计算，还需要进行更多计算。
其中之一是在每一对单体上运行带电荷嵌入的 SAPT 作业。
这是必需的，因为孤立二聚体的极化与嵌入在整个体系电荷中的二聚体的极化不同。
第二组作业（如果在执行 $\delta$HF 校正）是在每一对单体上运行 $\delta$HF 作业。
这些作业组同样会为体系的诱导能提供校正。

在 `$QC/bin/tools` 目录中存在两个帮助用户执行 XSAPT+MBD+$\delta$HF 计算的脚本。
名为 `xsapt_creation.py` 的脚本针对任意几何构型（由用户定义）创建三个文件：一个不带嵌入的 SAPT 作业、一个带嵌入的 SAPT 作业，以及一个 $\delta$HF 作业。
请参阅脚本以了解如何使用并修改脚本以供个人使用。
另一个名为 `xsapt_data_collection.py` 的脚本会遍历由 `xsapt_creation.py` 创建的三个作业的输出文件，
并执行所需的运算，以获得 XSAPT+MBD+$\delta$HF 作业正确的能量分解结果。
请参阅脚本以了解如何使用并修改它以供个人使用。

???+ example "示例 12.42: 水-水相互作用的 AO-XSAPT(KS)+ ai D3 计算。"
    ```qchem
    $molecule
    0 1
    --
       0 1
       O  -1.551007  -0.114520   0.000000
       H  -1.934259   0.762503   0.000000
       H  -0.599677   0.040712   0.000000
    --
       0 1
       O   1.350625   0.111469   0.000000
       H   1.680398  -0.373741  -0.758561
       H   1.680398  -0.373741   0.758561
    $end
    
    $rem
       JOBTYPE            xsapt
       EXCHANGE           gen
       LRC_DFT            true ! add LR-HFX
       BASIS              aug-cc-pVTZ
       MEM_TOTAL          46000
       MEM_STATIC         4000
       AO2MO_DISK         35000
       CHELPG_DX          5
       CHELPG_HEAD        30
       CHELPG_H           110
       CHELPG_HA          590
    $end
    
    $xpol
       embed   charges
       charges CHELPG
       DFT-LRC
       print   3
    $end
    
    $sapt
       algorithm     ao  ! for use with +aiD dispersion
       order         2   ! 2nd-order SAPT
       basis         projected
       Dispersion    aiD3
       print         3
    $end
    
    $xc_functional
       x   wPBE  1.0
       c   PBE   1.0
    $end
    
    $lrc_omega
       502
       502
    $end
    ```

???+ example "示例 12.43: 采用 PCM 边界条件的 XSAPT+MBD。"
    ```qchem
    $molecule
    0 1
    --
    0 1
    C    0.780147171  -0.609914733  -1.207556891
    H    0.896191595  -1.137639594  -2.144144625
    C    0.477942753   0.750993631  -1.207895407
    H    0.356964231   1.278167803  -2.144054074
    C    0.327289279   1.431867868  -0.000000000
    H    0.091465028   2.487139215   0.000000000
    C    0.477942754   0.750993631   1.207895407
    H    0.356964231   1.278167803   2.144054074
    C    0.780147171  -0.609914733   1.207556891
    H    0.896191595  -1.137639594   2.144144625
    C    0.931648311  -1.289981342   0.000000000
    H    1.168485730  -2.345213690  -0.000000000
    --
    0 1
    O   -2.743831210  -0.269262567   0.000000000
    H   -2.579027215  -1.213984095   0.000000000
    H   -1.856530267   0.102327758   0.000000000
    $end
    
    $rem
    jobtype ¯xsapt
    basis ¯¯def2-svpd
    lrc_dft ¯true
    method ¯¯lrc-wpbe
    scf_convergence 8
    solvent_method ¯pcm
    $end
    
    $xpol
    embed none
    dft-lrc
    print 3
    $end
    
    $sapt
    algorithm ao
    basis projected
    order 2
    print 3
    dispersion mbd
    $end
    
    $lrc_omega
    341
    502
    $end
    ```

???+ example "示例 12.44: Hg $\cdots$ H ${}_{2}$ O 范德华（van der Waals）复合物的 XSAPT+oC8(r)aimMBD。"
    ```qchem
    $comment
      XSAPT+oC8(r)aimMBD for the Hg...H2O van der Waals complex.
      def2-TZVPD auto-loads the matching ECP for Z > 36 (Hg), so the
      relativistic (r)aim free-atom reference is engaged automatically.
    $end
    
    $molecule
    0 1
    --
    0 1
       Hg    0.00000   0.00000   0.00000
    --
    0 1
       O     0.00000   0.00000   3.50000
       H     0.75670   0.00000   4.08590
       H    -0.75670   0.00000   4.08590
    $end
    
    $rem
       jobtype          xsapt
       method           hf
       basis            def2-tzvpd
       symmetry         false
       sym_ignore       true
       no_reorient      true
       scf_algorithm    diis
       scf_convergence  8
       mem_total        16000
       mem_static       8000
    $end
    
    $xpol
       embed none
       print 3            ! report per-atom Hirshfeld volume ratios
    $end
    
    $sapt
       algorithm  ao
       Dispersion OC8RAIMMBD   ! select the relativistic many-body AIM dispersion
    $end
    ```
