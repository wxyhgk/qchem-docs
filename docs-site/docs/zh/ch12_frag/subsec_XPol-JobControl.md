---
title: "12.8.3 XPol 的作业控制变量"
---

## 12.8.3 XPol 的作业控制变量

(July 4, 2026)

通过将 *$rem* 变量 XPOL 设置为 TRUE 来启用 XPol 计算。
XPol 方法可以与 Hartree-Fock 理论以及大多数密度泛函（Density Functional, DF）结合使用，
一个显著的例外是 XPol 尚未针对元广义梯度近似（meta-GGA）泛函实现（第 [5.3](../ch05_dft/sect_XCfuncs.md) 节）。
XPol 与溶剂化模型（第 [11.2](../ch11_env/topic_solvation.md) 节）或外部
电荷（*$external_charges*）的结合使用也不受支持。当使用 Mulliken、Löwdin 或 CM5 嵌入电荷时可解析计算梯度（Analytic Gradients），但对于 ChElPG 嵌入电荷尚不支持。

XPOL

### `XPOL`

> **执行自洽的 XPol 计算。**
>
> * **类型**: `BOOLEAN`
> * **默认值**: `FALSE`
> * **选项**:
>     * TRUE
>     * 执行 XPol 计算。
>     * FALSE
>     * 不执行 XPol 计算。
> * **建议**: 无（NONE）

其他 XPol 选项通过 *$xpol* 段中包含的关键字来指定。
这些关键字列示如下。

### `embed`

> **指定所使用的静电嵌入（electrostatic embedding）类型。输入段：$xpol**
>
> * **类型**: `STRING`
> * **默认值**: `Charges`
> * **选项**:
>     * None
>     * 不使用嵌入电荷。
>     * Charges
>     * 原子点电荷（标准 XPol 方法）。
>     * Density
>     * 片段密度（与 FMO 方法类似；参见
>     * 第 12.12
>     * 节）
> * **建议**: 标准 XPol 方法使用原子点电荷。

### `charges`

> **指定所使用的原子点电荷类型。输入段：$xpol**
>
> * **类型**: `STRING`
> * **默认值**: `CM5`
> * **选项**:
>     * Mulliken
>     * Mulliken 电荷
>     * Lowdin
>     * Löwdin 电荷
>     * CHELPG
>     * ChElPG 电荷
>     * CM5
>     * CM5 电荷
> * **建议**: 在扩展基组（extended basis sets）中使用 Mulliken 电荷出现的问题可能导致 XPol 收敛失败。Löwdin 电荷往往稍微更稳定，而 ChElPG 电荷相当稳健，并能提供精确的静电嵌入。然而，ChElPG 电荷的计算代价更高，并且在含有带电单体的体系中，其表现略逊于 CM5 电荷。CM5 电荷是一种性价比较高且略微更精确的选择。对于 XSAPT 计算（第 12.10 节），推荐使用 CM5 电荷。但是，CM5 电荷尚不适用于 AIFDEM 作业（第 12.14 节），在这种情况下推荐使用 ChElPG 电荷。

### `print`

> **指定 XPol 代码的输出级别。输入段：$xpol**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **选项**:
>     * $n$
>     * 期望的输出级别
> * **建议**: 较高的值会输出额外的信息

尤其在 SAPT(KS) 计算（参见第 [12.9](topic_sapt.md) 节）和 XSAPT(KS) 计算（第 [12.10](sect_XSAPT.md) 节）的背景下——
在这类方法中，单体的 Kohn-Sham 描述与对称适配微扰理论
（symmetry-adapted perturbation theory, SAPT）相结合——至关重要的是，
Kohn-Sham 密度泛函必须表现出正确的渐近行为。[[761]](../bib_references/bib.md#bib794)
大多数标准密度泛函*不*满足这一准则，但可以通过使用 range-separated（程分离）混合泛函来强加该准则，其中 range-separation（程分离）参数
$\omega$ 经过调节以满足 DFT 的电离势定理，
即 $\mbox{IE}(\omega)=-\epsilon_{\rm HOMO}(\omega)$。这一条件
应在 XPol 计算中对每个单体分别施加，这就要求
每个单体使用不同的 $\omega$ 值。通过在
*$xpol* 段中设置 **DFT-LRC** 选项来请求此功能。（注意，该关键字无需设置任何值；
只要它出现在 *$xpol* 段中，该选项即被启用。）

### `DFT-LRC`

> **指定是否使用单体专属的 range-separated（程分离）混合泛函。输入段：$xpol**
>
> * **类型**: `None`
> * **默认值**: `Not specified`
> * **选项**:
>     * 若该关键字存在，则启用此选项。
> * **建议**: 将此关键字放入 $xpol 段表示将使用单体专属的 $\omega$（range-separation，程分离参数）值，这就需要一个 $lrc_omega 输入段。

如果指定了 **DFT-LRC**，则还需要一个 *$lrc_omega* 输入段。
该输入段仅由每个单体的取值 $\omega_{1},\omega_{2},\ldots$ 组成，按各单体在
*$molecule* 段中出现的顺序逐行列出。这些值的单位与 range-separated 混合
泛函计算中使用的 *$rem* 变量 OMEGA 相同，即在原子单位制下
$\omega=$ OMEGA/1000。关于在 XSAPT(KS) 方法背景下如何使用
**DFT-LRC** 选项和 *$lrc_omega* 输入段的示例，请参见
第 [12.10.3](subsec_AO-XSAPT_KS_D.md) 节。
