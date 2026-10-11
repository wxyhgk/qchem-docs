---
title: "11.5.3 结合 EFP 的激发态计算"
---

## 11.5.3 结合 EFP 的激发态计算

（2026 年 7 月 4 日）

EFP 与 EOM-CCSD（通过 CCMAN 和 CCMAN2 两种方式）、CIS、CIS(D)、TDDFT 以及 ADC 的接口均已开发完成。[[1272]](../bib_references/bib.md#bib1325)

在激发态计算中，各片段（fragment）的诱导偶极被冻结在与电子基态（HF 或 DFT）一致的取值上。由此得到的激发能包含了可极化环境的零级响应。此外，微扰态特异（state-specific）极化校正[[1272]](../bib_references/bib.md#bib1325)按下式计算：

<a id="eq:EOM-EFP-ene2"></a>

$$
\Delta E_{\text{pol}}=\frac{1}{2}\sum_{k}\sum_{a}^{x,y,z}\Bigl{[}-(\mu_{\text{ex},a}^{k}-\mu_{\text{gr},a}^{k})(F_{a}^{\text{mult},k}+F_{a}^{\text{nuc},k})\\
+(\tilde{\mu}_{\text{ex},a}^{k}F_{\text{ex},a}^{\text{ai},k}-\tilde{\mu}_{\text{gr},a}^{k}F_{\text{gr},a}^{\text{ai},k})-(\mu_{\text{ex},a}^{k}-\mu_{\text{gr},a}^{k}+\tilde{\mu}_{\text{ex},a}^{k}-\tilde{\mu}_{\text{gr},a}^{k})F_{\text{ex},a}^{\text{ai},k}\Bigr{]} \tag{11.77}
$$

其中 $F_{\text{gr}}^{\text{ai}}$ 和 $F_{\text{ex}}^{\text{ai}}$ 分别是参考态密度和激发态电子密度所产生的电场。$\mu_{\text{gr}}^{k}$ 和 $\tilde{\mu}_{\text{gr}}^{k}$ 是与参考态密度一致的、位于分布式极化率点 $k$ 处的诱导偶极与共轭诱导偶极（conjugated induced dipole），而 $\mu_{\text{ex}}^{k}$ 和 $\tilde{\mu}_{\text{ex}}^{k}$ 则是对应于激发态密度的诱导偶极。

式 ([11.77](#eq:EOM-EFP-ene2)) 中的前两项给出了 QM/EFP 体系在激发态与基电子态下极化能之差；最后一项则是基态优化所得诱导偶极与激发态波函数相互作用的领头校正项。因此，激发态同时包含直接极化贡献和间接极化贡献。间接项来源于溶质在被溶剂诱导偶极所产生的场中的轨道弛豫。由式 ([11.77](#eq:EOM-EFP-ene2)) 给出的直接项则是可极化环境对激发时溶质电子密度变化的响应。需要注意的是，在 EOM-IP/EFP 中，由于中性物种与电离物种的电子密度差异很大，直接极化贡献可能非常大（可达零点几个 eV）。

微扰 QM/EFP 方案的一个重要优点在于：它不会损害单参考激发态计算的多态（multi-state）本质，并且由于目标态的电子波函数是在可极化环境的同一（参考态）场中求得的，它们彼此之间保持正交。例如，可以计算这些态之间的跃迁性质。

在 EOM-CCSD/EFP 计算中，参考态 CCSD 关于 $T$ 簇振幅的方程是使用经有效片段（effective fragments）的静电与极化贡献修正后的 HF 哈密顿量求解的，见式 ([11.62](sec_theory.md#eq:H-EFP))。在该耦合簇计算中，片段的诱导偶极被冻结在其 HF 取值上。

EOM-CC/EFP 方案适用于 **Q-Chem** 目前支持的任何类型的 EOM 激发算符 $\hat{R}_{k}$，即自旋翻转（spin-flipping, SF）、激发能（excitation energies, EE）、电离势（ionization potential, IP）、电子亲和能（electron affinity, EA）（详见第 [7.9.18](../ch07_excited/sub_ccjobcontol.md) 节）。然而，直接极化校正需要计算激发态的单电子密度，因此只会对已实现单电子性质的方法加以计算。
