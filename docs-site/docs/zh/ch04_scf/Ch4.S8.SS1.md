---
title: "4.8.1 Introduction"
---

## 4.8.1 Introduction

(July 4, 2026)

Closely related to the dual-basis approach of Section [4.7](sect_dualbasis.md), but
somewhat more general, is the Hartree-Fock perturbative correction (HFPC)
developed by Deng *et al.*.[[318]](../bib_references/bib.md#bib322)
 An HFPC calculation
consists of an iterative HF calculation in a small primary basis followed by a
single Fock matrix formation, diagonalization, and energy evaluation in a
larger, secondary basis. In the following, we denote a conventional HF
calculation by HF/basis, and a HFPC calculation by HFPC/primary/secondary. Using a primary basis of $n$ functions, the
restricted HF matrix elements for a 2$m$-electron system are

<a id="Ch4.E65"></a>
$$
F_{\mu\nu}=h_{\mu\nu}+\sum_{\lambda\sigma}^{n}P_{\lambda\sigma}\left[(\mu\nu|\lambda\sigma)-\frac{1}{2}(\mu\lambda|\nu\sigma)\right] \tag{4.65}
$$

Solving the Roothaan-Hall equation in the primary basis results in
molecular orbitals and an associated density matrix, $\mathbf{P}$. In an HFPC
calculation, $\mathbf{P}$ is subsequently used to build a new Fock matrix,
$\mathbf{F}^{[1]}$, in a larger secondary basis of $N$ functions

<a id="eq:F1"></a>
$$
F_{ab}^{[1]}=h_{ab}+\sum_{\lambda\sigma}^{n}P_{\lambda\sigma}\left[(ab|\lambda\sigma)-\frac{1}{2}(a\lambda|b\sigma)\right] \tag{4.66}
$$

where $\lambda$, $\sigma$ indicate primary basis functions and $a$, $b$
represent secondary basis functions. Diagonalization of $\mathbf{F}^{[1]}$ affords
improved molecular orbitals and an associated density matrix $\mathbf{P}^{[1]}$. The
HFPC energy is given by

<a id="eq:EHFPC"></a>
$$
E^{\text{HFPC}}=\sum_{ab}^{N}P^{[1]}_{ab}h_{ab}+\frac{1}{2}\sum_{abcd}^{N}P^{[1]}_{ab}P^{[1]}_{cd}\bigl{[}2(ab|cd)-(ac|bd)\bigr{]} \tag{4.67}
$$

where $a$, $b$, $c$ and $d$ represent secondary basis functions. This differs
from the DBHF energy evaluation where $\mathbf{PP}^{[1]}$, rather than
$\mathbf{P}^{[1]}\mathbf{P}^{[1]}$, is used. The inclusion of contributions that are
quadratic in $\mathbf{PP}^{[1]}$ is the key reason for the fact that HFPC is more
accurate than DBHF.

Unlike dual-basis HF, HFPC does not require that the small basis be a proper
subset of the large basis, and is therefore able to jump between any two basis
sets. Benchmark study of HFPC on a large and diverse data set of total and
reaction energies demonstrate that, for a range of primary/secondary
basis set combinations, the HFPC scheme can reduce the error of the primary
calculation by around two orders of magnitude at a cost of about one third that
of the full secondary calculation.[[318]](../bib_references/bib.md#bib322)

A density-functional version of HFPC (“DFPC”)[[320]](../bib_references/bib.md#bib324)
 seeks to
combine the low cost of pure DFT calculations using small bases and grids, with
the high accuracy of hybrid calculations using large bases and grids. The DFPC
approach is motivated by the dual-functional method of Nakajima and
Hirao[[974]](../bib_references/bib.md#bib1015)
 and the dual-grid scheme of Tozer
*et al.*

 Combining these features affords a triple
perturbation: to the functional, to the grid, and to the basis set. We call
this approach density-functional “triple jumping”.
