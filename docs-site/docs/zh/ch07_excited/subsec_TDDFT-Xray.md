---
title: "7.12.2 使用 TDDFT 的 X 射线光谱计算"
---

## 7.12.2 使用 TDDFT 的 X 射线光谱计算

（2026 年 7 月 4 日）

## 7.12.2.1 吸收光谱

X 射线吸收光谱可以通过 TDDFT 计算，方法是将激发空间限制为仅包含来自一组核心轨道（core orbitals）的激发。
这通过在 *$rem* 段中设置 TRNSS = TRUE 来实现，该设置会触发使用带有截断激发空间的 TDDFT，具体描述见第 [7.3.3](subsec_TRNSS.md) 节。
用户希望在此类计算中处于活跃状态的已占据核心轨道，应当在 *$alist* 输入段中逐一列出，并且此类轨道的数目必须通过在 *$rem* 段中设置 N_SOL 来指定。
这会调用 CVS 近似（core-valence separated approximation），对于 TDDFT 而言，该近似相当于冻结除 *$alist* 中所列轨道之外的所有已占据轨道，同时使用完整的虚轨道空间。

此类计算不适合描述扩展 X 射线吸收精细结构（EXAFS）区域，该区域对应于电离电子被相邻原子散射的过程。

标准的交换-关联泛函（包括杂化泛函）往往会严重低估核心激发能[[123]](../bib_references/bib.md#bib112)，

尽管化学位移（从一个化合物到另一个化合物）可能仍然有效[[404]](../bib_references/bib.md#bib413)。**Q-Chem** 提供了短程校正（short-range corrected, SRC）泛函，
其设计目标是准确预测 K 边核心激发能[[123]](../bib_references/bib.md#bib112)。

这些泛函是对更常见的长程校正泛函（long-range corrected functionals，见第 [5.6](../ch05_dft/sect_LRC-DFT.md) 节）的一种修改。
然而在 SRC-DFT 中，库仑算符的短程分量主要以 Hartree-Fock 交换处理，而中程到长程分量则主要用标准 DFT 交换处理。
SRC 泛函的作业控制变量列于下文，其与 CVS 近似配合使用的示例见示例 [7.12.2.1](#ex:TDDFT-CVS-0)。
基本 TDDFT 作业控制参见第 [7.3.6.1](subsec_TDDFT-Control.md#subsec:TDDFT-Control:Basic) 节。

### `HF_SR`

> **设置在 $r_{12}=0$ 处 Hartree-Fock 交换的比例。**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值`
> * **选项**:
>     * $n$: 对应于 = $n/1000$
> * **建议**: 无

### `HF_LR`

> **设置在 $r_{12}=\infty$ 处 Hartree-Fock 交换的比例。**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值`
> * **选项**:
>     * $n$: 对应于 = $n/1000$
> * **建议**: 无

### `OMEGA`

> **设置短程分量的库仑衰减（attenuation）参数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值`
> * **选项**:
>     * $n$: 对应于 $\omega=n/1000$，单位为 bohr ${}^{-1}$
> * **建议**: 无

### `OMEGA2`

> **设置长程分量的库仑衰减参数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值`
> * **选项**:
>     * $n$: 对应于 $\omega_{2}=n/1000$，单位为 bohr ${}^{-1}$
> * **建议**: 无

### `SRC_DFT`

> **选择短程校正泛函的形式。**
>
> * **类型**: `INTEGER`
> * **默认值**: `无默认值`
> * **选项**:
>     * `1`: SRC1 泛函。
>     * `2`: SRC2 泛函。
> * **建议**: 无

???+ example "示例 7.206：在 CVS 近似下使用 SRC-TDDFT 计算碳 K 边 [C(1s) $\rightarrow$ 虚轨道] 激发。"
    ```qchem
    $comment
    Carbon K-edge excitations for acetone.
    The only active occupied orbitals are three C(1s).
    The SRC1-R1 is parameterized for "first row" (C, N, O, ...)
    $end
    
    $molecule
    0 1
      C   -3.0219081    1.0061477    0.0000001
      O   -2.9337180    2.2246186    0.0000001
      C   -1.7817549    0.1662163   -0.0000003
      C   -4.3700966    0.3535647    0.0000004
      H   -0.8735407    0.8061311   -0.0000005
      H   -1.7663727   -0.4765415   -0.9049102
      H   -1.7663723   -0.4765416    0.9049094
      H   -5.1766925    1.1175964    0.0000006
      H   -4.4778785   -0.2802782    0.9049091
      H   -4.4778790   -0.2802781   -0.9049084
    $end
    
    $rem
    exchange           src1-r1  ! r1 = "first row"
    basis              6-31++G*
    cis_n_roots        25
    cis_triplets       false
    trnss              true
    trtype             3
    n_sol              3 ! no. of active orbs
    $end
    
    $alist
    2 3 4
    $end
    
    ```

对于较重元素 K 边 X 射线吸收光谱的计算，相对论效应会变得越来越重要。REL_SHIFT 关键字
会对计算得到的激发能引入一项校正，以考虑这些效应，如下文示例 [7.12.2.1](#ex:TDDFT-CVS-0) 所示。
所加入的元素特异性校正值等于孤立原子 $1s$ 轨道的相对论（Douglas-Kroll-Hess）与非相对论 Hartree-Fock 本征值之差[[118]](../bib_references/bib.md#bib113)。

对于 K 边激发，这大概足以描述相对论效应，但在 L 边或 M 边激发的情况下，由于自旋-轨道耦合的存在，问题会变得复杂。

### `REL_SHIFT`

> **对计算得到的 TDDFT 激发能进行标量相对论效应校正。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $Z$: 对应于核心电离元素的原子序数。
> * **建议**: 相对论校正值等于孤立原子 $1s$ 轨道的相对论（Douglas-Kroll-Hess）与非相对论 Hartree-Fock/cc-pCVTZ 本征值之差。

???+ example "示例 7.207：计算磷 K 边的核心激发态，包含标量相对论位移校正。"
    ```qchem
    $molecule
       0 1
       H     1.196206    0.000000   -0.469131
       P     0.000000    0.000000    0.303157
       H    -0.598103   -1.035945   -0.469131
       H    -0.598103    1.035945   -0.469131
    $end
    
    $rem
       EXCHANGE       SRC2-R2  ! R2 = "second row" (Al, S, P, ...)
       BASIS          6-311(2+,2+)G**
       CIS_N_ROOTS    6
       CIS_TRIPLETS   false
       TRNSS          true
       TRTYPE         3
       N_SOL          1
       REL_SHIFT      15
    $end
    
    $alist
       1
    $end
    ```

尽管 TDDFT 的计算成本相对较低，但对于大体系而言，计算 X 射线吸收光谱仍可能变得颇具挑战。
核心激发态的高密度使得光谱模拟比同等规模的 UV/vis 光谱计算在计算上更加昂贵。
当需要来自多个核心轨道的激发时尤其如此，这在研究有机分子的碳 K 边时是常见情形。
计算成本包含两个方面，其一是所需的 CPU 时间，其二是所需的内存。
一种名为 “fTDDFTs” 的 TDDFT 实现结合了强力的积分筛选（integral screening）与粗略的 DFT 求积网格（quadrature grid），
在计算 X 射线吸收光谱时格外高效[[126]](../bib_references/bib.md#bib115)。

该方法可以通过 *$rem* 变量 FAST_XAS、XAS_SCREEN_LEVEL 和 XAS_EDGE 进行微调。这些计算所需的内存
还可以进一步通过 TDDFT_NVIRT 关键字来降低，该关键字可减少 TDDFT 计算中所包含的虚轨道数目。
fTDDFTs 的作业控制变量列于下文，其用法在示例 [7.12.2.1](#ex:TDDFT-CVS-0) 中演示。

!!! note "注意"
    目前 fTDDFTs 仅适用于受限（restricted）CIS/TDA 计算，且未做并行化。
    （初始 SCF 计算可以使用多个线程，但随后的 CIS/TDA 计算是串行执行的。）


### `FAST_XAS`

> **控制是否用于核心激发的快速 TDDFT。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `TRUE`: 使用快速 TDDFT。
> * **建议**: 无

### `XAS_SCREEN_LEVEL`

> **设置快速 TDDFT 的积分筛选程序。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $1$: 仅计算在相关原子上包含内层核心基函数的积分。 $2$ 仅计算在相关原子上包含基函数的积分。
> * **建议**: 1

### `XAS_EDGE`

> **指定被激发元素的核电荷数。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$: 对应于被激发元素的核电荷数。
> * **建议**: 无

### `TDDFT_NVIRT`

> **指定 XAS TDDFT 计算中所包含的虚轨道数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **选项**:
>     * $n$: 对应于能量最低的
>     * $n$: 个虚轨道。
> * **建议**: 无

???+ example "示例 7.208：使用 fTDDFTs 对 CO 的氧 K 边核心激发态进行快速、低内存计算。"
    ```qchem
    $molecule
       0 1
       C     0.000000    0.000000   -0.648906
       O     0.000000    0.000000    0.486357
    $end
    
    $rem
       EXCHANGE           SRC1-R1
       BASIS              6-311G*
       CIS_N_ROOTS        6
       CIS_TRIPLETS       false
       TRNSS              true
       TRTYPE             3
       N_SOL              1
       FAST_XAS           true
       XAS_EDGE           6
       XAS_SCREEN_LEVEL   1
    $end
    
    $alist
       1
    $end
    ```

## 7.12.2.2 发射光谱

同样也可以使用 TDDFT 计算 X 射线发射光谱。这是通过采用带有一个核心空穴（core-hole）的参考行列式来实现的[[1419]](../bib_references/bib.md#bib1480)。
计算得到的激发能对基组的选择可能相当敏感，对于较重元素的 K 边，可能需要使用大的或专门适配的基组，
以便对核心区域给出良好的描述[[400]](../bib_references/bib.md#bib409)。

???+ example "示例 7.209：本示例展示了使用 TDDFT + MOM 计算水的 XES 光谱。"
    ```qchem
    $molecule
       0 1
       O   0.0000   0.0000   0.1168
       H   0.0000   0.7629  -0.4672
       H   0.0000  -0.7629  -0.4672
    $end
    
    $rem
       method       cam-b3lyp
       basis        cc-pvdz
    $end
    
    @@@
    
    $molecule
       +1 2
       O   0.0000   0.0000   0.1168
       H   0.0000   0.7629  -0.4672
       H   0.0000  -0.7629  -0.4672
    $end
    
    $rem
       method       cam-b3lyp
       basis        cc-pvdz
       scf_guess    read
       mom_start    1
       cis_n_roots  5
       cis_triplets false
    $end
    
    $occupied
       1:5
       2:5
    $end
    ```

## 7.12.2.3 用于开壳层基态的 XCIS-CVS

对于开壳层体系，XAS 光谱和核心激发态可以使用第 [7.2.3.1](Ch7.S2.SS3.md#topic:xcis) 节中的“扩展 CIS”（extended CIS, XCIS）方法来计算。
结合 CVS 近似，可以有针对性且高效地处理核心到价层的跃迁[[1015]](../bib_references/bib.md#bib1057)。

???+ example "示例 7.210：使用 XCIS-CVS 方法计算 ${}^{3}$ O ${}_{2}$ 的氧 pre-edge 与 K 边核心激发态。"
    ```qchem
    $molecule
    0 3
    O 0.0000 0.0000 0.0000
    O 0.0000 0.0000 1.2075
    $end
    
    $rem
     basis = aug-cc-pvtz
     method = hf
     rohf_dods = true
     !roscf_diag_scale_a = 50
     max_scf_cycles = 500
     scf_convergence = 8
    $end
    
    @@@
    
    $molecule
     read
    $end
    
    $rem
     method = hf
     basis = aug-cc-pvtz
     unrestricted = false
     scf_guess = read
     max_scf_cycles = 200
     scf_convergence = 8
     cis_n_roots = 5
     cis_max_cycles = 100
     xcis = true
     rpa = false
     trtype = 3
     n_sol = 2
     trnss = true
    $end
    
    $alist
    1 2
    $end
    ```
