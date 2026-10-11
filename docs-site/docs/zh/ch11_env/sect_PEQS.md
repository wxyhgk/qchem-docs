---
title: "11.2.11 泊松边界条件（Poisson Boundary Conditions）"
---

## 11.2.11 泊松边界条件

（2026 年 7 月 4 日）

上文所介绍的每一种隐式溶剂化模型都是为各向同性的体相（bulk）溶剂化而设计的——这种条件可以用标量介电常数 $\varepsilon$ 来作定性描述。对于*各向异性*环境，例如液/气界面，更通用的做法是使用空间变化的介电*函数* $\varepsilon(\mathbf{r})$ 来求解泊松方程（Poisson's equation）。例如，这种方法可以用来模拟空气/水界面：在空间的某些区域使用 $\varepsilon=1$（空气），而在另一些区域使用 $\varepsilon=78$（水）。[[267]](../bib_references/bib.md#bib267)
 其中的原子区域用自洽场（SCF）方法来描述。介电函数 $\varepsilon(\mathbf{r})$ 的构造基于溶质空腔（solute cavity），这在某种程度上类似于极化连续介质模型（PCM）计算中的溶质空腔，但介电值是从空腔内部（即原子化的量子力学区域）的 $\varepsilon=1$ *平滑*（而非突变）地过渡到连续溶剂外部的 $\varepsilon=\varepsilon_{\rm solvent}$。用于建模液/气界面的选项同样可用；参见第 [11.2.11.3](#sect:PEQS:job_control) 节。与 PCM 不同（PCM 必须近似处理由于 QM 电荷密度“尾部”穿透到溶质空腔之外所引起的“体极化”），在泊松边界条件下这一效应可以被精确描述。取消该近似所付出的代价是：电荷密度必须在三维空间上进行离散化和积分，而不仅仅是在二维的溶质空腔表面上。

**Q-Chem** 对*泊松方程求解器*（Poisson Equation Solver, PEqS）方法的实现最早见于文献 [[267]](../bib_references/bib.md#bib267)
，并在文献 [[266]](../bib_references/bib.md#bib268)
 与 [[1046]](../bib_references/bib.md#bib1091)
 中得到改进。对具有有限离子强度的介电环境的支持则由文献 [[1305]](../bib_references/bib.md#bib1362)
 加入。使用本方法的读者请引用文献 [[266]](../bib_references/bib.md#bib268)
 与 [[1046]](../bib_references/bib.md#bib1091)
。

## 11.2.11.1 理论

对于介电*函数*（而非介电*常数*），泊松方程最一般的形式为

<a id="eq:Poisson"></a>

$$
\hat{\bm{\nabla}}\bm{\cdot}\left[\varepsilon(\mathbf{r})\hat{\bm{\nabla}}\varphi_{\rm tot}(\mathbf{r})\right]=-4\pi\rho_{\rm sol}(\mathbf{r})\;. \tag{11.25}
$$

溶质的电荷密度将被拆分为核部分与电子部分，

<a id="eq:rho"></a>

$$
\rho_{\rm sol}(\mathbf{r})=\rho_{\rm nuc}(\mathbf{r})+\rho_{\rm elec}(\mathbf{r})\;. \tag{11.26}
$$

总静电势 $\varphi_{\rm tot}$ 由溶质自身的静电势 $\varphi_{\rm elec}+\varphi_{\rm nuc}$（由式 ([11.26](#eq:rho)) 中的密度求得）以及在介质中感应的极化势共同组成：

<a id="eq:phi"></a>

$$
\varphi_{\rm tot}(\mathbf{r})=\varphi_{\rm elec}(\mathbf{r})+\varphi_{\rm nuc}(\mathbf{r})+\varphi_{\rm pol}(\mathbf{r})\;. \tag{11.27}
$$

为计算 $\rho_{\rm elec}$，首先在笛卡尔网格上求出真空中静电势的电子贡献，

<a id="eq:phi_elec"></a>

$$
\varphi_{\rm elec}(\mathbf{r}_{i})=\sum_{\mu\nu}^{N_{\rm basis}}P_{\mu\nu}\Bigl{\langle}g_{\mu}(\mathbf{r})\Bigl{|}\frac{1}{|\mathbf{r}-\mathbf{r}_{i}|}\Bigr{|}g_{\nu}(\mathbf{r})\Bigr{\rangle}\;. \tag{11.28}
$$

其中 **P** 为单电子密度矩阵，$g_{\mu}$ 与 $g_{\nu}$ 是原子中心的 Gauss 型基函数，积分对 $\mathbf{r}$ 进行。于是溶质电荷密度的电子部分可由下式得到

<a id="eq:rho_elec"></a>

$$
\rho_{\rm elec}(\mathbf{r})=-\frac{1}{4\pi}\hat{\nabla}^{2}\varphi_{\rm elec}(\mathbf{r})\;, \tag{11.29}
$$

实际计算中，$\varphi_{\rm elec}$ 的拉普拉斯（Laplacian）采用八阶有限差分格式求值。[[266]](../bib_references/bib.md#bib268)
 核电荷密度 $\rho_{\rm nuc}$ 则按经典方式描述，

<a id="eq:rho_nuc"></a>

$$
\rho_{\rm nuc}(\mathbf{r})=-\sum_{A}^{N_{\rm atoms}}Z_{\!A}\ \delta\left(\mathbf{r}-\mathbf{R}_{A}\right)\;, \tag{11.30}
$$

但为避免数值问题，实际计算中会把核电荷“抹平”到一个笛卡尔网格体素（voxel）之内。具体做法是把 $Z_{A}/dV$ 加到最靠近 $\mathbf{R}_{A}$ 的网格点上，其中 $dV$ 是笛卡尔体素的体积。真空中核的精确静电势按下式计算

<a id="eq:phi_nuke"></a>

$$
\varphi_{\rm nuc}(\mathbf{r})=-\frac{1}{4\pi}\sum_{A}^{N_{\rm atoms}}\frac{Z_{\!A}}{|\mathbf{r}-\mathbf{R}_{A}|}\;. \tag{11.31}
$$

式 ([11.30](#eq:rho_nuc)) 中的 Dirac δ 函数具有（体积）${}^{-1}$ 的量纲，因此已包含了前述的 $dV^{-1}$ 因子。

在求得电子与核的电荷密度以及真空中的静电势之后，我们就已经得到了 $\varepsilon(\mathbf{r})=1$ 时式 ([11.25](#eq:Poisson)) 的精确解。随后，按照文献 [[390]](../bib_references/bib.md#bib398)
 与 [[48]](../bib_references/bib.md#bib31)
 所述流程，以迭代方式获得感应的极化电荷密度及相应的静电势。将式 ([11.25](#eq:Poisson)) 改写，使其形式上等同于真空中的泊松方程但附加了一个额外的源电荷密度：

<a id="A3.S8.EGx104"></a>

$$
\displaystyle\begin{aligned} \displaystyle\hat{\nabla}^{2}\varphi_{\rm tot}(\mathbf{r})&\displaystyle=-4\pi\left[\frac{\rho_{\rm sol}(\mathbf{r})}{\varepsilon(\mathbf{r})}+\frac{\hat{\bm{\nabla}}\ln\varepsilon(\mathbf{r})\bm{\cdot}\hat{\bm{\nabla}}\varphi_{\rm tot}(\mathbf{r})}{4\pi}\right]\\
&\displaystyle=-4\pi\bigl{[}\rho_{\rm sol}(\mathbf{r})+\rho_{\rm pol}(\mathbf{r})\bigr{]}\;,\end{aligned} \tag{11.32}
$$

其中极化电荷密度为

<a id="eq:rho_pol"></a>

$$
\rho_{\rm pol}(\mathbf{r})=\rho_{\rm iter}(\mathbf{r})+\left(\frac{1-\varepsilon(\mathbf{r})}{\varepsilon(\mathbf{r})}\right)\rho_{\rm sol}(\mathbf{r})\;. \tag{11.33}
$$

迭代电荷密度 $\rho_{\rm iter}(\mathbf{r})$ 的形式为

<a id="eq:rho_iter1"></a>

$$
\rho_{\rm iter}^{(k+1)}(\mathbf{r})=\frac{\hat{\bm{\nabla}}\ln\varepsilon(\mathbf{r})\bm{\cdot}\hat{\bm{\nabla}}\varphi^{(k)}_{\rm tot}(\mathbf{r})}{4\pi} \tag{11.34}
$$

此为第 $k+1$ 次迭代。该函数仅在介电值从真空插值到溶剂的过渡区域中非零。另请注意，式 ([11.33](#eq:rho_pol)) 中的第二项在所有 $\varepsilon(\mathbf{r})=1$ 处为零。对 $\rho_{\mathrm{iter}}(\mathbf{r})$ 通过式 ([11.34](#eq:rho_iter1)) 执行更新 $\rho_{\mathrm{iter}}^{(k)}(\mathbf{r})\rightarrow\rho_{\mathrm{iter}}^{(k+1)}(\mathbf{r})$ 迭代至收敛，其中取 $\varphi^{(0)}_{\mathrm{tot}}(\mathbf{r})$ 为溶质在真空中的静电势。每次更新 $\rho_{\rm iter}(\mathbf{r})$ 都会生成一个新的极化电荷密度，并求解式 ([11.32](#eq:Poisson2)) 以获得新的总静电势。为稳定 $\rho_{\rm iter}(\mathbf{r})$ 的迭代更新，我们采用如下阻尼格式

<a id="A3.S8.EGx105"></a>

$$
\displaystyle\begin{aligned} \displaystyle\rho_{\rm iter}^{(k+1)}(\mathbf{r})&\displaystyle=\frac{\eta}{4\pi}\bigl{[}\hat{\bm{\nabla}}\ln\varepsilon(\mathbf{r})\bm{\cdot}\hat{\bm{\nabla}}\varphi^{(k)}_{\rm tot}(\mathbf{r})\bigr{]}+(1-\eta)\rho_{\rm iter}^{(k)}(\mathbf{r})\\
&\displaystyle=\eta\rho_{\rm iter}^{(k+1)}+(1-\eta)\rho_{\rm iter}^{(k)}(\mathbf{r})\end{aligned} \tag{11.35}
$$

而不是直接使用式 ([11.34](#eq:rho_iter1)) 的原始形式。依照文献 [[390]](../bib_references/bib.md#bib398)
 与 [[48]](../bib_references/bib.md#bib31)
，我们取 $\eta=0.6$。

一旦总电荷密度与静电势迭代达到自洽，即可计算溶剂化自由能

<a id="eq:Gpol"></a>

$$
G_{\rm pol}=\frac{1}{2}\int d\textbf{r}\;\varphi_{\rm pol}(\textbf{r})\;\rho_{\rm sol}(\mathbf{r})\;, \tag{11.36}
$$

其中

<a id="eq:phi_pol"></a>

$$
\varphi_{\rm pol}(\textbf{r})=\varphi_{\rm tot}(\textbf{r})-\varphi_{\rm sol}(\textbf{r})\;. \tag{11.37}
$$

由于 $\varphi_{\mathrm{tot}}$ 与 $\rho_{\mathrm{tot}}$ 在每一次 SCF 迭代中都是自洽求得的，因此必须把极化效应纳入 Fock 矩阵。这通过加上修正项 $\Delta\hat{F}=\delta G_{\mathrm{pol}}/\delta\rho_{\mathrm{elec}}$ 来实现。该修正项在原子轨道基组下的矩阵形式为

<a id="eq:fock"></a>

$$
\Delta F_{\mu\nu}=\int d\textbf{r}\;\varphi_{\rm pol}(\textbf{r})\;g_{\mu}(\textbf{r})\;g_{\nu}(\textbf{r})\;. \tag{11.38}
$$

更多细节及算法的完整描述参见文献 [[266]](../bib_references/bib.md#bib268)
。

## 11.2.11.2 竖直电离的非平衡溶剂化

PCM 框架内的非平衡溶剂化在第 [11.2.3.3](topic_pcm-em.md#subsubsec:noneq-PCM) 节中讨论，该方法[[940]](../bib_references/bib.md#bib979)
 已被推广用于结合泊松边界条件的竖直电离（vertical ionization）过程。[[267]](../bib_references/bib.md#bib267)
 这里实现了一种态特定（state-specific）方案，需要求解非线性 Schrödinger 方程，即式 ([11.7](topic_pcm-em.md#eq:SS-sdeq))。对于参考态（对应式 ([11.7](topic_pcm-em.md#eq:SS-sdeq)) 中的 $i=0$），这等价于求解式 ([11.25](#eq:Poisson)) 得到感应极化势，并分别按式 ([11.36](#eq:Gpol)) 与式 ([11.38](#eq:fock)) 计算溶剂化自由能和 Fock 矩阵修正。对于电离态（用下标 $i$ 表示），溶剂极化被划分为快分量与慢分量。在 Marcus 划分方案[[1530]](../bib_references/bib.md#bib1593)
 下，式 ([11.32](#eq:Poisson2)) 变为[[266]](../bib_references/bib.md#bib268)

<a id="eq:neq1"></a>

$$
-\frac{1}{4\pi}\hat{\nabla}^{2}\varphi_{{\rm tot},i}(\mathbf{r})=\rho_{{\rm sol},i}(\mathbf{r})+\rho^{\rm slow}_{{\rm pol},0}(\mathbf{r})+\rho^{\rm fast}_{{\rm pol},i}(\mathbf{r})\;, \tag{11.39}
$$

其中电离态的快极化电荷密度 $\rho^{\rm fast}_{{\rm pol},i}$ 为

<a id="eq:rho_pol_neq1"></a>

$$
\rho^{\rm fast}_{{\rm pol},i}(\mathbf{r})=\rho_{{\rm iter},i}(\mathbf{r})+\left(\frac{1-\varepsilon_{\rm opt}(\mathbf{r})}{\varepsilon_{\rm opt}(\mathbf{r})}\right)\bigl{[}\rho_{{\rm sol},i}(\mathbf{r})+\rho^{\rm slow}_{{\rm pol},0}(\mathbf{r})\bigr{]} \tag{11.40}
$$

而快极化势 $\varphi^{\rm fast}_{{\rm pol},i}$ 为

<a id="eq:phi_pol_neq1"></a>

$$
\varphi^{\rm fast}_{{\rm pol},i}(\textbf{r})=\varphi_{{\rm tot},i}(\textbf{r})-\varphi_{{\rm sol},i}(\textbf{r})-\varphi^{\rm slow}_{{\rm pol},0}(\mathbf{r})\;. \tag{11.41}
$$

下标 $i$ 与 0 分别指电离态与参考态。式 ([11.40](#eq:rho_pol_neq1)) 中的 $\varepsilon_{\rm opt}$ 是溶剂的光学位（高频）介电常数，而 $\rho_{{\rm iter},i}$ 按式 ([11.35](#eq:rho_iter2)) 计算，只是使用由 $\varepsilon_{\rm opt}$ 构造的介电函数，并以 $\varphi^{\rm fast}_{{\rm tot},i}$ 取代 $\varphi_{\rm tot}$。在 Marcus 划分方案中，感应溶剂极化电荷密度的慢分量按式 ([11.9](topic_pcm-em.md#slow_q)) 的三维类比（体电荷而非面电荷）来计算。

## 11.2.11.3 基本任务控制

在 *$rem* 区段中设置 SOLVENT_METHOD = PEQS 即可请求使用泊松边界条件的计算。出于计算效率考虑，泊松方程求解器（PEqS）通常要等到真空 SCF 计算的误差低于某个指定阈值后才启用，该阈值默认为 $10^{3}~{}E_{h}$，用户可通过 *$rem* 变量 PEQS_SWITCH 自行控制。

**注意：

当请求使用 PEqS 溶剂化时，对称性与标准核取向会被自动禁用，等价于设置 POINT_GROUP_SYMMETRY = FALSE 与 NO_REORIENT = TRUE。
泊松方程是在三维笛卡尔网格上求解的，除非网格间距非常小，否则能量不必具有旋转不变性。
**

PEQS_SWITCH

### `PEQS_SWITCH`

> **当 SCF 误差低于 10 ${}^{-\rm PEQS\_SWITCH}$ 时开始计入溶剂效应。**
>
> * **类型**: `INTEGER`
> * **默认值**: `3`
> * **选项**:
>     * $n$
>     * 对应于 10
>     * ${}^{-n}$
> * **建议**: 使用默认值，除非需要在 SCF 流程中更早地引入溶剂效应。

泊松方程求解器（PEqS）例程的进一步任务控制由两个区段设定：*$peqs_grid* 与 *$peqs*。（可选的第三个区段 *$epsilon* 将在后文讨论。）*$peqs_grid* 区段用于定义笛卡尔离散化网格，格式如下：

> ```qchem
> $peqs_grid
>    DimX <Nx> <Xmin> <Xmax>
>    DimY <Ny> <Ymin> <Ymax>
>    DimZ <Nz> <Zmin> <Zmax>
> $end
> ```

笛卡尔网格必须是正交的（orthorhombic），`Nx`、`Ny` 与 `Nz` 分别指 $x$、$y$、$z$ 轴方向上的网格点数目。

**注意：

为加速求解式 ([11.32](#eq:Poisson2)) 的共轭梯度 PEqS 例程的收敛，采用了四阶多重网格（multigrid）算法。[[266]](../bib_references/bib.md#bib268)
 这要求网格点数为奇数，并有附加约束：$N_{x}-1$、$N_{y}-1$ 与 $N_{z}-1$ 都必须能被 8 整除。
**

*$peqs_grid* 区段最后两列中的数值给出 $x$、$y$、$z$ 的最小值与最大值，单位为埃（Å）。$x$ 方向上的网格长度为 $L_{x}=x_{\rm max}-x_{\rm min}$，网格间距为 $\Delta x=L_{x}/(N_{x}-1)$。在式 ([11.30](#eq:rho_nuc)) 的讨论中出现过的体积元为 $dV=\Delta x\Delta y\Delta z$。

*$peqs* 区段控制 PEqS 计算的其他方面，包括溶质空腔的构造，以及界面溶剂化或非平衡溶剂化所需的其他参数。其格式为：

> ```qchem
> $peqs
>    <Keyword>  <parameter/option>
> $end
> ```

下面介绍可用的关键字。

### `BatchSize`

> **对静电势积分按笛卡尔网格的小块分批求值，而不是在一批中计算全部积分。输入区段：$peqs**
>
> * **类型**: `INTEGER`
> * **默认值**: `5000`
> * **选项**:
>     * $n$
>     * 对应的批次大小为
>     * $n$
>     * 个网格点。
> * **建议**: 对于大网格（$\geq 10^{6}$ 个网格点），推荐批次大小 $n\approx N_{x}N_{y}N_{z}/5$。

### `MaxIter`

> **设置共轭梯度求解器使用的最大迭代次数。输入区段：$peqs**
>
> * **类型**: `INTEGER`
> * **默认值**: `500`
> * **选项**:
>     * 用户自定义。
> * **建议**: 使用默认值，除非计算无法收敛。

### `OpticalDielectric`

> **设置溶剂的光学位介电常数。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `1.7778`
> * **选项**:
>     * $\varepsilon_{\rm opt}$
>     * 期望的
>     * $\varepsilon_{\text{opt}}$
>     * 数值（无量纲）。
> * **建议**: 光学位介电常数等于折射率的平方。默认值对应 25 ${}^{\circ}$ C 下的水。

### `PolarIterScale`

> **指定式 ( 11.35 ) 中用于稳定极化电荷密度迭代求解的混合参数 $\eta$。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `0.6`
> * **选项**:
>     * $\eta$
>     * 期望的无量纲混合参数数值。
> * **建议**: 使用默认值（该值已在文献 390 Fisicaro G. et al. J. Chem. Phys. (2016) , 144 , pp. 014103 . Link 与文献 48 Andreussi O., Dabo I., Marzari N. J. Chem. Phys. (2012) , 136 , pp. 064102 . Link 中经过检验），除非计算被证明难以收敛。

### `Print`

> **指定输出文件中的打印详细程度。输入区段：$peqs**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 基本打印，包含每次 SCF 迭代中的部分 PEqS 信息。
>     * 1
>     * 额外打印用于空腔构造的原子 vdW 半径。
>     * 2
>     * 调试信息。
> * **建议**: 使用 0 或 1。

### `SoluteCavity`

> **指定溶质空腔类型，它决定介电函数 $\varepsilon(\mathbf{r})$ 的形式。输入区段：$peqs**
>
> * **类型**: `STRING`
> * **默认值**: `Vacuum`
> * **选项**:
>     * Vacuum
>     * 在真空中进行计算，
>     * $\varepsilon(\mathbf{r})\equiv 1$
>     * 。
>     * RigidVDW
>     * 使用球对称误差函数构造空腔。
>     * Spherical
>     * 在溶质周围构造单个球形空腔。
>     * Arbitrary
>     * 构造用户自定义的介电空腔，其数值来自
>     * $epsilon
>     * 输入区段。
> * **建议**: 无。

### `SolventDielectric`

> **设置溶剂的介电常数值。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `78.39`
> * **选项**:
>     * $\varepsilon$
>     * 期望的
>     * $\varepsilon$
>     * 数值（无量纲）。
> * **建议**: 默认值对应 25 ${}^{\circ}$ C 下的水。

### `SolverThresh`

> **当误差低于 10 ${}^{-\rm PEQSolverThresh}$ 时认为静电势已收敛。输入区段：$peqs**
>
> * **类型**: `INTEGER`
> * **默认值**: `5`
> * **选项**:
>     * $n$
>     * 对应于 10
>     * ${}^{-n}$
> * **建议**: 使用默认值，除非希望采用更严格的收敛判据（计算代价更高）。

## 11.2.11.4 空腔构造

在传统 PCM 中，溶质空腔是由原子球并集构成的刚性二维曲面，其半径一般取 van der Waals 半径（$r_{\text{vdW}}$）乘以 1.2 的缩放因子；参见第 [11.2.4](subsec_PCM_job_control.md) 节。[[561]](../bib_references/bib.md#bib576)
 所谓刚性，是指一旦给定原子坐标，空腔在 SCF 迭代过程中保持不变（第 11.2.6 节讨论的等密度空腔是一个例外，但它对 PEqS 方法不可用）。此外，在溶质/连续介质边界处介电常数发生突变且不连续。依照文献 [[390]](../bib_references/bib.md#bib398)
 的做法，PEqS 计算中实现了该空腔的三维类比，使用连续且可微的球对称误差函数。该介电函数以参数方式依赖于核位置 $\mathbf{R}_{A}$，其形式为

<a id="eq:rigidvdw"></a>

$$
\varepsilon(\mathbf{r};\{\mathbf{R}_{A}\})=\bigl{(}\varepsilon_{\rm solvent}-1\bigr{)}\ \left\{\prod_{A}^{N_{\rm atoms}}h(d_{A},\Delta;\lvert\mathbf{r}-\mathbf{R}_{A}\rvert)\right\}\;, \tag{11.42}
$$

其中

<a id="eq:h_func"></a>

$$
h(d_{A},\Delta;\lvert\mathbf{r}-\mathbf{R}_{A}\rvert)=\frac{1}{2}\left[1+{\rm
erf}\left(\frac{\lvert\mathbf{r}-\mathbf{R}_{A}\rvert-d_{A}}{\Delta}\right)\right]\;. \tag{11.43}
$$

式 ([11.42](#eq:rigidvdw)) 在约 $4\Delta$ 的长度尺度上于 $\varepsilon=1$ 与 $\varepsilon=\varepsilon_{\rm solvent}$ 之间进行平滑插值。$\Delta$ 的数值通过 **RigidScale** 关键字指定。式 ([11.42](#eq:rigidvdw)) 与式 ([11.43](#eq:h_func)) 中的 $d_{A}$ 给出原子 $A$ 的原子球半径。默认情况下 $d_{A}=1.2\,r_{\rm vdW}$，但可以按下文所述加以控制。

### `Radii`

> **设置所选用的原子 vdW 半径 $r_{\text{vdW}}$。输入区段：$peqs**
>
> * **类型**: `STRING`
> * **默认值**: `Bondi`
> * **选项**:
>     * Bondi
>     * 使用改进的 Bondi 半径集（文献
>     * 1186
>     * Rowland R. S., Taylor R.
>     * J. Phys. Chem.
>     * (1996)
>     * ,
>     * 100
>     * ,
>     * pp. 7384
>     * .
>     * Link
>     * ）。
>     * UFF
>     * 通用力场（Universal Force Field）半径（文献
>     * 1146
>     * Rappé A. K. et al.
>     * J. Am. Chem. Soc.
>     * (1992)
>     * ,
>     * 114
>     * ,
>     * pp. 10024
>     * .
>     * Link
>     * ）。
>     * Read
>     * 从
>     * $van_der_waals
>     * 输入区段读取用户自定义半径。
> * **建议**: 无。Read 选项的工作方式与 $pcm 区段中的相应关键字相同（见第 11.2.4.1 节），其 $van_der_waals 输入区段的格式见第 11.2.10 节。

### `RigidScale`

> **设定刚性 vdW 空腔构造中所用误差函数将介电值从真空插值到溶剂的长度尺度。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `0.265 Å`
> * **选项**:
>     * $\Delta$
>     * 指定期望数值（单位为 Å）；参见式 (
>     * 11.43
>     * )。
> * **建议**: 使用默认值。该值在文献 390 Fisicaro G. et al. J. Chem. Phys. (2016) , 144 , pp. 014103 . Link 中经过调参，使小分子溶剂化能量的误差约为 1 kcal/mol。

### `VDWtype`

> **指定刚性 vdW 空腔构造的细节。输入区段：$peqs**
>
> * **类型**: `STRING`
> * **默认值**: `Scaled`
> * **选项**:
>     * Unscaled
>     * $d_{A}=r_{\mathrm{vdW}}$
>     * Scaled
>     * $d_{A}=r_{\mathrm{vdW}}\times scale$
>     * Shifted
>     * $d_{A}=(r_{\mathrm{vdW}}+shift)\times scale$
> * **建议**: 无。$scale$ 与 $shift$ 的数值分别由 VDWscale 和 VDWshift 关键字设置。

### `VDWscale`

> **设置应用于原子 van der Waals 半径的经验缩放因子。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `1.2`
> * **选项**:
>     * $scale$
>     * 指定原子 vdW 半径的无量纲缩放因子。
> * **建议**: 使用默认值。

### `VDWshift`

> **在构造刚性 vdW 空腔时调整球对称误差函数的中心位置。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `0.0 Å`
> * **选项**:
>     * $shift$
>     * 指定期望的位移量（单位为 Å）。
> * **建议**: 若将 VDWtype 设为 Shifted，则 vdW 缩放因子默认设为 1.0。可用 VDWScale 关键字加以调整。

将 **SoluteCavity** 关键字设为 **Spherical** 即请求在溶质周围构造球形空腔，并使用双曲正切函数将介电值从真空平滑插值到溶剂：[[267]](../bib_references/bib.md#bib267)

<a id="eq:hyperbolic"></a>

$$
\varepsilon(r)=\frac{1}{2}\Bigl{\{}(\varepsilon_{\mathrm{solvent}}+1)+(\varepsilon_{\mathrm{solvent}}-1)\ \mbox{tanh}\bigl{[}\alpha(r-r_{\mathrm{mid}})\bigr{]}\Bigr{\}}\;. \tag{11.44}
$$

这里，$r_{\mathrm{mid}}$ 是介电取值 $\varepsilon(r_{\mathrm{mid}})=(\varepsilon_{\mathrm{solvent}}+1)/2$ 处的距离。
$r_{\mathrm{mid}}$ 取为球半径 $R$ 与插值长度一半之和：$r_{\mathrm{mid}}=R+L/2$。
球半径与插值长度由下文所述的 **SphereRadius** 与 **InterpolLength** 关键字控制。
参数 $\alpha$ 控制过渡的陡峭程度，默认取 $\alpha=4/L$。

### `SphereRadius`

> **设置球形溶质空腔的半径。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `无默认值。`
> * **选项**:
>     * $R$
>     * 期望的球形空腔半径（单位为 Å）。
> * **建议**: 无。更多信息请参见文献 267 Coons M. P., You Z.-Q., Herbert J. M. J. Am. Chem. Soc. (2016) , 138 , pp. 10879 . Link 的补充材料（Supporting Information）。

### `InterpolLength`

> **设定介电值从真空平滑插值到溶剂的长度尺度。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `无默认值。`
> * **选项**:
>     * $L$
>     * 期望的插值长度（单位为 Å）。
> * **建议**: 无。

### `InterpolScale`

> **在给定的插值长度 ( $L$ ) 下，( $\alpha$ ) 设定介电值从真空到溶剂过渡的陡峭程度。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `$\alpha$`
> * **选项**:
>     * $\alpha$
>     * 期望的插值尺度因子（单位为 Å
>     * ${}^{-1}$
>     * ）。
> * **建议**: 使用默认值，除非希望过渡区域更宽（$\alpha$ 更小）或更窄（$\alpha$ 更大）。

### `Interface`

> **在溶剂/真空界面上进行溶剂化计算。输入区段：$peqs**
>
> * **类型**: `STRING`
> * **默认值**: `False`
> * **选项**:
>     * True
>     * 修改介电函数以模拟溶剂与真空之间的界面。
>     * False
>     * 在体相溶剂中进行溶剂化计算。
> * **建议**: 用户还需指定介电值从体相溶剂平滑插值到真空的长度尺度，以及 Gibbs 分界面（Gibbs dividing surface）的位置（见下文）。

将 **Interface** 设为 **True** 后，笛卡尔网格上的介电函数会被进一步修改以模拟溶剂/真空界面。首先，按上文所述由 **SoluteCavity** 关键字指定的方式构造溶质空腔。然后，利用下述双曲正切切换函数，在 $z$ 方向上跨越 Gibbs 分界面（$z\equiv z_{\mathrm{GDS}}$）对介电函数进行平滑插值：[[267]](../bib_references/bib.md#bib267)

<a id="eq:hyperbolic2"></a>

$$
\varepsilon(z)=\frac{1}{2}\Bigl{\{}(\varepsilon_{\rm solvent}+1)+(1-\varepsilon_{\rm solvent})\ \mbox{tanh}\bigl{[}\beta(z-z_{\mathrm{GDS}})\bigr{]}\Bigr{\}}\;. \tag{11.45}
$$

该式在界面长度 $L_{\rm interface}$ 上对介电函数进行插值，插值区间以 Gibbs 分界面 $z\equiv z_{\mathrm{GDS}}$ 为中心。
这两个数值分别由关键字 **InterfaceLength** 与 **GibbsDS** 控制。与球形空腔构造中使用的参数 $\alpha$ 类似，参数 $\beta=4/L_{\rm interface}$
控制跨越 Gibbs 分界面的插值陡峭程度。

### `InterfaceLength`

> **设定介电函数在 $z$ 方向上从体相溶剂平滑过渡到真空的长度尺度。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `None`
> * **选项**:
>     * $L_{\rm interface}$
>     * 期望的界面长度（单位为 Å）。
> * **建议**: 该值决定式 ( 11.45 ) 中的 $\beta=4/L_{\rm interface}$。关于溶剂/真空界面构造的完整描述，请参见文献 267 Coons M. P., You Z.-Q., Herbert J. M. J. Am. Chem. Soc. (2016) , 138 , pp. 10879 . Link 的补充材料。

### `GibbsDS`

> **设置在 $z$ 方向上 Gibbs 分界面的位置。输入区段：$peqs**
>
> * **类型**: `FLOAT`
> * **默认值**: `None`
> * **选项**:
>     * $z_{\mathrm{GDS}}$
>     * 期望的 Gibbs 分界面位置（单位为 Å）。
> * **建议**: 请参考文献。确定该数值的一种途径是计算溶剂密度随 $z$ 的分布曲线，并将此位置设为溶剂密度降至体相值 50% 之处。通常 $z_{\mathrm{GDS}}\approx L_{\rm interface}/2$。

### `NonequilJob`

> **求取竖直电离过程的溶剂化非平衡自由能。输入区段：$peqs**
>
> * **类型**: `STRING`
> * **默认值**: `False`
> * **选项**:
>     * True
>     * 计算竖直电离过程的非平衡自由能。
>     * False
>     * 计算平衡溶剂化自由能。
> * **建议**: 无。

### `NonequilPartition`

> **指定将溶剂响应划分为快分量与慢分量的方式。输入区段：$peqs**
>
> * **类型**: `STRING`
> * **默认值**: `Marcus`
> * **选项**:
>     * Marcus
>     * 采用 Marcus 划分方案。
>     * Pekar
>     * 采用 Pekar 划分方案。
> * **建议**: 使用默认值。尽管两种方法的快、慢溶剂化响应不同，但总溶剂化自由能相同，1530 You Z.-Q. et al. J. Chem. Phys. (2015) , 143 , pp. 204104 . Link 只是 Pekar 方案比 Marcus 方案的计算代价更高。

### `NonequilState`

> **指定非平衡竖直电离中关注的目标态。输入区段：$peqs**
>
> * **类型**: `STRING`
> * **默认值**: `Reference`
> * **选项**:
>     * Reference
>     * 参考（初始）态，将从中移去一个电子。
>     * Ionized
>     * 终态（电离态）。
> * **建议**: 无。在复合输入任务中两个数值都需要用到，以便计算对竖直电离的非平衡响应；参见示例 11.2.11.5。

最后，将 *$peqs* 输入区段中的 **SoluteCavity** 设为 **Arbitrary**，用户即可选择指定完全由用户自定义的介电函数 $\varepsilon(\mathbf{r})$，[[31]](../bib_references/bib.md#bib15)
 该函数必须在外部生成，并按点（pointwise）的方式在 PEqS 网格上通过输入文件中的 *$epsilon* 区段送入 **Q-Chem**。
该区段的格式为笛卡尔网格点 $(x_{i},y_{i},z_{i})$ 后跟 $\varepsilon(x_{i},y_{i},z_{i})$，如下所示。

```qchem
$epsilon
x1  y1  z1    eps(x1,y1,z1)
x1  y1  z2    eps(x1,y1,z2)
. . .
x1  y1  zNz   eps(z1,y1,zNz)
x1  y2  z1    eps(x1,y2,z1)
. . .
x1  y2  zNz   eps(z1,y2,zNz)
. . .
. . .
xNx  yNy  zNz    eps(xNx,yNy,zNz)
$end
```

## 11.2.11.5 示例

下例计算浸没在水中的水分子的溶剂化自由能。笛卡尔网格为立方体，边长 15.0 Å，每个方向有 73 个网格点。使用刚性 vdW 空腔，原子球半径基于缩放后的 vdW 半径。未指定介电常数，因此取默认值 78.39。

???+ example "示例 11.20: 水在水中的溶剂化自由能。"
    ```qchem
    $molecule
       0 1
       O     0.053004    -0.020947    -0.034784
       H     0.003424     0.185855     0.910594
       H    -0.844842     0.146674    -0.358413
    $end
    
    $rem
       EXCHANGE          wB97X-V
       BASIS             6-31+G*
       SCF_CONVERGENCE   5
       THRESH            14
       SOLVENT_METHOD    PEQS
       PEQS_SWITCH       0
    $end
    
    $peqs
       SOLUTECAVITY RIGIDVDW
    $end
    
    $peqs_grid
       DimX 73 -7.50 7.50
       DimY 73 -7.50 7.50
       DimZ 73 -7.50 7.50
    $end
    ```

下一示例演示位于水/真空界面处的水分子的溶剂化自由能计算，其中 Gibbs 分界面置于 $z=0.50$ Å 处。界面长度设为 $L_{\rm interface}=2.75$ Å，介电值沿正 $z$ 方向跨越 Gibbs 分界面从体相溶剂插值到真空。笛卡尔网格、溶质空腔以及溶剂介电常数均与上一示例相同。

???+ example "示例 11.21: 水分子在水/真空界面处的溶剂化自由能。"
    ```qchem
    $molecule
       0 1
       O     0.053004    -0.020947    -0.034784
       H     0.003424     0.185855     0.910594
       H    -0.844842     0.146674    -0.358413
    $end
    
    $rem
       SCF_CONVERGENCE   5
       THRESH            14
       EXCHANGE          wB97X-V
       BASIS             6-31+G*
       SOLVENT_METHOD    PEQS
       PEQS_SWITCH       0
    $end
    
    $peqs
       SOLUTECAVITY RIGIDVDW
       INTERFACE TRUE
       INTERFACELENGTH 2.75
       GIBBSDS 0.50
       INTERFACEDIRECTION POSITIVE
    $end
    
    $peqs_grid
       DimX 73 -7.50 7.50
       DimY 73 -7.50 7.50
       DimZ 73 -7.50 7.50
    $end
    ```

最后一个示例演示 $\rm H_{2}O^{-}$ 在体相水中竖直电离的非平衡（**NonEquilJob** = **True**）溶剂化计算。
这是一个复合任务：先计算阴离子态的平衡溶剂化自由能（**NonEquilState** = **Reference**），
再计算电离态的非平衡能量修正（**NonEquilState** = **Ionized**）。两个任务之间用
“`@@@`”分隔。笛卡尔网格与溶剂介电常数同前述示例相同，但溶质空腔选为球形，半径为 2.0 Å。
使用 Marcus 方案（**NonEquilPartition** = **Marcus**）将溶剂响应划分为快、慢分量。
由于这是默认方法，故省略 **NonEquilPartition** 关键字。

???+ example "示例 11.22: $\rm H_{2}O^{-}$ 竖直电离的溶剂化非平衡自由能"
    ```qchem
    $molecule
       -1 2
       O     0.053004    -0.020947    -0.034784
       H     0.003424     0.185855     0.910594
       H    -0.844842     0.146674    -0.358413
    $end
    
    $rem
       SCF_CONVERGENCE   5
       THRESH            14
       EXCHANGE          HF
       BASIS             6-31++G*
       SOLVENT_METHOD    PEQS
       PEQS_SWITCH       0
    $end
    
    $peqs
       SOLUTECAVITY   SPHERICAL
       SPHERERADIUS   2.00
       NONEQUILJOB    TRUE
       NONEQUILSTATE  REFERENCE
    $end
    
    $peqs_grid
       DimX 73 -7.50 7.50
       DimY 73 -7.50 7.50
       DimZ 73 -7.50 7.50
    $end
    
    @@@
    
    $molecule
       0 1
       O     0.053004    -0.020947    -0.034784
       H     0.003424     0.185855     0.910594
       H    -0.844842     0.146674    -0.358413
    $end
    
    $rem
       SCF_CONVERGENCE   5
       THRESH            14
       EXCHANGE          HF
       BASIS             6-31++G*
       SOLVENT_METHOD    PEQS
       PEQS_SWITCH       0
    $end
    
    $peqs
       SOLUTECAVITY   SPHERICAL
       SPHERERADIUS   2.00
       NONEQUILJOB    TRUE
       NONEQUILSTATE  IONIZED
    $end
    
    $peqs_grid
       DimX 73 -7.50 7.50
       DimY 73 -7.50 7.50
       DimZ 73 -7.50 7.50
    $end
    ```
