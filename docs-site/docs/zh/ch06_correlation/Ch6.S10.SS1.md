---
title: "6.10.1 Introduction"
---

## 6.10.1 Introduction

(July 4, 2026)

A useful $\mathcal{O}(N^{4})$ approach called the direct random phase
approximation (dRPA) based on the RI approximation is available. This
particular implementation was added by Joonho Lee working with Martin
Head-Gordon.[[784]](../bib_references/bib.md#bib829)
 RI-dRPA has been applied to the
thermochemistry[[346]](../bib_references/bib.md#bib350)
 and non-covalent interaction
problems[[991]](../bib_references/bib.md#bib1033)
 and often demonstrated superior performance over
RI-MP2. In terms of the computational cost, RI-dRPA should be compared to the
scaled-opposite-spin MP2 while theoretically it involves diagrams far beyond
second-order and includes infinite-order diagrams similarly to coupled-cluster
theory. In fact, one can view dRPA as a reduced coupled-cluster with doubles
approach.[[1225]](../bib_references/bib.md#bib1280)
 In a nutshell, we define the dRPA energy as

<a id="Ch6.E53"></a>
$$
E=E_{\text{HF}}+E_{\text{c}}^{\text{dRPA}} \tag{6.53}
$$

where using the plasmon formula we compute[[373]](../bib_references/bib.md#bib377)

<a id="Ch6.E54"></a>
$$
E_{\text{c}}^{\text{dRPA}}=\int_{-\infty}^{\infty}\frac{\mathrm{d}\omega}{4\pi}\mathrm{tr}\left[\ln\left(\mathbf{I}+\mathbf{Q}(\omega)\right)-\mathbf{Q}(\omega)\right] \tag{6.54}
$$

where

<a id="Ch6.E55"></a>
$$
\mathbf{Q}(\omega)=2\mathbf{B}^{T}\mathbf{D}(\mathbf{D}^{2}+\omega^{2}\mathbf{I})^{-1}\mathbf{B} \tag{6.55}
$$

with

<a id="A3.S8.EGx21"></a>
$$
\displaystyle B_{ia,P} \tag{6.56}
$$

In this form, the cost of computing the dRPA correlation is quartic-scaling
which is comparable to SOS-MP2. To use this method, one must set
METHOD = RIDRPA along with AUXBASIS.
