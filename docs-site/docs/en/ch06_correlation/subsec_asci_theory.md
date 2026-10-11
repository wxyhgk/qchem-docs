---
title: "6.22.2 Theory"
---

## 6.22.2 Theory

(July 4, 2026)

If we have
a wave function $|\Psi\rangle=\displaystyle\sum\limits_{i}C_{i}|D_{i}\rangle$ (where $|D_{i}\rangle$
are Slater determinants with coefficients $C_{i}$) as an eigenstate of the Hamiltonian, then

<a id="Ch6.E104"></a>

$$
C_{i}=\frac{\sum_{j\neq i}H_{ij}C_{j}}{(H_{ii}-E)}\;, \tag{6.104}
$$

where $H_{ij}=\langle D_{i}|\mathbf{H}|D_{j}\rangle$ is the Hamiltonian matrix element between
determinants $i$ and $j$, and $E$ is the energy of the eigenstate $|\Psi\rangle$. This
exact relationship can be generalized to a metric to predict the expected weight of
a determinant $|D_{i}\rangle$ in a CI expansion, by how it connects to other determinants
in an approximate trial wave function. This metric is also used in Epstein-Nesbet
Perturbation theory as coefficients for the determinants in the first order wave function.

In the ASCI method, all determinants $|D_{i}\rangle$ that are single or double excitations
away from the most important determinants (as ranked by magnitude of coefficients) in
the trial wave function $|\psi_{k}\rangle$ are assigned an estimated importance $A_{i}$ given as

<a id="Ch6.E105"></a>

$$
A_{i}=\frac{\sum_{|D_{j}\rangle\in|\psi_{k}\rangle}H_{ij}C_{j}}{(H_{ii}-E_{k})}\;, \tag{6.105}
$$

where $E_{k}$ is the energy of the trial wave function $|\psi_{k}\rangle$. The search and
selection is only done in the space spanned by determinants connected to the top $c$
determinants in $|\psi_{k}\rangle$ because unimportant determinants are unlikely to be the
sole generator for a top ranked determinant, and this pruning of the search space greatly
accelerates the algorithm. The top $t$ determinants (as ranked by magnitude of $A_{i}$)
connected to $|\psi_{k}\rangle$ are used to form the new wave function $|\psi^{k+1}\rangle$ by
exact diagonalization within that Hilbert subspace.

Once several cycles of ASCI has been completed, the wave function will contain all (or
very nearly all) of the largest weight determinants in the FCI wave function and the
remaining determinants not included should be of small weight. The effect of these many
small remaining determinants are estimated by second order Epstein-Nesbet perturbation
theory (PT2).[[367]](../bib_references/bib.md#bib371)

This final PT2 correction gives extremely
accurate results, often within a kcal/mol of the absolute FCI energies even when only a
tiny fraction of the Hilbert space is included in the ASCI wave function.[[1378]](../bib_references/bib.md#bib1439)

An extrapolation of the variational energy against the PT2 correction (to the FCI limit
of of zero PT2 correction) can also be carried out to generate more accurate estimates,
and predict a metric for error in the final estimate. Indeed, it has been shown
that linear or quadratic fits are quite accurate for extrapolation of SCI energies
against the PT2 correction.[[512]](../bib_references/bib.md#bib524)

We observe essentially linear behavior in the case of ASCI.

ASCI may be used as the full-CI solver for a CASSCF calculation, permitting the extension
of CASSCF to active spaces of $\approx 50$ electrons in $\approx 50$ orbitals. The resulting
method is termed ASCI-SCF.[[807]](../bib_references/bib.md#bib844)

See Section [6.20](sec_casscf.md) for details on CASSCF job control.
