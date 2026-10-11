---
title: "7.9.11 俄歇光谱与核心能级态寿命"
---

## 7.9.11 俄歇光谱与核心能级态寿命

（2026 年 7 月 4 日）

某些类型的共振态可以借助 Feshbach–Fano 方法，通过实数值的 EOM-CC 波函数来描述。[[384]](../bib_references/bib.md#bib392)
本节描述 Feshbach–Fano 方法在核心激发态与核心电离态中的应用。[[1262]](../bib_references/bib.md#bib1316)

空穴态（core-hole state）属于 Feshbach 共振，会发生自电离——通常称为俄歇（Auger）衰变。俄歇电子能谱（Auger Electron Spectroscopy, AES）测量的是被发射电子的动能与强度。俄歇电子的能量由初始空穴态与最终衰变态之间的能量差计算得到。例如，对于常规俄歇衰变：

<a id="eq:Echannel_a"></a>

$$
E_{\text{Auger}}^{\mu n}=E_{n}^{\text{CoreIP}}-E_{\mu}^{\text{DIP}}, \tag{7.104}
$$

其中 $E_{n}^{\text{CoreIP}}$ 与 $E_{\mu}^{\text{DIP}}$ 分别是初始（空穴）态和最终（双电离价态）态的能量。
各衰变通道的强度由部分衰变宽度 $\Gamma_{\mu n}$ 给出。
在最粗略的近似下，可以将每个衰变通道赋予单位强度——如此计算得到的俄歇谱反映的是体系中双电离态的态密度。
若采用更严格的处理方式，衰变宽度可以通过 Feshbach–Fano 方法或复变量方法[[1262]](../bib_references/bib.md#bib1316)

来计算，用于处理电子共振（后一种方法在第 7.9.11 节与 [7.9.12](sec_AugerComplexVariable.md) 节中描述）。

Feshbach–Fano 理论[[384]](../bib_references/bib.md#bib392)
引入两个投影算符 $\hat{Q}$ 和 $\hat{P}$，将总波函数分解为类束缚（bound-like）分量与类连续（continuum-like）分量。对于核心能级态，这一分离可以通过在计算俄歇过程的初态与末态时采用 CVS 方案以及冻结芯（frozen-core）近似来实现（关于 CVS 的更多细节见第 [7.9.9](sub_cvs_eom.md) 节）。

初始（类束缚）态 $\Psi_{0}$ 是一个空穴电离态或空穴激发态，可以由 CVS-EOM-CC 描述。
最终（类连续）态 $\chi_{\mu,E_{k}}$ 表示为一个稳定通道态 $\Psi_{\mu}$（由合适的 EOM-CC 模型描述）与一个连续轨道 $\phi_{k}$ 的反对称化乘积，
即 $\chi_{\mu,E_{k}}\sim{\cal{A}}\{\phi_{k}\Psi_{\mu}\}$。
注意 $\Psi_{\mu}$ 比 $\Psi_{0}$ 少一个电子。定义 AES 的两个关键参数是衰变进入通道 $\mu$ 的速率，其表达式为

<a id="eqn:gamma"></a>

$$
\Gamma_{\mu}=2\pi\langle\Psi_{0}^{L}|\hat{H}-E_{0}|\chi_{\mu,E_{k}}^{R}\rangle\langle\chi_{\mu,E_{k}}^{L}|\hat{H}-E_{0}|\Psi_{0}^{R}\rangle, \tag{7.105}
$$

以及相对于零阶共振位置 $E_{0}$ 的部分能量修正 $\Delta_{\mu}$，定义为

<a id="eqn:delta"></a>

$$
\Delta_{\mu}=P.V.\int_{0}^{\infty}\frac{\langle\Psi_{0}^{L}|\hat{H}-E_{0}|\chi_{\mu,E}^{R}\rangle\langle\chi_{\mu,E}^{L}|\hat{H}-E_{0}|\Psi_{0}^{R}\rangle}{E_{0}-E_{\mu}-E}dE. \tag{7.106}
$$

在上述表达式中，$\hat{H}$ 是电子哈密顿量，$E_{\mu}$ 是通道态 $\Psi_{\mu}$ 的能量，$E_{k}$ 是被发射电子的能量（$E_{k}=E_{0}-E_{\mu}$），
上标 $L/R$ 表示左右 EOM-CCSD 波函数，$P.V.$ 表示柯西主值（Cauchy principle value）。
$\Gamma_{\mu}$ 的计算通过 CC_DO_FESHBACH 关键字启用。
默认情况下，连续轨道 $\phi_{k}$ 用平面波来近似。[[1262]](../bib_references/bib.md#bib1316)

也可以通过设置 CC_FESHBACH_CW = 1，用库仑波（Coulomb wave）来模拟 $\phi_{k}$。
该选项需要一个额外的输入段 *$coulomb_wave*，其中提供库仑波的参数，用于将库仑波按平面波与高斯型函数乘积（PW-CGTOs）展开，详见文献 [[1262]](../bib_references/bib.md#bib1316)
。各参数列举如下。

> ```qchem
> $coulomb_wave
>    lmax   =   4      ! Maximum angular momentum in the pseudo partial wave expansion
>    ncoeff =   6      ! Number of contraction coefficient for each \emph{l}
>    Rmin   =   0.05   ! PW-CGTO grid in atomic unit
>    Rmax   =   10
>    Rmid   =   2
>    Charge =   6.2    ! Effective charge of the Coulomb wave
>    cwave_center = 1  ! Atom index for the position of Coulomb wave. Starts from 1.
>    print_cw = false  ! For printing the partial wave and the PW-CGTO basis
> $end
> ```

库仑波由 PW-CGTO 的线性组合来近似。通常，*lmax* = 4-6 与 *ncoeff* = 6-8 即可提供良好的近似；
增大这些取值会显著提高计算成本。
网格由 *Rmin*、*Rmax* 和 *Rmid* 参数设定。
若指定了 *Rmid*，则从 *Rmin* 到 *Rmid* 的网格间距设为 0.05 bohr，从 *Rmid* 到 *Rmax* 设为 0.1 bohr。
若未提供 *Rmid*，则使用 0.1 bohr 的均匀网格间距。网格应当足够大，以便在衰变所涉及的定域-区域（bound-domain）轨道具有显著振幅的空间内准确表示连续函数。
*cwave_center* 设定库仑波的位置。默认情况下它位于原点（*cwave_center = 0*）。
用户可以通过在输入中定义一个虚原子（Ghost atom, Gh）并将其序号设为 *cwave_center*，把库仑波中心放置在某个特定原子上，或放置在任意其他位置，例如键的中点。
*print_cw* 选项会输出库仑波、其拟合表示形式（对每个 *l*）以及相应的库仑基组。
用户可以在 **Q-Chem** 输出文件中检查 *Fit square error:*（拟合平方误差），并通过改变 *ncoeff* 相应地调整这些参数。

也可以通过设置 CC_FESHBACH_CW = 3，在 *$coulomb_wave* 输入段中直接给出在外部优化（针对给定有效电荷与动能）得到的库仑波按 PW-CGTO 的展开式。

Feshbach 宽度的实现包含对发射电子所有可能方向（**k** 矢量）的数值积分。这一球面积分采用 Lebedev 求积完成，默认阶数为 5。
对于空穴态离域的分子（例如苯），可能需要更高阶的求积。求积阶数由 CC_FESHBACH_INT_ORDER 控制。
下面的示例 [7.9.11.2](#ex:auger1) 和 [7.9.11.2](#ex:auger1) 演示了分别使用平面波与库仑波处理方式计算俄歇衰变速率。

对于非共振俄歇衰变，初态可以由 CVS-EOM-IP-CCSD 方便地计算，其稳定衰变通道可以由 EOM-DIP-CCSD 计算。
调用原子俄歇衰变速率计算的一个输入段示例如下：

> ```qchem
> $rem
>    JOBTYPE         sp
>    METHOD          eom-ccsd
>    basis           6-31G*
>    CVS_EOM_IP_BETA [1,0,0,0,0,0,0,0] !This is the initial core-hole state
>    DIP_TRIPLETS    [0,0,0,0,0,1,1,1] !These are the final triplet decay channels
>    DIP_SINGLETS    [3,1,1,1,0,1,1,1] !These are the final singlet decay channels
>    CC_DO_DYSON     1                 !Needed for Feshbach-type calculations
>    CC_DO_FESHBACH  1
> $end
> ```

在共振俄歇衰变中，初态可以由 CVS-EOM-EE-CCSD 计算，相应的衰变通道可以由 EOM-IP-CCSD 计算。
默认情况下，Feshbach 计算会针对所有包含能量上允许衰变通道的可能态对进行。
然而，如果所关注的空穴态在给定对称性下并非最低态，或者使用库仑波来模拟连续轨道，这种做法并不实用。
在这种情况下，用户可以使用 *$trans_prop* 段并以 $dyson$ 作为请求的性质来指定进行 Feshbach 计算的态对：

> ```qchem
> $trans_prop
>    state_list
>    cvs_ip_beta  1 1 !state 1: CVS_IP with irrep = 1 and istate = 1
>    dip_singlets 1 3 !state 2: DIP_SINGLET state with irrep = 1 and istate = 3
>    dip_triplets 6 1 !state 3: DIP_TRIPLET state with irrep = 6 and istate = 1
>    end_list
>    state_pair_list
>    1 2   ! transition 1 <-> 2
>    1 3   ! transition 1 <-> 3
>    end_pairs
>    calc dyson
> $end
> ```

将 CC_DO_FESHBACH = 2 即可启用能量修正 $\Delta_{\mu}$ 的计算，
目前该功能仅在平面波近似下可用。

式 ([7.105](#eqn:gamma)) 中的积分以解析方式求值。式 ([7.106](#eqn:delta)) 中的积分数值求值，并被拆分为两个或三个区间，以绕过 $E=E_{0}-E_{\mu}$ 处的奇点。
这些区间的上限默认设置为与 $E_{0}$ 相关的值。用户也可以通过设置 CC_FESHBACH_DELTA_INTB = XX 和/或 CC_FESHBACH_DELTA_INTC = YY 来自定义上限（第一个区间除外），
其中 XX 和/或 YY 是以 eV 为单位的期望积分上限。

俄歇过程（或其他双电子衰变过程，如分子间库仑衰变与电子转移介导衰变）的分子轨道描述，可以通过对双粒子戴森振幅（$\Gamma_{\mu}$）进行奇异值分解获得[[631]](../bib_references/bib.md#bib655)
。该 procedure 会给出若干三轨道组合，它们代表空位态与价层衰变态。这些组合称为自然俄歇轨道（Natural Auger Orbitals, NAOs），能够对双电子衰变过程给出最为紧凑的描述[[631]](../bib_references/bib.md#bib655)
。在 Feshbach 计算中，可以通过 CC_DO_NAO 关键字启用 NAO 的计算。NAO 以 **MolDen** 格式输出在工作目录下创建的子目录中。其“能量”为奇异值的平方（未归一化），空穴 NAO 被赋予占据数 1，价层衰变 NAO 被赋予占据数 0。
输出 NAO 的默认阈值为 0.20，用户可以使用 WFA_ORB_THRESH 关键字控制该阈值（见第 [10.2](../ch10_properties/sec_wfa.md) 节）。下面的示例 [7.9.11.2](#ex:auger1)、[7.9.11.2](#ex:auger1) 和 [7.9.11.2](#ex:auger1) 演示了这一功能。

**注意：

NAO 是使用二体戴森振幅的 $\Gamma_{r\beta}^{p\alpha,q\beta}$ 分块计算得到的。这意味着在非共振俄歇衰变计算中，空穴应当对应于移除一个 $\beta$ 电子。
**

CC_DO_FESHBACH

### `CC_DO_FESHBACH`

> **使用 Feshbach-Fano 方法启用共振宽度计算。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 不进行 Feshbach-Fano 计算
>     * 1
>     * 进行 Feshbach-Fano 共振宽度计算
>     * 2
>     * 进行 Feshbach-Fano 共振宽度与共振位移计算
> * **建议**: 应正确指定初态和末态。

CC_FESHBACH_CW

### `CC_FESHBACH_CW`

> **启用被发射电子的库仑波描述。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 使用平面波
>     * 1
>     * 使用内部生成的库仑波
>     * 3
>     * 使用用户在
>     * $coulomb_wave
>     * 段中提供的库仑基组
> * **建议**: 需要在 $coulomb_wave 段中指定额外的细节。

CC_FESHBACH_INT_ORDER

### `CC_FESHBACH_INT_ORDER`

> **控制使用 Feshbach-Fano 方法计算共振宽度时的 k 矢量积分网格。**
>
> * **类型**: `INTEGER`
> * **默认值**: `5`
> * **选项**:
>     * $n$
>     * 对应 Lebedev 求积的阶数
> * **建议**: 使用默认值，除非需要更严格的收敛（取 16 可获得完全收敛的宽度）。

CC_FESHBACH_DELTA_INTB

### `CC_FESHBACH_DELTA_INTB`

> **指定 Feshbach-Fano 计算中能量位移计算的积分上限。**
>
> * **类型**: `INTEGER`
> * **默认值**: `Preset`
> * **选项**:
>     * $n$
>     * 对应以 eV 为单位的能量上限
> * **建议**: 使用默认值。

CC_FESHBACH_DELTA_INTC

### `CC_FESHBACH_DELTA_INTC`

> **指定 Feshbach-Fano 计算中能量位移计算的积分上限。**
>
> * **类型**: `INTEGER`
> * **默认值**: `Preset`
> * **选项**:
>     * $n$
>     * 对应以 eV 为单位的能量上限
> * **建议**: 使用默认值。

CC_DO_NAO

### `CC_DO_NAO`

> **在衰变宽度的 Feshbach–Fano 计算中启用 NAO 计算。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 0
>     * 不计算 NAO
>     * 1
>     * 计算 NAO
> * **建议**: 应正确指定初态和末态。

## 7.9.11.1 单中心近似

显式处理连续轨道 $\phi_{k}$ 的俄歇衰变 Feshbach–Fano 计算[[1262]](../bib_references/bib.md#bib1316)
需要求值束缚–连续混合的双电子积分，这是一个计算量很大的步骤。
此外，目前可用的 $\phi_{k}$ 模型只允许平面波或库仑波处理方式，其结果并不总是令人完全满意。

一种被广泛使用且计算高效的、替代显式处理连续态的方法，是单中心近似（one-center approximation, OCA）。[[1264]](../bib_references/bib.md#bib1318)
在该方法中，束缚–连续积分被替换为预先算好的原子积分：

<a id="Ch7.E107"></a>

$$
\langle\phi_{p}\phi_{q}||\phi_{k}\phi_{r}\rangle\approx\sum_{\mu\nu\rho}\langle\chi_{\mu}^{A}\chi_{\nu}^{A}||\chi_{E,lm}^{A}\chi_{\rho}^{A}\rangle D_{\mu p}D_{\nu q}D_{\rho r}. \tag{7.107}
$$

这里 $\langle\chi_{\mu}^{A}\chi_{\nu}^{A}||\chi_{E,lm}^{A}\chi_{\rho}^{A}\rangle$ 表示预计算的原子积分，
$D_{\mu p}$ 是通过对所选极小基组（Minimal Basis Set, MBS）投影分子基函数而构造的变换矩阵。

与上文描述的标准 Feshbach–Fano 设置类似，OCA 计算需要指定初始核心电离态（CVS-EOM-IP 或 CVS-EOM-EE）以及最终衰变通道（EOM-DIP 或 EOM-IP）。
该方法由两个关键字控制：CC_FESHBACH_OCA 和 OCA_ATOM_INDEX。
关键字 CC_FESHBACH_OCA 启用 OCA 计算，目前支持两个选项：1 表示 $1s$ 空穴（K-LL、K-LM 和 K-MM 衰变），2 表示 $2s$ 空穴（仅 L1-MM 衰变）。
关键字 OCA_ATOM_INDEX = $n$ 指定空穴定域所在的原子。编号从 1 开始，遵循 *$molecule* 段中给出的顺序。
对于较大体系，建议使用 PRINT_ORBITALS 选项以核实空穴轨道是否被正确识别。
对于空穴在对称性等价原子间离域的情形（例如苯，或 CO${}_{2}$ 的 O-edge），OCA_ATOM_INDEX 可以对应任一等价原子。
给定通道 $\mu$ 的最终衰变宽度 $\Gamma$ 由对相应的对称性等价空穴态 $\Psi_{0}$ 求和得到。

此外，OCA 计算需要通过 *$mbasis* 段指定一个极小基组（MBS）。基函数的排序很重要，必须遵循壳层结构：
$(1s,2s,2p,\ldots)$。已有工作测试了两种用于 OCA-EOM-CCSD 计算的 MBS 选择[[1264]](../bib_references/bib.md#bib1318)
：cc-pVTZ 基组的一个子集，以及 STO-3G。

示例 [7.9.11.2](#ex:auger1) 和 [7.9.11.2](#ex:auger1) 演示了 OCA 计算。

CC_FESHBACH_OCA

### `CC_FESHBACH_OCA`

> **通过 OCA 方法启用俄歇宽度计算。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **选项**:
>     * 1
>     * 1s 空穴
>     * 2
>     * 2s 空穴。
> * **建议**: 无

OCA_ATOM_INDEX

### `OCA_ATOM_INDEX`

> **定义带有空穴的原子。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * $n$
>     * 遵循 molecule 段中的顺序。
> * **建议**: 无

## 7.9.11.2 示例

示例 [7.9.11.2](#ex:auger1) 和 [7.9.11.2](#ex:auger1) 演示了核心电离水分子的共振俄歇衰变计算。初态由 CVS-EOM-IP-CCSD 描述，衰变通道由 EOM-DIP-CCSD 描述。
示例 [7.9.11.2](#ex:auger1) 对被发射电子采用平面波表示。
在示例 [7.9.11.2](#ex:auger1) 中，自电离电子由库仑波描述，并通过在 PW-CGTO 函数上的伪部分波展开来表示。
示例 [7.9.11.2](#ex:auger1)、[7.9.11.2](#ex:auger1) 和 [7.9.11.2](#ex:auger1) 演示了常规俄歇衰变与共振俄歇衰变中 NAO 的计算。

???+ example "示例 7.79: 计算核心电离水分子衰变到若干选定单重态与三重态末态的俄歇衰变速率。连续轨道为平面波。"
    ```qchem
    $molecule
    0 1
       O         0.0000    0.000    0.0000
       H        -0.7528    0.000   -0.5917
       H         0.7528    0.000   -0.5917
    $end
    
    $rem
       METHOD            ccsd
       BASIS             6-311+G(3df)
       CVS_EOM_IP_BETA   [1,0,0,0]
       DIP_SINGLETS      [4,1,2,2]
       DIP_TRIPLETS      [1,1,2,2]
       CC_DO_DYSON       1
       CC_DO_FESHBACH    1
    $end
    ```

???+ example "示例 7.80: 计算核心电离水分子衰变到若干选定单重态与三重态末态的俄歇衰变速率。连续轨道由库仑波近似。"
    ```qchem
    $molecule
    0 1
       O         0.0000    0.000    0.0000
       H        -0.7528    0.000   -0.5917
       H         0.7528    0.000   -0.5917
    $end
    
    $rem
       METHOD            ccsd
       BASIS             6-311+G(3df)
       CVS_EOM_IP_BETA   [1,0,0,0]
       DIP_TRIPLETS      [1,1,2,2]
       CC_DO_DYSON       1
       CC_DO_FESHBACH    1
       CC_FESHBACH_CW    1
    $end
    
    $trans_prop
    state_list
      cvs_ip_beta  1 1
      dip_triplets 3 2
    end_list
    state_pair_list
      1 2   ! transition 1 <-> 2
    end_pairs
    calc dyson
    $end
    
    $coulomb_wave
    lmax = 4
    ncoeff = 6
    Rmin = 0.05
    Rmax = 10
    Rmid = 2
    Charge = 4.9
    cwave_center = 1  !CW is centered on oxygen (atom #1)
    print_cw = false
    $end
    ```

???+ example "示例 7.81: 计算水中常规（非共振）俄歇衰变的自然俄歇轨道，同时包含单重态与三重态衰变通道。"
    ```qchem
    $comment
    NAO calculation - regular Auger decay in water
    $end
    
    $molecule
    0 1
    O         0.0000    0.000    0.0000
    H        -0.7528    0.000   -0.5917
    H         0.7528    0.000   -0.5917
    $end
    
    
    $rem
    jobtype              sp
    method               eom-ccsd
    basis                6-31g
    cvs_eom_ip_beta      [1,0,0,0]  !Initial core-hole state
    dip_singlets         [1,1,0,0]  !Final singlet decay channels
    dip_triplets         [0,1,0,0]  !Final triplet decay channels
    cc_do_dyson          1          !Needed for Feshbach-type calculations
    cc_do_feshbach       1          !Needed for Feshbach-type calculations
    cc_do_nao            1          !Needed for natural Auger orbitals
    wfa_orb_thresh       1          !Setting the threshold for singular value dceomposition
    mem_total            4000
    $end
    
    
    ```

???+ example "示例 7.82: 计算苯中常规（非共振）俄歇衰变的自然俄歇轨道，同时包含单重态与三重态衰变通道，并针对若干空穴态。"
    ```qchem
    $comment
    NAO calculation - regular Auger decay in benzene
    $end
    
    $molecule                                                                                                                         0 1
      H   2.4750347531   0.0000000000   0.0000000000
      C   1.3935929418   0.0000000000   0.0000000000
      C   0.6967964709   1.2068868901   0.0000000000
      H   1.2375173766   2.1434429715   0.0000000000
      C  -0.6967964709   1.2068868901   0.0000000000
      H  -1.2375173766   2.1434429715   0.0000000000
      C  -1.3935929418   0.0000000000   0.0000000000
      H  -2.4750347531   0.0000000000   0.0000000000
      C  -0.6967964709  -1.2068868901   0.0000000000
      H  -1.2375173766  -2.1434429715   0.0000000000
      C  0.6967964709   -1.2068868901   0.0000000000
      H  1.2375173766   -2.1434429715   0.0000000000
    $end
    
    $rem
    jobtype             sp
    method              ccsd
    basis               6-31g
    cvs_eom_ip_beta     [1,0,0,0,0,0,1,1] !Initial core-hole state
    dip_singlets        [2,0,0,1,0,0,0,0] !Final singlet decay channel
    dip_triplets        [1,0,0,1,0,0,0,0] !Final triplet decay channel
    cc_do_dyson         1                 !Needed for Feshbach-type calculation
    cc_do_feshbach      1                 !Needed for Feshbach-type calculation
    cc_do_nao           1                 !Needed for natural Auger orbital calculation
    mem_total           8000
    $end
    ```

???+ example "示例 7.83: 计算水中共振俄歇衰变的自然俄歇轨道。"
    ```qchem
    $comment
    NAO calculation - resonant Auger decay in water
    $end
    
    $molecule
    0 1
    O         0.0000    0.000    0.0000
    H        -0.7528    0.000   -0.5917
    H         0.7528    0.000   -0.5917
    $end
    
    
    $rem
    jobtype              sp
    method               eom-ccsd
    basis                6-31g
    cvs_ee_states        [1,0,0,0]  !Initial core-hole state
    ip_states            [1,0,1,0]  !Final  decay channels
    cc_do_dyson          1          !Needed for Feshbach-type calculations
    cc_do_feshbach       1          !Needed for Feshbach-type calculations
    cc_do_nao            1          !Needed for natural Auger orbitals
    mem_total            4000
    $end
    
    
    ```

???+ example "示例 7.84: 使用 OCA 计算核心电离水分子的俄歇衰变速率"
    ```qchem
    $comment
    OCA-EOM-CCSD Auger width calculation for core-ionized H2O(1s^-1)
    $end
    
    $molecule
    0 1
    O         0.0000    0.000    0.0000
    H        -0.7528    0.000   -0.5917
    H         0.7528    0.000   -0.5917
    $end
    
    $rem
    jobtype = sp
    basis = cc-pVTZ
    method = ccsd
    dip_singlets [1,0,0,0]
    cvs_eom_ip_beta [1,0,0,0]
    cc_do_dyson 1
    cc_feshbach_oca = 1 ! 1s core
    oca_atom_index = 1  ! Core localized on oxygen atom
    $end
    
    $mbasis
    !Subset of cc-pVTZ  used as Minimal Basis Set
    H     0
    S   5   1.00
          3.387000D+01           6.068000D-03
          5.095000D+00           4.530800D-02
          1.159000D+00           2.028220D-01
          3.258000D-01           5.039030D-01
          1.027000D-01           3.834210D-01
    ****
    O     0
    S   10   1.00
          1.533000D+04           5.080000D-04
          2.299000D+03           3.929000D-03
          5.224000D+02           2.024300D-02
          1.473000D+02           7.918100D-02
          4.755000D+01           2.306870D-01
          1.676000D+01           4.331180D-01
          6.207000D+00           3.502600D-01
          1.752000D+00           4.272800D-02
          6.882000D-01          -8.154000D-03
          2.384000D-01           2.381000D-03
    S   10   1.00
          1.533000D+04          -1.150000D-04
          2.299000D+03          -8.950000D-04
          5.224000D+02          -4.636000D-03
          1.473000D+02          -1.872400D-02
          4.755000D+01          -5.846300D-02
          1.676000D+01          -1.364630D-01
          6.207000D+00          -1.757400D-01
          1.752000D+00           1.609340D-01
          6.882000D-01           6.034180D-01
          2.384000D-01           3.787650D-01
    P   5   1.00
          3.446000D+01           1.592800D-02
          7.749000D+00           9.974000D-02
          2.280000D+00           3.104920D-01
          7.156000D-01           4.910260D-01
          2.140000D-01           3.363370D-01
    ****
    $end
    
    ```

???+ example "示例 7.85: 使用 OCA 计算核心电离 CO ${}_{2}$ 分子的俄歇衰变速率"
    ```qchem
    $comment
    OCA-EOM-CCSD Auger width calculation for core-ionized CO2 (O-edge 1s^-1)
    The core orbital is delocalized over two oxygen atoms
    For equivalent core atoms (O1 and O2) the final result is the sum
    over the two initial cvs_ip states in irreps A1g and B1u
    oca_atom_index can be chosen as 2 or 3
    $end
    
    $molecule
    0 1
    C         0.0000000000    0.0000000000    0.0000000000
    O         0.0000000000    0.0000000000    1.1702258366
    O         0.0000000000    0.0000000000   -1.1702258366
    $end
    
    $rem
    jobtype = sp
    basis = cc-pVTZ
    method = ccsd
    dip_singlets [1,0,0,0,0,0,0,0]
    cvs_eom_ip_beta [1,0,0,0,0,1,0,0]
    cc_do_dyson 1
    cc_feshbach_oca = 1   ! 1s decay
    oca_atom_index = 2    ! Second atom (O1) is chosen as OCA core
    n_frozen_core = 2     ! O-edge
    $end
    
    $mbasis
    !STO-3G is used as Minimal Basis Set
    C     0
    S   3   1.00
          0.7161683735D+02       0.1543289673D+00
          0.1304509632D+02       0.5353281423D+00
          0.3530512160D+01       0.4446345422D+00
    SP   3   1.00
          0.2941249355D+01      -0.9996722919D-01       0.1559162750D+00
          0.6834830964D+00       0.3995128261D+00       0.6076837186D+00
          0.2222899159D+00       0.7001154689D+00       0.3919573931D+00
    ****
    O     0
    S   3   1.00
          0.1307093214D+03       0.1543289673D+00
          0.2380886605D+02       0.5353281423D+00
          0.6443608313D+01       0.4446345422D+00
    SP   3   1.00
          0.5033151319D+01      -0.9996722919D-01       0.1559162750D+00
          0.1169596125D+01       0.3995128261D+00       0.6076837186D+00
          0.3803889600D+00       0.7001154689D+00       0.3919573931D+00
    ****
    $end
    
    ```
