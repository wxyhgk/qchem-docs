---
title: "4.5.14 Maximum Overlap Method (MOM)"
---

## 4.5.14 Maximum Overlap Method (MOM)

(July 4, 2026)

In general, the DIIS procedure (Section [4.5.3](sect_diis.md)) is remarkably successful. One difficulty that is
occasionally encountered is the problem of an SCF that occupies two different
sets of orbitals on alternating iterations, and therefore oscillates and fails
to converge. This can be overcome by choosing orbital occupancies that
maximize the overlap of the new occupied orbitals with the set previously
occupied. **Q-Chem** contains the maximum overlap method
(MOM),[[443]](../bib_references/bib.md#bib455)
 developed by Andrew Gilbert and Peter Gill. With
GEN_SCFMAN, the MOM algorithm can be applied to R, U, and RO SCF calculations when
paired with the DIIS algorithm.

MOM is therefore is a useful adjunct to DIIS in convergence problems involving
flipping of orbital occupancies. It is controlled by the *$rem* variable
MOM_START, which specifies the SCF iteration on which the MOM
procedure is first enabled. There are two strategies that are useful in setting
a value for MOM_START. To help maintain an initial configuration it
should be set to start on the first cycle. On the other hand, to assist
convergence it should come on later to avoid holding on to an initial
configuration that may be far from the converged one.

The MOM-related *$rem* variables in full are the following:

MOM_PRINT

### `MOM_PRINT`

> **Switches printing on within the MOM procedure.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Printing is turned off
>     * TRUE
>     * Printing is turned on.
> * **Recommendation**: None

MOM_START

### `MOM_START`

> **Determines when MOM is switched on to stabilize DIIS iterations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0 (FALSE)`
> * **Options**:
>     * 0 (FALSE)
>     * MOM is not used
>     * $n$
>     * MOM begins on cycle
>     * $n$
>     * .
> * **Recommendation**: Set to 1 if preservation of initial orbitals is desired. If MOM is to be used to aid convergence, an SCF without MOM should be run to determine when the SCF starts oscillating. MOM should be set to start just before the oscillations.

MOM_METHOD

### `MOM_METHOD`

> **Determines the target orbitals with which to maximize the overlap on each SCF cycle.**
>
> * **Type**: `INTEGER`
> * **Default**: `MOM`
> * **Options**:
>     * MOM
>     * Maximize overlap with the orbitals from the previous SCF cycle.
>     * IMOM
>     * Maximize overlap with the initial guess orbitals.
> * **Recommendation**: If appropriate guess orbitals can be obtained, then IMOM can provide more reliable convergence to the desired solution. 75 Barca G. M. J., Gilbert A. T. B., Gill P. M. W. J. Chem. Theory Comput. (2018) , 14 , pp. 1501 . Link

???+ example "Example 4.4.17: An example showing how to converge a ROHF calculation on the ${}^{3}\!A_{2}$ state
of DMX. Note the use of reading in orbitals from a previous closed-shell
calculation and the use of MOM to maintain the orbital occupancies. The ${}^{3}B_{1}$ is obtained if MOM is not used."
    ```qchem
    $molecule
      +1 1
       C       0.000000     0.000000     0.990770
       H       0.000000     0.000000     2.081970
       C      -1.233954     0.000000     0.290926
       C      -2.444677     0.000000     1.001437
       H      -2.464545     0.000000     2.089088
       H      -3.400657     0.000000     0.486785
       C      -1.175344     0.000000    -1.151599
       H      -2.151707     0.000000    -1.649364
       C       0.000000     0.000000    -1.928130
       C       1.175344     0.000000    -1.151599
       H       2.151707     0.000000    -1.649364
       C       1.233954     0.000000     0.290926
       C       2.444677     0.000000     1.001437
       H       2.464545     0.000000     2.089088
       H       3.400657     0.000000     0.486785
    $end
    
    $rem
       UNRESTRICTED      false
       METHOD            hf
       BASIS             6-31+G*
       SCF_GUESS         core
       THRESH            12
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       UNRESTRICTED      false
       METHOD            hf
       BASIS             6-31+G*
       SCF_GUESS         read
       MOM_START         1
       THRESH            12
    $end
    
    $occupied
       1:26 28
       1:26 28
    $end
    
    @@@
    
    $molecule
       -1 3
       read
    $end
    
    $rem
       UNRESTRICTED      false
       METHOD            hf
       BASIS             6-31+G*
       SCF_GUESS         read
       THRESH            12
    $end
    ```
