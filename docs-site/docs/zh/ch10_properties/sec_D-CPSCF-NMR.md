---
title: "10.11.3 Linear-Scaling NMR Chemical Shift Calculations"
---

## 10.11.3 Linear-Scaling NMR Chemical Shift Calculations

(July 4, 2026)

In conventional implementations, the cost for computation of NMR chemical
shifts within even the simplest quantum chemical methods such as Hartree-Fock
of DFT increases cubically with molecular size $M$, ${\cal{O}}({M^{3}})$. As such,
NMR chemical shift calculations have largely been limited to molecular systems
on the order of 100 atoms, assuming no symmetry. For larger systems it is
crucial to reduce the increase of the computational effort to linear, which is
possible for systems with a nonzero HOMO/LUMO gaps and was reported for
the first time by Kussmann and Ochsenfeld.[[1010]](../bib_references/bib.md#bib1054)

This approach incurs no loss of accuracy with respect to traditional
cubic-scaling implementations, and makes feasible NMR chemical shift
calculations using Hartree-Fock or DFT approaches in molecular systems with
1,000+ atoms. For many molecular systems the Hartree-Fock (GIAO-HF) approach
provides typically an accuracy of 0.2–0.4 ppm for the computation of ${}^{1}$H NMR
chemical shifts, for example.[[1013]](../bib_references/bib.md#bib1051)
 GIAO-HF/6-31G* calculations
with 1,003 atoms and 8,593 basis functions, without symmetry, have been
reported.[[1010]](../bib_references/bib.md#bib1054)
 GIAO-DFT calculations are even simpler and
faster for density functionals that do not contain Hartree-Fock exchange.

The present implementation of NMR shieldings employs the LinK (linear Hartree-Fock exchange)
method[[1011]](../bib_references/bib.md#bib1049)
 for the formation of
exchange contributions.[[1010]](../bib_references/bib.md#bib1054)
 Since the derivative of the
density matrix with respect to the magnetic field is skew-symmetric, its
Coulomb-type contractions vanish. For the remaining Coulomb-type matrices the
CFMM method[[1463]](../bib_references/bib.md#bib1518)
 is used.[[1010]](../bib_references/bib.md#bib1054)
 In addition, a
multitude of different approaches for the solution of the CPSCF equations can
be selected within **Q-Chem**.

To request a NMR chemical shift calculation using the density matrix approach,
set JOBTYPE to NMR in the *$rem* section.
Additional job-control variables can be found below.

D_CPSCF_PERTNUM

### `D_CPSCF_PERTNUM`

> **Specifies whether to do the perturbations one at a time, or all together.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Perturbed densities to be calculated all together.
>     * 1
>     * Perturbed densities to be calculated one at a time.
> * **Recommendation**: None

D_SCF_CONV_1

### `D_SCF_CONV_1`

> **Sets the convergence criterion for the level-1 iterations. This preconditions the density for the level-2 calculation, and does not include any two-electron integrals.**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $n<10$
>     * Sets convergence threshold to
>     * $10^{-n}$
>     * .
> * **Recommendation**: The criterion for level-1 convergence must be less than or equal to the level-2 criterion, otherwise the D-CPSCF will not converge.

D_SCF_CONV_2

### `D_SCF_CONV_2`

> **Sets the convergence criterion for the level-2 iterations.**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $n<10$
>     * Sets convergence threshold to
>     * $10^{-n}$
>     * .
> * **Recommendation**: None

D_SCF_MAX_1

### `D_SCF_MAX_1`

> **Sets the maximum number of level-1 iterations.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$
>     * User defined.
> * **Recommendation**: Use the default.

D_SCF_MAX_2

### `D_SCF_MAX_2`

> **Sets the maximum number of level-2 iterations.**
>
> * **Type**: `INTEGER`
> * **Default**: `30`
> * **Options**:
>     * $n$
>     * User defined.
> * **Recommendation**: Use the default.

D_SCF_DIIS

### `D_SCF_DIIS`

> **Specifies the number of matrices to use in the DIIS extrapolation in the D-CPSCF.**
>
> * **Type**: `INTEGER`
> * **Default**: `11`
> * **Options**:
>     * $n$
>     * $n$
>     * = 0 specifies no DIIS extrapolation is to be used.
> * **Recommendation**: Use the default.

???+ example "Example 10.61: NMR chemical shifts via the D-CPSCF method, showing all input options."
    ```qchem
     $molecule
     0  1
     H        0.00000        0.00000        0.00000
     C        1.10000        0.00000        0.00000
     F        1.52324        1.22917        0.00000
     F        1.52324       -0.61459        1.06450
     F        1.52324       -0.61459       -1.06450
     $end
    
     $rem
        JOBTYPE            NMR
        EXCHANGE           B3LYP
        BASIS              6-31G*
        D_CPSCF_PERTNUM    0    D-CPSCF number of perturbations at once
        D_SCF_SOLVER       430  D-SCF   leqs_solver
        D_SCF_CONV_1       4    D-SCF   leqs_conv1
        D_SCF_CONV_2       4    D-SCF   leqs_conv2
        D_SCF_MAX_1        200  D-SCF   maxiter level 1
        D_SCF_MAX_2        50   D-SCF   maxiter level 2
        D_SCF_DIIS         11   D-SCF   DIIS
        D_SCF_ITOL         2    D-SCF   conv. criterion
     $end
    ```
