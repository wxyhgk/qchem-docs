---
title: "10.8.6 Resonance Raman intensities"
---

## 10.8.6 Resonance Raman intensities

(July 4, 2026)

The theory of resonance Raman spectroscopy is fully described by the Kramers-Heisenberg-Dirac dispersion formalism based on the Raman polarizability tensor[[677]](../bib_references/bib.md#bib704)

<a id="eq:SOS"></a>

$$
\alpha_{\sigma\tau}(\omega_{\text{L}},\omega_{\text{S}})=\sum_{\upsilon}\left[\frac{\langle f|\hat{r}_{\sigma}|\upsilon\rangle\langle\upsilon|\hat{r}_{\tau}|i\rangle}{\hbar\omega_{\text{L}}-\hbar\omega_{\upsilon i}+i\Gamma_{i\upsilon}}+\frac{\langle f|\hat{r}_{\tau}|\upsilon\rangle\langle\upsilon|\hat{r}_{\sigma}|i\rangle}{\hbar\omega_{\upsilon i}+\hbar\omega_{\text{S}}+i\Gamma_{i\upsilon}}\right] \tag{10.74}
$$

between initial state $|i\rangle$ and final state $|f\rangle$. Here, $\omega_{\text{L}}$ and $\omega_{\text{S}}$ are the frequencies of the laser (incident photon) and of the scattered photon, respectively. Eq. ([10.74](#eq:SOS)) is inconvenient due to the sum over intermediate states $\upsilon$ (vibrational levels on all accessible
electronic states), and the usual procedure is to expand the static molecular polarizability as a Taylor series in the normal coordinates,[[35]](../bib_references/bib.md#bib18)
 which allows the Raman intensity to be decomposed into Franck–Condon (or “$A$-term”) contributions and
coordinate-dependent Herzberg–Teller (“$B$”- and “$C$”-term) contributions.[[35]](../bib_references/bib.md#bib18)

Nevertheless, each term contains sums over intermediate vibrational states and becomes difficult to evaluate for large
molecules with numerous vibrational modes.

As such, in most cases only the lowest-lying Raman-active excited electronic state
is considered in computing the RR spectrum. In principle one should consider the effects of Duschinsky rotation,[[1246]](../bib_references/bib.md#bib1299)
*i.e.*,
the fact that the normal modes are different in each electronic state. Neglecting this effect for simplicity and thus using
ground-state normal modes only, one arrives at the “independent-mode, displaced harmonic oscillator” (IMDHO) model,[[1082]](../bib_references/bib.md#bib1127)

in which resonant enhancements to the vibrational intensities (for modes 1 and 2, say)
are expressed as ratios[[552]](../bib_references/bib.md#bib563)

<a id="eq:RR_intens"></a>

$$
\frac{I_{1}}{I_{2}}\approx\left(\frac{\omega^{\rm g}_{1}\Delta_{1}}{\omega^{\rm g}_{2}\Delta_{2}}\right)^{\!2}\;. \tag{10.75}
$$

In this equation, $\omega_{1}^{\text{g}}$ and $\omega_{2}^{\text{g}}$ represent the ground-state vibrational frequencies for normal modes
$Q_{1}$ and $Q_{2}$ and $\omega$ is the electronic excitation energy. The first equality in Eq. ([10.75](#eq:RR_intens)), written as
an approximation here, is exact within the IMDHO model. The quantity

<a id="eq:Delta_k"></a>

$$
\Delta_{k}=\left(\frac{\omega_{k}}{\hbar}\right)^{1/2}\Delta Q_{k} \tag{10.76}
$$

evaluated at the ground-state geometry ($\mathbf{Q}=\bm{0}$),
is the slope of the excited-state potential energy surface along mode $k$.
This leads to the second equality in Eq. ([10.75](#eq:RR_intens)).

The time-dependent picture provides means to derive this expression.[[552]](../bib_references/bib.md#bib563)
 In this approach,
the requisite polarizability tensor elements involving different electronic states are expressed as the Fourier transformation of the
time-evolving overlap between initial- and final-state electronic wave functions:

<a id="Ch10.E77"></a>

$$
\alpha(\omega_{\text{L}})\propto\int_{0}^{\infty}e^{i\omega_{\text{L}}t-\Gamma
t}\langle\psi_{f}|\psi_{i}(t)\rangle dt+\text{NRT}\;. \tag{10.77}
$$

Here, “NRT” indicates the non-resonant terms that are neglected in RR spectroscopy. Large molecules likely spend no more
than 10–20 fs in the Franck-Condon region and the overlap integral is likely only significant on that timescale.[[552]](../bib_references/bib.md#bib563)

Within a model that considers only two electronic states, the RR intensity that one obtains is

<a id="eq:functional"></a>

$$
I_{k}\propto\omega_{\text{L}}(\omega_{\text{L}}-\omega_{k})^{3}(\omega_{k}\Delta_{k})^{2}\; \tag{10.78}
$$

where $\mu_{k}$ is the reduced mass of the $k$th normal mode.

Assuming identical force constants for $Q_{k}$ in both the ground and excited electronic state, one obtains
a linear transformation between the displacement $\Delta_{k}$ of the equilibrium position of this mode, expressed
in normal coordinates, and the displacements $\widetilde{\Delta}_{i}$ expressed in Cartesian coordinates:

<a id="Ch10.E79"></a>

$$
\widetilde{\Delta}_{i}=\sum_{k=1}^{3N-6}\left(\frac{L_{ik}}{m_{i}^{1/2}}\right)\Delta_{k}\;. \tag{10.79}
$$

In matrix form this is

<a id="Ch10.E80"></a>

$$
\mathbf{\Delta}_{Q}=\lambda^{-1}\mathbf{L}^{\dagger}\mathbf{M}^{1/2}\mathbf{V}_{X} \tag{10.80}
$$

where $\lambda$ is the eigenvalues of mass-weighted Hessian matrix, M defines the matrix of atomic masses and $V_{X}$ is the energy gradient in Cartesian coordinate
Raman intensities are related to the dimensionless displacements

<a id="Ch10.E81"></a>

$$
\Delta_{k}=\left(\frac{\lambda_{k}}{m_{e}}\right)^{\!1/4}\Delta_{Qk}\;. \tag{10.81}
$$

Setting JOBTYPE = RRAMAN invokes the calculation of resonance Raman intensities.

RR_NO_NORMALISE

### `RR_NO_NORMALISE`

> **Controls whether frequency job calculates resonance Raman intensities**
>
> * **Type**: `LOGICAL`
> * **Default**: `False`
> * **Options**:
>     * False
>     * Normalize RR intensities
>     * True
>     * Do not normalize RR intensities
> * **Recommendation**: False

???+ example "Example 10.44: Calculating resonance Raman intensities."
    ```qchem
    $molecule
       0 1
       C     1.8288506578   -0.1219336002    0.0000000000
       C     0.6155951063    0.3987918905    0.0000000000
       C    -0.6155955606   -0.3987931260    0.0000000000
       C    -1.8288502653    0.1219348794    0.0000000000
       H     2.7085214046    0.4909328271    0.0000000000
       H     1.9881851899   -1.1843222290    0.0000000000
       H     0.4885913610    1.4671254626    0.0000000000
       H    -0.4885933454   -1.4671268234    0.0000000000
       H    -1.9881816088    1.1843239478    0.0000000000
       H    -2.7085226822   -0.4909289672    0.0000000000
    $end
    
    $rem
       JOBTYPE                RRAMAN
       METHOD                 hf
       BASIS                  3-21G
       CIS_N_ROOTS            1
       CIS_STATE_DERIVATIVE   1
    $end
    ```
