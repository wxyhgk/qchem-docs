---
title: "12.6.7 采用非 *Aufbau*（非构造原理）电子组态的 ALMO-EDA"
---

## 12.6.7 采用非 *Aufbau*（非构造原理）电子组态的 ALMO-EDA

（2026 年 7 月 4 日）

**Q-Chem** 还支持一个或多个片段（fragment）处于非 *aufbau*（非构造原理）电子组态的 ALMO-EDA（绝对定域分子轨道能量分解分析，Absolutely Localized Molecular Orbital Energy Decomposition Analysis）计算。[[899]](../bib_references/bib.md#bib931)
该方法特别适用于如下情形：给定片段在形成分子间复合物后，其能量最稳定的电子态发生了变化——这在涉及开壳层（open-shell）物种（如卡宾、过渡金属阳离子等）的体系中十分常见。例如，孤立的 Ba${}^{+}$ 自由基阳离子的最低能量电子组态为 6s${}^{1}$；
然而，当其与 CO 配位时，若 Ba${}^{+}$ 的单电子从 6s${}^{1}$ 激发至 5d${}^{1}$，复合物反而更加稳定，因而相对于孤立的 Ba${}^{+}$ 阳离子，该组态处于非 *aufbau* 状态。
研究此类复合物形成的一种合理策略是：对处于 5d${}^{1}$ 电子组态的 Ba${}^{+}$ 执行 ALMO-EDA 计算，
然后评估 Ba${}^{+}$(5d${}^{1}$) 与 Ba${}^{+}$(6s${}^{1}$) 之间的能量差，并将其解释为单体的“电子激发制备（electronic preparation）”能。
为确保体系在整个计算过程中保持在给定的非 *aufbau* 电子组态，
最大重叠方法（Maximum Overlap Method）[[443]](../bib_references/bib.md#bib455)
（MOM，详见第 [4.5.14](../ch04_scf/topic_mom.md) 节）被应用于 ALMO-EDA 的几乎所有阶段，包括 (i) 孤立片段计算、(ii) 极化波函数计算，以及 (iii) 整个体系的完整自洽场（Self-Consistent Field, SCF）计算。
其中，(i) 与 (iii) 是使用 MOM 的标准 SCF 计算，而 (ii) 则是将 MOM 应用于 SCF-MI（片段间自洽场，SCF in Molecular Interacting fragments）计算，[[899]](../bib_references/bib.md#bib931)
该做法与使用直接迭代在子空间中的方法（Direct Inversion in the Iterative Subspace, DIIS）算法求解局域投影 SCF 方程（FRGM_METHOD = STOLL 或 GIA，见第 [12.5.1](sect_lp_scf.md) 节）相兼容。

具体而言，对处于非 *aufbau* 电子组态的复合物进行 ALMO-EDA 计算（假设仅有一个片段被激发）
包含以下步骤：

- •

对所有片段执行基态 SCF 计算
- •

使用 MOM，按输入中指定的方式计算该片段的非 *aufbau* 电子组态：激发该片段所消耗的能量在输出中以*制备（preparation）*能（$E_{\mathrm{prp}}$）的形式报告；
以此构建体系的冻结态（frozen state），即该片段处于非 *aufbau* 态，其余片段处于基态
- •

从冻结态出发，执行带 MOM 的 SCF-MI 计算，以获得非 *aufbau* 电子组态下的极化态（polarized state）
- •

从非 *aufbau* 态下的极化波函数出发，执行带 MOM 的完整 SCF 计算

此类计算除标准 EDA2 任务的常规设置外，还需要设置 EDA2_MOM = TRUE。
非 *aufbau* 电子态通过 *$scfmi_mom* 输入节来指定，其格式如下：

> ```qchem
> $scfmi_mom
> frag_idx1   X_1   Y_1   spin_1
> frag_idx2   X_2   Y_2   spin_2
> ...
> $end
> ```

在每一行中，第一个条目指定非 *aufbau* 片段的索引（从 1 开始）。第二个与第三个条目指定非 *aufbau*
电子组态，其构造方式为：在该片段的基态 SCF 计算完成后，将一个电子从该片段的 HOMO$-$X 激发到 LUMO$+$Y。
最后一个条目指定被交换的占据轨道与虚轨道的自旋（“a” 表示 $\alpha$ 电子，“b” 表示 $\beta$ 电子；
若第四个条目留空，则默认使用 $\alpha$ 轨道）。例如，若要在第一个片段上执行
HOMO$\rightarrow$LUMO 激发，该节只需写成

> ```qchem
> $scfmi_mom
> 1  0  0  a
> $end
> ```

**Q-Chem** 5 还允许在不执行完整 ALMO-EDA 流程的情况下，对非 *aufbau* 电子组态进行 SCF-MI 计算，[[899]](../bib_references/bib.md#bib931)
做法非常简单：只需在 SCF-MI 计算的 *$rem* 设置中添加 SCFMI_MOM = TRUE（见第 [12.6.2](sect_gen_scfmi.md) 节）。
非 *aufbau* 电子组态同样可以通过 *$scfmi_mom* 节按相同方式指定。

EDA2_MOM

### `EDA2_MOM`

> **使用 MOM 对非 *aufbau*（非构造原理）电子组态执行 ALMO-EDA 计算**
>
> * **类型**：`BOOLEAN`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE
>     * 标准 ALMO-EDA 计算
>     * TRUE
>     * 针对非
>     * aufbau
>     * 态的 ALMO-EDA 计算
> * **建议**：无

### `SCFMI_MOM`

> **使用 MOM 对非构造原理（non-aufbau）电子组态执行 SCF-MI 计算**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 标准 SCF-MI 计算
>     * TRUE
>     * 使用 MOM 的 SCF-MI 计算
> * **建议**: 无

请注意，EDA2_MOM 与 SCFMI_MOM 可以在不显式设置 *$scfmi_mom* 段的情况下使用，此时在 SCF-MI 或 ALMO-EDA 计算中，将由两个基态碎片构造的冻结态的电子组态得以保留。

???+ example "示例 12.19: 在 B3LYP/def2-TZVP 水平下，对 Ba 处于 5d ${}^{1}$ 非构造原理电子组态的 [Ba(CO)] ${}^{+}$ 配合物进行 ALMO-EDA 计算。$scfmi_mom 段指定将 6s 轨道中的单电子 $\alpha$ 电子提升至某个 5d 轨道。"
    ```qchem
    $molecule
    1 2
    --
    1 2
    Ba   0.0  0.0  0.0
    --
    0 1
    C    0.0  0.0  2.734
    O    0.0  0.0  3.876
    $end
    
    $rem
       JOBTYPE           EDA    !by default EDA2 = 2 with CT analysis
       METHOD            B3LYP
       BASIS             DEF2-TZVP
       ECP               DEF2-ECP
       UNRESTRICTED      TRUE
       SCF_CONVERGENCE   8
       SCF_ALGORITHM     DIIS
       EDA2_MOM          TRUE
    $end
    
    $scfmi_mom
    1 0 2
    $end
    ```
