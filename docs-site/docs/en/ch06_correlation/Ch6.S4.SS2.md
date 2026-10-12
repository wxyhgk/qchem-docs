---
title: "6.4.2 Algorithm Control and Customization"
---

## 6.4.2 Algorithm Control and Customization

(July 4, 2026)

The direct and semi-direct integral transformation algorithms used by **Q-Chem**
(*e.g.*, MP2, CIS(D)) are limited by available disk space, $D$, and memory, $C$,
the number of basis functions, $N$, the number of virtual orbitals, $V$ and the
number of occupied orbitals, $O$, as discussed above. The generic description
of the key *$rem* variables are:

### `MEM_STATIC`

> **Sets the memory for Fortran AO integral calculation and transformation modules.**
>
> * **Type**: `INTEGER`
> * **Default**: `192`
> * **Options**:
>     * $n$: User-defined number of megabytes.
> * **Recommendation**: For direct and semi-direct MP2 calculations, this must exceed OVN + requirements for AO integral evaluation (32–160 MB), as discussed above.

### `MEM_TOTAL`

> **Sets the total memory available to Q-Chem , in megabytes.**
>
> * **Type**: `INTEGER`
> * **Default**: `2000`
> * **Options**:
>     * $n$: User-defined number of megabytes.
> * **Recommendation**: Use the default, or set equal to the physical memory of your machine. Note that if the memory allocation total more than 1 GB for a CCMAN job, the memory is allocated as follows 12% MEM_STATIC 50% CC_MEMORY 35% Other memory requirements:

### `CD_ALGORITHM`

> **Determines the algorithm for MP2 integral transformations.**
>
> * **Type**: `STRING`
> * **Default**: `Program determined.`
> * **Options**:
>     * `DIRECT`: Uses fully direct algorithm (energies only).
>     * `SEMI_DIRECT`: Uses disk-based semi-direct algorithm.
>     * `LOCAL_OCCUPIED`: Alternative energy algorithm (see 6.4.1 ).
> * **Recommendation**: Semi-direct is usually most efficient, and will normally be chosen by default.

???+ example "Example 6.1: Example of an MP2/6-31G* calculation employing the frozen core approximation.
Note that the EXCHANGE $rem variable will default to HF"
    ```qchem
    $molecule
       0 1
       O
       H1  O  oh
       H2  O  oh  H1  hoh
    
       oh  = 1.01
       hoh = 105
    $end
    
    $rem
       METHOD          mp2
       BASIS           6-31g*
       N_FROZEN_CORE   fc
    $end
    ```
