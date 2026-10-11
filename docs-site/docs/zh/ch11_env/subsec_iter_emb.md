---
title: "11.6.4 超分子性质的迭代方法"
---

## 11.6.4 超分子性质的迭代方法

（2026 年 7 月 4 日）

迭代嵌入方法（Iterative Embedding Method）是计算超分子（Supermolecular）性质的一种有效方法。[[383]](../bib_references/bib.md#bib391)
 请求执行迭代嵌入计算的关键字是 EMB_ITER。
在该方法中，在后续的嵌入计算中，体系的不同部分被依次选为活性片段（Active Fragment）。
然后将该性质表示为各片段贡献之和。
必须对每个片段重复高精度（High-level）计算，但这比一次性的处理整个体系在计算上要廉价得多。

利用迭代嵌入方法可以计算超分子静态极化率（Static Polarizability）。在该方法中，
极化率张量 $\mathbb{\alpha}$ 的元素 $\alpha_{xy}$ 计算为

<a id="Ch11.E118"></a>

$$
\alpha_{xy}=\sum_{A}{(\alpha_{xy})_{A}} \tag{11.118}
$$

其中对活性片段 A 的求和涵盖整个体系。
该方法也可用于计算超分子偶极矩。偶极矩矢量 $\mathbb{\mu}$ 的分量 $\mu_{x}$ 由下式得到

<a id="Ch11.E119"></a>

$$
\mu_{x}=\sum_{A}{(\mu_{x})_{A}} \tag{11.119}
$$

触发上述功能的关键字分别为 EMB_POL 和 EMB_DIPOLE。

EMB_ITER

### `EMB_ITER`

> **开启迭代投影密度嵌入**
>
> * **类型**：`BOOLEAN`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE
>     * 不在不同片段之间进行迭代。
>     * TRUE
>     * 开启迭代密度嵌入。
> * **建议**：无

EMB_POL

### `EMB_POL`

> **触发迭代极化率张量的计算**
>
> * **类型**：`BOOLEAN`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE
>     * 不计算迭代极化率张量。
>     * TRUE
>     * 计算迭代极化率张量。
> * **建议**：无

EMB_DIPOLE

### `EMB_DIPOLE`

> **触发迭代偶极矩的计算**
>
> * **类型**：`BOOLEAN`
> * **默认值**：`FALSE`
> * **选项**：
>     * FALSE
>     * 不计算迭代偶极矩。
>     * TRUE
>     * 计算迭代偶极矩。
> * **建议**：无
