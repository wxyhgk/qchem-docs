---
title: "6.3.1 Overview"
---

## 6.3.1 Overview

(July 4, 2026)

Møller-Plesset Perturbation Theory[[957]](../bib_references/bib.md#bib998)
 is a widely used
method for approximating the correlation energy of molecules. In particular,
second-order Møller-Plesset perturbation theory (MP2) is one of the
simplest and most useful levels of theory beyond the Hartree-Fock
approximation. Conventional and local MP2 methods available in **Q-Chem** are
discussed in detail in Sections [6.4](sect_exactmp.md) and [6.5](topic_lmp2.md)
respectively. The MP3 method is still occasionally used, while MP4 calculations
are quite commonly employed as part of the G2 and G3 thermochemical
methods.[[296]](../bib_references/bib.md#bib297)
 In the remainder of this section, the
theoretical basis of Møller-Plesset theory is reviewed.

The Hartree-Fock wave function $\Psi_{0}$ and energy $E_{0}$ are
*approximate* solutions (eigenfunction and eigenvalue) to the exact
Hamiltonian eigenvalue problem or Schrödinger’s electronic wave equation,
Eq. ([4.5](../ch04_scf/Ch4.S2.SS1.md#eq404)). The HF wave function and energy are, however, exact solutions for the
Hartree-Fock Hamiltonian $H_{0}$ eigenvalue problem. If we assume that the
Hartree-Fock wave function $\Psi_{0}$ and energy $E_{0}$ lie near the exact wave
function $\Psi$ and energy $E$, we can now write the exact Hamiltonian
operator as

<a id="eq500"></a>

$$
H=H_{0}+\lambda V \tag{6.1}
$$

where $V$ is the small perturbation and $\lambda$ is a dimensionless parameter.
Expanding the exact wave function and energy in terms of the HF wave function
and energy yields

<a id="eq501"></a>

$$
E=E^{(0)}+\lambda E^{(1)}+\lambda^{2}E^{(2)}+\lambda^{3}E^{(3)}+\ldots \tag{6.2}
$$

and

<a id="eq02"></a>

$$
\Psi=\Psi_{0}+\lambda\Psi^{(1)}+\lambda^{2}\Psi^{(2)}+\lambda^{3}\Psi^{(3)}+\ldots \tag{6.3}
$$

Substituting these expansions into the Schrödinger equation and collecting terms according
to powers of $\lambda$ yields

<a id="eq503"></a>

$$
H_{0}\Psi_{0}=E^{(0)}\Psi_{0} \tag{6.4}
$$

<a id="eq504"></a>

$$
H_{0}\Psi^{(1)}+V\Psi_{0}=E^{(0)}\Psi^{(1)}+E^{(1)}\Psi_{0} \tag{6.5}
$$

<a id="eq505"></a>

$$
H_{0}\Psi^{(2)}+V\Psi^{(1)}=E^{(0)}\Psi^{(2)}+E^{(1)}\Psi^{(1)}+E^{(2)}\Psi_{0} \tag{6.6}
$$

and so forth. Multiplying each of the above equations by $\Psi_{0}$ and
integrating over all space yields the following expression for the $n$th-order
(MP$n$) energy:

<a id="eq506"></a>

$$
E^{(0)}=\langle{\Psi_{0}}|H_{0}|{\Psi_{0}}\rangle \tag{6.7}
$$

<a id="eq507"></a>

$$
E^{(1)}=\langle{\Psi_{0}}|V|{\Psi_{0}}\rangle \tag{6.8}
$$

<a id="eq508"></a>

$$
E^{(2)}=\left\langle{\Psi_{0}}|V|{\Psi^{(1)}}\right\rangle \tag{6.9}
$$

Thus, the Hartree-Fock energy

<a id="eq509"></a>

$$
E_{0}=\left\langle{\Psi_{0}}\right|H_{0}+V\left|{\Psi_{0}}\right\rangle \tag{6.10}
$$

is simply the sum of the zeroth- and first- order energies

<a id="eq510"></a>

$$
E_{0}=E^{(0)}+E^{(1)} \tag{6.11}
$$

The correlation energy can then be written

<a id="eq511"></a>

$$
E_{\mathrm{corr}}=E_{0}^{(2)}+E_{0}^{(3)}+E_{0}^{(4)}+\ldots \tag{6.12}
$$

of which the first term is the MP2 energy.

It can be shown that the MP2 energy can be written (in terms of spin-orbitals) as

<a id="eq512"></a>

$$
E_{0}^{(2)}=-\frac{1}{4}\sum_{ab}^{\mathrm{virt}}{\sum_{ij}^{\mathrm{occ}}{\frac{\left|{\left\langle{ab}\right|\left|{ij}\right\rangle}\right|^{2}}{\varepsilon_{a}+\varepsilon_{b}-\varepsilon_{i}-\varepsilon_{j}}}} \tag{6.13}
$$

where

<a id="eq513"></a>

$$
\left\langle ab||ij\right\rangle=\left\langle ab|ij\right\rangle-\left\langle
ab|ji\right\rangle \tag{6.14}
$$

and

<a id="eq514"></a>

$$
\left\langle{ab}|{cd}\right\rangle=\int\int\psi_{a}(\mathbf{r}_{1})\psi_{c}(\mathbf{r}_{1})\frac{1}{r_{12}}\psi_{b}(\mathbf{r}_{2})\psi_{d}(\mathbf{r}_{2})d\mathbf{r}_{1}d\mathbf{r}_{2} \tag{6.15}
$$

which can be written in terms of the two-electron repulsion integrals

<a id="eq515"></a>

$$
\left\langle{ab}|{cd}\right\rangle=\sum_{\mu}\sum_{\nu}\sum_{\lambda}\sum_{\sigma}C_{\mu a}C_{\nu c}C_{\lambda b}C_{\sigma d}\left(\mu\nu|\lambda\sigma\right) \tag{6.16}
$$

Expressions for higher order terms follow similarly, although with much greater
algebraic and computational complexity. MP3 and particularly MP4 (the third and
fourth order contributions to the correlation energy) are both occasionally
used, although they are increasingly supplanted by the coupled-cluster methods
described in the following sections. The disk and memory requirements for MP3
are similar to the self-consistent pair correlation methods discussed in
Section [6.12](topic_ccsd.md) while the computational cost of MP4 is similar to the
(T) corrections discussed in Section [6.13](topic_ccni.md).
