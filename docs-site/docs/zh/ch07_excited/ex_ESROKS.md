---
title: "7.7.4 受限开壳层 Kohn-Sham 方法"
---

## 7.7.4 受限开壳层 Kohn-Sham 方法

(July 4, 2026)

闭壳层分子的单激发态无法用单个非 *aufbau*（非构造原理）填充的 Slater 行列式来描述，因为自旋向上与自旋向下的电子被激发的概率相同，从而至少产生两个权重相等的组态。尽管如此， triplet（三重态）能量仍可由单个行列式求得，方法是从基态的 $M_{S}=0$ 子空间切换到 $M_{S}=\pm 1$ 子空间（*即*，让两个未配对电子的自旋指向同一方向，而不是一个向上、一个向下）。然而这一策略对单重激发态并不适用：在非 *aufbau* 填充组态中，仅激发自旋向上（或向下）的电子，其状态介于单重态与三重态之间（因而存在自旋污染）。这种混合态与破坏了自旋对称性的非受限（unrestricted）基态解并无本质区别。通过在 SCF 之后进行近似的自旋纯化（spin-purification）、扣除能量中的三重态贡献，可以获得真正的单重态能量。但这样一来，三重态能量就必须通过第二次轨道优化单独估算。

*受限开壳层 Kohn-Sham*（restricted open-shell Kohn-Sham, ROKS）方法为这类单重激发态提供了一条替代途径。当使用受限开壳层轨道时，混合的非 *aufbau* 组态（激发自旋向上或自旋向下）恰好位于单重态与三重态的正中间，其能量为 $E_{\text{mix}}$。三重态能量 $E_{\text{T}}$ 同样可以在 $M_{S}=\pm 1$ 子空间内由单个行列式计算得到。因此，ROKS 优化一组自旋受限轨道 $\{\phi_{\text{ROKS}}\}$，使得自旋纯化后的单重态能量

<a id="Ch7.E79"></a>

$$
E_{\text{S}}=2E_{\text{mix}}[\{\phi_{\text{ROKS}}\}]-E_{\text{T}}[\{\phi_{\text{ROKS}}\}]\;, \tag{7.79}
$$

