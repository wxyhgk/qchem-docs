---
title: "9.8.4 Job Control and Examples"
---

## 9.8.4 Job Control and Examples

(July 4, 2026)

For MECP optimization, set MECP_OPT = TRUE in the *$rem*
section, and note that the *$derivative_coupling* input section discussed in
Section [9.8.2](subsec_deriv-couple-jobcontrol.md) is not necessary in this case.

MECP_OPT

### `MECP_OPT`

> **Determines whether we are doing MECP optimizations.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Do MECP optimization.
>     * FALSE
>     * Do not do MECP optimization.
> * **Recommendation**: None.

MECP_METHODS

### `MECP_METHODS`

> **Determines which method to be used.**
>
> * **Type**: `STRING`
> * **Default**: `BRANCHING_PLANE`
> * **Options**:
>     * BRANCHING_PLANE
>     * Use the branching-plane updating method.
>     * MECP_DIRECT
>     * Use the direct method.
>     * PENALTY_FUNCTION
>     * Use the penalty-constrained method.
> * **Recommendation**: The direct method is stable for small molecules or molecules with high symmetry. The branching-plane updating method is more efficient for larger molecules but does not work if the two states have different symmetries. If using the branching-plane updating method, GEOM_OPT_COORDS must be set to 0 in the $rem section, as this algorithm is available in Cartesian coordinates only. The penalty-constrained method converges slowly and is suggested only if other methods fail.

MECP_STATE1

### `MECP_STATE1`

> **Sets the first Born-Oppenheimer state for MECP optimization.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `None`
> * **Options**:
>     * [
>     * $i$
>     * ,
>     * $j$
>     * ]
>     * Find the
>     * $j$
>     * th excited state with the total spin
>     * $i$
>     * ;
>     * $j=0$
>     * means the SCF ground state.
> * **Recommendation**: $i$ is ignored for restricted calculations; for unrestricted calculations, $i$ can only be 0 or 1.

MECP_STATE2

### `MECP_STATE2`

> **Sets the second Born-Oppenheimer state for MECP optimization.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `None`
> * **Options**:
>     * [
>     * $i$
>     * ,
>     * $j$
>     * ]
>     * Find the
>     * $j$
>     * th excited state with the total spin
>     * $i$
>     * ;
>     * $j=0$
>     * means the SCF ground state.
> * **Recommendation**: $i$ is ignored for restricted calculations; for unrestricted calculations, $i$ can only be 0 or 1.

CIS_S2_THRESH

### `CIS_S2_THRESH`

> **Determines whether a state is a singlet or triplet in unrestricted calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `120`
> * **Options**:
>     * $n$
>     * Sets the
>     * $\langle\hat{S}^{2}\rangle$
>     * threshold to
>     * $n/100$
> * **Recommendation**: For the default case, states with $\langle\hat{S}^{2}\rangle>1.2$ are treated as triplet states and other states are treated as singlets.

MECP_PROJ_HESS

### `MECP_PROJ_HESS`

> **Determines whether to project out the coupling vector from the Hessian when using branching plane updating method.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * TRUE
>     * FALSE
> * **Recommendation**: Use the default.

???+ example "Example 9.29: MECP optimization of an intersection between the S ${}_{2}$ and S ${}_{3}$ states of
NO ${}_{2}^{-}$ , using the direct method at the SOS-CIS(D0) level."
    ```qchem
    $molecule
       -1 1
       N1
       O2  N1  RNO
       O3  N1  RNO  O2  AONO
    
       RNO  = 1.50
       AONO = 100
    $end
    
    $rem
       JOBTYPE         = opt
       METHOD          = soscis(d0)
       BASIS           = aug-cc-pVDZ
       AUX_BASIS       = rimp2-aug-cc-pVDZ
       PURECART        = 1111
       CIS_N_ROOTS     = 4
       CIS_TRIPLETS    = false
       CIS_SINGLETS    = true
       MEM_STATIC      = 900
       MEM_TOTAL       = 1950
       MECP_OPT        = true
       MECP_STATE1     = [0,2]
       MECP_STATE2     = [0,3]
       MECP_METHODS    = mecp_direct
    $end
    ```

