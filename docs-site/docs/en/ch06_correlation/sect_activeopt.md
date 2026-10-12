---
title: "6.14.6 Convergence Strategies and More Advanced Options"
---

## 6.14.6 Convergence Strategies and More Advanced Options

(July 4, 2026)

These optimized orbital coupled-cluster active space methods enable the use of
the full valence space for larger systems than is possible with conventional
complete active space codes. However, we should note at the outset that often
there are substantial challenges in converging valence active space
calculations (and even sometimes optimized orbital coupled cluster calculations
without an active space). Active space calculations cannot be regarded as
“routine” calculations in the same way as SCF calculations, and often require
a considerable amount of computational trial and error to persuade them to
converge. These difficulties are largely because of strong coupling between the
orbital degrees of freedom and the amplitude degrees of freedom, as well as the
fact that the energy surface is often quite flat with respect to the orbital
variations defining the active space.

Being aware of this at the outset, and realizing that the program has nothing
against you personally is useful information for the uninitiated user of these
methods. What the program does have, to assist in the struggle to achieve a
converged solution, are accordingly many convergence options, fully documented
in Appendix [B](../app_b_quickref/app_quick_ref.md). In this section, we describe the basic options
and the ideas behind using them as a starting point. Experience plays a
critical role, however, and so we encourage you to experiment with toy jobs
that give rapid feedback in order to become proficient at diagnosing problems.

If the default procedure fails to converge, the first useful option to employ
is CC_PRECONV_T2Z, with a value of between 10 and 50. This is useful
for jobs in which the MP2 amplitudes are very poor guesses for the converged
cluster amplitudes, and therefore initial iterations varying only the
amplitudes will be beneficial:

### `CC_PRECONV_T2Z`

> **Whether to pre-converge the cluster amplitudes before beginning orbital optimization in optimized orbital cluster methods.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: No pre-convergence before orbital optimization.
>     * $n$: Up to
>     * $n$: iterations in this pre-convergence procedure.
> * **Recommendation**: Experiment with this option in cases of convergence failure.

Other options that are useful include those that permit some damping of step
sizes, and modify or disable the standard DIIS procedure. The main choices are
as follows.

### `CC_DIIS`

> **Specify the version of Pulay’s Direct Inversion of the Iterative Subspace (DIIS) convergence accelerator to be used in the coupled-cluster code.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Activates procedure 2 initially, and procedure 1 when gradients are smaller than DIIS12_SWITCH .
>     * `1`: Uses error vectors defined as differences between parameter vectors from successive iterations. Most efficient near convergence.
>     * `2`: Error vectors are defined as gradients scaled by square root of the approximate diagonal Hessian. Most efficient far from convergence.
> * **Recommendation**: DIIS1 can be more stable. If DIIS problems are encountered in the early stages of a calculation (when gradients are large) try DIIS1.

### `CC_DIIS_START`

> **Iteration number when DIIS is turned on. Set to a large number to disable DIIS.**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * $n$
>     * `User-defined`
> * **Recommendation**: Occasionally DIIS can cause optimized orbital coupled-cluster calculations to diverge through large orbital changes. If this is seen, DIIS should be disabled.

### `CC_DOV_THRESH`

> **Specifies minimum allowed values for the coupled-cluster energy denominators. Smaller values are replaced by this constant during early iterations only, so the final results are unaffected, but initial convergence is improved when the guess is poor.**
>
> * **Type**: `INTEGER`
> * **Default**: `$2502$`
> * **Options**:
>     * $abcde$: Integer code is mapped to $abc\times 10^{-de}$
> * **Recommendation**: Increase to 0.5 or 0.75 for non convergent coupled-cluster calculations.

!!! note "Note"
    Works only for CCMAN jobs, not enabled in CCMAN2.


### `CC_THETA_STEPSIZE`

> **Scale factor for the orbital rotation step size. The optimal rotation steps should be approximately equal to the gradient vector.**
>
> * **Type**: `INTEGER`
> * **Default**: `$100$`
> * **Options**:
>     * $abcde$: Integer code is mapped to $abc\times 10^{-de}$ If the initial step is smaller than 0.5, the program will increase step when gradients are smaller than the value of THETA_GRAD_THRESH , up to a limit of 0.5.
> * **Recommendation**: Try a smaller value in cases of poor convergence and very large orbital gradients. For example, a value of 01001 translates to 0.1

An even stronger—and more-or-less last resort—option permits iteration of the
cluster amplitudes without changing the orbitals:

### `CC_PRECONV_T2Z_EACH`

> **Whether to pre-converge the cluster amplitudes before each change of the orbitals in optimized orbital coupled-cluster methods. The maximum number of iterations in this pre-convergence procedure is given by the value of this parameter.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: No pre-convergence before orbital optimization.
>     * $n$: Up to
>     * $n$: iterations in this pre-convergence procedure.
> * **Recommendation**: A very slow last resort option for jobs that do not converge.
