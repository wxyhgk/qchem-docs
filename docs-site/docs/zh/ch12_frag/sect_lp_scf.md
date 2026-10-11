---
title: "12.5.1 Locally-Projected SCF"
---

## 12.5.1 Locally-Projected SCF

(July 4, 2026)

Constrained locally-projected SCF is an efficient method for removing the SCF
diagonalization bottleneck in calculations for systems of weakly interacting
components such as molecular clusters and molecular
complexes.[[683]](../bib_references/bib.md#bib705)
 The method is based on the equations
of the locally-projected SCF for molecular interactions (SCF-MI).[[1314]](../bib_references/bib.md#bib1371)
 In
the SCF-MI method, the occupied molecular orbitals on a fragment can be
expanded only in terms of the atomic orbitals of the same fragment. Such
constraints produce non-orthogonal MOs that are localized on fragments and are
called absolutely-localized molecular orbitals (ALMOs). The ALMO approximation
excludes charge-transfer from one fragment to another. It also prevents
electrons on one fragment from borrowing the atomic orbitals of other fragments
to compensate for incompleteness of their own AOs and, therefore, removes the
BSSE from the interfragment binding energies. The locally-projected SCF methods
perform an iterative minimization of the SCF energy with respect to the ALMOs
coefficients. The convergence of the algorithm is accelerated with the
locally-projected modification of the DIIS extrapolation
method.[[683]](../bib_references/bib.md#bib705)

The ALMO approximation significantly reduces the number of variational degrees
of freedom of the wave function. The computational advantage of the
locally-projected SCF methods over the conventional SCF method grows with both
basis set size and number of fragments. Although still cubic scaling, SCF-MI
effectively removes the diagonalization step as a bottleneck in these
calculations, because it contains such a small prefactor. In the current
implementation, the SCF-MI methods do not speed up the evaluation of the Fock
matrix and, therefore, do not perform significantly better than the
conventional SCF in the calculations dominated by the Fock build.

Two locally-projected schemes are implemented. One is based on the
locally-projected equations of Stoll *et al.*,[[1314]](../bib_references/bib.md#bib1371)
 the other uses the
locally-projected equations of Gianinetti *et al.*.[[440]](../bib_references/bib.md#bib451)
 These
methods have comparable performance. The Stoll iteration is only slightly
faster than the Gianinetti iteration but the Stoll equations might be a little
bit harder to converge. The Stoll equations also produce ALMOs that are
orthogonal within a fragment. The type of the locally-projected SCF
calculations is requested by specifying either STOLL or GIA
for the FRGM_METHOD keyword.

???+ example "Example 12.6: Locally-projected SCF method of Stoll"
    ```qchem
    $molecule
       0 1
       --
       -1 1
       B       0.068635     0.164710     0.123580
       F      -1.197609     0.568437    -0.412655
       F       0.139421    -1.260255    -0.022586
       F       1.118151     0.800969    -0.486494
       F       0.017532     0.431309     1.531508
       --
       +1 1
       N      -2.132381    -1.230625     1.436633
       H      -1.523820    -1.918931     0.977471
       H      -2.381590    -0.543695     0.713005
       H      -1.541511    -0.726505     2.109346
       H      -2.948798    -1.657993     1.873482
    $end
    
    $rem
       METHOD          BP86
       BASIS           6-31(+,+)G(d,p)
       FRGM_METHOD     STOLL
    $end
    
    $rem_frgm
       SCF_CONVERGENCE 2
       THRESH          5
    $end
    ```
