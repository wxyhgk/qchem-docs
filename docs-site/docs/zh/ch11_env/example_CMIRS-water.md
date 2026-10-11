---
title: "11.2.7 溶剂隐式表示组合法（CMIRS）"
---

## 11.2.7 溶剂隐式表示组合法（Composite Method for Implicit Representation of Solvent, CMIRS）

（2026 年 7 月 4 日）

PCM（极化连续介质模型）即便像 SS(V)PE 和 IEF-PCM 这样精细的模型，也只考虑了长程的溶质–溶剂相互作用，而一个精确的溶剂化自由能模型还必须包含对短程非静电相互作用的处理。各种模型以不同的方式分解这些相互作用，但非静电项通常试图模拟以下全部或大部分内容：溶质–溶剂色散（van der Waals）相互作用、溶质与溶剂之间的 Pauli（交换）排斥、在介电介质中形成溶质空腔所需的功（即所谓的"空腔化能"）、氢键以及由溶剂分子结构引起的其他特异性相互作用，以及在引入溶质后纯溶剂结构（从而熵）的变化。

Pomogaeva 和
Chipman[[1108]](../bib_references/bib.md#bib1155)
 提出了一种隐式溶剂化模型，试图在采用 PCM 方式处理整体静电作用的同时，对这些非静电相互作用进行建模。他们将这一方法称为"溶剂隐式表示组合法"（CMIRS），其第一步是采用 SS(V)PE 模型（第 [11.2.6](subsec_SS(V)PE.md) 节）对溶质–连续介质静电作用进行自洽处理。CMIRS 在该静电计算的基础上，加入了一个参照非局域 VV09 van der Waals 色散密度泛函建模的溶质–溶剂色散项[[1414]](../bib_references/bib.md#bib1475)、
一个依赖于延伸至溶质空腔之外的溶质电子密度尾部区域的 Pauli 排斥贡献，以及一个基于溶质在空腔表面所产生的电场法向分量的极大值与极小值的氢键校正项。溶剂化 Gibbs 自由能由此被建模为

<a id="eq:CMIRS-free-energy"></a>
$$
\begin{split}\displaystyle\Delta G_{\textrm{CMIRS}}(\rho_{s})=&\displaystyle\Delta G_{\textrm{SS(V)PE}}(\rho_{s})+\Delta G_{\textrm{DEFESR}}(\rho_{s})\;,\end{split} \tag{11.22}
$$

其中 $\Delta G_{\textrm{SS(V)PE}}$ 是来自 SS(V)PE 模型的连续介质静电贡献，该模型基于以溶质电荷密度的等值面 $\rho_{s}$ 定义的溶质空腔。第二项包含短程色散、交换以及"场极值短程"（DEFESR）相互作用：

<a id="eq:DEFESR-free-energy"></a>
$$
\begin{split}\displaystyle\Delta G_{\textrm{DEFESR}}=&\displaystyle\Delta G_{\textrm{disp}}+\Delta G_{\textrm{exch}}+\Delta G_{\textrm{FESR}}\;.\end{split} \tag{11.23}
$$

这些项只计算一次，使用的是 SS(V)PE 计算中已收敛的溶质电荷密度。

CMIRS 方法由 Zhi-Qiang You 和 John Herbert 在 **Q-Chem** 中实现[[1527]](../bib_references/bib.md#bib1594)
。在此工作过程中，他们发现 Pomogaeva 和 Chipman 在 **gamess** 程序中对 $\Delta G_{\textrm{disp}}$ 的原始实现存在一处严重错误。尽管对修正后的模型重新参数化后，在一个大型实验溶剂化自由能数据库上的整体误差统计只有微小变化，但式 ([11.23](#eq:DEFESR-free-energy)) 中各能量分量的分配却发生了显著变化[[1527]](../bib_references/bib.md#bib1594)
。应 Dan Chipman 的要求，**Q-Chem** 中的实现被称为"CMIRS v. 1.1"，而 v. 1.0 专指 Pomogaeva 和 Chipman 最初的 **gamess** 实现。

CMIRS 模型对每一种目标溶剂独立参数化，但每种溶剂使用的经验参数不超过五个。目前在 **Q-Chem** 中已支持水、乙腈、二甲基亚砜、苯和环己烷。$\Delta G$ 的误差统计与第 [11.2.9](ex_SMx-User-Solvent.md) 节所述的 SM$x$ 模型相比非常有优势，*例如*，在苯和环己烷中的平均绝对误差 $<0.7$ kcal/mol，在水中的平均绝对误差 $<1.5$ kcal/mol。后一项统计包含了具有挑战性的离子型溶质；而电荷中性水溶液溶质的误差还要更小[[1527]](../bib_references/bib.md#bib1594)
。

| 溶剂 | SolvRho | A | B | C | D | Gamma |
| --- | --- | --- | --- | --- | --- | --- |
| 苯 | $0.0421$ | $-0.00522$ | $0.01294$ |  |  |  |
| 环己烷 | $0.0396$ | $-0.00938$ | $0.03184$ |  |  |  |
| DMSO | $0.05279$ | $-0.00951$ | $0.044791$ |  | $-162.07$ | $4.1$ |
| $\rm CH_{3}CN$ | $0.03764$ | $-0.008178$ | $0.045278$ |  | $-0.33914$ | $1.3$ |
| 水 | $0.05$ | $-0.006736$ | $0.032698$ | $-1249.6$ | $-21.405$ | $3.7$ |

表 11.5： 使用 **RHOISO** = 0.0010 a.u. 优化得到的 CMIRS 参数（取自文献 [[1527]](../bib_references/bib.md#bib1594)
），对于离子，质子参考 $\Delta G$ 值取自文献 [[679]](../bib_references/bib.md#bib703)
。

| 溶剂 | SolvRho | A | B | C | D | Gamma |
| --- | --- | --- | --- | --- | --- | --- |
| 苯 | $0.0421$ | $-0.00572$ | $0.01116$ |  |  |  |
| 环己烷 | $0.0396$ | $-0.00721$ | $0.05618$ |  |  |  |
| DMSO | $0.05279$ | $-0.002523$ | $0.011757$ |  | $-817.93$ | $4.3$ |
| $\rm CH_{3}CN$ | $0.03764$ | $-0.003805$ | $0.03223$ |  | $-0.44492$ | $1.2$ |
| 水 | $0.05$ | $-0.006496$ | $0.050833$ | $-566.7$ | $-30.503$ | $3.2$ |

表 11.6： 使用 **RHOISO** = 0.0005 a.u. 优化得到的 CMIRS 参数（取自文献 [[1527]](../bib_references/bib.md#bib1594)
），对于离子，质子参考 $\Delta G$ 值取自文献 [[679]](../bib_references/bib.md#bib703)
。

**Q-Chem** 中 CMIRS 的当前实现使用 Chipman 的等密度 SS(V)PE 模块计算静电能。所得的等密度空腔和溶质电荷密度随后用于计算 DEFESR 相互作用。要请求 CMIRS 计算，用户必须在等密度 SS(V)PE 计算中将 IDEFESR 设为 1（见第 [11.2.6.2](subsec_SS(V)PE.md#subsec:SVP) 节）。CMIRS 模型中依赖于溶剂的经验参数 **A**、**B**、**C**、**D**、**Gamma** 需要在 *$pcm_nonels* 段中指定。此外还需要三个附加参数。其一是色散方程中的阻尼参数 **Delta**。我们建议将该参数固定为 $\delta=7$ a.u.（约 3.7 Å），这是一个优化值，只考虑分子间距离大于 van der Waals 接触距离时的色散作用。其二是溶剂的平均电子密度 **SolvRho**。最后是交换方程中对溶剂区域进行积分时所用 Gauss–Laguerre 点的数目 **GauLag_N**。我们建议使用 $40$ 个网格点以兼顾积分效率与精度。对于两种不同的 $\rho_{s}$ 值，所支持溶剂的优化参数列于表 [11.5](#table:CMIRS-params-rho0010) 和 [11.6](#table:CMIRS-params-rho0005)[[1527]](../bib_references/bib.md#bib1594)
。

???+ example "示例 11.15：甲烷在水溶剂中的 CMIRS 计算。"
    ```qchem
    $molecule
       0  1
       C     0.000000     0.000005     0.000000
       H     0.748558     0.801458     0.000000
       H     0.506094    -0.972902     0.000000
       H    -0.627326     0.085706     0.895425
       H    -0.627326     0.085706    -0.895425
    $end
    
    $rem
       EXCHANGE        = b3lyp5
       BASIS           = 6-31+g*
       SCF_CONVERGENCE = 8
       MEM_TOTAL       = 4000
       MEM_STATIC      = 400
    point_group_symmetry = False
       XC_GRID         = 000096000974
    $end
    
    @@@
    
    $rem
       EXCHANGE        = b3lyp5
       BASIS           = 6-31+g*
       SCF_CONVERGENCE = 8
       MAX_SCF_CYCLES  = 100
       SOLVENT_METHOD  = isosvp
       SCF_GUESS       = read
       MEM_TOTAL       = 4000
       MEM_STATIC      = 400
       SVP_MEMORY      = 1000
    point_group_symmetry = False
       XC_GRID         = 000096000974
    $end
    
    $molecule
       read
    $end
    
    $svp
       RHOISO=0.001, DIELST=78.36, NPTLEB=974,ITRNGR=2, IROTGR=2, IPNRF=1, IDEFESR=1
    $end
    
    $pcm_nonels
       A         -0.006736
       B          0.032698
       C      -1249.6
       D        -21.405
       Delta    7.0
       Gamma    3.7
       SolvRho  0.05
       GauLag_N 40
    $end
    ```
