---
title: "7.7.2 最大重叠法"
---

## 7.7.2 最大重叠法（Maximum Overlap Method, MOM）

（2026 年 7 月 4 日）

最大重叠法（Maximum Overlap Method, MOM）是获取低成本激发态时，对组态相互作用单激发（Configuration Interaction with Singles, CIS）和含时密度泛函理论（Time-Dependent Density Functional Theory, TDDFT）的一种有用的替代方法。[[443]](../bib_references/bib.md#bib455)
它通过修改自洽场（Self-Consistent Field, SCF）过程中的轨道选择步骤来工作。通过选择与上一轮最相似的轨道，而非本征值最低的轨道，可以得到非*构造原理（aufbau）*的激发态 SCF 行列式，这种方法有时被称为
*激发态 Kohn-Sham 理论（excited-state Kohn-Sham theory）*。[[520]](../bib_references/bib.md#bib534)

这代表了一种“$\Delta$SCF”计算激发能的形式，

在某些情况下它相比 TDDFT 具有优势。例如，TDDFT 在描述电荷转移（charge-transfer）激发和里德堡（Rydberg）激发时存在系统性问题，

而这两者都可以用 $\Delta$SCF 方法来建模。MOM 的使用还允许用户
轻松地将目标定位于非常高能量的态，例如涉及核心电子激发的态，[[118]](../bib_references/bib.md#bib113)
而这些态用其他激发态方法难以捕捉。

为了使用 MOM 计算激发态，用户必须正确
识别跃迁中所涉及的轨道。例如，在
$\pi\rightarrow\pi^{\ast}$ 跃迁中，必须识别出 $\pi$ 和 $\pi^{\ast}$ 轨道，而这通常需要一次预备计算。随后用户
使用 *$occupied* 节来操控轨道占据数，从 $\pi$ 轨道移除一个
电子并将其放入 $\pi^{\ast}$ 轨道。然后调用 MOM 来
保持这一轨道占据。MOM 的成功取决于计算初始猜测（initial guess）的质量。如果虚轨道
质量较差，则计算可能“跌落”到相同对称性的更低能量
态。通常情况下，相应阳离子的虚轨道更适合作为激发态的初始猜测轨道使用。

由于 MOM 态是单行列式，**Q-Chem** 所有现有的
单行列式性质和导数都可用。这使得例如可以在激发态上计算
解析谐频（analytic harmonic frequencies）。来自 Hartree-Fock MOM 计算的轨道也可以用于 MP2
计算。对于所有激发态计算，在基组（basis set）中加入弥散函数（diffuse functions）非常重要。如果要寻找里德堡
跃迁，这一点尤其正确。对于基于 DFT 的方法，还建议增大
积分网格（quadrature grid）的规模，以便对更弥散的密度进行
准确积分。

由于其单行列式描述，
用于开壳层单重态非限制 $\Delta$SCF 计算的 MOM 算法常常存在严重的自旋污染（spin contamination）。
可以通过采用限制开壳层 Kohn-Sham（Restricted Open-Shell Kohn-Sham, ROKS）形式来缓解自旋污染
（参见第 [7.7.4](ex_ESROKS.md) 节），
其中优化目标函数 $E_{\text{S}}=2E_{\text{M}}-E_{\text{T}}$，
这里 $E_{\text{S}}$ 是自旋纯单重态能量，
$E_{\text{M}}$ 是“混合”（或自旋污染）开壳层单重态的能量，
而 $E_{\text{T}}$ 是三重态能量。
MOM 可以与 ROKS 结合使用，以评估任意开壳层单重态电子组态的自旋纯
能量（此前在 ROKS 公式中只能访问 $S_{1}$）。

基于 MOM 的 $\Delta$SCF 方法可以与基于极性连续介质模型（Polarizable Continuum Model, PCM）的溶剂化描述相结合，
以考虑平衡效应和非平衡效应
（更多细节参见第 [7.7.9](sect_ROKS_neq-PCM.md) 节）。

以下 *$rem* 用于调用 MOM：

### `MOM_START`

> **确定 MOM 在何时被启用以保持轨道占据。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0 (FALSE)`
> * **选项**:
>     * `0 (FALSE)`: 不使用 MOM
>     * $n$: MOM 从第
>     * $n$: 轮开始。
> * **建议**: 对于激发态计算，通常需要进行一次不含 MOM 的初始计算以获得令人满意的起始轨道。应通过设置 SCF_GUESS = TRUE 和 = 1 来读入这些轨道。

### `MOM_METHOD`

> **确定在每一轮 SCF 中用于最大化重叠的目标轨道。**
>
> * **类型**: `INTEGER`
> * **默认值**: `MOM`
> * **选项**:
>     * `MOM`: 与上一轮 SCF 的轨道最大化重叠。
>     * `IMOM`: 与初始猜测轨道最大化重叠。
> * **建议**: 如果能够获得合适的猜测轨道，则 IMOM 可以更可靠地收敛到所需的解。75 Barca G. M. J., Gilbert A. T. B., Gill P. M. W. J. Chem. Theory Comput. (2018) , 14 , pp. 1501 . 链接

???+ example "示例 7.46: CO 最低单重态的计算。"
    ```qchem
    $comment
       CO spin-purified calculation
       Step 1: prepare MOs
    $end
    
    $molecule
       0 1
       C
       O  C  1.05
    $end
    
    $rem
       METHOD            B3LYP
       BASIS             6-31G*
    $end
    
    @@@
    
    $comment
      Step 2: spin purification (OPSING=TRUE)
    $end
    
    $molecule
       read
    $end
    
    $rem
       METHOD            B3LYP
       BASIS             6-31G*
       SCF_GUESS         read
       MOM_START         1
       UNRESTRICTED      true
       OPSING            true
    $end
    
    $occupied
       1 2 3 4 5 6 7
       1 2 3 4 5 6 8
    $end
    ```

???+ example "示例 7.47: 用于获得对应 $\pi\rightarrow\pi^{\ast}$ 跃迁的甲酰胺 ${}^{2}$ A ${}^{\prime}$ 激发态的输入。
如果第二次计算中不使用 MOM，则会得到 ${}^{1}$ A ${}^{\prime}$ 基态。请注意
使用弥散函数和更大的积分网格以准确模拟
更大的激发态。"
    ```qchem
    $molecule
       1  2
       C
       H  1  1.091480
       O  1  1.214713  2  123.10
       N  1  1.359042  2  111.98  3  -180.00
       H  4  0.996369  1  121.06  2    -0.00
       H  4  0.998965  1  119.25  2  -180.00
    $end
    
    $rem
       METHOD         B3LYP
       BASIS          6-311(2+,2+)G(d,p)
       XC_GRID        000100000194
    $end
    
    @@@
    
    $molecule
       0  1
       C
       H  1  1.091480
       O  1  1.214713  2  123.10
       N  1  1.359042  2  111.98  3  -180.00
       H  4  0.996369  1  121.06  2    -0.00
       H  4  0.998965  1  119.25  2  -180.00
    $end
    
    $rem
       METHOD         B3LYP
       BASIS          6-311(2+,2+)G(d,p)
       XC_GRID        000100000194
       MOM_START      1
       SCF_GUESS      read
       UNRESTRICTED   true
    $end
    
    $occupied
       1:12
       1:11 13
    $end
    ```

此外，还可以在 MOM 激发的基础上进行 CIS/TDDFT 计算。在模拟泵浦-探测（pump-probe）
光谱时，这一功能非常有用。为了先运行 MOM 再运行 CIS/TDDFT，必须指定 *$rem* 变量
CIS_N_ROOTS。也可以使用截断子空间（truncated subspaces），参见第 [7.3.3](subsec_TRNSS.md) 节。

???+ example "示例 7.48: MOM 价层激发后接使用限制子空间的核心态 TDDFT"
    ```qchem
    $molecule
       0 1
       O    0.0000    0.0000    0.1168
       H    0.0000    0.7629   -0.4672
       H    0.0000   -0.7629   -0.4672
    $end
    
    $rem
       METHOD       B3LYP
       BASIS        aug-cc-pvdz
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD         B3LYP
       BASIS          aug-cc-pvdz
       SCF_GUESS      read
       MOM_START      1
       UNRESTRICTED   true
       CIS_N_ROOTS    5
       TRNSS          true  ! use truncated subspace for TDDFT
       TRTYPE         3     ! specify occupied orbitals
       CUTVIR         15    ! truncate high energy virtual orbitals
       N_SOL          1     ! number core orbitals, specified in $solute section
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    $solute
       1
    $end
    
    $occupied
       1 2 3 4 5
       1 2 3 4 6
    $end
    ```

如果 MOM 激发对应于一个核心空穴（core hole），则必须使用约化子空间
以避免向核心空穴的退激发。*$rem* 变量
CORE_IONIZE 允许只指定空穴，这样就不需要在 *$solute* 节中输入所有
占据轨道。

### `CORE_IONIZE`

> **指示在约化激发子空间中如何指定轨道。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * `1`: 所有价轨道都在 $solute 节中列出
>     * `2`: 只指定空穴，其他所有占据与基态相同
> * **建议**: 对于 MOM + TDDFT，这指定了 $solute 节的输入形式。若设为 1，则必须指定所有占据轨道；设为 2 时，只需指定要忽略的空轨道。

???+ example "示例 7.49: 使用 MOM 的 O(1s) 核心激发态，后接价轨道间的激发。请注意必须使用约化激发子空间以避免向空核心空穴的“激发”"
    ```qchem
    $molecule
       0 1
       O   0.0000   0.0000   0.1168
       H   0.0000   0.7629  -0.4672
       H   0.0000  -0.7629  -0.4672
    $end
    
    $rem
       METHOD       B3LYP
       BASIS        aug-cc-pvdz
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD            B3LYP
       BASIS             aug-cc-pvdz
       SCF_GUESS         read
       MOM_START         1
       UNRESTRICTED      true
       CIS_N_ROOTS       5
       TRNSS             true  ! use truncated subspace for TDDFT
       TRTYPE            3     ! specify occupied orbitals
       N_SOL             1     ! number core holes, specified in $solute section
       CORE_IONIZE       2     ! hole orbital specified
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $solute
       6
    $end
    
    $occupied
       1 2 3 4 5
       2 3 4 5 6
    $end
    ```
