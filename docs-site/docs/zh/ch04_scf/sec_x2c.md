---
title: "4.9.6 相对论效应"
---

## 4.9.6 相对论效应

（2026 年 7 月 4 日）

相对论效应在若干物理与化学现象中扮演着重要角色，例如重元素的性质，以及在 X 射线谱学实验中所探测的最内层能级的正确描述。求解描述电子及其反粒子（正电子）的四分量 Dirac 方程计算代价高昂。由于大多数化学过程仅考虑电子波函数即可得到解释，人们提出了多种方法来有效解耦电子与正电子的自由度。

单电子精确二分量（exact two-component, X2C）哈密顿量为实现这种解耦提供了一条途径。[[610]](../bib_references/bib.md#bib633)

该方法依赖于以受限动量平衡（restricted kinetic balance, RKB）形式[[744]](../bib_references/bib.md#bib777)求解更易处理的单电子四分量 Dirac 哈密顿量，从而获得解耦幺正变换，用于修正单电子矩阵元（如动能与核吸引项），以计入相对论效应。X2C 变换矩阵的一个关键组成部分是计算

<a id="Ch4.E75"></a>
$$
W_{{\rm SF},\mu\nu}=\langle\phi_{\mu}|\vec{p}\cdot\left(V\vec{p}\right)|\phi_{\nu}\rangle \tag{4.75}
$$

其中 $W_{{\rm SF},\mu\nu}$ 是完整 Dirac 哈密顿量小分量（small-component）的矩阵元，仅计算标量相对论部分。这一计算的实现基于这样一个事实：动量算符是平移的生成元，其对基函数的作用可以通过对这些函数取适当导数来捕获。需要指出的是，为了通过 X2C 正确捕获小分量对电子波函数的影响，**必须使用全电子去收缩（decontracted）基组**。自 **Q-Chem** 7.0 版本发布以来，$W_{{\rm SF},\mu\nu}$ 的解析实现也已用于 SF-1eX2C，并被设为新的默认值。有限差分 X2C 算法的完整细节见文献 [[292]](../bib_references/bib.md#bib296)。关于如何加入标量相对论效应以模拟 K 边 X 射线谱学的示例可见第 [7.12.4](../ch07_excited/ex_COCOREIP.md) 节。

REL_X2C

### `REL_X2C`

> **启用 X2C 标量相对论计算**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值**:
>     * 0
>     * 执行常规的非相对论 SCF 计算
>     * 1
>     * 执行标量相对论 X2C 计算
> * **建议**: 若希望进行标量相对论 X2C 计算，则设为 1。

REL_X2C_FD

### `REL_X2C_FD`

> **使用基于有限差分的 W 矩阵元执行 X2C 计算**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值**:
>     * 0
>     * 以解析实现构建 W 矩阵
>     * 1
>     * 以有限差分实现构建 W 矩阵
> * **建议**: 在非测试用途下使用解析实现。截至 Q-Chem 7.0 版本，解析表达式仅对 SF-1eX2C 实现了支持。

REL_X2C_FD_DISPLACEMENT

### `REL_X2C_FD_DISPLACEMENT`

> **控制计算 W 时使用的有限差分步长**
>
> * **类型**: `INTEGER`
> * **默认值**: `100`
> * **取值**:
>     * $n$
>     * 将有限差分步长设置为
>     * $n\times 10^{-6}$
> * **建议**: 无

## 4.9.6.1 单电子自旋–轨道耦合

原则上，可以求得 1eX2C 哈密顿量的完整解，其中也将包含自旋–轨道耦合（spin-orbit coupling, SOC）项。然而，这需要自旋广义化的复数解。这一点可以从获得完整 $W$ 矩阵所需的附加矩阵 $W_{\text{SOC},\mu\ nu}$ 看出：

<a id="Ch4.E76"></a>
$$
W_{{\rm SOC},\mu\nu}=i\sigma\cdot\langle\phi_{\mu}|\vec{p}\times\left(V\vec{p}\right)|\phi_{\nu}\rangle \tag{4.76}
$$

该矩阵取复数值，并且需要对不同的 Pauli 矩阵做叉乘，从而导致自旋广义化的解。因此，只有在 cGHF 例程中调用 REL_X2C = 1 时才能计入 SOC 效应——其他计算（例如 RHF、UHF、ROHF）都将退化为 SF-1eX2C，不会包含 SOC 效应。在 cGHF 类中将 rem 变量 REL_X2C = 1 设置后，会自动计算 $W_{{\rm SOC},\mu\nu}$，除非同时将 REL_SF_X2C_CGHF 也设为 1。

REL_SF_X2C_CGHF

### `REL_SF_X2C_CGHF`

> **在 cGHF 例程中启用 X2C 标量相对论计算。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值**:
>     * 0
>     * 执行包含 SOC 效应的完整相对论 X2C 计算
>     * 1
>     * 执行标量相对论 X2C 计算
> * **建议**: 若希望在 cGHF 类中进行标量相对论 X2C 计算，则设为 1。必须与 REL_X2C = 1 配合使用。否则将执行不含 X2C 的非相对论计算，此 rem 变量会被忽略。

## 4.9.6.2 用于双电子 SOC 的屏蔽核自旋–轨道耦合

尽管原则上可以计算 X2C 中的双电子 SOC 项，但相关矩阵元往往极其复杂且难以求值。作为替代，在 X2C 框架下近似双电子 SOC 效应的一种流行做法是对完整 1eX2C 哈密顿量中依赖于自旋–轨道的项进行经验缩放。这一类方法称为屏蔽核自旋–轨道（screened-nuclear spin-orbit, SNSO）方法，最早由 Boettger 提出[[141]](../bib_references/bib.md#bib131)。此后，人们提出了改进的系数形式，以适配 $p$ 壳层高斯型轨道（Gaussian-Type-Orbitals, GTOs）的弥散/紧致程度，以及占据与虚拟分子轨道（MO）[[389]](../bib_references/bib.md#bib397)。特别地，还基于完整四分量 Dirac-Coulomb-Breit（DCB）哈密顿量的轨道分裂结果，对原始 SNSO 系数给出了新的参数化。[[362]](../bib_references/bib.md#bib367)

REL_SNSO

### `REL_SNSO`

> **在 cGHF 例程中启用 1eX2C-SNSO 计算。**
>
> * **类型**: `INTEGER`
> * **默认值**: `0`
> * **取值**:
>     * 0
>     * 使用未经调整的 SOC 哈密顿量执行完整相对论 X2C 计算
>     * 1
>     * 使用经原始 Boettger 系数调整的 SOC 哈密顿量执行完整相对论 X2C 计算
>     * 2
>     * 使用经 Yoshizawa 及其合作者修正的 SNSO 系数调整的 SOC 哈密顿量执行完整相对论 X2C 计算
>     * 3
>     * 使用来自 Ehrman 及其合作者的 DC-SNSO 系数调整的 SOC 哈密顿量执行完整相对论 X2C 计算
>     * 4
>     * 使用来自 Ehrman 及其合作者的通用 DCB-SNSO 系数调整的 SOC 哈密顿量执行完整相对论 X2C 计算
>     * 5
>     * 使用来自 Ehrman 及其合作者的行依赖（row-dependent）DCB-SNSO 系数调整的 SOC 哈密顿量执行完整相对论 X2C 计算
> * **建议**: 在大多数一般情形下设 1 即可。通用 DCB-SNSO 系数是 SNSO 方法族中最新的贡献，据报道能够给出准确的 $L_{2,3}$ 边的二重态分裂。
