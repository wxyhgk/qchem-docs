---
title: "5.11.5 约束密度泛函理论组态相互作用（CDFT-CI）"
---

## 5.11.5 约束密度泛函理论组态相互作用（Configuration Interaction with Constrained DFT, CDFT-CI）

（2026 年 7 月 4 日）

在某些情况下，基于单一组态的密度泛函理论（Density Functional Theory, DFT）计算无法很好地描述体系。例如，众所周知，大多数泛函对过渡态的描述较差，计算得到的势垒偏低。特别是，我们可以将双原子物种的均裂解离视为静态关联（static correlation）变得极其重要的情形。现有的 DFT 泛函在捕获动态关联（dynamic correlation）方面已被证明非常有效，但在存在强静态关联时常常表现出困难。组态相互作用（Configuration Interaction, CI）是波函数方法中广为人知的多参考（multireference）方法，非常适合捕获静态关联；CDFT-CI 技术允许在 DFT 计算之上进行 CI 计算，从而同时利用静态关联和动态关联方法。

约束 DFT（Constrained DFT, CDFT）用于计算两个或多个类非绝热（diabatic-like）态的密度（以及 Kohn-Sham 波函数）；随后利用这些态构建 CI 矩阵。对该矩阵进行对角化即可在组态空间内得到基态*以及*激发态的能量。程序会打印初始非绝热态的系数，以显示所得态的特征。

