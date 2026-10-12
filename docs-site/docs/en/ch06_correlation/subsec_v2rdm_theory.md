---
title: "6.23.2 Theory"
---

## 6.23.2 Theory

(July 4, 2026)

The electronic energy is an exact functional of the 1-RDM and 2-RDM

<a id="eq:v2rdm:energy"></a>

$$
E=\frac{1}{2}\sum_{pqrs}{}^{2}D^{pq}_{rs}(pr|qs)+\sum_{pq}{}^{1}D^{p}_{q}h_{pq}, \tag{6.106}
$$

where the 1-RDM (${}^{1}\mathbf{D}$) and 2-RDM are represented in a given
spin-orbital basis indexed by $p$, $q$, $r$, and $s$. The one-hole RDM
(${}^{1}\mathbf{Q}$), two-hole RDM (${}^{2}\mathbf{Q}$), particle-hole RDM
(${}^{2}\mathbf{G}$), partial three-particle RDMs ($\mathbf{T1}$ and $\mathbf{T2}$),
and full three-particle RDMs (${}^{3}\mathbf{D}$, ${}^{3}\mathbf{Q}$, ${}^{3}\mathbf{E}$,
${}^{3}\mathbf{F}$) are linear functions of ${}^{1}\mathbf{D}$ and
${}^{2}\mathbf{D}$.[[399]](../bib_references/bib.md#bib408)
 Minimizing the electronic energy with
respect to ${}^{2}\mathbf{D}$ while enforcing the linear relations among these
RDMs, the contraction and spin constraints placed on ${}^{2}\mathbf{D}$, and
the positive semidefinite property of all RDMs constitutes a semidefinite
program (SDP). The current v2RDM implementation uses a boundary-point SDP
(BPSDP) algorithm to solve the
SDP.[[1120]](../bib_references/bib.md#bib1167)

The primal formulation of the SDP is

<a id="A3.S8.EGx37"></a>

$$
\displaystyle E_{\rm primal} \tag{6.107}
$$

Here, $\mathbf{x}$ represents the primal solution vector, the vector $\mathbf{c}$
contains all information defining the quantum system (the one- and
two-electron integrals), and the mapping $M(\mathbf{x})$ maps the primal
solution onto the set of positive semidefinite RDMs:

<a id="eqn:vectormatrixmap"></a>

$$
M({\bf x})=\left(\begin{array}[]{cccc}{}^{1}{\mathbf{D}}&0&0&0\\
0&{}^{1}{\mathbf{Q}}&0&0\\
0&0&{}^{2}{\mathbf{D}}&0\\
0&0&0&{}\ddots\\
\end{array}\right)\succeq 0. \tag{6.108}
$$

Additional RDMs can be included in $M(\mathbf{x})$, depending on the choice
of N-representability conditions applied.
The action of the constraint matrix, ${\mathbf{A}}$, on ${\mathbf{x}}$ is a compact
representation of the $N$-representability conditions. ${\mathbf{A}}$ maintains
the appropriate mappings between each block of $M({\mathbf{x}})$ and enforces
the appropriate spin and contraction conditions. Alternatively, one could
consider the dual formulation of the semidefinite problem, expressed as

<a id="A3.S8.EGx38"></a>

$$
\displaystyle E_{\rm dual} \tag{6.109}
$$

where ${\mathbf{y}}$ and ${\mathbf{z}}$ are the dual solutions, and $M({\mathbf{z}})$ is
constrained to be positive semidefinite.

The BPSDP algorithm involves an iterative two-step procedure:

1. Solve $\mathbf{AA}^{T}\mathbf{y}=\mathbf{A}(\mathbf{c}-\mathbf{z})+\tau\mu(\mathbf{b}-\mathbf{A}\mathbf{x})$
for $\mathbf{y}$ by conjugate gradient methods.
2. Update $\mathbf{x}$ and $\mathbf{z}$ by separating $\mathbf{U}=M(\mu\mathbf{x}+\mathbf{A}^{T}\mathbf{y}-\mathbf{c})$ into its positive and negative components (by
diagonalization). The updated primal and dual solutions $\mathbf{x}$ and
$\mathbf{z}$ are given by $M(\mathbf{x})=\mathbf{U}(+)/\mu$ and $M(\mathbf{z})=-\mathbf{U}(-)$.

Here, $\tau$ is a step-length parameter that lies in the interval [1.0,1.6]
[[930]](../bib_references/bib.md#bib968)
. The penalty parameter $\mu$ controls how strictly the
primal or dual constraints are enforced and is updated dynamically according to
the protocol outlined in Ref. [[930]](../bib_references/bib.md#bib968)
. The frequency with
which $\mu$ is updated is controlled by the *$rem* keyword
RDM_MU_UPDATE_FREQUENCY. The algorithm is considered converged when
the primal error $||\mathbf{A}\mathbf{x}-\mathbf{b}||$, the dual error $||\mathbf{A}^{T}\mathbf{y}-\mathbf{c}+\mathbf{z}||$, and the primal/dual energy gap $|E_{\rm primal}-E_{\rm dual}|$ are sufficiently small. The convergence in the primal/dual errors and
the primal/dual energy gap are controlled by the *$rem* keywords
RDM_EPS_CONVERGENCE and RDM_E_CONVERGENCE, respectively.
The BPSDP algorithm scales $n^{6}$ for the DQG conditions and $n^{9}$ for the T1,
T2, and 3POS conditions where $n$ is the number of active orbitals in the v2RDM
computation.

In v2RDM-CASSCF, the BPSDP algorithm is carried out to determine the 1- and
2RDM for a subset of active molecular orbitals. These orbitals are
optimized with respect to restricted doubly occupied / active and active /
external rotations after a chosen number of v2RDM iterations (Steps 1. and 2. above).
The frequency of this orbital optimization is controlled by
the *$rem* keyword RDM_ORBOPT_FREQUENCY.

Given converged 1- and 2-RDMs from a v2RDM-CASSCF calculation, an estimate of
the remaining correlation effects can be obtained through the formalism
of MC-PDFT. In MC-PDFT, the total energy for the system is expressed as

<a id="EQ:EMCPDFT"></a>

$$
E_{\rm MC-PDFT}=\sum_{i}h^{i}_{i}+\sum_{tu}h^{t}_{u}{}^{1}D^{t}_{u}+E_{\rm H}+E_{\rm XC}\left[\rho({\bf r}),\Pi({\bf r}),|\nabla\rho({\bf r})|,|\nabla\Pi({\bf r})|\right] \tag{6.110}
$$

where the Hartree energy, $E_{\rm H}$, is the classical Coulomb repulsion

<a id="EQN:HARTREE_ENERGY"></a>

$$
E_{\rm H}=\frac{1}{2}\sum_{ij}(ii|jj)+\sum_{itu}(tu|ii){}^{1}D^{t}_{u}+\frac{1}{2}\sum_{tuvw}(tu|vw){}^{1}D^{t}_{u}{}^{1}D^{v}_{w} \tag{6.111}
$$

and $E_{\rm xc}$ represents an on-top pair density functional.
In Eq. [6.111](#EQN:HARTREE_ENERGY), the labels $i$ and $j$ represent doubly occupied spin orbitals, and the labels $t$, $u$, $v$, and $w$
represent active spin orbitals. The symbols $\rho({\bf r})$ and $\Pi({\bf r})$ represent
the density and on-top pair density, respectively, which are defined in terms of the molecular orbitals $\{\phi\}$ as

<a id="Ch6.E112"></a>

$$
\rho({\bf r})=\sum_{pq}\phi_{p}({\bf r})\phi_{q}({\bf r}){}^{1}D^{p}_{q} \tag{6.112}
$$

and

<a id="Ch6.E113"></a>

$$
\Pi({\bf r})=\sum_{pqrs}\phi_{p}({\bf r})\phi_{q}({\bf r})\phi_{r}({\bf r})\phi_{s}({\bf r}){}^{2}D^{pq}_{rs} \tag{6.113}
$$

and $\nabla\rho({\bf r})$ and $\nabla\Pi({\bf r})$ represent the gradients of these quantities.
In Q-Chem, $E_{\rm xc}$ is chosen to be a translated[[886]](../bib_references/bib.md#bib920)
 on-top pair density functional, which
is essentially the same as a functional of the density and spin density (and their gradients), with the spin-density
(and its gradient) re-expressed as a function
of the on-top pair density (and its gradient). The specific choice of on-top pair density functional is controlled
through the *$rem* variables PDFT_EXCHANGE and PDFT_CORRELATION.
