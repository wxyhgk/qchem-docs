---
title: "6.12.9 Quadratic Coupled Cluster Doubles (QCCD)"
---

## 6.12.9 Quadratic Coupled Cluster Doubles (QCCD)

(July 4, 2026)

The non variational determination of the energy in the CCSD, QCISD, and OD
methods discussed in the above subsections is not normally a practical problem.
However, there are some cases where these methods perform poorly. One such
example are potential curves for homolytic bond dissociation, using closed
shell orbitals, where the calculated energies near dissociation go
significantly below the true energies, giving potential curves with unphysical
barriers to formation of the molecule from the separated
fragments.[[1388]](../bib_references/bib.md#bib1450)
 The Quadratic Coupled Cluster Doubles
(QCCD) method[[1389]](../bib_references/bib.md#bib1451)
 recently proposed by Troy Van Voorhis at
Berkeley uses a different energy functional to yield improved behavior in
problem cases of this type. Specifically, the QCCD energy functional is defined
as

<a id="eq530"></a>

$$
E_{\mathrm{QCCD}}=\left\langle{\Phi_{0}\left({1+\hat{\Lambda}_{2}+\frac{1}{2}\hat{\Lambda}_{2}^{2}}\right)\left|{\hat{H}}\right|\exp\left({\hat{T}_{2}}\right)\Phi_{0}}\right\rangle_{C} \tag{6.77}
$$

where the amplitudes of both the $\hat{T}_{2}$ and $\hat{\Lambda}_{2}$
operators are determined by minimizing the QCCD energy functional.
Additionally, the optimal orbitals are determined by minimizing the QCCD
energy functional with respect to orbital rotations mixing occupied and
virtual orbitals.

To see why the QCCD energy should be an improvement on the OD energy, we first
write the latter in a different way than before. Namely, we can write a CCD
energy functional which when minimized with respect to the $\hat{T}_{2}$ and
$\hat{\Lambda}_{2}$ operators, gives back the same CCD equations defined earlier.
This energy functional is

<a id="eq531"></a>

$$
E_{\mathrm{CCD}}=\left\langle{\Phi_{0}\left({1+\hat{\Lambda}_{2}}\right)\left|{\hat{H}}\right|\exp\left({\hat{T}_{2}}\right)\Phi_{0}}\right\rangle_{C} \tag{6.78}
$$

Minimization with respect to the $\hat{\Lambda}_{2}$ operator gives the equations
for the $\hat{T}_{2}$ operator presented previously, and, if those equations are
satisfied then it is clear that we do not require knowledge of the $\hat{\Lambda}_{2}$ operator itself to evaluate the energy.

Comparing the two energy functionals, Eqs. ([6.77](#eq530)) and ([6.78](#eq531)), we see
that the QCCD functional includes up through quadratic terms of the Maclaurin
expansion of $\exp(\hat{\Lambda}_{2})$ while the conventional CCD functional
includes only linear terms. Thus the bra wave function and the ket wave function
in the energy expression are treated more equivalently in QCCD than in CCD.
This makes QCCD closer to a true variational treatment[[1388]](../bib_references/bib.md#bib1450)

where the bra and ket wave functions are treated precisely equivalently, but
without the exponential cost of the variational method.

In practice QCCD is a dramatic improvement relative to any of the conventional
pair correlation methods for processes involving more than two active electrons
(*i.e.*, the breaking of at least a double bond, or, two spatially close single
bonds). For example calculations, we refer to the original paper,[[1389]](../bib_references/bib.md#bib1451)

and the follow-up paper describing the full implementation.[[177]](../bib_references/bib.md#bib172)

We note that these improvements carry a computational price.
While QCCD scales formally with the 6th power of molecule size like
CCSD, QCISD, and OD, the coefficient is substantially larger. For this reason,
QCCD calculations are by default performed as OD calculations until they are
partly converged. **Q-Chem** also contains some configuration interaction models
(CISD and CISDT). The CI methods are inferior to CC due to size-consistency
issues, however, these models may be useful for benchmarking and development
purposes.
