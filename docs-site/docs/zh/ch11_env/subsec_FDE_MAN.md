---
title: "11.7.2 FDE-Man"
---

## 11.7.2 FDE-Man

（2026 年 7 月 4 日）

**Q-Chem** 的 FDE-Man 模块中提供了若干基于 FDET（冻结密度嵌入理论，Frozen-Density Embedding Theory）的方法。
FDE-Man 的任务控制分为两个部分，即 *$rem* 和 *$fde*。

各片段通过 *$molecule* 段中的片段描述符（fragment descriptor）来指定（见第 [12](../ch12_frag/chap_frag.md) 章），其中第一个片段对应被嵌入的体系（A），第二个片段表示环境（B）。

**注意：

当前实现仅允许闭壳层（closed shell）片段。
**

FDE

### `FDE`

> **开启密度嵌入（density embedding）。**
>
> * **类型**：`BOOLEAN`
> * **默认值**：`False`
> * **选项**：
>     * True
>     * 执行 FDET 计算。
>     * False
>     * 不执行 FDET 计算。
> * **建议**：将 $rem 变量设置为 TRUE 以启动 FDET 计算。

启用 FDE-Man 后，嵌入方法的指定以及其他任务控制参数（收敛阈值、最大迭代次数 *等*）应在 *$rem* 段中设置。

METHOD

### `METHOD`

> **确定当 FDE = TRUE 时，嵌入波函数应采用哪种基于 FDET 的方法。**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * NAME
>     * 使用
>     * =
>     * NAME
>     * ，其中
>     * NAME
>     * 取值为
>     * HF
>     *（Hartree-Fock 理论），或者为第
>     * 5.3.5
>     * 节所列的 DFT 方法之一。
> * **建议**：无

如第 [5.4](../ch05_dft/sect_DFT_METHOD.md) 节所述，也可以通过 EXCHANGE 和 CORRELATION 关键字来指定其他 DFT 泛函。

**注意：

当前实现仅限于由 SCFMAN 模块求解的 mean-field（平均场）方法。
**

FDE-Man 模块同样支持使用自定义基组（customized basis set）的标准功能。

## 11.7.2.1 FDE-ADC

FDE-ADC[[1121]](../bib_references/bib.md#bib1168)
 是一种密度嵌入方法，它将针对极化传播子（polarization propagator）的代数图构（Algebraic Diagrammatic Construction，ADC）方案（第 [7.10](../ch07_excited/sect_exadc.md) 节）与冻结密度嵌入理论（FDET）结合起来。
在这一特定变体中，子系统 A 由波函数描述，而子系统 B 由密度描述。FDE-ADC 方法采用线性化的 FDET 近似[[1539]](../bib_references/bib.md#bib1603)。

与其他方法类似，ADC 的相关设置也必须在 *$rem* 段内完成，如下所示。

METHOD

### `METHOD`

> **确定当 FDE = TRUE 时应采用哪种基于 FDET 的方法。**
>
> * **类型**：`STRING`
> * **默认值**：`None`
> * **选项**：
>     * adc(2)
>     * 执行 FDE-ADC(2)-s 计算。
>     * adc(2)-x
>     * 执行 FDE-ADC(2)-x 计算。
>     * adc(3)
>     * 执行 FDE-ADC(3) 计算（势由 MP(2) 密度构造）。
>     * cvs-adc(2)
>     * 执行核心激发（core excitation）的 FDE-ADC(2)-s 计算。
>     * cvs-adc(2)-x
>     * 执行核心激发的 FDE-ADC(2)-x 计算。
>     * cvs-adc(3)
>     * 执行核心激发的 FDE-ADC(3) 计算。
> * **建议**：无

FDE-ADC 还支持由 **libwfa** 模块执行的激发态分析（STATE_ANALYSIS）。
