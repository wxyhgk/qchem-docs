---
title: "4.6.3 Linear Scaling Exchange (LinK) Matrix Evaluation"
---

## 4.6.3 Linear Scaling Exchange (LinK) Matrix Evaluation

(July 4, 2026)

Hartree-Fock calculations and the popular hybrid density functionals such as
B3LYP also require two-electron integrals to evaluate the exchange energy
associated with a single determinant. There is no useful multipole expansion
for the exchange energy, because the bra and ket of the two-electron integral
are coupled by the density matrix, which carries the effect of exchange.
Fortunately, density matrix elements decay exponentially with distance for
systems that have a HOMO/LUMO gap.[[1221]](../bib_references/bib.md#bib1278)
 The better the
insulator, the more localized the electronic structure, and the faster the rate
of exponential decay. Therefore, for insulators, there are only a linear number
of numerically significant contributions to the exchange energy. With
intelligent numerical thresholding, it is possible to rigorously evaluate the
exchange matrix in linear scaling effort. For this purpose, **Q-Chem** contains
the linear scaling K (LinK) method[[1011]](../bib_references/bib.md#bib1049)
 to evaluate both
exchange energies and their gradients[[1012]](../bib_references/bib.md#bib1050)
 in linear scaling
effort (provided the density matrix is highly sparse). The LinK method
essentially reduces to the conventional direct SCF method for exchange in the
small molecule limit (by adding no significant overhead), while yielding large
speedups for (very) large systems where the density matrix is indeed highly
sparse. For full details, we refer the reader to the original
papers.[[1011]](../bib_references/bib.md#bib1049)
 LinK can be explicitly requested by the
following option (although **Q-Chem** automatically switches it on when the
program believes it is the preferable algorithm).

LIN_K

### `LIN_K`

> **Controls whether linear scaling evaluation of exact exchange (LinK) is used.**
>
> * **Type**: `LOGICAL`
> * **Default**: `Program chooses, switching on LinK whenever CFMM is used.`
> * **Options**:
>     * TRUE
>     * Use LinK
>     * FALSE
>     * Do not use LinK
> * **Recommendation**: Use for HF and hybrid DFT calculations with large numbers of atoms.

???+ example "Example 4.19: Q-Chem input for a large single point energy calculation. The CFMM is
switched on automatically when LinK is requested."
    ```qchem
    $comment
       HF/3-21G single point calculation on a large molecule
       read in the molecular coordinates from file
    $end
    
    $molecule
       read base_pair.inp
    $end
    
    $rem
       METHOD     HF      Hartree-Fock
       BASIS      sto-3g  Basis set
       LIN_K      TRUE    Calculate K using LinK
    $end
    ```
