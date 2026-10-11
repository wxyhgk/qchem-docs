---
title: "6.12.9 二次耦合簇 doubles（QCCD）"
---

## 6.12.9 二次耦合簇 doubles（QCCD）

（2026 年 7 月 4 日）

如上文各小节所讨论的，CCSD、QCISD 和 OD 方法中能量的非变分确定通常不是一个实际问题。
然而在某些情况下，这些方法的表现很差。其中一个例子是使用闭壳层轨道（closed shell orbitals）计算均裂键解离（homolytic bond dissociation）的势能曲线，此时在接近解离区域计算得到的能量会显著低于真实能量，从而给出具有非物理势垒的势能曲线（即从分离碎片形成分子时出现不合理的势垒）[[[1388]](../bib_references/bib.md#bib1450)。
由 Berkeley 的 Troy Van Voorhis 近期提出的二次耦合簇 doubles
（Quadratic Coupled Cluster Doubles, QCCD）方法[[[1389]](../bib_references/bib.md#bib1451)采用不同的能量泛函（energy functional），在此类问题案例中表现出更好的行为。具体而言，QCCD 能量泛函定义为

<a id="eq530"></a>

$$
E_{\mathrm{QCCD}}=\left\langle{\Phi_{0}\left({1+\hat{\Lambda}_{2}+\frac{1}{2}\hat{\Lambda}_{2}^{2}}\right)\left|{\hat{H}}\right|\exp\left({\hat{T}_{2}}\right)\Phi_{0}}\right\rangle_{C} \tag{6.77}
$$

其中 $\hat{T}_{2}$ 和 $\hat{\Lambda}_{2}$ 算符的振幅（amplitudes）均通过最小化 QCCD 能量泛函来确定。
此外，最优轨道（optimal orbitals）通过针对混合占据轨道与虚轨道的轨道旋转（orbital rotations）最小化 QCCD 能量泛函来确定。

为理解为何 QCCD 能量应当优于 OD 能量，我们首先以不同于之前的方式重写后者。
也就是说，我们可以写出一个 CCD 能量泛函，当它针对 $\hat{T}_{2}$ 和
$\hat{\Lambda}_{2}$ 算符最小化时，会重新得到前面定义的相同 CCD 方程。
该能量泛函为

<a id="eq531"></a>

$$
E_{\mathrm{CCD}}=\left\langle{\Phi_{0}\left({1+\hat{\Lambda}_{2}}\right)\left|{\hat{H}}\right|\exp\left({\hat{T}_{2}}\right)\Phi_{0}}\right\rangle_{C} \tag{6.78}
$$

针对 $\hat{\Lambda}_{2}$ 算符的最小化给出了前面介绍的 $\hat{T}_{2}$ 算符方程，并且，若这些方程得到满足，则显然我们在计算能量时无需知道
$\hat{\Lambda}_{2}$ 算符本身。

对比这两个能量泛函，即式 ([6.77](#eq530)) 和 ([6.78](#eq531))，我们可以看到
QCCD 泛函包含了 $\exp(\hat{\Lambda}_{2})$ 的麦克劳林展开（Maclaurin expansion）中直至二次的项，而传统的 CCD 泛函只包含线性项。因此在 QCCD 中，能量表达式里的左矢（bra）波函数和右矢（ket）波函数得到了比 CCD 中更对等的处理。
这使得 QCCD 更接近真正的变分处理[[[1388]](../bib_references/bib.md#bib1450)

在变分方法中左矢与右矢波函数被完全对等地处理，但 QCCD 无需承担变分方法那样的指数级计算代价。

实际上，对于涉及两个以上活性电子（active electrons）的过程（*即*，至少断裂一个双键，或者断裂两个空间上相邻的单键），QCCD 相对于任何传统的对关联（pair correlation）方法都有显著改进。
计算示例方面，我们参见原始论文[[[1389]](../bib_references/bib.md#bib1451)

以及描述完整实现的后续论文[[[177]](../bib_references/bib.md#bib172)。

我们需要注意，这些改进是以计算代价换来的。
虽然 QCCD 与 CCSD、QCISD 和 OD 一样，其形式化计算标度（scaling）随分子体系大小的六次方增长，但其前置系数（coefficient）要大得多。
因此，QCCD 计算默认先作为 OD 计算执行，直到部分收敛为止。**Q-Chem**
还包含某些组态相互作用（configuration interaction, CI）模型（CISD 和 CISDT）。由于尺寸一致性（size-consistency）问题，CI 方法劣于 CC 方法，不过这些模型可能对基准测试（benchmarking）和开发用途有帮助。
