---
title: "7.9.15 Single-Precision Arithmetic in EOM-CC Calculations"
---

## 7.9.15 Single-Precision Arithmetic in EOM-CC Calculations

(July 4, 2026)

Similar to ground-state CCSD calculations described in Section [6.18](../ch06_correlation/sec_SP_CC.md),
single precision can be used in EOM-CC, EOM-MP2, and EOM-CC2 calculations.[[1102]](../bib_references/bib.md#bib1149)

Currently, the following variants of EOM are supported: EE, SF,IP, EA, DIP, DEA;
both in standard and RI/CD implementations, for energies, gradients, and properties evaluation.
If you wish to use single-precision version of EOM, please first read Section [6.18](../ch06_correlation/sec_SP_CC.md) for
basic setup of single-precision coupled-cluster calculation.
Here we describe only additional EOM-specific keywords.

Precision selection is controlled by the
EOM_SINGLE_PREC keyword:
$0$ corresponds to double-precision calculation and $1$ corresponds to single-precision calculation.
EOM-specific convergence criteria are controlled by the same keywords as in the
double precision, but the same rule as for CCSD applies: too tight thresholds may
cause issues with convergence. The default Davidson threshold $10^{-5}$ works well for
most cases.[[1102]](../bib_references/bib.md#bib1149)

The keyword CC_SP_DM controls calculation of intermediates, density matrices,
and $\hat{S}^{2}$ for EOM calculations in the same manner as for CCSD, which is described in Section [6.18](../ch06_correlation/sec_SP_CC.md).

Calculations of analytical gradients require solving amplitude-response equations,
which can be done in single precision as well; this is
activated by EOM_ARESP_SINGLE_PREC = 1.
For using single precision in calculating response equations for 2PA calculations, use the
CC_EOM_2PA_SINGLE_PREC keyword (see also Section [7.9.21.6](sec_EOMGRAD.md#sec:2PA)).

### `EOM_SINGLE_PREC`

> **Precision selection for EOM-CC/MP2 calculations. Available in CCMAN2 only.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: single-precision calculation
>     * `2`: single-precision calculation is followed by double-precision clean-up iterations
> * **Recommendation**: Do not set too tight convergence criteria when use single precision

### `CC_EOM_2PA_SINGLE_PREC`

> **Precision selection for 2PA response equations. Available in CCMAN2 only.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: single-precision calculation
> * **Recommendation**: NONE

**Note: 

Remember to adjust convergence thresholds when using single precision.
**

???+ example "Example 7.92: A job evaluating EOM-EA-CCSD energies for formaldehyde anion using
single-precision execution combined with CD"
    ```qchem
    $comment
       Formaldehyde anion, single-precision calculation
    $end
    
    $molecule
       0 1
       C
       H  1  1.127888
       H  1  1.127888  2  100.546614
    $end
    
    $rem
       BASIS                 = cc-pvdz
       METHOD                = ccsd
       CHOLESKY_TOL          = 3
       EA_STATES             = [1,0,0,0]
       CC_REF_PROP           = 1   Compute properties of the CCSD reference
       !SP keywords
       CC_SINGLE_PREC        = 1
       CC_SP_T_CONV          = 4
       CC_SP_E_CONV          = 6
       CC_ERASE_DP_INTEGRALS = 0 ! set 1 to save disk space
       CC_SP_DM              = 1
       !EOM-specific keyword
       EOM_SINGLE_PREC       = 1
    $end
    ```

???+ example "Example 7.93: Geometry optimization of a triplet excited state of uracil-water complex
in single-precision setup"
    ```qchem
    $molecule
       0 1
       N     0.034130    -.986909    0.000000
       N    -1.173397     .981920    0.000000
       C    -1.218805    -.408164    0.000000
       C    -0.007302    1.702153    0.000000
       C     1.196200    1.107045    0.000000
       C     1.289085    -.345905    0.000000
       O     2.310232    -.996874    0.000000
       O    -2.257041   -1.026495    0.000000
       H     0.049329   -1.997961    0.000000
       H    -2.070598    1.437050    0.000000
       H    -0.125651    2.776484    0.000000
       H     2.111671    1.674079    0.000000
       O     1.747914   -1.338382   -3.040233
       H     2.180817   -1.817552   -2.333676
       H     0.813180   -1.472188   -2.883392
    $end
    
    $rem
       JOB_TYPE              = opt
       METHOD                = ccsd
       BASIS                 = cc-pvdz
       CC_STATE_TO_OPT       = [1,1]
       MEM_TOTAL             = 30000
       EE_TRIPLETS           = [1]
       CC_SP_T_CONV          = 4
       CC_SP_E_CONV          = 6
       CC_SINGLE_PREC        = 1
       EOM_SINGLE_PREC       = 1
       CC_SP_DM              = 1
       CC_EOM_PROP           = 1
       EOM_ARESP_SINGLE_PREC = 1
    $end
    
    ```
