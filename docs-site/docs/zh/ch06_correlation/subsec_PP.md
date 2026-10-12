---
title: "6.19.2 完美配对（Perfect Pairing, PP）"
---

## 6.19.2 完美配对（Perfect Pairing, PP）

（2026 年 7 月 4 日）

更具体地说，耦合簇完美配对（PP）波函数写作

<a id="eqn:PP"></a>

$$
\left|\Psi\right\rangle=\exp\left({\sum_{i=1}^{n_{\mathrm{active}}}{t_{i}\hat{a}_{i\ast}^{{\dagger}}\hat{a}_{\bar{i}\ast}^{{\dagger}}\hat{a}_{\bar{i}}\hat{a}_{i}}}\right)\left|\Phi\right\rangle \tag{6.84}
$$

其中 $n_{\mathrm{active}}$ 是活性电子数，$t_{i}$ 为线性数目的未知簇振幅（cluster amplitudes），对应于将第 $i$ 个电子对中的两个电子从其成键轨道对激发到反键轨道对。除 $t_{i}$ 之外，核心轨道和活性轨道同样会被优化以最小化 PP 能量。所使用的算法是对梯度下降法（Gradient Descent Method, GDM）的略微改进，该方法在[第 4.5.7 节](../ch04_scf/sect_gdm.md)中针对自洽场（SCF）计算进行了描述。尽管 PP 波函数形式简洁，仅包含线性数目的关联振幅，它仍然是探索强关联体系时有用的理论模型化学（model chemistry）。这是因为对于 PP 活性空间中的单个电子对，它是精确的；对于该活性空间中一组无相互作用的电子对，它同样是精确的。毕竟，从某种意义上说，分子正是由一组相互作用的电子对构成的！在实际应用中，PP 对分子可恢复其活性空间中 60% 到 80% 的关联能。

若计算为完美配对（CORRELATION = PP），则除了限制解之外，还可以寻找非限制解。对于电子数为奇数的分子，默认使用非限制轨道，但电子数为偶数的分子也可以指定使用非限制轨道。这通过设置 GVB_UNRESTRICTED = TRUE 来实现。然而，若给定限制初始猜测，通常仍会收敛到限制解，因此需要额外指定 REM 变量以确保初始猜测具有破缺的自旋对称性。这可以通过使用非限制 SCF 解作为初始猜测来实现，相关技术见[第 4 章](../ch04_scf/chap_scf.md)。或者，也可以在计算开始之前，使用下面描述的 GVB_GUESS_MIX 显式地对一组限制猜测轨道进行对称性破缺。此外还有活性对内非限制（Unrestricted-in-Active Pairs, UAP）的实现[[774]](../bib_references/bib.md#bib807)，这是 GVB 方法的默认非限制实现。该方法通过仅优化一组 ROHF 分子轨道系数以及每个占据-虚轨道对的单一旋转角来简化非限制化过程。这些角度用于构造一系列 $2\times 2$ 的 Givens 旋转矩阵，将其应用于 ROHF 系数以确定 $\alpha$ 自旋分子轨道系数，而其转置则应用于 ROHF 系数以确定 $\beta$ 自旋分子轨道系数。该算法速度快，并消除了非限制 GVB 方法在解离极限附近的许多病态行为。为了生成完整的势能曲线，我们发现最好的做法是从所需的 UHF 解离解出发作为 GVB 的猜测，然后向平衡键长方向追踪。

### `GVB_UNRESTRICTED`

> **控制 PP 计算使用限制还是非限制模式。通常自动处理。**
>
> * **类型**：`LOGICAL`
> * **默认值**：`与 UNRESTRICTED 取值相同`
> * **选项**：
>     * TRUE/FALSE
> * **建议**：仅在需要从 RHF 或 ROHF 初始猜测执行 UPP 计算时才显式设置此变量。若要保持默认并使用新的活性对内非限制 GVB 代码（该代码在与 GVB_DO_ROHF 配合使用时可返回 RHF 或 ROHF 解），则无需设置此变量，只需指定 UNRESTRICTED = TRUE。

### `GVB_DO_ROHF`

> **设置活性对内非限制（Unrestricted-in-Active Pairs）中保持限制状态的数目。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * 用户自定义
> * **建议**：若 $n$ 的值与 GVB_N_PAIRS 相同，则返回 GVB 的 ROHF 解。仅适用于 UNRESTRICTED = TRUE 的 GVB 实现且 GVB_OLD_UPP = 0（其默认值）。

### `GVB_OLD_UPP`

> **GVB 使用哪种非限制算法。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * 0
>     * 使用文献
>     * 774
>     * Lawler K. V., Small D. W., Head-Gordon M.
>     * J. Phys. Chem. A
>     * (2010)
>     * ,
>     * 114
>     * ,
>     * pp. 2930
>     * .
>     * 链接
>     * 中描述的活性对内非限制（Unrestricted-in-Active Pairs）方法
>     * 1
>     * 使用文献
>     * 110
>     * Beran G. J. O. et al.
>     * J. Phys. Chem. A
>     * (2005)
>     * ,
>     * 109
>     * ,
>     * pp. 9183
>     * .
>     * 链接
>     * 中描述的非限制实现
> * **建议**：仅适用于非限制 PP，不适用于其他 GVB 模型。

### `GVB_GUESS_MIX`

> **与 SCF_GUESS_MIX 类似，通过按用户定义的 LUMO 混入 HOMO 的比例来混合 $\alpha$ 的 HOMO 和 LUMO 轨道，从而对 UPP 进行 $\alpha/\beta$ 对称性破缺。设置为 100 对应于混合轨道中 HOMO 和 LUMO 的 1:1 比例。**
>
> * **类型**：`INTEGER`
> * **默认值**：`0`
> * **选项**：
>     * $n$
>     * 用户自定义，
>     * $0\leq n\leq 100$
> * **建议**：设置为 25 通常能在不过度阻碍收敛的情况下有效破缺对称性。

虽然本节中的所有描述均涉及通过投影法求解 PP，但如[第 6.19.3 节](subsec_CCVB.md)所述，也可以变分地求解 PP 能量。这种变分 PP 解是 CCVB 方法的参考波函数。在大多数情况下，使用自旋纯（spin-pure）CCVB 比试图通过允许轨道自旋极化来改进限制 PP 更为可取。
