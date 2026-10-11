---
title: "6.12.3 Coupled Cluster Singles, Doubles and Triples (CCSDT)"
---

## 6.12.3 Coupled Cluster Singles, Doubles and Triples (CCSDT)

(July 4, 2026)

The coupled-cluster method with
single, double and triple substitutions, abbreviated as CCSDT [[996]](../bib_references/bib.md#bib66)

includes single, double and triple excitation operators in the exponential ansatz.
The theory of the method is very similar to that of CCSD – with triple excitations
included fully. We only present the basic equations. These can be compared with
the CCSD equations presented in the previous section, so as to understand the similarities
and differences between CCSD and CCSDT.
The CCSDT wave-function defined by

<a id="eq_ccsdt_psi"></a>

$$
\left|{\Psi_{\mathrm{CCSD}}}\right\rangle=\exp\left({\hat{T}_{1}+\hat{T}_{2}+\hat{T}_{3}}\right)\left|{\Phi_{0}}\right\rangle \tag{6.64}
$$

where, the operators, $\hat{T}_{1}$ and $\hat{T}_{2}$ are defined using Eqs. [6.59](Ch6.S12.SS2.md#eq519) and [6.60](Ch6.S12.SS2.md#eq520).
The operator, $\hat{T}_{3}$ is defined by

<a id="eq_ccsdt_t3"></a>

$$
\hat{T}_{3}\left|{\Phi_{0}}\right\rangle=\frac{1}{36}\sum_{ijk}^{\mathrm{occ}}{\sum_{abc}^{\mathrm{virt}}{t_{ijk}^{abc}}}\left|{\Phi_{ijk}^{abc}}\right\rangle \tag{6.65}
$$

The CCSDT equations are coupled non-linear simultaneous equations of the tensors,
$\hat{T}_{1}$, $\hat{T}_{2}$ and $\hat{T}_{3}$. However, the correlation energy depends only on
$\hat{T}_{1}$ and $\hat{T}_{2}$ amplitudes (The energy equations is same as Eq [6.61](Ch6.S12.SS2.md#eq521)).
The effect of
triples is due to mutual coupling between singles, doubles and triples

<a id="A3.S8.EGx23"></a>

$$
\displaystyle E_{\mathrm{CCSDT}} \tag{6.66}
$$

Currently, the CCSDT functionality is available for computation of correlation energy only.
