---
title: "10.7 Finite-Difference Properties"
---

# 10.7 Finite-Difference Properties

(July 4, 2026)

Q-Chem offers the option of computing several properties that
can be expressed as derivatives of static (electric or magnetic) fields
and/or coordinates. This set of properties include nuclear gradients
and Hessians (harmonic and anharmonic frequencies), polarizabilities,
hyperpolarizabilities, dipole moment, NMR shielding, magnetizabilities,
and more. This option is particularly desirable for methods for which
analytic derivatives of desired order are unavailable.

Q-Chem also provides options to use predefined stencils for first-
and second-order finite-difference derivatives
through the use of the FDIFF_STENCIL keyword.
For first-order finite-difference derivatives such as gradients or Hessians
using analytic gradients, stencils yielding ${\cal{O}}({h^{2}})$ and ${\cal{O}}({h^{4}})$
errors are available; the former through the setting
FDIFF_STENCIL = 1 or 2 (default) and the latter through the setting
FDIFF_STENCIL = 3 or 4. Traditionally, in the context of first-order
derivatives, these are the 3-point and 5-point stencils, respectively.
For second-order finite-difference derivatives such as
Hessians using energies, economical ${\cal{O}}({h^{2}})$ (default),
regular ${\cal{O}}({h^{2}})$, and economical ${\cal{O}}({h^{4}})$
stencils are available through the setting FDIFF_STENCIL = 1, 2, and 3, respectively.

Finite-difference calculations consist of multiple, mutually independent evaluations,
forming an embarassingly parallel workload. Starting v6.3.0,
such calculations (except anharmonic frequency calcuations)
can exploit Q-Chem’s new hybrid MPI+OpenMP approach: the independent
finite-difference steps are distributed across MPI ranks,
while each rank exploits OpenMP for shared-memory parallelism within a node.
This strategy is particularly effective for large systems,
providing excellent scalability with minimal communication overhead.

### `IDERIV`

> **Controls the order of derivatives that are evaluated analytically. The user is not normally required to specify a value, unless numerical derivatives are desired. The derivatives will be evaluated numerically if is set lower than JOBTYPE requires.**
>
> * **Type**: `INTEGER`
> * **Default**: `Set to the order of derivative that`
> * **Options**:
>     * `2`: Analytic second derivatives of the energy (Hessian)
>     * `1`: Analytic first derivatives of the energy.
>     * `0`: Analytic energies only.
> * **Recommendation**: Usually set to the maximum possible for efficiency. Note that will be set lower if analytic derivatives of the requested order are not available.

### `FDIFF_STEPSIZE_QFF`

> **Displacement used for calculating third and fourth derivatives by finite difference.**
>
> * **Type**: `INTEGER`
> * **Default**: `5291`
> * **Options**:
>     * $n$: Use a step size of $n\times 10^{-5}$ .
> * **Recommendation**: Use the default, unless the potential surface is very flat, in which case a larger value should be used.

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

### `FDIFF_STEPSIZE_B`

> **External static magnetic field used for calculating derivatives by finite difference.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$: Use a step size of $n\times 10^{-m}$ , where
>     * $m$: is FINITEDIFFSZ_POWER .
> * **Recommendation**: None.

### `FDIFF_STEPSIZE_M`

> **Nuclear magnetic-moment field used for calculating derivatives by finite difference.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$: Use a step size of $n\times 10^{-m}$ , where
>     * $m$: is FINITEDIFFSZ_POWER .
> * **Recommendation**: None.

### `FDIFF_STENCIL`

> **Specifies the stencil to be used in the finite-difference calculation of first- and second-order derivatives.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: Corresponds to regular ${\cal{O}}({h^{2}})$ stencil for first-order and economical ${\cal{O}}({h^{2}})$ stencil for second-order finite-difference calculation. $2$ Corresponds to regular ${\cal{O}}({h^{2}})$ stencil for first-order and regular ${\cal{O}}({h^{2}})$ stencil for second-order finite-difference calculation. $3$ Corresponds to regular ${\cal{O}}({h^{4}})$ stencil for first-order and economical ${\cal{O}}({h^{4}})$ stencil for second-order finite-difference calculation. $4$ Corresponds to regular ${\cal{O}}({h^{4}})$ stencil for first-order finite-difference calculation. This option is unavailable in v. 6.4 for second-order finite-difference calculation.
> * **Recommendation**: None.
