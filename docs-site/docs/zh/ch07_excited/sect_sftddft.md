---
title: "7.3.4 自旋翻转 TDDFT"
---

## 7.3.4 自旋翻转 TDDFT（Spin-Flip TDDFT）

（2026 年 7 月 4 日）

自旋翻转（spin-flip, SF）方法提供了一条在单参考（single-reference）框架内描述某些棘手的多组态（multi-configurational）态的途径。[[726]](../bib_references/bib.md#bib757)

SF 特别适用于可以用两电子两轨道 [(2e,2o)] 或 (3e,3o) 描述的态。其基本思想是将这类目标态描述为从高自旋参考行列式（三重态或四重态）出发的自旋翻转激发（例如 $\alpha\rightarrow\beta$）。SF 处理既可以与不同的关联处理方法相结合（例如 EOM-CC、ADC、CI、RAS-CI）[[205]](../bib_references/bib.md#bib207)，也可以与密度泛函理论（Density Functional Theory, DFT）相结合。[[1239]](../bib_references/bib.md#bib1294)

SF-TDDFT 既可以描述基态，也可以描述若干低激发态。它可用于描述双自由基（diradical）、三自由基（triradical）、单分子磁体、HOMO-LUMO 能隙较小的体系，在某些情况下还可用于描述键断裂过程和锥形交叉（conical intersection）。[[205]](../bib_references/bib.md#bib207)

执行 SF-DFT 计算时，需要为参考态选择适当的多重度（multiplicity），并将 SPIN_FLIP 设为 1（常规 SF-TDDFT）或 2（MRSF-TDDFT）。SF-DFT 仅在 Tamm-Dancoff 近似（Tamm-Dancoff approximation, TDA）下使用（必须将 RPA 设为 FALSE）。

最初的 SF-DFT 采用共线（collinear）核（kernel）构建，要求使用含有较高比例 Hartree–Fock 交换的泛函。使用含约 $50$% Hartree–Fock 交换比例的泛函可获得最佳结果，[[1239]](../bib_references/bib.md#bib1294)

这一行为已从理论层面得到解释。[[603]](../bib_references/bib.md#bib626)

Becke 的"半半"泛函 BH&HLYP 已成为使用标准 SF-TDDFT 时的事实上的标准方法。

由 Ziegler 及其合作者最早提出的、采用非共线（non-collinear）交换关联势的 SF-TDDFT 方法也已在程序中实现。[[1424]](../bib_references/bib.md#bib1486)[[114]](../bib_references/bib.md#bib101)

这一非共线版本在激发能方面有时优于共线 SF-TDDFT，但其分母中含有自旋密度因子（$\rho_{\alpha}-\rho_{\beta}$），有时会导致稳定性问题。

SF-DFT 态可能存在自旋污染（spin-contamination）问题。该问题可以通过使用自旋适配（spin-adapted）版本的 SF-TDDFT（第 [7.2.3.3](Ch7.S2.SS3.md#safs-sftddft) 节）[[1549]](../bib_references/bib.md#bib1615)

来解决，也可以通过使用下文所述的混合参考（mixed-reference）SF-TDDFT 公式来解决。

所有 SF-TDDFT 变体均可计算永久偶极矩和跃迁偶极矩。自旋-轨道耦合（spin-orbit coupling, SOC）和波函数分析（自然轨道占据数转变 NTO 及激子描述符）可用于 SF-TDDFT 的标准共线与非共线公式以及 MR-SF-TDDFT。解析梯度与非绝热耦合（non-adiabatic coupling, NAC）可用于非自旋适配的共线及非共线 SF-TDDFT 公式。

以下示例展示了 **Q-Chem** 中 SF-DFT 的功能：[7.3.4.2](#ex:MRSFDFT)、[7.2.3.3](Ch7.S2.SS3.md#safs-sftddft)、
[7.3.10.1](Ch7.S3.SS10.md#ex:dftcis-soc)、[7.3.4.2](#ex:MRSFDFT)、
[9.8.4](../ch09_opt/sfdft_MECP1.md) 以及 [7.3.4.2](#ex:MRSFDFT)。
其他相关方法包括
SF-XCIS（第 [7.2.3.2](Ch7.S2.SS3.md#topic:sf) 节）、自旋适配 SF-CIS（第 [7.2.3.3](Ch7.S2.SS3.md#safs-sftddft) 节）、
EOM-SF-CC（第 [7.9.6](sec_EOMSF.md) 节）、SF-ADC（第 [7.10.8](sect_SF-ADC.md) 节），
以及 SF-RASCI（第 [7.11](topic_rasi.md) 节）。

## 7.3.4.1 混合参考 SF-TDDFT

在 MRSF-TDDFT 中，[[781]](../bib_references/bib.md#bib824)

参考态构造为两个 Kohn–Sham 行列式的等权混合，分别对应三重态的 $M_{S}=+1$ 和 $M_{S}=-1$ 分量。由此得到的混合参考约化密度矩阵（reduced density matrix, RDM）定义为

<a id="Ch7.E27"></a>

$$
\rho_{0}^{\rm MR}=\frac{1}{2}(\rho_{0}^{M_{S}=+1}+\rho_{0}^{M_{S}=-1}) \tag{7.27}
$$

它是非幂等的（non-idempotent），但通过对单占据自旋轨道进行复数变换可恢复幂等性。[[781]](../bib_references/bib.md#bib824)

通过将来自 $M_{S}=+1$ 分量的 $\alpha\rightarrow\beta$ 自旋翻转激发与来自 $M_{S}=-1$ 分量的 $\beta\rightarrow\alpha$ 激发耦合起来，MRSF-SF-TDDFT 恢复了常规 SF-TDDFT 中缺失的大部分行列式，从而恢复了自旋完备性（spin-completeness）。

MRSF-TDDFT 的当前实现

可用于 ROHF 参考（UNRESTRICTED = FALSE），能够同时描述单重态和三重态。它还可以计算跃迁性质，包括偶极矩与角动量算符的矩阵元、SOC 以及波函数分析。
MRSF-TDDFT 采用共线交换关联核，因此推荐使用杂化泛函，尤其是 Hartree–Fock 交换比例较高的杂化泛函。

轨道 Hessian 矩阵定义为[[793]](../bib_references/bib.md#bib828)

<a id="Ch7.E28"></a>

$$
A_{pq,rs}^{(k)}=A_{pq,rs}^{(k)(0)}+A_{pq,rs}^{{}^{\prime}(k)} \tag{7.28}
$$

其中 $k\in\{\text{S},\text{T}\}$ 表示单重态或三重态，且

<a id="Ch7.E29"></a>

$$
A_{pq,rs}^{(k)(0)}=U_{pq}^{k}\{\delta_{pr}F_{qs}^{\beta}-\delta_{qs}F_{pr}^{\alpha}-c_{H}(pr|sq)\}U_{rs}^{(k)}. \tag{7.29}
$$

项 $A_{pq,rs}^{{}^{\prime}(k)}$ 处理由两个三重态分量生成的行列式之间的耦合，其表达式为

<a id="A3.S8.EGx40"></a>

$$
\displaystyle\begin{aligned} \displaystyle A_{pq,rs}^{{}^{\prime}(k)}&\displaystyle=H_{p\underline{q},r\underline{s}}^{(k){\rm intra}}(U_{pq}^{\text{CO1}}-U_{pq}^{\text{CO2}})(U_{rs}^{\text{CO1}}-U_{rs}^{\text{CO2}})\\
&\displaystyle\qquad+H_{\underline{p}q,\underline{r}s}^{(k){\rm intra}}(U_{pq}^{\text{O1V}}-U_{pq}^{\text{O2V}})(U_{rs}^{\text{O1V}}-U_{rs}^{\text{O2V}})\\
&\displaystyle\qquad+H_{pq,rs}^{(k){\rm inter}}(U_{pq}^{\text{CO1}}U_{rs}^{\text{O2V}}+U_{pq}^{\text{CO2}}U_{rs}^{\text{O1V}}+U_{pq}^{O1V}U_{rs}^{\text{CO2}}+U_{pq}^{\text{O2V}}U_{rs}^{\text{CO1}})\;.\end{aligned} \tag{7.30}
$$

这里，$U_{pq}$ 是维度变换矩阵，且

<a id="Ch7.E31"></a>

$$
\displaystyle H_{pq,rs}^{(k)\text{intra}} \tag{7.31a}
$$

其中

<a id="Ch7.E32"></a>

$$
\text{sgn}(k)=\begin{cases}+1,&\text{if}~{}k=\text{S}\\
-1,&\text{if}~{}k=\text{T}\\
\end{cases} \tag{7.32}
$$

以及

<a id="Ch7.E33"></a>

$$
\underline{p}=\begin{cases}\text{O2},&\text{if}~{}p=\text{O1}\\
\text{O1},&\text{if}~{}p=\text{O2}\\
\end{cases} \tag{7.33}
$$

维度变换矩阵确保在 $k=\text{S}$ 和 $k=\text{T}$ 两种情况下，MRSF 激发子空间的维数都与 SF-TDDFT 空间的维数相匹配。得益于这种单重态空间与三重态空间完全解耦的结构，MRSF-TDDFT 与最初的 SF-TDDFT 不同，它分别求解单重态和三重态流形的本征值问题。

默认情况下，计算会为每个态打印 $\langle\hat{S}^{2}\rangle$ 值、TDDFT 振幅，以及相对于每个自旋流形中最低 SF 态的跃迁偶极矩。

启用关键词 STS_MOM=TRUE 可打印额外信息，包括每个计算态的永久偶极矩的笛卡尔分量（以原子单位 a.u. 计）、各态之间跃迁偶极矩的笛卡尔分量（以 a.u. 计），以及所有计算 SF 态之间相应的振子强度。若要计算 SOC，请使用 CALC_SOC=2。

示例 [7.3.4.2](#ex:MRSFDFT) 演示了丁二烯（butadiene）的 MR-SF-TDDFT 计算，包括态性质、跃迁性质和激子分析。

## 7.3.4.2 示例

???+ example "示例 7.8：使用推荐的 50-50 泛函对 TMM 双自由基最低 6 个态进行 SF-TDDFT 单点能计算。"
    ```qchem
    $molecule
       0 3
       C
       C  1  CC1
       C  1  CC2   2  A2
       C  1  CC2   2  A2     3  180.0
       H  2  C2H   1  C2CH   3    0.0
       H  2  C2H   1  C2CH   4    0.0
       H  3  C3Hu  1  C3CHu  2    0.0
       H  3  C3Hd  1  C3CHd  4    0.0
       H  4  C3Hu  1  C3CHu  2    0.0
       H  4  C3Hd  1  C3CHd  3    0.0
    
       CC1    = 1.35
       CC2    = 1.47
       C2H    = 1.083
       C3Hu   = 1.08
       C3Hd   = 1.08
       C2CH   = 121.2
       C3CHu  = 120.3
       C3CHd  = 121.3
       A2    = 121.0
    $end
    
    $rem
       EXCHANGE          gen
       BASIS             6-31G*
       SCF_GUESS         core
       SCF_CONVERGENCE   10
       MAX_SCF_CYCLES    100
       SPIN_FLIP         1
       CIS_N_ROOTS       6
       CIS_CONVERGENCE   10
       MAX_CIS_CYCLES    100
    $end
    
    $xc_functional
       X  HF    0.50
       X  S     0.08
       X  B     0.42
       C  VWN   0.19
       C  LYP   0.81
    $end
    ```

???+ example "示例 7.9：采用非共线交换关联泛函的 SF-TDDFT 计算 $\rm CH_{2}$ 的低激发态。"
    ```qchem
    $comment
      Non-collinear SF-DFT calculation for CH2 at 3B1 state geometry from
      EOM-CCSD(fT) calculation
    $end
    
    $molecule
       0 3
       C
       H  1 rCH
       H  1 rCH  2 HCH
    
       rCH = 1.0775
       HCH = 133.29
    $end
    
    $rem
       EXCHANGE             PBE0
       BASIS                cc-pVTZ
       SPIN_FLIP            1
       WANG_ZIEGLER_KERNEL  TRUE
       SCF_CONVERGENCE      10
       CIS_N_ROOTS          6
       CIS_CONVERGENCE      10
    $end
    ```

???+ example "示例 7.10：使用共线 B5050LYP 对 $p$-苯炔（p-benzyne）进行 SF-TDDFT 计算，并由 libwfa 执行波函数分析（自然轨道与 NTO）。"
    ```qchem
    $comment
    Para-benzyne diradical
    Equilibrium singlet state geom from:
    J. Chem. Phys. 136, 204103 (2012)
    Enu = 187.2138176166 hartree
    $end
    
    $molecule
       0 3
       H   2.145810  -1.225292   0.000000
       C   1.201382  -0.709285   0.000000
       C   1.201382   0.709285   0.000000
       H   2.145810   1.225292   0.000000
       C   0.000000   1.335664   0.000000
       C  -1.201382   0.709285   0.000000
       H  -2.145810   1.225291   0.000000
       C  -1.201382  -0.709285   0.000000
       H  -2.145810  -1.225291   0.000000
       C   0.000000  -1.335664   0.000000
    $end
    
    $rem
       METHOD          = b5050lyp
       BASIS           = 6-31G*
       CIS_N_ROOTS     = 4
       SPIN_FLIP       = true
       NEW_DFT         = true
       STATE_ANALYSIS  = true
       WFA_REF_STATE   = 1
       MOLDEN_FORMAT   = true
       NTO_PAIRS       = 4
    $end
    ```

???+ example "示例 7.11：包含激子分析的丁二烯混合参考 SF-TDDFT/BHHLYP 计算。"
    ```qchem
    $comment
    - Singlet states of butadiene using MRSF-TDDFT
    - State-to-state transition dipole moments, and oscillator strengths
    - Density matrix based analysis of the calculated MRSF states
    $end
    
    $molecule
    0 3
    C   -0.410990219   -1.798958603   0.000000000
    C   -0.559475119   -0.470573512   0.000000000
    C    0.410990219    1.798958603   0.000000000
    C    0.559475119    0.470573512   0.000000000
    H   -1.263114858   -2.463113554   0.000000000
    H    0.571968115   -2.252448386   0.000000000
    H    1.263114858    2.463113554   0.000000000
    H   -1.554995711   -0.040726039   0.000000000
    H   -0.571968115    2.252448386   0.000000000
    H    1.554995711    0.040726039   0.000000000
    $end
    
    $rem
    jobtype            SP
    unrestricted       FALSE
    basis              6-31G*
    exchange           bhhlyp
    correlation        none
    scf_guess          core
    SCF_CONVERGENCE    10
    SCF_ALGORITHM      DIIS
    MAX_SCF_CYCLES     100
    PRINT_ORBITALS     false   ! do not print orbitals
    SPIN_FLIP          2       ! keyword to perform MRSF-TDDFT calculation
    CIS_N_ROOTS        4       ! 4 MRSF states requested
    CIS_SINGLETS       TRUE    ! asking for singlet states
    CIS_TRIPLETS       FALSE
    CIS_CONVERGENCE    8
    MAX_CIS_CYCLES     100
    STS_MOM            TRUE    ! calculate state-to-state transition moments
    STATE_ANALYSIS     TRUE    ! density matrix based analysis of MRSF states
    NTO_PAIRS          2       ! write 2 NTO pairs per excited states
    $end
    ```
