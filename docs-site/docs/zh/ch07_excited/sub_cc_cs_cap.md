---
title: "7.9.10 亚稳态的 EOM-CC 计算"
---

## 7.9.10 亚稳态的 EOM-CC 计算

（2026 年 7 月 4 日）

常规的耦合簇（coupled-cluster）方法与运动方程（equation-of-motion, EOM）方法可以处理从性质良好的闭壳层分子到各种开壳层及电子激发态物种的电子结构问题[[729]](../bib_references/bib.md#bib760)，

但被称为共振（resonance）的亚稳电子态对理论方法而言却是一个棘手的难题。通过使用复标度（complex scaling）、复基函数（complex basis functions, CBFs）以及复吸收势（complex absorbing potential, CAP）技术，**Q-Chem** 将这些强大的方法扩展到对自电离（auto-ionizing）态的描述，例如瞬态阴离子、高激发电子态以及内壳层电离物种[[156]](../bib_references/bib.md#bib149)

（CC 与 EOM-CC 计算的 CBF 扩展分别在[第 4.9.5 节](../ch04_scf/sec_cbfscf.md)和[第 8.7 节](../ch08_basis/sect_zbas.md)中描述）。此外，

用户还可以采用带电球（charged sphere）和缩放原子电荷（scaled atomic charges）选项来使用稳态化（stabilization）技术。[[741]](../bib_references/bib.md#bib774)
 这些方法仅在 CCMAN2 中可用。复数 CC/EOM 代码由 COMPLEX_CCMAN 启用；
具体参数应在 *$complex_ccman* 段中指定。

### `COMPLEX_CCMAN`

> **请求复标度或 CAP 增强的 CC/EOM 计算。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`FALSE`
> * **选项**：
>     * TRUE
>     * 启用复数 CC/EOM 代码。
> * **建议**：在 CCMAN 中不可用。需要在 $complex_ccman 段中指定 CAP 强度或复标度参数。

*$complex_ccman* 段用于指定复标度/CAP 计算的细节，如下所示。如果用户指定了
CS_THETA，则执行复标度计算。

> ```qchem
> $complex_ccman
>    CS_THETA  10   Complex-scaling parameter theta=0.01, r->r exp(-i*theta)
>    CS_ALPHA  10   Real part of the scaling parameter alpha=0.01,
> !                 r->alpha r exp(-itheta)
> $end
> ```

或者，对于 CAP 计算，需要指定 CAP 参数。

> ```qchem
> $complex_ccman
>    CAP_ETA  1000  CAP strength in 10-5 a.u. (0.01)
>    CAP_X    2760  CAP onset along X in 10^-3 bohr (2.76 bohr)
>    CAP_Y    2760  CAP onset along Y in 10^-3 bohr (2.76 bohr)
>    CAP_Z    4880  CAP onset along Z in 10^-3 bohr (4.88 bohr)
>    CAP_TYPE 1     Use cuboid cap (CAP_TYPE=0/2 will use spherical/Voronoi CAP)
> $end
> ```

用户也可以通过 CAP_RE_ETA 添加实数吸收势；其格式与 CAP_ETA 相同。例如，
以下设置将添加纯实数吸收势，其强度为 $\eta$=0.01：

> ```qchem
> $complex_ccman
>    CAP_ETA     0000  CAP strength in 10-5 a.u. (0.00)
>    CAP_RE_ETA  1000  real CAP strength in 10-5 a.u. (0.01)
>    CAP_X    2760  CAP onset along X in 10^-3 bohr (2.76 bohr)
>    CAP_Y    2760  CAP onset along Y in 10^-3 bohr (2.76 bohr)
>    CAP_Z    4880  CAP onset along Z in 10^-3 bohr (4.88 bohr)
>    CAP_TYPE 1     Use cuboid cap (CAP_TYPE=0/2 will use spherical/Voronoi CAP)
> $end
> ```

CAP_TYPE 字段指定 CAP 的类型。目前的
选项有：球形 CAP（CAP_TYPE = 0）、长方体（cuboid）CAP
（CAP_TYPE = 1），以及平滑 Voronoi[[1283]](../bib_references/bib.md#bib1341)
 CAP
（CAP_TYPE = 2）。在采用 Voronoi CAP 的计算中，起始位置（onset）由 CAP_X 变量指定。

CS_THETA 以 弧度$\times$ 10${}^{-3}$ 为单位指定。
CS_ALPHA、CAP_X/Y/Z 以 a.u. $\times$
10${}^{-3}$ 为单位指定，*即*，CS_THETA = 10 表示 $\theta=0.01$；CAP_ETA
以 $10^{-5}$ $E_{h}$ 为单位指定。CAP 通过数值积分计算，默认网格为
($N_{r}=99,N_{\Omega}=590$)。
为检验数值积分的精度，程序会计算数值重叠矩阵并与解析结果进行比较。
如果默认网格的表现不佳，可以通过关键字 XC_GRID 更改网格类型（详见
[第 5.5 节](../ch05_dft/sect_quadrature.md)）。执行 CAP 计算时，CC_EOM_PROP 默认为 1；
这对于计算一阶微扰修正是必需的。

使用 CBF 的 EOM-CC（见[第 4.9.5 节](../ch04_scf/sec_cbfscf.md)）通过设置
COMPLEX_CCMAN = TRUE 和 COMPLEX_EXPONENTS = TRUE 来启用。与平均场
计算一样，必须按照[第 8.7 节](../ch08_basis/sect_zbas.md)中的说明指定复基组。

高级用户可能会发现以下选项很有用。执行复数计算有若干种方式，*即*，复标度/CAP 可以
在所有层级（HF、CCSD、EOM）上启用，也可以不启用。当在后 Hartree-Fock 层级应用时，
CAP 既可以添加到 Fock 矩阵的所有区块，也可以仅限制在虚-虚（virtual-virtual）区块。
后一种方法称为投影 CAP（projected CAP）[[1197]](../bib_references/bib.md#bib1251)，
它通过减小 CAP 经由占据轨道空间对目标态造成的微扰，
提高了计算结果相对于 CAP 起始位置的稳定性。

此类 CAP 投影目前仅对 EE/EA 计算实现，通过在 *$complex_ccman* 段中设置
PROJ_CAP 关键字来调用，方式如下。PROJ_CAP = 1 启用 CAP/EOM-CCSD，
在 CCSD 和 EOM 步骤中加入投影 CAP；PROJ_CAP = 2 启用
CAP/EOM-CCSD/MP2/MP2T，在 EOM 步骤中加入投影 CAP。后者意味着
$T$ 振幅（见[第 7.9.3 节](sec_EOMEE.md)）来自实数计算（CAP 强度为零），并且可以通过在
*$complex_ccman* 中指定 ETA_STEP 和 NSTEPS 参数来复用它们，
从而生成复本征值轨迹（eigenvalue trajectories）。

PROJ_CAP = 3 启用另一种形式的 CAP 投影 [[1284]](../bib_references/bib.md#bib1340)，
其中 CAP 哈密顿量被投影到由一组预先计算的 EOM 本征矢所张成的子空间上。默认情况下，
激发态本征矢来自单次实数计算，并且在输出文件中针对每个不可约表示打印以态基表示的 CAP 矩阵。
该功能适用于所有可在 EOM 目标态之间计算跃迁性质的 EOM-CC 模型。
要生成本征值轨迹，应将 CAP_ETA 设为非零的 CAP 强度，后续各点通过在
*$complex_ccman* 中指定 ETA_STEP 和 NSTEPS 参数来设定。轨迹会为每个不可约表示
写入单独的输出文件。此外，通过设置 PROJ_PROP = 1 可以获得一阶微扰修正。注意，
当 PROJ_PROP = 1 时，初始的一组实数本征矢是在复数代码、CAP 强度为零的条件下得到的。
因此，一阶微扰修正仅对复数 EOM-CC 模型可用。当 GUI = 2 且 PROJ_CAP = 3 时，
各态对之间完整的一粒子态密度矩阵与跃迁密度矩阵（OPDM）集合（这正是 CAP 投影所需的全部内容）
将被导出到检查点（checkpoint）文件以供进一步分析。

默认情况下，如果指定了 COMPLEX_CCMAN，EOM 计算将使用复数代码执行。
其他参数的设置如下：

> ```qchem
> $complex_ccman
>   CS_HF   = true
>   CS_CCSD = true
> $end
> ```

或者，用户可以禁用复数 HF。这些选项属于实验性质，
只应由高级用户使用。对于 CBF-EOM-CC，目前仅实现了 CS_HF =
TRUE 和 CS_CCSD = TRUE。

所有复标度和 CAP 增强的 CC/EOM-CC 模型均可使用非迭代三重激发（non-iterative triples）
修正，其请求方式与常规 CC/EOM-CC 相同（详见[第 7.9.27 节](sec_SD3.md)）。

为了考虑环境对电子共振的影响，CAP-EOM-CCSD 和 CBF-EOM-CCSD 可以与基于投影的嵌入
（projection-based embedding）[[1043]](../bib_references/bib.md#bib1088) 相结合，
具体描述见[第 7.9.3.1 节](sec_EOMEE.md#subsec:eomcc-pbe)和[第 11.6 节](../ch11_env/sect_den_emb.md)。

复标度或 CAP 增强的 CC/EOM-CC 计算可以像常规 CC/EOM-CC 一样请求分子性质和跃迁矩
（详见[第 7.9.21 节](sec_EOMGRAD.md)）。可以计算自然轨道（natural orbitals）和
自然跃迁轨道（natural transition orbitals），也可以分析激子（exciton）波函数，
其用法与实数 EOM-CCSD 相同（使用相同的关键字调用分析）。解析梯度对于复数 CC/EOM-CC
仅在长方体 CAP（CAP_TYPE = 1）且在 HF 层级引入（CS_HF = TRUE）时可用，
如文献 [[108]](../bib_references/bib.md#bib95) 所述。
对于 CAP-CC/EOM-CC 梯度计算，冻结芯层（frozen-core）近似会被禁用。
几何优化的请求方式与常规 CC/EOM-CC 相同（详见[第 7.9.21 节](sec_EOMGRAD.md)）。

## 7.9.10.1 复数 RI-EOM-CCSD

为降低内存需求，可以调用 RI 近似（resolution-of-identity approximation）来分解
电子排斥积分。该代码的结构与实数 RI-EOM-CCSD[[366]](../bib_references/bib.md#bib762)
相同，但采用复数 RI 分解[[1397]](../bib_references/bib.md#bib592)。
RI 近似可用于 CCSD 以及 EOM-IP/EA/EE/SF-CCSD，并与复标度、复基函数
以及复吸收势结合使用[[185]](../bib_references/bib.md#bib180)。
通过将 AUX_BASIS 设置为用户选定的辅助基组（*例如* RIMP2-aug-cc-pVTZ）即可调用。
对于使用复基函数的计算，还需要指定 COMPLEX_AUX_BASIS，
它通常与 AUX_BASIS 相同。使用用户自定义的辅助基组时，AUX_BASIS 在
*$aux_basis* 段中指定，而 COMPLEX_AUX_BASIS 在 *$aux_zbasis* 段中指定。
复数 RI 积分目前仅可用于能量和非弛豫（unrelaxed）单电子性质。
也可以将 RI 近似用于通过分解 CCSD 能量或通过 ACP 方法确定俄歇（Auger）
部分衰变宽度（见[第 7.9.11 节](sec_Auger.md)和[第 7.9.12 节](sec_AugerComplexVariable.md)）。

## 7.9.10.2 复数 RI-EOM-CC2

RI-EOM-CC2 方法同样可用于描述通过电子附着（electron attachment, EA）形成的亚稳态，
并与复吸收势（CAP）和复基函数（CBF）结合使用。CCMAN2 和 LIBGMBPT 模块中各有一种实现，
二者在算法效率和所支持的功能上有所不同。

CCMAN2 实现遵循与 RI-EOM-CCSD 类似的代码结构，可以通过在输入中指定 method = CCMAN2
来调用。然而，该实现并未采用最高效的算法，因为双激发振幅不是*即时（on-the-fly）*计算的。
因此，其内存需求仍为 $\mathcal{O}(N^{4})$，与 EOM-CCSD 相同。

LIBGMBPT 实现基于更高效的算法，将内存需求降低到 $\mathcal{O}(N^{3})$，
因此是较大体系的首选。EA-CC2 的自旋缩放（spin-scaled）变体，包括自旋分量缩放
（spin-component-scaling, SCS）和缩放反自旋（scaled opposite-spin, SOS），
也仅在该模块中提供，并可以按与 MP2 相同的方式调用（见[第 6.6.5 节](../ch06_correlation/topic_sbmp2.md)）。

在该实现中，未采用实数 EOM-CC2 中所使用的 Davidson/DIIS 混合求解器
（见[第 7.9.4 节](sec_eomcc2.md)）。取而代之的是，引入了一种改进的 Davidson
算法来求解电子附着的 CC2 赝本征值方程。

有若干输入特性值得注意。用户可以通过指定 EOM_USER_GUESS 关键字以及
*$eom_user_guess* 段来针对特定的附着态，其用法与 EOM-CC 中相同
（见[第 7.9.16 节](subsec_EOM-CC-diag.md)）。LIBGMBPT 中的轨道编号从第一个占据轨道开始，
与 CCMAN2 中从第一个空轨道开始不同，并且必须从轨道总数中减去冻结芯层轨道。
此外，通过设置 *$eom_user_guess* = 2，可以请求使用用户自定义猜测来顺序计算多个根。

最后，该实现尚不支持点群对称性。关于该实现及其在瞬态阴离子上性能的更多细节，
可参见文献 [[1382]](../bib_references/bib.md#bib1443)。

LIBGMBPT 实现可以通过设置 CCMAN2 = –1 来调用，当前默认值为 CCMAN2。
