---
title: "5.7.4 交换偶极模型（XDM）"
---

## 5.7.4 交换偶极模型（XDM）

（2026 年 7 月 4 日）

## 5.7.4.1 理论

Becke 和 Johnson 提出了一种色散的*交换偶极模型*（exchange dipole model，XDM）。[[87]](../bib_references/bib.md#bib83)

在该模型中，吸引性色散能量来源于一个分子中交换空穴（exchange hole）的瞬时偶极矩与另一个分子中的诱导偶极矩之间的相互作用。这是一种概念简单却十分强大的方法，已被证明无需拟合参数即可得到非常准确的色散系数。这使得在单一密度泛函理论（Density Functional Theory，DFT）框架内同时计算分子间和分子内色散相互作用成为可能。该方法在 **Q-Chem** 程序中的实现与验证详见文献 [[707]](../bib_references/bib.md#bib739)，其中在 **Q-Chem** v. 6.1.1 中加入了更新的一套阻尼参数[[1027]](../bib_references/bib.md#bib1070) [[483]](../bib_references/bib.md#bib494)。

交换空穴函数 $h_{\sigma}(\mathbf{r},\mathbf{r}^{\prime})$ 的偶极矩在点 $\mathbf{r}$ 处表示为

<a id="Ch5.E40"></a>
$$
d_{\sigma}(\mathbf{r})=-\mathbf{r}-\int h_{\sigma}(\mathbf{r},\mathbf{r}^{\prime})\;\mathbf{r}^{\prime}\;d\mathbf{r}^{\prime}\;, \tag{5.40}
$$

其中 $\sigma=\alpha,\beta$。该量依赖于交换空穴模型，**Q-Chem** 中的实现采用 Becke-Roussel（BR）模型。[[91]](../bib_references/bib.md#bib75) 在大多数实现中，BR 模型 $h_{\sigma}$ 没有解析形式，其数值必须在每个网格点上通过数值计算获得。**Q-Chem** 首次为该函数推导出了解析表达式，[[707]](../bib_references/bib.md#bib739) 该表达式基于非线性插值与样条技术，显著提升了计算效率与数值稳定性。

与 XDM 一起使用了两种不同的阻尼函数。其中一种仅依赖分子间 $C_{6}$ 系数，其在 **Q-Chem** 中的实现记为 "XDM6"。在该版本中，色散能量为[[87]](../bib_references/bib.md#bib83)

<a id="eq:XDM6"></a>
$$
E_{\text{vdW}}^{\text{XDM6}}=\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}E_{\text{vdW},AB}=-\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}\frac{C_{6,AB}}{R_{AB}^{6}+\kappa\,C_{6,AB}/E^{\text{corr}}_{AB}}\;. \tag{5.41}
$$

分母中的项 $\kappa\,C_{6,AB}/E^{\text{corr}}_{AB}$ 可防止短程发散。量 $E_{AB}^{\text{corr}}$ 是自由原子 $A$ 和 $B$ 的关联能绝对值之和，而 $\kappa$ 是一个阻尼参数，其"普适"之处在于它与泛函的选择无关。[[87]](../bib_references/bib.md#bib83)

色散系数 $C_{6,AB}$ 按如下公式计算[[87]](../bib_references/bib.md#bib83)

<a id="Ch5.E42"></a>
$$
C_{6,ij}=\frac{\langle d_{\rm X}^{2}\rangle_{\!A}\langle d_{\rm X}^{2}\rangle_{\!B}\;\alpha_{\!A}\,\alpha_{B}}{\langle d_{\text{X}}^{2}\rangle_{\!A}\,\alpha_{B}+\langle d_{\text{X}}^{2}\rangle_{\!B}\,\alpha_{A}} \tag{5.42}
$$

其中 $\langle d_{\rm X}^{2}\rangle_{\!A}$ 是原子 $A$ 的交换空穴偶极矩的平方，该原子（在分子中）的有效极化率为 $\alpha_{\!A}$。

XDM6 方案可以进一步推广以包含高阶色散系数，[[89]](../bib_references/bib.md#bib86) 这就导出了 **Q-Chem** 中的 "XDM10" 模型：

<a id="eq:XDM10"></a>
$$
E_{\rm vdW}^{\text{XDM10}}=-\sum^{\text{atoms}}_{A}\sum^{\text{atoms}}_{B<A}\left(\frac{C_{6,AB}}{R_{{\rm vdW},AB}^{6}+R_{AB}^{6}}+\frac{C_{8,AB}}{R_{{\rm
vdW},AB}^{8}+R_{AB}^{8}}+\frac{C_{10,AB}}{R_{{\rm vdW},AB}^{10}+R_{AB}^{10}}\right)\;. \tag{5.43}
$$

高阶色散系数利用交换空穴的高阶多极矩计算得到。[[651]](../bib_references/bib.md#bib675)

量 $R_{{\rm vdW},AB}$ 用于防止短程发散，名义上等于原子 $A$ 和 $B$ 的有效原子半径之和。实际中它由如下公式确定[[651]](../bib_references/bib.md#bib675)

<a id="eq:Rvdw-damp"></a>
$$
R_{{\rm vdW},AB}=a_{1}R_{{\text{crit}},AB}+a_{2} \tag{5.44}
$$

其中临界距离为

<a id="Ch5.E45"></a>
$$
R_{{\text{crit}},AB}=\frac{1}{3}\left[\left(\frac{C_{8,AB}}{C_{6,AB}}\right)^{1/2}+\left(\frac{C_{10,AB}}{C_{6,AB}}\right)^{1/4}+\left(\frac{C_{10,AB}}{C_{8,AB}}\right)^{1/2}\right] \tag{5.45}
$$

以及两个参数 $a_{1}$ 和 $a_{2}$。这些参数最初是使用 Hartree-Fock 交换拟合得到的，[[651]](../bib_references/bib.md#bib675) 但随后针对多种不同的交换-关联泛函进行了优化：PW86PBE、PBE、BLYP、B97-1、B3LYP、B3P86、B3PW91、PBE0、BHHLYP、LRC-$\omega$PBE 和 CAM-B3LYP。[[1027]](../bib_references/bib.md#bib1070) 这套泛函对应的参数已在 **Q-Chem** 中实现。[[483]](../bib_references/bib.md#bib494)

**注意：**

对于上述以外的泛函，将使用 Hartree-Fock 的参数值 $a_{1}$ 和 $a_{2}$，尽管这可能并非最优选择。

## 5.7.4.2 作业控制

与 DFT-D 类似，范德华能量作为 SCF 后的修正项加入。XDM6 和 XDM10 均支持解析梯度和 Hessian。色散修正通过在 *$rem* 段中设置 XDM = TRUE 来请求。所有其他作业控制变量都属于 *$xdm* 输入段，详见下文说明。其中只有 **NAtoms_Mol1** 是必需的，它用于确定 *$molecule* 段的哪一部分对应单体 $A$，其余部分则对应单体 $B$。要求 $A$ 的所有原子在 *$molecule* 段中必须分组放在一起。

XDM

### `XDM`

> **控制在 SCF 计算中是否加入 XDM 色散**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 不应用 XDM 方案。
>     * 1
>     * 将 XDM 色散作为对 SCF 能量（以及梯度，如适用）的修正加入。
>     * 2
>     * 将色散作为 DFT 泛函的一部分并执行完整的自洽场计算。
> * **建议**: 第二种（自洽）选项仅对 XDM6 可用。

### `NAtomsMol1`

> **设定单体 $A$ 的大小。输入段: $xdm**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $N$
>     * 单体
>     * $A$
>     * 由
>     * $molecule
>     * 段中的前
>     * $N$
>     * 个原子组成。
> * **建议**: 这是 $xdm 段中唯一必需的关键字。两个单体必须在 $molecule 段中各自分组放在一起；注意 Q-Chem 基于片段（fragment）的输入格式不能与 XDM 一起使用。

### `Method`

> **控制使用哪种 XDM 方法。输入段: $xdm**
>
> * **类型**: `STRING`
> * **默认值**: `XDM10`
> * **选项**:
>     * XDM6
>     * 使用仅含
>     * $C_{6}$
>     * 的模型，见式 (
>     * 5.41
>     * )。
>     * XDM10
>     * 使用包含
>     * $C_{8}$
>     * 和
>     * $C_{10}$
>     * 的模型，见式 (
>     * 5.43
>     * )。
> * **建议**: XDM10 通常更加准确，是现在首选的方法。

### `Damp_C6_K`

> **设定式 ( 5.41 ) 中的阻尼参数 $\kappa$。输入段: $xdm**
>
> * **类型**: `FLOAT`
> * **默认值**: `0.8`
> * **选项**:
>     * $x$
>     * 设置
>     * $\kappa=x$
>     * 。
> * **建议**: 默认值取自文献 Becke:2005a，其设计为普适值。

### `Damp_A1`

> **设定式 ( 5.44 ) 中的参数 $a_{1}$。输入段: $xdm**
>
> * **类型**: `FLOAT`
> * **默认值**: `Various`
> * **选项**:
>     * $x$
>     * 设置
>     * $a_{1}=x$
>     * 。
> * **建议**: 针对 HF、PW86PBE、PBE、BLYP、B97-1、B3LYP、B3P86、B3PW91、PBE0、BHHLYP、LRC-$\omega$PBE 和 CAM-B3LYP 提供了泛函特定的默认值，取自文献 1027 Otero-de-la-Roza A., Johnson E. R. J. Chem. Phys. (2013), 138, pp. 204109. 链接。对于其他泛函，默认使用 HF 的值（文献 651 Johnson E. R., Becke A. D. J. Chem. Phys. (2006), 124, pp. 174104. 链接），尽管 Q-Chem 会打印警告提示这可能并非最优。

### `Damp_A2`

> **设定式 ( 5.44 ) 中的参数 $a_{2}$。输入段: $xdm**
>
> * **类型**: `FLOAT`
> * **默认值**: `Various`
> * **选项**:
>     * $x$
>     * 设置
>     * $a_{2}=x$
>     * 。
> * **建议**: 关于泛函特定值的说明与 Damp_A1 的情况相同。

### `Print`

> **控制 XDM 过程的打印级别。输入段: $xdm**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * 0
>     * 不打印。
>     * 1
>     * 最少打印。
>     * 2
>     * 调试级别打印。
> * **建议**: 无

### `Use_Elec_Drv`

> **指定是否将梯度修正加到 XDM 能量中。输入段: $xdm**
>
> * **类型**: `LOGICAL`
> * **默认值**: `TRUE`
> * **选项**:
>     * TRUE
>     * 使用梯度修正。
>     * FALSE
>     * 不使用梯度修正。
> * **建议**: 该选项仅在与 Becke 的 $C_{6}$ 阻尼函数（使用插值的 BR89 模型）配合时有效。

???+ example "示例 5.14: 展示使用 XDM 色散修正对 vdW 复合物 He $\cdots$ N ${}_{2}$ 进行频率计算的输入文件样例"
    ```qchem
    $molecule
       0 1
       He 0.000000  0.00000   3.800000
       N  0.000000  0.000000  0.546986
       N  0.000000  0.000000 -0.546986
    $end
    
    $rem
       JOBTYPE             FREQ
       IDERIV              2
       EXCHANGE            B3LYP
       INCDFT              0
       SCF_CONVERGENCE     8
       BASIS               6-31G*
       XDM                 TRUE
    $end
    
    $xdm
      method      xdm6
      natoms_mol1 1
    $end
    ```
