---
title: "7.9.17 Using Projectors for Computing High-Lying EOM-CC Ctates"
---

## 7.9.17 Using Projectors for Computing High-Lying EOM-CC Ctates

(July 4, 2026)

**Q-Chem** offers a simple projection technique for computing high-lying
EOM-CCSD states, such as excited or
ionized states dominated by electron removal from inner-valence orbitals.

This technique provides a more robust alternative to the
overlap-based algorithms
described in Section [7.9.16](subsec_EOM-CC-diag.md) as
it allows to target multiple states of the given class in a single
calculation and
by applying a projector at every iteration it guarantees convergence
towards stable solutions.

This feature is controlled by the keywords EOM_EE_IV_PROJ and
EOM_IP_IV_PROJ, which activate a projector that is applied at each
iteration of the Davidson solver. The inner-valence projector is constructed
by including the specified number of lowest-lying active occupied orbitals.
Frozen orbitals, if present, are excluded from this count.

The applied projector enforces convergence toward states in which at least
one electron is removed from the inner-valence subspace defined by the
selected orbitals. This enables stable convergence to excited or ionized
states associated with deeper-lying orbitals. The inner-valence subspace is
defined automatically based on orbital energies. In contrast to the overlap-based Davidson algorithm, no user-specified initial guess is needed.
This feature may also be viewed as an alternative to CVS-type calculations[[269]](../bib_references/bib.md#bib270)
 of core-hole states without requiring to freeze core orbitals.

Examples [7.9.19](ex_CAPlibwfa.md) and [7.9.19](ex_CAPlibwfa.md) illustrate this
feature.
