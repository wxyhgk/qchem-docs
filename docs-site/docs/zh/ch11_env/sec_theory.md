---
title: "11.5.2 理论背景"
---

## 11.5.2 理论背景

（2026 年 7 月 4 日）

体系的总能量由有效碎片（effective fragments）之间的相互作用能（$E^{\text{ef-ef}}$）以及 *ab initio*（即量子力学，QM）区域在碎片场中的能量两部分组成。前者包含静电、极化、色散和交换排斥贡献项（荷电转移项——对于描述离子型和强极性体系可能很重要——在当前的实现中被忽略）：

<a id="Ch11.E61"></a>

$$
E^{\text{ef-ef}}=E_{\text{elec}}+E_{\text{pol}}+E_{\text{disp}}+E_{\text{ex-rep}}\;. \tag{11.61}
$$

QM-EF 相互作用的计算方式如下。EFP 势能的静电（Coulomb）部分和极化部分通过单电子项贡献到量子哈密顿量中，

<a id="eq:H-EFP"></a>

$$
H^{\prime}_{pq}=H_{pq}+\langle p|\hat{V}^{\text{Coul}}+\hat{V}^{\text{pol}}|q\rangle \tag{11.62}
$$

而色散和交换排斥的 QM-EF 相互作用则作为总能量的加和校正项来处理。

