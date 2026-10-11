---
title: "7.4.5 TAO-DFT 的实时扩展（RT-TAO）"
---

## 7.4.5 TAO-DFT 的实时扩展（RT-TAO）

（2026 年 7 月 4 日）

为了研究从基态出发的大型强关联体系的含时动力学，
并以最小化计算复杂度为重点，
Hung-Yi Tsai 与 Jeng-Da Chai 教授将热辅助占据密度泛函理论（thermally-assisted-occupation density functional theory, TAO-DFT）[[227]](../bib_references/bib.md#bib222)
 推广到了实时 TAO-DFT（RT-TAO）。[[1376]](../bib_references/bib.md#bib1437)

RT-TAO 方法首先进行一次 TAO-DFT 计算（参见第 [5.12.3](../ch05_dft/ex_ptao.md) 节），随后进行时间演化（参见第 [7.4](sec_TDKS.md) 节）。
RT-TAO 所需的计算代价与含时 Kohn-Sham（time-dependent Kohn-Sham）相当，
并且在不存在显著静态关联效应时，其计算代价与含时 Kohn-Sham 完全相同。

要执行 RT-TAO 计算，用户需在 *$rem* 输入段中设置 TAO_DFT = TRUE 和 TDKS = TRUE。
更多作业控制选项详见第 [5.12.3](../ch05_dft/ex_ptao.md) 节和第 [7.4.2](sec_TDKS_JobControl.md) 节。

RT-TAO 作为 TAO-DFT 的实时扩展，由一个记为 $\theta$ 的虚拟温度参数（fictitious temperature parameter）所控制。
将 TAO_DFT_THETA 设为 0，该方法即退化为普通的含时 Kohn-Sham。[[1376]](../bib_references/bib.md#bib1437)

在绝热近似下，除了交换关联（exchange-correlation, XC）泛函之外，RT-TAO 还需要一个额外的泛函 $E_{\theta}[\rho]$。

下面给出两个 RT-TAO 计算的示例：

???+ example "示例 7.37：RT-TAO-ALDA，对拉长的 H ${}_{2}$ 进行自旋限制计算"
    ```qchem
    $molecule
       0 1
       H 0.000000 0.000000 1.000000
       H 0.000000 0.000000 -1.000000
    $end
    
    $rem
       BASIS               6-31G*
       EXCHANGE            gen
       TDKS                true
       SCF_CONVERGENCE     7
       TAO_DFT             true
       TAO_DFT_THETA       40   ! theta = 40 mhartree
       TAO_DFT_THETA_NDP   3    ! default
    $end
    
    $xc_functional
       X   S             1.0
       C   PW92          1.0
       X   ETheta_LDA    1.0
    $end
    
    $tdks
       DT             0.05
       MAXITER        10 ! for production, want a much larger value
       PROPAGATOR     MMUT
       FIELD_VECTOR   1 1 1
       FIELD_TYPE     delta
       FIELD_AMP      0.0001
    $end
    ```

???+ example "示例 7.38：RT-TAO-ALDA，对拉长的 H ${}_{2}$ 进行自旋非限制计算"
    ```qchem
    $molecule
       0 1
       H 0.000000 0.000000 1.000000
       H 0.000000 0.000000 -1.000000
    $end
    
    $rem
       UNRESTRICTED        true
       BASIS               6-31G*
       EXCHANGE            gen
       TDKS                true
       SCF_CONVERGENCE     7
       TAO_DFT             true
       TAO_DFT_THETA       40   ! theta = 40 mhartree
       TAO_DFT_THETA_NDP   3    ! default
       SCF_GUESS           gwh
       SCF_GUESS_MIX       3    ! mix in 30% LUMO in alpha to break symmetry
    $end
    
    $xc_functional
       X   S             1.0
       C   PW92          1.0
       X   ETheta_LDA    1.0
    $end
    
    $tdks
       DT             0.05
       MAXITER        10 ! for production, want a much larger value
       PROPAGATOR     MMUT
       FIELD_VECTOR   1 1 1
       FIELD_TYPE     delta
       FIELD_AMP      0.0001
    $end
    ```
