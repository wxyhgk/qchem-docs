---
title: "12.6.5 EDA2 的作业控制"
---

## 12.6.5 EDA2 的作业控制

(July 4, 2026)

将 FERF 模型用于极化能的评估，并对冻结（frozen）项作进一步分解，共同构成了 ALMO-EDA 方法的第二代。与此同时，在同一套代码结构下，原始的基于 AO 分块（AO-block）的 ALMO 模型以及其他相关方法也同样可用——例如冻结波函数的约束弛豫[[594]](../bib_references/bib.md#bib618)
（使冻结能以变分方式计算），以及 polMO 模型[[59]](../bib_references/bib.md#bib42)
（可以说给出了极化贡献的下限）。**Q-Chem** 中基于 GEN_SCFMAN（见第 [4.3](../ch04_scf/sec_SCF_job-control.md) 节）实现的这一整套方法被称为“EDA2”。
在 **Q-Chem** 5.2 及之后的版本中，当请求“JOBTYPE = EDA”时，“EDA2”被用作默认的 ALMO-EDA 驱动流程。

得益于开发者提供的一系列预设选项，EDA2 的作业控制被大大简化。预设编号通过 *$rem* 变量 EDA2
（下文介绍）来设定。除此之外，为了灵活性，用户也可以覆盖部分预设 *$rem*
变量的取值：

- •

与孤立碎片计算相关：

- **–**

EDA_CHILD_SUPER_BASIS：碎片计算使用超系统（super-system）基组（默认：FALSE）。
- **–**

FRAGMO_GUESS_MODE：如第 [12.3](sect_FRAGMOguess.md) 节所述（默认：0）。
- •

与 FRZ 项的分解相关：

- **–**

FRZ_ORTHO_DECOMP：在 *$rem* 区段中将其值设为 $-1$ 即可关闭该选项
（默认：TRUE）。
- **–**

FRZ_ORTHO_DECOMP_CONV：如第 [12.6.4](sect_frz_decomp.md) 节所述（默认：6）。
- **–**

EDA_CLS_DISP：如第 [12.6.4](sect_frz_decomp.md) 节所述（默认：FALSE）。
- **–**

DISP_FREE_X：如第 [12.6.4](sect_frz_decomp.md) 节所述（默认：HF）。
- **–**

DISP_FREE_C：如第 [12.6.4](sect_frz_decomp.md) 节所述（默认：NONE）。
- •

与 POL 的评估与分析相关：

- **–**

CHILD_MP_ORDERS：如第 [12.6.3](sect_ferf.md) 节所述（默认：232 (DQ)）。
- **–**

SCFMI_FREEZE_SS：如第 [12.6.2](sect_gen_scfmi.md) 节所述（默认：0）。
- **–**

EDA_POL_A：执行非微扰极化分析（默认：FALSE；见第 [12.6.8](sect_eda2_vcta.md) 节）。
- •

与 CT 和 BSSE 的评估相关：

- **–**

EDA_NO_CT：在 EDA 流程中跳过 CT 项的评估
（默认：FALSE
（当 SCFMI_FREEZE_SS = TRUE 时自动开启））。
- **–**

EDA_BSSE：使用_counterpoise_校正后的单体计算来评估 BSSE
（默认：FALSE）。
- **–**

EDA_PCT_A：开启微扰式（基于 Roothaan 步骤）电荷转移分析（默认：FALSE）。
- **–**

EDA_VCT_A：开启非微扰电荷转移分析（默认：FALSE；见第 [12.6.8](sect_eda2_vcta.md) 节）。
- **–**

EDA_COVP：对电荷转移执行 COVP 分析（默认：FALSE；见第 [12.5.3](sect_eda1.md) 节）。
- **–**

EDA_PRINT_COVP：将 COVP 输出到分子轨道系数文件中（默认：FALSE；见第 [12.5.3](sect_eda1.md) 节）。

注意：当 EDA_PRINT_COVP 大于 1 时，EDA2 可以为每对供体与受体碎片自动生成其主要占据-虚互补轨道（complementary occupied-virtual orbitals）的 cube 文件。
- •

其他选项：

- **–**

EDA2_PRINT_LEVEL：当设置为 $>1$ 时，为部分 EDA 项输出额外细节（*e.g.* 经溶剂化校正的 ELEC/PAULI）（默认：1）

EDA2

### `EDA2`

> **开启 EDA2 并指定预设选项编号。**
>
> * **类型**：`INTEGER`
> * **默认值**：`2`
> * **可选值**：
>     * 0
>     * 不通过 EDA2 运行。
>     * 1
>     * 冻结能分解 + nMDQ-uFERF 极化
>     * （标准 EDA2 选项）
>     * 2
>     * 冻结能分解 + （基于 AO 分块的）ALMO 极化
>     * （旧方案，并增加了冻结能分解）
>     * 3
>     * 冻结能分解 + oDQ-FERF 极化
>     * （非常用选项）
>     * 4
>     * 冻结波函数弛豫 + 冻结能分解 + nDQ-FERF 极化
>     * （非常用选项）
>     * 5
>     * 冻结能分解 + polMO 极化
>     * （非常用选项）。
>     * 10
>     * 无预设。完全由用户的
>     * $rem
>     * 输入控制
>     * （仅供开发者使用）
> * **建议**：对于 **Q-Chem** 的 ALMO-EDA 作业建议开启，除非希望使用旧方案做 CTA。一般而言推荐选项 1，尤其是在使用相当大的基组时。当所用基组为小型或中型（可以说不超过增广三重-$\zeta$）时，可以使用原始 ALMO 方案（选项 2）。其余选项在日常应用中很少使用。

请注意，从 **Q-Chem** v. 5.2 开始，若请求 JOBTYPE = EDA
而用户未在 *$rem* 中指定变量 EDA2，
则后者默认为 EDA2 = 2，且 EDA_PCT_A = TRUE。

对于基于 EDA2 的计算，默认的 SCF 收敛判据被设为 10${}^{-8}$
（而不是 **Q-Chem** 常规 SCF 计算中的 10${}^{-5}$）。所涉及的碎片计算会被强制使用与主作业相同的 SCF 收敛判据。

当自由基是单个原子（*e.g.* $\bullet$Cl）或具有高度对称的几何构型（*e.g.* $\bullet$OH）时，可能存在多重简并的电子组态——未成对电子位于不同的轨道上——从而导致冻结态的定义带有任意性。对于这类体系，人们希望找到使冻结态能量最低的碎片自旋取向。这可以通过采用“先极化后退极化”（polarize-then-depolarize, PtD）方法[[895]](../bib_references/bib.md#bib930)
来实现：利用碎片间极化来解除自由基电子态的简并——先对整个体系的极化（SCF-MI）计算收敛，
然后以 ALMO 系数矩阵中对应的分块作为初始猜测，重新计算每个孤立碎片的 SCF 解。
为保证“退极化”后的碎片与完全极化波函数中的电子组态一致，这些碎片计算采用初始最大重叠方法
（initial maximum overlap method, IMOM）[[75]](../bib_references/bib.md#bib59)
。由此得到的碎片轨道随后唯一地确定冻结波函数。

在 **Q-Chem** 5.2 及之后的版本中，上述流程在对非限制（unrestricted）ALMO-EDA 计算时默认执行。也可以通过将
EDA_ALIGN_FRGM_SPIN 设置为 $>0$ 的值来手工请求。注意，该设置还能确保在初始极化步骤中获得稳定的 SCF-MI 解（见下文），而这对于该方法的成功至关重要。偶尔可能会发现，由“自旋对齐”的碎片构造出的冻结态能量高于初始值。这说明碎片自旋对齐流程未能正常工作，此时我们建议用户通过将 FRZ_RELAX = $-1$ 来在不执行该流程的情况下运行 EDA2 计算。

在 **Q-Chem** 6.2.1 及更高版本中，用户还可以指定不适用 PtD 方案的碎片。这些碎片可以通过
*$skip_frgm_spin_align* 区段来指定（碎片索引从 1 开始）。例如，

> ```qchem
> $skip_frgm_spin_align
>  2
> $end
> ```

表示第 2 个碎片将跳过自旋对齐流程。通常，对于自由基与闭壳层分子之间的相互作用，只需对自由基施加自旋对齐即可。

EDA_ALIGN_FRGM_SPIN

### `EDA_ALIGN_FRGM_SPIN`

> **启用片段自旋对齐过程**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 不执行自旋对齐过程（在非限制（unrestricted）情况下默认开启此选项，即不对齐）
>     * 1
>     * 执行片段自旋对齐；在分子轨道最大化（MOM）计算之前的极化步骤中使用广义密度矩阵（GDM）方法
>     * 2
>     * 执行片段自旋对齐；在极化步骤中使用 GDM 并进行稳定性分析
> * **建议**: 当自由基具有高度对称的结构时，使用 1 或 2

对于涉及开壳层物种的体系，另一项有用的功能是可以对用户指定的片段执行稳定性分析（Stability Analysis），因为确保每个片段的自洽场（SCF）解的稳定性十分重要。这可以通过 *$frgm_stability* 输入段来实现：

> ```qchem
> $frgm_stability
>    [frgm_idx1]  [frgm_idx2]  ...
> $end
> ```

用户只需在其中列出需要执行稳定性分析的片段索引即可。

???+ example "示例 12.14: 氨-硼烷络合物的能量分解分析（Energy Decomposition Analysis, EDA）。此处 POL 项采用 FERF-nDQ 模型（因使用了非常大的基组），并对冻结相互作用能进行分解（默认采用 Hartree-Fock 作为 DFXC 泛函）。"
    ```qchem
    $molecule
       0 1
       --
       0 1
       N       0.000000     0.000000    -0.727325
       H       0.947371     0.000000    -1.091577
       H      -0.473685    -0.820448    -1.091577
       H      -0.473685     0.820448    -1.091577
       --
       0 1
       B       0.000000     0.000000     0.930725
       H      -1.165774     0.000000     1.243063
       H       0.582887    -1.009590     1.243063
       H       0.582887     1.009590     1.243063
    $end
    
    $rem
       JOBTYPE           eda
       EDA2              1
       METHOD            wB97M-V
       BASIS             def2-TZVPPD
       MEM_TOTAL         4000
       MEM_STATIC        1000
       THRESH            14
       SCF_CONVERGENCE   8
       XC_GRID           000099000590
       NL_GRID           1
       FD_MAT_VEC_PROD   false
       INTEGRAL_SYMMETRY false
    $end
    ```

???+ example "示例 12.15: 采用低成本模型化学方法对水二聚体进行能量分解分析。极化能的评估使用原始的定域分子轨道（Absolutely Localized Molecular Orbital, ALMO）模型，并选择 revPBE 作为 DFXC 泛函。同时对基组重叠误差（Basis Set Superposition Error, BSSE）应用 Counterpoise 校正。"
    ```qchem
    $molecule
    0 1
    --
    0 1
    H1
    O1 H1 0.95641
    H2 O1 0.96500  H1 104.77306
    --
    0 1
    O2 H2 dist     O1 171.85474 H1 180.000
    H3 O2 0.95822  H2 111.79807 O1 -58.587
    H4 O2 0.95822  H2 111.79807 O1 58.587
    
    dist = 2.0
    $end
    
    $rem
       JOBTYPE          eda
       EDA2             2
       METHOD           b97m-v
       BASIS            def2-svpd
       SCF_CONVERGENCE  8
       THRESH           14
       DISP_FREE_X      revPBE
       DISP_FREE_C      PBE
       EDA_BSSE         true
       INTEGRAL_SYMMETRY false
    $end
    ```

???+ example "示例 12.16: 对 H ${}_{2}$ O $\cdots$ Cl ${}^{\bullet}$ 络合物进行非限制（Unrestricted）EDA 计算。执行片段自旋对齐过程以保证冻结波函数的唯一性（EDA_ALIGN_FRGM_SPIN = 2）。"
    ```qchem
    $molecule
       0 2
       --
       0 2
       Cl         0.00127        0.00000       -0.88139
       --
       0 1
       O         -0.06700        0.00000        1.72173
       H          0.50943       -0.76061        1.83598
       H          0.50943        0.76061        1.83598
    $end
    
    $rem
       JOBTYPE               eda
       METHOD                m06-2x
       BASIS                 6-31+g(d)
       EDA2                  2
       UNRESTRICTED          true
       SCF_ALGORITHM         diis
       SCF_CONVERGENCE       8
       MAX_SCF_CYCLES        200
       THRESH                14
       EDA_BSSE              true
       EDA_ALIGN_FRGM_SPIN   2
       INTEGRAL_SYMMETRY     false
       POINT_GROUP_SYMMETRY  false
    $end
    ```
