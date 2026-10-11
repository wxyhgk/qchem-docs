---
title: "9.9.2 概述与基本任务控制"
---

## 9.9.2 概述与基本任务控制

(July 4, 2026)

必须为原子核指定初始的笛卡尔坐标和速度。坐标按照惯例在 *$molecule* 段中指定，
而速度可以通过 *$velocity* 段来指定，其形式为：

> `$velocity` 
> 
> 
> $v_{x,1}~{}~{}~{}v_{y,1}~{}~{}~{}v_{z,1}$ 
> 
> 
> $v_{x,2}~{}~{}~{}v_{y,2}~{}~{}~{}v_{z,2}$ 
> 
> 
> $v_{x,N}~{}~{}~{}v_{y,N}~{}~{}~{}v_{z,N}$ 
> 
> 
> `$end`

这里 $v_{x,i}$、$v_{y,i}$ 和 $v_{z,i}$ 分别是第 $i$ 个原子核的 $x$、$y$、$z$
笛卡尔速度，以原子单位给出（bohr 每原子时间单位，其中 1 a.u. 时间约等于
0.0242 fs）。因此 *$velocity* 段与 *$molecule* 段形式相同，
只是不含原子符号，也不含指定电荷与自旋多重度的那一行。
在 *$velocity* 和 *$molecule* 两个段中，原子的排列顺序必须完全一致。

作为 *$velocity* 段的替代方案，初始核速度可以从某些分布（*e.g.*，麦克斯韦-玻尔兹曼分布，
Maxwell-Boltzmann）中抽样获得，这通过下文描述的 AIMD_INIT_VELOC 变量来实现。
AIMD_INIT_VELOC 还可以设置为 QUASICLASSICAL，
这将触发使用经典轨迹分子动力学（quasi-classical trajectory molecular dynamics，见
第 [9.9.6](subsec_QCT.md) 节）。

原子核质量可以通过形式如下的 *$mass* 段来初始化：

> `$mass` 
> 
> 
> $m_{1}~{}~{}~{}m_{2}$ 
> 
> 
> $m_{3}~{}~{}~{}$ ! mass of 3rd atom 
> 
> 
> $m_{4}$ 
> 
> 
> `$end`

*$mass* 段中数值的总数必须等于原子个数。单位为原子质量单位（amu），*e.g.*，
氢-1 原子的质量为 1.00783。若未初始化 *$mass* 段，则使用默认质量。

尽管 **Q-Chem** 输出文件会如实记录从头算分子动力学（*ab initio* molecular dynamics）
任务的进展，但最有用的信息并非打印在主输出文件中，而是打印在一个名为 “AIMD” 的
目录中，该目录是任务临时（scratch）目录下的子目录。（因此所有从头算分子动力学
任务都应使用第 [2.2](../ch02_install/sect_running.md) 节中描述的 *–save* 选项。）
AIMD 目录由一组文件构成，这些文件以 ASCII 格式记录每个时间步的一行信息。
每个文件包含若干以 “#” 标识的注释行，用于描述其内容，我们在下文中汇总列出。

- •

`Cost`：记录每个动力学步的 SCF 循环次数、总 CPU 时间以及总内存使用量。
- •

`EComponents`：记录总能的各种组成部分（均以 hartree 为单位）。
- •

`Energy`：记录总能量及其涨落。
- •

`MulMoments`：若请求了多极矩（multipole moments），则输出到此文件。
- •

`NucCarts`：记录每个时间步的核笛卡尔坐标 $x_{1}$，$y_{1}$，
$z_{1}$，$x_{2}$，$y_{2}$，$z_{2}$，…，$x_{N}$，$y_{N}$，$z_{N}$，
单位为 bohr 或埃（Ångstroms）。
- •

`NucForces`：记录每个时间步作用在原子核上的笛卡尔力
（顺序与坐标相同，但以原子单位给出）。
- •

`NucVeloc`：记录每个时间步原子核的笛卡尔速度
（顺序与坐标相同，但以原子单位给出）。
- •

