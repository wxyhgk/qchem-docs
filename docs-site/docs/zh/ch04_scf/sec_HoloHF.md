---
title: "4.9.4 全纯 Hartree-Fock 理论"
---

## 4.9.4 全纯 Hartree-Fock 理论

（2026 年 7 月 4 日）

## 4.9.4.1 理论

若要在 NOCI（非正交组态相互作用，Non-Orthogonal Configuration Interaction，参见 [7.5 节](../ch07_excited/subsec_NOCI.md)）中使用多个自洽场（SCF）解，必须保证所有这些解在我们关心的所有几何构型下都存在，以防止 NOCI 能量出现不连续。然而人们早已熟知，对称性破缺的 SCF 解会在势能面上的某些点处消失，例如 H${}_{2}$ 中的 Coulson-Fischer 点。全纯 Hartree-Fock 方法提供了一种在所有几何构型下对解进行解析延拓的手段。[[584]](../bib_references/bib.md#bib607)

在全纯 Hartree-Fock 理论中，真实的 Hartree-Fock 方程被解析延拓到复平面，而*不*引入分子轨道系数的复共轭。随后，多个解被认定为全纯能量[[584]](../bib_references/bib.md#bib607)的驻点

<a id="eq:HoloHFEnergy"></a>
$$
\widetilde{E}=\frac{\langle\Psi^{*}|\hat{H}|\Psi\rangle}{\langle\Psi^{*}|\Psi\rangle}, \tag{4.70}
$$

其中 $\hat{H}$ 定义为常规的电子哈密顿量

<a id="eq:HoloHamiltonian1"></a>
$$
\hat{H}=V_{\text{nuc}}+\sum_{i}^{N_{\text{e}}}\hat{h}(i)+\sum_{i<j}^{N_{\text{e}}}\frac{1}{r_{ij}}. \tag{4.71}
$$

因此，全纯 Hartree-Fock 方程关于轨道系数是复解析的，满足柯西-黎曼（Cauchy-Riemann）条件，并且可以证明驻点的数目在所有几何构型下保持恒定。[[173]](../bib_references/bib.md#bib169)

真实的 Hartree-Fock 态仍然是全纯 Hartree-Fock 能量的驻点；而在真实解消失的地方，其对应的全纯解仍以复轨道系数的形式存在。[[175]](../bib_references/bib.md#bib168)

通过对常规 SCF 算法做少量修改，即可定位全纯 Hartree-Fock 驻点。[[175]](../bib_references/bib.md#bib168)
其中最重要的是，在式 ([4.70](#eq:HoloHFEnergy)) 中去掉波函数的复共轭之后，所需的复全纯密度矩阵 $\mathbf{P}$ 与 Fock 矩阵 $\mathbf{F}$ 变为复对称矩阵（*cf.* 厄米矩阵，Hermitian），满足 $P^{\mu\nu}=P^{\nu\mu}$ 和 $F_{\mu\nu}=F_{\nu\mu}$。
此外，由于归一化约束中同样必须去掉复共轭，分子轨道系数必须构成一组复正交集（*cf*. 酉，unitary），即

<a id="eq:HoloComplexOrth"></a>
$$
\sum_{\mu\nu}C^{\cdot\mu}_{i\cdot}S_{\mu\nu}C^{\nu\cdot}_{\cdot j}=\delta_{ij}, \tag{4.72}
$$

最后，全纯 Hartree-Fock 的轨道能量与总能量在一般情况下也会变为复数，因此在每个 SCF 循环中依据轨道能量来选取新的占据轨道是没有明确定义的。作为替代，可以采用最大重叠方法（Maximum Overlap Method）的复对称类比形式（参见 [4.5.14 节](topic_mom.md)）。

让真实解越过 Coulson-Fischer 点延拓进入复平面常常十分困难，因为它们在实轴上会与对称性纯（symmetry-pure）的解发生合并。然而，通过引入复参数 $\lambda$ 对电子-电子相互作用进行缩放，*即*引入哈密顿量

<a id="eq:HoloHamiltonian"></a>
$$
\hat{H}=V_{\text{nuc}}+\sum_{i}^{N_{\text{e}}}\hat{h}(i)+\lambda\sum_{i<j}^{N_{\text{e}}}\frac{1}{r_{ij}}, \tag{4.73}
$$

可以证明 Coulson-Fischer 点在实轴上构成*孤立*的例外点（exceptional points）。[[174]](../bib_references/bib.md#bib170)
因此，沿着一条合适的复 $\lambda$ 轨迹，可以将真实解从实轴上扰动开来，从而轻松地引导其越过 Coulson-Fischer 点，进入其复全纯区域。[[174]](../bib_references/bib.md#bib170)

随后，这些被扰动的解可以松弛回到实轴，从而确定 NOCI 所需的全纯 Hartree-Fock 态。

## 4.9.4.2 作业控制

在 **Q-Chem** 中，全纯 Hartree-Fock 方法实现在 **libnoci** 软件包内（参见 [7.5.2 节](../ch07_excited/subsec_LIBNOCI.md)），通过设置 USE_LIBNOCI = TRUE 来访问，其设计目标是为 NOCI 计算定位多个 SCF 解。

SCF_HOLOMORPHIC

### `SCF_HOLOMORPHIC`

> **启用全纯 Hartree-Fock 轨道。**
>
> * **类型**: `LOGICAL`
> * **默认值**: `FALSE`
> * **选项**:
>     * FALSE
>     * 关闭全纯 Hartree-Fock
>     * TRUE
>     * 开启全纯 Hartree-Fock。
> * **建议**: 若设为 TRUE，则始终使用全纯 Hartree-Fock 的复轨道系数。若设为 FALSE 但同时 COMPLEX = TRUE，则使用复厄米轨道。

SCF_EESCALE_MAG

### `SCF_EESCALE_MAG`

> **控制 $\lambda$ 电子-电子缩放的幅值大小。**
>
> * **类型**: `INTEGER`
> * **默认值**: `$10000$`
> * **选项**:
>     * $abcde$
>     * 对应于
>     * $a.bcde$
> * **建议**: 对于全纯 Hartree-Fock 轨道，仅使用输入值的幅值；而对于真实 Hartree-Fock 轨道，输入值的符号表示 $\lambda$ 的符号。

SCF_EESCALE_ARG

### `SCF_EESCALE_ARG`

> **控制复 $\lambda$ 电子-电子缩放的相位角。**
>
> * **类型**: `INTEGER`
> * **默认值**: `$00000$`
> * **选项**:
>     * $abcde$
>     * 对应于
>     * $a.bcde$
> * **建议**: 通常设置为复相位角 $00500$（即 $0.0500$）就足以安全地将某个解引导越过 Coulson-Fischer 点，并转入其对应的复全纯解。
