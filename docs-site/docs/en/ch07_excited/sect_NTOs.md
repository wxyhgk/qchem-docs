---
title: "7.13.3 Natural Transition Orbitals"
---

## 7.13.3 Natural Transition Orbitals

(July 4, 2026)

In certain situations, even the attachment/detachment densities may be
difficult to analyze. An important class of examples are systems with multiple
chromophores, which may support exciton states consisting of linear
combinations of localized excitations. For such states, both the attachment
and the detachment density are highly delocalized and occupy basically the same
region of space.[[752]](../bib_references/bib.md#bib785)
 Lack of phase information makes the
attachment/detachment densities difficult to analyze, while strong mixing
of the canonical MOs means that excitonic states are also difficult to
characterize in terms of MOs.[[572]](../bib_references/bib.md#bib586)

Analysis of these and other excited states is greatly simplified by
constructing natural transition orbitals (NTOs) for the excited states.[[572]](../bib_references/bib.md#bib586)

(The basic idea behind NTOs is rather old,[[864]](../bib_references/bib.md#bib898)
 and has been
rediscovered several times.[[913]](../bib_references/bib.md#bib947)
 These orbitals were
later shown to be equivalent to CIS natural orbitals.[[1331]](../bib_references/bib.md#bib1390)
) Let
$\mathbf{T}$ denote the transition density matrix from an excited-state
calculation. The dimension of this matrix is $O\times V$, where $O$ and $V$
denote the number of occupied and virtual MOs, respectively. The NTOs are
defined by transformations $\mathbf{U}$ and $\mathbf{V}$ obtained by singular
value decomposition (SVD) of the matrix $\mathbf{T}$, *i.e.*,[[925]](../bib_references/bib.md#bib962)

<a id="eq:NTO_SVD"></a>

$$
\mathbf{UTV}^{\dagger}=\bm{\Lambda} \tag{7.188}
$$

The matrices $\mathbf{U}$ and $\mathbf{V}$ are unitary and $\bm{\Lambda}$ is
diagonal, with the latter containing at most $O$ non-zero elements. The matrix
$\mathbf{U}$ is a unitary transformation from the canonical occupied MOs to a
set of NTOs that together represent the “hole” orbital that is left by the
excited electron, while $\mathbf{V}$ transforms the canonical virtual MOs into
a set of NTOs representing the excited electron. (Equivalently, the “holes”
are the eigenvectors of the $O\times O$ matrix $\mathbf{TT}^{\dagger}$ and the
particles are eigenvectors of the $V\times V$ matrix
$\mathbf{T}^{\dagger}\mathbf{T}$.[[913]](../bib_references/bib.md#bib947)
) These “hole” and
“particle” NTOs come in pairs, and their relative importance in describing
the excitation is governed by the diagonal elements of $\bm{\Lambda}$, which
are excitation amplitudes in the NTO basis. By virtue of the SVD in
Eq. ([7.188](#eq:NTO_SVD)), any excited state may be represented using at most $O$
excitation amplitudes and corresponding hole/particle NTO pairs. (The
discussion here assumes that $V\geq O$, which is typically the case except
possibly in minimal basis sets. Although it is possible to use the transpose
of Eq. ([7.188](#eq:NTO_SVD)) to obtain NTOs when $V<O$, this has not been
implemented in **Q-Chem** due to its limited domain of applicability.)

The SVD generalizes the concept of matrix diagonalization to the case of
rectangular matrices, and therefore reduces as much as possible the number of
non-zero outer products needed for an exact representation of $\mathbf{T}$. In
this sense, the NTOs represent the best possible particle/hole picture of
an excited state. The detachment density is recovered as the sum of the
squares of the “hole” NTOs, while the attachment density is precisely the sum
of the squares of the “particle” NTOs. Unlike the attachment/detachment densities, however, NTOs preserve phase information, which can be
very helpful in characterizing the diabatic character (*e.g.*, $\pi\pi^{\ast}$ or
$n\pi^{\ast}$) of excited states in complex systems. In the limit that there is only one significant pair of NTOs,
the squares of these two orbitals ($|\psi_{\text{hole}}(\mathbf{r})|^{2}$ and $|\psi_{\text{particle}}(\mathbf{r})|^{2}$) are
precisely equivalent to the detachment and attachment densities that were introduced in
Section [7.13.2](sect_AttachDetach.md).

Even when there is more than one significant NTO amplitude, the NTOs still represent a significant
compression of information, as compared to the canonical MO basis.

NTOs are available within **Q-Chem** for CIS, RPA, TDDFT, ADC, and EOM-CC methods. For
the correlated wave functions (EOM-CC and ADC) and for SF-DFT, they can be computed using **libwfa** 
module. The simplest way to visualize the NTOs is to generate them in
a format suitable for viewing with the freely-available **MolDen** or
**MacMolPlt** programs, as described in Chapter [10](../ch10_properties/chap_properties.md).
