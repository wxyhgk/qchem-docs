---
title: "4.10.1 Introduction"
---

## 4.10.1 Introduction

(July 4, 2026)

The xTB family of semiempirical tight-binding methods offers an efficient route
to low-cost electronic-structure calculations for large molecular systems. The
present **Q-Chem** implementation is based on the GFN2-xTB Hamiltonian of
Bannwarth, Ehlert, and Grimme,[[73]](../bib_references/bib.md#bib58)
 which combines an extended
Hückel-like zeroth-order Hamiltonian with self-consistent isotropic and
anisotropic electrostatic and exchange-correlation contributions. For
open-shell systems, **Q-Chem** also supports an unrestricted spin-polarized
variant in the spirit of the spGFN2-xTB developments described in
Refs. [[986]](../bib_references/bib.md#bib1030)
, [[959]](../bib_references/bib.md#bib999)
, and
[[958]](../bib_references/bib.md#bib1000)
.

## 4.10.1.1 Theoretical Background

GFN2-xTB belongs to the density-functional tight-binding (DFTB)
family,

 in which the Kohn–Sham DFT energy is expanded
around a superposition of neutral atomic reference densities,

<a id="Ch4.E77"></a>

$$
\rho_{0}(\mathbf{r})=\sum_{A}\rho_{A}^{0}(\mathbf{r}), \tag{4.77}
$$

with the density fluctuation defined as $\delta\rho=\rho-\rho_{0}$. In
schematic form, the energy expansion is

<a id="Ch4.E78"></a>

$$
E[\rho]=E^{(0)}[\rho_{0}]+E^{(1)}[\rho_{0},\delta\rho]+E^{(2)}[\rho_{0},(\delta\rho)^{2}]+E^{(3)}[\rho_{0},(\delta\rho)^{3}]+\cdots. \tag{4.78}
$$

The zeroth-order term defines the reference atomic energies together with a
short-range repulsion model, the first-order term yields the extended
Hückel-like valence Hamiltonian, and the higher-order terms account for the
self-consistent response to charge-density fluctuations.[[73]](../bib_references/bib.md#bib58)

In GFN2-xTB, the higher-order response includes isotropic shell-charge terms as
well as anisotropic multipole corrections.

The working GFN2-xTB energy expression is[[73]](../bib_references/bib.md#bib58)

<a id="Ch4.E79"></a>

$$
E_{\mathrm{GFN2-xTB}}=E_{\mathrm{rep}}+E_{\mathrm{disp}}+E_{\mathrm{EHT}}+E_{\mathrm{IES}}+E_{\mathrm{IXC}}+E_{\mathrm{AES}}+E_{\mathrm{AXC}}+G_{\mathrm{Fermi}}. \tag{4.79}
$$

Here, $E_{\mathrm{rep}}$ is a classical short-range repulsion term,
$E_{\mathrm{EHT}}$ is the extended Hückel covalent-bonding contribution,
$E_{\mathrm{IES}}$ and $E_{\mathrm{IXC}}$ are the isotropic electrostatic and
exchange-correlation terms, $E_{\mathrm{AES}}$ and $E_{\mathrm{AXC}}$ are the
anisotropic multipole electrostatic and exchange-correlation corrections, and
$G_{\mathrm{Fermi}}$ is the finite-temperature entropy term that allows
fractional occupations. In the original standalone GFN2-xTB model,
$E_{\mathrm{disp}}$ is the self-consistent D4 dispersion contribution. For
open-shell systems, the spin-polarized extension adds a shell-wise
spin-polarization energy based on Mulliken spin populations and atomic spin
constants.[[986]](../bib_references/bib.md#bib1030)

This implementation is intended for rapid screening, structure refinement, and
inexpensive single-point calculations. In practice it is most useful as a
fast preoptimization or exploratory tool before higher-level calculations are
carried out.

!!! note "Note"
    The present **Q-Chem** implementation does *not* include the D4
    dispersion contribution that is part of the original standalone
    GFN2-xTB model. Consequently, total energies and optimized structures can
    differ from those obtained with the reference `xtb` program,
    especially for systems where dispersion interactions are important.

