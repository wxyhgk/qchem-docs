---
title: "6.12.4 Second-Order Approximate Coupled Cluster Singles and Doubles (CC2)"
---

## 6.12.4 Second-Order Approximate Coupled Cluster Singles and Doubles (CC2)

(July 4, 2026)

The equations for the second-order approximate coupled cluster singles and doubles model (CC2) [[249]](../bib_references/bib.md#bib250)

are similar to the CCSD equations with the doubles amplitude equations approximated as:

<a id="Ch6.E70"></a>

$$
E_{\mathrm{CC2}}=\langle\Phi_{0}\left|\hat{H}\exp\left(\hat{T}_{1}+\hat{T}_{2}\right)\right|\Phi_{0}\rangle \tag{6.70}
$$

<a id="Ch6.E71"></a>

$$
0=\left\langle{\Phi_{i}^{a}\left|{\bar{H}}+\left[{\bar{H}},\hat{T}_{2}\right]\right|\Phi_{0}}\right\rangle \tag{6.71}
$$

<a id="Ch6.E72"></a>

$$
0=\left\langle{\Phi_{ij}^{ab}\left|{\bar{H}}+\left[\hat{F},\hat{T}_{2}\right]\right|\Phi_{0}}\right\rangle \tag{6.72}
$$

where the similarity-transformed Hamiltonian with the exponential function of the
single excitation cluster operator is given by:

<a id="Ch6.E73"></a>

$$
\bar{H}=\exp\left(-\hat{T}_{1}\right)\hat{H}\exp\left(\hat{T}_{1}\right) \tag{6.73}
$$

CC2 energies are available in **Q-Chem**, and are requested by setting the keyword METHOD to CC2 or EOM-CC2. CC2 and MP2 ground state energies and properties are of similar quality, but CC2 can be efficiently combined with the EOM formalism to treat excited/electron attached/ionized/… states.
When used with resolution-of-identity (RI; see Section [6.12.10](topic_ricc.md)), RI-CC2 can be applied to large systems.
RI-CC2 can be used either via CCMAN2 or via **libgmbpt**;
Section [7.9.4](../ch07_excited/sec_eomcc2.md) provides a guide for setting up CC2 and EOM-CC2 calculations.
