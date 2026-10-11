---
title: "6.21.2 Theory"
---

## 6.21.2 Theory

(July 4, 2026)

Electronic energy is retrieved by iFCI using an $n$-body expansion of the form

<a id="eqn:mbe"></a>
$$
E=E_{\mathrm{ref}}+E_{C}=E_{\mathrm{ref}}+\sum_{i}\epsilon_{i}+\sum_{j<i}\epsilon_{ij}+\sum_{k<j<i}\epsilon_{ijk}+\cdots \tag{6.96}
$$

where each $\epsilon_{X}$ term denotes an increment of correlation energy and
$i,j,k$ refer to bodies of the expansion. Incremental correlation energies are
defined as

<a id="A3.S8.EGx35"></a>
$$
\displaystyle\epsilon_{i} \tag{6.97}
$$

where terms $n>1$ subtract lower-order increments to avoid double counting.
Terms represent $n$-body additions to the correlation energy from $2n$
electrons in the mean field of the remaining $2(N-n)$ electrons, where each
$\epsilon_{X}$ value is computed by solving CAS-CI for $2n$ electrons in $N_{v}+n$
orbitals. For example, $n=1$ performs CAS($2,N_{v}+1$)-CI to give the value of
$E_{C}(i)=E(\mathrm{CAS}(2,N_{v}+1))$. Proceeding likewise for higher $n$,
CAS($2n,N_{v}+n$)-CI produces each $E_{C}(X)$.

Heat-bath CI (HBCI) is utilized to solve each CAS-CI Hamiltonian, performing
selected CI computations according to determinants, $j$, coupled to the CI wave
function in the form $|H_{ij}c_{i}|>\varepsilon_{i}$, where $\varepsilon_{i}$ is the
energy cutoff and $c_{i}$ are determinants in the HBCI subspace.

Truncation of incremental terms is performed by considering natural orbital
(NO) occupancy cutoffs, $\eta^{(m)}$, where

<a id="A3.S8.EGx36"></a>
$$
\displaystyle\epsilon_{i}^{(m)} \tag{6.100}
$$

Doing so reduces the size of the virtual space by only including virtual orbitals
with sufficiently large NO eigenvalues. Convergence for each iFCI increment is
reached when

<a id="eqn:ifcizeta"></a>
$$
\zeta>|\epsilon^{(m+1)}-\epsilon^{m}| \tag{6.102}
$$

with units of $10^{-\zeta}$ E${}_{\mathrm{h}}$. Further truncation in $n\geq 3$ can be
performed by utilizing the $\zeta$ parameter and a screening cutoff,
$\mathcal{C}_{n}$, in the form

<a id="eqn:ifcicutoff"></a>
$$
\mathcal{C}_{n}=10^{-\zeta}\times\mathcal{S}_{n} \tag{6.103}
$$

where $\mathcal{C}_{n}$ is in E${}_{\mathrm{h}}$ and $\mathcal{S}_{n}$ is a scalar. This screening
is performed by selecting $n-1$ body correlation energy contributions that are
above $\mathcal{C}_{n}$. See Ref. [[1148]](../bib_references/bib.md#bib1200)
 for more details. $\mathcal{S}_{n}$
is a parameter in the input.

iFCI requires a high-spin perfect pairing (PP) reference, where NOs are
localized as local bonding-antibonding pairs, or geminals.
