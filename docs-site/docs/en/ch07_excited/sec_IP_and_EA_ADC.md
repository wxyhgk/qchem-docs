---
title: "7.10.3 IP- and EA-ADC"
---

## 7.10.3 IP- and EA-ADC

(July 4, 2026)

Similar to ADC scheme of the polarization propagator (ADC), the procedure can also be applied to
the $(N-1)$- and $(N+1)$-parts of the electron propagator, which is given in its spectral
representation as

<a id="Ch7.E140"></a>
$$
G_{pq}(\omega)=\underbrace{\sum_{n}\frac{\bigl{\langle}\Psi_{0}^{N}\bigl{\lvert}c_{p}\bigr{\rvert}\Psi_{n}^{N+1}\bigr{\rangle}\bigl{\langle}\Psi_{n}^{N+1}\bigl{\lvert}c_{q}^{\dagger}\bigr{\rvert}\Psi_{0}^{N}\bigr{\rangle}}{\omega+E_{0}^{N}-E_{n}^{N+1}}}_{(N+1)\text{-electron (EA) part}}+\underbrace{\sum_{n}\frac{\bigl{\langle}\Psi_{0}^{N}\bigl{\lvert}c_{q}^{\dagger}\bigr{\rvert}\Psi_{n}^{N-1}\bigr{\rangle}\bigl{\langle}\Psi_{n}^{N-1}\bigl{\lvert}c_{p}\bigr{\rvert}\Psi_{0}^{N}\bigr{\rangle}}{\omega+E_{n}^{N-1}-E_{0}^{N}}}_{(N-1)\text{-electron (IP) part}}. \tag{7.140}
$$

Doing so, the (non-Dyson) IP- and EA-ADC methods up to third order of perturbation theory
have been derived.[[1208]](../bib_references/bib.md#bib1263)

As in the case of the ADC scheme of the polarization propagator, the derivation of the
same working equations is possible via the ISR formalism, the only difference to the
procedure shown in the previous section [7.10.2](sec_adc_pp_scheme.md) being the excitation
operators

<a id="A3.S8.EGx63"></a>
$$
\displaystyle\left\{\hat{C}_{J}^{N-1}\right\} \tag{7.141}
$$

replacing the electron number-conserving one $\hat{C}_{J}$ in
Eq. ([7.133](sec_adc_pp_scheme.md#eq:adc_pp_precursor_states)).

Diagonalization of the IP- and EA-ADC secular matrices $\mathbf{M}$ yields
electron-detachment energies (or ionization potentials, IPs) and
electron-attachment energies (or negative electron affinities, EAs),
respectively. In
addition, relative spectral intensities of $(N-1)$- and
$(N+1)$-transitions are accessible as pole strengths $P_{n}$, which
are computed according to

<a id="Ch7.E143"></a>
$$
P_{n}=\sum_{p}\left|x_{pn}\right|^{2}, \tag{7.143}
$$

where the $x_{pn}$ are the spectroscopic factors computed by means of the IP- and
EA-ADC eigenvectors $\mathbf{X}$ and the matrix of
effective transition amplitudes $\mathbf{f}$ using the relations

<a id="A3.S8.EGx64"></a>
$$
\displaystyle x_{pn}^{N-1} \tag{7.144}
$$

When requesting electron-detached or electron-attached states, the pole
strengths are automatically computed. For IP- and EA-ADC(2) calculations,
second-order pole strengths are used [*i.e.*, the IP- and EA-ADC(2) $\mathbf{f}$
matrix is employed in their computation]. As suggested
in Ref. [[1208]](../bib_references/bib.md#bib1263)
, for computational reasons the same second-order pole
strengths are computed in case of strict IP- and EA-ADC(3) calculations, *i.e.*,
using the second-order ground state density throughout the $\mathbf{M}$ matrix
equations, ADC_DENSITY_ORDER = 2. When requesting a higher-order
ground state density to be used, *e.g.*, by setting
ADC_DENSITY_ORDER = 3 (corresponding to the $\Sigma(4)$
scheme[[1372]](../bib_references/bib.md#bib1435)
) or ADC_DENSITY_ORDER = 4 (corresponding
to the $\Sigma(4+)$ scheme,[[1372]](../bib_references/bib.md#bib1435)
 also denoted as standard IP-
and EA-ADC(3) schemes), the corresponding pole
strengths are used, *i.e.*, third-order pole strenghts in case of $\Sigma(4)$
and improved third-order pole strengths in case of $\Sigma(4+)$.

The spectroscopic factors also allow for computing the Dyson orbitals
$|\phi_{n}\rangle$
connected to electron detachment and attachment processes

<a id="Ch7.E146"></a>
$$
\left|\phi_{n}\right>=\sum_{p}x_{pn}\left|\varphi_{p}\right>, \tag{7.146}
$$

where in the latter relation the $\varphi_{p}$ denote HF orbitals. Dyson
orbital output is triggered by
ADC_DO_DYSON = TRUE together with
STATE_ANALYSIS = TRUE. Also see Section [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md) for
further details.
