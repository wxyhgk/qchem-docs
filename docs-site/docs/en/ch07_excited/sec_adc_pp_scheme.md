---
title: "7.10.2 The Algebraic Diagrammatic Construction (ADC) Scheme"
---

## 7.10.2 The Algebraic Diagrammatic Construction (ADC) Scheme

(July 4, 2026)

The Algebraic Diagrammatic Construction (ADC) of the polarization
propagator is an excited state method originating from Green’s function theory.
It has first been derived employing the diagrammatic perturbation expansion of
the polarization propagator using the Møller-Plesset partition of the
Hamiltonian.[[1210]](../bib_references/bib.md#bib1262)
 An alternative derivation is available in
terms of the intermediate state representation (ISR),[[1209]](../bib_references/bib.md#bib1264)
 which
will be presented in the following.

As starting point for the derivation of ADC equations via ISR serves the exact
N electron ground state $\left|\Psi_{0}^{N}\right>$. From $\left|\Psi_{0}^{N}\right>$ a
complete set of correlated excited states is obtained by applying physical
excitation operators $\hat{C}_{J}$.

<a id="eq:adc_pp_precursor_states"></a>

$$
\left|\bar{\Psi}_{J}^{N}\right>=\hat{C}_{J}\left|\Psi_{0}^{N}\right> \tag{7.133}
$$

with

<a id="eq:adc_pp_excitation_operator"></a>

$$
\left\{\hat{C}_{J}\right\}=\left\{c^{\dagger}_{a}c_{i};c^{\dagger}_{a}c^{\dagger}_{b}c_{i}c_{j},i<j,a<b;\ldots\right\} \tag{7.134}
$$

Yet, the resulting excited states do not form an orthonormal basis. To
construct an orthonormal basis out of the $|\bar{\Psi}_{J}^{N}\rangle$ the
Gram-Schmidt orthogonalization scheme is employed successively on the excited
states in the various excitation classes starting from the exact ground state,
the singly excited states, the doubly excited states *etc.*. This procedure
eventually yields the basis of intermediate states
$\{|\tilde{\Psi}_{J}^{N}\rangle\}$ in which the Hamiltonian of the system can be
represented forming the Hermitian ADC matrix

<a id="Ch7.E135"></a>

$$
M_{IJ}=\left<\tilde{\Psi}_{I}^{N}\right|\hat{H}-E_{0}^{N}\left|\tilde{\Psi}_{J}^{N}\right> \tag{7.135}
$$

Here, the Hamiltonian of the system is shifted by the exact ground state
energy $E_{0}^{N}$. The solution of the secular ISR equation

<a id="Ch7.E136"></a>

$$
\mathbf{M}\mathbf{X}=\mathbf{X}\mathbf{\Omega},\;\;\text{ with }\;\;\mathbf{X}^{\dagger}\mathbf{X}=\mathbf{1} \tag{7.136}
$$

yields the exact excitation energies $\Omega_{n}$ as eigenvalues. From the
eigenvectors the exact excited states in terms of the intermediate states can
be constructed as

<a id="Ch7.E137"></a>

$$
\left|\Psi_{n}^{N}\right>=\sum_{J}X_{nJ}\left|\tilde{\Psi}_{J}^{N}\right> \tag{7.137}
$$

This also allows for the calculation of dipole transition moments via

<a id="Ch7.E138"></a>

$$
T_{n}=\left<\Psi_{n}^{N}\right|\hat{\mu}\left|\Psi_{0}^{N}\right>=\sum_{J}X_{nJ}^{\dagger}\left<\tilde{\Psi}_{J}^{N}\right|\hat{\mu}\left|\Psi_{0}^{N}\right>, \tag{7.138}
$$

as well as excited state properties via

<a id="Ch7.E139"></a>

$$
O_{n}=\left<\Psi_{n}^{N}\right|\hat{o}\left|\Psi_{n}^{N}\right>=\sum_{I,J}X_{nI}^{\dagger}X_{nJ}\left<\tilde{\Psi}_{I}^{N}\right|\hat{o}\left|\Psi_{J}^{N}\right>, \tag{7.139}
$$

where $O_{n}$ is the property associated with operator $\hat{o}$.

Up to now, the exact $N$-electron ground state has been employed in the
derivation of the ADC scheme, thereby resulting in exact excitation energies
and exact excited state wave functions. Since the exact ground state is usually
not known, a suitable approximation must be used in the derivation of the ISR
equations. An obvious choice is the $n$th order Møller-Plesset ground state
yielding the $n$th order approximation of the ADC scheme. The appropriate
ADC equations have been derived in detail up to third order.[[1371]](../bib_references/bib.md#bib1432)

Due to the dependency on
the Møller-Plesset ground state the $n$th order ADC scheme should only
be applied to molecular systems whose ground state is well described by the
respective MP($n$) method.

As in Møller-Plesset perturbation theory, the first ADC scheme which goes
beyond the non-correlated wave function methods in Section [7.2](sect_noncorr.md)
is ADC(2). ADC(2) is available in a *strict* and an *extended*
variant which are usually referred to as ADC(2)-s and
ADC(2)-x, respectively. The strict variant ADC(2)-s
scales with the 5th power of the basis set. The quality of ADC(2)-s
excitation energies and corresponding excited states is comparable to the
quality of those obtained with CIS(D) (Section [7.8](sect_excorr.md)) or CC2. More
precisely, excited states with mostly single excitation character are
well-described by ADC(2)-s, while excited states with double
excitation character are usually found to be too high in energy. The
ADC(2)-x variant which scales as the sixth power of the basis set
improves the treatment of doubly excited states, but at the cost of introducing
an imbalance between singly and doubly excited states. As result, the
excitation energies of doubly excited states are substantially decreased in
ADC(2)-x relative to the states possessing mostly single excitation
character with the excitation energies of both types of states exhibiting
relatively large errors. Still, ADC(2)-x calculations can be used
as a diagnostic tool for the importance doubly excited states in the low-energy
region of the spectrum by comparing to ADC(2)-s results. A
significantly better description of both singly and doubly excited states is
provided by the third order ADC scheme ADC(3). The accuracy of excitation
energies obtained with ADC(3) is almost comparable to CC3, but at computational
costs that scale with the sixth power of the basis set only.[[528]](../bib_references/bib.md#bib542)
