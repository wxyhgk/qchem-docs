---
title: "7.13.2 Attachment/Detachment Density Analysis"
---

## 7.13.2 Attachment/Detachment Density Analysis

(July 4, 2026)

Consider the one-particle density matrices of the initial and final states of
interest, $\mathbf{P}_{1}$ and $\mathbf{P}_{2}$ respectively. Assuming that each state is
represented in a finite basis of spin-orbitals, such as the molecular orbital
basis, and each state is at the same geometry. Subtracting these matrices
yields the difference density

<a id="eq623"></a>

$$
\bm{\Delta}={\rm{\bf P}}_{1}-{\rm{\bf P}}_{2} \tag{7.180}
$$

Now, the eigenvectors of the one-particle density matrix $\mathbf{P}$ describing a
single state are termed the natural orbitals, and provide the best orbital
description that is possible for the state, in that a CI expansion using the
natural orbitals as the single-particle basis is the most compact. The basis
of the attachment/detachment analysis is to consider what could be termed
natural orbitals of the electronic transition and their occupation numbers
(associated eigenvalues). These are defined as the eigenvectors $\mathbf{U}$ defined by

<a id="eq624"></a>

$$
{\rm{\bf U}}^{\dagger}\bm{\Delta}{\rm{\bf U}}=\delta \tag{7.181}
$$

The sum of the occupation numbers $\delta_{p}$ of these orbitals is then

<a id="eq625"></a>

$$
\mbox{tr}(\bm{\Delta})=\sum\limits_{p=1}^{N}{\delta_{p}}=n \tag{7.182}
$$

where $n$ is the net gain or loss of electrons in the transition. The net gain
in an electronic transition which does not involve ionization or electron
attachment will obviously be zero.

The detachment density

<a id="eq:detach_density_matrix"></a>

$$
\textbf{D}=\textbf{UdU}^{\dagger} \tag{7.183}
$$

is defined as the sum of all natural orbitals of the difference density with
negative occupation numbers, weighted by the absolute value of their
occupations where $\mathbf{d}$ is a diagonal matrix with elements

<a id="eq627"></a>

$$
d_{p}=-\min(\delta_{p},0) \tag{7.184}
$$

The detachment density corresponds to the electron density associated with
single particle levels vacated in an electronic transition or hole density.

The attachment density

<a id="eq:attach_density_matrix"></a>

$$
\textbf{A}=\textbf{UaU}^{\dagger} \tag{7.185}
$$

is defined as the sum of all natural orbitals of the difference density with
positive occupation numbers where $\mathbf{a}$ is a diagonal matrix with elements

<a id="eq629"></a>

$$
a_{p}=\max(\delta_{p},0)\;. \tag{7.186}
$$

The attachment density corresponds to the electron density associated with
the single particle levels occupied in the transition or particle density.
The difference between the attachment and detachment densities yields the
original difference density matrix

<a id="eq630"></a>

$$
\bm{\Delta}=\mathbf{A}-\mathbf{D}\;. \tag{7.187}
$$

Within a CIS or TDDFT calculation, where the transitions are strictly one-electron in nature,
the matrices $\mathbf{A}$ and $\mathbf{D}$ are the particle (virtual-virtual) and hole (occupied-occupied)
components of the unrelaxed difference density matrix.
