---
title: "4.6.7 PARI-K Fast Exchange Algorithm"
---

## 4.6.7 PARI-K Fast Exchange Algorithm

(July 4, 2026)

PARI-K[[891]](../bib_references/bib.md#bib925)
 is an algorithm that significantly accelerates the
construction of the exchange matrix in Hartree-Fock and hybrid density
functional theory calculations with large basis sets. The speedup is made
possible by fitting products of atomic orbitals using only auxiliary basis
functions found on their respective atoms. The PARI-K implementation in
**Q-Chem** is an efficient MO-basis formulation similar to the AO-basis
formulation of Merlot *et al.*[[938]](../bib_references/bib.md#bib978)
 PARI-K is highly recommended for
calculations using basis sets of size augmented triple-zeta or larger, and
should be used in conjunction with the standard RI-J algorithm for constructing
the Coulomb matrix.[[1442]](../bib_references/bib.md#bib1502)
 The exchange fitting basis sets of
Weigend[[1442]](../bib_references/bib.md#bib1502)
 (cc-pVTZ-JK and cc-pVQZ-JK) are recommended for use
in conjunction with PARI-K. The errors associated with the PARI-K approximation
appear to be only slightly worse than standard RI-HF.[[938]](../bib_references/bib.md#bib978)

### `PARI_K`

> **Controls the use of the PARI-K approximation in the construction of the exchange matrix**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Use PARI-K.
> * **Recommendation**: Use for basis sets aug-cc-pVTZ and larger.
