---
title: "10.8.4 Partial Hessian Vibrational Analysis"
---

## 10.8.4 Partial Hessian Vibrational Analysis

(July 4, 2026)

The computation of harmonic frequencies for systems with a very large number of
atoms can become computationally expensive. However, in many cases only a few
specific vibrational modes or vibrational modes localized in a region of the
system are of interest. A typical example is the calculation of the vibrational
modes of a molecule adsorbed on a surface. In such a case, only the vibrational
modes of the adsorbate are useful, and the vibrational modes associated with
the surface atoms are of less interest. If the vibrational modes of interest
are only weakly coupled to the vibrational modes associated with the rest of
the system, it can be appropriate to adopt a partial Hessian approach. In this
approach,[[120]](../bib_references/bib.md#bib109)
 only the part of the Hessian matrix
comprising the second derivatives of a subset of the atoms defined by the user
is computed. These atoms are defined in the *$alist* block. This results in a
significant decrease in the cost of the calculation. Physically, this
approximation corresponds to assigning an infinite mass to all the atoms
excluded from the Hessian and will only yield sensible results if these atoms
are not involved in the vibrational modes of interest. VPT2 and TOSH anharmonic
frequencies can be computed following a partial Hessian
calculation.[[519]](../bib_references/bib.md#bib533)
 It is also possible to include a subset of
the harmonic vibrational modes with an anharmonic frequency calculation by setting
ANHAR_SEL = TRUE in the *$rem* section.
This can be useful to reduce the
computational cost of an anharmonic frequency calculation or to explore the
coupling between specific vibrational modes.

Alternatively, vibrationally averaged interactions with the rest of the system
can be folded into a partial Hessian calculation using vibrational subsystem
analysis.[[1574]](../bib_references/bib.md#bib1636)
 Based on an adiabatic approximation,
this procedure reduces the cost of diagonalizing the full Hessian, while
providing a local probe of fragments vibrations, and providing better than
partial Hessian accuracy for the low frequency modes of large
molecules.[[439]](../bib_references/bib.md#bib450)
 Mass-effects from the rest of the system can be
vibrationally averaged or excluded within this scheme.

### `PHESS`

> **Controls whether partial Hessian calculations are performed.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: Partial Hessian calculation.
>     * `2`: Vibrational subsystem analysis (massless).
>     * `3`: Vibrational subsystem analysis (weighted).
> * **Recommendation**: None

### `N_SOL`

> **Specifies number of atoms included in the Hessian.**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * `User defined`
> * **Recommendation**: None

### `PH_FAST`

> **Lowers integral cutoff in partial Hessian calculation is performed.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Lower integral cutoffs
> * **Recommendation**: None

???+ example "Example 10.43: This example shows a partial Hessian frequency calculation of the vibrational
frequencies of acetylene on a model of the C(100) surface"
    ```qchem
    $comment
       acetylene - C(100)
       partial Hessian calculation
    $end
    
    $molecule
    0 1
       C  0.000  0.659 -2.173
       C  0.000 -0.659 -2.173
       H  0.000  1.406 -2.956
       H  0.000 -1.406 -2.956
       C  0.000  0.786 -0.647
       C  0.000 -0.786 -0.647
       C  1.253  1.192  0.164
       C -1.253  1.192  0.164
       C  1.253 -1.192  0.164
       C  1.297  0.000  1.155
       C -1.253 -1.192  0.164
       C  0.000  0.000  2.023
       C -1.297  0.000  1.155
       H -2.179  0.000  1.795
       H -1.148 -2.156  0.654
       H  0.000 -0.876  2.669
       H  2.179  0.000  1.795
       H -1.148  2.156  0.654
       H -2.153 -1.211 -0.446
       H  2.153 -1.211 -0.446
       H  1.148 -2.156  0.654
       H  1.148  2.156  0.654
       H  2.153  1.211 -0.446
       H -2.153  1.211 -0.446
       H  0.000  0.876  2.669
    $end
    
    $rem
       JOBTYPE           freq
       METHOD            hf
       BASIS             sto-3g
       PHESS             TRUE
       N_SOL             4
    $end
    
    $alist
    1
    2
    3
    4
    $end
    ```
