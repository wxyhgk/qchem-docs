---
title: "6.20.1 Introduction & Theory"
---

## 6.20.1 Introduction & Theory

(July 4, 2026)

The complete active space (CAS) methods are a family of methods for dealing
with strongly correlated systems. In this method, a subset of a system’s
orbitals and electrons are denoted as *active* and the full configuration
interaction (FCI) problem is solved exactly in this small active space. The
remaining occupied orbitals are denoted *inactive* and are treated in a
mean-field manner, while the remaining unoccupied orbitals are denoted *virtual*.
In CAS-CI, this is the end of the matter. In CASSCF, the orbitals spanning these
three spaces (inactive, active, and virtual) are then optimized to obtain the
lowest possible energy. In other words, the CASSCF problem is to find the optimal
(by energy) partitioning of the orbital Hilbert space. This allows moderately sized
systems to be studied as long as the active space is relatively small, due to
combinatorial growth in the number of possible Slater determinants that encompass
all possible configurations within the active space. Indeed, the total number of
possible Slater determinants for an active space with $M$ *spatial* orbitals,
$N_{\uparrow}$ up spins and $N_{\downarrow}$ down spins is:

<a id="A3.S8.EGx28"></a>
$$
\displaystyle N_{\text{total}} \tag{6.87}
$$

Modern computing architectures can handle active spaces of approximately 18 electrons
in 18 orbitals ($\approx 2\times 10^{9}$ determinants), though we do not recommend using
such a large active-space for routine calculations.

Nuclear gradients for CASSCF calculation are also available in **Q-Chem**. In addition to full CAS
calculations, arbitrary order truncated CI (CIS, CISD, CISDT, etc.) may also be carried out in
the requested active space and orbitally optimized.

The electronic energy is an exact functional of the 1-RDM and 2-RDM

<a id="eq:casscf:energy"></a>
$$
E=\frac{1}{2}\sum_{pqrs}\Gamma_{pqrs}g_{pqrs}+\sum_{pq}D_{pq}h_{pq}, \tag{6.88}
$$

Given the 1- and 2-PDMs, the generalized Fock matrices may be generated for this MCSCF.
The derivation and further details are neatly described by Helgaker, Jorgensen, and
Olsen,

 but the key results are summarized here.
In the following, $m,n,p,q,\ldots$ are general indices, $i,j,k,\ldots$ are inactive
indices, $t,u,v,w,\ldots$ are active indices, and $a,b,c,\ldots$ are virtual indices.

The generalized Fock matrix is defined as

<a id="A3.S8.EGx29"></a>
$$
\displaystyle F_{mn}=\sum_{q}D_{pq}h_{pq}+\sum_{qrs}\Gamma_{mqrs}g_{nqrs} \tag{6.89}
$$

where $h_{pq}$ are the 1-electron integrals and $g_{nqrs}$ are the 2-electron integrals and
all indices run over all orbital classes (inactive, active, and virtual). This, generally
non-symmetric, matrix can be simplified by taking advantage of the fact that the form of
the density matrices when some indices are inactive or virtual are much simpler than when
the indices are active. When the first index of the generalized Fock matrix is inactive
and the second is general:

<a id="A3.S8.EGx30"></a>
$$
\displaystyle F_{in}=2({}^{I}F_{ni}+{}^{A}F_{ni}) \tag{6.90}
$$

where the *inactive* and *active Fock matrices* are

<a id="A3.S8.EGx31"></a>
$$
\displaystyle{}^{I}F_{mn} \tag{6.91}
$$

In other words, the inactive Fock matrix is the Fock matrix formed from using only the
inactive density and the active Fock matrix is sum of J and K matrices built from the
active space 1-PDM. When the first index is active, and the second index is general, we
have

<a id="A3.S8.EGx32"></a>
$$
\displaystyle F_{tn}=\sum_{u}{}^{I}F_{nu}D_{vu}+Q_{tn} \tag{6.93}
$$

where the auxiliary Q matrix is

<a id="A3.S8.EGx33"></a>
$$
\displaystyle Q_{tm}=\sum_{u,v,w}\Gamma_{tuvw}g_{muvw} \tag{6.94}
$$

and finally, if the first index is virtual then $F_{an}=0$. This formulation of the
generalized Fock matrix is quite useful because it only requires density matrices with
all indices active and two-electron integrals in the MO basis with three indices active
and one general index, greatly reducing the storage and computational cost of the MO
transformation. The orbital gradient is then given by

<a id="A3.S8.EGx34"></a>
$$
\displaystyle\frac{\partial E}{\partial\Delta_{pq}}=2(F_{pq}-F_{qp}) \tag{6.95}
$$
