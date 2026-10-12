---
title: "8.5.1 Overview"
---

## 8.5.1 Overview

(July 4, 2026)

In addition to defining a custom basis set, it is also possible to specify
different standard basis sets for different atoms. For example, in a large
alkene molecule the hydrogen atoms could be modeled by the STO-3G basis, while
the carbon atoms have the larger 6-31G(d) basis. This can be specified within
the *$basis* block using the more familiar basis set labels.

!!! note "Note"
    (1) It is not possible to augment a standard basis set in this way; the whole
    basis needs to be inserted as for a user-defined basis (angular
    momentum, exponents, contraction coefficients) and additional functions
    added. Standard basis set exponents and coefficients can be easily
    obtained by setting the PRINT_GENERAL_BASIS *$rem* variable to TRUE.
    (2) The PURECART flag must be set for *all* general basis
    input containing $d$ angular momentum or higher functions, regardless of
    whether standard basis sets are entered in this non-standard manner.


The user can also specify different basis sets for atoms of the same type, but
in different parts of the molecule. This allows a larger basis set to be used
for the active region of a system, and a smaller basis set to be used in the
less important regions. To enable this the BASIS keyword must be set
to MIXED and a *$basis* section included in the input deck that gives a
complete specification of the basis sets to be used. The format is exactly the
same as for the user-defined basis, except that the atom number (as ordered in
the *$molecule* section) must be specified in the field after the atomic
symbol. A basis set must be specified for every atom in the input, even if the
same basis set is to be used for all atoms of a particular element. Custom
basis sets can be entered, and the shorthand labeling of basis sets is also supported.

The use of different basis sets for a particular element means the global
potential energy surface is no longer unique. The user should exercise caution
when using this feature of mixed basis sets, especially during geometry
optimizations and transition state searches.

???+ example "Example 8.2: Example of adding a user defined non-standard basis set. The user is able to
specify different standard basis sets for different atoms."
    ```qchem
    $molecule
       0  1
       O
       H  O  oh
       H  O  oh  2  hoh
    
       oh  =   1.2
       hoh = 110.0
    $end
    
    $rem
       EXCHANGE   hf
       BASIS      General   user-defined general basis
       PURECART   2         Cartesian D functions
       BASIS2     sto-3g    use STO-3G as initial guess
    $end
    
    $basis
       H 0
       6-31G
       ****
       O 0
       6-311G(d)
       ****
    $end
    ```

???+ example "Example 8.3: Example of using a mixed basis set for methanol. The user is able to specify
different standard basis sets for some atoms and supply user-defined exponents
and contraction coefficients for others. This might be particularly useful in
cases where the user has constructed exponents and contraction coefficients for
atoms not defined in a standard basis set so that only the non-defined atoms
need have the exponents and contraction coefficients entered. Note that a
basis set has to be specified for every atom in the molecule, even if the same
basis is to be used on an atom type."
    ```qchem
    $molecule
      0  1
      C    0.0000000    0.0148306    0.7155831
      H    0.9153226    0.5361067    1.0707116
      H    0.0000000   -1.0112551    1.1374379
      H   -0.9153226    0.5361067    1.0707116
      O    0.0000000   -0.0695490   -0.6801243
      H    0.0000000    0.8662925   -1.0101622
    $end
    
    $rem
       EXCHANGE   hf
       BASIS      mixed          ! user-defined mixed basis
       PRINT_GENERAL_BASIS true  ! confirm what basis functions are used
    $end
    
    $basis
       C  1
       3-21G
       ****
       H  2
       sto-3g
       ****
       H  3
       sto-3g
       ****
       H  4
       sto-3g
       ****
       O  5
       S  3  1.00
          3.22037000E+02   5.92394000E-02
          4.84308000E+01   3.51500000E-01
          1.04206000E+01   7.07658000E-01
       SP 2 1.00
          7.40294000E+00  -4.04453000E-01   2.44586000E-01
          1.57620000E+00   1.22156000E+00   8.53955000E-01
       SP 1 1.00
          3.73684000E-01   1.00000000E+00   1.00000000E+00
       SP 1 1.00
          8.45000000E-02   1.00000000E+00   1.00000000E+00
       ****
       H  6
       6-31(+,+)G(d,p)
       ****
    $end
    ```
