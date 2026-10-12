---
title: "6.18.1 Overview"
---

## 6.18.1 Overview

(July 4, 2026)

Memory footprint and execution time of coupled-cluster calculations can be
reduced by approximately a factor of 2 by using single-precision
arithmetic.[[1102]](../bib_references/bib.md#bib1149)
 The errors due to using single precision
are small and comparable with typical convergence thresholds.[[1102]](../bib_references/bib.md#bib1149)

If loss of accuracy is undesirable, one can follow up a converged single-precision
calculation with a small number of “clean-up” iterations in double precision,
which recover the full accuracy of a double-precision calculation.
Eventually, single-precision execution of
coupled-cluster calculations will become the default, however, for now setting
the single precision calculation needs to be done manually, as described below.

Single-precision capabilities are only available for the CCMAN2 suite. They work
with both variants of the tensor-contraction backend (controlled by
CC_BACKEND). Currently enabled features include energies, gradients,
and properties calculations for both canonical and RI/CD versions. Single-precision
versions of most EOM-CC methods are also available; the respective keywords are
described in Section [7.9.15](../ch07_excited/sec_SP_EOM_CC.md).

**Note: 

When using single-precision, the thresholds need to be adjusted accordingly, as
explained below. Using too tight convergence thresholds in single precision
results in a non-convergent behavior.
**

**Note: 

In rare cases, slow performance of the current code in single precision
with default CC_BACKEND was noted; this issue is being investigated.
Please monitor the performance and report any issues you encounter.
**

Webinar showing how to use the single-precision functionality in **Q-Chem**,
including the monitoring of errors.

To deploy a single- or a mixed-precision coupled-cluster calculation, use
CC_SINGLE_PREC. Its possible values are: $0$ (default corresponding to
double-precision calculation), $1$ (single-precision calculation), and $2$
(single-precision calculation followed by a couple of iterations in
double precision, to recover full accuracy).

To adjust the convergence thresholds in single-precision calculation, use
CC_SP_T_CONV (threshold for $T$ and $\Lambda$ amplitudes)
and CC_SP_E_CONV (threshold for energies).
Because too tight convergence criteria can cause non-convergent behavior,
these thresholds should not be tighter than $10^{-6}$ a.u. for energies and
$10^{-4}$ for amplitudes.

Calculations of intermediates, density matrices, and $\langle\hat{S}^{2}\rangle$ can also
be done in single precision, leading to negligible errors
in energies and optimized geometries. This is controlled by the CC_SP_DM variable: $0$ corresponds to calculation in
double precision, $1$ corresponds to calculation in single precision.

Calculation of perturbative triples corrections, (T) and (fT),
can be executed in single precision using **libpt**; additional keywords
deploying these features are USE_LIBPT and LIBPT_MIXED_PRECISION.

**Note: 

Calculation of numerical derivatives in single precision, such as
finite difference evaluation of nuclear gradients and finite-field calculations,
require using larger step sizes or field strengths, respectively.
**

### `CC_SINGLE_PREC`

> **Precision selection for CCSD calculation. Available in CCMAN2 only.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: single-precision calculation
>     * `2`: single-precision calculation followed by double-precision clean-up iterations
> * **Recommendation**: Do not set too tight convergence thresholds when using single precision

### `CC_SP_T_CONV`

> **Amplitude convergence threshold in single precision in CCSD calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * $n$: Corresponding to $10^{-n}$ convergence criterion
> * **Recommendation**: Set 4 to be consistent with the default threshold in double precision in a pure single-precision run. When used with clean-up version, it should be smaller than double-precision threshold not to introduce extra iterations.

### `CC_SP_E_CONV`

> **Energy convergence criterion in single precision in CCSD calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: Corresponding to $10^{-n}$ convergence criterion
> * **Recommendation**: Set 6 to be consistent with the default threshold in double precision in a pure single-precision calculation. When used with clean-up version, it should be smaller than double-precision threshold not to introduce extra iterations.

### `CC_SP_DM`

> **Precision selection for CCSD and EOM-CCSD intermediates, density matrices, gradients, and $\langle\hat{S}^{2}\rangle$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: single-precision calculation
> * **Recommendation**: NONE

### `CC_ERASE_DP_INTEGRALS`

> **Controls storage of requisite objects computed with double precision in a single-precision calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: do not store
> * **Recommendation**: Do not erase integrals if clean-up in double precision is intended.

### `LIBPT_MIXED_PRECISION`

> **Deploys single-precision evaluation of (T) and (fT) within libpt .**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: use single precision
> * **Recommendation**: Use in combination with USE_LIBPT .

???+ example "Example 6.51: A job evaluating CCSD and CCSD(T) energy using single-precision execution"
    ```qchem
    $comment
       Uracil+H2O cc-pvdz
       CCSD(T) energy
    $end
    
    $molecule
       0 1
       N      0.034130   -0.986909    0.000000
       N     -1.173397    0.981920    0.000000
       C     -1.218805   -0.408164    0.000000
       C     -0.007302    1.702153    0.000000
       C      1.196200    1.107045    0.000000
       C      1.289085   -0.345905    0.000000
       O      2.310232   -0.996874    0.000000
       O     -2.257041   -1.026495    0.000000
       H      0.049329   -1.997961    0.000000
       H     -2.070598    1.437050    0.000000
       H     -0.125651    2.776484    0.000000
       H      2.111671    1.674079    0.000000
       O      1.747914   -1.338382   -3.040233
       H      2.180817   -1.817552   -2.333676
       H      0.813180   -1.472188   -2.883392
    $end
    
    $rem
       METHOD                  ccsd(t)
       BASIS                   cc-pvdz
       USE_LIBPT               true  evaluate triples with libpt code
       CC_SINGLE_PREC          1
       EOM_SINGLE_PREC         1
       CC_SP_DM                1
       CC_SP_T_CONV            4
       CC_SP_E_CONV            6
       CC_ERASE_DP_INTEGRALS   1
       LIBPT_MIXED_PRECISION   1
    $end
    ```
