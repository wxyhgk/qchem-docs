---
title: "11.5.5 大分子扩展：碎片化 EFP 方案"
---

## 11.5.5 大分子扩展：碎片化 EFP 方案

（2026 年 7 月 4 日）

蛋白质或 DNA 等大分子涉及大量可用 QM/EFP 框架描述的电子结构问题（光化学、氧化还原化学、反应性）。EFP 已通过所谓的碎片化 EFP 方案（fragmented EFP scheme, fEFP）扩展至此类复杂体系。当前的 **Q-Chem** 实现允许：(i) 计算配体与大分子之间的相互作用能（二者均以 EFP 表示），以及 (ii) 使用 QM/EFP 方案计算与 fEFP 大分子相互作用的 QM 片团的激发能、电离势和电子亲和能（见第 [11.5.3](sec_EOM-EFP.md) 节）。在当前实现中，配体不能与大分子以共价键相连。

将大分子切割为单元的方式有多种，具体取决于两个共价键合残基之间切割位置的选择。切割蛋白质的一种直观方式是沿肽键切割，使每个碎片代表一个氨基酸。另一种方式是在两个同类型原子之间切割（羰基与碳-$\alpha$ 之间，或碳-$\alpha$ 与侧链第一个碳之间）。用户可以选择最合适的切割方式。

