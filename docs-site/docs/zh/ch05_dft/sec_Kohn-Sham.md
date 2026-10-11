---
title: "5.2 Kohn-Sham Density Functional Theory"
---

# 5.2 Kohn-Sham Density Functional Theory

(July 4, 2026)

The density functional theory by Hohenberg, Kohn, and Sham[[587]](../bib_references/bib.md#bib610)
 stems from earlier work by
Dirac,[[329]](../bib_references/bib.md#bib333)
 who showed that the exchange energy of a uniform electron gas can be computed exactly from
the charge density along. However, while this traditional *density* functional approach, nowadays called
“orbital-free” DFT, makes a direct connection to the density alone, in practice it is
constitutes a direct approach where the necessary equations contain only the electron density,
difficult to obtain decent approximations for the kinetic energy functional.
Kohn and Sham sidestepped this difficulty via an indirect approach in which the kinetic energy is computed exactly
for a noninteracting reference system, namely, the Kohn-Sham determinant.[[701]](../bib_references/bib.md#bib732)

It is the Kohn-Sham approach that first made DFT into a practical tool for calculations.

Within the Kohn-Sham formalism,[[701]](../bib_references/bib.md#bib732)
 the ground state
electronic energy, $E$, can be written as

<a id="eq:DFT_energy_components"></a>
$$
E=E_{\text{T}}+E_{\text{V}}+E_{\text{J}}+E_{\text{XC}} \tag{5.1}
$$

where $E_{\text{T}}$ is the kinetic energy, $E_{\mathrm{V}}$ is the electron–nuclear
interaction energy, $E_{\text{J}}$ is the Coulomb self-interaction of the
electron density, $\rho(\mathbf{r})$ and $E_{\text{XC}}$ is the exchange-correlation
energy. Adopting an unrestricted format, the $\alpha$ and $\beta$ total electron
densities can be written as

<a id="eq429"></a>
$$
\displaystyle\rho_{\alpha}(\mathbf{r}) \tag{5.2a}
$$

where $n_{\alpha}$ and $n_{\beta}$ are the number of alpha and beta electron
respectively, and $\psi_{i}$ are the Kohn-Sham orbitals. Thus, the total electron density is

<a id="eq430"></a>
$$
\rho(\mathbf{r})=\rho_{\alpha}(\mathbf{r})+\rho_{\beta}(\mathbf{r}) \tag{5.3}
$$

Within a finite basis set, the density is represented by[[1112]](../bib_references/bib.md#bib1163)

<a id="eq431"></a>
$$
\rho(\mathbf{r})=\sum_{\mu\nu}P_{\mu\nu}\phi_{\mu}(\mathbf{r})\phi_{\nu}(\mathbf{r})\;, \tag{5.4}
$$

where the $P_{\mu\nu}$ are the elements of the one-electron density matrix; see
Eq. ([4.24](../ch04_scf/Ch4.S2.SS2.md#eq:P(mu,nu))) in the discussion of Hartree-Fock theory. The various energy components in
Eq. ([5.1](#eq:DFT_energy_components)) can now be written

<a id="A3.S8.EGx16"></a>
$$
\displaystyle E_{\mathrm{T}} \tag{5.5}
$$

Minimizing $E$ with respect to the unknown Kohn-Sham orbital coefficients
yields a set of matrix equations exactly analogous to Pople-Nesbet equations of the UHF case,
Eq. ([4.13](../ch04_scf/Ch4.S2.SS1.md#eq:Pople-Nesbet)),
but with modified Fock matrix elements [*cf*. Eq. ([4.27](../ch04_scf/Ch4.S2.SS2.md#eq:F(mu,nu)))]

<a id="eq437"></a>
$$
\displaystyle F_{\mu\nu}^{\alpha} \tag{5.9a}
$$

Here, $\mathbf{F}^{\mathrm{XC}\alpha}$ and $\mathbf{F}^{\mathrm{XC}\beta}$ are the
exchange-correlation parts of the Fock matrices and depend on the
exchange-correlation functional used. UHF theory is recovered as a special case simply by taking
$F_{\mu\nu}^{\mathrm{XC}\alpha}=K_{\mu\nu}^{\alpha}$, and similarly for $\beta$.
Thus, the density and energy are obtained
in a manner analogous to that for the HF method. Initial guesses are
made for the MO coefficients and an iterative process is applied until self-consistency is achieved.
