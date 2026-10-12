---
title: "9.2.2 Optimize Job Control"
---

## 9.2.2 **Optimize** Job Control

(July 4, 2026)

### `GEOM_OPT_HESSIAN`

> **Determines the initial Hessian status.**
>
> * **Type**: `STRING/INTEGER`
> * **Default**: `$-$`
> * **Options**:
>     * $-$
>     * `1`: Approximate Hessian based on the force constant matrix (same as the “Model” option in Libopt3 )
>     * `READ`: Have exact or initial Hessian. Use as is if Cartesian, or transform if internals.
> * **Recommendation**: An accurate initial Hessian will improve the performance of the optimizer, but it may be expensive to compute. Note that more options for the initial Hessian are available in Libopt3 , controlled by INITIAL_HESSIAN under the $geom_opt section (see Sec. 9.2.5 ).

### `GEOM_OPT_COORDS`

> **Controls the type of optimization coordinates.**
>
> * **Type**: `INTEGER`
> * **Default**: `$-$`
> * **Options**:
>     * `0`: Optimize in Cartesian coordinates.
>     * `1`: Generate and optimize in internal coordinates, if this fails abort. $-$
>     * `1`: Generate and optimize in internal coordinates, if this fails at any stage of the optimization, switch to Cartesian and continue.
>     * `2`: Optimize in $Z$ -matrix coordinates, if this fails abort. $-$
>     * `2`: Optimize in $Z$ -matrix coordinates, if this fails during any stage of the optimization switch to Cartesians and continue.
> * **Recommendation**: Use the default, as delocalized internals are more efficient. Note that optimization in $Z$ -matrix coordinates requires that the input be specified in $Z$ -matrix format.

### `GEOM_OPT_TOL_GRADIENT`

> **Convergence on maximum gradient component.**
>
> * **Type**: `INTEGER`
> * **Default**: `300`
> * **Options**:
>     * $n$: Integer value (tolerance = $n\times 10^{-6}$ ).
> * **Recommendation**: Use the default. To converge and one of GEOM_OPT_TOL_DISPLACEMENT and GEOM_OPT_TOL_ENERGY must be satisfied.

### `GEOM_OPT_TOL_DISPLACEMENT`

> **Convergence on maximum atomic displacement.**
>
> * **Type**: `INTEGER`
> * **Default**: `1200`
> * **Options**:
>     * $n$: Integer value (tolerance = $n\times 10^{-6}$ ).
> * **Recommendation**: Use the default. To converge GEOM_OPT_TOL_GRADIENT and one of and GEOM_OPT_TOL_ENERGY must be satisfied.

### `GEOM_OPT_TOL_ENERGY`

> **Convergence on energy change of successive optimization cycles.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$: Integer value (tolerance = value $n\times 10^{-8}$ ).
> * **Recommendation**: Use the default. To converge GEOM_OPT_TOL_GRADIENT and one of GEOM_OPT_TOL_DISPLACEMENT and must be satisfied.

### `GEOM_OPT_MAX_CYCLES`

> **Maximum number of optimization cycles.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $n$: User defined positive integer.
> * **Recommendation**: The default should be sufficient for most cases. Increase if the initial guess geometry is poor, or for systems with shallow potential wells.

### `GEOM_OPT_PRINT`

> **Controls the amount of Optimize print output.**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * `0`: Error messages only.
>     * `1`: Level 0 plus summary and warning print out.
>     * `2`: Level 1 plus standard information.
>     * `3`: Level 2 plus gradient print out.
>     * `4`: Level 3 plus Hessian print out.
>     * `5`: Level 4 plus iterative print out.
>     * `6`: Level 5 plus internal generation print out.
>     * `7`: Debug print out.
> * **Recommendation**: Use the default.

### `GEOM_OPT_SYMFLAG`

> **Controls the use of symmetry in Optimize .**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`: Make use of point group symmetry.
>     * `FALSE`: Do not make use of point group symmetry.
> * **Recommendation**: Use the default.

### `GEOM_OPT_MODE`

> **Determines Hessian mode followed during a transition state search.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Mode following off.
>     * $n$: Maximize along mode
>     * $n$: .
> * **Recommendation**: Use the default, for geometry optimizations.

### `GEOM_OPT_MAX_DIIS`

> **Controls maximum size of subspace for GDIIS.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not use GDIIS.
>     * `-1`: Default size = min(NDEG, NATOMS, 4) NDEG = number of molecular degrees of freedom.
>     * $n$: Size specified by user.
> * **Recommendation**: Use the default or do not set $n$ too large.

### `GEOM_OPT_DMAX`

> **Maximum allowed step size. Value supplied is multiplied by 10 ${}^{-3}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `300`
> * **Options**:
>     * $n$: User-defined cutoff.
> * **Recommendation**: Use the default.

### `GEOM_OPT_UPDATE`

> **Controls the Hessian update algorithm.**
>
> * **Type**: `INTEGER`
> * **Default**: `-1`
> * **Options**:
>     * `-1`: Use the default update algorithm.
>     * `0`: Do not update the Hessian (not recommended).
>     * `1`: Murtagh-Sargent update.
>     * `2`: Powell update.
>     * `3`: Powell/Murtagh-Sargent update (TS default).
>     * `4`: BFGS update (OPT default).
>     * `5`: BFGS with safeguards to ensure retention of positive definiteness (GDIIS default).
> * **Recommendation**: Use the default.

### `GEOM_OPT_LINEAR_ANGLE`

> **Threshold for near linear bond angles (degrees).**
>
> * **Type**: `INTEGER`
> * **Default**: `165 degrees.`
> * **Options**:
>     * $n$: User-defined level.
> * **Recommendation**: Use the default.

### `FINITEDIFFSZ_POWER`

> **The exponent controlling the order of magnitude of the step size used for calculating derivatives by finite difference.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: Use an exponent of $10^{-n}$ .
> * **Recommendation**: None.

### `FDIFF_STEPSIZE`

> **Displacement used for calculating derivatives by finite difference.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$: Use a step size of $n\times 10^{-m}$ , where
>     * $m$: is FINITEDIFFSZ_POWER .
> * **Recommendation**: Use the default except in cases where the potential surface is very flat in which case a larger value should be used. See FDIFF_STEPSIZE_QFF for third and fourth derivatives.
