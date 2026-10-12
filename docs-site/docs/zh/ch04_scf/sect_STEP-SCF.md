---
title: "4.5.16 态定向能量投影（State-Targeted Energy Projection, STEP）"
---

## 4.5.16 态定向能量投影（State-Targeted Energy Projection, STEP）

（2026 年 7 月 4 日）

最大重叠方法（Maximum Overlap Method, MOM，见第 [4.5.14](topic_mom.md) 节）在许多情况下都能成功，但在优化激发态轨道时，容易发生变分塌缩（variational collapse，即从目标组态跌落至基态）。这一问题通过"初始"MOM（initial MOM, IMOM）流程得到了改善，该流程使用初始猜测的分子轨道系数作为重叠判据的参考（详见第 [7.7.2](../ch07_excited/ex_OpSing.md) 节）。尽管 IMOM 对 MOM 有显著改进，但它偶尔也会遭遇变分塌缩，这促使人们寻找这些方法的替代方案。

其中一种替代方案由 Kevin Carter-Fenk 和 John Herbert 提出，即态定向能量投影（state-targeted energy projection, STEP）流程，它采用一个简单的能级偏移（level-shift）形式体系来收敛到目标态。[[196]](../bib_references/bib.md#bib189)

STEP 算法保留了 MOM 流程的性价比（每次迭代的代价与普通自洽场（SCF）计算基本相同），同时在收敛到目标态方面far为稳健。
有关 STEP 流程的更多细节参见第 [7.7.8](../ch07_excited/ex_ROSTEP.md) 节，关于 STEP 算法的完整论述，请读者参阅文献 [[196]](../bib_references/bib.md#bib189)
。

与 STEP 相关的 *$rem* 变量如下：

### `STEP`

> **启用 STEP 流程。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **可选值**:
>     * `FALSE`: 不应用 STEP 能级偏移算法。
>     * `TRUE`: 应用 STEP 能级偏移算法。
> * **建议**: 无

### `STEP_EPSILON`

> **以 $N$ /100 Hartree 为单位调节能级偏移所施加的占据/虚拟轨道间隙的大小。**
>
> * **类型**: `INTEGER`
> * **默认值**: `10`
> * **可选值**:
>     * $N$
> * **建议**: 除非出现收敛问题，否则使用默认值；此时可以使用较大的值，直到找到所需的状态。请注意，在能级偏移算法中增大占据/虚拟间隙会减缓收敛速度，因此在需要较大偏移时，建议同时增大 SCF_MAX_CYCLES。

### `STEP_PRINT`

> **控制 STEP 算法信息的打印级别。**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **可选值**:
>     * `0`: 在 SCF 迭代之间不打印任何关于 STEP 的信息。
>     * `1`: 打印每次 SCF 迭代所施加的能级偏移（R-STEP 与 U-STEP）。
>     * `2`: 针对三重态（triplet）态和混合（mixed）态，每次 SCF 迭代都打印其能级偏移（RO-STEP）。
> * **建议**: 使用默认值。能级偏移为 0 表明构造原理（aufbau）判据足以确定轨道占据情况，而偏移 $>0$ 则意味着占据空间的选取偏离了构造原理。
