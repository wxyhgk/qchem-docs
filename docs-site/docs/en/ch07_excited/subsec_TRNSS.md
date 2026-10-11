---
title: "7.3.3 TDDFT within a Reduced Single-Excitation Space"
---

## 7.3.3 TDDFT within a Reduced Single-Excitation Space

(July 4, 2026)

Much of chemistry and biology occurs in solution or on surfaces. The molecular
environment can have a large effect on electronic structure and may change
chemical behavior. **Q-Chem** is able to compute excited states within a local
region of a system through performing the TDDFT (or CIS) calculation with a
reduced single excitation subspace,[[124]](../bib_references/bib.md#bib106)
 in which some of the
amplitudes $\mathbf{x}$ in Eq. ([7.15](sect_tddftintro.md#eq:TDDFT)) are excluded. (This is implemented
within the TDA, so $\mathbf{y}\equiv\mathbf{0}$.) This allows the excited states of a
solute molecule to be studied with a large number of solvent molecules reducing
the rapid rise in computational cost. The success of this approach relies on
there being only weak mixing between the electronic excitations of interest and
those omitted from the single excitation space. For systems in which there are
strong hydrogen bonds between solute and solvent, it is advisable to include
excitations associated with the neighboring solvent molecule(s) within the
reduced excitation space.

The reduced single excitation space is constructed from excitations between a
subset of occupied and virtual orbitals. These can be selected from an analysis
based on Mulliken populations and molecular orbital coefficients. For this
approach the atoms that constitute the solvent needs to be defined.
Alternatively, the orbitals can be defined directly.
Truncated excitation space within TDDFT/TDA is deployed by activating the
TRNSS and TRTYPE keywords. The atoms or orbitals are
specified within a *$solute* block. These approach is implemented within the
TDA and has been used to study the excited states of formamide in
solution,[[122]](../bib_references/bib.md#bib107)
 CO on the Pt(111) surface,[[125]](../bib_references/bib.md#bib108)
 and
the tryptophan chromophore within proteins.[[1176]](../bib_references/bib.md#bib1229)

Restricting excitation space by using TRNSS and *$solute* can be used to deploy
core-valence separation[[218]](../bib_references/bib.md#bib215)

within TDDFT in calculations of core-excited states, see Section [7.12.2](subsec_TDDFT-Xray.md).