EFP 能量的静电组分描述 Coulomb 相互作用。对于含氢键或极性分子的体系，这是分子间总相互作用能的主导贡献。[[169]](../bib_references/bib.md#bib163)
 通过对原子中心和键中点（即电子密度较高的点）进行多极展开（源自 Stone 的分布式多极分析），并将该展开截断至八极（octupole）项，可以得到对静电势的精确描述。[[1316]](../bib_references/bib.md#bib1372)
 碎片-碎片静电相互作用由电荷–电荷、电荷–偶极、电荷–四极、电荷–八极、偶极–偶极、偶极–四极以及四极–四极项组成，还包括电子多极与原子核之间的相互作用项以及核排斥能。

当碎片间距过近时，碎片静电密度的多极表示会失效。由于电子密度的显著重叠以及电荷穿透（charge-penetration）效应，多极相互作用会变得过于排斥。在极性体系中，电荷穿透效应的量级通常约为静电总能量的 15%，但在静电相互作用较弱的体系中可高达 200%。[[1270]](../bib_references/bib.md#bib1323)
 为了解释电荷穿透效应，对电荷-电荷项采用简单的指数阻尼。[[406]](../bib_references/bib.md#bib415)
 展开点 $k$ 与 $l$ 之间经屏蔽（screened）的电荷-电荷能量由下式给出，其中 $\alpha_{k}$ 和 $\alpha_{l}$ 是与相应展开点关联的阻尼参数：

<a id="eq:EFP-elec-damp"></a>

$$
E^{\text{ch-ch}}_{kl}=\begin{cases}\left[1-(1+\alpha_{k}R_{kl}/2)e^{-\alpha_{k}R_{kl}}\right]\frac{q^{k}q^{l}}{R_{kl}}&\text{if $\alpha_{k}=\alpha_{l}$}\\
\left[1-\left({\alpha_{l}^{2}\over\alpha_{l}^{2}-\alpha_{k}^{2}}\right)e^{-\alpha_{k}R_{kl}}-\left({\alpha_{k}^{2}\over\alpha_{k}^{2}-\alpha_{l}^{2}}\right)e^{-\alpha_{l}R_{kl}}\right]\frac{q^{k}q^{l}}{R_{kl}}&\text{if $\alpha_{k}\neq\alpha_{l}$}\\
\end{cases}\;. \tag{11.63}
$$

或者，也可以用球面高斯重叠（spherical Gaussian overlap，SGO）近似来获得短程电荷穿透能：[[1271]](../bib_references/bib.md#bib1324)

<a id="eq:overlap-damping"></a>

$$
E^{\text{pen}}_{kl}=-2\left({1\over{-2ln|S_{kl}|}}\right)^{1/2}\frac{S^{2}_{kl}}{R_{kl}} \tag{11.64}
$$

其中 $S_{kl}$ 是定域分子轨道（LMO）$k$ 与 $l$ 之间的重叠积分，按交换排斥项（式 ([11.76](#eq:ex_rep))）计算。该电荷穿透能独立于其余静电能分别计算并输出。基于重叠的阻尼通常能对分子间相互作用给出更均衡的描述，因此推荐使用；仅在短程排斥相互作用是研究对象的场合可能例外。[[198]](../bib_references/bib.md#bib195)

有效碎片与 QM 部分之间的静电相互作用通过 *ab initio* 哈密顿量的微扰 $\hat{V}^{\text{Coul}}$ 来描述[参见式 ([11.62](#eq:H-EFP))]。该微扰以有效碎片各展开点贡献之和的形式进入哈密顿量的单电子部分。每个展开点的贡献由四项组成，分别源自相应多极（电荷、偶极、四极和八极）的静电势：

<a id="eq:QM-EFP-elec"></a>

$$
V^{\text{Coul}}_{k}(x)=q_{k}T(r_{kx})-\sum^{x,y,z}_{a}\mu^{k}_{a}T_{a}(r_{kx})+\frac{1}{3}\sum^{x,y,z}_{ab}\Theta^{k}_{ab}T_{ab}(r_{kx})-\frac{1}{15}\sum^{x,y,z}_{abc}\Omega^{k}_{abc}T_{abc}(r_{kx})\;, \tag{11.65}
$$

其中 $q$、$\mu$、$\Theta$ 和 $\Omega$ 分别是位于多极展开点 $k$（所有原子和键中点）的净电荷、偶极、四极和八极。
$T$ 是零阶至三阶的静电张量。
QM 电子密度与多极电荷的相互作用还可以辅以高斯型阻尼函数，[[504]](../bib_references/bib.md#bib517)
 此时式 ([11.65](#eq:QM-EFP-elec)) 变为

<a id="A3.S8.EGx106"></a>

$$
\displaystyle\begin{aligned} \displaystyle V^{\text{Coul}}_{k}(x)=\big{[}q_{k}^{\text{nuc}}+q_{k}^{\text{ele}}(1-\exp{(-\beta_{k}r^{2}_{kx})}\big{]}T(r_{kx})&\displaystyle-\sum^{x,y,z}_{a}\mu^{k}_{a}\;T_{a}(r_{kx})+\frac{1}{3}\sum^{x,y,z}_{ab}\Theta^{k}_{ab}\;T_{ab}(r_{kx})\\
&\displaystyle-\frac{1}{15}\sum^{x,y,z}_{abc}\Omega^{k}_{abc}\;T_{abc}(r_{kx})\;,\end{aligned} \tag{11.66}
$$

其中 $q_{k}^{\text{nuc}}$ 是原子核电荷，$q_{k}^{\text{ele}}$ 是多极点 $k$ 上的电子电荷。因此，只有电子电荷会被高斯函数阻尼（涂抹）。
式 ([11.63](#eq:EFP-elec-damp)) 和 ([11.66](#eq:QM-EFP-elec-damp)) 中的阻尼参数 $\alpha$ 和 $\beta$ 是这样确定的：在每个碎片的参数生成计算（parameter-generating calculation）中，最小化经阻尼的多极展开静电势与电子波函数产生的静电势之间的差异。
（参见第 [11.5.9](sec_makefp.md) 节。）

极化描述分子内部电荷对外部电场的响应再分布。它是导致分子协同行为的多体相互作用的主要成分。EFP 采用置于价层 LMO 中心的分布式极化率。与各向同性的分子总极化率张量不同，分布式极化率张量是各向异性的。

由 *ab initio* 区域和有效碎片区域组成的体系，其极化能为[[309]](../bib_references/bib.md#bib314)

<a id="eq:pol_energy"></a>

$$
E^{\text{pol}}=-\frac{1}{2}\sum_{k}\sum^{x,y,z}_{a}\mu^{k}_{a}\big{(}F^{\text{mult},k}_{a}+F^{\text{ai,nuc},k}_{a}\big{)}+\frac{1}{2}\sum_{k}\sum^{x,y,z}_{a}\bar{\mu}^{k}_{a}\;F^{\text{ai,elec},k}_{a} \tag{11.67}
$$

其中 $\mu^{k}$ 和 $\bar{\mu}^{k}$ 分别是分布式点 $k$ 上的感应偶极和共轭感应偶极；$F^{\text{mult},k}$ 是其他碎片的静态多极和原子核产生的外电场，$F^{\text{ai,elec},k}$ 和 $F^{\text{ai,nuc},k}$ 则分别是 *ab initio* 部分的电子密度和原子核产生的电场。

每个极化率点 $k$ 上的感应偶极按下式计算

<a id="eq:ind_dip"></a>

$$
\mu^{k}=\alpha^{k}F^{\text{total},k} \tag{11.68}
$$

其中 $\alpha^{k}$ 是 $k$ 处的分布式极化率张量。
总电场由静态电场、其他感应偶极产生的电场 $F^{\text{ind}}_{k}$，以及 *ab initio* 区域的原子核和电子密度产生的电场共同组成：

<a id="eq:pol_total_field"></a>

$$
F^{\text{ai,total},k}=F^{\text{mult},k}+F^{\text{ind},k}+F^{\text{ai,elec},k}+F^{\text{ai,nuc},k}\;. \tag{11.69}
$$

由上式可见，某一特定碎片上的感应偶极取决于所有其他碎片感应偶极的取值。
此外，有效碎片上的感应偶极取决于 *ab initio* 电子密度，而 *ab initio* 电子密度反过来又受到这些感应偶极通过哈密顿量的单电子贡献所产生的电场的影响：

<a id="eq:hamilt_pol"></a>

$$
\hat{V}^{\text{pol}}_{k}(x)=\frac{1}{2}\sum_{a}^{x,y,z}\big{(}\mu_{a}^{k}+\bar{\mu}_{a}^{k}\big{)}\;T_{a}(r_{kx}) \tag{11.70}
$$

其中 $k$ 为极化率展开点。总极化贡献采用双层迭代程序自洽地计算。外层与内层迭代的目标分别是收敛波函数，以及在给定固定波函数下收敛感应偶极。当不存在 *ab initio* 区域时，对 EF 体系的感应偶极进行迭代直至彼此自洽。

对极化的自洽处理计入了多体相互作用效应。EFP 碎片之间的极化能用默认参数为 $\alpha=\beta=0.6$ 的高斯型阻尼函数加以增强，该阻尼函数作用于电场 $F$ 上：[[1271]](../bib_references/bib.md#bib1324)

<a id="eq:pol_damp_1"></a>

$$
F=F_{0}f^{\mathrm{damp}} \tag{11.71}
$$

<a id="eq:pol_damp_2"></a>

$$
f^{\text{damp}}=1.0-\big{(}1+\sqrt{\alpha\beta}r^{2}\big{)}e^{-(\alpha\beta)^{1/2}r^{2}} \tag{11.72}
$$

色散是范德华（van der Waals）相互作用和 $\pi$-堆积相互作用的主导贡献，[[197]](../bib_references/bib.md#bib190)
 其最低阶贡献为

<a id="eq:disp_basic"></a>

$$
E^{\text{disp}}=\sum_{n}\frac{C_{6}}{R^{6}} \tag{11.73}
$$

其中系数 $C_{6}$ 由频域分布式极化率导出，其展开点位于 LMO 质心，即与极化展开点位于相同的中心。更高阶的色散项（感应偶极-感应四极、感应四极/感应四极等）近似取为 $C_{6}$ 项的 $1/3$。[[21]](../bib_references/bib.md#bib5)

当有效碎片间距较小时，色散相互作用需对电荷穿透和电子密度重叠效应进行校正，校正方式可采用参数 $b=1.5$ 的 Tang-Toennies 阻尼公式[[1342]](../bib_references/bib.md#bib1400)

<a id="eq:disp_TT_damp"></a>

$$
C_{6}^{kl}\rightarrow\left(1-e^{-bR}\sum_{k=0}^{6}{{(bR)^{k}}\over{k!}}\right)C_{6}^{kl}\;, \tag{11.74}
$$

或者采用碎片间重叠（所谓基于重叠的阻尼）：[[1271]](../bib_references/bib.md#bib1324)

<a id="eq:disp_overlap_damp"></a>

$$
C_{6}^{kl}\rightarrow\left(1-S_{kl}^{2}\left(1-2\log|S_{kl}|+2\log^{2}|S_{kl}|\right)\right)C_{6}^{kl}\;. \tag{11.75}
$$

**注意：

QM/EFP 色散相互作用目前处于禁用状态。
**

交换排斥源于泡利不相容原理（Pauli exclusion principle），该原理要求两个全同费米子的波函数必须是反对称的。在传统的经典力场中，交换排斥以正（排斥）项的形式引入，例如 Lennard-Jones 势中的 $R^{-12}$ 项。与之相反，EFP 使用基于波函数的形式体系来描述这一本质上属于量子力学的效应。

交换排斥相互作用按分子间重叠的级数展开导出，并截断至二次项，[[638]](../bib_references/bib.md#bib658)
 这要求每个有效碎片携带一个基组，用于计算每对相互作用碎片的重叠积分和动能单电子积分。属于碎片 $A$ 和 $B$ 的定域轨道 $i$ 与 $j$ 每一对所产生的交换排斥贡献为：

<a id="A3.S8.EGx107"></a>

$$
\displaystyle\begin{aligned} \displaystyle E^{\text{exch}}_{ij}=&\displaystyle-4\sqrt{-2\ln|S_{ij}|\over\pi}{S^{2}_{ij}\over R_{ij}}\\
&\displaystyle-2S_{ij}\left(\sum_{k\in A}F^{A}_{ik}S_{kj}+\sum_{l\in B}F^{B}_{jl}S_{il}-2T_{ij}\right)\\
&\displaystyle+2S^{2}_{ij}\left(\sum_{J\in B}{-Z_{J}R^{-1}_{iJ}}+2\sum_{l\in B}{R^{-1}_{il}}+\sum_{I\in A}{-Z_{I}R^{-1}_{Ij}}+2\sum_{k\in A}{R^{-1}_{kj}}-R^{-1}_{ij}\right)\end{aligned} \tag{11.76}
$$

其中 $i$、$j$、$k$ 和 $l$ 为 LMO，$I$ 和 $J$ 为原子核，$S$ 和 $T$ 为分子间重叠积分和动能积分，$F$ 为 Fock 矩阵元。

$E^{\text{exch}}_{ij}$ 的表达式涉及定域轨道对之间的重叠积分和动能积分。此外，由于式 ([11.76](#eq:ex_rep)) 是在完备基组近似下推导的，需要相当大（ reasonably large，即足够大）的基组才能保证精度。
[推荐使用 6-311++G(3df,2p) 基组，6-31+G* 被认为是最小的可接受基组。]
这些因素使得交换排斥成为中等规模体系中 EFP 能量计算里计算代价最昂贵的部分。

大型体系需要额外的考量。由于总交换排斥能是式 ([11.76](#eq:ex_rep)) 对所有碎片对的项求和，其计算代价相对于有效碎片数 $N$  formally（形式上）按 ${\cal{O}}({N^{2}})$ 标度。然而，交换排斥是短程相互作用；重叠积分和动能积分随碎片间距离呈指数衰减。因此，通过采用基于距离的筛选，重叠积分和动能积分的数目可按 ${\cal{O}}({N})$ 标度。 consequently（由此），对于大型体系，交换排斥的计算代价可能低于 EFP 的长程组分（如 Coulomb 相互作用）。

**注意：

QM/EFP 交换排斥能目前处于禁用状态。
**
