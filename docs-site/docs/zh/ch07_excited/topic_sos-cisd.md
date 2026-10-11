---
title: "7.8.4 SOS-CIS(D) 模型"
---

## 7.8.4 SOS-CIS(D) 模型

（2026 年 7 月 4 日）

与 MP2 情形类似，可以通过对 CIS(D) 表达式中的异自旋（opposite-spin）分量进行半经验缩放来提高 CIS(D) 计算的精度：

<a id="Ch7.E91"></a>
$$
E^{\mathrm{SOS-CIS(D)}}=c_{U}\left\langle{\Psi^{\mathrm{CIS}}}\right|V\left|{U_{2}^{\mathrm{OS}}\Psi^{\mathrm{HF}}}\right\rangle+c_{T}\left\langle{\Psi^{\mathrm{CIS}}}\right|V\left|{T_{2}^{\mathrm{OS}}U_{1}\Psi^{\mathrm{{HF}}}}\right\rangle \tag{7.91}
$$

对应的基态能量为

<a id="Ch7.E92"></a>
$$
E^{\mathrm{SOS-MP2}}=c_{T}\left\langle{\Psi^{\mathrm{HF}}}\right|V\left|{T_{2}^{\mathrm{OS}}\Psi^{\mathrm{HF}}}\right\rangle \tag{7.92}
$$

更重要的是，通过采用 Laplace 变换技术，该 SOS-CIS(D) 能量的计算量仅随分子尺寸的四次方增长。[[1162]](../bib_references/bib.md#bib1215)

因此，SOS-CIS(D) 可以应用于相对较大分子的激发能计算。
