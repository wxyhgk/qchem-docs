---
title: "7.8.6 CIS(D) Job Control and Examples"
---

## 7.8.6 CIS(D) Job Control and Examples

(July 4, 2026)

The legacy CIS(D) algorithm in **Q-Chem** is handled by the CCMAN/CCMAN2
modules of **Q-Chem**’s and shares many of the *$rem* options.
RI-CIS(D), SOS-CIS(D), and SOS-CIS(D${}_{0}$) do not depend on the coupled-cluster
routines. Users who will not use this legacy CIS(D) method may skip to
Section [7.8.7](subsect_RI-CIS_D.md).

As with all post-HF calculations, it is important to ensure there are
sufficient resources available for the necessary integral calculations and
transformations. For CIS(D), these resources are controlled using the *$rem*
variables CC_MEMORY, MEM_STATIC and MEM_TOTAL
(see Section [6.12.12](../ch06_correlation/sec_CCcontrols.md)).

To request a CIS(D) calculation the METHOD *$rem* should be set to
CIS(D) and the number of excited states to calculate should be
specified by EE_STATES (or EE_SINGLETS and
EE_TRIPLETS when appropriate). Alternatively, CIS(D) will be
performed when EXCHANGE = HF, CORRELATION = CI
and EOM_CORR = CIS(D). The SF-CIS(D) is invoked by using
SF_STATES.

### `EE_STATES`

> **Sets the number of excited state roots to find. For closed-shell reference, defaults into EE_SINGLETS . For open-shell references, specifies all low-lying states.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ excited states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `EE_SINGLETS`

> **Sets the number of singlet excited state roots to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ excited states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `EE_TRIPLETS`

> **Sets the number of triplet excited state roots to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ excited states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `SF_STATES`

> **Sets the number of spin-flip target states roots to find.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ SF states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

!!! note "Note"
    It is a symmetry of a *transition* rather than that of a *target state*
    that is specified in excited state calculations. The symmetry of the
    target state is a product of the symmetry of the reference state and the
    transition. For closed-shell molecules, the former is fully symmetric and the
    symmetry of the target state is the same as that of transition, however, for
    open-shell references this is not so.


### `CC_STATE_TO_OPT`

> **Specifies which state to optimize.**
>
> * **Type**: `INTEGER ARRAY`
> * **Default**: `None`
> * **Options**:
>     * `[`: $i$ , $j$ ] optimize the $j$ th state of the $i$ th irrep.
> * **Recommendation**: None

!!! note "Note"
    Since there are no analytic gradients for CIS(D), the symmetry should be
    turned off for geometry optimization and frequency calculations, and
    CC_STATE_TO_OPT should be specified assuming $C_{1}$ symmetry, *i.e.*,
    as [1,N] where N is the number of state to optimize (the states are numbered
    from 1).


???+ example "Example 7.64: CIS(D) excitation energy calculation for ozone at the experimental ground
state geometry $C_{2v}$"
    ```qchem
    $molecule
       0 1
       O
       O  1  RE
       O  2  RE  1  A
    
       RE = 1.272
       A  = 116.8
    $end
    
    $rem
       METHOD           CIS(D)
       BASIS            6-31G*
       N_FROZEN_CORE    3            use frozen core
       EE_SINGLETS      [2,2,2,2]    find 2 lowest singlets in each irrep.
       EE_TRIPLETS      [2,2,2,2]    find 2 lowest triplets in each irrep.
       CCMAN2           false
    $end
    ```

???+ example "Example 7.65: CIS(D) geometry optimization for the lowest triplet state of water. The
symmetry is automatically turned off for finite difference calculations"
    ```qchem
    $molecule
       0 1
       o
       h  1  r
       h  1  r  2  a
    
       r  0.95
       a  104.0
    $end
    
    $rem
       JOBTYPE            opt
       BASIS              3-21g
       METHOD             cis(d)
       EE_TRIPLETS        1  calculate one lowest triplet
       CC_STATE_TO_OPT    [1,1] optimize the lowest state (1st state in 1st irrep)
    $end
    ```

???+ example "Example 7.66: CIS(D) excitation energy and transition property calculation (between all
states) for ozone at the experimental ground state geometry $C_{2v}$"
    ```qchem
    $molecule
       0 1
       O
       O  1  RE
       O  2  RE  1  A
    
       RE = 1.272
       A  = 116.8
    $end
    
    $rem
       BASIS              6-31G*
       PURCAR             2            Non-spherical (6D)
       METHOD             CIS(D)
       EE_SINGLETS        [2,2,2,2]
       EE_TRIPLETS        [2,2,2,2]
       CC_TRANS_PROP      1
       CCMAN2             FALSE
    $end
    ```
