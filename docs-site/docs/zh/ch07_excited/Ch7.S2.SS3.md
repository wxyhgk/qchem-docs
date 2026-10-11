---
title: "7.2.3 具有扩展激发流形的 CIS 方法"
---

## 7.2.3 具有扩展激发流形的 CIS 方法

（2026 年 7 月 4 日）

人们提出了多种类 CIS（CIS-like）方法，它们在 CIS 激发空间中加入了有限数量的双激发，
以便在克服 CIS 某些固有缺陷的同时，避免像 CISD 或 CCSD 这类包含全部双激发的方法所带来的高昂的
${\cal{O}}({N^{6}})$ 计算成本。本节将讨论这些"扩展"的 CIS 方法，首先从 Maurice 和 Head-Gordon 提出的原始扩展 CIS（XCIS）方法[[920]](../bib_references/bib.md#bib956)开始。

## 7.2.3.1 扩展 CIS（XCIS）

XCIS 的动机源于这样一个事实：ROCIS 和 UCIS 对自由基的效果不如 CIS 对闭壳层分子的效果。
利用 attaching/detaching density（附着/剥离密度）分析程序[[538]](../bib_references/bib.md#bib555)，
ROCIS 和 UCIS 方法在硝基甲基自由基（nitromethyl radical）上的失效被追溯到对某一类双替换的忽略，该类双替换涉及同时将一个 $\alpha$ 自旋电子从单占据轨道激发出去，以及将一个 $\beta$ 自旋电子激发进入单占据轨道。
自旋适配的组态

<a id="eq611"></a>

$$
\left|{\tilde{\Psi}_{i}^{a}(1)}\right\rangle=\frac{1}{\sqrt{6}}\left(|\Psi_{\bar{i}}^{\bar{a}}\rangle-|\Psi_{i}^{a}\rangle\right)+\frac{2}{\sqrt{6}}|\Psi_{p\bar{i}}^{a\bar{p}}\rangle \tag{7.12}
$$

具有至关重要的意义。（这里，$a,b,c,\ldots$ 表示虚轨道；$i,j,k,\ldots$ 表示占据轨道；$p,q,r,\ldots$ 表示单占据轨道。）
类似地，其他受关注的自由基中类似的激发很可能也非常重要。

XCIS 方案是 CIS 向开壳层分子更令人满意的一种推广，其做法是同时纳入一类受限的双替换，
这些双替换与式 ([7.12](#eq611)) 中的类似。为说明这一点，考虑限制开壳层 Hartree-Fock（ROHF）计算所得的轨道空间：
双占据（$d$）、单占据（$s$）和虚轨道（$v$）。以此为出发点，我们可以区分三类与基态具有相同多重度的单激发：
$d\rightarrow s$、$s\rightarrow v$ 和 $d\rightarrow v$。于是，自旋适配的 ROCIS 波函数为

<a id="eq612"></a>

$$
\left|{\Psi_{\mathrm{ROCIS}}}\right\rangle=\frac{1}{\sqrt{2}}\sum_{ia}^{dv}a_{i}^{a}\left(|\Psi_{i}^{a}\rangle+|\Psi_{\bar{i}}^{\bar{a}}\rangle\right)+\sum_{pa}^{sv}a_{p}^{a}|\Psi_{p}^{a}\rangle+\sum_{ip}^{ds}a_{\bar{i}}^{\bar{p}}|\Psi_{\bar{i}}^{\bar{p}}\rangle \tag{7.13}
$$

将 CIS 理论扩展到纳入更高阶激发时，仍以 ROHF 作为基态参考，并在 ROCIS 波函数中加入与式 ([7.13](#eq612)) 类似的项，
以及那些双激发在 $\alpha$ 和 $\beta$ 空间中经由不同轨道发生的项：

<a id="eq613"></a>

$$
\begin{array}[]{r}\left|{\Psi_{\mathrm{XCIS}}}\right\rangle=\frac{1}{\sqrt{2}}{\displaystyle\sum_{ia}^{dv}}a_{i}^{a}\left(|\Psi_{i}^{a}\rangle+|\Psi_{\bar{i}}^{\bar{a}}\rangle\right)+{\displaystyle\sum_{pa}^{sv}}a_{p}^{a}|\Psi_{p}^{a}\rangle+{\displaystyle\sum_{ip}^{ds}}a_{\bar{i}}^{\bar{p}}|\Psi_{\bar{i}}^{\bar{p}}\rangle\\
+{\displaystyle\sum_{iap}^{dvs}}\tilde{a}_{i}^{a}(p)|\tilde{\Psi}_{i}^{a}(p)\rangle+{\displaystyle\sum_{ia,p\neq q}^{dv,ss}}a_{p\bar{i}}^{a\bar{q}}|\Psi_{p\bar{i}}^{a\bar{q}}\rangle\\
\end{array} \tag{7.14}
$$

XCIS 只能从限制开壳层 Hartree-Fock 基态参考来定义，因为在 UHF 波函数中难以唯一地定义单占据轨道。
此外，自旋翻转双激发所经由的 $\beta$ 空轨道，在轨道特征甚至对称性上都可能与半占据的 $\alpha$ 轨道不匹配。

对于具有闭壳层基态的分子，HF 基态和 CIS 激发态都通过对哈密顿量在 HF 参考态与单激发组态状态函数（configuration state functions）空间中进行对角化而得到。
XCIS 的情况则不同，因为它所纳入的那类受限双激发可能与基态发生混合并降低其能量。为避免这种混合，以保持基态能量的尺寸一致性（size consistency）。

由于在激发态中纳入了受限集合的双激发而基态中未纳入，人们可能会预期能回收一部分相关能，从而导致激发态能量异常偏低。
然而，XCIS 波函数中所包含的双激发占全部双激发总数的比例非常小，且这些引入的组态无法描述任意电子对的对相关（pair correlation）。
因此，XCIS 方法可以被视为一种忽略电子相关的方法。

XCIS 的计算成本大约比 CIS 和 ROCIS 高四倍，其对开壳层分子的精度通常与 CIS 方法对闭壳层分子的精度相当。
总体而言，它能与实验结果达到定性一致。XCIS 可从双重态（doublet）ROHF 基态处理出发，用于双重态和四重态（quartet）激发态，且仅适用于激发能的计算。

???+ example "示例 7.5: 对一个不饱和自由基——苯基自由基（phenyl radical）——进行 XCIS 激发态计算，
其中双替换对低能激发态有相当大的贡献。"
    ```qchem
    $comment
       C6H5 phenyl radical C2v symmetry MP2(full)/6-31G* = -230.7777459
    $end
    
    $molecule
       0  2
       c1
       x1  c1  1.0
       c2  c1  rc2  x1  90.0
       x2  c2  1.0  c1  90.0  x1    0.0
       c3  c1  rc3  x1  90.0  c2    tc3
       c4  c1  rc3  x1  90.0  c2   -tc3
       c5  c3  rc5  c1   ac5  x1  -90.0
       c6  c4  rc5  c1   ac5  x1   90.0
       h1  c2  rh1  x2  90.0  c1  180.0
       h2  c3  rh2  c1   ah2  x1   90.0
       h3  c4  rh2  c1   ah2  x1  -90.0
       h4  c5  rh4  c3   ah4  c1  180.0
       h5  c6  rh4  c4   ah4  c1  180.0
    
       rh1  =    1.08574
       rh2  =    1.08534
       rc2  =    2.67299
       rc3  =    1.35450
       rh4  =    1.08722
       rc5  =    1.37290
       tc3  =   62.85
       ah2  =  122.16
       ah4  =  119.52
       ac5  =  116.45
    $end
    
    $rem
       BASIS            =  6-31+G*
       EXCHANGE         =  hf
       MEM_STATIC       =  80
       INTSBUFFERSIZE   =  15000000
       SCF_CONVERGENCE  =  8
       CIS_N_ROOTS      =  5
       XCIS             =  true
    $end
    ```

## 7.2.3.2 自旋翻转扩展 CIS（SF-XCIS）

自旋翻转扩展 CIS（spin-flip extended CIS，SF-XCIS）[[202]](../bib_references/bib.md#bib199)
是自旋翻转单激发组态相互作用（SF-CIS）方法[[727]](../bib_references/bib.md#bib758)的自旋完备扩展。

该方法包含所有满足如下条件的组态：高自旋三重态（triplet）参考中至多一个虚能级被占据，且至多一个双占据能级变为空。

SF-XCIS 只能从限制开壳层 Hartree-Fock 三重态基态参考来定义。最终的 SF-XCIS 波函数对应自旋纯的 $M_{S}=0$（单重态或三重态）态。
由于对半占据参考轨道采用了完全平衡的处理方式，该方法非常适用于存在两个强相关电子的体系，例如单键解离、具有显著双基态（diradical）特征的体系，或研究具有显著双激发特征的激发态。

SF-XCIS 的计算成本随分子尺寸的标度方式与 CIS 本身相同，只是前置因子大 13 倍。

???+ example "示例 7.6: 对三亚甲基甲烷（trimethylenemethane，TMM）双自由基的基态和激发态进行 SF-XCIS 计算，
其中双替换对低能激发态有相当大的贡献。"
    ```qchem
    $molecule
       0 3
       C
       C 1 CC1
       C 1 CC2   2 A2
       C 1 CC2   2 A2    3 180.0
       H 2 C2H   1 C2CH  3 0.0
       H 2 C2H   1 C2CH  4 0.0
       H 3 C3Hu  1 C3CHu 2 0.0
       H 3 C3Hd  1 C3CHd 4 0.0
       H 4 C3Hu  1 C3CHu 2 0.0
       H 4 C3Hd  1 C3CHd 3 0.0
    
       CC1    = 1.35
       CC2    = 1.47
       C2H    = 1.083
       C3Hu   = 1.08
       C3Hd   = 1.08
       C2CH   = 121.2
       C3CHu  = 120.3
       C3CHd  = 121.3
       A2     = 121.0
    $end
    
    $rem
      UNRESTRICTED    = false   SF-XCIS runs from ROHF triplet reference
      EXCHANGE        = HF
      BASIS           = 6-31G*
      SCF_CONVERGENCE = 10
      SCF_ALGORITHM   = DM
      MAX_SCF_CYCLES  = 100
      SPIN_FLIP_XCIS  = true    Do SF-XCIS
      CIS_N_ROOTS     = 3
      CIS_SINGLETS    = true    Do singlets
      CIS_TRIPLETS    = true    Do triplets
    $end
    ```

## 7.2.3.3 自旋适配自旋翻转 CIS

自旋适配自旋翻转 CIS（spin-adapted spin-flip CIS，SA-SF-CIS）[[1549]](../bib_references/bib.md#bib1615)
是自旋翻转单激发组态相互作用（SF-CIS）方法[[727]](../bib_references/bib.md#bib758)的自旋完备扩展。
与 SF-XCIS 不同，SA-SF-CIS 仅包含消除常规 SF-CIS 方法中自旋污染所需的最小电子组态集合。
SA-SF-CIS 的目标态的自旋本征值比参考 ROHF 态小一个单位，*即*，若目标为单重态（$S=0$），则参考态应为三重态（$S=1$）；若目标为双重态（$S=1/2$），则参考态应为四重态（$S=3/2$）。
SA-SF-CIS 方法采用张量形式的运动方程（equation-of-motion）形式体系[[1185]](../bib_references/bib.md#bib1239)，
使得 SA-SF-CIS 中 CI 矢量的维数与常规 SF-CIS 完全相同[[1549]](../bib_references/bib.md#bib1615)。

可以为 SA-SF-CIS 加上 DFT 修正（*即*，SA-SF-TDDFT）；参见第 [7.3.4](sect_sftddft.md) 节。
与其他 SF-TDDFT 方法一样，BH&HLYP 泛函实际上已成为事实上的标准选择[[1550]](../bib_references/bib.md#bib1617)。
该泛函对许多基态问题也是一种足够的选择[[484]](../bib_references/bib.md#bib496)。

???+ example "示例 7.7: 对乙烯的单重态基态和激发态进行 SA-SF-DFT 计算。"
    ```qchem
    $molecule
    0 3
     C
     C    1    B1
     H    1    B2    2    A1
     H    1    B3    2    A2    3    D1
     H    2    B4    1    A3    3    D2
     H    2    B5    1    A4    3    D3
    
       B1       1.32808942
       B2       1.08687297
       B3       1.08687297
       B4       1.08687297
       B5       1.08687297
       A1     121.62604150
       A2     121.62604150
       A3     121.62604150
       A4     121.62604150
       D1     180.00000000
       D2     180.00000000
       D3     180.00000000
    $end
    ```
