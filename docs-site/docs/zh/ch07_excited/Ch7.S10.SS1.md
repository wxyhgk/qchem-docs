---
title: "7.10.1 引言"
---

## 7.10.1 引言

（2026 年 7 月 4 日）

ADC($n$) 系列相关激发态方法是一组基于微扰论的尺寸广延（size-extensive）激发态方法。ADC 的每一个阶数 $n$ 都给出了与基态著名的 $n$ 阶 Møller-Plesset 微扰论（Møller-Plesset perturbation theory, MP）相对应的激发态方法。目前，**Q-Chem** 中实现了 ADC(0)、ADC(1)、ADC(2)-s、ADC(2)-x 和 ADC(3) 等 ADC 变体。[[1494]](../bib_references/bib.md#bib1555)
 密度拟合（resolution-of-the-identity，RI）近似可与任意 ADC 变体配合使用。此外，两种 ADC(2) 变体还提供了自旋相反标度（spin-opposite scaling）版本。[[717]](../bib_references/bib.md#bib749)
 借助核价分离（core-valence separation，CVS）近似，可以计算核激发态，用于模拟 X 射线吸收光谱。目前可用的方法有 CVS-ADC(1)、CVS-ADC(2)-s、CVS-ADC(2)-x 和 CVS-ADC(3)。[[1494]](../bib_references/bib.md#bib1555)

电离态和电子附着态可以使用非 Dyson 的 IP-ADC 和 EA-ADC 方法进行计算。目前已实现 IP-ADC(2)、IP-ADC(3)、EA-ADC(2) 和 EA-ADC(3) 方法。[[317]](../bib_references/bib.md#bib317)

除基于 Møller-Plesset 的（MP-）ADC 之外，针对激发态还提供了基于尺寸一致（size-consistent）的 Brillouin-Wigner（BWs）分割的正则方案（另见 [6.8](../ch06_correlation/topic_bws2.md)）。
目前，Q-Chem 中实现了与密度拟合近似相结合的 BWs-ADC(0)、BWs-ADC(2)-s、BWs-ADC(2)-x 和 BWs-ADC(3)。
