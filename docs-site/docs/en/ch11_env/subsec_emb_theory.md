---
title: "11.6.1 Introduction and Theory"
---

## 11.6.1 Introduction and Theory

(July 4, 2026)

The formally exact density embedding method developed by Manby, Miller and
coworkers[[878]](../bib_references/bib.md#bib913)
 affords a step further than electrostatic embedding
in the description of chemical environment. This embedding scheme allows for the
partition of a system into two interacting subsystems that are treated at two different
levels of QM theories, *e.g.*, coupled cluster embedded in
DFT. This type of embedding fully accounts for polarization as well as quantum
mechanical exchange, as calculated from the super-molecular embedding density
and the exchange correlation functional used. The goal of this embedding
theory is to perform a higher-level QM calculation in an environment
described by a lower-level QM theory.

## 11.6.1.1 Working Equations

For a system whose total density can be represented as $\boldsymbol{\gamma}=\boldsymbol{\gamma}^{A}+\boldsymbol{\gamma}^{B}$, *i.e.*, the molecular
orbitals on fragments $A$ and $B$ are orthogonal to each other, its total
energy can be expressed as

<a id="A3.S8.EGx111"></a>

$$
\displaystyle\begin{aligned} \displaystyle E_{\text{tot}}[\boldsymbol{\gamma}^{A}+\boldsymbol{\gamma}^{B}]&\displaystyle=\underbrace{\mathrm{tr}(\boldsymbol{\gamma}^{A}\mathbf{h})+J[\boldsymbol{\gamma}^{A}]+E_{\text{xc}}[\boldsymbol{\gamma}^{A}]}_{\text{Energy of A}}+\underbrace{\mathrm{tr}(\boldsymbol{\gamma}^{B}\mathbf{h})+J[\boldsymbol{\gamma}^{B}]+E_{\text{xc}}[\boldsymbol{\gamma}^{B}]}_{\text{Energy of B}}\\
&\displaystyle\qquad+\underbrace{J[\boldsymbol{\gamma}^{A},\boldsymbol{\gamma}^{B}]+E_{\text{xc}}[\boldsymbol{\gamma}^{A},\boldsymbol{\gamma}^{B}]}_{\text{Non-additive terms}}\end{aligned} \tag{11.99}
$$

where $\mathbf{h}$ is the core-Hamiltonian matrix, $J$ and $E_{\text{xc}}$
are the Coulomb and XC energies (exact exchange $K$ will also be present
if a hybrid functional is employed). In an embedding calculation where the
electron density of $A$ (denoted as $\tilde{\gamma}^{A}$) is optimized at a high-level
theory in the presence of $\gamma^{B}$ (which is obtained at a low-level theory and
then fixed), the total energy can be expressed as

<a id="eq:Etot_dft_in_dft"></a>

$$
E_{\text{tot}}[\tilde{\gamma}^{A},\gamma^{B}]=E^{\text{high}}[\tilde{\gamma}^{A}]+E^{\text{low}}[\tilde{\gamma}^{A}+\gamma^{B}]-E^{\text{low}}[\tilde{\gamma}^{A}]. \tag{11.100}
$$

Differentiating Eq. ([11.100](#eq:Etot_dft_in_dft)) with respect to $\tilde{\gamma}^{A}$ gives the
Fock matrix for the embedding calculation:

<a id="Ch11.E101"></a>

$$
\mathbf{f}^{\text{A-in-B}}=\frac{\delta}{\delta\tilde{\gamma}^{A}}E_{\text{tot}}[\tilde{\gamma}^{A},\gamma^{B}]=\mathbf{F}^{\text{high}}[\tilde{\gamma}^{A}]+\mathbf{v}_{\text{emb}}[\tilde{\gamma}^{A},\gamma^{B}], \tag{11.101}
$$

where the embedding potential

<a id="A3.S8.EGx112"></a>

$$
\displaystyle\begin{aligned} \displaystyle\mathbf{v}_{\text{emb}}[\tilde{\gamma}^{A},\gamma^{B}]&\displaystyle=\frac{\partial}{\partial\tilde{\gamma}^{A}}\left(E^{\text{low}}[\tilde{\gamma}^{A}+\gamma^{B}]-E^{\text{low}}[\tilde{\gamma}^{A}]\right)\\
&\displaystyle=\mathbf{F}^{\text{low}}[\tilde{\gamma}^{A}+\gamma^{B}]-\mathbf{F}^{\text{low}}[\tilde{\gamma}^{A}]\\
&\displaystyle=(\mathbf{J}[\boldsymbol{\gamma}^{A}+\boldsymbol{\gamma}^{B}]-\mathbf{J}[\boldsymbol{\gamma}^{A}])+(\mathbf{v}^{\text{low}}_{\text{xc}}[\boldsymbol{\gamma}^{A}+\boldsymbol{\gamma}^{B}]-\mathbf{v}^{\text{low}}_{\text{xc}}[\boldsymbol{\gamma}^{A}])+\mu\mathbf{P}^{B},\end{aligned} \tag{11.102}
$$

where $\mathbf{P}^{B}=\mathbf{S}\boldsymbol{\gamma}^{B}\mathbf{S}$ is the
projector formed by $B$’s orbitals and $\mu$ is a large enough constant
(*e.g.* 10${}^{6}$ a.u.) that effectively elevates the energies of $B$’s orbitals
and thereby enforces the orthogonality between MOs
on $A$ and $B$. In the **Q-Chem** implementation (with GEN_SCFMAN_EMBED
= TRUE), an alternative approach is employed, where one diagonalizes a
modified Fock matrix from which the variational degrees of freedom spanned by $B$’s orbitals are
projected out:

<a id="Ch11.E103"></a>

$$
\tilde{\mathbf{f}}^{\text{A-in-B}}=(\mathbf{I}-\mathbf{S}\boldsymbol{\gamma}^{B})\mathbf{f}^{\text{A-in-B}}(\mathbf{I}-\boldsymbol{\gamma}^{B}\mathbf{S}), \tag{11.103}
$$

where $\mathbf{S}$ is the AO overlap matrix.

One disadvantage of using the energy expression given by Eq. ([11.100](#eq:Etot_dft_in_dft)) is that
the embedding potential [Eq. ([11.102](#eq:v_emb))] depends on $\tilde{\gamma}^{A}$, which needs to
be updated in every iteration of the embedding calculation. Thus this scheme affords no savings
in computational cost for DFT-in-DFT calculations. To address this limitation, a linearized
approximation was suggested,[[792]](../bib_references/bib.md#bib827)
 which is based on the following expansion
(to the first order of $\tilde{\gamma}^{A}-\gamma^{A}$):

<a id="eq:linear_expansion"></a>

$$
E^{\text{low}}[\tilde{\gamma}^{A}+\gamma^{B}]-E^{\text{low}}[\tilde{\gamma}^{A}]\approx E^{\text{low}}[\gamma^{A}+\gamma^{B}]-E^{\text{low}}[\gamma^{A}]+\mathrm{Tr}\left((\tilde{\gamma}^{A}-\gamma^{A})\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}]\right), \tag{11.104}
$$

where

<a id="Ch11.E105"></a>

$$
\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}]=\frac{\delta}{\delta\gamma^{A}}\left(E^{\text{low}}[\gamma^{A}+\gamma^{B}]-E^{\text{low}}[\gamma^{A}]\right)=\mathbf{F}^{\text{low}}[\gamma^{A}+\gamma^{B}]-\mathbf{F}[\gamma^{A}] \tag{11.105}
$$

Based on this linearized approximation, the total energy of the entire system is approximately given by

<a id="eq:Etot_dft_in_dft_approx"></a>

$$
E_{\text{tot}}[\tilde{\gamma}^{A};\gamma^{A},\gamma^{B}]=E^{\text{high}}[\tilde{\gamma}^{A}]+E^{\text{low}}[\gamma^{A}+\gamma^{B}]-E^{\text{low}}[\gamma^{A}]+\mathrm{Tr}\left((\tilde{\gamma}^{A}-\gamma^{A})\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}]\right), \tag{11.106}
$$

and the Fock matrix for embedding calculation:

<a id="Ch11.E107"></a>

$$
\mathbf{f}^{\text{A-in-B}}=\frac{\delta}{\delta\tilde{\gamma}^{A}}E_{\text{tot}}[\tilde{\gamma}^{A};\gamma^{A},\gamma^{B}]=\mathbf{F}^{\text{high}}[\tilde{\gamma}^{A}]+\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}] \tag{11.107}
$$

where the embedding potential stays unchanged during the embedding calculation.
In **Q-Chem** 5.4.1 and versions after, this linearized approximation is used by default in projection-based
embedding calculations.

For wave function-in-DFT calculations, one can absorb the embedding potential
$\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}]$ into the Hamiltonian that is used
for the correlated wave function calculation, converting Eq. ([11.106](#eq:Etot_dft_in_dft_approx)) into

<a id="eq:Etot_wft_in_dft_approx"></a>

$$
E[\Psi^{A};\gamma^{A},\gamma^{B}]=\langle\Psi^{A}|\hat{H}^{\text{A-in-B}}|\Psi^{A}\rangle+E^{\text{low}}[\gamma^{A}+\gamma^{B}]-E^{\text{low}}[\gamma^{A}]-\mathrm{Tr}\left(\gamma^{A}\mathbf{v}_{\text{emb}}[\gamma^{A},\gamma^{B}]\right)\;. \tag{11.108}
$$

## 11.6.1.2 Partition of the Occupied Space

An embedding calculation usually starts from an SCF calculation of the full
system at the lower level of theory, which yields canonical MOs. Therefore, it
is necessary to partition the occupied space and assign orbitals to fragments
$A$ and $B$ (without losing generality, assuming $A$ is the embedded fragment).
In the original work by Manby *et al.*,[[878]](../bib_references/bib.md#bib913)
 this was achieved by

- •

Performing a Pipek-Mezey localization[[1093]](../bib_references/bib.md#bib1138)
 of the canonical
occupied orbitals;
- •

Assigning a PM-localized orbital to the “active” fragment $A$ if its
Mulliken population on $A$ is greater than 0.4.

This approach has been adopted as the default occupied space partition method
in **Q-Chem**.

Recently a parameter-free and more robust partition scheme was proposed by
Claudino and Mayhall, which is known as the Subsystem Projected AO
Decomposition (SPADE) procedure.[[253]](../bib_references/bib.md#bib254)

In this approach, one first transforms the occupied orbitals into the symmetrically
orthogonalized AO basis:

<a id="Ch11.E109"></a>

$$
\bar{\mathbf{C}}_{\text{occ}}=\mathbf{S}^{1/2}\mathbf{C}_{\text{occ}} \tag{11.109}
$$

and then denotes the rows in $\bar{\mathbf{C}}_{\text{occ}}$ that correspond to
fragment $A$ as $\bar{\mathbf{C}}_{\text{occ}}^{A}$. A singular value
decomposition (SVD) is then applied to $\bar{\mathbf{C}}_{\text{occ}}^{A}$:
$\bar{\mathbf{C}}_{\text{occ}}^{A}=\mathbf{U}^{A}\Sigma^{A}(\mathbf{V}^{A})^{T}$,
and the SPADE orbitals are then obtained by rotating the original
$\mathbf{C}_{\text{occ}}$:

<a id="Ch11.E110"></a>

$$
\mathbf{C}_{\text{occ}}^{\text{SPADE}}=\mathbf{C}_{\text{occ}}\mathbf{V}^{A}. \tag{11.110}
$$

The largest gap in the singular value spectrum determines the most appropriate
occupied orbital partition under the given fragmentation.

## 11.6.1.3 Truncation of the Virtual Space Using Concentric Localization

A wave function-in-DFT calculation requires not only the occupied orbitals on the
“active” fragment but also the virtual orbitals. Unlike the occupied orbitals,
the virtual orbitals obtained from a projection-based embedding calculation
are not assigned to fragments but stay delocalized. If the full virtual space is
used in the post-SCF calculation, the savings on computational cost will be
rather limited since only the number of occupied orbitals is reduced. Therefore,
it is desirable to further truncate the virtual space so that one can significantly
reduce the computational cost of wave function-in-DFT calculations.

Claudino and Mayhall recently proposed a simple and efficient approach to
truncate the virtual space based on concentric localization (CL),[[254]](../bib_references/bib.md#bib255)

which shares the same spirit as the SPADE partition scheme for occupied space. As
the first step, the original set of delocalized virtual orbitals ($\mathbf{C}_{\text{vir}}$)
represented in the working basis (WB) are projected onto the embedded fragment
$A$ in a user-specified projection basis (PB):

<a id="Ch11.E111"></a>

$$
{}^{A}\mathbf{C}_{\text{vir}}^{\prime}=(\mathbf{S}_{\text{PB},A}^{-1})(^{A}\mathbf{S}_{\text{PB,WB}})\mathbf{C}_{\text{vir}} \tag{11.111}
$$

where the superscript “$A$” indicates that only the rows corresponding to
fragment $A$’s basis functions are included and $\mathbf{S}_{\text{PB},A}$
denotes the overlap matrix for PB functions on fragment $A$ only. One can
choose PB to be the same as WB or even a smaller basis set. A particular set of virtual
orbitals denoted as $\mathbf{C}_{0}$ can then be selected by performing an SVD
on the overlap between ${}^{A}\mathbf{C}_{\text{vir}}^{\prime}$ and $\mathbf{C}_{\text{vir}}$:

<a id="eq:cl_step1"></a>

$$
(^{A}\mathbf{C}_{\text{vir}}^{\prime})^{T}(^{A}\mathbf{S}_{\text{PB,WB}})\mathbf{C}_{\text{vir}}=\mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{T} \tag{11.112}
$$

with

<a id="Ch11.E113"></a>

$$
\displaystyle\mathbf{V} \tag{11.113a}
$$

By construction, $\mathbf{C}_{0}$ should consist of the virtual valence
shell of the WB. In order to achieve higher accuracy for the embedded
correlated method, one can select more virtual orbitals from
$\mathbf{C}_{\text{null},0}$ in a stepwise fashion. A recommended way[[254]](../bib_references/bib.md#bib255)

is to singular value decompose the matrix
$\mathbf{C}^{T}\mathbf{F}\mathbf{C}_{\text{null},0}$, *i.e.*, the coupling
between $\mathbf{C}_{0}$ and $\mathbf{C}_{\text{null},0}$ through the Fock operator

<a id="eq:cl_step2"></a>

$$
\mathbf{C}_{0}^{T}\mathbf{F}\mathbf{C}_{\text{null},0}=\mathbf{U}_{0}\boldsymbol{\Sigma}_{0}\mathbf{V}_{0}^{T} \tag{11.114}
$$

where

<a id="Ch11.E115"></a>

$$
\displaystyle\mathbf{V}_{0} \tag{11.115a}
$$

As the size of $\mathbf{C}_{1}$ is the same as $\mathbf{C}_{0}$, going through
the procedure given by Eq. ([11.114](#eq:cl_step2)) doubles the number of active
virtual orbitals. This procedure can be carried on iteratively, rendering the
accuracy of this method tunable:

<a id="eq:cl_iter"></a>

$$
\mathbf{C}_{n}^{\top}\mathbf{F}\mathbf{C}_{\text{null},n}=\mathbf{U}_{n}\boldsymbol{\Sigma}_{n}\mathbf{V}_{n}^{T} \tag{11.116}
$$

where

<a id="Ch11.E117"></a>

$$
\displaystyle\mathbf{V}_{n} \tag{11.117a}
$$

The virtual orbitals that span the null space, $\mathbf{C}_{\text{null},n+1}$, will
remain inactive in the post-SCF calculations. In practice, one is often able to
obtain sub-kcal/mol accuracy by only including $\mathbf{C}_{0}$ and $\mathbf{C}_{1}$,
which is known as the “double-$\zeta$” CL shell model.
