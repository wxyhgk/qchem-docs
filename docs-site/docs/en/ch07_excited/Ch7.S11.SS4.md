---
title: "7.11.4 Short-Range Density Functional Correlation within RAS-CI"
---

## 7.11.4 Short-Range Density Functional Correlation within RAS-CI

(July 4, 2026)

Alternatively, effective dynamic correlation can be introduced into the RAS-CI wave function
by means of short-range density functional correlation energy.
The idea relies on the different ability of wave function methods and DFT to treat
non-dynamic and dynamic correlations.
Concretely, the RAS-CI-$sr$DFT (or RAS-$sr$DFT) method[[211]](../bib_references/bib.md#bib206)

is based on the range separation of the electron-electron Coulomb operator ($\hat{V}_{ee}$)
through the error function to describe long-range interactions,

<a id="A3.S8.EGx69"></a>

$$
\displaystyle\hat{V}_{\text{ee}}^{lr,\mu} \tag{7.166}
$$

where $r_{ij}$ is the inter electronic distance and the parameter $\mu$ controls
the extend of short- and long-range interactions.
Such splitting of $\hat{V}_{\text{ee}}$ provides a well-defined approach to merge WFT with
DFT by applying $\hat{V}_{\text{ee}}^{lr,\mu}$ to RAS-CI and $V_{\text{ee}}^{lr,\mu}$ to DFT.
Within the RAS-$sr$DFT approach, the energy of an electronic state can be expressed as:

<a id="Ch7.E168"></a>

$$
E^{\text{RAS-}sr\text{DFT}}=\min_{\Psi^{\mu}}\left[\langle\Psi^{\mu}|\hat{T}+\hat{V}_{ne}+\hat{V}_{ee}^{lr,\mu}|\Psi^{\mu}\rangle+E_{\text{H}}^{sr,\mu}[\rho]+E_{\text{xc}}^{sr,\mu}[\rho]\right] \tag{7.168}
$$

where $\rho\equiv\rho[\Psi^{\mu}]$, and $E_{\text{H}}^{sr,\mu}[\rho]$ and $E_{\text{xc}}^{sr,\mu}[\rho]$
are the short-range Hartree and exchange-correlation energy functionals, respectively.
The RAS-CI wave function can be combined with different short-range exchange and
correlation functionals (Sections [5.3.3](../ch05_dft/sect_DFTexchange.md) and [5.3.4](../ch05_dft/sect_DFTcorrelation.md)).
