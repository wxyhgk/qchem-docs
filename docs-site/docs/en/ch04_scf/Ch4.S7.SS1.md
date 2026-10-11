---
title: "4.7.1 Introduction"
---

## 4.7.1 Introduction

(July 4, 2026)

The dual-basis
approximation[[825]](../bib_references/bib.md#bib859)

to self-consistent field (HF or DFT) energies provides an efficient means for
obtaining large basis set effects at vastly less cost than a full SCF
calculation in a large basis set. First, a full SCF calculation is performed
in a chosen small basis (specified by BASIS2). Second, a single
SCF-like step in the larger, target basis (specified, as usual, by
BASIS) is used to perturbatively approximate the large basis energy.
This correction amounts to a first-order approximation in the change in density
matrix, after the single large-basis step:

<a id="Ch4.E64"></a>
$$
E_{\text{total}}=E_{\text{small basis}}+\mbox{tr}[(\Delta\mathbf{P})\mathbf{F}]_{\text{large basis}}\;. \tag{4.64}
$$

Here $\mathbf{F}$ (in the large basis) is built from the converged (small basis)
density matrix. Thus, only a single Fock build is required in the large basis
set. Currently, HF and DFT energies (SP) as well as analytic first derivatives
(FORCE or OPT) are available.

**Note: 

As of version 4.0, first derivatives of unrestricted dual-basis DFT
energies—though correct—require a code-efficiency fix. We do not recommend
use of these derivatives until this improvement has been made.
**

Across the G3 set[[296]](../bib_references/bib.md#bib297)
 of 223
molecules, using cc-pVQZ, dual-basis errors for B3LYP are 0.04 kcal/mol
(energy) and 0.03 kcal/mol (atomization energy per bond) and are at least an
order of magnitude less than using a smaller basis set alone. These errors are
obtained at roughly an order of magnitude savings in cost, relative to the
full, target-basis calculation.
