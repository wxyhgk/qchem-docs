---
title: "9.10.1 理论"
---

## 9.10.1 理论

（2026 年 7 月 4 日）

即使在玻恩-奥本海默（Born-Oppenheimer）分离成立的情况下，求解电子薛定谔方程（electronic Schrödinger equation）也可能只完成了一半的工作。另一半则是求解*核*薛定谔方程，以获得相应的本征值（eigenvalues）与本征函数（eigenfunctions）。这一半通常在临界点处采用谐振子近似（harmonic approximation）来处理，但非谐性（anharmonicity）、隧穿效应（tunneling）以及低频（"柔性"，floppy）运动可能导致极度离域的核分布，尤其对于质子和非共价相互作用而言更是如此。

虽然玻恩-奥本海默分离使得电子问题可以在（核空间中的）每一点上局部求解，但薛定谔方程的核部分却是完全非局域的，需要在构型空间的广阔区域内计算势能面（potential energy surfaces）。因此，基于网格（Grid-based）的方法其计算量随自由度数目呈指数增长，除极小分子外很快便无能为力。

对于平衡态热分布，路径积分（path integral, PI）形式体系提供了一种既优雅又在计算上可行的替代方案。平衡态配分函数（partition function）可以写成热构型空间密度矩阵的迹，

<a id="eq:primitive_Z"></a>

$$
Z=\mbox{tr}\bigl{(}e^{-\beta\hat{H}}\bigr{)}=\int dx\;\bigl{\langle}x\bigl{|}e^{-\beta\hat{H}}\bigr{|}x\bigr{\rangle}=\int dx\;\rho(x,x;\beta)\;. \tag{9.66}
$$

