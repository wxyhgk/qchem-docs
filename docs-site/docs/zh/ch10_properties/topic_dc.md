---
title: "10.15.2 基于绝热态（Diabatic-State-Based）的方法"
---

## 10.15.2 基于绝热态（Diabatic-State-Based）的方法

（2026 年 7 月 4 日）

## 10.15.2.1 电荷转移中的电子耦合

电荷转移涉及一对分子片段中电子数目的变化。作为示例，必要时我们将使用如下反应，将其推广到其他情形是直接的：

<a id="eq:electron-transfer"></a>

$$
\mathrm{D}^{-}\mathrm{A}\longrightarrow\mathrm{D}\mathrm{A}^{-} \tag{10.177}
$$

其中额外的电子初始定域在给体（donor，D）上，而在终态中它定域在受体（acceptor，A）上。初态与终电子态的两态久期方程（secular equation）可写为

<a id="eq:2by2HS"></a>

$$
{\bf H}-E{\bf S}=\left(\begin{array}[]{cc}H_{\mathrm{ii}}-S_{\mathrm{ii}}E&H_{\mathrm{if}}-S_{\mathrm{if}}E\\
H_{\mathrm{if}}-S_{\mathrm{if}}E&H_{\mathrm{ff}}-S_{\mathrm{ff}}E\end{array}\right)=0 \tag{10.178}
$$

