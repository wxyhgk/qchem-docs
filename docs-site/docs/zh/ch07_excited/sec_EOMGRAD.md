---
title: "7.9.21 CCSD 与 EOM-XX-CCSD 的解析梯度及性质"
---

## 7.9.21 CCSD 与 EOM-XX-CCSD 的解析梯度及性质

(July 4, 2026)

**Q-Chem** 中的耦合簇（Coupled-Cluster, CC）方法套件可以计算目标 EOM 态的各类性质，包括永久偶极矩、角动量投影、静态极化率（static polarizabilities）、$\langle\hat{S}^{2}\rangle$ 与 $\langle\hat{R}^{2}\rangle$ 值、$g$ 张量（仅限 CCSD）、核梯度（以及几何优化）。目标态通过在 *$rem* 段落中设置 CC_STATE_TO_OPT 来选取，该关键字指定 EOM 态的对称性与序号。除了态性质之外，还可以计算各种态间（interstate）性质，包括跃迁偶极矩、角动量矩阵元、双光子吸收（two-photon absorption）跃迁矩（及截面）、自旋–轨道耦合、电子圆二色谱（Electronic Circular Dichroism, ECD）旋转强度、Dyson 轨道以及光电离截面。

CCSD 及所有 EOM-CCSD 方法的解析梯度对闭壳层与开壳层参考（仅限 UHF 和 RHF）均可用，并支持冻结芯/虚轨道（frozen core/virtual）功能[[804]](../bib_references/bib.md#bib838)
 以及二电子积分的 RI/Cholesky 表示（另见第 [6.16](../ch06_correlation/sec_CCGRAD.md) 节）。
只要相应的单点能计算可行，这些计算就应当是可行的。

**注意：

ROHF 及非 HF（*e.g.*，B3LYP）轨道的梯度尚不可用。
**

对于 CCSD 和 EOM-CCSD 波函数，**Q-Chem** 可以计算永久及跃迁偶极矩、振子强度、
ECD 旋转强度 [包括长度规范（length gauge，与原点相关）和速度规范（velocity gauge，与原点无关）两种形式]、$\langle\hat{R}^{2}\rangle$
（以及 XX、YY、ZZ 分量各自的值，这有助于指认不同的里德堡（Rydberg）态，*e.g.*，$3p_{x}$ 与 $3s$ 的区分，*etc.*），以及
$\langle\hat{S}^{2}\rangle$ 值。$g$ 张量的计算对 CCSD 波函数可用
（见第 [10.11.4](../ch10_properties/sec_magnetman.md) 节及示例 [10.11.4.4](../ch10_properties/sec_magnetman.md#ex:CCSD-gtensor)）。

**注意：

$g$ 张量也可以按照文献 [[660]](../bib_references/bib.md#bib684)
 所述，使用 EOM-CC 与 RAS-CI 波函数通过组态相互作用（state-interaction）方法计算。
**。

CCSD 与 EOM-CCSD 程序与 NBO 5.0 程序包的接口同样可用。此外，可以请求对 EOM-CCSD 激发态进行激发态分析。对于 EOM-MP2，只有态性质（偶极矩、角动量投影、$\langle\hat{R}^{2}\rangle$、$\langle\hat{S}^{2}\rangle$）可用。
类似的功能对某些 EOM-OD 和 CI 模型（仅限 CCMAN）也可用。

还可以对实值与复值 EOM-CC 波函数进行分析；
见第 [7.9.30](ex_eomip-wfa.md) 节与第 [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) 节。EOM-IP/DIP /EA/DEA/SF 态的自然轨道（NTO）分析显然仅可用于 EOM 态之间的跃迁，
因此需要使用 CC_STATE_TO_OPT 关键字，与跃迁性质的计算方式相同。

用户必须了解所研究体系的点群对称性，
以及所关注的激发（目标）态的对称性。可以通过 CC_SYMMETRY 关闭对称性的使用。若将其设置为
FALSE，分子将按 $C_{1}$ 对称性处理，
且所有态均属于 $A$ 对称性。

**Q-Chem** 允许通过 CC_TRANS_PROP 关键字或 rem 段落 *$trans_prop* 灵活地控制态间性质的计算：用户可以
请求所有已计算 EOM 目标态与参考态之间的跃迁（CC_TRANS_PROP = 1），或者计算所有已计算的 EOM 目标态之间
全部跃迁性质（CC_TRANS_PROP = 2）。默认情况下，参考态是 CCSD
参考。若要计算相对于某一特定 EOM 态的跃迁性质，
请使用 CC_STATE_TO_OPT。

默认情况下，仅计算单电子性质。若要启用双电子性质（如 NAC、SOC、2PA）的计算，
需要激活额外的关键字，如下文所述。

*$trans_prop* 输入段落允许用户精确指定为哪些态对计算哪些性质。当输入中存在 *$trans_prop*
段落时，它将覆盖 *$rem* 变量 CC_TRANS_PROP 的设置。但是，要使 *$trans_prop* 生效，
CC_TRANS_PROP *确实*需要被设置。

> ```qchem
> $trans_prop
>    state_list         ! Start a list of states
>    ee_singlets 1 1    ! state 1: EE singlet with irrep = 1 and istate = 1
>    ee_triplets 1 2    ! state 2: EE triplet with irrep = 1 and istate = 2
>    ref                ! state 3: Reference state (can be CC or MP2, but the latter NYI
>                       ! in transition prop driver)
>    end_list           ! End list
>    state_pair_list    ! Start to specify pairs of states,
>    3 1                ! transition from state 3 to state 1 (known bug here: CC state
>                       ! needs to be 1st one)
>    3 2                ! transition from state 3 to state 2 (known bug here: CC state
>                       ! needs to be 1st one)
>    end_pairs          ! End list of pairs
>    calc nac           ! Compute NAC for all transition pairs listed before this keyword
>    state_list         ! Start another list of states (user is able to request multiple
>                       ! state lists for multiple tasks)
>    ref                ! reference state
>    ee_singlets 0 0    ! zero means all requested irreps/istate in $rem
>    end_list
>    calc dipole soc    ! Compute transition dipole and SOC
>    calc opdm_norm     ! Compute norm of transition OPDM
> $end
> ```

关于 *$trans_prop* 输入段落的说明：

1. 1.

`calc` 为其*前面*的*第一个*态对列表（或态列表）计算性质。
2. 2.

态对列表是*可选的*：若没有态对列表，则考虑态列表内所有可能的组合。
3. 3.

`calc` 之后的选项包括：`nac`、`soc`、`dyson`、
`2pa`、`dipole`、`default`、`pcm`、`opdm_norm`、
`wfa`、`ang`、`linmom`、`dipole linmom`、`ecd`。目前仅实现了其中的一部分。

**注意：

*$trans_prop* 段落是一项新功能，仍在开发之中——使用风险自负。
最终，该段落将取代其他控制方式并成为默认设置。
**

## 7.9.21.1 使用 EOM-CC 波函数计算角动量矩阵元

角动量矩阵元可用于分析波函数、指认态的特征，或
识别线性分子的项（term）对称性标签。与其他单电子性质一样，这些矩阵元
利用单粒子态密度矩阵和跃迁密度矩阵来求值。
角动量是一个与规范相关的性质，即其数值依赖于规范原点。
规范位置可通过 *$gauge_origin* 输入段落控制。
默认的规范位置对应于坐标系的原点 $(0,0,0)$。

> ```qchem
> $gauge_origin            Position of the gauge origin for
>    1.00  0.200  0.500       angular momentum calculations in angstroms.
> $end
> ```

## 7.9.21.2 EOM-CC 在速度规范与混合规范下的振子强度

单光子吸收的振子强度通常在长度规范（“lg”）下计算

<a id="Ch7.E110"></a>
$$
f^{\rm{lg}}=\frac{2\omega_{fn}}{3}\sum_{\alpha=x,y,z}\langle n|\hat{\mu}_{\alpha}|f\rangle\langle f|\hat{\mu}_{\alpha}|n\rangle, \tag{7.110}
$$

其中 $\hat{\mu}$ 是电偶极矩算符，但它也可以在速度规范（“vg”）和混合规范（“mx”）下表示为

<a id="Ch7.E111"></a>
$$
f^{\rm{vg}}=\frac{2}{3\omega_{fn}}\sum_{\alpha=x,y,z}\langle n|\hat{p}_{\alpha}|f\rangle\langle f|\hat{p}_{\alpha}|n\rangle, \tag{7.111}
$$

<a id="Ch7.E112"></a>
$$
f^{\rm{mx}}=\frac{2i}{3}\sum_{\alpha=x,y,z}\langle n|\hat{\mu}_{\alpha}|f\rangle\langle f|\hat{p}_{\alpha}|n\rangle, \tag{7.112}
$$

其中 $\hat{p}$ 是线动量算符。

三种规范均已实现，作为 **Q-Chem** 中 EOM-CCSD 跃迁性质的一部分。
$f^{\rm lg}$ 作为默认跃迁性质计算，另外两种则需要手动激活。这可以在 *$trans_prop* 输入段落中通过指定 `calc linmom`（仅速度规范）或 `calc dipole linmom`（三种规范全部）来完成。
示例 [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) 对此进行了演示。

请注意：

- –

若输入中激活了 ECD 计算，$f^{\rm lg}$、$f^{\rm vg}$ 和 $f^{\rm mx}$ 也将被计算；
- –

若两个态之间的能量差非常小（阈值为 $10^{-6}$），如（近）简并态的情况，
会发出警告并跳过速度规范振子强度的计算。

## 7.9.21.3 在长度与速度规范下计算 EOM-CC 旋转强度（ECD 与 XCD）

**Q-Chem** 可以按照文献 [[46]](../bib_references/bib.md#bib29)
 所述的形式体系与实现，使用 EOM-CC 波函数进行 ECD 和 XCD 计算。
CC 理论下 ECD 的旋转强度定义为：

<a id="A3.S8.EGx56"></a>
$$
\displaystyle R^{\text{lg}}_{nf} \tag{7.113}
$$

分别对应长度（“lg”）和速度（“vg”）表达形式。$\hat{\mu}$ 是电偶极矩算符，$\hat{p}$ 是线动量算符。式 ([7.113](#eq:length)) 中的长度规范表达式与规范原点相关，而式 ([7.114](#eq:velocity)) 与规范原点无关。

ECD 可用于价层及核激发（core-excited）区域的基态与激发态 EOM-EE-CCSD 跃迁。后者
基于 fc-CVS-EOM-EE-CCSD 框架。ECD 也可用于 EOM-EA-CCSD 态之间的跃迁。EOM-IP/EOM-DIP 计算的 ECD 尚不可用。

旋转强度的计算可以通过激活 CC_EOM_ECD，或通过 *$trans_prop* 段落来启用，如示例 [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) 所示。
在后一种情况下，用户既可以请求同时计算跃迁偶极矩、线动量和角动量算符（“`calc dipole linmom ang`”），
也可以仅请求 ECD（“`calc ecd`”）。

请注意：

- –

旋转强度将在长度规范和速度规范下同时计算；
- –

长度、速度和混合规范下的振子强度也将一并计算；
- –

若两个态之间的能量差非常小（阈值为 $10^{-6}$），如（近）简并 s
s 态的情况，会发出警告并跳过速度规范强度的计算。

## 7.9.21.4 使用 EOM-CC 波函数计算自旋-轨道耦合

EOM-CC 波函数的自旋-轨道耦合（spin-orbit coupling, SOC）计算在 CCMAN2 中可用。[[364]](../bib_references/bib.md#bib370)

我们采用微扰处理方法，
其中 SOC 使用零阶非相对论波函数，作为 Breit–Pauli 哈密顿量相应部分的矩阵元来计算。
通过 CALC_SOC 可以使用两个版本的代码。
旧代码将 SOC 计算为一对需显式计算的态之间的矩阵元；因此每次跃迁只能产生
一个矩阵元。虽然这种方法可以通过旋转分子来
提取整个矩阵，[[1107]](../bib_references/bib.md#bib1150)

但这些矩阵元之间的相对相位会
丢失。新版本代码解决了这一问题，并提升了
性能。[[1103]](../bib_references/bib.md#bib1151)
 新代码利用
Wigner–Eckart 定理计算完整的自旋-轨道矩阵。我们按自旋属性
对激发算符进行划分。由于自旋–轨道
算符是三重（triplet）算符，可以考虑如下三重
激发算符

<a id="A3.S8.EGx57"></a>
$$
\displaystyle T^{1,1}_{p,q}=-a^{\dagger}_{p\alpha}a_{q\beta} \tag{7.115}
$$

若应用 Wigner–Eckart 定理，下列矩阵元可
分解为 Clebsch–Gordan 系数与约化矩阵元：

<a id="eq:WignerEckart_u"></a>
$$
\langle\Psi_{I}SM|T^{1,k}_{p,q}|\Psi_{J}S^{\prime}M^{\prime}\rangle=\langle S^{\prime}M^{\prime}|1k|SM\rangle\langle\Psi_{I}S||T^{1,\cdot}_{p,q}||\Psi_{J}S^{\prime}\rangle, \tag{7.118}
$$

其中 $S$ 和 $S^{\prime}$ 表示自旋，$M$ 和 $M^{\prime}$ 分别表示 $\Psi_{I}$ 和 $\Psi_{J}$ 的自旋
投影。这些约化矩阵元构成一个新的无自旋三重跃迁密度矩阵，我们将其
记为 $u^{1,\cdot}$。自旋-轨道约化矩阵元通过与 $u^{1,\cdot}$ 求迹得到：

<a id="A3.S8.EGx58"></a>
$$
\displaystyle\langle\Psi_{I}S||H_{L_{-}}||\Psi_{J}S^{\prime}\rangle=-\frac{1}{2}\sum_{p,q}h^{SO}_{L_{-};p,q}u^{1,\cdot}_{p,q} \tag{7.119}
$$

再次应用 Wigner–Eckart 定理，即可由约化矩阵元生成所有可能的矩阵元。该算法可用于
MP2 和 CCSD 参考的 EOM-EE/SF/IP/EA/DIP /DEA 波函数，以及 CCSD 参考与 EOM-EE/SF 之间的计算。
示例 [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1)、[7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1)、[7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) 演示了
各种 EOM-CC 模型的 SOC 计算。

```qchem
A(Ket)->B(Bra) transition SO matrices
 Analyzing Sz ans S^2 of the pair of states...
 Ket state:  Computed S^2 = 2.019877 will be treated as 2.000000 Sz = 0.000000
 Bra state:  Computed S^2 = 0.019216 will be treated as 0.000000 Sz = 0.000000
 Clebsch-Gordan coefficient: <1.000,0.000;1.000,0.000|0.000,0.000> = 0.577
 One-electron SO (cm-1)
 Reduced matrix elements:
 <S|| Hso(L-) ||S’> = (-2.660965,-22.180075)
 <S|| Hso(L0) ||S’> = (0.000000,-20.019517)
 <S|| Hso(L+) ||S’> = (-2.660965,22.180075)
 SOCC = 21.593626
 Actual matrix elements:
       |Sz=-1.00>           |Sz=0.00>           |Sz=1.00>
 <Sz=0.00|(1.536309,12.805673)(0.000000,-11.558274)(1.536309,-12.805673)
 Mean-field SO (cm-1)
 Reduced matrix elements:
 <S|| Hso(L-) ||S’> = (-2.069801,-9.910572)
 <S|| Hso(L0) ||S’> = (0.000000,-10.692261)
 <S|| Hso(L+) ||S’> = (-2.005570,9.957712)
 Singlet part of <S|| Hso(L0) ||S’> = (-0.000000,0.037101) (excluded from all matrix elements)
 L-/L+ Averaged reduced matrix elements:
 <S|| Hso(L-) ||S’> = (-2.037685,-9.934142)
 <S|| Hso(L+) ||S’> = (-2.037685,9.934142)
 SOCC = 10.328006
 Actual matrix elements:
       |Sz=-1.00>           |Sz=0.00>           |Sz=1.00>
 <Sz=0.00|(1.176458,5.735480)(0.000000,-6.173180)(1.176458,-5.735480)
```

该算法通过将 CALC_SOC 设置为 1 或 2 来激活。
其执行依赖于非零的 Clebsch-Gordan 系数（否则无法
从跃迁密度矩阵中提取所需信息）。若 Clebsch-Gordan 系数为零，
将打印警告并跳过该跃迁。通常可以通过选取自旋翻转（SF）或电子激发（EE），
或在 EA、IP 情况下选取 alpha 或 beta 电子，
来挑选出使 Clebsch-Gordan 系数非零的态。态多重度的
判定基于 $\hat{S}^{2}$。若存在严重的自旋污染，
会打印警告，并采用最接近的多重度。

在开壳层参考的情况下，所得的约化矩阵元可能
违反自旋-轨道算符所隐含的对称性。将
CALC_SOC 设置为 1 会产生这些约化矩阵元，但实际的自旋-轨道
矩阵将由*平均后的*约化
矩阵元构造，其中所需的对称性得到恢复。将
CALC_SOC 设置为 2 则在不平均约化矩阵元的情况下直接构造自旋-轨道矩阵。
尽管在实践中这两种选项的差异很小，但平均化可以简化
能级分裂的分析。示例 [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) 和 [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1)
演示了在使用 SOMF 的乙炔-O 复合物中计算 SOC。

**注意：

在存在有效核势（ECP）的情况下，尝试使用上述算法
（CALC_SOC=1 或 2）计算 SOC，
很可能得到非物理的极低 SOC 值。
作为替代，我们建议使用有效核电荷（CALC_SOC=4）。
**

要对无自旋单粒子跃迁密度矩阵进行 NTO 分析[[1105]](../bib_references/bib.md#bib1152)

并计算 NTO 上的自旋-轨道积分，
请在 CALC_SOC = 1、2 或 4 之外，
设置 STATE_ANALYSIS = TRUE 以及 MOLDEN_FORMAT = TRUE。

**Q-Chem** 还支持使用带有效核电荷的单电子 SO 算符计算 SOC。[[380]](../bib_references/bib.md#bib384)

该方法的依据是：SOC 算符的
平均场双电子部分的效应可以用屏蔽核电荷来近似。
在全电子计算（无 ECP）的情况下，该方法不如 SOMF 严格，
但它完全不使用双电子积分，因此计算代价更低。
此外，使用有效核电荷可以在存在 ECP 时获得合理的 SOC 值。
该计算通过 CALC_SOC = 4 激活。**Q-Chem** 的输出将包含
使用原始核电荷与屏蔽（有效）核电荷计算的单电子 SOC。
在开壳层参考的情况下，SOC 使用 $L_{+}/L_{-}$ 平均（与
CALC_SOC = 1 的情况相同）计算。默认情况下，计算使用 Fedorov *et al.* 的
有效核电荷[[380]](../bib_references/bib.md#bib384)，
其数值已对 Li 至 At 的元素列表，
镧系元素除外。对于全电子计算，
使用基于 6-31G 基组的有效核电荷，对于 ECP，则使用 SBKJC 电荷。
另外，用户可以通过输入段落
*$soc_eff_charges* 提供自定义的有效核电荷，方式如下：

> ```qchem
> $soc_eff_charges
>    8.0  6.0   !use eff. charge=6 for oxygen (Z=8)
>    17.0 11.0 !use eff. charge=11 for chlorine (Z=17)
> $end
> ```

示例 [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) 和 [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) 演示了这一功能。

旧版（legacy）代码包含完整的双电子处理及平均场
近似。要启用 SOC 计算，必须通过 CC_TRANS_PROP 启用 EOM 态之间的跃迁性质，
并将 CALC_SOC 设置为 3 以请求 SOC。默认情况下，将计算单电子和平均场
双电子耦合。完整双电子耦合计算通过设置 CC_EOM_PROP_TE 激活。

与其他 EOM 跃迁性质一样，初始 EOM 态由
CC_STATE_TO_OPT 设定，耦合在该态与
所有其他 EOM 态之间计算。若未设置 CC_STATE_TO_OPT，则 SOC 在
参考态与所有 EOM-EE 或 EOM-SF 态之间计算。

**注意：

在自旋受限（spin-restricted）的情况下，如使用闭壳层
参考态的 EOM-EE 计算，无法计算单重态与三重态 EOM 组态之间的 SOC（只能
计算参考态与 EOM 三重态之间的 SOC）。若要计算 EOM-EE 单重态与 EOM-EE 三重态之间的 SOC，请在
相同作业中设置 UNRESTRICTED = TRUE 重新运行，
使三重态和单重态出现在同一组态中。
**

**注意：

计算跃迁性质最灵活的控制方式由
*$trans_prop* 输入段落提供，如第 7.9.21 节所述。
**

## 7.9.21.5 使用 EOM-CC 波函数计算非绝热耦合

EOM-CC 波函数的非绝热（绝热）耦合（nonadiabatic (derivative) couplings, NACs）计算在 CCMAN2 中可用。
我们采用 Szalay 的方法，其中耦合通过修改的解析梯度代码，经由“求和态（summed states）”计算：[[1336]](../bib_references/bib.md#bib1394)

<a id="eq:Szalay:ExactH"></a>
$$
h^{x}_{IJ}\equiv\langle\Psi_{I}|H^{x}|\Psi_{J}\rangle=\frac{1}{2}\left(G_{(I+J)}-G_{I}-G_{J}\right), \tag{7.122}
$$

其中 $G_{I}$、$G_{J}$ 和 $G_{IJ}$ 分别是态 $I$、$J$
以及虚拟求和态 $|\Psi_{I+J}\rangle\equiv|\Psi_{I}\rangle+|\Psi_{J}\rangle$ 的解析梯度。目前，EE/IP/EA 的 NAC 可用。[[375]](../bib_references/bib.md#bib380)

**注意：

请注意，NAC 向量的各个分量依赖于分子的
取向。
**

## 7.9.21.6 EOM-EE-CCSD 内的双光子吸收跃迁矩与截面

EOM-EE-CCSD 波函数的双光子吸收（two-photon absorption, 2PA）跃迁矩与截面计算在 **Q-Chem** 中可用（仅限 CCMAN2）。CCSD-EOM 和 EOM-EOM
跃迁均可计算。其形式体系见
文献 [[977]](../bib_references/bib.md#bib1018)
。该功能在常规（canonical）实现和 RI/CD 实现中均可用。EOM-DEA-CCSD 态之间的无阻尼常规 2PA 截面
也可用。相关关键字为 CC_EOM_2PA（开启计算，控制 NTO 计算）、CC_STATE_TO_OPT（用于
EOM-EOM 跃迁）；额外的定制可通过
*$2pa* 段落完成。输出的物理量是微观截面
$\delta^{TPA}$（也称为旋转平均 2PA 强度），定义见文献 [[977]](../bib_references/bib.md#bib1018)
 的式 (30)。

*$2pa* 段落用于指定满足共振条件的频率对范围。若输入中不存在 *$2pa* 段落，
则对两个简并光子计算跃迁矩，其总能量
与各目标 EOM 态的激发能（对 CCSD-EOM）或各
EOM-EOM 能量差（对 EOM-EOM 跃迁）相匹配：$2h\nu=E_{ex}$
对于共振或近共振计算（*i.e.*，当其中一个光子与某一激发态
共振时），应使用阻尼响应理论（damped response theory）；
这类计算通过在 *$2pa* 段落中添加 DAMPED_EPSILON 来执行
（$\epsilon$ 的值以 hartree 为单位指定，通常 0.001 就足够了）。

> ```qchem
> $2pa                      Non-degenerate resonant 2PA
>    N_2PA_POINTS 6         Number of frequency pairs
>    OMEGA_1 500000 10000   Scans 500 cm$^{-1}$ to 550 cm$^{-1}$
>                           in steps of 10 cm$^{-1}$
> $end
> ```

N_2PA_POINTS 是光谱范围内的频率对数目。
OMEGA_1 关联的第一个值是光谱起始处频率 $\times 1000$（单位 cm${}^{-1}$），第二个值是
步长 $\times 1000$（单位 cm${}^{-1}$）。每一步中第二个光子的频率
由程序内部按激发能减去
OMEGA_1 确定。

为深入理解计算得到的 2PA 截面，可以对响应单粒子密度矩阵进行 NTO
分析 [[979]](../bib_references/bib.md#bib1020)
。要
激活 2PA 响应单粒子跃迁密度矩阵的 NTO 分析，请设置
STATE_ANALYSIS = TRUE、MOLDEN_FORMAT
= TRUE（将轨道导出为 **MolDen** 文件）、
NTO_PAIRS（指定要打印的轨道数目）。NTO
分析将对完整的 2PA 响应单粒子跃迁
密度矩阵以及归一化的 $\omega$DM 进行（更多细节见
文献 [[979]](../bib_references/bib.md#bib1020)
）。

默认情况下，无阻尼和阻尼的 2PA 响应波函数均使用一种名为 **Dalton**
求解器的新型迭代 Davidson 型子空间方法计算。[[248]](../bib_references/bib.md#bib251)

该方法由 DALTON_XCONV、DALTON_PRECOND_START、
DALTON_MAXITER 和 DALTON_MAXSPACE
关键字控制。阻尼 2PA 响应波函数也可以通过设置 DAMPED_DALTON_SOLVER = FALSE
使用较旧的 DIIS 过程计算。
DIIS 求解器由
CC_MAX_ITER、CC_DIIS_START、
CC_DIIS_SIZE、CC_EOM_2PA_ECONV 和 CC_EOM_2PA_XCONV 控制。

**注意：

**Dalton** 求解器在判断收敛时使用残差范数的平方（与 Davidson 求解器相同），
而 DIIS 求解器使用相邻迭代之间响应向量之差的范数。
**

2PA 计算可以通过激活
CC_EOM_2PA_SINGLE_PREC 关键字（连同激活 CC 与 EOM-CC 方程单精度执行的关键字，见第 [7.9.15](sec_SP_EOM_CC.md) 节）
以单精度进行。计算其他非线性性质的能力包括 RIXS（见第 [7.9.9.1](sub_cvs_eom.md#sec:cvs_eom_rixs) 节）
以及静态和动态极化率（第 [7.9.21.8](#sec:EOMpol) 节）。

## 7.9.21.7 CCSD 波函数旋光度的计算

**Q-Chem** 可以对 CCSD 波函数（在 CCMAN2 中）计算旋光（optical rotation, OR）张量及相关的比旋光度[[1058]](../bib_references/bib.md#bib1103)

（在对应于旋光仪工作 lamp 所选频率处）[[46]](../bib_references/bib.md#bib29)
。该理论基于
期望值方法，*i.e.*，利用响应态将按态求和（sum-over-states）表达式
改写为封闭形式表达式[[46]](../bib_references/bib.md#bib29)
。计算涉及常规（无阻尼）或阻尼
响应波函数的求解。使用长度规范、速度规范及修正速度规范[[1059]](../bib_references/bib.md#bib1104)
。

常规（即无阻尼）旋光的计算通过将 CC_OPTROT 设置为 5 来执行，涉及利用零阶波函数和
响应波函数计算（无阻尼）密度矩阵。
若线偏振（lp）光的探测频率接近某一激发能的共振，无阻尼响应计算
将发散。通过给频率附加一个唯象的虚数阻尼因子
（*e.g.*，0.001 hartree），即可计算相应的
阻尼响应波函数。

在长度（速度）规范下，阻尼旋光张量的实部（虚部）对应于
线偏振光两个圆偏振分量的差分吸收，
即电子圆二色谱（ECD）。其虚部（实部）对应于旋光色散（ORD）。
目前，这些功能仅在常规实现中可用（无 RI/CD）。

**注意：

这些计算要求将 CC_FULLRESPONSE 设置为 0，
并将 CC_REF_PROP 设置为 TRUE。
**

OR 的响应方程使用与极化率响应方程相同的求解器
（相关关键字见第 [7.9.21.8](#sec:EOMpol) 节）。

典型的在钠 D 线（589.6 nm = 16960.651 cm${}^{-1}$）处进行常规（无阻尼）旋光计算的 *$opt_rot*
段落输入为：

> ```qchem
> $opt_rot
> omega_1  16960651 0 1    !One calculation at D-line
> damped_epsilon 0.0       ! Disables damped OR [mandatory].
> length_gauge <0 or 1>    ! Computes length-gauge OR if set to 1
> velocity_gauge <0 or 1>  ! Computes (modified) velocity gauge OR if set to 1
> $end
> ```

对于阻尼计算，频率范围、阻尼因子和规范选择通过 *$opt_rot* 段落按如下方式设置：

> ```qchem
> $opt_rot
> omega_1  500000 10000 6  !Scans 500 cm$^{-1}$ to 550 cm$^{-1}$
>                          !      in steps of 10 cm$^{-1}$
> damped_epsilon 0.01      ! (Optional) Use for damped CCSD OR only.
>                          ! Sets a damping factor of 0.01 Hartrees.
> length_gauge <0 or 1>    ! Computes length-gauge OR if set to 1
> velocity_gauge <0 or 1>  !Computes (modified) velocity gauge OR if set to 1
> $end
> ```

**注意：

与其他跃迁性质一样，ECD/XCD 光谱也可以由 EOM-CC/CVS-EOM-CC 态之间的
旋转强度计算得到。
见第 7.9.21 节。
**

## 7.9.21.8 CCSD 与 EOM-CCSD 波函数静态及动态极化率的计算

CCSD 与 EOM-EE/SF-CCSD 波函数的静态和动态偶极极化率计算在 CCMAN2 中可用。极化率的计算方式有两种：
作为 CCSD 或 EOM-CCSD 能量的二阶导数[[978]](../bib_references/bib.md#bib1019)
，以及
使用期望值方法，*i.e.*，精确波函数的按态求和表达式[[976]](../bib_references/bib.md#bib1021)
。在解析导数方法
（或响应理论形式体系）中，只考虑簇振幅的响应；不包含轨道弛豫。
若要用该方法计算极化率（CC_POL
和 EOM_POL 均须等于 1 或 2），必须将 CC_FULLRESPONSE 设置为 2，
以关闭轨道弛豫但在 EOM 计算中允许振幅响应。CC_POL
和 EOM_POL = 3 或 4 与
CC_FULLRESPONSE = 0 结合使用将启用期望值
极化率。请注意，这些计算要求将 CC_REF_PROP 和 CC_EOM_PROP/
设置为 TRUE。

动态极化率通过 *$dyn_pol* 段落启用，该段落
指定频率范围。若没有此段落，将只计算静态
极化率。
CCSD 与 EOM-EE/SF-CCSD 在虚频率下的动态极化率也可通过 *$dyn_pol* 段落
使用。阻尼响应理论框架下的 CCSD 静态与动态极化率同样可用，
可通过在 *$dyn_pol* 段落中指定
*damped_epsilon* 变量来开启。

> ```qchem
> $dyn_pol
>    500000 10000 6  ! Scans 500 cm$^{-1}$ to 550 cm$^{-1}$
>                    !       in steps of 10 cm$^{-1}$
> damped_epsilon 10  ! (Optional) Use for damped CCSD polarizabilities only.
>                    ! Sets a damping factor of 10/1000 Hartrees.
> $end
> ```

目前，这些功能仅在常规实现中可用。

**注意：

EOM-CCSD 极化率仅对 EE 和 SF 波函数可用。
**

默认情况下，无阻尼和阻尼的极化率响应波函数均使用一种名为 **Dalton**
求解器的新型迭代 Davidson 型子空间方法计算。[[248]](../bib_references/bib.md#bib251)

该方法由 DALTON_XCONV、DALTON_PRECOND_START、
DALTON_MAXITER 和 DALTON_MAXSPACE
关键字控制。阻尼极化率响应波函数也可以通过设置 DAMPED_DALTON_SOLVER = FALSE
使用较旧的 DIIS 求解器计算。DIIS 求解器由 CC_MAX_ITER、CC_DIIS_START、CC_DIIS_SIZE 和 CC _CONVERGENCE 控制。

**注意：

**Dalton** 求解器在判断收敛时使用残差范数的平方（与 Davidson 求解器相同），而 DIIS 求解器使用相邻迭代之间响应向量之差的范数。响应计算（2PA、极化率、RIXS）的默认收敛阈值为 5。
**

## 7.9.21.9 CCSD 波函数静态及动态第一超极化率的计算

CCSD 波函数的静态和动态偶极第一超极化率计算在 CCMAN2 中可用（目前仅限常规实现）。
第一超极化率在阻尼响应的期望值
框架内计算[[981]](../bib_references/bib.md#bib1024)
。
将 CC_1HPOL 设置为 1 所启动的算法
以最少数目的响应波函数计算来获得该性质。
将 CC_1HPOL 设置为 3，则通过构造
二阶响应密度矩阵来计算该性质，这需要计算
大量的二阶响应波函数。随后利用这些二阶响应密度矩阵，
通过 **libwfa** 计算二阶响应自然轨道，
用于定量的波函数与轨道分析。
第一超极化率的计算需要 *$1hpol* 段落，其中
指定两个光子的频率范围（$\omega_{1}$ 和 $\omega_{2}$；
$\omega_{3}=\omega_{1}+\omega_{2}$），
以及相应的阻尼因子。

**注意：

这些计算要求将 CC_FULLRESPONSE 设置为 0，
并将 CC_REF_PROP 设置为 TRUE。
**

> ```qchem
> $1hpol
> omega_1 0000000 1500000 3 0.01 !Scans omega_1 from 0 cm$^{-1}$ to (3-1)*1500 cm$^{-1}
>                                ! in steps of 1500 cm$^{-1}$
>                                ! damping factor epsilon_1 is 0.01 Hartrees
> omega_2 0000000 2500000 4 0.01 !Scans omega_2 from 0 cm$^{-1}$ to (4-1)*2500 cm$^{-1}
>                                ! in steps of 2500 cm$^{-1}$
>                                ! damping factor epsilon_2 is 0.01 Hartrees
> omega_3 0.01                   ! damping factor epsilon_3 is 0.01 Hartrees
> $end
> ```

示例 [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) 在阻尼响应理论与
期望值方法的框架下，计算了 LiH 的 CCSD/STO-3G 波函数的静态与动态第一超极化率。
针对以下光子组（频率单位 cm${}^{-1}$）计算该性质：
(0, 0; 0), (2500, 0; -2500), (5000, 0; -5000), (0, 3500; -3500), (0, 7000; -7000), (2500, 3500; -6000), (2500, 7000; -9500),
(5000, 3500; -8500), (5000, 7000; -12000)。

## 7.9.21.10 光电离与电子解离（Photodetachment）截面及光电子角分布（PAD）

**Q-Chem** 可以按照基于 Dyson 轨道[[478]](../bib_references/bib.md#bib490)
的理论框架，计算描述光电离/电子解离的物理量。
既可以使用计算得到的 Dyson 轨道，然后用独立的
**ezDyson** 程序[[478]](../bib_references/bib.md#bib490)
计算截面，也可以请求由 **Q-Chem** 完成这些计算；
后一种方式效率更高。
这些计算需要连接初始态与目标态的 Dyson 轨道以及
自由电子的波函数。目前仅提供平面波（plane-wave）处理。此功能
仅在 ccman2 中可用。

可以按照以下设置计算总截面和角分辨光电离截面。首先，用户应请求计算
合适的初始态与目标态以及相应的 Dyson 轨道（使用 CC_DO_DYSON 关键字，或在 *$trans_prop* 段落中做相应设置）。其次，应将 CC_FREE_ELECTRON 设置为 TRUE。
第三，截面的相关参数——如光的偏振、光电子的能量范围以及取向
平均的细节——应在 *$free_electron* 段落中指定。

> ```qchem
> $free_electron
> N_ENERGY_POINTS 20  !number of points in the kinetic energy grid
> KE_MIN 10   !minimum kinetic energy of the free-electron in 1E-2  eV (here, 0.1 eV)
> KE_MAX 1010  !maximum kinetic energy of the free-electron in 1E-2  eV  (here, 10.1 eV)
> SPIN_DEG 2  !spin degeneracy factor
> ORB_DEG 1  !orbital degeneracy factor
> POL_X 0  !X-component of the polarization vector in 1E-2 (here, 0)
> POL_Y 0  !Y-component of the polarization vector in 1E-2 (here, 0)
> POL_Z 100  !Z-component of the polarization vector in 1E-2 (here, 1)
> CIRC_POL 0  !if circular polarization is requested
> DO_AVERAGE 0  !if orientational averaging to be performed
> N_THETA 50  !number of theta-points in the angular grid
> N_PHI 10  !number of phi-points in the angular grid
> $end
> ```

采用类似的设置，还可以计算 Dyson 轨道与
平面波之间的重叠。该计算通过 DYSON_PW_COUPLING 关键字激活
（CC_DO_DYSON 也应设置为 TRUE）。
计算的参数，例如 $|{\mathbf{k}}|$ 值的数目
以及是否应对不同 ${\mathbf{k}}$ 取向进行平均，
在 *$free_electron* 段落中指定。示例 [7.9.29.2](topic_dyson.md#ex:DYSONPW) 和 [7.9.29.2](topic_dyson.md#ex:DYSONPW)
及下文摘录演示了这一功能。默认不进行平均，
$|{\mathbf{k}}|$ 使用五个网格点。

> ```qchem
> $free_electron
> k_avg  1  !perform averaging over k-orientations using default grid of 50( theta)x10(phi)
> k_grid_points 6  !Coupling computed for |k|-values  from 0.0 eV to 0.1x(k_grid_points -1)
> $end
> ```

**注意：

$|{\mathbf{k}}|$ 值的网格按
$\sqrt{2E}$ 计算，其中 $E$ 从 0.0 eV 变化到 0.1*($k\_grid\_points$-1) eV。
**

> ```qchem
> $free_electron
> k_x  100  ! kx=1 (k_x/100)
> k_y  100  ! ky=1
> k_z  100  ! kz=1
> k_grid_points 6  ! coupling computed for  |k|-values  from 0.0 eV to 0.1x(k_grid_points -1)
> $end
> ```

**注意：

$|{\mathbf{k}}|$ 的大小无关紧要，只有方向重要。
**

光电子角分布（photoelectron angular distribution, PAD）——$\Omega(\theta,\phi)$，
其中 $\theta$ 和 $\phi$ 是光电子矢量
$\mathbf{k}$ 在实验室坐标系中的角坐标——将为每个电离态
（即 pad_1A1、pad_1B2 等）写入单独的文件。对于线偏振光，将连同
截面一起计算不对称参数 $\beta$。
计算的输入参数通过 *$free_electron* 段落指定。
默认值为：SPIN_DEG=2、ORB_DEG=1，以及 DO_AVERAGE=0（不做平均）。
计算要求用户指定若干 $\theta$ 和 $\phi$ 点
（默认分别为 50 和 10），以确定计算 PAD 时
波矢 $\mathbf{k}$
的方向。
用户应指定偏振的三个分量（用于线偏振）
或圆偏振；这两种选项互斥。对于圆偏振光，
$z$ 为光的传播方向。
若将 DO_AVERAGE 设置为 1，则对所有分子取向进行平均，
并假设光的偏振沿 $z$ 轴（偏振设置
将被忽略）。
这些功能在下文的示例 [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1)-[7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) 中演示。

CC_FREE_ELECTRON

### `CC_FREE_ELECTRON`

> **指定是否计算涉及自由电子的性质。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE/FALSE
> * **建议**: 无

DYSON_PW_COUPLING

### `DYSON_PW_COUPLING`

> **计算 Dyson 轨道与平面波之间的重叠。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE (do not compute coupling)`
> * **选项**:
>     * TRUE/FLSE
> * **建议**: 需要时激活。必须同时开启 CC_DO_DYSON。
