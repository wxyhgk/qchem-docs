---
title: "10.2.4 有效未成对电子布居数"
---

## 10.2.4 有效未成对电子布居数

(July 4, 2026)

在拉伸的氢分子中，平衡时配对形成共价键的两个电子变为未配对，并定域在各自的 H 原子上。在单线态双自由基（singlet diradicals）或双线态三自由基（doublet triradicals）中，这种弱配对即使在平衡几何下也存在。在单行列式自洽场（Self-Consistent Field, SCF）理论层面，像 H${}_{2}$ 这样的单线态体系的价电子始终保持完美配对，需要引入非动态关联（non-dynamical correlation）才能解偶键合电子对，从而产生有效未成对（"odd"，自由基化）电子的布居。[[1339]](../bib_references/bib.md#bib1573)

当静态关联（static correlation）较强时，这些电子基本保持未配对状态，可以被描述为定域在单个原子上。

这些现象可以在波函数形式体系中得到了恰当描述。在密度泛函理论（Density Functional Theory, DFT）中，这些效应可以通过破缺对称性（broken-symmetry）方法或使用自旋翻转含时 DFT（SF-TDDFT）来描述（参见第 [7.3.1](../ch07_excited/sect_tddftintro.md) 节）。下面我们将介绍如何在不依赖自旋污染解的情况下，从这类低自旋开壳层体系的纯 DFT 描述中导出此类信息。

对应于单行列式波函数（*e.g.*，SCF 或 Kohn-Sham DFT）的一阶约化密度矩阵（first-order reduced density matrix, 1-RDM）是幂等的：

<a id="A3.S8.EGx73"></a>
$$
\displaystyle\begin{aligned} \displaystyle\rho_{\sigma}({\mathbf{r}_{1}})&\displaystyle=\int\gamma_{\sigma}^{\text{SCF}}(1;2)\;\gamma_{\sigma}^{\text{SCF}}(2;1)\,d{\mathbf{r}_{2}}\\
\displaystyle\gamma_{\sigma}^{\text{SCF}}(1;2)&\displaystyle=\sum_{i}^{\text{occ}}\psi_{i\sigma}^{\mathrm{KS}}(1)\psi_{i\sigma}^{\mathrm{KS}}(2)\;,\end{aligned} \tag{10.9}
$$

其中 $\rho_{\sigma}(1)$ 是位置 $\mathbf{r}_{1}$ 处自旋为 $\sigma$ 的电子密度，$\gamma_{\sigma}^{\text{SCF}}$ 是单个 Slater 行列式的自旋分辨 1-RDM。交叉乘积
$\gamma_{\sigma}^{\text{SCF}}(1;2)\;\gamma_{\sigma}^{\text{SCF}}(2;1)$
反映了由 HF 交换空穴（exchange hole）所决定的 Hartree-Fock 交换（或 Kohn-Sham 精确交换）：

<a id="A3.S8.EGx74"></a>
$$
\displaystyle\begin{aligned} \displaystyle\gamma_{\sigma}^{\text{SCF}}(1;2)\;\gamma_{\sigma}^{\text{SCF}}(2;1)&\displaystyle=\rho_{\alpha}(1)h_{\mathrm{X}\sigma\sigma}(1,2)\\
\displaystyle\int{h}_{{\text{X}}\sigma\sigma}(1,2)\>d{\bf r}_{2}&\displaystyle=1\;.\end{aligned} \tag{10.10}
$$

当 1-RDM 包含电子关联时，它将变得非幂等：

<a id="eq:non-idempotent1"></a>
$$
D_{\sigma}(1)\equiv{\rho}_{\sigma}(1)-\int\gamma_{\sigma}(1;2)\gamma_{\sigma}(2;1)\>d{\mathbf{r}_{2}}\geq 0\,. \tag{10.11}
$$

函数 $D_{\sigma}(1)$ 度量了关联 1-RDM 偏离幂等性的程度，并给出在点 ${\mathbf{r}_{1}}$ 处自旋为 $\sigma$ 的有效未成对（odd）电子密度。[[1339]](../bib_references/bib.md#bib1573)

因此，单线态体系中有效未成对电子的产生纯粹是一种基于关联的现象。将 $D_{\sigma}(1)$ 对自旋分量求和即得 odd 电子的总密度，再将其对空间积分即得 odd 电子的平均总数 $\bar{N}_{u}$：

<a id="eq:total-odds"></a>
$$
D_{u}(1)=2\sum_{\sigma}D_{\sigma}(1)d{\mathbf{r}_{1}},\,\,{\bar{N}}_{u}=\int D_{u}(1)d{\mathbf{r}_{1}}\,. \tag{10.12}
$$

上式 Eq. ([10.12](#eq:total-odds)) 中出现因子 2 的原因，可参阅 Ref. [[1132]](../bib_references/bib.md#bib1172) 中的讨论。在 Kohn-Sham DFT 中，SCF 1-RDM 始终是幂等的，这阻碍了在该理论层面对 odd 电子形成的分析。Ref. [[1129]](../bib_references/bib.md#bib1180) 针对这一情况提出了一种补救方案。人们注意到，进入 Eq. ([10.11](#eq:non-idempotent1)) 的关联 1-RDM 交叉乘积反映的是一种有效交换（effective exchange），亦称累积量交换（cumulant exchange）。[[135]](../bib_references/bib.md#bib125)
 KS 精确交换空穴本身人为地过于离域。然而，在具有强左右（*i.e.*，静态）关联的有限体系中，总交换-关联相互作用通常相当定域，大致局限于约原子尺寸的区域内。[[100]](../bib_references/bib.md#bib82)
 用关联 1-RDM 交叉乘积描述的有效交换也应当是相当定域的。基于这一考虑，文献提出了如下形式的关联 1-RDM 交叉乘积：[[1129]](../bib_references/bib.md#bib1180)

<a id="eq:b05-3"></a>
$$
\gamma_{\sigma}(1;2)\;\gamma_{\sigma}(2;1)=\rho_{\sigma}(1)\;\bar{h}_{\text{X}\sigma\sigma}^{\text{eff}}(1,2)\;. \tag{10.13}
$$

函数 $\bar{h}_{{\text{X}}\sigma\sigma}^{\text{eff}}(1;2)$ 是 Becke-Roussel (BR) 形式的模型 DFT 交换空穴，用于 Becke 的 B05 方法。[[101]](../bib_references/bib.md#bib85)
 后者用某种有效交换-关联空穴来描述左右静态关联效应。[[101]](../bib_references/bib.md#bib85)
 仅靠 HF 交换空穴所带来的额外离域，可由某些具有物理依据的实空间修正来补偿：[[101]](../bib_references/bib.md#bib85)

<a id="eq:B05-ND-XChole"></a>
$$
\bar{h}_{{\text{XC}}\alpha\alpha}(1,2)=\bar{h}_{{\text{X}}\alpha\alpha}^{\text{eff}}(1,2)+f_{{\mathrm{c}}}(1)\;\bar{h}_{{\text{X}}\beta\beta}^{\text{eff}}(1,2)\;. \tag{10.14}
$$

BR 交换空穴 $\bar{h}_{{\text{X}}\sigma\sigma}^{\text{eff}}$ 在 B05 中用作辅助函数，使得弛豫后的 BR 空穴所产生的势与精确交换空穴的势相等。这导致辅助 BR 空穴的弛豫归一化（relaxed normalization）小于或等于 1：

<a id="eq:BR-auxiliary"></a>
$$
\int\bar{h}_{{\text{X}}\sigma\sigma}^{\text{eff}}(1;2)\;d\mathbf{r}_{2}=N_{X\sigma}^{\text{eff}}(1)\;\leq 1\,. \tag{10.15}
$$

弛豫归一化 $N_{\text{X}\sigma}^{\text{eff}}(\mathbf{r})$ 的表达式相当复杂，但可以将其写成闭合解析形式。[[1131]](../bib_references/bib.md#bib1177)
 弛豫归一化 $N_{X\alpha}^{\mathrm{eff}}(1)$ 越小，对应的精确交换空穴就越离域。[[101]](../bib_references/bib.md#bib85)
 $\alpha\!-\!\alpha$ 交换空穴会被 $\beta\!-\!\beta$ 交换空穴的一部分
$f_{{\mathrm{c}}}(1)\,{\bar{h}}_{{\mathrm{X}}\beta\beta}^{\mathrm{eff}}(1,2)$
进一步加深，由此产生左右静态关联。Eq. ([10.14](#eq:B05-ND-XChole)) 中的局域关联因子 $f_{\mathrm{c}}$ 主导这种加深程度，从而决定每一点上静态关联的强度：[[101]](../bib_references/bib.md#bib85)

<a id="eq:f-factor1"></a>
$$
f_{\text{c}}(\mathbf{r})=\min\bigl{(}f_{\alpha}(\mathbf{r}),~{}f_{\beta}(\mathbf{r}),~{}1\bigr{)} \tag{10.16a}
$$

利用 Eq. ([10.16](#eq:f-factor1))、([10.12](#eq:total-odds)) 和 ([10.13](#eq:b05-3))，odd 电子密度可写为：

<a id="A3.S8.EGx75"></a>
$$
\displaystyle\begin{aligned} \displaystyle D_{\alpha}(1)&\displaystyle=\rho_{\alpha}(1)(1-N_{X\alpha}^{\text{eff}}(1))\\
&\displaystyle=\rho_{\alpha}(1)f_{\mathrm{c}}(1)\,N_{X\beta}^{\text{eff}}(1)\;.\end{aligned} \tag{10.17}
$$

自旋求和后的 odd 电子密度以及 odd 电子平均总数的最终公式为：

<a id="A3.S8.EGx76"></a>
$$
\displaystyle\begin{aligned} \displaystyle D_{u}(1)&\displaystyle=4a_{\text{nd}}^{\text{op}}\;f_{\text{c}}(1)\left[{\rho}_{\alpha}(1)\,N_{X\beta}^{\mathrm{eff}}(1)+{\rho}_{\beta}(1)\,N_{X\alpha}^{\mathrm{eff}}(1)\right]\\
\displaystyle\bar{N}_{u}&\displaystyle=\int D_{u}(\mathbf{r_{1}})\;d\mathbf{r_{1}}\;.\end{aligned} \tag{10.18}
$$

这里 $a_{\text{c}}^{\text{nd-opp}}=0.526$ 是 B05 泛函中反自旋静态关联能项的 SCF 优化线性系数。[[101]](../bib_references/bib.md#bib85)

将 odd 电子平均总数分解为原子贡献是很有信息量的。将 odd 电子平均总数 $\bar{N}_{u}$ 在实空间中按原子贡献进行划分，我们得到 odd 电子的原子布居（$F_{A}^{\text{r}}$）：

<a id="eq:b05-12"></a>
$$
F_{A}^{\mathrm{r}}=\int_{\Omega_{A}}D_{u}(\mathbf{r_{1}})\,d{\mathbf{r}_{1}}\,. \tag{10.19}
$$

这里 $\Omega_{A}$ 是体系中分配给原子 $A$ 的子区域。为了以简单的方式定义这些原子区域，我们采用 Becke 网格积分方案中将网格空间划分为原子子群的划分方法。[[94]](../bib_references/bib.md#bib73)
 由于本方法不需要对称性破缺，即使在键长强烈拉伸的情况下，单线态态也以限制型 Kohn-Sham（Restricted Kohn-Sham, RKS）方式进行计算。这样可以避免自旋污染对 $F_{A}^{\text{r}}$ 以及 Kohn-Sham 轨道的破坏性影响。$F_{A}^{\text{r}}$ 的计算只有在 RI-B05 和 RI-mB05 泛函下才能完全自洽地进行。在这些情况下无需特殊关键字，只需在 *$rem* 段中选择相应的 EXCHANGE 即可。使用任何其他泛函时，也可分两步估算 odd 电子的原子布居：首先用所选泛函完成一次收敛的 SCF 计算，然后使用 RI-B05 或 RI-mB05 泛函、从前一次计算读取猜测（guess），执行单次 post-SCF 迭代，如下面的输入示例所示：

???+ example "示例 10.10.2: 计算拉伸 H ${}_{2}$ 中 odd 电子的原子布居数与关联键级，分别使用 B3LYP/RI-mB05（post-SCF）以及完全 SCF 的 RI-mB05"
    ```qchem
    $comment
       Stretched H2: example of B3LYP calculation of the atomic population of odd electrons
       with post-SCF RI-BM05 extra iteration.
    $end
    
    $molecule
       0 1
       H   0.  0.   0.0
       H   0.  0.   1.5000
    $end
    
    $rem
       SCF_GUESS         CORE
       METHOD            B3LYP
       BASIS             G3LARGE
       PURECART          222
       THRESH            14
       MAX_SCF_CYCLES    80
       PRINT_INPUT       TRUE
       SCF_FINAL_PRINT   1
       INCDFT            FALSE
       XC_GRID           000128000302
       SCF_CONVERGENCE   9
       POINT_GROUP_SYMMETRY FALSE
       INTEGRAL_SYMMETRY    FALSE
    $end
    
    @@@
    
    $comment
       Now one RI-B05 extra-iteration after B3LYP to generate the odd-electron atomic
       population and the correlated bond order.
    $end
    
    $molecule
       read
    $end
    
    $rem
       SCF_GUESS         READ
       EXCHANGE          BM05
       PURECART          22222
       BASIS             G3LARGE
       AUX_BASIS         riB05-cc-pvtz
       THRESH            14
       PRINT_INPUT       TRUE
       INCDFT            FALSE
       XC_GRID           000128000302
       MAX_SCF_CYCLES    0
       SCF_CONVERGENCE   9
       DFT_CUTOFFS       0
       POINT_GROUP_SYMMETRY FALSE
       INTEGRAL_SYMMETRY    FALSE
    $end
    
    @@@
    
    $comment
       Finally, a fully SCF run RI-B05 using the previous output as a guess.
       The following input lines are obligatory here:
       PURECART     22222
       AUX_BASIS    riB05-cc-pvtz
       DFT_CUTOFFS  0
    $end
    
    $molecule
       read
    $end
    
    $rem
       SCF_GUESS        READ
       EXCHANGE         BM05
       PURECART         22222
       BASIS            G3LARGE
       AUX_BASIS        riB05-cc-pvtz
       THRESH           14
       PRINT_INPUT      TRUE
       INCDFT           FALSE
       IPRINT           3
       XC_GRID          000128000302
       SCF_FINAL_PRINT  1
       MAX_SCF_CYCLES   80
       SCF_CONVERGENCE  8
       DFT_CUTOFFS      0
       POINT_GROUP_SYMMETRY FALSE
       INTEGRAL_SYMMETRY    FALSE
    $end
    ```

一旦获得 odd 电子的原子布居，程序代码中会随之计算对应的 Mayer 型关联键级（correlated bond order），利用 $F_{A}^{\mathrm{r}}$、$F_{B}^{\mathrm{r}}$ 与 Mayer 型关联键级 $B_{AB}$ 之间的某些精确关系。这两个新性质会在输出末尾、多极矩（multipoles）部分之后打印出来。将关联键级与 Mayer 型 SCF 键级进行比较是很有用的。若要打印后者，请使用 SCF_FINAL_PRINT = 1。
