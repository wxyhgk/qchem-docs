---
title: "9.4.3 Frozen Atoms"
---

## 9.4.3 Frozen Atoms

(July 4, 2026)

Absolute atom positions can be frozen with the *FIXED* section. The
section starts with the *FIXED* keyword as the first line and ends with
the *ENDFIXED* keyword on the last. The format to fix a coordinate or
coordinates of an atom is:

`atom    coordinate_reference`

*coordinate_reference* can be any combination of up to three characters
$X$, $Y$ and $Z$ to specify the coordinate(s) to be fixed: $X$, $Y$, $Z$,
*XY*, *XZ*, *YZ*, *XYZ*. The fixing characters must be next
to each other. *e.g.*,

> ```qchem
> FIXED
> 2 XY
> ENDFIXED
> ```

means the $x$-coordinate and $y$-coordinate of atom 2 are fixed, whereas

> ```qchem
> FIXED
> 2 X Y
> ENDFIXED
> ```

will yield erroneous results.

**Note: 

When the *FIXED* section is specified within *$opt*, the
optimization will proceed in Cartesian coordinates.
**

Note that *frequency* calculations for a system with frozen atom constraints will generally produce
imaginary frequencies. These arise because the Hessian computed
for the frequency calculation has different physics compared to the gradient
computed during the fixed-atom optimization.
One possible workaround is simply to zero out the elements of the Hessian associated
with the frozen atoms. This removes the contribution of the frozen atoms to
the normal modes and reduces the number of frequencies computed. For a system
with $N$ atoms, where $n$ atoms are frozen, there will be $3(N-n)-6$ normal
modes, or $3(N-n)-5$ if the system is linear. This “zeroing out” approach can be requested with a pair of *$rem* variables,
FRZN_OPT and FRZ_ATOMS, as described below. A more elegant approach is to replace the strictly
fixed atomic positions with soft harmonic confining potentials, which achieves effectively the same result but allows for relaxation
(*i.e.*, optimization) of all atomic coordinates, so that a proper vibrational frequency calculation can be performed. The use of
harmonic confining potentials as a replacement for fixed atom constraints is described in Section [9.4.7](subsec_HarmonicConfiner.md).

FRZN_OPT

### `FRZN_OPT`

> **Controls whether the job uses zeroed Hessian technique in the frequency calculations**
>
> * **Type**: `LOGICAL`
> * **Default**: `False`
> * **Options**:
>     * False
>     * Do not use the zeroed out Hessian
>     * True
>     * Use the zeroed out Hessian
> * **Recommendation**: False

FRZ_ATOMS

### `FRZ_ATOMS`

> **Controls the number of frozen atoms**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * User defined
> * **Recommendation**: None

**Note: 

The above two *$rem* variables are only relevant to frequency calculations; they are
not required in geometry optimization with fixed atoms.
**

???+ example "Example 9.12: Optimization of the water dimer structure with the structure of the first water frozen"
    ```qchem
    $molecule
     0 1
     O   -1.551007  -0.114520   0.000000
     H   -1.934259   0.762503   0.000000
     H   -0.599677   0.040712   0.000000
     O    1.350625   0.111469   0.000000
     H    1.680398  -0.373741  -0.758561
     H    1.680398  -0.373741   0.758561
    $end
    
    $rem
     JOBTYPE          OPT
     METHOD           B3LYP
     BASIS            6-31G(D)
     SCF_CONVERGENCE  8
    $end
    
    $opt
     FIXED
     1:3  XYZ
     ENDFIXED
    $end
    ```

???+ example "Example 9.13: Frequency calculations using zeroed out Hessian technique. Note the frozen atom indices
are specified in the $frozen_opt section."
    ```qchem
    $molecule
       0 1
       C        -0.0014570824    1.4001468208    0.0000000000
       H        -0.0030029737    2.4867609686    0.0000000000
       C        -1.2093554750    0.6986986619    0.0000000000
       H        -2.1525287416    1.2392252926    0.0000000000
       C        -1.2094237515   -0.6985901650    0.0000000000
       H        -2.1508487680   -1.2427180000    0.0000000000
       C        -0.0003285453   -1.3965954363    0.0000000000
       H        -0.0006460438   -2.4839940415    0.0000000000
       C         1.2098250013   -0.6978846084    0.0000000000
       H         2.1493830451   -1.2446769146    0.0000000000
       C         1.2133329176    0.6987868208    0.0000000000
       H         2.1550504173    1.2408406009    0.0000000000
    $end
    
    $rem
       JOBTYPE      freq
       METHOD       b3lyp
       BASIS        6-31G*
       FRZN_OPT     1  ! Turns on the freq calculation with frozen Hessians
       FRZ_ATOMS    2  ! No. of frozen atoms
       POINT_GROUP_SYMMETRY false
       INTEGRAL_SYMMETRY    false
    $end
    
    $frozen_opt
    1 11
    $end
    ```