???+ example "Example 9.30: Optimization of the ethylidene MECP between S ${}_{0}$ and S ${}_{1}$ at the SF-TDDFT level using the branching-plane updating method."
    ```qchem
    $molecule
       0 3
       C   0.044626  -0.2419240   0.357157
       C   0.008905   0.6727548   1.460500
       H   0.928425  -0.1459163  -0.272095
       H  -0.831032  -0.1926895  -0.288529
       H  -0.009238   0.9611331   2.479936
       H   0.068314  -1.2533580   0.778847
    $end
    
    $rem
       JOBTYPE           opt
       METHOD            bhhlyp
       BASIS             6-31G(d,p)
       MECP_OPT          true
       MECP_METHODS      branching_plane
       MECP_PROJ_HESS    true  ! project out y vector from the hessian
       GEOM_OPT_COORDS   0     ! currently only works for Cartesian coordinate
       GEOM_OPT_DRIVER   optimize
       SPIN_FLIP         true
       UNRESTRICTED      true
       CIS_N_ROOTS       4
       MECP_STATE1       [0,1]
       MECP_STATE2       [0,2]
       CIS_S2_THRESH     120
    $end
    ```

???+ example "Example 9.31: Optimization of the twisted-pyramidalized ethylene MECP between S ${}_{0}$ and
S ${}_{1}$ at the SF-TDDFT level using the penalty-constrained updating method."
    ```qchem
    $molecule
       0 3
       C  -0.015889   0.073532  -0.059559
       C   0.012427  -0.002468   1.315694
       H   0.857876   0.147014  -0.710529
       H  -0.936470  -0.011696  -0.626761
       H   0.764557   0.663381   1.762573
       H   0.740773  -0.869764   1.328583
    $end
    
    $rem
       JOBTYPE         opt
       MECP_OPT        true
       MECP_METHODS    penalty_function
       METHOD          bhhlyp
       SPIN_FLIP       true
       UNRESTRICTED    true
       BASIS           6-31G(d,p)
       CIS_N_ROOTS     4
       MECP_STATE1     [0,1]
       MECP_STATE2     [0,2]
       CIS_S2_THRESH   120
       GEOM_OPT_DRIVER optimize
    $end
    ```

???+ example "Example 9.32: Optimization of the $\tilde{B}^{1}A_{2}$ and $\tilde{A}^{1}B_{2}$ states of
N ${}_{3}^{+}$ at the EOM-EE-CCSD level using the direct method.
See Section 7.9.28 for the specifics of performing MECP
optimization with coupled cluster."
    ```qchem
    $molecule
       1 1
       N1
       N2 N1 rNN
       N3 N2 rNN N1 aNNN
    
       rNN  =  1.54
       aNNN = 50.0
    $end
    
    $rem
       JOBTYPE                opt
       MECP_OPT               true
       MECP_METHODS           mecp_direct
       METHOD                 eom-ccsd
       BASIS                  6-31g
       EE_SINGLETS            [0,2,0,2]
       XOPT_STATE_1           [0,2,2]
       XOPT_STATE_2           [0,4,1]
       CCMAN2                 false
       GEOM_OPT_TOL_GRADIENT  30
       GEOM_OPT_DRIVER        optimize
    $end
    ```

???+ example "Example 9.33: Optimization of the ethylidene MECP between S ${}_{0}$ and S ${}_{1}$ at the SF-TDDFT level with analytic derivative couplings."
    ```qchem
    $molecule
       0 3
       C   0.044626  -0.241924   0.357157
       C   0.008905   0.672754   1.460500
       H   0.928425  -0.145916  -0.272095
       H  -0.831032  -0.192689  -0.288529
       H  -0.009238   0.961133   2.479936
       H   0.068314  -1.253358   0.778847
    $end
    
    $rem
       JOBTYPE            opt
       MECP_OPT           true
       MECP_METHODS       branching_plane
       MECP_PROJ_HESS     true
       GEOM_OPT_COORDS    0
       MECP_STATE1        [0,1]
       MECP_STATE2        [0,2]
       UNRESTRICTED       true
       SPIN_FLIP          true
       CIS_N_ROOTS        4
       CALC_NAC           true
       CIS_DER_NUMSTATE   2
       MAX_CIS_CYCLES     50
       EXCHANGE           bhhlyp
       BASIS              6-31G(d,p)
       INTEGRAL_SYMMETRY  true
    $end
    ```
