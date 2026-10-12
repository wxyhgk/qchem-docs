---
title: "7.4.2 作业控制"
---

## 7.4.2 作业控制

（2026 年 7 月 4 日）

属于 TDKS 作业控制且需放在 *$rem* 段中的变量只有两个：TDKS = TRUE 用于请求此类计算，以及（可选的）TDKS_RESTART = TRUE 用于恢复先前的时间演化。其余所有作业控制均依赖于 *$tdks* 输入段，其说明见下文。传播子算法在文献 [[1578]](../bib_references/bib.md#bib1641) 中有详细描述，而利用 TDKS 获得宽谱（broadband spectra）的方法则见文献 [[1578]](../bib_references/bib.md#bib1641) 和 [[566]](../bib_references/bib.md#bib585)。

## 7.4.2.1 基础：传播子与时间步长

假定 TDKS_RESTART = FALSE，程序会先执行一次标准的基态自洽场（SCF）计算，以得到 $t=0$ 时刻的电子密度。在该计算中，SCF_CONVERGENCE 的值需要设置得足够严格，因为在随后的 TDKS 计算中，密度会被外场扰动（以产生含时叠加态），因此初始密度中的任何收敛误差都必须小于人们试图在 TDKS 时间传播步骤中积分的、由扰动引起的涨落。推荐使用增量式 Fock 矩阵构建（INCFOCK = TRUE）来降低大量、时间间隔紧密的 Fock 构建的开销。基本 TDKS 传播计算的输入文件见下面的示例。基本作业相对简单，但更复杂的作业需要额外的输入文件，并产生额外的输出。

???+ example "示例 7.33: 基本 TDKS 作业。"
    ```qchem
    $molecule
       0 1
       O 0.000000 0.000000 0.000000
       H 0.758602 0.000000 0.504284
       H 0.758602 0.000000 -0.504284
    $end
    
    $rem
       METHOD            pbe0
       BASIS             6-31G*
       TDKS              true
       SCF_CONVERGENCE   7
    $end
    
    $tdks
       DT             0.05
       MAXITER        10 ! for production, want a much larger value
       PROPAGATOR     MMUT
       FIELD_VECTOR   1 1 1
       FIELD_TYPE     delta
       FIELD_AMP      0.0001
    $end
    ```

TDKS 方法在大多数实际应用都需要大量的时间步，因此程序提供了重启（restart）功能。通过在 *$rem* 段中设置 TDKS_RESTART = TRUE，可以将一次长的动力学模拟分段执行（*e.g.*, 以规避共享计算资源上的墙钟时间限制）。上一次作业的结果存储在暂存（scratch）目录中，下一个作业通过从同一目录读取数据来启动，并从中断的时间传播处继续。因此，后续 **Q-Chem** 作业必须使用 `-save` 标志，并且两次作业应使用同名（同一）暂存目录。默认情况下，中间结果每 1,000 步自动存储一次。如果作业在达到所请求的时间步数之前被意外终止，可以轻松地从最后保存的步骤重新启动。

### `TDKS_RESTART`

> **通过继续上一个作业来重启计算**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `TRUE`: TDKS 计算从上一次计算继续。
>     * `FALSE`: TDKS 计算从头开始。
> * **建议**: 无。

???+ example "示例 7.34: 展示重启功能的 TDKS 计算。"
    ```qchem
    $molecule
       0 1
       H    0.000000   0.000000   0.000000
       H    0.000000   0.000000   0.750000
    $end
    
    $rem
       METHOD            pbe
       BASIS             6-31G
       SCF_CONVERGENCE   9
       TDKS_RESTART      0
       TDKS              1
       INTEGRAL_SYMMETRY false
    $end
    
    $tdks
       dt                0.05
       maxiter           25
       propagator        MMUT
       field_vector      1 1 1
       field_type        delta
       field_amp         0.0001
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD            pbe
       BASIS             6-31G
       SCF_CONVERGENCE   9
       TDKS_RESTART      1
       TDKS              1
       SCF_GUESS         read
       INTEGRAL_SYMMETRY false
    $end
    
    $tdks
       dt                0.05
       maxiter           25
       propagator        MMUT
       field_vector      1 1 1
       field_type        delta
       field_amp         0.0001
    $end
    ```

其余的作业控制参数属于 *$tdks* 输入段。

### `dt`

> **时间步长 $\Delta t$ 的取值，以原子单位表示。INPUT SECTION: $tdks**
>
> * **类型**: `DOUBLE`
> * **默认值**: `0.02`
> * **选项**:
>     * $\Delta t>0$
> * **建议**: 对于激发能 $\hbar\omega<30$ eV 范围内宽谱的通用计算，取 $\Delta t=0.1$ a.u.。对于更高能量，$\Delta t=\pi/(10\Delta E)$（以原子单位计）是可靠的选择。

### `MaxIter`

> **最大步数 INPUT SECTION: $tdks**
>
> * **类型**: `INTEGER`
> * **默认值**: `15000`
> * **选项**:
>     * $>0$
> * **建议**: 总传播长度为 $\Delta t\times\mbox{{\bf MaxIter}}$。

### `Propagator`

> **时间传播算法 INPUT SECTION: $tdks**
>
> * **类型**: `STRING`
> * **默认值**: `MMUT`
> * **选项**:
>     * `EULER`: 欧拉（Euler）方法
>     * `MMUT`: 改进中点酉变换（Modified mid-point unitary transformation）方法
>     * `LFLPPC`: 线性 Fock、线性密度预测/校正（Linear Fock, linear density predictor/corrector）方法
>     * `EPPC`: 指数密度预测/校正（Exponential density predictor/corrector）方法
> * **建议**: 使用 MMUT、LFLPPC 或 EPPC。（不推荐使用欧拉方法。）与 MMUT 相比，两种预测/校正方法能够使用更大的时间步长实现稳定的动力学，并且还能对动力学的稳定性进行实时（on-the-fly）一致性检查，但这些方法在单步开销上比 MMUT 更昂贵。

### `PC_Fock_Thresh`

> **预测/校正算法中用于一致性检查的 Fock 矩阵阈值。INPUT SECTION: $tdks**
>
> * **类型**: `INTEGER`
> * **默认值**: `7 (for`
> * **选项**:
>     * `> 0`
> * **建议**: 无。

### `PC_Den_Thresh`

> **预测/校正算法中用于一致性检查的密度矩阵阈值。INPUT SECTION: $tdks**
>
> * **类型**: `INTEGER`
> * **默认值**: `7 (for`
> * **选项**:
>     * `> 0`
> * **建议**: 无。

### `PC_Max_Iter`

> **预测/校正方法每个时间步的最大自洽迭代次数 INPUT SECTION: $tdks**
>
> * **类型**: `INTEGER`
> * **默认值**: `20`
> * **选项**:
>     * `> 0`
> * **建议**: 无。

## 7.4.2.2 微扰场

TDKS 方法的基础是对一个（先前无场的）基态 $|\Psi_{0}\rangle$ 施加微扰电场 $\bm{\mathcal{E}}$。该微扰会产生所有对称性允许的激发态 $|\Psi_{n}\rangle$ 的叠加态，*i.e.*, 那些具有非零矩阵元 $\langle\Psi_{n}|\bm{\mathcal{E}}|\Psi_{0}\rangle$ 的激发态。可供选择微扰场有若干种，通过 *$tdks* 输入段中的 **Field_Type** 关键字来指定。（某些场类型需要额外的作业控制参数，详见下文。）

### `Field_Type`

> **外加电场 INPUT SECTION: $tdks**
>
> * **类型**: `STRING`
> * **默认值**: `DELTA`
> * **选项**:
>     * `DELTA`: $\delta$ 函数冲击（kick）
>     * `CW`: 连续波（continuous-wave）场
>     * `IMPULSE`: 脉冲场（高斯包络）
>     * `IMPULSE2`: 脉冲场（余弦平方包络）
>     * `STATIC`: 静电场
>     * `NONE`: 无场
> * **建议**: 无。

**Field_Type** 的这些选择可总结如下。注意 $\bm{\mathcal{E}}=(\mathcal{E}_{x},\mathcal{E}_{y},\mathcal{E}_{z})$ 是一个矢量，其大小由 **Field_Amp** 控制，其方向由 **Field_Vector** 控制。

- •

**Delta** 模拟狄拉克 $\delta$ 函数冲击，场 $\bm{\mathcal{E}}$ 仅在前两个时间步内（以恒定振幅）开启。
振幅由下方记录在案的 **Field_Amp** 关键字控制。为了在不同 $\Delta t$ 选择之间进行归一化，**Field_Amp** 实际指定的是*积分后*的场强 $\bm{\mathcal{E}}\Delta t$，即电场强度本身为
(**Field_Amp**)/$(\Delta t)$.[[566]](../bib_references/bib.md#bib585)

如此一来，**Field_Amp** 控制的便是 $\delta$ 函数脉冲向体系注入的总能量，这也是使采用两个不同时间步长的模拟结果可以进行并排比较的唯一方法。
- •

**CW** 模拟形式为 $\bm{\mathcal{E}}(t)=\mathbf{A}_{0}\sin(\omega t)$ 的连续波电场，其振幅 $\mathbf{A}_{0}$ 和频率 $\omega$ 分别在 *$tdks* 段中使用关键字 **Field_Amp** 和 **Field_Frequency** 设置。
- •

**Impulse** 场具有如下高斯包络，

<a id="Ch7.E60"></a>

$$
\bm{\mathcal{E}}(t)=\mathbf{A}_{0}\exp\left(\frac{(t-t_{\text{peak}})^{2}}{2\tau^{2}}\right)\sin(\omega t) \tag{7.60}
$$

其中 $\mathbf{A}_{0}$ 和频率 $\omega$ 分别使用 **Field_Amp** 和 **Field_Frequency** 设置。
场参数 $\tau$ 和 $t_{\text{peak}}$ 分别在 *$tdks* 段中使用 **Field_Tau** 和 **Field_Peak** 设置。方向 $\mathbf{A}_{0}$ 使用 **Field_Vector** 设置。
- •

**Impulse2** 场具有余弦平方包络，场 $\bm{\mathcal{E}}$ 初始即开启，并在 $t=2t_{\text{peak}}$ 时关闭。对于 $0\leq t\leq 2t_{\text{peak}}$，

<a id="Ch7.E61"></a>

$$
\bm{\mathcal{E}}(t)=\mathbf{A}_{0}\cos^{2}\left[\frac{\pi}{2t_{\text{peak}}}(t_{\text{peak}}-t)\right]\cos[\omega(t-t_{\text{peak}})] \tag{7.61}
$$

其中 $\mathbf{A}_{0}$ 和频率 $\omega$ 分别使用 **Field_Amp** 和 **Field_Frequency** 设置。
场参数 $t_{\text{peak}}$ 在 *$tdks* 段中使用 **Field_Peak** 设置。方向 $\mathbf{A}_{0}$ 使用 **Field_Vector** 设置。

### `Field_Vector`

> **外加电场矢量的方向 INPUT SECTION: $tdks**
>
> * **类型**: `VECTOR`
> * **默认值**: `1.0 1.0 1.0`
> * **选项**:
>     * `NONE`
> * **建议**: NONE

### `Field_Amp`

> **外场的振幅（以 a.u. 计）INPUT SECTION: $tdks**
>
> * **类型**: `DOUBLE`
> * **默认值**: `0.0001`
> * **选项**:
>     * `NONE`
> * **建议**: $10^{-3}$ – $10^{-4}$ a.u. 的取值对应弱场，适用于模拟吸收光谱（ i.e. ，处于线性响应范围之内，但无需线性响应含时密度泛函理论（LR-TDDFT）所要求的逐根（root-by-root）计算）。更大的场振幅对应强场动力学，例如二次谐波产生（second harmonic generation）。

### `Field_Frequency`

> **外场的频率 $\omega$，以 eV 为单位。INPUT SECTION: $tdks**
>
> * **类型**: `DOUBLE`
> * **默认值**: `0.001`
> * **选项**:
>     * `NONE`
> * **建议**: 使用能量单位是为了在利用 TDKS 产生宽谱时更加方便。

### `Field_Peak`

> **高斯或余弦平方脉冲场的峰值位置 $t_{\text{peak}}$（以时间的原子单位计）。INPUT SECTION: $tdks**
>
> * **类型**: `DOUBLE`
> * **默认值**: `0.0`
> * **选项**:
>     * `NONE`
> * **建议**: NONE

### `Field_Tau`

> **高斯脉冲场中 $\tau$ 的取值（以时间的原子单位计）。INPUT SECTION: $tdks**
>
> * **类型**: `DOUBLE`
> * **默认值**: `0.7`
> * **选项**:
>     * `NONE`
> * **建议**: NONE

## 7.4.2.3 复吸收势（Complex Absorbing Potential, CAP）

在高能量区域模拟宽谱时（*e.g.*, K 边的 X 射线吸收光谱（x-ray absorption spectroscopy）计算，对应 1s $\rightarrow$ 虚轨道激发），所涉及的电子动力学往往对应于使密度涨落到高斯基组所覆盖空间区域边缘的过程。基组的边缘施加了一堵人为的势垒墙，含时波包会从这堵墙上反射，然后与其自身的出射波发生干涉，而这种干涉只是有限基组近似的纯粹人为体现[[1579]](../bib_references/bib.md#bib1642)。

实际上，这会给人为地在 TDKS 计算得到的宽谱中引入虚假振荡。在强场电子动力学（如高次谐波产生（high harmonic generation））的 TDKS 模拟中也是如此[[1579]](../bib_references/bib.md#bib1642)。

这些不良的人为假象可以通过引入复吸收势（CAP）来消除，CAP 会湮灭遇到它的出射波。

对于 TDKS 计算，可用的 CAP 由各原子中心球形势的叠加构成，这些球形势可以相互重叠[[1579]](../bib_references/bib.md#bib1642)。

在每一个这样的势中，势在原子 $k$ 的位置 $\mathbf{R}_{k}$ 周围截止半径 $r_{0}$ 内为零。超出该半径后，势以曲率 $\eta$ 二次增长。
这是通过一组原子中心的 CAP 函数来实现的

<a id="eqn:fk_CAP"></a>

$$
f^{\text{CAP}}_{k}(\mathbf{r})=\begin{cases}0,&\|\mathbf{r}-\mathbf{R}_{k}\|<r_{0}\\
\eta\big{(}\|\mathbf{r}-\mathbf{R}_{k}\|-r_{0}\big{)}^{2},&\|\mathbf{r}-\mathbf{R}_{k}\|\geq r_{0}\end{cases}\;. \tag{7.62}
$$

在空间任意一点 $\mathbf{r}$，CAP 的值取为 $\text{i}\upsilon_{\text{CAP}}(\mathbf{r})$，其中 $\upsilon_{\text{CAP}}(\mathbf{r})$ 取各原子中心势以及截止值
$E_{\text{max}}=10~{}E_{h}$ 中的最小值，后者的引入是为了避免数值溢出问题。综合起来，

<a id="Ch7.E63"></a>

$$
\upsilon_{\text{CAP}}(\mathbf{r})=\min\big{\{}E_{\text{max}},f_{1}^{\text{CAP}}(\mathbf{r}),f_{2}^{\text{CAP}}(\mathbf{r}),\ldots,\big{\}}\;. \tag{7.63}
$$

$r_{0}$ 的值由用户指定，并且针对具体应用应当进行检验。（在模拟强场电离动力学时，曾使用过
$r_{0}=3.5\times R_{\text{vdW}}$ 的取值，[[716]](../bib_references/bib.md#bib748)

其中 $R_{\text{vdW}}$ 为原子的代表性范德华半径。）
注意，将 $r_{0}$ 放置在高斯基函数本身的延展范围之外不会有任何效果。对于指数为 $\zeta$ 的高斯基函数，该函数的半高全宽（FWHM）为

<a id="Ch7.E64"></a>

$$
\text{FWHM}(\zeta)=2\left(\frac{\ln 2}{\zeta}\right)^{1/2}\;, \tag{7.64}
$$

因此该值的一半即是所讨论基函数径向延展的度量。
这可以用来估计基组的空间延展，此时 $\zeta$ 取最小（最弥散）的指数。

注意，当使用 PRINT_GENERAL_BASIS = TRUE 请求输出基函数信息时，指数 $\zeta$ 以 $a_{0}^{-2}$ 的原子单位打印。

*$tdks* 输入段中的以下变量控制 TDKS 计算中 CAP 的使用。

### `Do_CAP`

> **为 TDKS 计算激活复吸收势 INPUT SECTION: $tdks**
>
> * **类型**: `LOGICAL`
> * **默认值**: `False`
> * **选项**:
>     * `TRUE`: 使用 CAP
>     * `FALSE`: 不使用 CAP
> * **建议**: 无。

### `CAP_R0`

> **CAP 的截止半径（以 a.u. 计）INPUT SECTION: $tdks**
>
> * **类型**: `DOUBLE`
> * **默认值**: `0`
> * **选项**:
>     * `> 0`
> * **建议**: 推荐使用大于最大原子范德华半径两倍的取值，并根据需要进行检验。

### `CAP_Eta`

> **指定 CAP 的曲率 INPUT SECTION: $tdks**
>
> * **类型**: `DOUBLE`
> * **默认值**: `1.0`
> * **选项**:
>     * `> 0`
> * **建议**: 典型取值为 4.0–5.0，但建议进行检验。