`TandV`：记录动能与势能，以及各自的涨落。
- •

`View.xyz`：`NucCarts` 的笛卡尔格式版本，
用于在外部可视化程序中查看轨迹。

对于 ELMD 任务，还有其他一些输出文件：

- •

`ChangeInF`：记录在 Cholesky 正交化原子轨道（AO）基下
$\Delta\mathbf{F}=\mathbf{F}(t+\delta t)-\mathbf{F}(t)$ 的矩阵范数及最大元素模。
文件 ChangeInP、ChangeInL 和 ChangeInZ 分别为密度矩阵 $\mathbf{P}$
以及在文献 [[558]](../bib_references/bib.md#bib572)
中定义的 Cholesky 正交化矩阵 $\mathbf{L}$ 和 $\mathbf{Z}$ 提供类似信息。
- •

`DeltaNorm`：记录文献 [[558]](../bib_references/bib.md#bib572)
中定义的曲步（curvy-steps）旋转角矩阵 $\Delta$ 的范数及最大元素模。
$\Delta$ 的矩阵元是代表电子自由度的动力学变量。
输出文件 DeltaDotNorm 为电子速度矩阵 $d\Delta/{dt}$ 提供相同的信息。
- •

`ElecGradNorm`：记录 Cholesky 基下电子梯度矩阵 $\mathbf{FP}-\mathbf{PF}$
的范数及最大元素模。
- •

`dTfict:`：记录每个时间步虚拟动能（fictitious kinetic energy）的瞬时时间导数，
以原子单位给出。

通过将 JOBTYPE = AIMD 进行指定来请求从头算分子动力学任务。
初始速度必须通过 *$velocity* 段或下文描述的 AIMD_INIT_VELOC 关键字来指定。
此外，任何从头算分子动力学任务都必须指定以下 *$rem* 变量：

AIMD_METHOD

### `AIMD_METHOD`

> **选择从头算分子动力学算法。**
>
> * **类型**: `STRING`
> * **默认值**: `BOMD`
> * **选项**:
>     * BOMD
>     * 玻恩-奥本海默分子动力学（Born-Oppenheimer molecular dynamics）。
>     * CURVY
>     * 曲步扩展拉格朗日分子动力学（Curvy-steps Extended Lagrangian molecular dynamics）。
>     * QCMD
>     * Meyer-Miller 非绝热分子动力学（Meyer-Miller nonadiabatic molecular dynamics）。
> * **建议**: BOMD 在能量守恒可接受的条件下产生精确的经典分子动力学。ELMD 是对精确经典动力学的一种近似，其有效性应针对所关心的性质进行检验。QCMD 启动 Meyer-Miller 非绝热动力学方法，包括对称经典方法（symmetric quasiclassical approach）或传统的 Ehrenfest 方法。

TIME_STEP

### `TIME_STEP`

> **以原子单位指定分子动力学的时间步长（1 a.u. = 0.0242 fs）。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None.`
> * **选项**:
>     * 由用户指定。
> * **建议**: 较小的时间步长带来更好的能量守恒；时间步长过大可能导致任务完全失败。在能量守恒可接受的前提下，尽可能增大时间步长。

AIMD_TIME_STEP_CONVERSION

### `AIMD_TIME_STEP_CONVERSION`

> **修改分子动力学的时间步长以提高粒度。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * $n$
>     * 分子动力学时间步长为
>     * TIME_STEP
>     * /
>     * $n$
>     * a.u.
> * **建议**: 无

AIMD_STEPS

### `AIMD_STEPS`

> **指定所请求的分子动力学步数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None.`
> * **选项**:
>     * 由用户指定。
> * **建议**: 无。

从头算分子动力学计算可能非常昂贵，因此 **Q-Chem** 包含若干旨在加速此类计算的算法。
在自洽场（self-consistent field，SCF，即 Hartree-Fock 与密度泛函理论（Density
Functional Theory, DFT））层面，利用先前时间步的信息为新分子轨道或 Fock 矩阵构造
良好的初始猜测，从而加速 SCF 收敛，可以大幅加快 BOMD 计算。
为此提供了基于 Pulay 和 Fogarasi 建议[[1135]](../bib_references/bib.md#bib1185)
的 Fock 矩阵外推（extrapolation）过程[[559]](../bib_references/bib.md#bib573)。

原子轨道基下的 Fock 矩阵元 $F_{\mu\nu}$ 是关于时间 $t$ 的振荡函数，
**Q-Chem** 的外推过程将这些振荡拟合为 $t$ 的幂级数：

<a id="Ch9.E61"></a>
$$
F_{\mu\nu}(t)=\sum\limits_{n=0}^{N}{c_{n}\,}t^{n} \tag{9.61}
$$

$N+1$ 个外推系数 $c_{n}$ 由对从前几个时间步保留的 $M$ 个 Fock 矩阵集合的拟合确定。
Fock 矩阵外推可以显著减少每个时间步所需的 SCF 迭代次数，但对于低阶外推，
或者当 SCF_CONVERGENCE 设置过小时，可能会观察到总能量的系统性漂移。
测试能量守恒极限的基准计算可见文献 [[559]](../bib_references/bib.md#bib573)，
结果表明在显著降低成本的同时可以获得数值上精确的经典动力学（无能量漂移）。

通过为 $N$ 和 $M$ 指定数值来请求 Fock 矩阵外推，形式为以下两个 *$rem* 变量：

FOCK_EXTRAP_ORDER

### `FOCK_EXTRAP_ORDER`

> **指定 Fock 矩阵外推的多项式阶数 $N$。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $N$
>     * 使用
>     * $N$
>     * 阶多项式进行外推（
>     * $N>0$
>     * ）。
> * **建议**: 无

FOCK_EXTRAP_POINTS

### `FOCK_EXTRAP_POINTS`

> **指定为外推而保留的旧 Fock 矩阵数目 $M$。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $M$
>     * 保存
>     * $M$
>     * 个 Fock 矩阵用于外推
>     * $(M>N)$
> * **建议**: 到一定程度为止，保留更多 Fock 矩阵的高阶外推比低阶外推更快且能量守恒更好。在许多情况下，方案（$N$ = 6，$M$ = 12）配合 SCF_CONVERGENCE = 6，可在保持能量守恒的同时节省约 50% 的计算成本。

当使用轨道未经优化的底层电子结构方法（如 MP2）计算核力时，
必须求解一组响应方程（response equations）[[29]](../bib_references/bib.md#bib13)。
虽然这些方程是线性的，但其维数决定了需要采用迭代求解
[[1115]](../bib_references/bib.md#bib1161)，
在实践中其形式与 SCF 方程十分相似。这里外推同样有用
[[1304]](../bib_references/bib.md#bib1360)，
且 $Z$ 矢量（响应）外推的语法与 Fock 外推类似。

Z_EXTRAP_ORDER

### `Z_EXTRAP_ORDER`

> **指定 $Z$ 矢量外推的多项式阶数 $N$。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $N$
>     * 使用
>     * $N$
>     * 阶多项式进行外推（
>     * $N>0$
>     * ）。
> * **建议**: 无

Z_EXTRAP_POINTS

### `Z_EXTRAP_POINTS`

> **指定为外推而保留的旧 $Z$ 矢量数目 $M$。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * $M$
>     * 保存
>     * $M$
>     * 个先前的
>     * $Z$
>     * 矢量用于外推
>     * $(M>N)$
> * **建议**: 在使用默认 $Z$ 矢量收敛设置的情况下，$(M,N)=(4,2)$ 外推被证明能提供最大的加速。在该设置下，迭代次数可减少 2–3 倍。

假设能量守恒良好，BOMD 计算代表在玻恩-奥本海默（Born-Oppenheimer）势能面上的
精确经典动力学。与之相对，所谓的扩展拉格朗日分子动力学（extended Lagrangian
molecular dynamics，ELMD）方法为了加快计算而对精确经典动力学做出近似。
ELMD 方法（其中最著名的是 Car–Parrinello 分子动力学）为电子（轨道）自由度
引入虚拟动力学（fictitious dynamics），这些自由度与核自由度一起被*传播*
（propagated），而不是像在 BOMD 计算中那样在每个时间步被*优化*。
虚拟电子动力学由虚拟质量参数 $\mu$ 控制，$\mu$ 的取值同时影响方法的
精度与效率。在 $\mu$ 很小的极限下，核与轨道绝热地传播，ELMD
模仿真实的经典动力学。较大的 $\mu$ 值会减慢电子动力学，
允许使用更大的时间步长（从而动力学在计算上更高效），
代价是对真实经典动力学的近似程度不断加大。

**Q-Chem** 的 ELMD 算法基于将密度矩阵（在以原子为中心的高斯轨道基下表示）
沿允许密度矩阵流形 $\mathbf{P}$ 的最短距离路径（测地线，geodesics）进行传播。
$\mathbf{P}$ 的幂等性（idempotency）在构造上于每个时间步都得以保持，
因此我们的算法既不需要密度矩阵纯化（purification），也不需要求解
拉格朗日乘子（Lagrange multipliers）的迭代过程（以强制分子轨道的正交性）。
我们将此过程称为“曲步”（curvy steps）ELMD[[558]](../bib_references/bib.md#bib572)，
从某种意义上说，它是用于收敛 SCF 单点计算的 GDM 算法
（第 [4.5](../ch04_scf/sect_convergence.md) 节）的含时实现。

ELMD 在多大程度上构成对 BOMD 的重大近似，目前仍有争论。在评估 ELMD 的精度时，
首要考虑的是核振荡与电子振荡之间是否存在时间尺度的分离：核振荡的时间尺度
$\tau_{\mathrm{nuc}}$ 由最快振动频率的周期决定，而电子振荡的时间尺度
$\tau_{\mathrm{elec}}$ 可根据[[558]](../bib_references/bib.md#bib572)估计为

<a id="Ch9.E62"></a>
$$
\tau_{\mathrm{elec}}\geq\left(\frac{\mu}{\varepsilon_{\rm LUMO}-\varepsilon_{\rm HOMO}}\right)^{1/2} \tag{9.62}
$$

文献 [[558]](../bib_references/bib.md#bib572)
中给出的保守估计是，当 $\tau_{\mathrm{nuc}}>$ 10
$\tau_{\mathrm{elec}}$ 时即可达到本质精确的经典动力学。在实践中，
我们建议进行细致的基准测试，以确保 ELMD 能忠实重现所关心的 BOMD 可观测量。

由于存在快速时间尺度 $\tau_{\mathrm{elec}}$，ELMD 需要比 BOMD 更小的时间步长。
当 BOMD 与 Fock 矩阵外推相结合以加速收敛时，至少在高斯基组中，
ELMD 方法是否明显更高效已不再清楚[[559]](../bib_references/bib.md#bib573)。

ELMD 任务需要以下 *$rem* 变量：

AIMD_FICT_MASS

### `AIMD_FICT_MASS`

> **以原子单位指定虚拟电子质量 $\mu$ 的值，其中 $\mu$ 的量纲为（能量）$\times$（时间）${}^{2}$。**
>
> * **类型**: `INTEGER`
> * **默认值**: `None`
> * **选项**:
>     * 由用户指定
> * **建议**: 在测试计算中使用了 50–200 a.u. 范围内的值；相关示例与讨论参见文献 558 Herbert J. M., Head-Gordon M. J. Chem. Phys. (2004), 121, pp. 11542. Link。

AIMD_PRINT

### `AIMD_PRINT`

> **指定 AIMD 输出的详细程度。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * 由用户指定
> * **建议**: 数值越大，输出越详细。
