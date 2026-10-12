---
title: "6.19.3 耦合簇价键（CCVB）"
---

## 6.19.3 耦合簇价键（Coupled Cluster Valence Bond, CCVB）

(July 4, 2026)

完美配对（Perfect Pairing, PP）方法需要改进的情形包括：含有多个强相关电子对、且这些电子对都局域在空间同一区域的分子，因此涉及显著的(pair)间相关以及(pair)内相关。对于某些这类体系，耦合簇价键（Coupled Cluster Valence Bond, CCVB）是一种合适的方法。[[1274]](../bib_references/bib.md#bib1328)
CCVB 旨在定性地描述共价键的断裂。在最基础的理论层面上，当一个分子体系解离为一组开壳层碎片时，其能量应当趋近于各碎片的限制开壳层 Hartree-Fock（ROHF）能量之和。CCVB 能够为一大类问题重现这一行为，同时保持正确的自旋对称性。与这一主要优势相伴的，是许多 GVB-CC 方法共有的空间对称性破缺问题。

与本章讨论的其他方法一样，CCVB 波函数的主要贡献来自完美配对波函数，其形式见式 ([6.84](subsec_PP.md#eqn:PP))。一个重要的区别在于，CCVB 将 PP 波函数作为参考态，正如其他 GVBMAN 方法使用参考行列式一样。

PP 波函数是简单强正交单重态 geminal（配对函数）的乘积。忽略归一化因子，这些 geminal 有两种等价的表达形式

<a id="A3.S8.EGx26"></a>

$$
\displaystyle(\phi_{i}\phi_{i}+t_{i}\phi_{i}^{*}\phi_{i}^{*})(\alpha\beta-\beta\alpha)\ \ \ (\text{Natural-orbital form}) \tag{6.85}
$$

其中左边是空间部分（涉及 $\phi$ 和 $\chi$ 轨道），右边是自旋耦合。VB 形式的轨道在同一个对（pair）内是非正交的，通常类似于原子轨道（AO）。CCVB 使用 VB 形式，而其他 GVBMAN 方法使用自然轨道（NO）形式。事实证明，占据的 UHF 轨道也可以旋转（而不影响能量）成为 VB 形式（此时自旋部分就只有 $\alpha\beta$），因此 CCVB 的轨道系数按照与 UHF 相同的方式进行存储（尽管在 CCVB 中并不为轨道指定单一自旋）。

这些 geminal 之间不相关，正如分子轨道在 HF 计算中不相关一样。因此，它们能够描述非耦合的、即相互独立的单键断裂过程，例如 C${}_{2}$H${}_{6}$ $\rightarrow$ 2 CH${}_{3}$，但无法描述耦合的多键断裂过程，例如 N${}_{2}$ 的解离。在后一体系中，三个键可以用三个单重态 geminal 来描述，但这一图像必须以某种方式转化为两个自旋四重态（spin-quartet）N 原子耦合为一个整体单重态——这正是解离极限处的情形。要在 GVB 框架内实现这一点，就必须对 geminal 引入关联。该关联中对键断裂至关重要的部分，可以通过将若干单重态 geminal 组成的簇（cluster）替换为三重态 geminal，并将这些三重态重新耦合为整体单重态来获得。一个三重态 geminal 只需相应地修改单重态 geminal 的自旋分量即可得到。由此我们得到 CCVB 波函数：

<a id="A3.S8.EGx27"></a>

$$
\displaystyle|\Psi\rangle \tag{6.86}
$$

在这一展开式中，求和遍历所有活化的单重态对（active singlet pairs），ket（狄拉克符号）标记中所示的指标对应于按上文所述方式被耦合的对。我们可以看到，该波函数耦合了由偶数个 geminal 组成的簇。此外还可以看到，包含超过 2 个 geminal 的簇的振幅是由 2 对簇的振幅来参数化的。这一近似对于计算可行性很重要，但它实际上只是整个 CCVB 方法族中的一个：完全可以纳入由奇数对组成的耦合簇，也可以为高阶振幅引入独立的参数。目前，**Q-Chem** 中只包含了最简单的这一级别。

试图描述与 CCVB 本质相同的电子关联效应的较早方法有 IP[[1387]](../bib_references/bib.md#bib1449)
 和
RCC[[1390]](../bib_references/bib.md#bib1452)
 波函数。一般而言应优先使用 CCVB。事实上 CCVB 与 GVB-IP 模型存在关联。具体来说，如果将 CCVB 波函数相对于一组行列式展开，我们会发现对于每一对单重态对，CCVB 只包含两个相关 GVB-IP 双激发振幅中的一个。因此，CCVB 的各项计算需求和耗时与 GVB-IP 非常相似。两种模型的主要区别在于如何利用双激发振幅去参数化四体（quadruples）、六体（sextuples）等更高阶项，而这正是 CCVB 能够在全键解离处给出正确能量的原因。

通过设置 CORRELATION = CCVB 即可调用 CCVB 计算。活化的单重态 geminal 数目必须通过 GVB_N_PAIRS 指定。此后需要选择一个初始猜测。对此有三个主要选项，由以下关键字指定

### `CCVB_GUESS`

> **指定 CCVB 计算的初始猜测**
>
> * **类型**: `INTEGER`
> * **默认值**: `NONE`
> * **可选值**:
>     * `1`: 标准 GVBMAN 猜测（通过 GVB_LOCAL + Sano 过程进行轨道定域化）。
>     * `2`: 使用先前 GVBMAN 计算的轨道，需配合 SCF_GUESS = READ。
>     * `3`: 将 UHF 轨道转换为配对 VB 形式。
> * **建议**: 选项 1 总体最实用。GVBMAN 方法的成功往往依赖于定域化轨道，此猜测正是瞄准这一点。选项 2 适用于将结果与其他 GVBMAN 方法对比，或者当其他 GVBMAN 方法能更高效地获得期望结果时使用。选项 3 在键断裂情形下、且已找到相关的 UHF 解时很有用。它对小型体系效果最好，或者当自旋非限制化（unrestriction）只是较大分子中的局域现象时。如果非限制化是非局域的且体系较大，此猜测得到的解往往不是全局极小值。任何 UHF 解都有一定数目的非限制化对（pair），程序会输出该数目。如果 GVB_N_PAIRS 超过这个数目，将使用标准 GVBMAN 初始猜测过程为超出的那些对构造猜测。

对于势能面（potential energy surfaces），建议从前一次计算得到的 CCVB 解出发进行重启。这通过 GVB_RESTART = TRUE 来调用。每当使用此选项，或任何时候将其他计算的轨道直接读入 CCVB 时，都务必同时设置：

- •

SCF_GUESS = READ
- •

MP2_RESTART_NO_SCF = TRUE
- •

SCF_ALGORITHM = DIIS

这就绕过了 **Q-Chem** 中其他位置使用的正交化方案，这些方案很可能会打乱 CCVB 的猜测。

除了上文讨论的原生（parent）CCVB 方法之外，我们还纳入了两种相关的能量优化方案，其运行由以下关键字控制：

### `CCVB_METHOD`

> **可选地修改基本 CCVB 方法**
>
> * **类型**: `INTEGER`
> * **默认值**: `1`
> * **可选值**:
>     * `1`: 标准 CCVB 模型
>     * `3`: CCVB 的独立电子对近似（Independent Electron Pair Approximation, IEPA）
>     * `4`: 变分 PP（即 CCVB 的参考能量）
> * **建议**: 通常推荐使用选项 1。选项 4 适用于预条件处理（preconditioning），以及获得定域化轨道解，后者可用于后续计算。当常规 GVBMAN PP 代码出现变分不稳定时，选项 4 也很有用。选项 3 是 CCVB 的一种简单独立振幅近似。它避免了 CCVB 的三次方标度（cubic-scaling）振幅方程，并且能够为任意分子体系达到正确的解离能（而常规 CCVB 仅在 UHF 能够达到正确解离极限的情形下才能做到）。不过，CCVB 的 IEPA 近似有时会出现变分不稳定，而我们在常规 CCVB 中尚未观察到这种现象。

???+ example "示例 6.52：处于中间解离区域的 N ${}_{2}$ 分子。在本例中，必须使用 SCF_ALGORITHM DIIS 才能获得未破缺对称性的 RHF
解，而该解本身又是获得正确 CCVB 解所必需的。注意，许多 GVBMAN 通用关键字同样用于 CCVB。"
    ```qchem
    $molecule
       0 1
       N  0  0  0
       N  0  0  2.0
    $end
    
    $rem
       UNRESTRICTED       = false
       BASIS              = 6-31g*
       EXCHANGE           = hf
       CORRELATION        = ccvb
       GVB_N_PAIRS        = 3
       CCVB_METHOD        = 1
       CCVB_GUESS         = 1
       GVB_LOCAL          = 2
       GVB_ORB_MAX_ITER   = 100000
       GVB_ORB_CONV       = 7
       GVB_RESTART        = false
       SCF_CONVERGENCE    = 10
       THRESH             = 14
       SCF_GUESS          = sad
       MP2_RESTART_NO_SCF = false
       SCF_ALGORITHM      = diis
       MAX_SCF_CYCLES     = 2000
       PRINT_ORBITALS     = true
       INTEGRAL_SYMMETRY    = false
       POINT_GROUP_SYMMETRY = false
    $end
    ```
