---
title: "7.7.5 梯度平方极小化"
---

## 7.7.5 梯度平方极小化

（2026 年 7 月 4 日）

梯度平方极小化（squared-gradient minimization, SGM）算法[[511]](../bib_references/bib.md#bib526)
 通过在轨道旋转变量 $\vec{\theta}$ 空间中最小化能量梯度的平方，
绕开了在轨道旋转变量空间中优化鞍点这一难题。基态自洽场（SCF）方法
力求最小化能量 $E$（关于 $\vec{\theta}$），因此在收敛时梯度
$\hat{\bm{\nabla}}_{\vec{\theta}}E$ 必须为零。于是，通过最小化
$\Delta(\vec{\theta})=\|\hat{\bm{\nabla}}_{\vec{\theta}}E\|^{2}$
使其趋于零，同样可以获得相同的结果。然而，$E$ 的所有驻点都是
$\Delta(\vec{\theta})$ 的极小点，而不仅仅是基态。因此，只要从一个合理的
初始猜测出发（例如对应于激发态的非 *aufbau*（构造原理）
排布），并通过最小化 $\Delta(\vec{\theta})$ 来优化，就有可能获得激发态
轨道。这避免了尝试优化 $E$ 中不稳定驻点所带来的各种陷阱，从而防止了
变分坍缩（variational collapse）。

**Q-Chem** 中的 SGM 算法可用于优化两种不同激发态方法的轨道：
$\Delta$SCF 和 ROKS。前者简单地尝试最小化单个 Slater
行列式的能量，这对许多具有挑战性的激发（包括许多双
激发）而言通常已经足够。[[75]](../bib_references/bib.md#bib59)
 然而，许多激发（包括从闭壳层基态出发的所有单激发）会打破电子对，
导致其状态无法用单个行列式描述。可以 *a posteriori*（事后）对自旋污染的、
非 *aufbau* 行列式的能量进行自旋纯化，
但这至少需要两次独立的轨道优化。另一种选择是 ROKS（如第 [7.7.4](ex_ESROKS.md)
节所述），它只需要优化一组轨道，且自旋纯化后的能量对该组轨道而言是驻定的。
$\Delta$SCF 和 ROKS 均已有解析核梯度可用，因此可以进行几何结构优化和
*ab initio*（从头算）分子动力学。$\Delta$SCF
已有解析频率可用，包括包含 VV10 非局域关联的泛函。

由于实现难易程度的不同，SGM 在不同轨道类别中的使用略有差异。
使用限制闭壳层（R）和非限制（U）轨道的 $\Delta$SCF 过程，可以通过
SCF_ALGORITHM = SGM_LS 或 SCF_ALGORITHM =
SGM_QLS 运行，其初始轨道占据由 *$occupied* 块指定（如第
[7.7.2](ex_OpSing.md) 节以及下文示例 7.7.5 和
7.7.5 所述）。使用限制开壳层（RO）轨道的 $\Delta$SCF 计算或
ROKS 计算可通过 SCF_ALGORITHM = SGM 或
SCF_ALGORITHM = SGM_LS 执行，并且需要对轨道进行重新排序，
以确保未配对轨道位于前沿（frontier）。（见下文示例 7.7.5 和
7.7.5。）对于 R-、U- 和 RO-$\Delta$SCF，$\Delta(\vec{\theta})$
的梯度是解析计算的（包含 VV10 非局域关联的泛函除外），其成本相当于一次
Fock 矩阵构建。然而，在 ROKS 情况下以及对于包含 VV10
的泛函，$\Delta(\vec{\theta})$ 的梯度采用有限差分方法计算
[参见式 ([4.47](../ch04_scf/sub_stability_analysis.md#eq:fd_mat_vec))]。在这些情况下，其成本相当于
两次 Fock 矩阵构建。累计下来，当解析 $\Delta(\vec{\theta})$
梯度可用时，单次 SGM 迭代的成本是单次 GDM 迭代的两倍；若必须使用
有限差分构造，则为三倍，不过这并不影响计算随体系规模增长的渐近标度行为。

激发态轨道优化有时需要比基态 SCF
计算通常所需的更多迭代次数，因此应将 MAX_SCF_CYCLES
设置为一个较大的值（例如 200），而不是默认的 50。如果只需要能量，
也可以采用较宽松的收敛阈值 SCF_CONVERGENCE = 4，但必须在
任务完成后明确确认多次迭代间的能量变化远小于所需的精度（例如，若变化大于
$10^{-3}~{}E_{h}$ 或 0.03 eV，就会相当成问题）。进一步降低
SCF_CONVERGENCE 可能会损害偶极矩或核梯度等性质，因此不推荐这样做。

SCF_ALGORITHM

### `SCF_ALGORITHM`

> **用于使 SCF 收敛的算法。**
>
> * **类型**: `STRING`
> * **默认值**: `None`
> * **选项**:
>     * SGM
>     * SGM_LS
>     * SGM_QLS
> * **建议**: SGM 应仅用于 RO-$\Delta$SCF 或 ROKS 计算。对于 R- 或 U-$\Delta$SCF，推荐使用 SGM_LS，但它也可用于 RO-$\Delta$SCF 或 ROKS。SGM_QLS 是 R- 和 U-$\Delta$SCF 计算中较慢但更稳健的选择。

DELTA_GRADIENT_SCALE

### `DELTA_GRADIENT_SCALE`

> **将 $\Delta$ 的梯度按 $N$/100 进行缩放，通过减小步长，可用于收敛困难的情况。**
>
> * **类型**: `INTEGER`
> * **默认值**: `100`
> * **选项**:
>     * $N$
> * **建议**: 使用默认值。对于有问题的情况，$N=$ 50、25、10 甚至 $N=1$ 可能会有用。

ROKS

### `ROKS`

> **控制是否执行 ROKS 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不执行 ROKS。
>     * TRUE
>     * 将执行 ROKS。
> * **建议**: 若需要 ROKS 计算，请设置为 TRUE。同时应确保 UNRESTRICTED = FALSE。

???+ example "示例 7.52: 使用 SGM_QLS 并以基态轨道作为初始猜测，对 Be 原子 $2s$ 到 $2p$ 的限制型 $\Delta$SCF 双激发进行计算。"
    ```qchem
    $comment
       Calculates Delta-SCF excitation energy for the 2s^2 -> 2p^2 excitation of Be
       using SCAN and SGM_QLS scf convergence
    $end
    
    $molecule
       0 1
       Be
    $end
    
    $rem
       METHOD            scan
       BASIS             aug-cc-pVTZ
       THRESH            14
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     diis
       XC_GRID           000099000590
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD            scan
       BASIS             aug-cc-pVTZ
       THRESH            14
       SCF_ALGORITHM     sgm_qls
       SCF_GUESS         read
       XC_GRID           000099000590
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    $occupied
       1 3
       1 3
    $end
    ```

???+ example "示例 7.53: NH ${}_{3}$ $\cdots$ F ${}_{2}$ 模型复合物从 HOMO 到 LUMO 的 ROKS 单激发，该激发描述从 NH ${}_{3}$ 到 F ${}_{2}$ 的电子转移。以基态轨道作为初始猜测。"
    ```qchem
    $molecule
       0 1
       N  0.0000   0.0000    0.0000
       H  0.0000  -0.9377   -0.3816
       H  0.8121   0.4689   -0.3816
       H -0.8121   0.4689   -0.3816
       F  0.0000   0.0000    6.0000
       F  0.0000   0.0000    7.4120
    $end
    
    $rem
       METHOD            pbe0
       BASIS             cc-pVDZ
       SCF_CONVERGENCE   8
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY False
    $end
    
    @@@
    
    $comment
       The reorder section is superfluous here since the excitation is HOMO to LUMO
       and thus the unpaired electron orbitals are already at the frontier.
    $end
    
    $molecule
       read
    $end
    
    $rem
       METHOD            pbe0
       BASIS             cc-pVDZ
       SCF_ALGORITHM     sgm
       ROKS              true
       SCF_GUESS         read
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $reorder_mo
       1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
       1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
    $end
    ```

???+ example "示例 7.54: HCHO 分子从 HOMO $-1$ 到 LUMO $+1$ 的非限制型 $\Delta$SCF 单激发，使用 SGM_LS SCF 收敛算法并以基态轨道作为初始猜测。"
    ```qchem
    $comment
       Calculates Delta-SCF excitation energy for the HOMO-1 -> LUMO+1
       excitation of HCHO using SCAN and SGM_LS convergence
    $end
    
    $molecule
       0 1
       O1     0.0000   0.0000   1.2050
       C2     0.0000   0.0000   0.0000
       H3     0.0000   0.9429  -0.5876
       H4     0.0000  -0.9429  -0.5876
    $end
    
    $rem
       METHOD            scan
       BASIS             aug-cc-pVTZ
       THRESH            14
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     diis
       XC_GRID           000099000590
       GEN_SCFMAN        true
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD            scan
       BASIS             aug-cc-pVTZ
       THRESH            14
       SCF_ALGORITHM     sgm_ls
       SCF_GUESS         read
       XC_GRID           000099000590
       GEN_SCFMAN        true
       UNRESTRICTED      true
       SCF_CONVERGENCE   7
       MAX_SCF_CYCLES    500
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $occupied
       1 2 3 4 5 6 8 10
       1 2 3 4 5 6 7 8
    $end
    ```

???+ example "示例 7.7.55: 结合 RO-$\Delta$SCF 芯层电离态与 $1s\rightarrow\text{LUMO}+1$ ROKS 芯激发态。"
    ```qchem
    $molecule
       0 1
       F       0.0000  0.0000  0.0000
       H       0.0000  0.0000  0.9168
    $end
    
    $rem
       method            scan
       basis             aug-cc-pCVTZ
       integral_symmetry false
    $end
    
    @@@
    
    $comment
       Calculates the RO-DeltaSCF core ionized state. The reorder section pushes F1s
       (first by energy) to the frontier, instead of the HOMO (5th orbital).
    $end
    
    $molecule
       1 2
       F       0.0000  0.0000  0.0000
       H       0.0000  0.0000  0.9168
    $end
    
    $rem
       METHOD            scan
       BASIS             aug-cc-pCVTZ
       UNRESTRICTED      false
       SCF_GUESS         read
       SCF_ALGORITHM     sgm
       INTEGRAL_SYMMETRY false
    $end
    
    $reorder_mo
       2 3 4 5 1
       2 3 4 5 1
    $end
    
    @@@
    
    $comment
       Calculates the ROKS core excited state. The O1s orbital is in the place of the HOMO
       from the previous reordering. The present reorder section pushes the LUMO+1 orbital
       (the 7th orbital) to the frontier, instead of the LUMO (6th orbital).
    $end
    
    $molecule
       0 1
       F       0.0000  0.0000  0.0000
       H       0.0000  0.0000  0.9168
    $end
    
    $rem
       METHOD           scan
       ROKS             true
       BASIS            aug-cc-pCVTZ
       SCF_GUESS        read
       SCF_ALGORITHM    sgm
       INTEGRAL_SYMMETRY false
    $end
    
    ```
