---
title: "6.6.7 Brueckner CC2"
---

## 6.6.7 Brueckner CC2

（2026 年 7 月 4 日）

已有研究表明，Brueckner 轨道（Brueckner Orbitals, BOs）能够在很大程度上缓解 Hartree-Fock（HF）级别下出现的人为对称性破缺问题。[[783]](../bib_references/bib.md#bib826)

这甚至可以为那些通常以 HF 轨道作为起点的高阶波函数理论带来更好的结果。遗憾的是，最廉价的经典 Brueckner 理论——Brueckner 双激发（Brueckner Doubles, BD）——在计算上仍然相当昂贵。轨道优化 MP2（Orbital Optimized MP2, OOMP2）被提出作为 BD 的低标度近似，[[852]](../bib_references/bib.md#bib888)
 这源于它与轨道优化耦合簇双激发（Orbital Optimized Coupled Cluster Doubles, OOCCD）的相似性。获得近似 BD 轨道的另一途径是 Brueckner CC2（BCC2）。[[30]](../bib_references/bib.md#bib14)

与 OOMP2 优化能量不同，BCC2 通过优化轨道使 CC2 的单激发振幅 t${}_{1}$ 降为 0。在不存在 t${}_{1}$ 振幅的情况下，CC2 的双激发振幅与 MP2 完全相同，而单激发振幅方程如下：

<a id="eq:bcc2"></a>
$$
\Omega_{i}^{a}=f_{ai}+\sum_{jb}f_{jb}t_{ij}^{ab}+\frac{1}{2}\sum_{jbc}\langle
ja||cb\rangle t_{ij}^{bc}+\frac{1}{2}\sum_{jkb}\langle jk||bi\rangle t_{jk}^{ab} \tag{6.30}
$$

BCC2 的计算成本按 $\mathcal{O}(o^{2}v^{3})$ 标度——相比 OOCCD/BD 有显著改进；并且由于减少了人为的自旋污染，它能大幅提升开壳层分子中轨道的质量（相对于 HF）。

???+ example "示例 6.16: BCC2 方法示例"
    ```qchem
    $molecule
       1 2
       F
       H 1 1.001
    $end
    
    $rem
       UNRESTRICTED      TRUE
       JOBTYPE           SP
       EXCHANGE          HF
       GEN_SCFMAN_FINAL  TRUE
       DO_BCC2           3                run BCC2
       SCF_ALGORITHM     DIIS
       SCF_GUESS         GWH
       BASIS             sto-3g
       AUX_BASIS         rimp2-vdz
       SCF_CONVERGENCE   8
       THRESH            14
       PURECART          1111
       INTEGRAL_SYMMETRY FALSE
    $end
    ```

由于 CC2 是一种类似于 MP2 的微扰方法，在存在轨道简并时会发生失效（breakdown）。虽然 BCC2 并不显式地优化能量、从而不会将轨道推向简并，但当轨道能差变小时，结果仍然会受到严重不利影响。由 Joonho Lee 和 Martin Head-Gordon 最初提出的 $\kappa$ 正则化器（regularizer）[[782]](../bib_references/bib.md#bib825)
 在这种情况下可用于进一步改善 BCC2 的结果。该正则化器通过按如下方式修改 $t_{ij}^{ab}$ 振幅来实现：

<a id="eq:kbcc2"></a>
$$
t_{ij}^{ab}=\frac{-\langle ab||ij\rangle}{\Delta_{ij}^{ab}}\left(1-\exp(-\kappa\Delta_{ij}^{ab})\right)^{2} \tag{6.31}
$$

与 $\kappa$-OOMP2 类似，参数 $\kappa$ 决定正则化强度，其中 $\kappa=0$ 得到 HF，$\kappa=\infty$ 得到未正则化的 BCC2。对大多数应用，建议取值 $\kappa=1.2$ $E_{h}^{-1}$。$\kappa$-BCC2 通过 `libgscf` 和 `libgmbpt` 运行。
目前，应使用 DIIS 来收敛 BCC2 轨道，因为单激发残差不等于轨道梯度，不能用于基于梯度的算法。BCC2 代码目前支持限制（Restricted, R）和非限制（Unrestricted, U）两种轨道类型。

与运行 $\kappa$-BCC2 相关的 rem 变量总结如下：

| CORRELATION | None（默认） |
| --- | --- |
| JOBTYPE | sp（默认）单点能计算 |
| BASIS | 用户自选（标准基组或用户自定义：GENERAL 或 MIXED） |
| GEN_SCFMAN_FINAL | TRUE |
| SCF_ALGORITHM | DIIS（基于梯度的算法目前不支持） |
| AUX_BASIS | 对应的辅助基组（标准基组或用户自定义： |
|  | AUX_GENERAL 或 AUX_MIXED） |
| DO_BCC2 | 3（运行 BCC2） |
| REGULARIZED_BCC2 | 0（不使用正则化器；默认） |
|  | 1（$\delta$-正则化器） |
|  | 2（$\kappa$-正则化器；推荐） |
|  | 3（$\sigma$-正则化器） |
| REG_PARAMETER | 正则化参数乘以 1e ${}^{3}$；无默认值 |
|  | 1200（$\kappa$-BCC2 的推荐值） |
| N_FROZEN_CORE | 0（目前不支持冻结芯层） |
| N_FROZEN_VIRTUAL | 0（目前不支持冻结芯层） |
| DO_S2 | 0（默认） |
|  | 1（在 MP2 级别计算 $\langle\hat{S}^{2}\rangle$） |

???+ example "示例 6.17: 采用 R 轨道类型的 $\kappa$-BCC2 应用于水二聚体"
    ```qchem
    $molecule
       0  1
       O    -2.766559046    0.187082886    0.566917837
       H    -3.696304300    1.179189102   -0.642506882
       H    -3.395837846   -1.509891173    0.389283582
       O     2.587035064    0.275900014   -0.746441819
       H     3.579141280    0.918406897    0.633058252
       H     0.852266482    0.311804811   -0.156847268
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvdz
       AUX_BASIS_CORR    rimp2-cc-pvdz
       THRESH            14
       INPUT_BOHR        true
       SCF_CONVERGENCE   8
       MAXSCF            1000
       SCF_GUESS         sad
       GEN_SCFMAN_FINAL  true
       UNRESTRICTED      false    use restricted
       DO_BCC2           3        run BCC2
       REGULARIZED_O2    2        use kappa-regularizer
       REG_VARIABLE      1450     set kappa = 1.45
       INTEGRAL_SYMMETRY false
    $end
    ```

???+ example "示例 6.18: 采用 U 轨道类型的 $\kappa$-BCC2 应用于 OH 自由基"
    ```qchem
    $molecule
    0  2
    O -2.766559046 0.187082886 0.566917837
    H -3.6963043 1.179189102 -0.642506882
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvdz
       AUX_BASIS_CORR    rimp2-cc-pvdz
       THRESH            14
       INPUT_BOHR        true
       SCF_CONVERGENCE   8
       MAXSCF            1000
       SCF_GUESS         sad
       GEN_SCFMAN_FINAL  true
       UNRESTRICTED      true   ! use unrestricted
       DO_BCC2           3      ! run BCC2
       REGULARIZED_O2    2      ! use kappa-regularizer
       REG_VARIABLE      1450   ! set kappa = 1.45
       INTEGRAL_SYMMETRY false
    $end
    ```
