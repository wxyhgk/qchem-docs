---
title: "9.8.3 Minimum-Energy Crossing Points"
---

## 9.8.3 Minimum-Energy Crossing Points

(July 4, 2026)

The seam space of a conical intersection is really a (hyper)surface of
dimension $N_{\rm int}-2$, and while the two electronic states in question are
degenerate at every point within this space, the electronic energy varies from
one point to the next. To provide a simple picture of photochemical reaction
pathways, it is often convenient to locate the minimum-energy crossing point
(MECP) within this $(N_{\rm int}-2)$-dimensional seam. Two separate
minimum-energy pathway searches, one on the excited state starting from the
ground-state geometry and terminating at the MECP, and the other on the ground
state starting from the MECP and terminating at the ground-state geometry, then
affords a photochemical mechanism. (See Ref. [[1546]](../bib_references/bib.md#bib1612)
 for a
simple example.) In some sense, then, the MECP is to photochemistry what the
transition state is to reactions that occur on a single Born-Oppenheimer
potential energy surface. One should be wary of pushing this analogy too far,
because whereas a transition state reasonably be considered to be a bottleneck
point on the reaction pathway, the path through a conical intersection may be
downhill and perhaps therefore more likely to proceed from one surface to the
other at a point “near" the intersection, and in addition there can be
multiple conical intersections between the same pair of states so more than one
photochemical mechanism may be at play. Such complexity could be explored,
albeit at significantly increased cost, using nonadiabatic “surface hopping"
*ab initio* molecular dynamics, as described in Section [9.9.7](sect_fssh.md).
Here we describe the computationally-simpler procedure of locating an MECP
along a conical seam.

Recall that the branching space around a conical intersection between
electronic states $J$ and $K$ is spanned by two vectors, $\mathbf{g}_{JK}$
[Eq. ([9.49](subsec_NACMEs_and_CIs.md#eq:gJK))] and $\mathbf{h}_{JK}$ [Eq. ([9.50](subsec_NACMEs_and_CIs.md#eq:hJK))]. While the
former is readily available in analytic form for any electronic structure
method that has analytic excited-state gradients, the nonadiabatic coupling
vector $\mathbf{h}_{JK}$ is *not* available for most methods. For this
reason, several algorithms have been developed to optimize MECPs without the
need to evaluate $\mathbf{h}_{JK}$, and three such algorithms are available
in **Q-Chem**.

Martínez and coworkers[[805]](../bib_references/bib.md#bib840)
 developed a penalty-constrained
MECP optimization algorithm that consists of minimizing the objective function

<a id="Ch9.E52"></a>
$$
F_{\sigma}(\mathbf{R})=\tfrac{1}{2}\bigl{[}E_{I}(\mathbf{R})+E_{J}(\mathbf{R})\bigr{]}+\sigma\left(\frac{\bigl{[}E_{I}(\mathbf{R})-E_{J}(\mathbf{R})\bigr{]}^{2}}{E_{I}(\mathbf{R})-E_{J}(\mathbf{R})+\alpha}\right)\;, \tag{9.52}
$$

where $\alpha$ is a fixed parameter to avoid singularities and $\sigma$ is a
Lagrange multiplier for a penalty function meant to drive the energy gap to
zero. Minimization of $F_{\sigma}$ is performed iteratively for increasingly
large values $\sigma$.

A second MECP optimization algorithm is a simplification of the
penalty-constrained approach that we call the “direct” method. Here, the
gradient of the objective function is

<a id="eq:direct_MECP"></a>
$$
\mathbf{G}=\mathbf{P}\mathbf{G}_{\rm mean}+2(E_{K}-E_{J})\mathbf{G}_{\rm diff}\;, \tag{9.53}
$$

where

<a id="Ch9.E54"></a>
$$
\mathbf{G}_{\rm mean}=\tfrac{1}{2}(\mathbf{G}_{J}+\mathbf{G}_{K}) \tag{9.54}
$$

is the mean energy gradient, with $\mathbf{G}_{i}=\partial E_{i}/\partial\mathbf{R}$ being the nuclear gradient for state $i$, and

<a id="Ch9.E55"></a>
$$
\mathbf{G}_{\rm diff}=\frac{\mathbf{G}_{K}-\mathbf{G}_{J}}{||\mathbf{G}_{K}-\mathbf{G}_{J}||} \tag{9.55}
$$

is the normalized difference gradient. Finally,

<a id="eq:MECP_projector1"></a>
$$
\mathbf{P}=\bm{1}-\mathbf{G}_{\rm diff}\mathbf{G}_{\rm diff}^{\top} \tag{9.56}
$$

projects the gradient difference direction out of the mean energy gradient in
Eq. ([9.53](#eq:direct_MECP)). The algorithm then consists in minimizing along
the gradient $\mathbf{G}$, with for the iterative cycle over a Lagrange
multiplier, which can sometimes be slow to converge.

The third and final MECP optimization algorithm that is available in **Q-Chem**
is the branching-plane updating method developed by Morokuma and
coworkers[[871]](../bib_references/bib.md#bib906)
 and implemented in **Q-Chem** by Zhang and
Herbert.[[1546]](../bib_references/bib.md#bib1612)
 This algorithm uses a gradient that is similar to
that in Eq. ([9.53](#eq:direct_MECP)) but projects out not just $\mathbf{G}_{\rm diff}$ in Eq. ([9.56](#eq:MECP_projector1)) but also a second vector that is
orthogonal to it, representing an iteratively-updated approximation to the
branching space.

None of these three methods requires evaluation of nonadiabatic couplings, and
all three can be used to optimize MECPs at the CIS, SF-CIS, TDDFT, SF-TDDFT,
and SOS-CIS(D0) levels. The direct algorithm can also be used for EOM-XX-CCSD
methods (XX = EE, IP, or EA). It should be noted that since EOM-XX-CCSD is a
linear response method, it suffers from the same topology problem around
conical intersections involving the ground state that was described in regards
to TDDFT in Section [9.8.1](subsec_NACMEs_and_CIs.md). With spin-flip approaches,
correct topology is obtained.[[1547]](../bib_references/bib.md#bib1613)

Analytic derivative couplings are available for (SF-)CIS and (SF-)TDDFT, so for
these methods one can alternatively employ an optimization algorithm that makes
use of both $\mathbf{g}_{JK}$ and $\mathbf{h}_{JK}$. Such an algorithm,
due to Schlegel and coworkers,[[85]](../bib_references/bib.md#bib70)
 is available in **Q-Chem**
and consists of optimization along the gradient in
Eq. ([9.53](#eq:direct_MECP)) but with a projector

<a id="eq:MECP_projector2"></a>
$$
\mathbf{P}=\bm{1}-\mathbf{G}_{\rm diff}\mathbf{G}_{\rm diff}^{\top}-\mathbf{y}\mathbf{y}^{\top} \tag{9.57}
$$

where

<a id="Ch9.E58"></a>
$$
\mathbf{y}=\frac{(\bm{1}-\mathbf{x}\mathbf{x}^{\top})\mathbf{h}_{JK}}{||(\bm{1}-\mathbf{x}\mathbf{x}^{\top})\mathbf{h}_{JK}||}\;, \tag{9.58}
$$

in place of the projector in Eq. ([9.56](#eq:MECP_projector1)).
Equation ([9.57](#eq:MECP_projector2)) has the effect of projecting the span of
$\mathbf{g}_{JK}$ and $\mathbf{h}_{JK}$ (*i.e.*, the branching space) out
of state-averaged gradient in Eq. ([9.53](#eq:direct_MECP)). The tends to reduce
the number of iterations necessary to converge the MECP, and since calculation
of the (optional) $\mathbf{h}_{JK}$ vector represents only a slight amount
of overhead on top of the (required) $\mathbf{g}_{JK}$ vector, this last
algorithm tends to yield significant speed-ups relative to the other three.[[1547]](../bib_references/bib.md#bib1613)

As such, it is the recommended choice for (SF-)CIS and (SF-)TDDFT.

It should be noted that while the spin-flip methods cure the topology problem
around conical intersections that involve the ground state, this method tends
to exacerbate spin contamination relative to the corresponding spin-conserving
approaches.[[1549]](../bib_references/bib.md#bib1615)

While spin contamination is certainly present
in traditional, spin-conserving CIS and TDDFT, it presents the following unique
challenge in spin-flip methods. Suppose, for definiteness, that one is
interested in singlet excited states. Then the reference state for the
spin-flip methods should be the high-spin triplet. A spin-flipping excitation
will then generate S${}_{0}$, S${}_{1}$, S${}_{2},\ldots$ but will also generate the
$M_{S}=0$ component of the triplet reference state, which therefore appears in
what is ostensibly the singlet manifold. **Q-Chem** attempts to identify this
automatically, based on a threshold for $\langle\hat{S}^{2}\rangle$, but severe
spin contamination can sometimes defeat this algorithm,[[1546]](../bib_references/bib.md#bib1612)

hampering **Q-Chem**’s ability to distinguish singlets from triplets (in this
particular example). An alternative might be the state-tracking procedure that
is described in Section [9.8.5](sec_state_following.md). The spin-adapted spin-flip (SA-SF) method,
either at the CIS or the TDDFT level, can be used to eliminate spin contamination by adding
the minimal number of determinants necessary to obtain $\hat{S}^{2}$ eigenstates.[[1549]](../bib_references/bib.md#bib1615)

The SA-SF approach is described in Section [7.2.3.3](../ch07_excited/Ch7.S2.SS3.md#safs-sftddft). It presently lacks analytic gradients
but can be used to spot-check trajectories or MECP optimization paths obtained using SF-TDDFT.
