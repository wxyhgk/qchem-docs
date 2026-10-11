---
title: "6.6.6 轨道优化 MP2（Orbital-Optimized MP2）"
---

## 6.6.6 轨道优化 MP2（Orbital-Optimized MP2）

（2026 年 7 月 4 日）

当人们无法确定 Hartree-Fock（HF）级别是否发生了人为对称性破缺时，Brueckner 轨道（Brueckner Orbitals, BOs）是非常有吸引力的选择。称之为*人为的（artificial）*对称性破缺，是因为这种破缺仅仅反映了 HF 级别下动态关联（dynamic correlation）的缺失，而非强关联（strong correlation）的存在。另一方面，单参考（single-reference）方法也可能通过*本质性（essential）*对称性破缺来尝试描述强关联体系。因此，通常关键在于通过在考虑电子关联的前提下求得轨道，从而区分这两种情形。[[783]](../bib_references/bib.md#bib826)

由于轨道优化的耦合簇 singles-doubles（Orbital-Optimized Coupled-Cluster Doubles, OOCCD）计算代价较高（$\mathcal{O}(o^{2}v^{4})$），Rohini Lochan 在 Martin Head-Gordon 的指导下提出通过对 MP2 关联能进行优化来获得轨道。为此，将 Brueckner 轨道引入 SOSMP2 与 MOSMP2 方法，以解决常与 Hartree-Fock 轨道相关联的对称性破缺和自旋污染（spin contamination）问题。分子轨道的优化基于平均场能量加上作为二体微扰二阶关联能之自旋相反分量（opposite-spin component）的关联能，并乘以一个经验选取的标度参数。这种"优化二阶自旋相反"（optimized second-order opposite-spin, O2）方法[[852]](../bib_references/bib.md#bib888)
 在每个轨道迭代步需要四阶（fourth-order）计算量。结果表明，对于闭壳层（closed-shell）分子，O2 方法给出的结构和频率预测与标度 MP2 方法非常接近；而对于开壳层（open-shell）分子，O2 则带来了显著改进，其自旋污染与对称性破缺问题被大幅缓解。

???+ example "示例 6.12: O2 方法应用于 ${\cal{O}}({N^{4}})$ SOSMP2 的示例"
    ```qchem
    $molecule
       1 2
       F
       H 1 1.001
    $end
    
    $rem
       EXCHANGE          HF
       BASIS             sto-3g
       UNRESTRICTED      TRUE
       JOBTYPE           FORCE            Options are SP/FORCE/OPT
       DO_O2             1                O2 with O(N^4) SOS-MP2 algorithm
       SOS_FACTOR        1000000          Opposite Spin scaling factor = 1.0
       SCF_ALGORITHM     DIIS_GDM
       SCF_GUESS         GWH
       AUX_BASIS         rimp2-vdz
       SCF_CONVERGENCE   8
       THRESH            14
       PURECART          1111
       INTEGRAL_SYMMETRY FALSE
    $end
    ```

???+ example "示例 6.13: O2 方法应用于 ${\cal{O}}({N^{4}})$ MOSMP2 的示例"
    ```qchem
    $molecule
       1 2
       F
       H 1 1.001
    $end
    
    $rem
       UNRESTRICTED      TRUE
       JOBTYPE           FORCE      ! Options are SP/FORCE/OPT
       EXCHANGE          HF
       DO_O2             2          ! O2 with O(N^4) MOS-MP2 algorithm
       OMEGA             600        ! Omega = 600/1000 = 0.6 a.u.
       SCF_ALGORITHM     DIIS_GDM
       SCF_GUESS         GWH
       BASIS             sto-3g
       AUX_BASIS         rimp2-vdz
       SCF_CONVERGENCE   8
       THRESH            14
       PURECART          1111
       INTEGRAL_SYMMETRY FALSE
    $end
    ```

尽管 O2（即 OOMP2）在众多应用中取得了成功，该模型仍存在两点局限。首先，能量优化常常会遇到由 MP2 能量在小能分母处出现奇点所引起的数值不稳定性。其次，Coulson-Fischer 点的消失阻碍了*本质性*对称性破缺的使用。这促使 David Stück 与 Martin Head-Gordon 发展了正则化 OOMP2（regularized OOMP2），其中采用线性能级移动（level shift）参数 $\delta$ 来稳定较小的能分母。[[1318]](../bib_references/bib.md#bib1376)
 然而研究发现，当希望保持 $\delta$ 足够大以恢复 Coulson-Fischer 点时，$\delta$-OOMP2 的热化学性能令人失望。[[1155]](../bib_references/bib.md#bib1207)

Joonho Lee 在 Martin Head-Gordon 的指导下开发了一套新的正则化 OOMP2 方法族，与 $\delta$-正则化器（$\delta$-regularizer）不同，它采用了一种依赖于能量的正则化器（$\kappa$-正则化器，$\kappa$-regularizer）。[[782]](../bib_references/bib.md#bib825)

$\kappa$-正则化器对 MP2 关联能的修正如下：

<a id="eq:kmp2"></a>
$$
E_{\kappa-\text{MP2}}=-\frac{1}{4}\sum_{ijab}\frac{|\langle ij||ab\rangle|^{2}}{\Delta_{ij}^{ab}}\left(1-\exp(-\kappa\Delta_{ij}^{ab})\right)^{2} \tag{6.29}
$$

其中能分母 $\Delta_{ij}^{ab}=\epsilon_{a}\epsilon_{b}-\epsilon_{i}-\epsilon_{j}$，$\kappa$ 控制正则化的强度。显然，$\kappa=0$ 时关联能为零（*即*，回到 HF），而 $\kappa\rightarrow\infty$ 则恢复未正则化的 MP2 能量表达式。在 $\kappa$-OOMP2 中，轨道由 $E_{\text{HF}}E_{\kappa-\text{MP2}}$ 的极小值确定。推荐使用 $\kappa = 1.45\ E_{h}^{-1}$，因为它在 Coulson-Fischer 点的恢复与热化学性能之间取得了良好平衡。需要注意的是，$\kappa$-OOMP2 通过 **Q-Chem** 全新的 SCF 库 `libgscf` 和全新的 MP2 库 `libgmbpt` 运行。较旧的 OOMP2 代码（由 Rohini Lochan 和 David Stück 编写）已不再受支持，若使用须格外谨慎。此外，新的 OOMP2 代码可以处理限制型（restricted, R）、复数限制型（complex restricted, cR）、非限制型（unrestricted, U）、广义型（generalized, G）以及复数广义型（complex generalized, cG）轨道类型。复数非限制型（complex unrestricted, cU）轨道类型由于其适用性有限，目前尚不支持。

用于运行 $\kappa$-OOMP2 的相关 rem 变量汇总：

| CORRELATION | None（默认值） |
| --- | --- |
| JOBTYPE | sp（默认）单点能计算；force（支持受力计算）；opt（支持几何结构优化） |
| BASIS | 用户自选（标准基组或用户自定义基组：GENERAL 或 MIXED） |
| GEN_SCFMAN_FINAL | TRUE（若请求 $\kappa$ -OOMP2，则为默认值） |
|  | FALSE（其他 SCF 计算的默认值） |
| SCF_ALGORITHM | GDM（默认值） |
|  | DIIS |
|  | GDM-LS |
| AUX_BASIS | 相应的辅助基组（标准基组或用户自定义基组： |
|  | AUX_GENERAL 或 AUX_MIXED） |
| REGULARIZED_O2 | 0（不使用正则化器；默认值） |
|  | 1（$\delta$ -正则化器） |
|  | 2（$\kappa$ -正则化器；推荐） |
|  | 3（$\sigma$ -正则化器） |
| REG_PARAMETER | 正则化参数乘以 1e ${}^{3}$ ；无默认值 |
|  | 1450（$\kappa$ -OOMP2 的推荐值） |
| N_FROZEN_CORE | 0（代码支持此功能，但由于存在某些收敛问题， |
|  | 不推荐使用） |
| N_FROZEN_VIRTUAL | 0（代码支持此功能，但由于存在某些收敛问题， |
|  | 不推荐使用） |
| SCS | 0（默认值） |
|  | 1 开启自旋成分标度（spin-component scaling），采用 SCS-OOMP2、 |
|  | 2 SOS-OOMP2、 |
|  | 3 任意自旋成分标度的 SCS-OOMP2 |
| SSS_FACTOR | 1000000（默认值）指定同自旋成分（same-spin-component）标度因子（乘以 1e ${}^{6}$ ） |
| SOS_FACTOR | 1000000（默认值）指定自旋相反成分（opposite-spin-component）标度因子（乘以 1e ${}^{6}$ ） |
| DO_S2 | 0（默认值） |
|  | 1（在 MP2 级别计算 $\langle\hat{S}^{2}\rangle$） |

???+ example "示例 6.14: 采用 cG 轨道类型的 $\kappa$ -OOMP2 应用于 OH 的示例"
    ```qchem
    $molecule
       0  2
       O  -2.766559046  0.187082886   0.566917837
       H  -3.696304300  1.179189102  -0.642506882
    $end
    
    $rem
       BASIS              cc-pvdz
       AUX_BASIS          rimp2-cc-pvdz
       EXCHANGE           hf
       THRESH             14
       INPUT_BOHR         true
       SCF_CONVERGENCE    8
       SCF_ALGORITHM      gdm
       MAXSCF             1000
       SCF_GUESS          sad
       GEN_SCFMAN         true
       GEN_SCFMAN_FINAL   true
       N_FROZEN_CORE      0      ! no frozen core
       N_FROZEN_VIRTUAL   0      ! no frozen virtual
       DO_O2              3      ! run OOMP2
       REGULARIZED_O2     2      ! use kappa-regularizer
       REG_VARIABLE       1450   ! set kappa = 1.45
       SCS                3      ! use arbitrary SCS
       SOS_FACTOR         883532 ! use cos = 0.883532
       SSS_FACTOR         883532 ! use css = 0.883532
       DO_S2              1      ! compute s^2 at the MP2 level
       UNRESTRICTED       true   ! use unrestricted
       GHF                true   ! use generalized
       COMPLEX            true   ! use complex
       INTEGRAL_SYMMETRY  false
    $end
    ```

???+ example "示例 6.15: 采用 R 轨道类型的 $\kappa$ -OOMP2 应用于水二聚体的示例"
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
       BASIS             cc-pvdz
       AUX_BASIS_CORR    rimp2-cc-pvdz
       EXCHANGE          hf
       THRESH            14
       INPUT_BOHR        true
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     gdm
       MAXSCF            1000
       SCF_GUESS         sad
       GEN_SCFMAN        true
       UNRESTRICTED      false  ! use restricted
       DO_O2             3      ! run OOMP2
       REGULARIZED_O2    2      ! use kappa-regularizer
       REG_VARIABLE      1450   ! set kappa = 1.45
       INTEGRAL_SYMMETRY false
    $end
    ```
