---
title: "6.12.8 优化轨道耦合簇双激发（OD）"
---

## 6.12.8 优化轨道耦合簇双激发（OD）

（2026 年 7 月 4 日）

通过省略单替换（single substitutions）（*即*，将 $T_{1}$ 算符置为零），可以极大地简化 CCSD 方程。如果仍使用相同的单行列式参考态（具体为 Hartree-Fock 行列式），则由此定义了耦合簇双激发（coupled-cluster doubles, CCD）方法，其由下列方程给出：

<a id="eq527"></a>
$$
\displaystyle E_{\text{CCD}} \tag{6.75a}
$$

CCD 方法本身通常不被推荐，因为虽然所有的对关联（pair correlations）都被正确包含，但对单替换的忽略使得计算得到的能量和性质明显不如 CCSD 可靠。单替换所起的作用与轨道优化极为相似：它们实际上改变了参考行列式，使其更适合用于描述电子关联（而 Hartree-Fock 行列式是在不考虑电子关联的条件下优化得到的）。

由此提出了一种 CCSD 和 QCISD 的替代方法，并且它具有若干额外的优势。这就是优化轨道 CCD 方法（optimized orbital CCD, OO-CCD），我们通常简称为优化双激发（optimized doubles, OD）。[[1251]](../bib_references/bib.md#bib1304)
 OD 方法由上述 CCD 方程加上一组附加条件定义，即团簇能量相对于轨道变化取极小值。这可以用数学形式表达为

<a id="eq529"></a>
$$
\frac{\partial E_{\mathrm{CCD}}}{\partial\theta_{i}^{a}}=0 \tag{6.76}
$$

其中旋转角 $\theta_{i}^{a}$ 将第 $i$ 个占据轨道与第 $a$ 个虚（空）轨道混合。因此，定义单行列式参考态的轨道经过优化以使耦合簇能量极小化，从而在变分意义上最适合这一目的。所得到的轨道是近似的 Brueckner 轨道（Brueckner orbitals）。

OD 方法的优点在于形式上的简洁性（轨道变化与单替换本质上是冗余变量）。在 Hartree-Fock 理论表现不佳的情况下（例如非物理的对称性破缺，或者不收敛），使用不需要 HF 轨道的 OD 方法，相比于 CCSD 或 QCISD，在实际应用中也具有优势。**Q-Chem** 支持使用 OD 方法计算能量和解析梯度。OD 能量的计算成本是 CCSD 或 QCISD 方法的两倍多，但能量加梯度的总成本大致相当，尽管 OD 仍然更为昂贵。OD 方法的另一个优点是它可以在活性空间（active space）中进行，如后文 [6.14](sect_ccactive.md) 节所述。
