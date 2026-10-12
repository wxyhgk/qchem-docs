---
title: "8.3.2 Customization"
---

## 8.3.2 Customization

(July 4, 2026)

**Q-Chem** offers a number of standard and special customization features. One
of the most important is that of supplying additional diffuse functions.
Diffuse functions are often important for studying anions and excited states of
molecules, and for the latter several sets of additional diffuse functions may
be required. These extra diffuse functions can be generated from the standard
diffuse functions by applying a scaling factor to the exponent of the original
diffuse function. This yields a geometric series of exponents for the diffuse
functions which includes the original standard functions along with more diffuse functions.

When using very large basis sets, especially those that include many diffuse
functions, or if the system being studied is very large, linear dependence in
the basis set may arise. This results in an over-complete description of the
space spanned by the basis functions, and can cause a loss of uniqueness in the
molecular orbital coefficients. Consequently, the SCF may be slow to converge
or behave erratically. **Q-Chem** will automatically check for linear dependence
in the basis set, and will project out the near-degeneracies, if they exist.
This will result in there being slightly fewer molecular orbitals than there are
basis functions. **Q-Chem** checks for linear dependence by considering the
eigenvalues of the overlap matrix. Very small eigenvalues are an indication
that the basis set is close to being linearly dependent. The size at which the
eigenvalues are considered to be too small is governed by the *$rem* variable
BASIS_LIN_DEP_THRESH. By default this is set to 6, corresponding to
a threshold of $10^{-6}$. This has been found to give reliable results, however SCF
convergence failure (especially for large molecules or those with highly diffuse basis sets)
may be a symptom of linear dependencies. The smallest
overlap matrix eigenvalue is printed in the **Q-Chem** output file, and usually when
this number goes below $10^{-5}$, numerical issues caused by basis function linear
dependence may occur and the SCF calculation may not give reasonable solutions.
If the smallest overlap matrix eigenvalue is less than the
square root of the integral threshold, a warning message will be printed urging the
use to set THRESH = 14. Especially for larger molecules, and in basis sets
that contain diffuse functions, tightening the integral threshold sometimes has the nonintuitive
effect of *decreasing* the time-to-solution, by significantly reducing the number of SCF cycles
at only a modest per-cycle increase in cost.[[479]](../bib_references/bib.md#bib495)

### `PRINT_GENERAL_BASIS`

> **Controls print out of built in basis sets in input format**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Print out standard basis set information
>     * `FALSE`: Do not print out standard basis set information
> * **Recommendation**: Useful for modification of standard basis sets.

### `BASIS_LIN_DEP_THRESH`

> **Sets the threshold for determining linear dependence in the basis set**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n$: Sets the threshold to $10^{-n}$
> * **Recommendation**: Set to 5 or smaller if you have a poorly behaved SCF and you suspect linear dependence in you basis set. Lower values (larger thresholds) may affect the accuracy of the calculation.
