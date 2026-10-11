---
title: "6.12.5 随机化 CC2 与 CCSD"
---

## 6.12.5 随机化 CC2 与 CCSD

(July 4, 2026)

**libgmbpt** 中提供了随机化 RI-CC2（sRI-CC2）的实现。
目前，代码支持 RI-CC2 与 sRI-CC2 的性质计算，包括基态与激发态（单重态和三重态）能量、基态与激发态的解析梯度、振子强度以及导数耦合（derivative couplings）。
sRI-CC2 的主要优势在于其更低的计算标度（scaling）——${\cal{O}}({N^{3}})$，相比之下 RI-CC2 为 ${\cal{O}}({N^{5}})$——这使得该方法可以应用于大得多的分子体系。
这些代码仍在开发之中。建议用户参考名为 `libgmbpt_sricc$\ast$` 和 `libgmbpt_thc_sricc$\ast$` 的示例作业以获取使用指导。

**注意：

sRI-CC2 目前不支持冻结芯层（frozen core）：N_FROZEN_CORE 必须设为零。
**

**注意：

sRI-CC2 目前不支持几何结构优化，只能与 JOBTYPE=SP 配合使用。
**

RI-CC2 与 sRI-CC2 通过设置 METHOD = CC2 *并且* 适当指定
AIX_BASIS 来启用。
SRI-CC2 仅在 **libgmbpt** 中可用，因此应在 *$rem* 段中设置 CCMAN2 = -1，并在
*$development* 段中添加 do_sri = 1。
然后，在 *$development* 段中，添加关键字 sri 以控制 sRI 的使用：0 表示确定性
RI 计算，1 表示具有 ${\cal{O}}({N^{3}})$ 标度的 sRI 计算，2 表示部分 sRI（partial sRI）计算。
在某些情况下（例如梯度计算），sRI 方法会引入显著噪声。
为缓解此类问题，可以采用部分 sRI 方案，其标度次优（为 ${\cal{O}}({N^{4}})$），但精度有所提升。

关键字 sri_ntheta 指定 sRI 轨道的数目。它相当于标度中的前置因子，
较大的取值可带来更好的精度。

???+ example "示例 6.31: 水分子的 sRI-CC2 激发能。"
    ```qchem
    $molecule
        0 1
        O 0.0 0.0 0.0
        H 0.0  0.75410300 -0.56492300
        H 0.0 -0.75410300 -0.56492300
    $end
    
    $rem
        CCMAN2        -1                ! use code in libgmbpt
        method        CC2
        BASIS         cc-pvdz
        AUX_BASIS     RIMP2-cc-pVDZ
        EE_SINGLETS   [1]
        N_FROZEN_CORE 0                 ! frozen core (FC) electrons
    $end
    
    ! below for sRI development
    $development
        do_sri        1
        sri           1                 ! if use sRI, 0-RI, 1-complete sRI, 2-partial sRI
        nsinglets     1                 ! number of singlet states
    !    ntriplets    0                 ! number of triplet states
        sri_ntheta    5000              ! number of stochastic orbitals
        sri_nseed     0                 ! index to generate stochastic seed : 0~23
    $end
    
    ```

THC（张量超收缩，tensor hypercontraction）实现（THC-sRI-CC2）为 sRI-CC2 提供了进一步改进，
在同样的性质集合上具有 ${\cal{O}}({N^{3}})$ 标度并降低了随机噪声。
通过在 *$rem* 段中添加 thc = $1$ 并在 *$development* 段中设置 sri = $2$ 即可调用
THC-sRI-CC2。其余关键字与 sRI-CC2 相同。

???+ example "示例 6.32: 水分子的 THC-sRI-CC2 基态解析梯度。"
    ```qchem
    $molecule
        0 1
        O 0.0 0.0 0.0
        H 0.0  0.75410300 -0.56492300
        H 0.0 -0.75410300 -0.56492300
    $end
    
    $rem
        CCMAN2        -1                ! use code in libgmbpt
        method        CC2
        BASIS         cc-pvdz
        AUX_BASIS     RIMP2-cc-pVDZ
        N_FROZEN_CORE 0                 ! frozen core (FC) electrons, n
        CC_EOM_PROP   true              ! properties calculation
        thc           1                 ! if use THC
    $end
    
    ! below for sRI development
    $development
        do_sri 1
        sri 2                           ! 2-THC-sRI
        sri_ntheta 5000                 ! number of stochastic orbitals for energy
        sri_grad_ntheta 5000            ! number of stochastic orbitals for gradient solution
        sri_nseed 0                     ! index to generate stochastic seed : 0~23
        gradient_gs 1                   ! ground_state gradient calculation
    $end
    
    ```

最后，THC-sRI-CCSD 可用于以 ${\cal{O}}({N^{3}})$ 标度计算
基态与激发态能量。
通过在 *$development* 段中添加 sriccsd = 1 即可调用 THC-sRI-CCSD。

???+ example "示例 6.33: 水分子的 THC-sRI-CCSD 基态能量。"
    ```qchem
    $molecule
        0 1
        O 0.0 0.0 0.0
        H 0.0  0.75410300 -0.56492300
        H 0.0 -0.75410300 -0.56492300
    $end
    
    $rem
        CCMAN2         -1                ! use code in libgmbpt
        method         CC2
        BASIS          cc-pvdz
        AUX_BASIS      RIMP2-cc-pVDZ
        N_FROZEN_CORE  0                 ! frozen core (FC) electrons, n
        CC_CONVERGENCE 6
        thc            1                 ! if use THC
    $end
    
    ! below for sRI development
    $development
        do_sri         1
        sri            2                 ! if use sri, 0-THC, 2-THC-sRI
        sri_ntheta     5000              ! number of stochastic orbitals
        sri_nseed      0                 ! index to generate stochastic seed : 0~23
        sriccsd        1                 ! CCSD
    $end
    
    ```

更多技术细节，参见参考文献 [[1554]](../bib_references/bib.md#bib1632)
.
