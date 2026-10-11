---
title: "4.9.4 Holomorphic Hartree-Fock Theory"
---

## 4.9.4 Holomorphic Hartree-Fock Theory

(July 4, 2026)

## 4.9.4.1 Theory

To use multiple SCF solutions in NOCI (see Section [7.5](../ch07_excited/subsec_NOCI.md)),
it is essential that all solutions
exist across all geometries of interest to prevent discontinuities in the
NOCI energies. However, it is well known that symmetry-broken SCF solutions
can disappear at certain points along a potential energy surface,
for example at the Coulson-Fischer point in H${}_{2}$.
The holomorphic Hartree-Fock approach provides a means of analytically
continuing solutions across all geometries.[[584]](../bib_references/bib.md#bib607)

In holomorphic Hartree-Fock theory, the real Hartree-Fock equations are
analytically continued into the complex plane *without* introducing
the complex conjugation of molecular orbital coefficients.
Multiple solutions are then identified as the stationary points of the
holomorphic energy[[584]](../bib_references/bib.md#bib607)

<a id="eq:HoloHFEnergy"></a>

$$
\widetilde{E}=\frac{\langle\Psi^{*}|\hat{H}|\Psi\rangle}{\langle\Psi^{*}|\Psi\rangle}, \tag{4.70}
$$

where $\hat{H}$ defines the conventional electronic Hamiltonian

<a id="eq:HoloHamiltonian1"></a>

$$
\hat{H}=V_{\text{nuc}}+\sum_{i}^{N_{\text{e}}}\hat{h}(i)+\sum_{i<j}^{N_{\text{e}}}\frac{1}{r_{ij}}. \tag{4.71}
$$

As a result, the holomorphic Hartree-Fock equations are complex-analytic in the
orbital coefficients, satisfying the Cauchy-Riemann conditions,
and the number of stationary points is found to be constant across all geometries.[[173]](../bib_references/bib.md#bib169)

Real Hartree-Fock states remain stationary points of
the holomorphic Hartree-Fock energy, and where real solutions vanish, their
holomorphic counterparts continue to exist with complex orbital coefficients.[[175]](../bib_references/bib.md#bib168)

Holomorphic Hartree-Fock stationary points can be located using minor
modifications to conventional SCF algorithms.[[175]](../bib_references/bib.md#bib168)
.
Most significantly, by removing the complex conjugate of the wave function in
Eq. ([4.70](#eq:HoloHFEnergy)), the required complex holomorphic density
$\mathbf{P}$ and Fock $\mathbf{F}$ matrices become complex-symmetric
(*cf.* Hermitian), satisfying $P^{\mu\nu}=P^{\nu\mu}$ and $F_{\mu\nu}=F_{\nu\mu}$.
Moreover, since the complex conjugation must also be removed from the
normalisation constraint, the molecular orbital coefficients must form
a complex-orthogonal set (*cf*. unitary), *i.e.*,

<a id="eq:HoloComplexOrth"></a>

$$
\sum_{\mu\nu}C^{\cdot\mu}_{i\cdot}S_{\mu\nu}C^{\nu\cdot}_{\cdot j}=\delta_{ij}, \tag{4.72}
$$

Finally, the holomorphic Hartree-Fock orbital energies and total energy can
in general also become complex, and thus selecting the new occupied orbitals
on each SCF cycle using the orbital energies is poorly defined. Instead,
a complex-symmetric analogue to the Maximum Overlap Method can
be employed (see Section [4.5.14](topic_mom.md)).

Following real solutions past the Coulson-Fischer point into the complex
plane can often be difficult due to their coalesence with symmetry-pure
solutions on the real axis. However, by scaling the electron-electron
interaction using a complex parameter $\lambda$, *i.e.* introducing the Hamiltonian

<a id="eq:HoloHamiltonian"></a>

$$
\hat{H}=V_{\text{nuc}}+\sum_{i}^{N_{\text{e}}}\hat{h}(i)+\lambda\sum_{i<j}^{N_{\text{e}}}\frac{1}{r_{ij}}, \tag{4.73}
$$

it is possible to show that Coulson-Fischer points form *isolated*
exceptional points on the real axis.[[174]](../bib_references/bib.md#bib170)
 Consequently, following
a suitable complex $\lambda$ trajectory allows real solutions to be perturbed off
the real axis and followed with ease past the Coulson-Fischer point
into their complex holomorphic regimes.[[174]](../bib_references/bib.md#bib170)

These perturbed solutions can then be relaxed onto the real axis to
identify the holomorphic Hartree-Fock states required for NOCI.

## 4.9.4.2 Job Control

Within **Q-Chem**, the holomorphic Hartree-Fock approach is implemented in
the **libnoci** package (see Section [7.5.2](../ch07_excited/subsec_LIBNOCI.md)), accessed using
USE_LIBNOCI = TRUE and designed for locating multiple SCF solutions for
use in NOCI calculations.

SCF_HOLOMORPHIC

### `SCF_HOLOMORPHIC`

> **Turn on the use of holomorphic Hartree-Fock orbitals.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Holomorphic Hartree-Fock is turned off
>     * TRUE
>     * Holomorphic Hartree-Fock is turned on.
> * **Recommendation**: If TRUE, holomorphic Hartree-Fock complex orbital coefficients will always be used. If FALSE, but COMPLEX = TRUE , complex Hermitian orbitals will be used.

SCF_EESCALE_MAG

### `SCF_EESCALE_MAG`

> **Control the magnitude of the $\lambda$ electron-electron scaling.**
>
> * **Type**: `INTEGER`
> * **Default**: `$10000$`
> * **Options**:
>     * $abcde$
>     * corresponding to
>     * $a.bcde$
> * **Recommendation**: For holomorphic Hartree-Fock orbitals, only the magnitude of the input is used, while for real Hartree-Fock orbitals, the input sign indicates the sign of $\lambda$ .

SCF_EESCALE_ARG

### `SCF_EESCALE_ARG`

> **Control the phase angle of the complex $\lambda$ electron-electron scaling.**
>
> * **Type**: `INTEGER`
> * **Default**: `$00000$`
> * **Options**:
>     * $abcde$
>     * corresponding to
>     * $a.bcde$
> * **Recommendation**: A complex phase angle of $00500$ , meaning $0.0500$ , is usually sufficient to follow a solution safely past the Coulson-Fischer point and onto its complex holomorphic counterpart.
