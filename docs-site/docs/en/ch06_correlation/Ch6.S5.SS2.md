---
title: "6.5.2 EPAO Evaluation Options"
---

## 6.5.2 EPAO Evaluation Options

(July 4, 2026)

When a local MP2 job (requested by the LOCAL_MP2 option for
CORRELATION) is performed, the first new step after the SCF
calculation is converged is to extract a minimal basis of polarized atomic
orbitals (EPAOs) that spans the occupied space. There are three valid choices
for this basis, controlled by the PAO_METHOD and
EPAO_ITERATE keywords described below.

- **Non-iterated EPAOs:** The initial guess EPAOs are the default for
local MP2 calculations, and are defined as follows. For each atom, the
covariant density matrix (SPS) is diagonalized, giving eigenvalues which
are approximate natural orbital occupancies, and eigenvectors which are
corresponding atomic orbitals. The $m$ eigenvectors with largest
populations are retained (where $m$ is the minimal basis dimension for
the current atom). This non-orthogonal minimal basis is symmetrically
orthogonalized, and then modified as discussed in
Ref. [[789]](../bib_references/bib.md#bib820)
 to ensure that these functions rigorously span the
occupied space of the full SCF calculation that has just been performed.
These orbitals may be denoted as EPAO(0) to indicate that no iterations
have been performed after the guess. In general, the quality of the local
MP2 results obtained with this option is very similar to the EPAO option
below, but it is much faster and fully robust. For the example of the
torsional barrier calculations discussed above,[[790]](../bib_references/bib.md#bib819)
 the
TRIM RMS deviations of 0.03 kcal/mol from full MP2 calculations are
increased to only 0.04 kcal/mol when EPAO(0) orbitals are employed rather
than EPAOs.
- **EPAOs:** EPAOs are defined by minimizing a localization functional
as described in Ref. [[789]](../bib_references/bib.md#bib820)
. These functions were designed
to be suitable for local MP2 calculations, and have yielded excellent
results in all tests performed so far. Unfortunately the functional is
difficult to converge for large molecules, at least with the algorithms
that have been developed to this stage. Therefore it is not the default,
but is switched on by specifying a (large) value for
EPAO_ITERATE, as discussed below.
- **PAO:** If the SCF calculation is performed in terms of a
molecule-optimized minimal basis, as described in Chapter [4](../ch04_scf/chap_scf.md), then the
resulting PAO-SCF calculation can be corrected with either conventional
or local MP2 for electron correlation. PAO-SCF calculations alter the
SCF energy, and are therefore not the default. This can be enabled by
specifying PAO_METHOD = PAO, in a job with
CORRELATION = LOCAL_MP2.

### `PAO_METHOD`

> **Controls the type of PAO calculations requested.**
>
> * **Type**: `STRING`
> * **Default**: `EPAO`
> * **Options**:
>     * `EPAO`: Find EPAOs by minimizing delocalization function.
>     * `PAO`: Do SCF in a molecule-optimized minimal basis.
> * **Recommendation**: None

### `EPAO_ITERATE`

> **Controls iterations for EPAO calculations (see PAO_METHOD ).**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Optimize the EPAOs for up to
>     * $n$: iterations.
> * **Recommendation**: Use the default. For molecules that are not too large, one can test the sensitivity of the results to the type of minimal functions by the use of optimized EPAOs in which case a value of $n=500$ is reasonable.

### `EPAO_WEIGHTS`

> **Controls algorithm and weights for EPAO calculations (see PAO_METHOD ).**
>
> * **Type**: `INTEGER`
> * **Default**: `115`
> * **Options**:
>     * `15`: Standard weights, with 1 ${}^{\mathrm{st}}$ order optimization only.
> * **Recommendation**: Use the default, unless convergence failure is encountered.

A local MP2 calculation (requested by the LOCAL_MP2 option for
CORRELATION) consists of the following steps:

- After the SCF is converged, a minimal basis of EPAOs are obtained.
- The TRIM (and DIM) local MP2 energies are then evaluated (gradients are
not yet available).

Details of the efficient implementation of the local MP2 method described above
are reported in the recent thesis of Dr. Michael Lee.

 Here we
simply summarize the capabilities of the program. The computational advantage
associated with these local MP2 methods varies depending upon the size of
molecule and the basis set. As a rough general estimate, TRIM MP2 calculations
are feasible on molecule sizes about twice as large as those for which
conventional MP2 calculations are feasible on a given computer, and this is
their primary advantage. Our implementation is well suited for large basis set
calculations. The AO basis two-electron integrals are evaluated four times.
DIM MP2 calculations are performed as a by-product of TRIM MP2 but no
separately optimized DIM algorithm has been implemented.

The resource requirements for local MP2 calculations are as follows:

- *Memory:* The memory requirement for the integral transformation
does not exceed $OON$, and is thresholded so that it asymptotically grows
linearly with molecule size. Additional memory of approximately 32$N^{2}$
is required to complete the local MP2 energy evaluation.
- *Disk:* The disk space requirement is only about $8OVN$, but is
not governed by a threshold. This is a very large reduction from the case
of a full MP2 calculation, where, in the case of four integral
evaluations, $OVN^{2}$/4 disk space is required. As the local MP2 disk
space requirement is not adjustable.

The evaluation of the local MP2 energy does not require any further
customization. An adequate amount of MEM_STATIC (at least 80 –160 Mb)
should be specified to permit efficient AO basis two-electron integral
evaluation, but all large scratch arrays are allocated from
MEM_TOTAL.

???+ example "Example 6.2: A relative energy evaluation using the local TRIM model for MP2 with the
6-311G** basis set. The energy difference is the internal rotation barrier in
acrolein, with the first geometry being planar trans, and the second the
transition structure."
    ```qchem
    $molecule
       0 1
       C
       C  1  1.32095
       C  2  1.47845  1  121.19
       O  3  1.18974  2  123.83  1   180.00
       H  1  1.07686  2  121.50  3     0.00
       H  1  1.07450  2  122.09  3   180.00
       H  2  1.07549  1  122.34  3   180.00
       H  3  1.09486  2  115.27  4   180.00
    $end
    
    $rem
       METHOD        local_mp2
       BASIS         6-311g**
    $end
    
    @@@
    
    $molecule
       0 1
       C
       C  1  1.31656
       C  2  1.49838  1  123.44
       O  3  1.18747  2  123.81  1   92.28
       H  1  1.07631  2  122.03  3   -0.31
       H  1  1.07484  2  121.43  3  180.28
       H  2  1.07813  1  120.96  3  180.34
       H  3  1.09387  2  115.87  4  179.07
    $end
    
    $rem
       METHOD        local_mp2
       BASIS         6-311g**
    $end
    ```