密度矩阵在逆温度 $\beta=(k_{B}T)^{-1}$ 下由最后一个等式定义。计算式 ([9.66](#eq:primitive_Z)) 中的积分仍然需要求解 $\hat{H}$ 的本征态，而这通常是难以处理的。然而，若插入 $N-1$ 个恒等式的完备展开，则可得

<a id="Ch9.E67"></a>

$$
Z=\int dx_{1}\int dx_{2}\cdots\int dx_{N}\ \rho\left(x_{1},x_{2};\frac{\beta}{N}\right)\rho\left(x_{2},x_{3};\frac{\beta}{N}\right)\cdots\rho\left(x_{N},x_{1};\frac{\beta}{N}\right)\;. \tag{9.67}
$$

此处，密度矩阵所对应的逆温度为 $\beta/N$，相当于将实际温度 $T$ 乘以因子 $N$。

密度矩阵的高温形式可以表示为

<a id="Ch9.E68"></a>

$$
\rho\left(x,x^{\prime};\frac{\beta}{N}\right)=\left(\frac{mN}{2\pi\beta\hbar^{2}}\right)^{\!1/2}\exp\left\{-\left(\frac{mN}{2\beta\hbar^{2}}\right)(x-x^{\prime})^{2}-\left(\frac{\beta}{2N}\right)\Bigl{[}V(x)+V(x^{\prime})\Bigr{]}\right\} \tag{9.68}
$$

当 $T\rightarrow\infty$（即量子力学收敛于经典力学的极限）时，该式变为精确；换言之，当 $\beta\rightarrow 0$ 或 $N\rightarrow\infty$ 时亦然。利用 $N$ 个时间切片，配分函数因此被转化为如下形式

<a id="eq:PI_partition_fn"></a>

$$
Z=\left(\frac{mN}{2\pi\beta\hbar^{2}}\right)^{\!N/2}\int dx_{1}\int dx_{2}\cdots\int dx_{N}\;\exp\left\{-\frac{\beta}{N}\left[\frac{mN^{2}}{2\beta^{2}\hbar^{2}}\sum_{i=1}^{N}\left(x_{i}-x_{i+1}\right)^{2}+\sum_{i=1}^{N}V(x_{i})\right]\right\}\;, \tag{9.69}
$$

其中隐含了循环条件 $x_{N+1}\equiv x_{1}$。这里的 $V(x)$ 是"珠粒"（beads）在其上运动的势函数，即由 **Q-Chem** 所产生的电子势。

式 [9.69](#eq:PI_partition_fn) 具有如下形式

<a id="eq:PI_equiv_to_classical"></a>

$$
Z\propto\int e^{-\beta V_{\rm eff}}\;, \tag{9.70}
$$

其中有效势 $V_{\rm eff}$ 的形式可由式 ([9.69](#eq:PI_partition_fn)) 的被积函数看出。式 ([9.70](#eq:PI_equiv_to_classical)) 表明，量子配分函数的路径积分表述为配分函数提供了一个*经典*的构型积分，尽管是在一个扩展维空间中。该有效势描述了一个具有 $N$ 个珠粒的经典"环聚合物"（ring polymer），其中相邻珠粒通过来自动能量子特性的谐振势相耦合。因此，这个呈指数扩展的非局域核量子力学问题被映射为一个完全经典的问题，从而可以采用标准的构型采样方法来处理。这些方法通常涉及分子动力学（molecular dynamics）或蒙特卡洛（Monte Carlo）采样。重要的是，当温度不是过低时，扩展自由度的数目 $N$ 可以相当小：涉及氢原子的室温体系通常使用大约 $N\approx 30$ 个珠粒即可收敛。因此，可以在大约仅为经典从头算分子动力学（AIMD）模拟 30 倍的代价下获得完全量子力学的核分布。通过将 JOBTYPE 设置为 PIMC 来启用路径积分蒙特卡洛（Path Integral Monte Carlo, PIMC）。

上述方程的单珠粒（$N=1$）极限就是经典的构型采样。当温度（由 PIMC_TEMP 关键字控制）较高，或只涉及较重原子时，经典极限通常是合适的。可以使用路径积分机制（配合单个"珠粒"）来执行经典玻尔兹曼采样。此时，配分函数就变为如下简单的形式

<a id="Ch9.E71"></a>

$$
Z=\int dx\ e^{-\beta V(x)} \tag{9.71}
$$

这正是 AIMD 模拟中所通常执行的操作。使用更多珠粒会引入更多的量子离域效应，代价约为经典 AIMD 模拟的 $N$ 倍，而这正是 PI 模拟中的主要输入变量。该变量由关键字 PIMC_NBEADSPERATOM 控制。逆温度与珠粒数之比（$\beta/N$）决定了关于珠粒数目的收敛性，因此当温度降低时，需要相应地增加珠粒数目。

对构型空间的积分通过 Metropolis 蒙特卡洛（MC）方法执行。MC 步数由 PIMC_MCMAX 关键字控制，通常应 $\gtrsim 10^{5}$，具体取决于所需的统计收敛程度。可以使用 PIMC_WARMUP_MCMAX 关键字执行预热运行（warm-up run），在此过程中让 PI 环聚合物在不累积统计的情况下达到平衡。

与 AIMD 模拟类似，**Q-Chem** 中 PIMC 任务的主要结果并不在任务输出文件中，而是输出到（用户暂存目录下的 `$QCSCRATCH/PIMC`，因此 PIMC 任务应始终带 *-save* 选项运行。不过，输出文件确实包含一些有用的信息，包括对模拟的基本数据分析。平均能量（热力学估计器）、键长（小于 5 Å）、键长标准差及误差会在输出文件末尾打印。`$QCSCRATCH/PIMC` 目录还包含以下文件：

- `BondAves`：键长的滑动平均，用于收敛测试。
- `BondBins`：显著键长的归一化分布，以平均键长的 5 倍标准差范围内分箱。
- `ChainCarts`：可读的构型坐标文件，可能用于进一步的外部统计分析。该文件可能变得相当大，因此务必提供充足的暂存空间！
- `ChainView.xyz`：Cartesian 格式的文件，用于在外部可视化程序中查看环聚合物的采样情况。（采样过程保证环聚合物体系的质心保持居中。）
- `Vcorr`：势关联函数，用于评估采样中的统计相关性。

在上述每个文件中，前几行都包含对数据排列方式的说明。

在使用 PIMC 过程中，一个不幸的"必经之路"便是认识到：当逼近关于 $N$ 的收敛时，僵硬的珠粒-珠粒相互作用会带来严重后果。接近收敛（即量子力学结果正确）时，统计相关性的长度会急剧增长，需要采用特殊的采样技术以避免冗长（或不收敛）的模拟。环聚合物的笛卡尔位移或简正模式（normal-mode）位移都会导致这种严重的僵硬化。虽然这两种朴素的采样方案在 **Q-Chem** 中都可用，但并不推荐使用。相反，可以直接对路径积分作用量中的自由粒子（谐振珠粒耦合）项进行采样。为此有若干方案可用。**Q-Chem** 目前采用了其中最简单的方案，即 Levy 飞行（Levy flights）。随机选取环聚合物的一段 $n$ 个珠粒（$n<N$），其长度 $n$ 由 PIMC_SNIP_LENGTH 关键字控制。在该片段的两端点之间，通过 Levy 构造生成一条自由粒子路径，它*精确地*对作用量中的自由粒子部分进行采样。随后对由此产生的势项进行 Metropolis 检验（只需要被移动珠粒上的势值），从而决定是否接受。

任务输出文件中提供了两项衡量采样效率的指标。势自关联函数 $\langle V_{0}V_{\tau}\rangle$ 的寿命以 MC 步数 $\tau$ 表示。该数值指示了相互统计关联的构型数目。类似地，还给出了相邻 MC 构型之间的均方位移。最大化该数值和/或最小化统计寿命即可实现高效采样。请注意，在 MC 模拟中，最优高效的接受率可能*并非* 50%。在 Levy 飞行中，唯一控制接受率与采样效率的变量是片段的长度。采样效率可以在相对较短的运行中获得，期间由用户对 Levy 片段长度进行优化。
