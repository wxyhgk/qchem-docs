---
title: "4.4.5 Basis Set Projection"
---

## 4.4.5 Basis Set Projection

(July 4, 2026)

**Q-Chem** also includes a novel basis set projection method developed by Dr Jing
Kong of **Q-Chem** Inc. It permits a calculation in a large basis set to
bootstrap itself up *via* a calculation in a small basis set that is
automatically spawned when the user requests this option. When basis set
projection is requested (by providing a valid small basis for BASIS2),
the program executes the following steps:

- •

A simple DFT calculation is performed in the small basis,
BASIS2, yielding a converged density matrix in this basis.
- •

The large basis set SCF calculation (with different values of
EXCHANGE and CORRELATION set by the input) begins by
constructing the DFT Fock operator in the large basis but with the
density matrix obtained from the small basis set.
- •

By diagonalizing this matrix, an accurate initial guess for the density
matrix in the large basis is obtained, and the target SCF calculation
commences.

Two different methods of projection are available and can be set using the
BASISPROJTYPE *$rem*. The OVPROJECTION option expands the MOs
from the BASIS2 calculation in the larger basis, while the
FOPPROJECTION option constructs the Fock matrix in the larger basis
using the density matrix from the initial, smaller basis set calculation. Basis
set projection is a very effective option for general basis sets, where the SAD
guess is not available. In detail, this initial guess is controlled by the
following *$rem* variables:

### `BASIS2`

> **Sets the small basis set to use in basis set projection.**
>
> * **Type**: `STRING`
> * **Default**: `No second basis set default.`
> * **Options**:
>     * Symbol. Use standard basis sets as per Chapter
>     * `8`: .
>     * `BASIS2_GEN`: General BASIS2
>     * `BASIS2_MIXED`: Mixed BASIS2
> * **Recommendation**: BASIS2 should be smaller than BASIS. There is little advantage to using a basis larger than a minimal basis when BASIS2 is used for initial guess purposes. Larger, standardized BASIS2 options are available for dual-basis calculations (see Section 4.7 ).

### `BASISPROJTYPE`

> **Determines which method to use when projecting the density matrix of BASIS2**
>
> * **Type**: `STRING`
> * **Default**: `OVPROJECTION`
> * **Options**:
>     * `FOPPROJECTION`: Construct the Fock matrix in the second basis
>     * `OVPROJECTION`: Projects MOs from BASIS2 to BASIS .
> * **Recommendation**: None

**Note: 

BASIS2 sometimes affects post-Hartree-Fock calculations. It is
recommended to split such jobs into two subsequent one, such that in the first
job a desired Hartree-Fock solution is found using BASIS2, and in the
second job, which performs a post-HF calculation,
SCF_GUESS = READ is invoked.
**

???+ example "Example 4.7: Input where basis set projection is used to generate a good initial guess for
a calculation employing a general basis set, for which the default initial
guess is not available."
    ```qchem
    $molecule
       0  1
       O
       H  1  r
       H  1  r  2  a
    
       r    0.9
       a  104.0
    $end
    
    $rem
       METHOD        mp2
       BASIS         general
       BASIS2        sto-3g
    $end
    
    $basis
       O   0
       S   3   1.000000
               3.22037000E+02   5.92394000E-02
               4.84308000E+01   3.51500000E-01
               1.04206000E+01   7.07658000E-01
       SP  2   1.000000
               7.40294000E+00  -4.04453000E-01   2.44586000E-01
               1.57620000E+00   1.22156000E+00   8.53955000E-01
       SP  1   1.000000
               3.73684000E-01   1.00000000E+00   1.00000000E+00
       SP  1   1.000000
               8.45000000E-02   1.00000000E+00   1.00000000E+00
    ****
       H   0
       S   2   1.000000
               5.44717800E+00   1.56285000E-01
               8.24547000E-01   9.04691000E-01
       S   1   1.000000
               1.83192000E-01   1.00000000E+00
    ****
    $end
    ```
