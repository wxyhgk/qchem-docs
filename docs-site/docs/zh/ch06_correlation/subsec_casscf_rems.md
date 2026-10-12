---
title: "6.20.2 CAS-CI 与 CASSCF 作业控制选项"
---

## 6.20.2 CAS-CI 与 CASSCF 作业控制选项

（2026 年 7 月 4 日）

### `CAS_METHOD`

> **指示是否请求轨道优化。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * 0
>     * 不进行 CAS 计算
>     * 1
>     * CAS-CI（不进行轨道优化）
>     * 2
>     * CASSCF（进行轨道优化）
> * **建议**：为获得最佳精度请使用 2，但对于大活性空间，此类计算可能变得不可行。

### `CAS_M_S`

> **CAS 波函数中期望的非配对电子数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * $N$
>     * 对于具有
>     * $N$
>     * 个非配对电子的波函数

### `CAS_N_ELEC`

> **指定活性电子数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * $N$
>     * 在活性空间中包含
>     * $N$
>     * 个电子
>     * -1
>     * 在活性空间中包含所有电子
> * **建议**：对给定体系使用尽可能小的活性空间。

### `CAS_N_ORB`

> **指定活性轨道数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * $N$
>     * 在活性空间中包含
>     * $N$
>     * 个轨道
>     * -1
>     * 在活性空间中包含所有轨道
> * **建议**：对给定体系使用尽可能小的活性空间。

### `CAS_N_ROOTS`

> **指定要求解的电子态数目。**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **可选值**：
>     * $N$
>     * 求解哈密顿量的
>     * $N$
>     * 个根（本征值）

### `CAS_THRESH`

> **指定包含在 CAS 哈密顿量中的矩阵元阈值。**
>
> * **类型**：`INTEGER`
> * **默认值**：`12`
> * **可选值**：
>     * $N$
>     * 对应阈值为
>     * $10^{-N}$

### `CAS_SAVE_NAT_ORBS`

> **将 CAS 自然轨道保存以替代参考轨道。**
>
> * **类型**：`BOOLEAN`
> * **默认值**：`FALSE`
> * **可选值**：
>     * TRUE
>     * 用 CAS 自然轨道覆盖参考轨道
>     * FALSE
>     * 不保存 CAS 自然轨道

### `MAX_CASSCF_CYCLES`

> **CASSCF 轨道优化的最大循环次数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`50`
> * **可选值**：
>     * $N$
>     * 将最大优化循环次数设置为
>     * $N$

### `CAS_USE_RI`

> **指示是否使用分辨率恒等（Resolution of the Identity, RI）近似。**
>
> * **类型**：`BOOLEAN`
> * **默认值**：`FALSE`
> * **可选值**：
>     * FALSE
>     * 解析计算双电子积分
>     * TRUE
>     * 对双电子积分使用 RI 近似
> * **建议**：解析积分更精确，RI 积分更快。

### `CAS_DAVIDSON_TOL`

> **指定 CAS 中所用 Davidson 求解器的收敛容限。**
>
> * **类型**：`INTEGER`
> * **默认值**：`5`
> * **可选值**：
>     * $N$
>     * 对应阈值为
>     * $10^{-N}$
> * **建议**：默认值在大多数情况下均已适用。

### `CAS_DAVIDSON_MAXVECTORS`

> **指定在 CAS 中用于扩展 Davidson 搜索空间的最大向量数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`10`
> * **可选值**：
>     * $N$
>     * 将 Davidson 子空间最大尺寸设置为
>     * $N$
>     * 加上
>     * CAS_N_ROOTS
> * **建议**：默认值在大多数情况下均已适用。

### `CAS_SOLVER`

> **指定活性空间所使用的求解器。**
>
> * **类型**：`INTEGER`
> * **默认值**：`1`
> * **可选值**：
>     * 1
>     * CAS-CI/CASSCF
>     * 2
>     * ASCI（参见第
>     * 6.22
>     * 节）
>     * 3
>     * 截断 CI（CIS、CISD、CISDT 等）

### `TRUNC_CI_LEVEL`

> **指定活性空间中使用的截断 CI 阶数。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **可选值**：
>     * 0
>     * 不执行截断 CI
>     * 1
>     * CIS
>     * 2
>     * CISD
>     * 3
>     * CISDT
>     * 4
>     * CISDTQ
>     * 依此类推。

???+ example "示例 6.55：N ${}_{2}$ 基态的 CASCI(6,14) 计算。"
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.8
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvtz
       CAS_METHOD        1    ! 1 for CAS-CI, 2 for CASSCF
       CAS_M_S           0    ! M_s value*2
       ASCI_DIAG         2    ! Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC        6    ! N_elec
       CAS_N_ORB         14   ! N_orb
       CAS_N_ROOTS       1    ! N_roots
       CAS_SOLVER        1    ! 2=ASCI, 1=Olsen, 0=naive
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

???+ example "示例 6.56：N ${}_{2}$ 基态的 CASSCF(6,6) 计算。"
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.8
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvtz
       CAS_METHOD        2    !1 for CAS-CI, 2 for CASSCF
       CAS_M_S           0    !M_s value*2
       ASCI_DIAG         2    !Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC        6    !N_elec
       CAS_N_ORB         6    !N_orb
       CAS_N_ROOTS       1    !N_roots
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

???+ example "示例 6.57：在 CASSCF(6,6)/cc-pVTZ 理论水平下对 N ${}_{2}$ 基态进行几何优化。"
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.3
    $end
    
    $rem
       JOBTYPE              opt
       EXCHANGE             hf
       BASIS                cc-pvtz
       CAS_METHOD           2    !1 for CAS-CI, 2 for CASSCF
       CAS_M_S              0    !M_s value*2
       ASCI_DIAG            2    !Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC           6    !N_elec
       CAS_N_ORB            6    !N_orb
       CAS_N_ROOTS          1    !N_roots
       CAS_SAVE_NAT_ORBS    true !overwrite MOs with CAS natural orbs
       THRESH               14
       MAX_SCF_CYCLES       400
       SCF_CONVERGENCE      6
       MEM_TOTAL            4000
       MEM_STATIC           1000
       SCF_ALGORITHM        diis_gdm
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "示例 6.58：利用 CASCI 程序对 N ${}_{2}$ 基态进行截断 CI（S、D、T）计算。"
    ```qchem
    $molecule
       0 1
       N   0.0   0.0   0.0
       N   0.0   0.0   1.1
    $end
    
    $rem
       EXCHANGE          hf
       BASIS             cc-pvdz
       CAS_METHOD        1   !1 for CAS-CI, 2 for CASSCF
       CAS_M_S           0   !M_s value*2
       ASCI_DIAG         2   !Arma Sparse=0, Davidson=1, Eigen Sparse=2
       CAS_N_ELEC        6   !N_elec
       CAS_N_ORB        -1   !N_orb (-1: include all orbitals in the active space)
       CAS_N_ROOTS       1   !N_roots
       CAS_SOLVER        3   !2=ASCI, 1=Olsen, 0=naive
       TRUNC_CI_LEVEL    3   !include up to triples excitations
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
