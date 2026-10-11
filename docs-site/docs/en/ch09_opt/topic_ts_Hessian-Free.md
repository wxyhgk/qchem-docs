---
title: "9.2.3 Hessian-Free Characterization of Stationary Points"
---

## 9.2.3 Hessian-Free Characterization of Stationary Points

(July 4, 2026)

**Q-Chem** allows the user to characterize the stationary point found by a
geometry optimization or transition state search without performing a full
analytical Hessian calculation, which is sometimes unavailable or
computationally unaffordable. This is achieved via a finite difference Davidson
procedure developed by Sharada *et al.*[[1243]](../bib_references/bib.md#bib1297)
 For a geometry
optimization, it solves for the lowest eigenvalue of the Hessian ($\lambda_{1}$)
and checks if $\lambda_{1}>0$ (a negative $\lambda_{1}$ indicates a saddle
point); for a TS search, it solves for the lowest two eigenvalues, and
$\lambda_{1}<0$ and $\lambda_{2}>0$ indicate a transition state. The lowest
eigenvectors of the updated P-RFO (approximate) Hessian at convergence are used
as the initial guess for the Davidson solver.

The cost of this Hessian-free characterization method depends on the rate of
convergence of the Davidson solver. For example, to characterize an energy
minimum, it requires $2\times N_{\mathrm{iter}}$ total energy + gradient calculations,
where $N_{\mathrm{iter}}$ is the number of iterations that the Davidson algorithm
needs to converge, and “2" is for forward and backward displacements on each
iteration. According to Ref. [[1243]](../bib_references/bib.md#bib1297)
, this method can be much
more efficient than exact Hessian calculation for substantially large systems.

**Note: 

At the moment, this method does not support QM/MM or systems with fixed atoms.
**

GEOM_OPT_CHARAC

### `GEOM_OPT_CHARAC`

> **Use the finite difference Davidson method to characterize the resulting energy minimum/transition state.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * do not characterize the resulting stationary point.
>     * TRUE
>     * perform a characterization of the stationary point.
> * **Recommendation**: Set it to TRUE when the character of a stationary point needs to be verified, especially for a transition structure.

GEOM_OPT_CHARAC_CONV

### `GEOM_OPT_CHARAC_CONV`

> **Overide the built-in convergence criterion for the Davidson solver.**
>
> * **Type**: `INTEGER`
> * **Default**: `0 (use the built-in default value 10`
> * **Options**:
>     * $n$
>     * Set the convergence criterion to 10
>     * ${}^{-n}$
>     * .
> * **Recommendation**: Use the default. If it fails to converge, consider loosening the criterion with caution.
