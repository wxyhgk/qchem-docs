---
title: "6.12.4 二阶近似耦合簇单双激发模型 (CC2)"
---

## 6.12.4 二阶近似耦合簇单双激发模型 (CC2)

(July 4, 2026)

二阶近似耦合簇单双激发模型（second-order approximate coupled cluster singles and doubles model，CC2）[[249]](../bib_references/bib.md#bib250)的方程与 CCSD 方程类似，其中双激发振幅方程采用如下近似：

<a id="Ch6.E70"></a>
$$
E_{\mathrm{CC2}}=\langle\Phi_{0}\left|\hat{H}\exp\left(\hat{T}_{1}+\hat{T}_{2}\right)\right|\Phi_{0}\rangle \tag{6.70}
$$

<a id="Ch6.E71"></a>
$$
0=\left\langle{\Phi_{i}^{a}\left|{\bar{H}}+\left[{\bar{H}},\hat{T}_{2}\right]\right|\Phi_{0}}\right\rangle \tag{6.71}
$$

<a id="Ch6.E72"></a>
$$
0=\left\langle{\Phi_{ij}^{ab}\left|{\bar{H}}+\left[\hat{F},\hat{T}_{2}\right]\right|\Phi_{0}}\right\rangle \tag{6.72}
$$

其中，以单激发簇算符指数函数进行的相似变换哈密顿量为：

<a id="Ch6.E73"></a>
$$
\bar{H}=\exp\left(-\hat{T}_{1}\right)\hat{H}\exp\left(\hat{T}_{1}\right) \tag{6.73}
$$

**Q-Chem** 中可计算 CC2 能量，通过将关键字 METHOD 设置为 CC2 或 EOM-CC2 来请求计算。CC2 与 MP2 的基态能量及性质精度相当，但 CC2 可以高效地与 EOM（方程运动，Equation of Motion）形式体系结合，用于处理激发态/电子附着态/电离态等状态。
若结合分辨率恒等近似（resolution-of-identity，RI；参见第 [6.12.10](topic_ricc.md) 节），RI-CC2 可应用于大体系。
RI-CC2 既可通过 CCMAN2 使用，也可通过 **libgmbpt** 使用；
第 [7.9.4](../ch07_excited/sec_eomcc2.md) 节提供了设置 CC2 与 EOM-CC2 计算的指南。