处于平稳状态。因此它只需要一次轨道优化，与前一段提到的 $\Delta$SCF 方法所需的两组轨道形成对比。不过，由于方程具有双行列式的性质，ROKS 的 Fock 矩阵结构更为复杂。[[579]](../bib_references/bib.md#bib600)

还需要注意的是，这一激发态方法与用于开壳层*基态*的 ROKS 理论是不同的，后者是一种对应于具有多个未配对电子的高自旋态的单行列式方法。

**Q-Chem** 中 ROKS 激发态的实现基本上遵循 Filatov 与 Shaik 建立的理论框架；[[388]](../bib_references/bib.md#bib396) 关于最低激发单重态（$S_{1}$ 态）采用基于 DIIS 方法的情形，可见文献 [[714]](../bib_references/bib.md#bib746)。下面给出一个示例。借助平方梯度法（squared-gradient approach，第 [7.7.5](ex_BEDSCF.md) 节）、最大重叠方法（maximum overlap method，第 [7.7.2](ex_OpSing.md) 节）或态定向能量投影（state-targeted energy projection，第 [7.7.8](ex_ROSTEP.md) 节），ROKS 也可以处理更高的激发态。

人们发现，在描述电荷转移态时，ROKS 的精度显著优于 TDDFT，[[513]](../bib_references/bib.md#bib523) 初步证据表明对 Rydberg 态同样如此。ROKS 在芯层（core）激发能方面也非常精确，使用 SCAN 泛函对小分子的 K 边与 L 边激发可获得低于 0.5 eV 的误差。[[510]](../bib_references/bib.md#bib525)

使用 ROKS/SGM 计算芯激发态的例子见第 [7.7.5](ex_BEDSCF.md) 节。（激发态的）解析核梯度同样可用，因此也能进行几何优化和分子动力学计算，以及有限差分频率计算。ROKS 代码的使用者被要求在引用文献 [[714]](../bib_references/bib.md#bib746) 的同时，若采用了 SGM 实现则再引用文献 [[511]](../bib_references/bib.md#bib526)，若用于电荷转移态则引用文献 [[513]](../bib_references/bib.md#bib523)，若用于芯激发则引用文献 [[510]](../bib_references/bib.md#bib525)。

ROKS 的主要局限在于它只能描述含一个断裂电子对的态。因此它仅适用于闭壳层体系的某些激发态：所有可由单对自然跃迁轨道（natural transition orbital, NTO）良好描述的单重单激发态，或者总共只断裂一个电子对的更高单重态（例如 tetrazine 的 ${}^{1}$B${}_{3g}$ 双激发态）。幸运的是，大多数电荷转移和芯激发并不需要断裂多于一个电子对，所以这一局限在实际应用中并非严重问题。

此外，当两个开壳层轨道属于同一空间对称性时，ROKS 常常出现非物理的相互混合，这在 $\pi\to\pi^{\ast}$ 和 $1s\to 3s$ 激发中表现尤为明显。[[408]](../bib_references/bib.md#bib417)

这与为双行列式波函数定义有效 Fock 算符时固有的模糊性相关。[[579]](../bib_references/bib.md#bib600) 对于出现这种混合的态，收敛往往很困难，并且与基态的重叠可能相当显著。可以采用两种方案来缓解这一问题。第一种是能级平移（level-shift）技术，它拉开两个单占据轨道之间的能量，从而抑制它们的混合。[[714]](../bib_references/bib.md#bib746) 该技术仅在使用 DIIS 且基于旧 SCF 引擎的 ROKS 实现（GEN_SCFMAN = FALSE）中可用。第二种是完全抑制单占据轨道之间的混合。虽然这可能违背正确的变分条件，[[579]](../bib_references/bib.md#bib600) 但它能得到与基态重叠小得多的激发态，并带来更平滑的收敛。参见示例 7.7.4 的演示。

要执行 ROKS 激发态计算，只需设置关键字 ROKS = TRUE 并确保 UNRESTRICTED = FALSE。建议先对该体系进行一次预备性的基态计算，然后通过 SCF_GUESS = READ 利用基态轨道构造初始猜测。两个任意的组态之间（通常是基态与用 $\Delta$SCF 或 ROKS 计算得到的某个激发态）的跃迁偶极矩，可以在初态计算中设置 TRANS_MOM_SAVE = TRUE、在末态计算中设置 TRANS_MOM_READ = TRUE 来求得。轨道基组之间的非正交性已被考虑在内。

### `ROKS`

> **控制是否执行 ROKS 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `FALSE`: 不执行 ROKS。
>     * `TRUE`: 执行 ROKS。
> * **建议**: 若希望进行 ROKS 计算则设为 TRUE。请确保 UNRESTRICTED 未被设为 TRUE。

### `ROKS_LEVEL_SHIFT`

> **引入 $N$/100 hartree 的能级平移以辅助 DIIS 收敛。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **可选值**:
>     * `0`: 不平移 $N$ 平移量为 $N$ /100 hartree。
> * **建议**: 在 DIIS 收敛困难的情况使用。仅对基于旧 SCF 引擎（GEN_SCFMAN = FALSE）的 ROKS 实现可用。

### `ROKS_SS_MIXING`

> **允许两个单占据分子轨道之间的耦合。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **可选值**:
>     * `0`: 抑制耦合。
>     * `1`: 允许耦合。
> * **建议**: 当所得态难以收敛和/或与基态重叠显著时，抑制耦合。仅适用于基于 GDM 和 SGM 的求解器。

### `TRANS_MOM_SAVE`

> **保存轨道，供后续跃迁偶极矩计算使用。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `FALSE`: 不保存轨道。
>     * `TRUE`: 保存轨道。
> * **建议**: 保存设置该变量的那次计算的轨道。通常会是基态计算，但也可以是任意受限 SCF、非受限 SCF 或 ROKS 计算，从而允许计算一般的态间跃迁偶极矩。

### `TRANS_MOM_READ`

> **读取先前保存的参考轨道，并与当前计算的轨道一起计算跃迁偶极矩。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `FALSE`: 不读取轨道。
>     * `TRUE`: 读取轨道。
> * **建议**: 该选项假定先前已用 TRANS_MOM_SAVE 保存过一组轨道。若是如此，则读取这些轨道，并与当前计算的轨道一起求跃迁偶极矩。

???+ example "示例 7.50: 在 RO-PBE0/6-311+G* 水平下计算甲醛激发态的梯度，使用基态轨道作为初始猜测。此处采用了文献 714 Kowalczyk T. et al. J. Chem. Phys. (2013), 138, pp. 164101. Link. 中基于 DIIS 的实现。"
    ```qchem
    $comment
       ROKS excited state gradient of formaldehyde
       Use orbitals from ground state for initial guess
    $end
    
    $rem
       EXCHANGE          pbe0
       BASIS             6-311+G*
       SCF_CONVERGENCE   9
    point_group_symmetry False
    $end
    
    $molecule
       0 1
       H      -0.940372    0.000000    1.268098
       H       0.940372    0.000000    1.268098
       C       0.000000    0.000000    0.682557
       O       0.000000    0.000000   -0.518752
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       ROKS              true
       UNRESTRICTED      false
       EXCHANGE          pbe0
       BASIS             6-311+G*
       JOBTYPE           force
       SCF_CONVERGENCE   9
    point_group_symmetry False
       SCF_GUESS         read
    $end
    ```

???+ example "示例 7.51: 在 $\omega$B97X-D/STO-3G 水平下对丙酮最低 $\pi\to\pi^{\ast}$ 激发态进行 ROKS 计算。若要观察开壳层轨道之间的混合以及抑制混合的效果，可尝试将 ROKS_SS_MIXING 设为 TRUE/FALSE 运行本例。"
    ```qchem
    $comment
      Plain old SCF on the ground state.
    $end
    
    $molecule
      0   1
      C   0.00000000      0.00000000      0.18807702
      C   0.00000000      2.42007545     -1.31764698
      C   0.00000000     -2.42007545     -1.31764698
      O   0.00000000      0.00000000      2.48269094
      H   0.00000000      4.03690733     -0.05185132
      H   0.00000000     -4.03690733     -0.05185132
      H   1.66061256      2.48420530     -2.53995285
      H  -1.66061256      2.48420530     -2.53995285
      H   1.66061256     -2.48420530     -2.53995285
      H  -1.66061256     -2.48420530     -2.53995285
    $end
    
    $rem
      METHOD               WB97X-D
      UNRESTRICTED         FALSE
      BASIS                STO-3G
      INPUT_BOHR           TRUE
      INTEGRAL_SYMMETRY    FALSE
      POINT_GROUP_SYMMETRY TRUE
      GEN_SCFMAN           TRUE
      SCF_ALGORITHM        DIIS_GDM
      SCF_CONVERGENCE      8
      MAX_SCF_CYCLES       200
      MEM_TOTAL            1000
      MEM_STATIC           100
      THRESH               14
    $end
    
    @@@
    
    $comment
      Plain old SCF on the ground state with UNRESTRICTED = TRUE
      to enable TRANS_MOM_SAVE.
    $end
    
    $molecule
      read
    $end
    
    $rem
      METHOD               WB97X-D
      UNRESTRICTED         TRUE
      BASIS                STO-3G
      INPUT_BOHR           TRUE
      INTEGRAL_SYMMETRY    FALSE
      POINT_GROUP_SYMMETRY TRUE
      SYM_IGNORE           TRUE
      GEN_SCFMAN           TRUE
      SCF_GUESS            READ
      SCF_ALGORITHM        DIIS
      SCF_CONVERGENCE      10
      MAX_SCF_CYCLES       200
      TRANS_MOM_SAVE       1
      MEM_TOTAL            1000
      MEM_STATIC           100
      THRESH               14
    $end
    
    @@@
    
    $comment
      ROKS calculation targeting the \pi -> \pi^{*} state. Attempt
      to run this calculation with ROKS_SS_MIXING = TRUE to see
      what happens.
    $end
    
    $molecule
      read
    $end
    
    $rem
      METHOD               WB97X-D
      UNRESTRICTED         FALSE
      ROKS                 TRUE
      ROKS_SS_MIXING       FALSE
      BASIS                STO-3G
      INPUT_BOHR           TRUE
      INTEGRAL_SYMMETRY    FALSE
      POINT_GROUP_SYMMETRY TRUE
      GEN_SCFMAN           TRUE
      SCF_GUESS            READ
      SCF_ALGORITHM        GDM
      SCF_CONVERGENCE      7
      MAX_SCF_CYCLES       1000
      TRANS_MOM_READ       2
      THRESH               14
      MEM_STATIC           100
      MEM_TOTAL            1000
    $end
    
    $reorder_mo
      1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 15 17
      1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 15 17
    $end
    
    ```
