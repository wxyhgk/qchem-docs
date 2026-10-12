---
title: "7.7.8 态靶向能量投影（State-Targeted Energy Projection）"
---

## 7.7.8 态靶向能量投影（State-Targeted Energy Projection, STEP）

（2026 年 7 月 4 日）

态靶向能量投影（state-targeted energy projection, STEP）方法[[196]](../bib_references/bib.md#bib189)

为第 [7.7.2](ex_OpSing.md) 节中描述的 MOM 与 IMOM 流程提供了一种稳健且经济高效的替代方案。
STEP 通过对 Fock 矩阵进行简单修改来施加能级平移（level shift），

<a id="Ch7.E80"></a>

$$
\text{{F}}^{\prime}=\text{{F}}+\eta\text{{SQS}}\;, \tag{7.80}
$$

其中 **Q** 是投影到用户定义虚空间（virtual space）上的投影算符的矩阵表示，$\eta$ 是一个参数。
由 $\eta\text{{SQS}}$ 提供的能级平移将虚分子轨道 $\psi_{a}$ 的能量从 $\varepsilon_{a}$ 提升至
$\varepsilon_{a}+\eta$，对每一个包含在 **Q** 中的未占据轨道均如此。
参数 $\eta$ 的选取原则是：在保留目标电子组态的前提下提供最小的能级平移，其定义如下：

<a id="eq:eta-shift"></a>

$$
\eta=|\varepsilon_{\text{HOMO}}-\varepsilon_{\text{LUMO}}|+\epsilon^{\prime} \tag{7.81}
$$

式 ([7.81](#eq:eta-shift)) 中的 HOMO/LUMO 能隙指的是用户所定义组态的 HOMO 和 LUMO；也就是说，
与 MOM 流程类似，STEP 需要一组初始猜测分子轨道（通常来自基态计算）。
小的经验参数 $\epsilon^{\prime}$ 控制已占据轨道与未占据轨道之间能隙的大小，可通过 *$rem* 变量
STEP_EPSILON 进行设置。STEP 能级平移的应用约束了 SCF 方程的解，通过在每一个 SCF 循环中
强制对目标占据空间施加 *aufbau*（构造原理）占据方式，从而防止变分坍缩（variational collapse）。

**Q-Chem** 中 STEP 的实现利用了这样一个事实：通常允许一个动态的能级平移参数 $\eta$，
使其随每个循环中新的 HOMO/LUMO 能隙而变化，可以实现更快的收敛，
这与文献 [[196]](../bib_references/bib.md#bib189) 中报告的静态 $\eta$ 参数不同。
在最极端的情况下，如果无需施加能级平移投影即可平凡地满足目标 *aufbau* 组态，
STEP 会将 $\eta$ 设为 0，这就允许在优化 Fock 矩阵时进行不受约束的占据/虚轨道旋转，
从而快速收敛到目标态。与此同时，参数 $\epsilon^{\prime}$ 保持恒定，以便在整个优化过程中，
当需要持续施加能级平移时，可以控制其相对大小。

在更困难的情形下，动态能级平移方法（虽然效率更高）可能导致变分坍缩。
如果动态能级平移不足以解决问题，回退到文献 [[196]](../bib_references/bib.md#bib189)
中最初报告的实现方式，可以显著提升 STEP 的稳健性。在这种方法中，式 ([7.81](#eq:eta-shift))
中的能级平移参数在每个 SCF 循环中始终生效，即 $\eta$ 永不为零。

STEP 可以直接作为 $\Delta$SCF 流程使用（此时激发态往往会引入自旋污染），
也可以在限制开壳层（restricted open-shell）框架内使用（第 [7.7.4](ex_ESROKS.md) 节），
以直接收敛自旋纯（spin-pure）的激发态。在 **Q-Chem** 中，STEP 算法可用于
限制（restricted）、非限制（unrestricted）以及限制开壳层（restricted open-shell）轨道。

$\Delta$SCF（R- 或 U-STEP）与 RO-STEP 计算的作业控制：
在 *$rem* 部分激活 STEP 之后，
其余的 STEP 选项均通过 *$step* 输入部分来处理。

### `STEP`

> **激活 STEP 流程。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不应用 STEP 能级平移算法。
>     * `TRUE`: 应用 STEP 能级平移算法。
> * **建议**: 无

### `Epsilon`

> **以 $N$ /100 Hartree 的尺度调节能级平移所施加的占据/虚轨道能隙大小。输入部分: $step**
>
> * **类型**: `INTEGER`
> * **默认值**: `10`
> * **选项**:
>     * $N$
> * **建议**: 使用默认值，除非出现收敛问题，此时可以增大该值直至找到目标态。请注意，在能级平移算法中增大占据/虚轨道能隙会减慢收敛速度，因此在需要较大平移量时，建议同时增大 SCF_MAX_CYCLES。

### `Print`

> **控制 STEP 算法信息的打印级别。输入部分: $step**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * `0`: 不在 SCF 循环之间打印任何关于 STEP 的信息。
>     * `1`: 打印每个 SCF 循环所施加的能级平移（R- 和 U-STEP）。
>     * `2`: 打印每个 SCF 循环中混合态与三重态的能级平移（RO-STEP）。
> * **建议**: 使用默认值。能级平移为 0 表明 *aufbau* 判据足以确定轨道占据方式；平移 $>0$ 则意味着占据空间的选择违背了 *aufbau* 原则。

### `Always_Active`

> **切换至 STEP 的原始实现方式，即使用静态能级平移（每个循环均施加）。输入部分: $step**
>
> * **类型**: `STRING`
> * **默认值**: `None`
> * **选项**:
>     * `alpha`: 对 alpha 自旋轨道施加恒定的能级平移。
>     * `beta`: 对 beta 自旋轨道施加恒定的能级平移。
>     * `both`: 对 alpha 和 beta 自旋轨道均施加恒定的能级平移。
> * **建议**: 在动态能级平移无法取得满意结果时使用。对于 U-STEP，该约束只需施加在必须维持非 *aufbau* 组态的轨道上（即单电子 alpha 激发只需施加 alpha 约束，而双电子激发则需要同时施加两种约束）。对于 RO-STEP，该关键字默认为 both 且无法关闭。对于 R-STEP，只有当使用动态能级平移参数无法找到目标双激发组态时，采用 both 才是合理的。

### `ROKS`

> **控制是否执行 ROKS 计算。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * `FALSE`: 不执行 ROKS。
>     * `TRUE`: 执行 ROKS。
> * **建议**: 若需要 ROKS 计算则设为 TRUE。同时应确保 UNRESTRICTED = FALSE。

???+ example "示例 7.58: 使用带 STEP 的 $\Delta$ SCF 方法计算乙炔最低能量的 $\pi\rightarrow\pi^{\ast}$ 跃迁"
    ```qchem
    $comment
       Ground state calculation for reference orbitals
    $end
    
    $molecule
       0 1
       C    0.0000000000   -0.0000000177   -0.6043240964
       C    0.0000000000    0.0000000000    0.6043240820
       H    0.0000000000    0.0000000654   -1.6654864149
       H    0.0000000000    0.0000000198    1.6654865011
    $end
    
    $rem
       METHOD            b3lyp
       BASIS             def2-tzvpd
       SCF_CONVERGENCE   7
    $end
    
    @@@
    
    $comment
       Actual U-STEP calculation
    $end
    
    $molecule
       read
    $end
    
    $rem
       METHOD            b3lyp
       BASIS             def2-tzvpd
       SCF_GUESS         read
       STEP              true
       UNRESTRICTED      true
       SCF_CONVERGENCE   7
    $end
    
    ! default level-shift is 0.1 Hartree
    ! beta orbital promotion means only betas need constrained
    $step
    Epsilon 10
    Always_Active   beta
    $end
    
    $occupied
       1:7
       1:6 8
    $end
    ```

???+ example "示例 7.59: 使用带 STEP 的 ROKS 方法计算乙炔最低能量的自旋纯 $\pi\rightarrow\pi^{\ast}$ 跃迁"
    ```qchem
    $comment
       Generates the ground-state reference orbitals
    $end
    
    $molecule
       0 1
       C    0.0000000000   -0.0000000177   -0.6043240964
       C    0.0000000000    0.0000000000    0.6043240820
       H    0.0000000000    0.0000000654   -1.6654864149
       H    0.0000000000    0.0000000198    1.6654865011
    $end
    
    $rem
       METHOD            b3lyp
       BASIS             def2-tzvpd
       SCF_CONVERGENCE   7
    $end
    
    @@@
    
    $comment
       Actual RO-STEP calculation
    $end
    
    $molecule
       read
    $end
    
    $rem
       METHOD            b3lyp
       BASIS             def2-tzvpd
       SCF_ALGORITHM     gdm ! usually recommended with ROKS, but not necessary
       SCF_GUESS         read
       ROKS              true
       STEP              true
       SCF_CONVERGENCE   7
    $end
    
    ! prints all level-shift information
    $step
    Epsilon 10
    Print   2
    $end
    
    $reorder_mo
       1 2 3 4 5 6 7
       1 2 3 4 5 6 7
    $end
    ```
