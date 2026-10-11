---
title: "7.8.5 SOS-CIS(D 0 ) Model"
---

## 7.8.5 SOS-CIS(D${}_{0}$) Model

(July 4, 2026)

CIS(D) and its cousins explained in the above are all based on a second-order
non-degenerate perturbative correction scheme on the CIS energy
(“diagonalize-and-then-perturb” scheme). Therefore, they may fail when
multiple excited states come close in terms of their energies. In this case,
the system can be handled by applying quasi-degenerate perturbative correction
scheme (“perturb-and-then-diagonalize” scheme). The working expression can be
obtained by slightly modifying CIS(D) expression shown in
Section [7.8.2](topic_cisd.md).[[541]](../bib_references/bib.md#bib557)

First, starting from Eq. ([7.87](topic_cisd.md#eq619)), one can be explicitly write the CIS(D)
energy as[[206]](../bib_references/bib.md#bib198)

<a id="Ch7.E93"></a>

$$
\omega^{\rm CIS}+\omega^{(2)}=\bf b^{(0)^{\mathbf{t}}}{\rm{\bf A}_{SS}^{(0)}}\bf b^{(0)}+\bf b^{(0)^{\mathbf{t}}}{\rm{\bf A}_{SS}^{(2)}}\bf b^{(0)}-\bf b^{(0)^{\mathbf{t}}}{\rm{\bf A}_{SD}^{(1)}\left({\bf D}_{DD}^{(0)}-\omega^{CIS}\right)^{-1}{\bf A}_{DS}^{(1)}}\bf b^{(0)} \tag{7.93}
$$

To avoid the failures of the perturbation theory near degeneracies, the entire
single and double blocks of the response matrix should be diagonalized. Because
such a diagonalization is a non-trivial non-linear problem, an additional
approximation from the binomial expansion of the
$\rm\left({\bf D}_{DD}^{(0)}-\omega^{CIS}\right)^{-1}$ is further
applied:[[541]](../bib_references/bib.md#bib557)

<a id="Ch7.E94"></a>

$$
\rm\left({\bf D}_{DD}^{(0)}-\omega^{CIS}\right)^{-1}=\left({\bf D}_{DD}^{(0)}\right)^{-1}\left(1+\omega\left({\bf D}_{DD}^{(0)}\right)^{-1}+\omega^{2}\left({\bf D}_{DD}^{(0)}\right)^{-2}+...\right) \tag{7.94}
$$

The CIS(D${}_{0}$) energy $\omega$ is defined as the eigen-solution of the response
matrix with the zero-th order expansion of this equation. Namely,

<a id="Ch7.E95"></a>

$$
\rm\left({\bf A}_{SS}^{(0)}+{\bf A}_{SS}^{(2)}-{\bf A}_{SD}^{(1)}({\bf D}_{DD}^{(0)})^{-1}{\bf A}_{DS}^{(1)}\right)\bf b=\omega\bf b \tag{7.95}
$$

Similar to SOS-CIS(D), SOS-CIS(D${}_{0}$) theory is defined by taking the opposite-spin
portions of this equation and then scaling them with two semi-empirical
parameters:[[206]](../bib_references/bib.md#bib198)

<a id="Ch7.E96"></a>

$$
\rm\left({\bf A}_{SS}^{(0)}+{\it c_{T}}{\bf A}_{SS}^{OS(2)}-{\it c_{U}}{\bf A}_{SD}^{OS(1)}({\bf D}_{DD}^{(0)})^{-1}{\bf A}_{DS}^{OS(1)}\right)\bf b=\omega\bf
b \tag{7.96}
$$

Using the Laplace transform and the auxiliary basis expansion techniques, this
can also be handled with a 4th-order scaling computational effort. In
**Q-Chem**, an efficient 4th-order scaling analytical gradient of SOS-CIS(D${}_{0}$)
is also available. This can be used to perform excited state geometry
optimizations on the electronically excited state surfaces.
