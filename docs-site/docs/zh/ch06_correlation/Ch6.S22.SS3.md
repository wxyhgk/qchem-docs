---
title: "6.22.3 ASCI 作业控制"
---

## 6.22.3 ASCI 作业控制

（2026 年 7 月 4 日）

活性空间（Active Space）的指定与收敛细节由第 [6.20.2](subsec_casscf_rems.md) 节中所述的 *$rem* 变量控制。在 ASCI 计算过程中，会在临时目录（scratch directory）中创建一个名为 `wf_data` 的文件，其中包含 ASCI 波函数中行列式（determinant）及其权重（weight）的信息。

ASCI_DIAG

### `ASCI_DIAG`

> **指定对角化过程所使用的算法。**
>
> * **类型**: `INTEGER`
> * **默认值**: `2`
> * **可选值**:
>     * 1
>     * Davidson 求解器（Davidson solver）
>     * 2
>     * Eigen 稀疏矩阵求解器（Eigen sparse matrix solver）
> * **建议**: 使用 2 可在速度与内存占用之间取得最佳平衡。若内存占用过高，可切换为 1。

ASCI_NDETS

### `ASCI_NDETS`

> **指定 ASCI 波函数中包含的行列式数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * $N$
>     * 表示波函数包含
>     * $N$
>     * 个行列式
> * **建议**: 典型的 ASCI 展开规模在 50,000 到 2,000,000 个行列式之间，具体取决于活性空间大小、问题复杂度以及所需的精度。

ASCI_CDETS

### `ASCI_CDETS`

> **指定在 ASCI 波函数增长（growth）步骤中需要搜索的行列式数目。**
>
> * **类型**: `INTEGER`
> * **默认值**: `-5`
> * **可选值**:
>     * $N>0$
>     * 从权重最高者开始搜索 $N$
>     * 个行列式
>     * $N<0$
>     * 从权重最高者开始搜索，直至其在波函数中的累积权重对应于
>     * $1-2^{N}$
>     * 为止
> * **建议**: 使用动态确定的取值（$N<0$）可获得更好的结果。

ASCI_USE_NAT_ORBS

### `ASCI_USE_NAT_ORBS`

> **指定在各增长步骤之间是否应旋转到自然轨道（Natural Orbital）基组。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `TRUE`
> * **可选值**:
>     * TRUE
>     * 在波函数各增长步骤之间旋转到自然轨道基组
>     * FALSE
>     * 不旋转到自然轨道基组
> * **建议**: 自然轨道旋转可显著提升 ASCI 波函数的紧凑性，从而提高其精度。

ASCI_DAVIDSON_GUESS

### `ASCI_DAVIDSON_GUESS`

> **指定用于 ASCI 的 Davidson 求解器的截断组态相互作用（truncated CI）初始猜测。**
>
> * **类型**: `INTEGER`
> * **默认值**: `2`
> * **可选值**:
>     * $N$
>     * 为 ASCI Davidson 初始猜测显式求解的截断 CI 的阶数。
> * **建议**: 精确的激发态以及基态的快速收敛都有赖于对低能谱良好的零阶初始猜测。通常默认值即已足够。

ASCI_SKIP_PT2

### `ASCI_SKIP_PT2`

> **指定是否应计算 ASCI 的 PT2 修正。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **可选值**:
>     * FALSE
>     * 计算 ASCI PT2 贡献
>     * TRUE
>     * 不计算 ASCI PT2 贡献
> * **建议**: PT2 修正对于获得收敛的 ASCI 能量至关重要。

ASCI_RESTART

### `ASCI_RESTART`

> **指定是否使用 `wf_data` 文件来初始化 ASCI 波函数。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **可选值**:
>     * TRUE
>     * 从
>     * wf_data
>     * 文件中读取 CI 系数
>     * FALSE
>     * 不从磁盘读取 CI 系数

ASCI_SPIN_PURIFY

### `ASCI_SPIN_PURIFY`

> **指示是否应通过补充缺失的行列式来增强 ASCI 波函数，以确保其为自旋纯（spin-pure）态。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **可选值**:
>     * TRUE
>     * 通过补充行列式来增强波函数，以确保其为自旋本征态（spin eigenstate）
>     * FALSE
>     * 不增强波函数

???+ example "示例 6.60: N ${}_{2}$ 最低三重态（$M_{s}=1$）的 CASCI 计算。采用自适应采样方法（adaptive sampling）来处理大活性空间 (14e, 32o)，并在 ASCI 波函数之上执行 PT2 修正。"
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.8
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvtz
       CAS_METHOD        1     !1 for CAS-CI, 2 for CASSCF
       CAS_M_S           2     !M_s value*2 (2: triplet)
       ASCI_DIAG         2     !Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC        14    !N_elec
       CAS_N_ORB         32    !N_orb
       CAS_N_ROOTS       1     !N_roots
       CAS_SOLVER        2     !2=ASCI, 1=Olsen, 0=naive
       ASCI_NDETS        28000 !Number of ASCI Determinants
       THRESH            14
       MAX_SCF_CYCLES    400
       SCF_CONVERGENCE   8
       MEM_TOTAL         4000
       MEM_STATIC        1000
       ROSCF             true
       SCF_ALGORITHM     diis_gdm
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "示例 6.61: N ${}_{2}$ 基态的 ASCI-SCF 计算（对 CAS 使用自适应采样方法），活性空间较大 (14e, 32o)。本例中不执行 PT2 修正。"
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.8
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvtz
       CAS_METHOD        2  !1 for CAS-CI, 2 for CASSCF
       CAS_M_S           0  !M_s value*2
       ASCI_DIAG         2  !Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC        14 !N_elec
       CAS_N_ORB         32 !N_orb
       CAS_N_ROOTS       1 !N_roots
       CAS_SOLVER        2 !2=ASCI, 1=Olsen, 0=naive
       ASCI_NDETS        28000 !Number of ASCI Determinants
       ASCI_SKIP_PT2     1
       THRESH            14
       MAX_SCF_CYCLES    400
       SCF_CONVERGENCE   6
       MEM_TOTAL         4000
       MEM_STATIC        1000
       SCF_ALGORITHM     diis_gdm
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
