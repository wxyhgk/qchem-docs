---
title: "11.6.4 超分子性质的迭代方法"
---

## 11.6.4 超分子性质的迭代方法

(July 4, 2026)

迭代嵌入方法（iterative embedding method）是计算超分子性质（supermolecular properties）的一种有效方法。[[383]](../bib_references/bib.md#bib391)
 用于请求迭代嵌入计算的关键字是 EMB_ITER。
在该方法中，系统的不同部分在后续的嵌入计算中被依次选为活性片段（active fragment）。
性质随后表示为各个片段贡献之和。
每个片段都必须重复进行高层级（high-level）计算，但这比一次性处理整个体系的计算代价更低。

可以利用迭代嵌入方法计算超分子的静态极化率（static polarizabilities）。在该方法中，极化率张量 $\mathbb{\alpha}$ 的元素 $\alpha_{xy}$ 按如下方式计算

<a id="Ch11.E118"></a>
$$
\alpha_{xy}=\sum_{A}{(\alpha_{xy})_{A}} \tag{11.118}
$$

其中对活性片段 A 的求和覆盖整个体系。
该方法同样可用于计算超分子的偶极矩（dipole moments）。偶极矩矢量 $\mathbb{\mu}$ 的分量 $\mu_{x}$ 按如下方式获得

<a id="Ch11.E119"></a>
$$
\mu_{x}=\sum_{A}{(\mu_{x})_{A}} \tag{11.119}
$$

触发这些功能的关键字分别为 EMB_POL 和 EMB_DIPOLE。

EMB_ITER

### `EMB_ITER`

> **开启基于投影的迭代密度嵌入（iterative projection-based density embedding）**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 不对不同片段进行迭代。
>     * TRUE
>     * 开启迭代密度嵌入。
