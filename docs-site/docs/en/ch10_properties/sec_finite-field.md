---
title: "10.13.2 Numerical Calculation of Static Polarizabilities"
---

## 10.13.2 Numerical Calculation of Static Polarizabilities

(July 4, 2026)

Where analytic gradients are not available, static polarizabilities (only) can
be computed via finite-difference in the applied field, which is known as the
*finite field* (FF) approach. Beginning with **Q-Chem** 5.1, a
sophisticated “Romberg” approach to FF differentiation is available, which
includes procedures for assessing the stability of the results with respect to
the finite-difference step size. The Romberg approach is described in
Section [10.13.3](sect_Romberg.md). This section describes **Q-Chem**’s older approach
to FF calculations based on straightforward application of small electric
fields along the appropriate Cartesian directions.

Dipole moments can be calculated numerically as the first derivative of the
energy with respect to $\vec{F}$ by setting JOBTYPE = DIPOLE and
IDERIV = 0. If IDERIV is not specified explicitly, the dipole
moment will be calculated analytically, which for post-Hartree–Fock levels of
theory invokes a gradient calculation in order to utilize the relaxed wave function.

Similarly, set JOBTYPE = POLARIZABILITY for numerical
evaluation of the static polarizability tensor
$\mathord{\buildrel{\lower 3.0pt\hbox{$\scriptscriptstyle\leftrightarrow$}}\over{\alpha}}$. This is performed by either first-order finite difference, taking
first-order field derivatives of analytic dipole moments, or by second-order
finite difference of the energy. The latter is useful (indeed, required) for
methods where analytic gradients are not available, such as CCSD(T) for
example. Note, however, that the electron cloud is formally unbound in the
presence of static electric fields and therefore a bound solution is a
consequence of using a finite basis set. (With analytic derivative techniques
the perturbing field is infinitesimal so this is not an issue.) This fact,
along with the overall sensitivity of numerical derivatives to the
finite-difference step size, means that care must be taken in choosing the
strength of the applied finite field.

To control the order for numerical differentiation with respect to the applied
electric field, use IDERIV in the same manner as for geometric
derivatives, *i.e.*, for polarizabilties use IDERIV = 0 for second-order
finite-difference of the energy and IDERIV = 1 for first-order finite
difference of gradients. In addition, for numerical polarizabilities at the
Hartree-Fock or DFT level set RESPONSE_POLAR = $-1$ in order to disable
the analytic polarizability code.

### `RESPONSE_POLAR`

> **Control the use of analytic or numerical polarizabilities.**
>
> * **Type**: `INTEGER`
> * **Default**: `0 or`
> * **Options**:
>     * `0`: Perform an analytic polarizability calculation. $-$
>     * `1`: Perform a numeric polarizability calculation even when analytic 2nd derivatives are available.
> * **Recommendation**: None
