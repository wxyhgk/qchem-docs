---
title: "5.11.6 CDFT-CI Job Control and Examples"
---

## 5.11.6 CDFT-CI Job Control and Examples

(July 4, 2026)

### `CDFTCI`

> **Initiates a constrained DFT-configuration interaction calculation**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Perform a CDFT-CI Calculation
>     * `FALSE`: No CDFT-CI
> * **Recommendation**: Set to TRUE if a CDFT-CI calculation is desired.

### `CDFTCI_PRINT`

> **Controls level of output from CDFT-CI procedure to Q-Chem output file.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Only print energies and coefficients of CDFT-CI final states
>     * `1`: Level 0 plus CDFT-CI overlap, Hamiltonian, and population matrices
>     * `2`: Level 1 plus eigenvectors and eigenvalues of the CDFT-CI population matrix
>     * `3`: Level 2 plus promolecule orbital coefficients and energies
> * **Recommendation**: Level 3 is primarily for program debugging; levels 1 and 2 may be useful for analyzing the coupling elements

### `CDFT_LAMBDA_MODE`

> **Allows CDFT potentials to be specified directly, instead of being determined as Lagrange multipliers.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Standard CDFT calculations are used.
>     * `TRUE`: Instead of specifying target charge and spin constraints, use the values from the input deck as the value of the Becke weight potential
> * **Recommendation**: Should usually be set to FALSE. Setting to TRUE can be useful to scan over different strengths of charge or spin localization, as convergence properties are improved compared to regular CDFT(-CI) calculations.

### `CDFTCI_SKIP_PROMOLECULES`

> **Skips promolecule calculations and allows fractional charge and spin constraints to be specified directly.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Standard CDFT-CI calculation is performed.
>     * `TRUE`: Use the given charge/spin constraints directly, with no promolecule calculations.
> * **Recommendation**: Setting to TRUE can be useful for scanning over constraint values.

!!! note "Note"
    CDFT_LAMBDA_MODE and CDFTCI_SKIP_PROMOLECULES
    are mutually incompatible.


### `CDFTCI_SVD_THRESH`

> **By default, a symmetric orthogonalization is performed on the CDFT-CI matrix before diagonalization. If the CDFT-CI overlap matrix is nearly singular ( i.e. , some of the diabatic states are nearly degenerate), then this orthogonalization can lead to numerical instability. When computing $\mathbf{S}^{-1/2}$ , eigenvalues smaller than $10^{-\mathrm{CDFTCI\_SVD\_THRESH}}$ are discarded.**
>
> * **Type**: `INTEGER`
> * **Default**: `4`
> * **Options**:
>     * $n$: for a threshold of $10^{-n}$ .
> * **Recommendation**: Can be decreased if numerical instabilities are encountered in the final diagonalization.

### `CDFTCI_STOP`

> **The CDFT-CI procedure involves performing independent SCF calculations on distinct constrained states. It sometimes occurs that the same convergence parameters are not successful for all of the states of interest, so that a CDFT-CI calculation might converge one of these diabatic states but not the next. This variable allows a user to stop a CDFT-CI calculation after a certain number of states have been converged, with the ability to restart later on the next state, with different convergence options.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Stop after converging state
>     * $n$: (the first state is state $1$ ) $0$ Do not stop early
> * **Recommendation**: Use this setting if some diabatic states converge but others do not.

### `CDFTCI_RESTART`

> **To be used in conjunction with CDFTCI_STOP , this variable causes CDFT-CI to read already-converged states from disk and begin SCF convergence on later states. Note that the same $cdft section must be used for the stopped calculation and the restarted calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Start calculations on state $n+1$
> * **Recommendation**: Use this setting in conjunction with CDFTCI_STOP .

???+ example "Example 5.5.28: CDFT-CI calculation of couplings between the anionic GFP chromophore
(CHR:1–27) and a tyrosine (TYR:28–43) residue. The two diabatic states are
CHR( $M_{S}=0$ ) $\cdots$ TYR( $M_{S}=0$ ) and CHR( $M_{S}=1/2$ ) $\cdots$ TYR( $M_{S}=1/2$ )."
    ```qchem
    $molecule
       -1 1
       C        -1.453000       -1.953000       -0.264000
       N        -0.278000       -1.402000       -0.440000
       N        -1.804000       -2.052000        1.091000
       C        -0.687000       -1.548000        1.806000
       O        -0.688000       -1.514000        3.031000
       C         0.291000       -1.140000        0.799000
       C         1.500000       -0.563000        1.254000
       H         1.585000       -0.660000        2.346000
       C         2.608000        0.030000        0.605000
       C         2.763000        0.182000       -0.865000
       H         1.926000       -0.073000       -1.543000
       C         3.733000        0.548000        1.313000
       H         3.682000        0.571000        2.326000
       C         3.821000        0.875000       -1.473000
       H         3.844000        1.102000       -2.575000
       C         4.938000        1.111000        0.700000
       H         5.734000        1.441000        1.308000
       C         5.037000        1.228000       -0.739000
       O         6.011000        1.818000       -1.261000
       C        -3.000000       -2.533000        1.832000
       H        -2.859000       -2.250000        2.892000
       H        -3.829000       -2.121000        1.354000
       C        -2.373000       -2.282000       -1.448000
       H        -1.790000       -3.026000       -2.045000
       H        -2.626000       -1.300000       -1.865000
       H        -3.054000       -3.631000        1.855000
       H        -3.308000       -2.854000       -1.357000
       C         7.648000       -5.429000        0.303000
       H         8.028000       -4.514000        0.845000
       H         7.274000       -5.098000       -0.671000
       C         6.499001       -5.986000        1.016000
       C         6.462999       -6.032001        2.390000
       H         7.284000       -5.579000        2.957000
       C         5.243000       -6.435000        3.018000
       H         5.190001       -6.315001        4.035000
       C         4.242001       -7.048000        2.189000
       O         3.095000       -7.615000        2.715000
       H         2.500999       -7.869000        1.979000
       C         5.454000       -6.469000        0.200000
       H         5.565001       -6.363000       -0.835000
       C         4.294001       -7.003000        0.803000
       H         3.469000       -7.324000        0.139000
       H         8.511000       -6.108000        0.245000
    $end
    
    $rem
       METHOD           = b3lyp
       BASIS            = cc-pvdz
       UNRESTRICTED     = true
       SCF_CONVERGENCE  = 8
       MAX_SCF_CYCLES   = 200
       CDFTCI           = true
       CDFTCI_PRINT     = 2
       CDFT_THRESH      = 7
       INTEGRAL_SYMMETRY = off
       POINT_GROUP_SYMMETRY = false
    $end
    
    $cdft
       1.0
       1.0   1   27
       0.0
       1.0   1   27 S
    --------------
       0.0
       1.0   1   27
      -1.0
       1.0   1   27 S
    $end
    ```
