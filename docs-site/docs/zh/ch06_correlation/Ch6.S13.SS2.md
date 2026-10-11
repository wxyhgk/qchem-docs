---
title: "6.13.2 (2) Triples and Quadruples Corrections"
---

## 6.13.2 (2) Triples and Quadruples Corrections

(July 4, 2026)

While the (T) corrections discussed above have been extraordinarily successful,
there is nonetheless still room for further improvements in accuracy, for at
least some important classes of problems. They contain judiciously chosen terms
from 4th- and 5th-order Møller-Plesset perturbation
theory, as well as higher order terms that result from the fact that the
converged cluster amplitudes are employed to evaluate the 4th- and 5th-order
order terms. The (T) correction therefore depends upon the bare
reference orbitals and orbital energies, and in this way its effectiveness
still depends on the quality of the reference determinant. Since we are
correcting a coupled-cluster solution rather than a single determinant, this is
an aspect of the (T) corrections that can be improved. Deficiencies of the (T)
corrections show up computationally in cases where there are near-degeneracies
between orbitals, such as stretched bonds, some transition states, open shell
radicals, and diradicals.

Prof. Steve Gwaltney, while working at Berkeley with Martin Head-Gordon, has
suggested a new class of non iterative correction that offers the prospect of
improved accuracy in problem cases of the types identified above.[[507]](../bib_references/bib.md#bib520)
**Q-Chem** contains Gwaltney’s implementation of this new
method, for energies only. The new correction is a true second-order correction
to a coupled-cluster starting point, and is therefore denoted as (2). It is
available for two of the cluster methods discussed above, as OD(2) and
CCSD(2).[[507]](../bib_references/bib.md#bib520)
 Only energies are available at present.

The basis of the (2) method is to partition not the regular Hamiltonian into
perturbed and unperturbed parts, but rather to partition a
similarity-transformed Hamiltonian, defined as $\tilde{H}=e^{-\hat{T}}\hat{H}e^{\hat{T}}$. In the truncated space (call it the $p$-space)
within which the cluster problem is solved (*e.g.*, singles and doubles for
CCSD), the coupled-cluster wave function is a true eigenvalue of $\tilde{H}$.
Therefore we take the zero order Hamiltonian, $\tilde{H}^{(0)}$,
to be the full $\tilde{H}$ in the p-space, while in the space of
excluded substitutions (the q-space) we take only the one-body part of $\tilde{H}$
(which can be made diagonal). The fluctuation potential describing
electron correlations in the $q$-space is $\tilde{H}-\tilde{H}^{(0)}$,
and the (2) correction then follows from second-order perturbation
theory.

The new partitioning of terms between the perturbed and unperturbed
Hamiltonians inherent in the (2) correction leads to a correction that shows
both similarities and differences relative to the existing (T) corrections.
There are two types of higher correlations that enter at second-order: not only
triple substitutions, but also quadruple substitutions. The quadruples are
treated with a factorization ansatz, that is exact in 5th order
Møller-Plesset theory,[[731]](../bib_references/bib.md#bib764)
 to reduce their computational
cost from $N^{9}$ to $N^{6}$. For large basis sets this can still be larger
than the cost of the triples terms, which scale as the 7th power of
molecule size, with a factor twice as large as the usual (T) corrections.

These corrections are feasible for molecules containing between four and ten
first row atoms, depending on computer resources, and the size of the basis set
chosen. There is early evidence that the (2) corrections are superior to the
(T) corrections for highly correlated systems.[[507]](../bib_references/bib.md#bib520)
 This shows
up in improved potential curves, particularly at long range and may also extend
to improved energetic and structural properties at equilibrium in problematical
cases. It will be some time before sufficient testing on the new (2)
corrections has been done to permit a general assessment of the performance of
these methods. However, they are clearly very promising, and for this reason
they are available in **Q-Chem**.
