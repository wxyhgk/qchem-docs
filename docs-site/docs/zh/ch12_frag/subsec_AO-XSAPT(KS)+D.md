---
title: "12.10.3 色散模型（Dispersion Models）"
---

## 12.10.3 色散模型（Dispersion Models）

（2026 年 7 月 4 日）

SAPT(KS) 计算及其多体扩展形式 XSAPT(KS)，采用 Kohn-Sham 密度泛函理论（Kohn-Sham Density Functional Theory, KS-DFT）来描述各个单体，从而以低成本的方式引入*分子内*（intra*molecular*）电子关联，随后再用二阶对称匹配微扰理论（Symmetry-Adapted Perturbation Theory, SAPT）来描述*分子间*（inter*molecular*）相互作用。正如前文所述，即便使用了经过调参的长程校正（LRC）泛函[[761]](../bib_references/bib.md#bib794)，所得到的相互作用能也无法达到基准（benchmark）精度，这是因为虽然对单体使用 DFT 通常能改善氢键的描述（相对于基于 Hartree-Fock 的 SAPT0 计算），但对色散作用的描述往往会变差[[560]](../bib_references/bib.md#bib574)。无论如何，SAPT0 的色散项本身也达不到基准精度，因为它带有 MP2 方法对色散作用的高估这一通病。与此同时，色散项与交换-色散（exchange-dispersion）项正是 SAPT0 或 SAPT(KS) 计算中最昂贵的部分，其关于体系规模的形式标度分别达到 ${\cal{O}}({N^{4}})$ 与 ${\cal{O}}({N^{5}})$。SAPT0 中的其他各项标度不超过 ${\cal{O}}({N^{3}})$，并且可以借助 SAPT 中非色散项的原子轨道（atomic orbital, AO）基实现，对大单体进行高效计算[[764]](../bib_references/bib.md#bib798)。

有鉴于此，如果把二阶色散项，*即*式 ([12.61](Ch12.S9.SS1.md#eq:SAPT_interaction)) 与式 ([12.65](Ch12.S9.SS1.md#eq:E(2)_disp)) 中的 $E_{\mathrm{disp}}^{(2)}+E_{\mathrm{exch\mbox{-}disp}}^{(2)}$，替换为一个*特设（ad hoc）*的、形如 $-C_{6}/R^{6}-C_{8}/R^{8}-\cdots$ 的原子-原子色散势，那么 XSAPT(KS) 计算的效率与精度都会得到提升。这让人联想到色散校正 DFT，即第 [5.7.3](../ch05_dft/subsec_DFT-D.md) 节所介绍的 DFT-D 方法。不过与 DFT 的情形不同，色散能在 SAPT 框架内是有明确定义且可分离的，因此可以用原子-原子势来替换它，而不必担心关联效应的重复计算（double counting）问题——而 DFT-D 中这种重复计算是不可避免的。此外在本方法中，由于色散贡献可分离，这些色散势可以直接拟合到高精度 SAPT 计算 [SAPT(DFT) 与 SAPT2+(3)] 给出的 *ab initio* 色散能。因此，尽管下文描述的色散势在形式上是经典的，也确实包含拟合参数，但仍然可以合理地称之为 *ab initio* 色散势。我们将该方法记作“+*ai*D”[[764]](../bib_references/bib.md#bib798)，以区别于 DFT-D 的“+D”色散校正，尽管在我们早期的工作中曾简单地称其为“+D”[[759]](../bib_references/bib.md#bib792)。该组合方法称为 XSAPT(KS)+*ai*D；概览见文献 [[760]](../bib_references/bib.md#bib793)，AO 基下的高效实现见文献 [[764]](../bib_references/bib.md#bib798)。后者展现出 ${\cal{O}}({N^{3}})$ 的标度且没有显著内存瓶颈，可应用于单体含 $\gtrsim 100$ 个原子的超分子复合物[[764]](../bib_references/bib.md#bib798)。

若要请求一次 XSAPT(KS)+*ai*D 计算，请在 *$rem* 区段中设置 JOBTYPE = XSAPT 以执行 XSAPT，并选择合适的 SCF 方法（Hartree-Fock 或 DFT）。算法中的 +*ai*D 部分由 *$sapt* 输入区段中的两个关键字来启用：首先，将 **Algorithm** 设为 **AO** 以选择基于 AO 的 ${\cal{O}}({N^{3}})$ 版 XSAPT；其次，按照下文所述的选项之一，在 *$sapt* 区段中设置 **Dispersion**。可用的模型包括成对经验色散（+*ai*D）模型[[759]](../bib_references/bib.md#bib792)，多体色散（+MBD）势[[200]](../bib_references/bib.md#bib188)及其修订版本（+MBDrev）[[1406]](../bib_references/bib.md#bib1465)，以及“优化型”（optimized）$C_{6}$-$C_{8}$ MBD 模型，下文将逐一说明。就小分子的总相互作用能而言，这些模型的结果非常接近[[762]](../bib_references/bib.md#bib795)，但在处理大分子和离子时表现有所不同[[200]](../bib_references/bib.md#bib188)。

### `Dispersion`

> **请求用于 (X)SAPT 的色散势。输入区段：$sapt**
>
> * **类型**: `STRING`
> * **默认值**: `aiD3`
> * **选项**:
>     * aiD
>     * 第一代经验成对色散势
>     * aiD2
>     * 第二代经验成对色散势
>     * aiD3
>     * 第三代经验成对色散势
>     * MBD
>     * 多体
>     * $C_{6}$
>     * 与
>     * $C_{8}$
>     * 色散势
>     * MBDrev
>     * 修订版 MBD 色散，针对 SAPT10K 数据重新拟合
>     * OC8AIMMBD
>     * 采用非相对论性自由原子参考数据的优化型
>     * $C_{6}$
>     * -
>     * $C_{8}$
>     * MBD
>     * OC8RAIMMBD
>     * 采用相对论性参考数据的优化型
>     * $C_{6}$
>     * -
>     * $C_{8}$
>     * MBD
>     * RAIMVDW
>     * 仅含成对的分子内原子（atoms-in-molecules）色散（不含 MBD 项），
>     * 使用相对论性参考数据
> * **建议**: 基于 MBD 的模型通常优于 ai D 模型，尤其是对于 MBD 效应（超出成对加和的部分）变得重要的大体系。优化型 $C_{6}$ - $C_{8}$ MBD 模型在离子体系上表现更佳，并通过相对论性参考数据将 MBD 拓展至重元素。

+*ai*D 势对色散采用成对近似，即假定相互作用势在所有原子对上可加和。成对色散近似使用形如下的原子对求和，

<a id="eq:PairwiseDispersion"></a>
$$
E_{\text{disp}}=-\sum_{i\in A}\sum_{\begin{subarray}{c}j\in B\\
A\neq B\end{subarray}}\Bigg{[}f_{6}(R_{ij})\frac{C_{6}^{ij}}{R^{6}_{ij}}+f_{8}(R_{ij})\frac{C_{8}^{ij}}{R^{8}_{ij}}\Bigg{]}\;, \tag{12.68}
$$

其中 $i$ 与 $j$ 分别是分子 $A$ 和分子 $B$ 中的原子核。最初的 +*ai*D1 模型[[759]](../bib_references/bib.md#bib792)是拟合到总相互作用能，而非直接拟合 *ab initio* 色散数据，因此它在复现各个能量分量方面表现差得多，不再推荐使用[[760]](../bib_references/bib.md#bib793)。+*ai*D2[[760]](../bib_references/bib.md#bib793) 与 +*ai*D3[[762]](../bib_references/bib.md#bib795) 的区别在于后者拥有更大的训练集，其设计目的是更好地覆盖 $\pi$ 堆积（$\pi$-stacked）体系。因此在 +*ai*D 系列的成对势中，+*ai*D3 校正更优。但话说回来，由于原子对之间的相互作用会受到分子中局域电动力学环境（local electrodynamic environment）的调制，色散的成对近似在极大体系的极限下会失效[[764]](../bib_references/bib.md#bib798)。尽管有人基于 XSAPT 与 SAPT 色散能之差提出了对这一成对近似的修正[[765]](../bib_references/bib.md#bib799)，但所有 +*ai*D 模型都是*特设的（ad hoc）*，其修正并不依赖于所采用的理论水平。+MBD 势使用了 Ambrosetti 等*人*[[43]](../bib_references/bib.md#bib27)提出的多体色散（many-body dispersion）势的一个改进版本（见第 [5.7.6](../ch05_dft/sect_MBD.md) 节），以便自然地刻画非加和色散[[200]](../bib_references/bib.md#bib188)。由于 +MBD 方法基于电子密度，它与所使用的 *ab initio* 方法有着更紧密的联系[[199]](../bib_references/bib.md#bib191)。与 XSAPT 流程结合后，XSAPT+MBD 能量分解能够同时计入非加和的极化效应与色散效应。凭借其在任意体系规模下的出色表现，+MBD 势在多数情况下都是推荐选择。为了提升色散相互作用在多样化学环境中的可迁移性与精度，MBD 模型中的四个参数已针对由 SAPT2+(3)(CCD)/aug-cc-pVTZ 色散能构成的综合性 SAPT10K 基准数据集重新优化[[1406]](../bib_references/bib.md#bib1465)。由此得到的修订模型记作 MBDrev，它与用于非色散贡献的 (X)SAPT 联合使用，相较原始 (X)SAPT+MBD 方案带来了系统性的精度提升，在包含数百个原子的、化学上真实的体系上同样如此[[767]](../bib_references/bib.md#bib800)。然而，MBD 类色散模型所固有的 Hirshfeld 划分对离子而言定义不佳，MBD 在离子上有时会给出较差的结果[[557]](../bib_references/bib.md#bib588)，甚至不及 +*ai*D3[[481]](../bib_references/bib.md#bib492)。出于这一原因，还提供了一族优化型的“分子内原子”（atoms-in-molecules）色散模型，其中每个原子的响应性质 $(\alpha_{0}$、$C_{6}$ 与 $R_{\mathrm{vdW}})$ 通过对自由原子参考数据进行 Tkatchenko–Scheffler 标度得到[[1361]](../bib_references/bib.md#bib1421)，并使用了在离子情形下表现更好的迭代版 Hirshfeld 体积划分。与原始的 (X)SAPT+MBD 方案一样[[200]](../bib_references/bib.md#bib188)，这些模型同时结合了 $C_{6}/R^{6}$ 与 $C_{8}/R^{8}$ 色散项，前者由 Tkatchenko MBD 模型的 Drude 振子哈密顿量[[43]](../bib_references/bib.md#bib27)计算。不过这一新的“优化型”方法使用的 $C_{8}$ 参数，是从 $C_{6}$ MBD 计算中的 Drude 振子不变量（invariants）以最优方式导出的[[464]](../bib_references/bib.md#bib477)。这一供 (X)SAPT 使用的新模型族统称为 “oC8aimMBD”（optimized atoms-in-molecules MBD），其中有三个变体，彼此仅在自由原子参考数据上有所不同，具体如上文 **Dispersion** 关键字说明中所示。oC8aimMBD 方法对自由原子使用非相对论性 Hartree–Fock 参考数据，而 oC8(r)aimMBD 则在非收缩（uncontracted）Dyall 基组中使用四分量 Dirac–Hartree–Fock 参考，凡出现 $Z>36$ 的元素时均推荐使用后者。最后，(r)aimVDW 模型仅保留成对的 $C_{6}/R^{6}$ 校正，而去掉了多体项。按碎片进行的 Hirshfeld 计算会自动启用；在 *$xpol* 区段中将 **print** 设为 3，即可报告用于标度色散参数的逐原子 Hirshfeld 体积比。

与 XPol 一样，XSAPT 与 XSAPT(KS)+*ai*D 方法无法处理外部电荷（external changes）。它们只提供单点能，且不允许使用冻结轨道（frozen orbitals）。闭壳层（restricted）与开壳层（unrestricted）两种版本均可用。使用 XSAPT(KS)+*ai*D 的研究者被要求引用：+*ai*D1 见文献 [[759]](../bib_references/bib.md#bib792)，+*ai*D2 见文献 [[760]](../bib_references/bib.md#bib793)，