考虑由 $N$ 个氨基酸 $A_{1}A_{2}\ldots A_{N}$ 组成的蛋白质（$P$），将其分割为 $N$ 个碎片（$A_{i}$）。碎片可以用“氢连接原子”（hydrogen link atom, HLA）[[1259]](../bib_references/bib.md#bib1311)
 饱和，也可以用来自相邻碎片的一价原子团饱和，后者在本文中称为“盖层连接原子”（cap link atom, CLA）。若采用 HLA 方案对碎片加盖，则氢原子位于肽键轴向上，其距离对应于 C–H 键的平衡键长：

<a id="eq:hla"></a>
$$
P=A_{1}H+\sum_{i=2}^{N-1}HA_{i}H+HA_{N} \tag{11.89}
$$

在 CLA 方案中，盖层与相应相邻基团具有完全相同的几何结构。若沿肽键切割（一个碎片为一个氨基酸），则盖层（$C^{i}$）或者是用于饱和碎片 -N(H) 端的醛基，或者是用于饱和碎片 -C(=O) 端的胺基。

<a id="eq:cla"></a>
$$
P=A_{1}C^{2}+\sum_{i=2}^{N-1}C^{i-1}A_{i}C^{i+1}+C^{N-1}A_{N} \tag{11.90}
$$

**Q-Chem** 提供了一个位于 `$QC/bin` 中的两步脚本 `prefefp.pl`，它读取 PDB 文件并将其拆分为加盖碎片，输出为 **gamess** 格式，从而可以为这些加盖碎片生成 EFP 参数，具体如第 [11.5.11](sec_fefp-param.md) 节所述。由于 EFP 参数是针对每个加盖碎片生成的，在 HLA 和 CLA 方案中，由于盖层的重叠，相邻碎片会存在重复的参数点（重叠区域）。由于多极展开点和极化率展开点都是按标准流程在每个加盖残基上计算的，因此需要从重叠区域中移除相应的多极矩（及阻尼项）和极化率（$C^{\emptyset}$）。

式 ([11.89](#eq:hla)) 和 ([11.90](#eq:cla)) 变为：

<a id="eq:hcla"></a>
$$
P=A_{1}C^{\emptyset}+\sum_{i=2}^{N-1}C^{\emptyset}A_{i}C^{\emptyset}+C^{\emptyset}A_{N} \tag{11.91}
$$

有关这一移除过程的细节见第 [11.5.11](sec_fefp-param.md) 节。

一旦从加盖碎片的 EFP 参数中移除这些重复参数，即可照常进行 EFP-EFP 和 QM-EFP 计算。

目前，fEFP 包含静电贡献和极化贡献，它们出现在 EFP(配体)/fEFP(大分子) 以及 QM/fEFP 计算中（注意 QM 部分与大分子之间没有共价键连接）。因此，配体（$L$）与被分割为碎片的蛋白质（$P$）之间的总相互作用能（$E^{\text{tot}}$）为：

<a id="eq:fefp-tot"></a>
$$
E^{\text{tot}}(P-L)=E^{\text{elec}}(P-L)+E^{\text{pol}}(P-L) \tag{11.92}
$$

静电作用是加和项；其对碎片-碎片以及配体-碎片相互作用的贡献按如下方式计算：

<a id="eq:la-fefp-elec"></a>
$$
E^{\text{elec}}(P-L)=\sum_{i}^{N}{E^{\text{elec}}\left(C^{\emptyset}A_{i=1}C^{\emptyset}-L\right)}\;. \tag{11.93}
$$

纯 EFP 体系（无 QM）中的极化贡献为：

<a id="eq:pol-efpfefp"></a>
$$
E^{\text{pol}}(P-L)=-\frac{1}{2}\sum_{k\in P,L}\mu^{k}F^{\text{mult},k}+\frac{1}{2}\sum_{k\in P}\mu^{k}F^{\text{mult},k}\;. \tag{11.94}
$$

第一项是配体诱导偶极（$\mu^{k}_{\text{efp}}(L)$）与所有碎片诱导偶极（$\mu^{k}_{\text{fefp}}(A_{i})$）收敛后得到的极化能。
因此整个体系被完全极化，所有碎片（A${}_{i}$ 或 L）相互极化直至达到自洽：

<a id="A3.S8.EGx110"></a>
$$
\displaystyle\mu^{k}_{\text{efp}}(L) \tag{11.95}
$$

式 ([11.94](#eq:pol-efpfefp)) 的第二项是蛋白质自身的极化；一旦诱导偶极
[式 ([11.95](#eq:pol-mu-fefp))] 收敛，就应减去该值。

LA 方案可用于执行 QM/fEFP 计算。在这种情况下，fEFP 必须包含一个大分子（碎片之间存在共价键）。该方案目前尚不能执行 QM/fEFP/EFP 计算，即无法让大分子与溶剂分子同时以 EFP 理论水平描述并构成 fEFP 环境。

除 HLA 和 CLA 方案外，**Q-Chem** 还提供了*含共轭盖层的分子碎片化*（molecular fragmentation with conjugated caps, MFCC）方法，[[1542]](../bib_references/bib.md#bib1608)

该方法避免了饱和碎片之间重叠的问题。
MFCC 流程由两部分组成：对配体与加盖残基（CLA 方案）之间相互作用求和，再减去合并盖层（$C^{i+1}C^{i-1}$）与配体之间相互作用的部分。[[568]](../bib_references/bib.md#bib578)
（这些即所谓的共轭盖层或“concaps”。[[537]](../bib_references/bib.md#bib551)）
实际使用 $N-1$ 个 concap 碎片来消除重叠效应。

<a id="eq:mfcc"></a>
$$
P=A_{1}C^{2}+\sum_{i=2}^{N-1}C^{i-1}A_{i}C^{i+1}+C^{N-1}A_{N}-\sum_{i}^{N-1}C^{i+1}C^{i-1} \tag{11.97}
$$

在该方案中，由盖层重叠产生的贡献直接相互抵消，EFP 参数无需任何修改，这与 HLA 或 CLA 流程不同。然而，需要生成的参数数量更大，即 $N$ 个加盖碎片和 $N-1$ 个 concaps。

MFCC 静电相互作用能等于每个加盖碎片（$C^{i-1}A_{i}C^{i+1}$）与配体之间的相互作用能之和，减去每个 concap（$C^{i-1}C^{i+1}$）与配体之间的相互作用能之和：

<a id="eq:mfcc-fefp-elec"></a>
$$
E^{\text{elec}}(P-L)=\sum_{i}^{N}{E^{\text{elec}}\left(C^{i-1}A_{i}C^{i+1}-L\right)}-\sum_{i}^{N-1}{E^{\text{elec}}\left(C^{i-1}C^{i+1}-L\right)} \tag{11.98}
$$

MFCC 的主要优点在于，在每个加盖残基或 concap 上获得的多极展开在 $E^{\text{elec}}(P-L)$ 计算中被完整保留。
在当前实现中，不包含极化贡献。MFCC 方案尚不能用于 QM/fEFP。
