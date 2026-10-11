---
title: "7.4.1 Introduction & Theory"
---

## 7.4.1 Introduction & Theory

(July 4, 2026)

Although the theory discussed in Section [7.3](sect_tddft.md) is known universally as “time-dependent” DFT (TDDFT),
in truth it is the frequency-domain transformation of linear-response (LR) DFT,[[418]](../bib_references/bib.md#bib427)

and is sometimes given the additional designation of LR-TDDFT in order to distinguish it from the “real time” (RT)
version of TDDFT that is described in this section. The phrase “real-time time-dependent DFT” (RT-TDDFT) is
sufficiently awkward that the theory described here is also known as *time-dependent Kohn-Sham* (TDKS)
theory,[[1578]](../bib_references/bib.md#bib1641)
 terminology that is actually more consistent with the original language used by
Gross and co-workers developing a theory based on the time-dependent Kohn-Sham equation.[[498]](../bib_references/bib.md#bib511)

The TDKS approach is explicitly time-dependent, and amounts to propagation of
time-dependent Kohn-Sham MOs following a perturbation of the ground-state density.

LR-TDDFT calculations are often the most efficient way to predict resonant
electronic response frequencies and intensities when only a small number of low-lying excited states are desired.
To obtain broadband spectra (in the x-ray regime, say), hundreds of excited states may be required, however.
In such cases, the real-time approach may be preferable because it can be used to obtain the entire absorption
spectrum (at all excitation energies) via Fourier transform of the time-dependent dipole moment function, without
the need to compute the spectrum state-by-state. This is the theoretical basis of *real-time*
electronic structure methods in general.[[1124]](../bib_references/bib.md#bib1171)

A perturbation creates a superposition of all (symmetry-allowed) excitations, and the Fourier components of the
ensuing time evolution encode all of the excitation energies. This theory is described in somewhat more detail in
the next section, following which the TDKS job control variables are described in Section [7.4.2](sec_TDKS_JobControl.md).
Calculation of broadband absorption spectra using the TDKS approach is discussed in Section [7.4.3](sec_TDKS_Spectra.md).

Starting with v. 5.3, **Q-Chem**’s TDKS module has been substantially rewritten, including support for
advanced propagators,[[1578]](../bib_references/bib.md#bib1641)
 complex absorbing potentials,[[1579]](../bib_references/bib.md#bib1642)
 and Padé approximants
to accelerate convergence of the Fourier-transformed dipole moment function.[[566]](../bib_references/bib.md#bib585)

Users of the TDKS/RT-TDDFT code are asked to cite Refs. [[1579]](../bib_references/bib.md#bib1642)
 and [[566]](../bib_references/bib.md#bib585)
.

Following a perturbation to the ground-state MOs $\phi_{k}(\mathbf{r},0)$ at $t=0$, these MOs
evolve in time according to the time-dependent Schrödinger equation. For an SCF level of theory, this is a one-electron equation

<a id="eq:TDKS"></a>
$$
\text{i}\hbar\frac{d\phi_{k}(\mathbf{r},t)}{dt}=\hat{F}(t)\phi_{k}(\mathbf{r},t)\;. \tag{7.58}
$$

This time evolution can equivalently be expressed in terms of the
Liouville-von Neumann equation for the time evolution of the density $\rho(\mathbf{r},t)$:

<a id="eq:LvN"></a>
$$
\text{i}\hbar\frac{d\rho(\mathbf{r},t)}{dt}=\bigl{[}\hat{F}(t),\;\rho(\mathbf{r},t)]\;. \tag{7.59}
$$

In addition to obtaining broadband spectra, real-time SCF methods can be used to simulate attosecond
dynamics of electrons, perhaps in the presence of strong fields. Note that the dynamics that is simulated by
integrating either Eq. ([7.58](#eq:TDKS)) or Eq. ([7.59](#eq:LvN)) is *electron* dynamics, the fundamental
timescale of which is attoseconds, as can be estimated by the magnitude of the atomic unit of time
($\hbar/E_{h}\approx 2.4\times 10^{-17}$ s). The finite integration time step $\Delta t$
must be small compared to this value, and the default in **Q-Chem** is set to $\Delta t=0.02~{}\mbox{a.u.}=4.8\times 10^{-4}$ fs.
The maximum timescale that can therefore reasonably
be simulated is likely only picoseconds, and at present this time propagation is available only within the clamped-nuclei
approximation, *i.e.*, it is not possible to simulate the couple electron–nuclear dynamics.

Because the Fock operator $\hat{F}$ depends on its own (time-evolving) eigenfunctions $\phi_{i}(\mathbf{r},t)$,
the operator $\hat{F}(t)$ that governs the time evolution in Eq. ([7.58](#eq:TDKS)) or Eq. ([7.59](#eq:LvN)) is time-dependent,
which complicates the integration of these equations.[[1578]](../bib_references/bib.md#bib1641)
 The simplest possible algorithm to integrate
these equations (over a finite time step $\Delta t$ is the *modified midpoint unitary transformation* (MMUT)
procedure,[[819]](../bib_references/bib.md#bib848)
 which approximates the operator $\hat{F}(t+\Delta t/2)$. When the MMUT algorithm is used,
the cost of a single electron dynamics time step is comparable to the cost of a single SCF cycle of a ground-state
SCF calculation, *i.e.*, it requires a single construction and diagonalization of the Fock matrix. The memory footprint
is about twice that of the ground state, because the time-dependent MOs are complex-valued, but this is usually
considerably smaller than the memory footprint for linear-response (LR-)TDDFT, especially of the number of roots
requested in the LR-TDDFT calculation is large (as required for broadband spectra), or if the density of states is
high (as in models of semiconductors).[[962]](../bib_references/bib.md#bib1004)

As compared to the first-order MMUT algorithm, higher-order predictor/corrector algorithms to integrate
the dynamics are also available.[[1578]](../bib_references/bib.md#bib1641)

These algorithms enable the use of larger time steps $\Delta t$ at a cost of a few Fock builds per time step.
Perhaps more importantly, the predictor/corrector algorithms iterate the Fock operators $\hat{F}(t)$ and
$\hat{F}(t+\Delta t)$ to self-consistency over each time step, which guarantees stable time propagation (assuming
that the self-consistent procedure converges). Stable dynamics is *not* guaranteed by the MMUT algorithm,
and total energy conservation turns out to be a necessary but not sufficient criterion to ensure that the trajectory has
been integrated accurately. Using MMUT, examples can be found where energy is conserved yet spectra are still shifted
(with respect to benchmarks results obtained using very small time steps) due to the use of a too-large value of $\Delta t$
that is undetected and undiagnosed by non-self-consistent MMUT algorithm.[[1578]](../bib_references/bib.md#bib1641)

Propagation of the electron dynamics requires only ground-state computational machinery (albeit with complex-valued
orbitals), and thus is available at any SCF level of theory, including Hartree-Fock theory or DFT. The name “TDKS”
(in contrast to the cumbersome “RT-TDDFT”) emphasizes that
Eq. ([7.58](#eq:TDKS)) is the Kohn-Sham analogue of the time-dependent Schrödinger equation.
The cost per time step for a TDKS calculation should be no larger than a few times the cost of a ground-state SCF cycle.
**Q-Chem**’s implementation exploits shared-memory parallelism and the use of at least 8 (but possibly more) processor
cores is highly recommended, since the number of required time steps (and thus the number of Fock builds) is likely to be
quite large. (The use of multiple cores is requested using the `-nt` flag.)

A TDKS calculation is requested by setting TDKS = TRUE in the *$rem* input section, and other
job control options are discussed in Section [7.4.2](sec_TDKS_JobControl.md).
Section [7.4.3](sec_TDKS_Spectra.md) discusses how to compute broadband spectra from TDKS simulations of electron dynamics.
Section [7.4.4](sec_TDKS_HHG_Spectra.md) discusses how to compute high-harmonic generation (HHG) spectra from TDKS simulations
of electron dynamics.

TDKS

### `TDKS`

> **Job control keyword to turn on TDKS calculation**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Perform a TDKS calculation following a ground-state SCF calculation
>     * FALSE
>     * Do not perform a TDKS calculation
> * **Recommendation**: None.
