---
title: "6.8.1 Introduction"
---

## 6.8.1 Introduction

(July 4, 2026)

While second-order Møller-Plesset perturbation theory (MP2)
offers the simplest and most cost-effective *ab initio* correlation energy,
it requires a separate formulation for degenerate states
because the MP2 energy diverges in the zero-gap limit.
Second-order Brillouin-Wigner perturbation theory (BW2) requires
no such reformulation, as the second-order energy given by,

<a id="Ch6.E33"></a>
$$
E_{\text{c}}^{(2)}=-\frac{1}{4}\sum\limits_{ijab}\frac{|\langle ij||ab\rangle|^{2}}{\Delta_{ij}^{ab}+E_{\text{c}}^{(2)}} \tag{6.33}
$$

is finite when the orbital energy gap $\Delta_{ij}^{ab}=\varepsilon_{a}+\varepsilon_{b}-\varepsilon_{i}-\varepsilon_{j}$ is zero due to the presence of the correlation energy
in the denominator.
However, the BW2 correlation energy is not size-consistent
in the sense that it does not satisfy
$E(A\cup B)=E(A)+E(B)$ for two distant, noninteracting subsystems
A and B, severely limiting its applicability to chemistry.

Recently, Carter-Fenk and Head-Gordon introduced a size-consistent-to-second-order
Brillouin-Wigner perturbation theory (BW-s2)
that retains this essential property while remaining
finite for zero-gap systems.[[195]](../bib_references/bib.md#bib196)

This theory, based on a repartitioning of the zeroth-order Hamiltonian,
results in a slightly-modified amplitude equation. Whereas
the MP2 amplitudes can be found by solving,

<a id="Ch6.E34"></a>
$$
\Delta_{ijkl}^{abcd}\cdot t_{kl}^{cd}=-\langle ij||ab\rangle\;, \tag{6.34}
$$

the BW-s2 amplitude equation contains a regularizing tensor,

<a id="Ch6.E35"></a>
$$
\big{(}\Delta_{ijkl}^{abcd}+R_{ijkl}^{abcd}\big{)}\cdot t_{kl}^{cd}=-\langle ij||ab\rangle \tag{6.35}
$$

In the above equations $\Delta_{ijkl}^{abcd}$ is
composed of Fock matrix elements and reduces to
the familiar $\Delta_{ij}^{ab}$ when canonical orbitals are used,
and

<a id="eq:Rtensor"></a>
$$
R_{ijkl}^{abcd}=\frac{\alpha}{2}\big{(}W_{ik}\delta_{jl}+\delta_{ik}W_{jl}\big{)}\delta_{ac}\delta_{bd} \tag{6.36}
$$

where,

<a id="Ch6.E37"></a>
$$
W_{ij}=\frac{1}{2}\sum\limits_{kab}\big{(}t_{ik}^{ab}\langle jk||ab\rangle+t_{jk}^{ab}\langle ik||ab\rangle\big{)} \tag{6.37}
$$

This form of $\mathbf{W}$ was chosen because it is size-consistent, leading to a
size-consistent BW-s2 correlation energy.
Physically, $\mathbf{W}$ represents the correlation energy of a Koopmans’ (static orbital)
ionization process. Thus, the occupied orbitals in BW-s2
are imbued with correlation such that the occupied/virtual gap increases.
After rotating the occupied orbitals into a basis where $\bm{\Delta}+\bm{R}$ is
diagonal, the BW-s2 working equation looks like that of MP2,

<a id="Ch6.E38"></a>
$$
E_{\text{c}}^{(2)}=-\frac{1}{4}\sum\limits_{ijab}\frac{|\widetilde{\langle ij||ab\rangle}|^{2}}{\varepsilon_{a}+\varepsilon_{b}-\tilde{\varepsilon}_{i}-\tilde{\varepsilon}_{j}} \tag{6.38}
$$

but the orbitals and corresponding anti-symmetrized two-electron integrals have
been rotated into the new basis.

In equation [6.36](#eq:Rtensor) there is an implicit parameter $\alpha$
that controls the regularization strength.
Initially, this parameter was set to $\alpha=1$ to obtain the exact
result for the two-electron two-orbital system of minimal-basis H${}_{\text{2}}$
at the dissociation limit,
but $\alpha$ was later tuned to achieve much more accurate results
for a wide array of chemical problems ranging from thermochemical properties
to noncovalent interaction energies and closed-shell transition-metal
reaction energies.[[201]](../bib_references/bib.md#bib197)

The optimal $\alpha$ value for the resultant BW-s2($\alpha$) approach
varies somewhat between chemical problems,
but was found to be more flexible than gap-dependent regularizer parameters
like $\kappa$-, $\sigma$-, or $\sigma^{2}$-MP2.
A “universal” parameter of $\alpha=4$ was suggested as a compromise to achieve
the best all-around results for a wide array of chemical
properties.[[201]](../bib_references/bib.md#bib197)
