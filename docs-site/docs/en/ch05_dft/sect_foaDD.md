---
title: "5.12.2 Derivative Discontinuity Restoration"
---

## 5.12.2 Derivative Discontinuity Restoration

(July 4, 2026)

From the perspective of perturbation theory, Chai and Chen[[222]](../bib_references/bib.md#bib227)

proposed a systematic procedure for the evaluation of the derivative
discontinuity of the exchange-correlation energy functional in Kohn-Sham
DFT, wherein the exact derivative discontinuity can in principle be obtained by
summing up all the perturbation corrections to infinite order. Truncation of
the perturbation series at low order yields an efficient scheme for obtaining
the approximate derivative discontinuity. In particular, the first-order
correction term is equivalent to the frozen-orbital approximation method. Its
implementation in **Q-Chem** supports only local and GGA functionals at present,
not meta-GGA, hybrid, or non-local functionals. Job control variables and examples appear below.

### `FOA_FUNDGAP`

> **Compute the frozen-orbital approximation of the fundamental gap.**
>
> * **Type**: `Boolean`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not compute FOA derivative discontinuity and fundamental gap.
>     * `TRUE`: Compute and print FOA fundamental gap information. Implies KS_GAP_PRINT .
> * **Recommendation**: Use in conjunction with KS_GAP_UNIT if true.

### `KS_GAP_PRINT`

> **Control printing of (generalized Kohn-Sham) HOMO-LUMO gap information.**
>
> * **Type**: `Boolean`
> * **Default**: `false`
> * **Options**:
>     * `false`: (default) do not print gap information
>     * `true`: print gap information
> * **Recommendation**: Use in conjunction with KS_GAP_UNIT if true.

### `KS_GAP_UNIT`

> **Unit for KS_GAP_PRINT and FOA_FUNDGAP (see Section 5.12.2 )**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: (default) hartrees
>     * `1`: eV
> * **Recommendation**: none

???+ example "Example 5.29: Frozen-orbital approximation of derivative discontinuity with
PBE and LFAs-PBE functionals on carbon atom."
    ```qchem
    $comment
        Frozen-orbital derivative discontinuity, C atom, PBE
    $end
    
    $molecule
       0 3
       C
    $end
    
    $rem
       BASIS         6-31G*
       METHOD        PBE
       FOA_FUNDGAP   true
       KS_GAP_UNIT   1    ! print gap info in eV
       THRESH        14
    $end
    
    @@@
    
    $comment
       with LFAs-PBE functional instead
    $end
    
    $molecule
       READ
    $end
    
    $rem
       BASIS         6-31G*
       SCF_GUESS     READ
       EXCHANGE      gen
       FOA_FUNDGAP   true
       KS_GAP_UNIT   1
       THRESH        14
    $end
    
    $xc_functional
       X   PBE    1.0
       X   LFAs   1.0
       C   PBE    1.0
    $end
    ```
