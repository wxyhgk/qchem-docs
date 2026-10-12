---
title: "7.8.7 RI-CIS(D), SOS-CIS(D), and SOS-CIS(D 0 ): Job Controls and Examples"
---

## 7.8.7 RI-CIS(D), SOS-CIS(D), and SOS-CIS(D${}_{0}$): Job Controls and Examples

(July 4, 2026)

These methods are activated by setting the *$rem* keyword METHOD to
RICIS(D), SOSCIS(D), and SOSCIS(D0), respectively.
Other keywords are the same as in CIS method explained in
Section [7.2.2](subsec_CIS.md). As these methods rely on the RI approximation,
AUX_BASIS needs to be set by following the same guide as in RI-MP2
(Section [6.6](../ch06_correlation/topic_rimp2.md)).

### `METHOD`

> **Excited state method of choice**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `RICIS(D)`: Activate RI-CIS(D) SOSCIS(D) Activate SOS-CIS(D) SOSCIS(D0) Activate SOS-CIS(D ${}_{0}$ )
> * **Recommendation**: None

### `CIS_N_ROOTS`

> **Sets the number of excited state roots to find**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: $n>0$ Looks for
>     * $n$: excited states
> * **Recommendation**: None

### `CIS_SINGLETS`

> **Solve for singlet excited states (ignored for spin unrestricted systems)**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Solve for singlet states
>     * `FALSE`: Do not solve for singlet states.
> * **Recommendation**: None

### `CIS_TRIPLETS`

> **Solve for triplet excited states (ignored for spin unrestricted systems)**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Solve for triplet states
>     * `FALSE`: Do not solve for triplet states.
> * **Recommendation**: None

### `CIS_STATE_DERIV`

> **Sets the excited state index for analytical gradient calculation for geometry optimizations and vibrational analysis with SOS-CIS(D ${}_{0}$ )**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Select the
>     * $n$: th state.
> * **Recommendation**: Check to see that the states do no change order during an optimization. For closed-shell systems, either CIS_SINGLETS or CIS_TRIPLETS must be set to false.

### `MEM_STATIC`

> **Sets the memory for individual program modules**
>
> * **Type**: `INTEGER`
> * **Default**: `192`
> * **Options**:
>     * $n$: User-defined number of megabytes.
> * **Recommendation**: At least $150(N^{2}+N)D$ of is required ( $N$ : number of basis functions, $D$ : size of a double precision storage, usually 8). Because a number of matrices with $N^{2}$ size also need to be stored, 32–160 MB of additional is needed.

### `MEM_TOTAL`

> **Sets the total memory available to Q-Chem**
>
> * **Type**: `INTEGER`
> * **Default**: `2000`
> * **Options**:
>     * $n$: User-defined number of megabytes
> * **Recommendation**: The minimum memory requirement of RI-CIS(D) is approximately MEM_STATIC + max $(3SVXD,3X^{2}D)$ ( $S$ : number of excited states, $X$ : number of auxiliary basis functions, $D$ : size of a double precision storage, usually 8). However, because RI-CIS(D) uses a batching scheme for efficient evaluations of electron repulsion integrals, specifying more memory will significantly speed up the calculation. Put as much memory as possible if you are not sure what to use, but never put any more than what is available. The minimum memory requirement of SOS-CIS(D) and SOS-CIS(D ${}_{0}$ ) is approximately MEM_STATIC + $20X^{2}D$ . SOS-CIS(D ${}_{0}$ ) gradient calculation becomes more efficient when $30X^{2}D$ more memory space is given. Like in RI-CIS(D), put as much memory as possible if you are not sure what to use. The actual memory size used in these calculations will be printed out in the output file to give a guide about the required memory.

### `SOS_FACTOR`

> **Sets the scaling parameter $c_{T}$**
>
> * **Type**: `INTEGER`
> * **Default**: `1300000`
> * **Options**:
>     * $n$: $c_{T}=n/1000000$
> * **Recommendation**: Use the default

### `SOS_UFACTOR`

> **Sets the scaling parameter $c_{U}$**
>
> * **Type**: `INTEGER`
> * **Default**: `151`
> * **Options**:
>     * $n$: $c_{U}=n/100$
> * **Recommendation**: Use the default

???+ example "Example 7.67: Input for an RI-CIS(D) calculation."
    ```qchem
    $molecule
       0 1
       C     0.667472     0.000000     0.000000
       C    -0.667472     0.000000     0.000000
       H     1.237553     0.922911     0.000000
       H     1.237553    -0.922911     0.000000
       H    -1.237553     0.922911     0.000000
       H    -1.237553    -0.922911     0.000000
    $end
    
    $rem
       METHOD          ricis(d)
       BASIS           aug-cc-pVDZ
       MEM_TOTAL       1000
       MEM_STATIC      100
       AO2MO_DISK      1000
       AUX_BASIS       rimp2-aug-cc-pVDZ
       PURECART        1111
       CIS_N_ROOTS     10
       CIS_SINGLETS    true
       CIS_TRIPLETS    false
    $end
    ```

???+ example "Example 7.68: Input for an SOS-CIS(D) calculation."
    ```qchem
    $molecule
       0 1
       C    -0.627782     0.141553     0.000000
       O     0.730618    -0.073475     0.000000
       H    -1.133677    -0.033018    -0.942848
       H    -1.133677    -0.033018     0.942848
    $end
    
    $rem
       METHOD          soscis(d)
       BASIS           aug-cc-pVDZ
       MEM_TOTAL       1000
       MEM_STATIC      100
       AO2MO_DISK      500000     ! 0.5 Terabyte of disk space available
       AUX_BASIS       rimp2-aug-cc-pVDZ
       PURECART        1111
       CIS_N_ROOTS     5
       CIS_SINGLETS    true
       CIS_TRIPLETS    true
    $end
    ```

???+ example "Example 7.69: Input for an SOS-CIS(D ${}_{0}$ ) geometry optimization on S ${}_{2}$ surface."
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
       JOBTYPE           = opt
       METHOD            = soscis(d0)
       BASIS             = 6-31G**
       AUX_BASIS         = rimp2-VDZ
       PURECART          = 1112
       CIS_STATE_DERIV   = 2
       CIS_N_ROOTS       = 5
       CIS_SINGLETS      = true
       CIS_TRIPLETS      = false
    $end
    ```
