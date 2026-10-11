---
title: "7.8.5 SOS-CIS(D${}_{0}$) 模型"
---

## 7.8.5 SOS-CIS(D${}_{0}$) 模型

(July 4, 2026)

上文所阐述的 CIS(D) 及其衍生方法均基于对 CIS 能量的二阶非简并微扰修正方案（即“先对角化、后微扰”（diagonalize-and-then-perturb）方案）。因此，当多个激发态的能量彼此接近时，这些方法可能会失效。在这种情况下，可以通过施加准简并微扰修正方案（即“先微扰、后对角化”（perturb-and-then-diagonalize）方案）来处理该体系。其工作表达式可通过对第 [7.8.2](topic_cisd.md) 节中给出的 CIS(D) 表达式进行略微修改而得到。[[541]](../bib_references/bib.md#bib557)

首先，从式 ([7.87](topic_cisd.md#eq619)) 出发，可以将 CIS(D) 能量显式地写为[[206]](../bib_references/bib.md#bib198)

<a id="Ch7.E93"></a>

$$
\omega^{\rm CIS}+\omega^{(2)}=\bf b^{(0)^{\mathbf{t}}}{\rm{\bf A}_{SS}^{(0)}}\bf b^{(0)}+\bf b^{(0)^{\mathbf{t}}}{\rm{\bf A}_{SS}^{(2)}}\bf b^{(0)}-\bf b^{(0)^{\mathbf{t}}}{\rm{\bf A}_{SD}^{(1)}\left({\bf D}_{DD}^{(0)}-\omega^{CIS}\right)^{-1}{\bf A}_{DS}^{(1)}}\bf b^{(0)} \tag{7.93}
$$

为避免微扰理论在近简并情形下失效，应当对整个单激发与双激发块构成的响应矩阵进行对角化。由于这样的对角化是一个非平凡的非线性问题，因此进一步引入了对该式二项式展开的附加近似：[[541]](../bib_references/bib.md#bib557)

<a id="Ch7.E94"></a>

$$
\rm\left({\bf D}_{DD}^{(0)}-\omega^{CIS}\right)^{-1}=\left({\bf D}_{DD}^{(0)}\right)^{-1}\left(1+\omega\left({\bf D}_{DD}^{(0)}\right)^{-1}+\omega^{2}\left({\bf D}_{DD}^{(0)}\right)^{-2}+...\right) \tag{7.94}
$$

SOS-CIS(D${}_{0}$) 能量 $\omega$ 被定义为利用该式的零阶展开所得响应矩阵的本征解。即：

<a id="Ch7.E95"></a>

$$
\rm\left({\bf A}_{SS}^{(0)}+{\bf A}_{SS}^{(2)}-{\bf A}_{SD}^{(1)}({\bf D}_{DD}^{(0)})^{-1}{\bf A}_{DS}^{(1)}\right)\bf b=\omega\bf b \tag{7.95}
$$

与 SOS-CIS(D) 类似，SOS-CIS(D${}_{0}$) 理论通过取该式的反自旋（opposite-spin）部分，并以两个半经验参数对其进行标度来定义：[[206]](../bib_references/bib.md#bib198)

<a id="Ch7.E96"></a>

$$
\rm\left({\bf A}_{SS}^{(0)}+{\it c_{T}}{\bf A}_{SS}^{OS(2)}-{\it c_{U}}{\bf A}_{SD}^{OS(1)}({\bf D}_{DD}^{(0)})^{-1}{\bf A}_{DS}^{OS(1)}\right)\bf b=\omega\bf
b \tag{7.96}
$$

借助拉普拉斯变换（Laplace transform）与辅助基组展开技术，该方法的计算量同样可以控制在四阶标度（4th-order scaling）。在 **Q-Chem** 中，还实现了高效的 SOS-CIS(D${}_{0}$) 四阶标度解析梯度。该梯度可用于在电子激发态势能面上进行激发态几何优化。
