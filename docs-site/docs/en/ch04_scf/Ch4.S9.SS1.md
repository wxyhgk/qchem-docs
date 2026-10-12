---
title: "4.9.1 Polarized Atomic Orbital (PAO) Calculations"
---

## 4.9.1 Polarized Atomic Orbital (PAO) Calculations

(July 4, 2026)

Polarized atomic orbital (PAO) calculations are an interesting unconventional
SCF method, in which the molecular orbitals and the density matrix are not
expanded directly in terms of the basis of atomic orbitals. Instead, an
intermediate molecule-optimized minimal basis of polarized atomic orbitals
(PAOs) is used.[[787]](../bib_references/bib.md#bib816)
 The polarized atomic orbitals are defined by
an atom-blocked linear transformation from the fixed atomic orbital basis,
where the coefficients of the transformation are optimized to minimize the
energy, at the same time as the density matrix is obtained in the PAO
representation. Thus a PAO-SCF calculation is a constrained variational
method, whose energy is above that of a full SCF calculation in the same basis.
However, a molecule optimized minimal basis is a very compact and useful
representation for purposes of chemical analysis, and it also has potential
computational advantages in the context of MP2 or local MP2 calculations, as
can be done after a PAO-HF calculation is complete to obtain the PAO-MP2 energy.

PAO-SCF calculations tend to systematically underestimate binding energies
(since by definition the exact result is obtained for atoms, but not for
molecules). In tests on the G2 database, PAO-B3LYP/6-311+G(2df,p) atomization
energies deviated from full B3LYP/6-311+G(2df,p) atomization energies by
roughly 20 kcal/mol, with the error being essentially extensive with the number
of bonds. This deviation can be reduced to only 0.5 kcal/mol
with the use of a simple non-iterative second order
correction for “beyond-minimal basis” effects.[[788]](../bib_references/bib.md#bib818)
 The second
order correction is evaluated at the end of each PAO-SCF calculation, as it
involves negligible computational cost. Analytical gradients are available
using PAOs, to permit structure optimization. For additional discussion of the
PAO-SCF method and its uses, see the references cited above.

Calculations with PAOs are determined controlled by the following *$rem*
variables. PAO_METHOD = PAO invokes PAO-SCF calculations,
while the algorithm used to iterate the PAOs can be controlled with
PAO_ALGORITHM.

### `PAO_ALGORITHM`

> **Algorithm used to optimize polarized atomic orbitals (see PAO_METHOD )**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Use efficient (and riskier) strategy to converge PAOs.
>     * `1`: Use conservative (and slower) strategy to converge PAOs.
> * **Recommendation**: None

### `PAO_METHOD`

> **Controls evaluation of polarized atomic orbitals (PAOs).**
>
> * **Type**: `STRING`
> * **Default**: `EPAO`
> * **Options**:
>     * `PAO`: Perform PAO-SCF instead of conventional SCF.
>     * `EPAO`: Obtain EPAOs after a conventional SCF.
> * **Recommendation**: None