由于 DFT 只给出收敛的密度而非真正的波函数，计算非对角耦合元 $H_{12}$ 并非完全直截了当，因为 Kohn-Sham 波函数的物理含义并不十分明确。不过，我们可以进行如下推导:[[1502]](../bib_references/bib.md#bib1560)

<a id="A3.S8.EGx20"></a>

$$
\displaystyle\begin{aligned} \displaystyle H_{12}&\displaystyle=\frac{1}{2}\Bigl{[}\langle 1|H+V_{C_{1}}\omega_{C_{1}}-V_{C1}\omega_{C_{1}}|2\rangle+\langle 1|H+V_{C_{2}}\omega_{C_{2}}-V_{C_{2}}\omega_{C_{2}}|2\rangle\Bigr{]}\\
&\displaystyle=\frac{1}{2}\Bigl{[}\left(E_{1}+V_{C_{1}}N_{C_{1}}+E_{2}+V_{C_{2}}N_{C_{2}}\right)\langle 1|2\rangle-V_{C_{1}}\langle 1|\omega_{C_{1}}|2\rangle-V_{C_{2}}\langle 1|\omega_{C_{2}}|2\rangle\Bigr{]}\end{aligned} \tag{5.74}
$$

其中收敛态 $|i\rangle$ 被假定为 $H+V_{C_{i}}\omega_{C_{i}}$ 的基态，其本征值为 $E_{i}+V_{C_{i}}N_{C_{i}}$）。这一推导消除了表达式中的双电子积分，并且经验表明，使用 Kohn-Sham 轨道的 Slater 行列式来近似量 $\langle 1|2\rangle$ 和 $\langle 1|\omega_{C_{i}}|2\rangle$ 是合理的。

请注意，由于这些约束态是不同的哈密顿量（由于不同的约束势）的本征函数，它们*不是*正交态，因此我们必须将 CI 矩阵构造成广义本征值问题。默认使用对称正交化，不过在较高的打印级别下，非正交基下的重叠矩阵和哈密顿矩阵也会被打印出来，以便事后使用其他正交化方案。在少数情况下，可以为 CDFT-CI 哈密顿量找到一组正交基，从而可以为正交态赋予物理诠释。在这类情形中，程序会对 Becke 权重算符的矩阵表示进行对角化，所得的（正交）本征态可以被表征描述。[[1497]](../bib_references/bib.md#bib1561)
 在提高的打印级别下，该矩阵以“CDFT-CI Population Matrix”（CDFT-CI 粒子数矩阵）的形式打印。

为了执行 CDFT-CI 计算，必须定义 $N$ 个相互作用的态，这可以通过使用 *$cdft* 输入段来完成，其方式与 CDFT 态的指定类似：

> ```qchem
> $cdft
> STATE_1_CONSTRAINT_VALUE_X
> COEFFICIENT1_X       FIRST_ATOM1_X       LAST_ATOM1_X    TYPE1_X
> COEFFICIENT2_X       FIRST_ATOM2_X       LAST_ATOM2_X    TYPE2_X
> ...
> STATE_1_CONSTRAINT_VALUE_Y
> COEFFICIENT1_Y       FIRST_ATOM1_Y       LAST_ATOM1_Y    TYPE1_Y
> COEFFICIENT2_Y       FIRST_ATOM2_Y       LAST_ATOM2_Y    TYPE2_Y
> ...
> ---
> STATE_2_CONSTRAINT_VALUE_X
> COEFFICIENT1_X       FIRST_ATOM1_X       LAST_ATOM1_X    TYPE1_X
> COEFFICIENT2_X       FIRST_ATOM2_X       LAST_ATOM2_X    TYPE2_X
> ...
> STATE_2_CONSTRAINT_VALUE_Y
> COEFFICIENT1_Y       FIRST_ATOM1_Y       LAST_ATOM1_Y    TYPE1_Y
> COEFFICIENT2_Y       FIRST_ATOM2_Y       LAST_ATOM2_Y    TYPE2_Y
> ...
> $end
> ```

每个态由 CONSTRAINT_VALUE 以及相应权值指定，这些权值作用于若干原子集合，其平均值应等于约束值。不同的态之间用一行包含三个或更多短划线字符（dash）的线分隔。

如果希望将某个无约束态作为相互作用组态之一，可以对原子范围 0 到 0 施加电荷和自旋约束，其值为零。

!!! note "注意"
    出于下文所述的原因，必须为每一个电荷约束指定相应的自旋约束（并且它在输入文件中必须紧跟在该电荷约束之后）。


除了输入文件中的 *$cdft* 输入段之外，CDFT-CI 计算还必须将 CDFTCI 标志设为 TRUE 才能运行。但请注意，CDFT 标志是由 CDFT-CI 在内部使用的，*不应*在输入文件中设置。变量 CDFTCI_PRINT 也可手动设置以控制输出级别。默认值为 0，将打印 $N$ 个 CDFT-CI 态的能量和权重（在非绝热基下）。将其设为 1 或更高还会打印 CDFT-CI 重叠矩阵、基变换之前的 CDFT-CI 哈密顿矩阵以及 CDFT-CI 粒子数矩阵。将其设为 2 或更高还会打印 CDFT-CI 粒子数矩阵的本征向量和本征值。将其设为 3 会产生更多输出，仅在对程序进行调试时才有用。

为方便起见，如果输入文件中未设置 CDFTCI_PRINT，它将被设置为 SCF_PRINT 的值。

如上一节所述，我们对电荷的化学直觉与实际的量子力学电荷之间存在差异。此前给出的例子是 LiF，根据直觉锂原子的形式电荷为 $+1$；类似地，我们可能会设想对 $\text{H}_{2}$ 进行 CDFT-CI 计算，包含两个离子态和两个自旋约束态。然而，这相当于试图将 $\text{H}_{2}$ 的两个电子都强行压到同一个原子核上，而这样的计算是无法收敛的（因为由于 Becke 权重算符的本质，在中等核间距下总会有部分非零密度的份额被分配到另一个原子上）。为解决此类问题，我们采用了一种机制，将化学直觉中的形式电荷转换为合理的量子力学电荷约束。我们使用“预分子”（promolecule）密度的形式体系，即将分子按（约束算符的划分方式）分割为若干片段，并对这些彼此完全隔离的片段分别进行 DFT 计算。[[1497]](../bib_references/bib.md#bib1561)
（正是这一步骤要求同时提供自旋和电荷约束，以便为每个片段做出正确的电子划分。）随后将所得的、各分离片段已收敛的预分子密度相加，并将各权重算符作用于这一新密度所得的值，作为实际 CDFT 计算中对相互作用态的约束。预分子密度方法补偿了附近原子对将被约束的实际密度的影响。

关于 CDFT 计算自洽场（SCF）收敛的评述同样适用于 CDFT-CI 所使用的计算，此外还需注意：如果 SCF 收敛但 CDFT 未收敛，则可能需要使用更稠密的积分网格或降低 CDFT_THRESH 的值。

解析梯度不可用。许多与 CDFT 相关的 *$rem* 变量同样适用于 CDFT-CI 计算。有关使用 CDFT-CI 计算反应势垒高度的详情，参见文献 [[1498]](../bib_references/bib.md#bib1562)
。