除初态与终态之间的非正交性之外，这非常接近一个本征值问题。利用 Löwdin 变换可以得到式 ([10.178](#eq:2by2HS)) 的标准本征值形式：

<a id="Ch10.E179"></a>

$$
\mathbf{H}_{\textrm{eff}}=\mathbf{S}^{-1/2}\mathbf{H}\mathbf{S}^{-1/2}, \tag{10.179}
$$

其中有效哈密顿矩阵的非对角元表示该反应的*电子耦合（electronic coupling）*，其定义为

<a id="eq:coupling-normal"></a>

$$
V=H^{\textrm{eff}}_{\mathrm{if}}=\frac{H_{\mathrm{if}}-S_{\mathrm{if}}(H_{\mathrm{ii}}+H_{\mathrm{ff}})/2}{1-S^{2}_{\mathrm{if}}} \tag{10.180}
$$

在初态与终态未归一化的一般情形下，电子耦合写作

<a id="eq:coupling"></a>

$$
V=\sqrt{S_{\mathrm{ii}}S_{\mathrm{ff}}}\times\frac{H_{\mathrm{if}}-S_{\mathrm{if}}(H_{\mathrm{ii}}/S_{\mathrm{ii}}+H_{\mathrm{ff}}/S_{\mathrm{ff}})/2}{S_{\mathrm{ii}}S_{\mathrm{ff}}-S^{2}_{\mathrm{if}}} \tag{10.181}
$$

因此，原则上在计算出哈密顿 $H$ 与重叠矩阵 $S$ 的矩阵元之后即可获得 $V$。

直接耦合（direct coupling，DC）方案通过式 ([10.181](#eq:coupling)) 计算电子耦合值，并被广泛用于电荷转移耦合的计算。[[1014]](../bib_references/bib.md#bib1056)
 在 DC 方案中，耦合矩阵元是使用电荷定域的行列式（电子转移文献中的“绝热态”，diabatic states）直接计算的。在电子转移体系中已表明，这类电荷定域态可以由对称性破缺的非限制性 Hartree-Fock（UHF）解来近似。[[1014]](../bib_references/bib.md#bib1056)
 在 DC 计算中，假定绝热本征态是两个对称性破缺 UHF 解的对称与反对称线性组合。因此，DC 耦合可以看作两构型（two-configuration）求解的结果，该求解或许能够恢复非动态（non-dynamical）关联。

DC 方法的核心基于相应的轨道变换（corresponding orbital transformation）[[689]](../bib_references/bib.md#bib715)
 以及对 Slater 行列式在 $H_{\mathrm{if}}$ 和 $S_{\mathrm{if}}$ 中的计算。[[376]](../bib_references/bib.md#bib381)
 遗憾的是，对于密度泛函理论（Density Functional Theory, DFT）方法无法计算 $H_{\mathrm{if}}$，因为两个密度 $\rho_{\mathrm{i}}$ 与 $\rho\mathrm{f}$ 的泛函形式未知，且不存在 $H_{\mathrm{if}}$ 的已有近似形式。[[1502]](../bib_references/bib.md#bib1560)

为了用 DFT 计算电荷转移耦合，我们可以使用 CDFT-CI 方法（第 [5.11.5](../ch05_dft/sect_CDFT-CI.md) 节）、前线分子轨道（frontier molecular orbital，FMO）方法（第 [10.15.2.5](#subsubsect:FMO-DC) 节）[[1384]](../bib_references/bib.md#bib1456)
，或者混合方案，即使用 CDFT 波函数的 DC（第 [10.15.2.4](#subsubsect:DC) 节）。

## 10.15.2.2 相应的轨道变换

设 $|\Psi_{a}\rangle$ 与 $|\Psi_{b}\rangle$ 为初态和终态的两个单 Slater 行列式波函数，$\mathbf{a}$ 与 $\mathbf{b}$ 分别为其自旋轨道集合：

<a id="A3.S8.EGx91"></a>

$$
\displaystyle\mathbf{a} \tag{10.182}
$$

由于两组自旋轨道不正交，可以定义重叠矩阵 $\mathbf{S}$：

<a id="Ch10.E184"></a>

$$
\mathbf{S}=\int\mathbf{b}^{\dagger}\mathbf{a}\ d\tau. \tag{10.184}
$$

需要注意的是，由于初态与终态的分子轨道是分别独立确定的，$\mathbf{S}$ 一般来说不是厄米矩阵。为计算矩阵元 $H_{ab}$ 与 $S_{ab}$，可通过相应的轨道变换[[689]](../bib_references/bib.md#bib715)
 使用两组新的正交自旋轨道。在此方法中，每组自旋轨道 $\mathbf{a}$ 与 $\mathbf{b}$ 进行线性变换，

<a id="A3.S8.EGx92"></a>

$$
\displaystyle\hat{\mathbf{a}} \tag{10.185}
$$

其中 $\mathbf{V}$ 与 $\mathbf{U}$ 分别是 $\mathbf{S}$ 的奇异值分解（singular value decomposition，SVD）中的左奇异矩阵与右奇异矩阵：

<a id="Ch10.E187"></a>

$$
\mathbf{S}=\mathbf{U}\hat{\mathbf{s}}\mathbf{V}^{\dagger} \tag{10.187}
$$

新基下的重叠矩阵此时为对角矩阵

<a id="Ch10.E188"></a>

$$
\int\hat{\mathbf{b}}^{\dagger}\hat{\mathbf{a}}=\mathbf{U}^{\dagger}\left(\int\mathbf{b}^{\dagger}\mathbf{a}\right)\mathbf{V}=\hat{\mathbf{s}} \tag{10.188}
$$

## 10.15.2.3 广义密度矩阵

分子中电子的哈密顿量是一电子算符与二电子算符之和。下面推导一电子与二电子算符的表达式

<a id="Ch10.E189"></a>

$$
\displaystyle\Omega^{(1)} \tag{10.189a}
$$

其中

<a id="Ch10.E190"></a>

$$
\displaystyle\omega(i) \tag{10.190a}
$$

于是哈密顿的矩阵元可表示为 $H_{ab}=\Omega^{(1)}_{ab}+\Omega^{(2)}_{ab}$，其中

<a id="Ch10.E191"></a>

$$
\Omega^{(1)}_{ab}=\langle\Psi_{b}|\Omega^{(1)}|\Psi_{a}\rangle=\det(\mathbf{U})\det(\mathbf{V}^{\dagger})\sum^{N}_{i=1}\langle\hat{b}_{i}|\omega(1)|\hat{a}_{i}\rangle\prod^{N}_{j\neq i}\hat{s}_{jj} \tag{10.191}
$$

以及

<a id="eq:2par"></a>

$$
\Omega^{(2)}_{ab}=\langle\Psi_{b}|\Omega^{(2)}|\Psi_{a}\rangle=\frac{1}{2}\det(\mathbf{U})\det(\mathbf{V}^{\dagger})\sum^{N}_{ij}\langle\hat{b}_{i}\hat{b}_{j}|\omega(1,2)(1-P_{12})|\hat{a}_{i}\hat{a}_{j}\rangle\prod^{N}_{k\neq{i,j}}\hat{s}_{kk}\;. \tag{10.192}
$$

重叠积分为

<a id="eq:1par"></a>

$$
S_{ab}=\langle\Psi_{b}|\Psi_{a}\rangle=\det(\mathbf{U})\det(\mathbf{V}^{\dagger})\prod_{i=1}^{N}\hat{s}_{ii}\;. \tag{10.193}
$$

在原子轨道基组（atomic orbital basis set）$\{\chi\}$ 中，我们可以将分子自旋轨道 $\mathbf{a}$ 与 $\mathbf{b}$ 展开，

<a id="A3.S8.EGx95"></a>

$$
\displaystyle\mathbf{a}=\chi\mathbf{A},\qquad\hat{\mathbf{a}}=\chi\mathbf{A}\mathbf{V}=\chi\hat{\mathbf{A}} \tag{10.194}
$$

一电子项，即式 ([10.193](#eq:1par))，可以表示为

<a id="A3.S8.EGx96"></a>

$$
\displaystyle\Omega^{(1)}_{ab} \tag{10.196}
$$

其中 $\displaystyle T_{ii}=S_{ab}/\hat{s}_{ii}$，并定义广义密度矩阵（generalized density matrix）$\mathbf{G}$：

<a id="eq:g-density"></a>

$$
\mathbf{G}=\hat{\mathbf{A}}\mathbf{T}\hat{\mathbf{B}}^{\dagger}\;. \tag{10.197}
$$

类似地，二电子项，即式 ([10.192](#eq:2par))，为

<a id="A3.S8.EGx97"></a>

$$
\displaystyle\begin{aligned} \displaystyle\Omega^{(2)}_{ab}&\displaystyle=\frac{1}{2}\sum_{ij}\sum_{\lambda\sigma}\sum_{\mu\nu}\hat{A}_{\lambda i}\hat{A}_{\sigma j}\left(\frac{1}{\hat{s}_{ii}}\right)T_{jj}\hat{B}^{\dagger}_{i\mu}\hat{B}^{\dagger}_{j\nu}\langle\chi_{\mu}\chi_{\nu}|\omega(1,2)|\chi_{\lambda}\chi_{\sigma}\rangle\\
&\displaystyle=\sum_{\lambda\sigma\mu\nu}G^{\text{L}}_{\lambda\mu}G^{\text{R}}_{\sigma\nu}\langle\mu\nu||\lambda\sigma\rangle\end{aligned} \tag{10.198}
$$

其中 $\mathbf{G}^{\text{R}}$ 与 $\mathbf{G}^{\text{L}}$ 是如式 ([10.197](#eq:g-density)) 所定义的广义密度矩阵，只是 $\mathbf{G}^{\text{L}}$ 中的 $T_{ii}$ 被替换为 $1/(2s_{ii})$。

$\alpha$ 自旋与 $\beta$ 自旋轨道被显式处理。用空间轨道表示时，一电子与二电子贡献可化简为

<a id="eq:1par-g-ab"></a>

$$
\Omega^{(1)}_{ab}=\sum_{\lambda\sigma}G^{\alpha}_{\lambda\sigma}\omega_{\sigma\lambda}+\sum_{\lambda\sigma}G^{\beta}_{\lambda\sigma}\omega_{\sigma\lambda} \tag{10.199}
$$

<a id="A3.S8.EGx98"></a>

$$
\displaystyle\begin{aligned} \displaystyle\Omega^{(2)}_{ab}&\displaystyle=\sum_{\lambda\sigma\mu\nu}G^{\text{L}\alpha}_{\lambda\mu}G^{\text{R}\alpha}_{\sigma\nu}(\langle\mu\nu|\lambda\sigma\rangle-\langle\mu\nu|\sigma\lambda\rangle)+\sum_{\lambda\sigma\mu\nu}G^{\text{L}\beta}_{\lambda\mu}G^{\text{R}\alpha}_{\sigma\nu}\langle\mu\nu|\lambda\sigma\rangle\\
&\displaystyle\qquad+\sum_{\lambda\sigma\mu\nu}G^{\text{L}\alpha}_{\lambda\mu}G^{\text{R}\beta}_{\sigma\nu}\langle\mu\nu|\lambda\sigma\rangle+\sum_{\lambda\sigma\mu\nu}G^{\text{L}\beta}_{\lambda\mu}G^{\text{R}\beta}_{\sigma\nu}(\langle\mu\nu|\lambda\sigma\rangle-\langle\mu\nu|\sigma\lambda\rangle)\end{aligned} \tag{10.200}
$$

所得的一电子与二电子贡献，即式 ([10.199](#eq:1par-g-ab)) 与式 ([10.200](#eq:2par-g-ab))，可以很方便地借助广义密度矩阵，使用 **Q-Chem** 中标准的一电子与二电子积分程序计算得到。

## 10.15.2.4 用于电子耦合的直接耦合方法

对 DC 方案而言，获得合适的电荷定域初态与终态十分重要，这一步骤决定了耦合值的质量。**Q-Chem** 提供三种构造电荷定域态的途径：

- •

**“1+1”方法

**由于体系由给体与受体分子或片段组成，且电荷定域在给体或受体上，因此将各个给体片段与受体片段的波函数组合成电荷定域波函数是直观的做法。我们称此方法为“1+1”，因为零级波函数由两个片段的 Hartree-Fock（HF）波函数构成。

例如，对于式 ([10.177](#eq:electron-transfer)) 所示的情形，我们可以用 **Q-Chem** 计算两个 HF 波函数：阴离子给体与中性受体的波函数，二者共同构成初态。对于终态，则使用中性给体与阴离子受体的波函数。随后通过式 ([10.181](#eq:coupling)) 计算耦合值。

???+ example "示例 10.74：使用“1+1”电荷定域态计算乙烯二聚体的电子转移耦合"
    ```qchem
    $molecule
      -1  2
    --
      -1  2,  0  1
       C    0.662489    0.000000    0.000000
       H    1.227637    0.917083    0.000000
       H    1.227637   -0.917083    0.000000
       C   -0.662489    0.000000    0.000000
       H   -1.227637   -0.917083    0.000000
       H   -1.227637    0.917083    0.000000
    --
       0  1, -1  2
       C    0.720595    0.000000    4.5
       H    1.288664    0.921368    4.5
       H    1.288664   -0.921368    4.5
       C   -0.720595    0.000000    4.5
       H   -1.288664   -0.921368    4.5
       H   -1.288664    0.921368    4.5
    $end
    
    $rem
       METHOD               HF
       BASIS                6-31G(d)
       SCF_PRINT_FRGM       FALSE
       SCF_GUESS            FRAGMO
       STS_DC               TRUE
       POINT_GROUP_SYMMETRY FALSE
    $end
    ```

在 *$molecule* 小节中，第一行给出整个体系的电荷与多重度。随后的各块是两个分子片段（给体与受体）的输入。在每一块中，第一行依次给出对应片段在初态中的电荷与自旋多重度、一个逗号，然后是终态中的电荷与多重度。接下来的行是该片段的核种类及其位置。例如在上述示例中，第一块表示电子给体初始为双重态的乙烯阴离子，在终态中变为单重态的中性粒子。第二块对应另一个乙烯，从单重态中性分子变为双重态阴离子。

请注意，本例中最后三个 *$rem* 变量 POINT_GROUP_SYMMETRY、SCF_GUESS 与 STS_DC 必须设置为示例中所示的取值，才能使用“1+1”电荷定域态执行 DC 计算。此外还包含一个额外的 *$rem* 变量 SCF_PRINT_FRGM。当它设为 TRUE 时，会给出片段 HF 自洽场（self-consistent field，SCF）计算的详细输出。
- •

**“弛豫”（relaxed）方法

**在“1+1”方法中，初态与终态忽略了分子间相互作用，因此最终的电子耦合可能被低估。作为第二种方法，**Q-Chem** 可以使用“1+1”波函数作为初始猜测，通过进一步的 HF 自洽场计算来寻找电荷定域波函数。此方法会“弛豫”由“1+1”方法构造的波函数，并在初态与终态波函数中纳入分子间相互作用效应。然而，该方法有时会失败，导致收敛问题，或得到一个无法表示所需电荷定域态的 HF 波函数。当使用扩散性基函数进行计算，或给体与受体分子彼此非常接近时，更有可能出现此问题。

要执行弛豫 DC 计算，设置 STS_DC = RELAX。
- •

**混合方案：约束 DFT 电荷定域态

**约束 DFT（constrained DFT，CDFT）（第 [5.11](../ch05_dft/topic_cdft.md) 节）可用于获得电荷定域态。建议同时设置电荷约束与自旋约束，以产生正确的电荷定域。要用 CDFT 态执行 DC 计算，在批作业（batch job）的前两个作业中设置 SAVE_SUBSYSTEM = 10 与 SAVE_SUBSYSTEM = 20 以保存 CDFT 分子轨道，然后在批作业的第三个作业中设置 SCF_GUESS = READ 与 STS_DC = TRUE 来计算电子耦合值。

???+ example "示例 10.10.75：使用 CDFT 电荷定域态计算乙烯二聚体的电子转移耦合"
    ```qchem
    $molecule
     -1  2
     C  0.662489  0.000000  0.000000
     H  1.227637  0.917083  0.000000
     H  1.227637 -0.917083  0.000000
     C -0.662489  0.000000  0.000000
     H -1.227637 -0.917083  0.000000
     H -1.227637  0.917083  0.000000
     C  0.720595  0.000000  4.500000
     H  1.288664  0.921368  4.500000
     H  1.288664 -0.921368  4.500000
     C -0.720595  0.000000  4.500000
     H -1.288664 -0.921368  4.500000
     H -1.288664  0.921368  4.500000
    $end
    
    $rem
       METHOD          =  wb97xd
       BASIS           =  cc-pvdz
       CDFT            =  true
       SAVE_SUBSYSTEM  =  10
       POINT_GROUP_SYMMETRY = False
    $end
    
    $cdft
     1.0
     1.0  1 6
     1.0
     1.0  1 6  s
    $end
    
    @@@
    
    $molecule
     read
    $end
    
    $rem
       METHOD          =  wb97xd
       BASIS           =  cc-pvdz
       CDFT            =  true
    point_group_symmetry = False
       SAVE_SUBSYSTEM  =  20
    $end
    
    $cdft
     1.0
     1.0  7 12
     1.0
     1.0  7 12  s
    $end
    
    @@@
    
    $molecule
     read
    $end
    
    $rem
       METHOD      =  hf
       BASIS       =  cc-pvdz
    point_group_symmetry = False
       SCF_GUESS   =  read
       STS_DC      =  true
    $end
    ```

## 10.15.2.5 前线分子轨道方法

前线分子轨道（FMO）方法常与 DFT 一起用于计算电子转移（electron transfer，ET）耦合。[[1384]](../bib_references/bib.md#bib1456)
 FMO 耦合值本质上是一个考虑了重叠的 Kohn-Sham 矩阵非对角元，

<a id="eq:coupling-FMO"></a>

$$
V^{\mathrm{FMO}}=\frac{f_{\mathrm{DA}}-S\left(f_{\mathrm{DD}}+f_{\mathrm{AA}}\right)/2}{1-S^{2}} \tag{10.201}
$$

其中 $f_{\mathrm{DA}}=\langle\phi^{\mathrm{D}}_{\mathrm{FMO}}|\hat{f}|\phi^{\mathrm{A}}_{\mathrm{FMO}}\rangle$，$\hat{f}$ 为给体-受体体系的 Kohn-Sham 算符。量 $\phi^{\text{D}}_{\text{FMO}}$ 与 $\phi^{\text{A}}_{\text{FMO}}$ 分别是给体片段与受体片段的 Kohn-Sham 前线分子轨道，它代表电荷转移过程的一粒子图像。

在此方法中，计算通常分别在两个片段上进行，随后计算 FMO 下的非对角 Kohn-Sham 算符（以及重叠矩阵）。为计算 FMO 耦合，**Q-Chem** 的设置方式与“1+1”方法类似。

有时人们希望计算超越“给体 HOMO 与受体 LUMO”的前线轨道之间的耦合。可使用 *$rem* 选项 STS_TRANS_DONOR 与 STS_TRANS_ACCEPTOR 为 FMO 耦合计算选取一定范围的占据轨道与虚轨道。

### `STS_TRANS_DONOR`

> **在 ET 耦合的 FMO 方法中控制给体前线分子轨道的范围。**
>
> * **类型**：`STRING`
> * **默认值**：`NONE`
> * **选项**：
>     * $o$
>     * -
>     * $v$
>     * 分别计算 $o$ 与 $v$ 所指定的占据分子轨道与虚分子轨道之间的耦合。
> * **建议**：无

### `STS_TRANS_ACCEPTOR`

> **在 ET 耦合的 FMO 方法中控制受体前线分子轨道的范围。**
>
> * **类型**：`STRING`
> * **默认值**：`NONE`
> * **选项**：
>     * $o$
>     * -
>     * $v$
>     * 分别计算 $o$ 与 $v$ 所指定的占据分子轨道与虚分子轨道之间的耦合。
> * **建议**：无

???+ example "示例 10.76：使用 FMO 方法计算堆积型乙烯二聚体的电子转移耦合"
    ```qchem
    $molecule
     0  1
    --
     0  1
     C   0.662489   0.000000   0.000000
     H   1.227637   0.917083   0.000000
     H   1.227637  -0.917083   0.000000
     C  -0.662489   0.000000   0.000000
     H  -1.227637  -0.917083   0.000000
     H  -1.227637   0.917083   0.000000
    --
     0  1
     C   0.720595   0.000000   4.500000
     H   1.288664   0.921368   4.500000
     H   1.288664  -0.921368   4.500000
     C  -0.720595   0.000000   4.500000
     H  -1.288664  -0.921368   4.500000
     H  -1.288664   0.921368   4.500000
    $end
    
    $rem
       METHOD              =  lrcwpbe
       OMEGA               =  
    $end
    ```
