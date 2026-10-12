---
title: "10.8.7 振动分辨的电子光谱与共振拉曼光谱"
---

## 10.8.7 振动分辨的电子光谱与共振拉曼光谱

（2026 年 7 月 4 日）

光学光谱学研究的是光与物质之间的相互作用，其涵盖范围广泛的物理与化学行为，
并可由光谱仪直接记录。现代光谱技术已应用于众多研究领域，
并成为获取物质结构与动力学特征信息的常用工具。
然而，实验测得的光谱并不能直接给出物质的微观信息。光谱的理论计算可作为实验测量的
补充手段，并帮助人们更深入地理解底层物理与化学现象。[[1060]](../bib_references/bib.md#bib1105)

通过对比实验结果与计算值，人们可以容易地确定物质的几何结构、电子结构与动力学特征。
此外，不同效应对光谱性质的影响也可以通过计算加以量化。

振动分辨的单光子吸收（one-photon absorption, OPA）与发射（one-photon emission, OPE）光谱，
以及共振拉曼散射（resonance Raman scattering, RRS）光谱，均涉及分子振动态与电子态的同步变化，
因此能够揭示可靠的分子结构—性质关系。对这些光谱进行理论预测，
需要同时结合电子结构理论与量子动力学方法，分别用于获取结构参数和描述量子动力学过程。
[[1288]](../bib_references/bib.md#bib1343)

关于使用 IMDHO 模型（忽略 Duschinsky 旋转）进行 RRS 模拟，请参见第 [10.8.6](subsec_RR-IMDHO.md) 节。

## 10.8.7.1 光谱模拟的含时方法

基于微扰理论，从初态 $|I\rangle$ 到末态 $|F\rangle$ 的单光子或双光子跃迁过程的跃迁速率
正比于 $k_{IF}=|\langle F|\hat{M}|I\rangle|^{2}\delta(\Delta\omega)$，其中 $\delta(\Delta\omega)$ 为线型函数，
对单光子跃迁有 $\Delta\omega=\omega_{i}-\omega_{FI}$，对双光子过程有 $\Delta\omega=\omega_{1}+\omega_{2}-\omega_{FI}$。
这里 $\omega_{i}$、$\omega_{1}$ 与 $\omega_{2}$ 表示入射光子频率，算符 $\hat{M}$ 定义为

<a id="Ch10.E82"></a>

$$
\hat{M}=\begin{cases}\hat{\mu}&\text{(one-photon transition)}\\
\sum_{L}\left[\frac{{\bf\mu}\cdot\hat{e}_{2}|L\rangle\langle L|{\bf\mu}\cdot\hat{e}_{1}}{(\omega_{1}-\omega_{LI})}+\frac{{\bf\mu}\cdot\hat{e}_{1}|L\rangle\langle L|{\bf\mu}\cdot\hat{e}_{2}}{(\omega_{2}-\omega_{LI})}\right]&\text{(two-photon transition)}\end{cases}\;. \tag{10.82}
$$

在双光子情形中存在中间态或所谓“虚态” $|L\rangle$。

拉曼散射是一个双光子过程。在该过程中，频率为 $\omega_{i}$ 的一个光子被吸收，
频率为 $\omega_{S}$ 的另一个光子被发射，同时体系从初振动态跃迁至末振动态。
基于微扰理论，拉曼过程的跃迁速率正比于
$S(\omega_{i},\omega_{S})=|\langle F|\hat{M}|I\rangle|^{2}\delta(\Delta\omega)$，其中

<a id="A3.S8.EGx80"></a>

$$
\displaystyle\hat{M}=\sum_{L}\left[\dfrac{\mu\cdot\hat{e}_{2}|L\rangle\langle L|\mu\cdot\hat{e}_{1}}{(\omega_{i}-\omega_{LI})}-\dfrac{\mu\cdot\hat{e}_{1}|L\rangle\langle L|\mu\cdot\hat{e}_{2}}{(\omega_{S}+\omega_{LI})}\right] \tag{10.83}
$$

且 $\Delta\omega=\omega_{S}-\omega_{i}+\omega_{FI}$。
微分光子散射截面由下式给出[[35]](../bib_references/bib.md#bib18)

<a id="rrs1"></a>

$$
\sigma(\omega_{i},\omega_{S})\propto\frac{4\omega_{i}\omega_{S}^{3}}{9c^{4}}S(\omega_{i},\omega_{S}). \tag{10.84}
$$

RRS 光谱是振动拉曼光谱的一种，其入射激光频率接近所研究分子或晶体的某一电子跃迁频率。
由于 $L$ 态与初始 $I$ 态之间的绝热能隙 $\omega_{LI}$ 接近激光频率 $\omega_{i}$，
中间态 $L$ 将对 RRS 起主导贡献。在“共振”条件下，非共振电子态的贡献可以被忽略。

可以通过 Herzberg–Teller（HT）展开来计算 $M_{IF}=\langle\Phi_{F}|\hat{M}|\Phi_{I}\rangle$，
*即*，将积分围绕核平衡构型 $Q=0$ 进行展开。将纯自旋 Born–Oppenheimer（psBO）
函数写成电子波函数 $\Psi$ 与振动波函数 $\Lambda$ 的乘积

<a id="Ch10.E85"></a>

$$
\Phi_{n}(q,Q)=\Psi_{n}(q,Q)\Lambda_{n}(Q)\;, \tag{10.85}
$$

则有

<a id="A3.S8.EGx81"></a>

$$
\displaystyle\begin{aligned} \displaystyle\Psi_{n}(q,Q)&\displaystyle=\Psi_{n}(q,0)+[\partial{\Psi_{n}(q,0)}/{\partial Q}]_{Q=0}Q+\cdots\;,\\
\displaystyle M_{IF}&\displaystyle=M_{IF}(Q=0)+[\partial{M_{IF}}/{\partial Q}]_{Q=0}Q+\cdots\;.\end{aligned} \tag{10.86}
$$

式（[10.86](#HT1)）中的第二项源自 HT 展开。若在最低阶非零项之后截断展开，$M_{IF}$ 可写为

<a id="A3.S8.EGx82"></a>

$$
\displaystyle M_{IF} \tag{10.87}
$$

若第一项（直接跃迁）为零，则该过程为轨道禁阻（orbitally forbidden）。

为计算电-振（vibronic）矩阵元剩余部分中的振动项，我们可以采用谐振子近似。
此时波函数的振动部分可写为 $\Lambda_{n}=\prod^{N}_{k=1}\chi_{k}^{(n)}(\nu_{n})$，
其中 $N$ 是简正模式 $\chi_{k}$ 的总数，$\nu_{n}$ 是态 $|n\rangle$ 中与模式 $k$ 相关联的振动量子数。

$\delta$ 函数 $\delta(\Delta\omega)$ 可表示为傅里叶积分

<a id="eq4"></a>

$$
\delta(\Delta\omega)=\frac{1}{2\pi\hbar}\int_{-\infty}^{+\infty}\mathrm{e}^{(i\Delta\omega)t/\hbar}\,dt\;, \tag{10.88}
$$

于是从初态到末态的跃迁速率变为

<a id="eq:rate2"></a>

$$
k_{IF}=\int_{-\infty}^{+\infty}\exp[i(\omega_{0}+E_{i}-E_{f})t/\hbar-\gamma t]C_{i}(t)dt \tag{10.89}
$$

其中 $\gamma$ 为阻尼因子，且

<a id="Ch10.E90"></a>

$$
C_{i}(t)=\frac{\mbox{tr}[e^{-\beta\hat{H}_{i}}\mathrm{e}^{i\hat{H}_{i}t/\hbar}\hat{M}e^{-iH_{f}t/\hbar}\hat{M})}{\mbox{tr}[\mathrm{e}^{-\beta\hat{H}_{i}}]}\;. \tag{10.90}
$$

这里 $\beta=1/k_{B}T$；在单光子吸收与发射过程中 $\omega_{0}=\omega_{i}$，
在拉曼散射过程中 $\omega_{0}=\omega_{i}-\omega_{S}$。记号 $\mbox{tr}(\cdots)$ 表示对核与电子
自由度求迹，且 $\hat{M}=|\Lambda_{i}\rangle M_{IF}\langle\Lambda_{f}|+|\Lambda_{f}\rangle M_{FI}\langle\Lambda_{i}|$。
量 $\hat{H}_{i}$ 与 $\hat{H}_{f}$ 分别表示电子基态与激发态的核哈密顿量。

基态与激发态上振动运动的哈密顿量可写为

<a id="Ch10.E91"></a>

$$
\displaystyle H_{g} \tag{10.91a}
$$

其中 $P$ 与 $Q$ 分别为振动简正模式的动量与坐标。基态与激发态的简正模式坐标
通过 Duschinsky 旋转矩阵 $\bar{D}$ 相关联，

其关系为 $Q_{e}=\bar{D}Q_{g}+\bar{\Delta}$。量 $\bar{\Delta}$ 是基态与激发态之间
简正模式坐标的位移，*即*，与第 [10.8.6](subsec_RR-IMDHO.md) 节 IMDHO 理论中式（[10.76](subsec_RR-IMDHO.md#eq:Delta_k)）
中出现的量为同一物理量。相应的无量纲形式为 $\Delta_{j}=(\omega_{j}^{e})^{1/2}\bar{\Delta}_{j}$ 与
$D_{ij}=(\omega_{i}^{e}/\omega_{j}^{g})^{1/2}\bar{D}_{ij}$。
由上可知，跃迁速率可以利用关联函数方法在时域中直接计算。这一含时方法
已被实现用于计算振动分辨光谱。[[867]](../bib_references/bib.md#bib902)

显然，基态与激发态具有不同的势能面，因而具有不同的振动频率和简正模式。
质量加权笛卡尔位移坐标 $x$ 与简正模式坐标 $Q$ 之间的关系为

<a id="A3.S8.EGx84"></a>

$$
\displaystyle\begin{aligned} \displaystyle x^{g}-x_{0}^{g}&\displaystyle=L_{g}Q_{g}\;,\\
\displaystyle x^{e}-x_{0}^{e}&\displaystyle=L_{e}Q_{e}\;,\end{aligned} \tag{10.92}
$$

其中 $x_{0}^{g}$ 与 $x_{0}^{e}$ 分别为基态与激发态的平衡结构。对于理想的 $N$ 维谐振子，
基态与激发态的简正模式坐标之间满足

<a id="A3.S8.EGx85"></a>

$$
\displaystyle\begin{aligned} \displaystyle Q_{e}&\displaystyle=(L_{e})^{\top}L_{g}Q_{g}+(L_{e})\top(x_{0}^{g}-x_{0}^{e})\\
&\displaystyle=\bar{D}Q_{g}+\bar{\Delta}\;.\end{aligned} \tag{10.93}
$$

计算 Duschinsky 旋转矩阵与位移矢量需要势能面上的极小点以及 Hessian 矩阵。
计算激发态势能面可能非常耗时，尤其对大分子而言，而且常因态交叉（state crossings）而产生问题。
线性耦合模型（linear coupling model, LCM），亦称垂直梯度（vertical gradient, VG）近似，
被提出以规避这一问题。[[219]](../bib_references/bib.md#bib214)
 假设激发态势能面可由基态势能面（PES）的平移来近似，即 $\omega_{j}^{e}=\omega_{j}^{g}$ 且 $L_{e}=L_{g}$，
则 $Q_{j}$ 的位移可由激发态能量梯度 $(\partial E/\partial Q)_{j}$ 计算得到，$\Delta^{\!\text{VG}}$ 可写为

<a id="eq:VG"></a>

$$
\Delta_{j}^{\!\text{VG}}=(\omega_{j}^{g})^{-3/2}\left(\frac{\partial E}{\partial Q}\right)_{j}=\sum\limits_{i}(\omega_{j}^{g})^{-3/2}\left(\frac{\partial E}{\partial x_{i}}\right)L^{ij}_{g}. \tag{10.94}
$$

VG 近似等价于第 [10.8.6](subsec_RR-IMDHO.md) 节所讨论的 IMDHO 近似。[[665]](../bib_references/bib.md#bib689)

一般而言，Franck–Condon（FC）近似对于强允许的单光子或双光子跃迁已足够准确，
但对禁阻或弱允许的跃迁则失效，此时 FC 项趋于零。
在这种情况下，应当通过引入 Herzberg–Teller（HT）效应或非 Condon（non-Condon）
效应来修正这一偏差。[[831]](../bib_references/bib.md#bib863)

HT 型电-振耦合源于跃迁矩对简正模式坐标的依赖。当这些量按简正模式坐标展开时，
线性坐标依赖项的贡献通常被称为 HT 效应。[[35]](../bib_references/bib.md#bib18)

大量工作——无论是否考虑模式混合（Duschinsky 旋转，DR）效应——
都表明 HT 效应在 OPA、OPE 与 RRS 光谱中的重要性。[[824]](../bib_references/bib.md#bib862)

为预测 OPA、OPE 与 RRS 光谱，需要对基态和激发态进行电子结构计算。
在不同近似层级下所需的计算任务总结如下：

- •

FC。该模型可用于 OPA、OPE 与 RRS 光谱。

1. 1.

$x_{0}^{g}\neq x_{0}^{e}$，$L_{g}=L_{e}$，且 $\omega^{g}=\omega^{e}$。
先在激发态势能面上进行几何优化，随后进行基态几何优化与频率分析。
2. 2.

$x_{0}^{g}\neq x_{0}^{e}$，$L_{g}\neq L_{e}$，且 $\omega^{g}\neq\omega^{e}$。
需要在基态和激发态上分别进行几何优化与频率计算。
- •

FCHT。该模型可用于 OPA、OPE 与 RRS 光谱。

- •

$x_{0}^{g}\neq x_{0}^{e}$，$L_{g}\neq L_{e}$，且 $\omega^{g}\neq\omega^{e}$。它与第二类 FC 计算类似，
其中跃迁偶极矩导数通过激发态频率计算获得。需要在基态和激发态上
分别进行几何优化与频率计算。
- •

VG。该模型可用于 OPA 与 RRS 光谱。

- •

$x_{0}^{g}=x_{0}^{e}$，$L_{g}=L_{e}$，且 $\omega^{g}=\omega^{e}$。
仅涉及基态的几何优化与频率计算。激发态的频率与简正模式
被假定与基态相同。位移矢量由式（[10.94](#eq:VG)）近似给出，
其中激发态势能面的梯度由激发态受力（force）计算产生。
当然，VG 模型只包含 FC 项的贡献。

## 10.8.7.2 任务控制

由于基态与激发态参数均为必需，预测振动分辨光谱的流程被设计为两个步骤。
首先执行激发态计算，激发态相关信息将保存在 `$QCSCRATCH/savename` 中。
然后在完成基态频率分析之后调用振动光谱工具来模拟所请求的光谱。
需将 POINT_GROUP_SYMMETRY 设为 FALSE，以防止分子几何被变换到标准取向。
因此，振动光谱任务的输入可以按两种方式设置。其一，如第 [3.5](../ch03_inputs/sec_multiple_jobs.md) 节所述，
多个任务可用字符串 `@@@` 分隔。其二，如下文所述并如示例 [10.8.7.3](#ex:VibronicPFB1) 与
[10.8.7.3](#ex:VibronicPFB1) 所示，利用 `$QCSCRATCH/savename` 将任务拆分为独立的输入。

> ```qchem
> qchem infile_excited_state outfile_excited_state savename
> qchem infile_ground_state outfile_ground_state savename
> ```

振动光谱计算涉及两个 *$rem* 变量与一个 *$vibronic* 段。

### `SAVE_VIBRONIC_PARAMS`

> **保存振动光谱模拟所请求的激发态信息。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `FALSE`
> * **建议**: TRUE

### `VIBRONIC_SPECTRA`

> **指定将要预测的振动光谱类型。应在频率计算任务（jobtype = Freq）中使用。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * `0`: 不预测振动光谱。
>     * `1`: 计算 OPA 光谱。
>     * `2`: 计算 OPE 光谱。
>     * `3`: 计算 RRS 光谱。
> * **建议**: 使用默认值。

*$vibronic* 段中的变量：

### `MODEL`

> **指定用于模拟振动光谱的模型类型。输入段：$vibronic**
>
> * **类型**: `INTEGER`
> * **默认值**: `-1`
> * **可选值**:
>     * `1`: FC。
>     * `2`: FCHT。
>     * `3`: VG。
> * **建议**: 由用户自定义

### `TEMPERATURE`

> **指定振动光谱模拟中的温度。输入段：$vibronic**
>
> * **类型**: `FLOAT`
> * **默认值**: `$298.15$`
> * **可选值**:
>     * $t$: 温度，单位为 K。
> * **建议**: 由用户自定义

### `FREQ_RANGE`

> **指定振动光谱的频率范围。输入段：$vibronic**
>
> * **类型**: `FLOAT`
> * **默认值**: `$1.0\ 40000.0\ 10.0$`
> * **可选值**:
>     * $\nu_{\text{min}}\ \nu_{\text{max}}\ \delta\nu$: 最小值、最大值与步长，单位为 $\text{cm}^{-1}$。
> * **建议**: 由用户自定义

### `TIME_RANGE`

> **指定时域传播中的步长与步数。输入段：$vibronic**
>
> * **类型**: `FLOAT and INTEGER`
> * **默认值**: `$1.0\ 40000$`
> * **可选值**:
>     * $\delta t\ n_{\text{step}}$: 时间步长（以原子单位 a.u. 计）以及步数。
> * **建议**: 由用户自定义

### `DAMPING`

> **指定阻尼因子。输入段：$vibronic**
>
> * **类型**: `FLOAT`
> * **默认值**: `$300.0$`
> * **可选值**:
>     * $\gamma$: 阻尼因子，单位为 $\text{cm}^{-1}$。
> * **建议**: 由用户自定义

### `FREQ_SCALE_FACTOR`

> **指定频率缩放因子。输入段：$vibronic**
>
> * **类型**: `FLOAT`
> * **默认值**: `$1.0\ 1.0\ 1.0\ 1.0$`
> * **可选值**:
>     * $\lambda_{\text{H}}^{g}\ \lambda_{\text{H}}^{e}\ \lambda_{\text{ZPE}}^{g}\ \lambda_{\text{ZPE}}^{e}$: 依次为基态谐振频率、激发态谐振频率、基态零点能以及激发态零点能的缩放因子
> * **建议**: 由用户自定义

### `EPSILON`

> **指定光谱展宽因子。仅对 RRS 光谱模拟有效。输入段：$vibronic**
>
> * **类型**: `FLOAT`
> * **默认值**: `$25.0$`
> * **可选值**:
>     * $\varepsilon$: 展宽因子，单位为 $\text{cm}^{-1}$。
> * **建议**: 由用户自定义

## 10.8.7.3 振动光谱任务示例

???+ example "示例 10.45: 在 FCHT 近似下甲醛对应于 $S_{0}\rightarrow S_{1}$ 跃迁的 OPA 光谱输入文件。
第一步，在 $S_{1}$ 平衡几何处进行频率分析。然后对 $S_{0}$ 基态优化结构运行基态频率分析。"
    ```qchem
    $molecule
      0 1
      O    -0.0367447359    -0.0007590817     0.6963163574
      C     0.1461299638     0.0026846285    -0.5839700302
      H    -0.0732270514     0.9340547891    -1.1138640182
      H    -0.0391581765    -0.9359803358    -1.1140167891
    $end
    
    $rem
      JOBTYPE                freq
      METHOD                 b3lyp
      BASIS                  def2-TZVP
      CIS_STATE_DERIV        1
      CIS_SINGLETS           true
      CIS_TRIPLETS           false
      CIS_N_ROOTS            10
      SAVE_VIBRONIC_PARAMS   true ! enables saving information of S1 state
      MEM_TOTAL              5000
      POINT_GROUP_SYMMETRY   false
    $end
    
    @@@
    
    $molecule
       0 1
       O    0.0000000000     0.0000000000     0.6637077571
       C    0.0000000000     0.0000000000    -0.5351027012
       H    0.0000000000     0.9394749352    -1.1220697679
       H    0.0000000000    -0.9394749352    -1.1220697679
    $end
    
    $rem
       JOBTYPE              freq
       METHOD               b3lyp
       BASIS                def2-TZVP
       VIBRONIC_SPECTRA     1 !enables vibronic_spectra and reads saved information
       MEM_TOTAL            5000
       POINT_GROUP_SYMMETRY false
    $end
    
    $vibronic
       model        2
       freq_range   20000. 60000. 10.
       time_range   1. 40000
       damping      40.
    $end
    ```

???+ example "示例 10.46: 采用第一类 FC 模型计算振动分辨荧光，即 OPE，其方法如下。
以 p -氟苄基自由基（p-fluorobenzyl radical）从 $D_{1}$ 到 $D_{0}$ 的发射为例。
这是整个振动光谱模拟的第一个任务，通过运行激发态几何优化并将信息保留在
$QCSCRATCH/savename 中。完成示例 10.8.7.3 中的模拟需要用到本任务的信息。"
    ```qchem
    $molecule
       0 2
       C         1.4840482200    0.0000338155    0.0000000000
       C         0.7160497031    0.0000524901   -1.2119311870
       C        -0.7159596058    0.0000542629   -1.2126930961
       C        -1.4043236629    0.0000543088    0.0000000000
       C        -0.7159596058    0.0000542629    1.2126930961
       C         0.7160497031    0.0000524901    1.2119311870
       C         2.8748450131    0.0000120580    0.0000000000
       H         1.2370230923    0.0000896598   -2.1693859212
       H        -1.2717579173    0.0000412967   -2.1497435961
       H        -1.2717579173    0.0000412967    2.1497435961
       H         1.2370230923    0.0000896598    2.1693859212
       H         3.4346492051    0.0000003003   -0.9330758768
       H         3.4346492051    0.0000003003    0.9330758768
       F        -2.7508602624    0.0000394216    0.0000000000
    $end
    
    $rem
       JOBTYPE                opt
       METHOD                 b3lyp
       BASIS                  def2-SVP
       CIS_STATE_DERIV        1
       CIS_N_ROOTS            10
       SAVE_VIBRONIC_PARAMS   true !saved into $QCSCRATCH/savename
       POINT_GROUP_SYMMETRY   false
    $end
    ```

???+ example "示例 10.47: 使用来自示例 10.8.7.3 的第一类 FC 模型 OPE 方法，
获取 p -氟苄基自由基 $D_{1}$ 到 $D_{0}$ 跃迁的振动分辨荧光的最终任务。"
    ```qchem
    $molecule
       0 2
       C       1.4578807306     0.0130092784     0.0000000000
       C       0.7102753558     0.0082793447    -1.2194714816
       C      -0.6772053823    -0.0007923729    -1.2210832164
       C      -1.3603507249    -0.0052928605     0.0000000000
       C      -0.6772053834    -0.0007923730     1.2210832170
       C       0.7102753546     0.0082793447     1.2194714789
       C       2.8669152234     0.0219746232     0.0000000000
       H       1.2502372081     0.0119050313    -2.1697312391
       H      -1.2498963812    -0.0045285858    -2.1510495277
       H      -1.2498963822    -0.0045285858     2.1510495285
       H       1.2502372136     0.0119050313     2.1697312323
       H       3.4299577819     0.0255536038    -0.9358170827
       H       3.4299577814     0.0255536038     0.9358170860
       F      -2.7010161586    -0.0142661666     0.0000000000
    $end
    
    $rem
       JOBTYPE              freq
       METHOD               b3lyp
       BASIS                def2-SVP
       VIBRONIC_SPECTRA     2
       POINT_GROUP_SYMMETRY false
    $end
    
    $vibronic
       model        1
       temperature  0.
       freq_range   1. 40000. 10.
       time_range   1. 40000
       damping      20.
    $end
    ```

???+ example "示例 10.48: 采用 VG 近似计算苯氧基自由基（phenoxyl radical）的 RRS 光谱（$D_{0}\rightarrow D_{3}$ 跃迁）。
因此第一个任务在基态优化几何处计算 $D_{3}$ 态的受力，随后进行基态频率分析。
激发态受力和基态频率均在基态平衡几何处计算。"
    ```qchem
    $molecule
       0 2
       C       0.0000000000     1.2271514002    -1.0879472096
       C       0.0000000000     0.0000408897    -1.7873074655
       C       0.0000000000    -1.2270324440    -1.0880160727
       C       0.0000000000    -1.2409681161     0.2924435676
       C       0.0000000000    -0.0000313560     1.0551142042
       C       0.0000000000     1.2409428316     0.2924458686
       H       0.0000000000     2.1656442172    -1.6487551860
       H       0.0000000000    -0.0001767539    -2.8803293768
       H       0.0000000000    -2.1655968771    -1.6487220344
       H       0.0000000000    -2.1715667156     0.8648121894
       H       0.0000000000     2.1714692701     0.8649813475
       O       0.0000000000     0.0001236541     2.3063351676
    $end
    
    $rem
       JOBTYPE                force
       METHOD                 b3lyp
       BASIS                  def2-SVP
       CIS_STATE_DERIV        3
       CIS_N_ROOTS            10
       SAVE_VIBRONIC_PARAMS   true
       POINT_GROUP_SYMMETRY   false
    $end
    
    @@@
    
    $molecule
       read !VG approximation uses the same geometry for ground and excited state
    $end
    
    $rem
       JOBTYPE              freq
       METHOD               b3lyp
       BASIS                def2-SVP
       VIBRONIC_SPECTRA     3
       POINT_GROUP_SYMMETRY false
    $end
    
    $vibronic
       MODEL         3
       TEMPERATURE   0.
       FREQ_RANGE    1. 4000. 1.
       TIME_RANGE    1. 40000
       DAMPING       100.
       EPSILON       25.
    $end
    ```
