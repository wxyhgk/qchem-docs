---
title: "10.11.2 NMR 化学位移与 J-耦合"
---

## 10.11.2 NMR 化学位移与 *J*-耦合

（2026 年 7 月 4 日）

NMR 计算可在 Hartree-Fock 和 DFT（密度泛函理论，Density Functional Theory）两个理论层次上进行。[[551]](../bib_references/bib.md#bib566)
**Q-Chem** 使用规范不变原子轨道（gauge-including atomic orbitals, GIAOs）[[334]](../bib_references/bib.md#bib338)
计算 NMR 化学屏蔽张量，该方法已被证明在许多应用中可靠且精确。[[550]](../bib_references/bib.md#bib564)

屏蔽张量 $\bm{\sigma}$ 是一个二阶性质，依赖于外磁场 $\mathbf{B}$ 以及给定核的自旋角动量 $\bm{m}$：

<a id="Ch10.E116"></a>
$$
\Delta E=-\bm{m}\bm{\cdot}(\mathbf{1}-\bm{\sigma})\bm{\cdot}\mathbf{B}\;. \tag{10.116}
$$

利用解析求导技术计算 $\bm{\sigma}$，该 $3\times 3$ 张量的各分量按如下方式计算：

<a id="Ch10.E117"></a>
$$
\sigma_{ij}=\sum_{\mu\nu}P_{\mu\nu}\left(\frac{\partial^{2}h_{\mu\nu}}{\partial B_{i}\partial m_{j}}\right)+\sum_{\mu\nu}\frac{\partial P_{\mu\nu}}{\partial B_{i}}\frac{\partial h_{\mu\nu}}{\partial m_{j}} \tag{10.117}
$$

其中 $i,j\in\{x,y,z\}$ 表示笛卡尔分量。注意，每个 $\bm{m}$（即每个核）都有一个独立的化学屏蔽张量。要计算 $\sigma_{ij}$，需求解耦合微扰自洽场（coupled-perturbed SCF, CPSCF）方程以获得微扰密度 $\partial P/\partial B_{i}$，这可以通过基于分子轨道（MO）的 "MOProp" 模块来实现，其用法将在下文说明。（使用 MOProp 模块计算分子光学性质的内容已在第 [10.10](sec_ElectricProps.md) 节中讨论。）此外，还提供了一种线性标度的、基于密度矩阵的 CPSCF（D-CPSCF）方法，[[1010]](../bib_references/bib.md#bib1054)
 相关说明见第 [10.11.3](sec_D-CPSCF-NMR.md) 节。

除化学位移外，间接核自旋-自旋耦合常数（亦称标量耦合或 $J$-耦合）也可在 SCF 层次上计算。原子 $A$ 与 $B$ 之间的耦合张量 $\mathbf{J}^{AB}$ 定义为电子能量对核磁矩 $\bm{m}$ 的二阶导数：

<a id="issc"></a>
$$
\mathbf{J}^{AB}=\frac{\partial^{2}E}{\partial\bm{m}_{A}\partial\bm{m}_{B}}\;. \tag{10.118}
$$

间接耦合张量包含五项不同的贡献。抗磁自旋-轨道（diamagnetic spin-orbit, DSO）贡献是用基态波函数计算的期望值。其余贡献为顺磁自旋-轨道（paramagnetic spin-orbit, PSO）、自旋-偶极（spin-dipole, SD）、费米接触（Fermi contact, FC）以及 SD/FC 混合贡献。这些项需要体系对外磁场（由磁性核产生的微扰）的电子响应。每个微扰核都需要求解十个不同的 CPSCF 方程，这使得 $J$-耦合常数的计算比化学位移更为耗时。

一些作者建议对 ${}^{1}$H–${}^{1}$H 耦合常数仅计算费米接触贡献，[[71]](../bib_references/bib.md#bib56)
 而忽略其他贡献。为此，**Q-Chem** 允许用户跳过四项贡献（FC、SD、PSO 或 DSO）中的任意一项。（只要同时计算 SD 和 FC 贡献，SD/FC 混合贡献就会自动计算，无需额外代价。）详见第 [10.10.3](moprop_jobcontrol.md) 节。注意，从理论上讲，省略任何一项贡献都是缺乏依据的。此类计算的结果应极其谨慎地解释。

**注意：

1.

在任何 $J$-耦合计算中，强烈推荐使用了专用的基组（Basis Set），例如 pcJ-$n$ 基组族。[[634]](../bib_references/bib.md#bib660)

2.

Hartree-Fock 理论层次*不适合*获得任何可靠程度的 $J$-耦合常数。请改用 GGA 或杂化密度泛函。

**

### 10.11.2.1 FD-NMR 作业控制与示例

**Q-Chem** 全新的 FD-NMR 功能通过对某个解析性质施加有限差分（finite differentiation）来计算 NMR 屏蔽张量，该解析性质可以是总能量（当 IDERIV = 0 时），也可以是逐原子的感应磁场（当 IDERIV = 1 时），即能量对核磁矩的一阶导数。基于 FD1 的屏蔽计算远比 FD2 高效，并且可在限制型（restricted）SCF 层次下使用（即最高支持到第 4 级 rung 的杂化/范围分离杂化泛函）。FD2 对某些 $O(N^{5})$ 相关方法（如（正则化）RI-MP2）也提供有限的支持。

???+ example "示例 10.55：在 RI-MP2/pcSseg-2 层次上对水分子进行基于 FD2 的 NMR 计算。"
    ```qchem
    $molecule
    0 1
    O          0.00000        0.00000        0.11779
    H          0.00000        0.75545       -0.47116
    H          0.00000       -0.75545       -0.47116
    $end
    
    $rem
    JOBTYPE             SP ! Required: zero-field job to prepare the initial guess for field-on job
    METHOD              HF
    SYM_IGNORE          1
    SYMMETRY            FALSE
    BASIS               pcSseg-2
    AUX_BASIS_J         RIJK-def2-TZVP
    AUX_BASIS_K         RIJK-def2-TZVP
    RI_J                TRUE
    RI_K                TRUE
    SCF_ALGORITHM       DIIS
    SCF_CONVERGENCE     10
    MAX_SCF_CYCLES      100
    NMR_SAVE            1 ! Required: zero-field job to prepare the initial guess for field-on job
    MEM_TOTAL           4000
    $end
    
    @@@
    
    $molecule
    READ
    $end
    
    $rem
    JOBTYPE             NMRSHIELD
    METHOD              RIMP2
    IDERIV              0 ! Required for FD2 logic
    SYM_IGNORE          1
    SYMMETRY            FALSE
    BASIS               pcSseg-2
    AUX_BASIS_J         RIJK-def2-TZVP
    AUX_BASIS_K         RIJK-def2-TZVP
    AUX_BASIS_CORR      RIMP2-def2-TZVP
    RI_J                TRUE
    RI_K                TRUE
    SCF_ALGORITHM       DIIS
    SCF_CONVERGENCE     10
    DO_FINITE_B_OR_M    1
    FDIFF_STEPSIZE_B    100 ! B field finite Difference step size in 1E-5 A.U.
    TENSOR_DIAG_ONLY    TRUE ! Calculates diagonal elements only
    COMPLEX             TRUE ! Required
    USE_LIBQINTS        TRUE ! Required
    MEM_TOTAL           4000
    $end
    
    $shielding ! select atom for shielding computation, index starts from 0
    0 1 2
    $end
    
    ```

???+ example "示例 10.56：在 HF/pcSseg-3 层次上对苯分子进行基于 FD1 的 NMR 计算。"
    ```qchem
    $molecule
    0 1
    H         -8.15907        2.62281        1.60092
    C         -8.66658        2.57679        0.63197
    C        -10.05547        2.62953        0.57123
    H        -10.64089        2.71700        1.49206
    C        -10.70043        2.57096       -0.65988
    H        -11.79336        2.61234       -0.70769
    C         -9.95678        2.45974       -1.83037
    H        -10.46440        2.41365       -2.79910
    C         -8.56799        2.40692       -1.76952
    H         -7.98287        2.31923       -2.69053
    C         -7.92294        2.46549       -0.53841
    H         -6.83011        2.42401       -0.49049
    $end
    
    $rem
    JOBTYPE             SP ! Required: zero-field job to prepare the initial guess for field-on job
    METHOD              HF
    SYM_IGNORE          1
    SYMMETRY            FALSE
    BASIS               pcSseg-3
    AUX_BASIS_J         RIJK-def2-QZVP
    AUX_BASIS_K         RIJK-def2-QZVP
    RI_J                TRUE
    OCC_RI_K            TRUE
    SCF_ALGORITHM       DIIS
    SCF_CONVERGENCE     10
    NMR_SAVE            1 ! Required: zero-field job to prepare the initial guess for field-on job
    MEM_TOTAL           8000
    $end
    
    @@@
    
    $molecule
    READ
    $end
    
    $rem
    JOBTYPE             NMRSHIELD
    METHOD              HF
    IDERIV              1 ! Required for FD1 logic
    SYM_IGNORE          1
    SYMMETRY            FALSE
    BASIS               pcSseg-3
    AUX_BASIS_J         RIJK-def2-QZVP
    AUX_BASIS_K         RIJK-def2-QZVP
    RI_J                TRUE
    OCC_RI_K            TRUE
    SCF_ALGORITHM       DIIS
    SCF_CONVERGENCE     10
    DO_FINITE_B_OR_M    1
    FDIFF_STEPSIZE_B    100 ! B field finite Difference step size in 1E-5 A.U.
    COMPLEX             TRUE
    USE_LIBQINTS        TRUE ! Required
    NMR_FORWARD_DIFF    TRUE ! Calculates NMR properties with forward difference instead of central difference
    MEM_TOTAL           8000
    $end
    
    ```

### 10.11.2.2 NMR 作业控制与示例

本节介绍 **Q-Chem** 基于 MO 的 CPSCF 代码的使用方法，该代码包含在 "MOProp" 模块中，该模块同时负责计算电学性质。通过设置 MOPROP = 1 来请求计算 NMR 化学位移，通过设置 JOBTYPE = ISSC 来计算 $J$-耦合。关于与 MOProp 模块相关的更多作业控制变量，以及下面示例中所用变量的说明，请参见第 [10.10.3](moprop_jobcontrol.md) 节。此外，还提供另一种 ${\cal{O}}({N})$ 标度、基于密度矩阵的 NMR 化学位移实现，详见第 [10.11.3](sec_D-CPSCF-NMR.md) 节。注意，设置 JOBTYPE = NMR 调用的是基于密度的代码，而非基于 MO 的代码。

???+ example "示例 10.57：基于 MO 的 NMR 计算。"
    ```qchem
    $molecule
    0  1
      H        0.00000        0.00000        0.00000
      C        1.10000        0.00000        0.00000
      F        1.52324        1.22917        0.00000
      F        1.52324       -0.61459        1.06450
      F        1.52324       -0.61459       -1.06450
    $end
    
    $rem
      METHOD             B3LYP
      BASIS              6-31G*
      MOPROP               1
      MOPROP_PERTNUM       0  ! do all perturbations at once
      MOPROP_CONV_1ST      7  ! sets the CPSCF convergence threshold
      MOPROP_DIIS_DIM_SS   4  ! no. of DIIS subspace vectors
      MOPROP_MAXITER_1ST 100  ! max iterations
      MOPROP_DIIS          5  ! turns on DIIS (=0 to turn off)
      MOPROP_DIIS_THRESH   1
      MOPROP_DIIS_SAVE     0
    $end
    ```

在下面的复合作业中，我们演示当 NMR 计算超出最大 CPSCF 迭代次数（由 MOPROP_MAXITER_1ST 指定）时，或者在共享计算资源上因超时而中断时，如何重启计算。注意，第一个作业是*故意*设置为超出最大迭代次数的，因此会崩溃；但计算在第二个作业中被重启并完成。

???+ example "示例 10.58：演示如何重启 NMR 计算。在第一个作业中，我们故意将最大迭代次数设得过小，以强制计算提前结束，从而可以在第二个作业中展示重启功能。"
    ```qchem
    $molecule
    0  1
      H        0.00000        0.00000        0.00000
      C        1.10000        0.00000        0.00000
      F        1.52324        1.22917        0.00000
      F        1.52324       -0.61459        1.06450
      F        1.52324       -0.61459       -1.06450
    $end
    
    $rem
       METHOD               B3LYP
       BASIS                6-31G*
       SCF_ALGORITHM        DIIS
       MOPROP               1
       MOPROP_MAXITER_1ST   10   ! too small, for demonstration only
       GUESS_PX             1
       MOPROP_DIIS_SAVE     0   ! don’t hang onto the subspace vectors
    $end
    
    @@@
    
    $molecule
    0  1
      H        0.00000        0.00000        0.00000
      C        1.10000        0.00000        0.00000
      F        1.52324        1.22917        0.00000
      F        1.52324       -0.61459        1.06450
      F        1.52324       -0.61459       -1.06450
    $end
    
    $rem
       METHOD               B3LYP
       BASIS                6-31G*
       SCF_GUESS            READ
       SKIP_SCFMAN          TRUE   ! no need to redo the SCF
       MOPROP               1
       MOPROP_RESTART       1
       MOPROP_MAXITER_1ST   100  ! more reasonable choice
       GUESS_PX             1
       MOPROP_DIIS_SAVE     0
    $end
    ```

???+ example "示例 10.59：$J$-耦合计算：使用 B3LYP/cc-pVDZ 的水分子"
    ```qchem
    $molecule
       0 1
       O
       H1 O OH
       H2 O OH H1 HOH
    
       OH  = 0.947
       HOH = 105.5
    $end
    
    $rem
       JOBTYPE           ISSC
       EXCHANGE          B3LYP
       BASIS             cc-pVDZ
       LIN_K             FALSE
       MOPROP_CONV_1ST   6
       INTEGRAL_SYMMETRY TRUE
    $end
    ```

如果只关心某些特定原子对之间的自旋-自旋耦合，可以限制计算耦合的原子对。选择通过 *$spin-spin* 输入段完成，其原子索引从零开始。例如，下面的输入段

> ```qchem
> $spin-spin
> 0 1 5
> $end
> ```

将计算 *$molecule* 段中第一个、第二个和第六个原子之间所有可能配对的耦合：(1, 2)、(1, 6) 和 (2, 6)。若未指定 *$spin-spin* 段，则将计算 *$molecule* 中所有原子对之间的耦合。

### 10.11.2.3 核独立化学位移：芳香性的探针

对芳香性程度的明确理论估计仍有迫切需求。NMR 化学位移方法提供了一种独特的芳香性探针，其依据是芳香体系的一个定义性特征：其维持同向环电流（diatropic ring current）的能力。这使得体系对外加磁场产生响应，在环中心处表现出强（负）屏蔽。Von Schleyer *et al.* 利用这一现象提出了一种新的独特芳香性探针。[[1383]](../bib_references/bib.md#bib1468)
 他们提议将环中心处计算得到的绝对磁屏蔽（重原子环坐标的未加权平均）作为一种新的芳香性判据，称为核独立化学位移（nucleus-independent chemical shift, NICS）。芳香环在环中心处表现出强负屏蔽（负 NICS），而反芳香体系在环中心处则呈现正 NICS。例如，用 **Q-Chem** 在 Hartree-Fock/6-31G* 层次上估算的苯典型 NICS 值约为 $-11.5$ ppm。参考文献 [[1383]](../bib_references/bib.md#bib1468)
 中也报道了相同的苯 NICS 值。**Q-Chem** 计算得到的呋喃 NICS 值为 $-13.9$ ppm，与参考文献 [[1383]](../bib_references/bib.md#bib1468)
 中报道的呋喃数值基本一致。下面给出一个使用 **Q-Chem**（借助鬼原子（ghost atom）选项）计算呋喃 NICS 的输入示例。鬼原子置于呋喃环的中心，并且在基组混合（basis mix）选项中为其指定的基组必须是用于氢原子的基组。

???+ example "示例 10.60：计算呋喃的 NMR NICS 探针，HF/6-31G* 层次。注意置于环中心的鬼原子。"
    ```qchem
    $molecule
       0 1
       C    -0.69480       -0.62270       -0.00550
       C     0.72110       -0.63490        0.00300
       C     1.11490        0.68300        0.00750
       O     0.03140        1.50200        0.00230
       C    -1.06600        0.70180       -0.00560
       H     2.07530        1.17930        0.01410
       H     1.37470       -1.49560        0.00550
       H    -1.36310       -1.47200       -0.01090
       H    -2.01770        1.21450       -0.01040
       @H    0.02132        0.32584        0.00034
    $end
    
    $rem
       JOBTYPE               NMR
       METHOD                HF
       BASIS                 6-31G*
       PURCAR                111
       SCF_CONVERGENCE       7
       NO_REORIENT           1
       POINT_GROUP_SYMMETRY  FALSE
    $end
    ```
