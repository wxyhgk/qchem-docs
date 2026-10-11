---
title: "7.6.2 Static Exchange"
---

## 7.6.2 Static Exchange

(July 4, 2026)

In the simplest form of STEX,[[605]](../bib_references/bib.md#bib628)
 one computes excitation energies by diagonalizing the virtual space of a Fock matrix for the ionized system. When using STEX on multiple core-ionized states,[[28]](../bib_references/bib.md#bib12)
 the underlying assumptions are that the coupling between non-orthogonal determinants is negligible, and that all relevant excited determinants can be formed by single electron-attachment to the core-ionized state. In this way, STEX can be considered to be an approximation to NOCIS.

The STEX algorithm is very similar to NOCIS. The ground-state calculation includes the Boys localization of the reference orbitals before the MOM. However, the open-shell references are formed from the core-ionized reference, instead of optimizing them separately, rendering these states orthogonal to the rest of the core-excitations from that particular atom. After the matrix build, the orthogonal matrix blocks are projected against the ground state (contrasted with NOCIS, where the whole matrix is projected against the ground state), the eigenvalue problem is solved. Because the basis of excited determinants is not orthogonal to the ground state, NOCI is required to compute the oscillator strengths.

Like NOCIS, STEX is spin-pure and size-consistent. However, due to the de-coupling of the references, STEX calculations break the spatial symmetry of the final states.
