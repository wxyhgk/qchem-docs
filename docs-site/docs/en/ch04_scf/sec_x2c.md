---
title: "4.9.6 Relativistic Effects"
---

## 4.9.6 Relativistic Effects

(July 4, 2026)

Relativistic effects play a major role in several physical and chemical phenomena, such as the properties of heavy elements and the proper characterization of the most inner energy levels probed in x-ray espectroscopy experiments. Solving the four component Dirac equation, which describes both electrons and its anti-particles (positrons), is computationally expensive. Since most chemical proceses can be explained by solely taking the electronic wave function into account, several ways of effectively decoupling the electronic and positronic degrees of freedom have been proposed.

The one-electron exact two-component (1eX2C) Hamiltonian provides a route for achieving such a
decoupling.[[610]](../bib_references/bib.md#bib633)

The method relies on solving the more tractable one electron four-component Dirac Hamiltonian in a restricted kinetic balance (RKB) form,[[744]](../bib_references/bib.md#bib777)
 to obtain the decoupling unitary transformations that will be used to modify the one-electron matrix elements, such as the kinetic energy and nuclear-attraction, to account for relativistic effects. A key ingredient to the X2C transformation matrices is to compute

<a id="Ch4.E75"></a>

$$
W_{{\rm SF},\mu\nu}=\langle\phi_{\mu}|\vec{p}\cdot\left(V\vec{p}\right)|\phi_{\nu}\rangle \tag{4.75}
$$

where $W_{{\rm SF},\mu\nu}$ is a matrix elements for the small-component of the full Dirac Hamiltonian, only computing the scalar-relativistic component. This is accomplished by noting that the the momentum operator is the generator of translations and its effects on a basis function can be captured by taking appropriate derivatives of such functions. It should be noted that, in order to properly capture the effects of the small components to the electronic wave function through X2C, **all-electron decontracted basis sets are required**. Since the **Q-Chem** 7.0 release, analytic implementation for $W_{{\rm SF},\mu\nu}$ is also available for SF-1eX2C and is set as new default. Full details of the finite difference X2C algorithm are provided in Ref. [[292]](../bib_references/bib.md#bib296)
. An example on how to include scalar relativistic effects to model K-edge x-ray spectroscopy can be found in Section [7.12.4](../ch07_excited/ex_COCOREIP.md).

REL_X2C

### `REL_X2C`

> **Enables X2C scalar relativistic calculation**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Perform a regular, non-relativistic SCF calculation
>     * 1
>     * Perform a scalar relativistic X2C calculation
> * **Recommendation**: Set to 1 if a scalar relativistic X2C calculation is desired.

REL_X2C_FD

### `REL_X2C_FD`

> **Performs X2C calculation with finite difference based W matrix elements**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Build the W matrix with analytic implementation
>     * 1
>     * Build the W matrix with finite difference implementation
> * **Recommendation**: Use the analytic implementation for non-testing purposes. As of the Q-Chem 7.0 release, the analytic expression is only implemented for SF-1eX2C.

REL_X2C_FD_DISPLACEMENT

### `REL_X2C_FD_DISPLACEMENT`

> **Controls finite difference step for calulating W**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$
>     * Set finite difference step to
>     * $n\times 10^{-6}$
> * **Recommendation**: None

## 4.9.6.1 One-Electron Spin–Orbit Coupling

In principle, the full solution to the 1eX2C Hamiltonian can be achieved, which will also include a spin-orbit coupling term.
This, however, requires a spin-generalized and complex-valued solution.
This can be seen by the additional matrix $W_{\text{SOC},\mu\ nu}$ required to obtain a full $W$ matrix:

<a id="Ch4.E76"></a>

$$
W_{{\rm SOC},\mu\nu}=i\sigma\cdot\langle\phi_{\mu}|\vec{p}\times\left(V\vec{p}\right)|\phi_{\nu}\rangle \tag{4.76}
$$

which is complex-valued and requires a cross product of different pauli matrices, resulting in a spin-generalized solution. Thus SOC effects may only be included when REL_X2C = 1 is called in cGHF routine - other calculations (e.g., RHF, UHF, ROHF) will all result in SF-1eX2C and will not include SOC effects. Setting the rem varaible REL_X2C = 1 in cGHF class automatically computes $W_{{\rm SOC},\mu\nu}$ unless REL_SF_X2C_CGHF is also set to 1.

REL_SF_X2C_CGHF

### `REL_SF_X2C_CGHF`

> **Enables X2C scalar relativistic calculation in a cGHF routine.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Perform a full relativistic X2C calculation with SOC effects
>     * 1
>     * Perform a scalar relativistic X2C calculation
> * **Recommendation**: Set to 1 if a scalar relativistic X2C calculation in a cGHF class is desired. Must be used with REL_X2C = 1 . Otherwise, non-relativistic calculation is performed without X2C, and this rem variable is ignored.

## 4.9.6.2 Screened-Nuclear Spin–Orbit Coupling for Two-Electron SOC

Although two-electron SOC terms in the X2C term can in principle be computed, the relevant matrix elements are often highly complicated and difficult to be evaluated.
Instead, a popular approach to approximation the two-electron SOC effects in X2C scheme is to empirically scale the spin-orbit dependent terms of the full 1eX2C
Hamiltonian. The family of this methods is called screened-nuclear spin-orbit approach (SNSO), first suggested by Boettger [[141]](../bib_references/bib.md#bib131)
.
Since then, improved form of the coefficient which accommodate diffuseness/tightness of the $p$-shell Gaussian-Type-Orbitals (GTOs)
as well as occupied and virtual MOs [[389]](../bib_references/bib.md#bib397)
 were suggested. Particularly, a new parametrization of the original SNSO
coefficients based on the full four-component Dirac-Coulomb-Breit (DCB) Hamiltonian orbital splitting results was provided.[[362]](../bib_references/bib.md#bib367)

REL_SNSO

### `REL_SNSO`

> **Enables 1eX2C-SNSO calculation in a cGHF routine.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Perform a full relativistic X2C calculation with unadjusted SOC Hamiltonian
>     * 1
>     * Perform a full relativistic X2C calculation with SOC Hamiltonian adjusted by original Boetter coefficients
>     * 2
>     * Perform a full relativistic X2C calculation with SOC Hamiltonian adjusted by modified SNSO coefficients by Yoshizawa and co-workers
>     * 3
>     * Perform a full relativistic X2C calculation with SOC Hamiltonian adjusted by DC-SNSO coefficients from Ehrman and co-workers
>     * 4
>     * Perform a full relativistic X2C calculation with SOC Hamiltonian adjusted by universal DCB-SNSO coefficients from Ehrman and co-workers
>     * 5
>     * Perform a full relativistic X2C calculation with SOC Hamiltonian adjusted by row-dependent DCB-SNSO coefficients from Ehrman and co-workers
> * **Recommendation**: Set to 1 for most general cases. Universal DCB-SNSO coefficients are the most recent contribution to the SNSO family and is reported to give accurate doublet splitting of $L_{2,3}$ -edges.
