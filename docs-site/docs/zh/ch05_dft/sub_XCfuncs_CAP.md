---
title: "5.13.3 可用于复吸收势的密度泛函近似"
---

## 5.13.3 可用于复吸收势（Complex Absorbing Potentials）的密度泛函近似

(July 4, 2026)

为常规实值电子密度定义的现有泛函可以复用于复变量密度泛函理论（complex-variable DFT）计算。[[1575]](../bib_references/bib.md#bib1638)

因此，本节列出的泛函衍生自 **Q-Chem** 中已有的泛函（参见第 [5.3 节](sect_XCfuncs.md)），
但已针对处理复值电子密度进行了适配。
其名称由原始泛函名称加上前缀 "cx_" 构成。

## 5.13.3.1 交换泛函

**注：

本节所有交换泛函均可通过 *$rem* 变量 EXCHANGE 调用。
**

- $\circ$

局域自旋密度近似（Local Spin-Density Approximation, LSDA）

- $\bullet$

cx_Slater: Slater-Dirac 交换泛函（X$\alpha$ 方法，$\alpha=2/3$）[[329]](../bib_references/bib.md#bib333)
- $\circ$

广义梯度近似（Generalized Gradient Approximation, GGA）

- $\bullet$

cx_B88: Becke 1988 年提出的交换泛函[[95]](../bib_references/bib.md#bib74)
- $\bullet$

cx_PBE: Perdew、Burke 和 Ernzerhof 交换泛函[[1062]](../bib_references/bib.md#bib1112)

## 5.13.3.2 相关泛函

**注：

本节所有相关泛函均可通过 *$rem* 变量 CORRELATION 调用。
**

- $\circ$

局域自旋密度近似（Local Spin-Density Approximation, LSDA）

- $\bullet$

cx_VWN5 / cx_VWN: Vosko-Wilk-Nusair 的 LSDA 相关能参数化形式 #5[[1410]](../bib_references/bib.md#bib1470)
- $\bullet$

cx_VWN1RPA: 采用 RPA 值的 Vosko-Wilk-Nusair LSDA 相关能参数化形式 #1[[1410]](../bib_references/bib.md#bib1470)
- $\circ$

广义梯度近似（Generalized Gradient Approximation, GGA）

- $\bullet$

cx_PBE: Perdew、Burke 和 Ernzerhof 相关泛函[[1062]](../bib_references/bib.md#bib1112)
- $\bullet$

cx_LYP: Lee-Yang-Parr 反平行自旋相关泛函[[780]](../bib_references/bib.md#bib813)

## 5.13.3.3 交换-相关泛函

**注：

本节所有交换-相关泛函均可通过 *$rem* 变量 METHOD 调用。
**

- $\circ$

局域自旋密度近似（Local Spin-Density Approximation, LSDA）

- $\bullet$

cx_LDA / cx_SVWN5: Slater LSDA 交换 + VWN5 LSDA 相关
- $\circ$

广义梯度近似（Generalized Gradient Approximation, GGA）

- $\bullet$

cx_PBE: PBE GGA 交换 + PBE GGA 相关
- $\bullet$

cx_BLYP: B88 GGA 交换 + LYP GGA 相关
- $\bullet$

cx_BPBE: B88 GGA 交换 + PBE GGA 相关
- $\circ$

全局杂化广义梯度近似（Global Hybrid Generalized Gradient Approximation, GH GGA）

- $\bullet$

cx_B1LYP: 25% HF 交换 + 75% B88 GGA 交换 + LYP GGA 相关[[17]](../bib_references/bib.md#bib1)
- $\bullet$

cx_B3LYP: 20% HF 交换 + 8% Slater LSDA 交换 + 72% B88 GGA 交换 + 19% VWN1RPA
LSDA 相关 + 81% LYP GGA 相关[[96]](../bib_references/bib.md#bib78)
- $\bullet$

cx_B3LYP5: 20% HF 交换 + 8% Slater LSDA 交换 + 72% B88 GGA 交换 + 19% VWN5 LSDA
相关 + 81% LYP GGA 相关[[96]](../bib_references/bib.md#bib78)
- $\bullet$

cx_B5050LYP: 50% HF 交换 + 8% Slater LSDA 交换 + 42% B88 GGA 交换 + 19% VWN5
LSDA 相关 + 81% LYP GGA 相关[[1239]](../bib_references/bib.md#bib1294)
- $\bullet$

cx_BHHLYP: 50% HF 交换 + 50% B88 GGA 交换 + LYP GGA 相关，有时称为 BH&H-LYP[[484]](../bib_references/bib.md#bib496)
- $\bullet$

cx_HFLYP: 100% HF 交换 + LYP GGA 相关
- $\bullet$

cx_PBE0: 25% HF 交换 + 75% PBE GGA 交换 + PBE GGA 相关[[19]](../bib_references/bib.md#bib3)
- $\bullet$

cx_PBE50: 50% HF 交换 + 50% PBE GGA 交换 + PBE GGA 相关[[114]](../bib_references/bib.md#bib101)
