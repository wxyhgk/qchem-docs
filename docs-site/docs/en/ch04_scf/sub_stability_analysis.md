---
title: "4.5.17 Internal Stability Analysis and Automated Correction for Energy Minima"
---

## 4.5.17 Internal Stability Analysis and Automated Correction for Energy Minima

(July 4, 2026)

At convergence, the SCF energy will be at a stationary point with respect to
changes in the MO coefficients. However, this stationary point is not
guaranteed to be an energy minimum, and in cases where it is not, the wave
function is said to be unstable. Even if the wave function is at a minimum,
this minimum may be an artifact of the constraints placed on the form of the
wave function. For example, an unrestricted calculation will usually give a
lower energy than the corresponding restricted calculation, and this can give
rise to an RHF $\rightarrow$ UHF instability.

Based on our experience, even for very simple data set such as the G2
atomization energies,[[293]](../bib_references/bib.md#bib298)
 using the default algorithm (DIIS)
produces unstable solutions for several species (even for single atoms with
some density functionals). In such cases, failure to check the internal
stability of SCF solutions can result in flawed benchmark results. Although in
general the use of gradient-based algorithms such as GDM is more likely to
locate the true minimum, it still cannot entirely eliminate the possibility
of finding an unstable solution.

To understand what instabilities can occur, it is useful to consider the most
general form possible for the spin orbitals:

<a id="eq427"></a>

$$
\chi_{i}({\rm{\bf r}},\zeta)=\psi_{i}^{\alpha}({\rm{\bf r}})\alpha(\zeta)+\psi_{i}^{\beta}({\rm{\bf r}})\beta(\zeta)\;. \tag{4.45}
$$

Here, $\psi_{i}^{\alpha}$ and $\psi_{i}^{\beta}$ are complex-valued functions of the
Cartesian coordinates $\mathbf{r}$, and $\alpha$ and $\beta$ are spin eigenfunctions
of the spin-variable $\zeta$. The first constraint that is almost universally
applied is to assume the spin orbitals depend only on one or other of the
spin-functions $\alpha$ or $\beta$. Thus, the spin-functions take the form

<a id="Ch4.E46"></a>

$$
\chi_{i}(\mathbf{r},\zeta)=\psi_{i}^{\alpha}(\mathbf{r})\alpha(\zeta)\quad\mathrm{or}\quad\chi_{i}(\mathbf{r},\zeta)=\psi_{i}^{\beta}(\mathbf{r})\beta(\zeta)\;. \tag{4.46}
$$

In addition, most SCF calculations use real functions, and this places an
additional constraint on the form of the wave function. If there exists a
complex solution to the SCF equations that has a lower energy, the wave
function exhibits a real $\rightarrow$ complex instability. The final constraint
that is commonly placed on the spin-functions is that $\psi_{i}^{\alpha}=\psi_{i}^{\beta}$, *i.e.*, that the spatial parts of the spin-up and spin-down
orbitals are the same. This gives the familiar restricted formalism and can
lead to an RHF $\rightarrow$ UHF instability as mentioned above. Further details about
the possible instabilities can be found in Ref. [[1227]](../bib_references/bib.md#bib1282)
.

Wave function instabilities can arise for several reasons, but frequently occur if

- There exists a singlet diradical at a lower energy then the closed-shell
singlet state.
- There exists a triplet state at a lower energy than the lowest singlet
state.
- There are multiple solutions to the SCF equations, and the calculation
has not found the lowest energy solution.

**Q-Chem**’s previous stability analysis package suffered from the following
limitations:

- It is only available for restricted (close-shell) and unrestricted SCF
calculations.
- It requires the analytical orbital Hessian of the wave function energy.
- The calculation terminates after the corrected MOs are generated, and a
second job is needed to read in these orbitals and run another SCF
calculation.

The implementation of internal stability analysis in GEN_SCFMAN overcomes
almost all these shortcomings. Its availability has been extended to all the
implemented orbital types. As in the old code, when the analytical Hessian of
the given orbital type and theory (*e.g.* RO/B3LYP) is available, it computes
matrix-vector products analytically for the Davidson
algorithm.[[307]](../bib_references/bib.md#bib311)
 If the analytical Hessian is not available, users
can still run stability analysis by using the finite-difference matrix-vector
product technique developed by Sharada *et al.*,[[1244]](../bib_references/bib.md#bib1298)
 which
requires the gradient (related to the Fock matrix) only:

<a id="eq:fd_mat_vec"></a>

$$
\mathbf{Hb}_{1}=\frac{\hat{\bm{\nabla}}E(\mathbf{X}_{0}+\xi\mathbf{b}_{1})-\hat{\bm{\nabla}}E(\mathbf{X}_{0}-\xi\mathbf{b}_{1})}{2\xi} \tag{4.47}
$$

where $\mathbf{H}$ is the Hessian matrix, $\mathbf{b}_{1}$ is a trial vector,
$\mathbf{X}_{0}$ stands for the current stationary point, and $\xi$ is the finite
step size. With this method, internal stability analysis is available for all
the implemented orbital types in GEN_SCFMAN. It should be noted that since
the second derivative of NLC functionals (except for VV10) is not available in
**Q-Chem**, this finite-difference method will be used by default for the
evaluation of Hessian-vector products.

GEN_SCFMAN allows multiple SCF calculations and stability analyses to be
performed in a single job so that it can make use of the corrected MOs and
locate the true minimum automatically. The MOs are displaced along the
direction of the lowest-energy eigenvector (with line search) if an SCF
solution is found to be unstable. A new SCF calculation that reads in these
corrected MOs as initial guess will be launched automatically if
INTERNAL_STABILITY_ITER > 0. Such macro-loops will keep going until
a stable solution is reached.

!!! note "Note"
    The stability analysis package can be used to analyze both HF and DFT
    wave functions.


## 4.5.17.1 Job Control

### `INTERNAL_STABILITY`

> **Perform internal stability analysis in GEN_SCFMAN.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not perform internal stability analysis after convergence.
>     * `TRUE`: Perform internal stability analysis and generate the corrected MOs.
> * **Recommendation**: Turn it on when the SCF solution is prone to unstable solutions, especially for open-shell species.

### `FD_MAT_VEC_PROD`

> **Compute Hessian-vector product using the finite difference technique.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE (TRUE when the employed functional contains non-local correlation (except VV10))`
> * **Options**:
>     * `FALSE`: Compute Hessian-vector product analytically.
>     * `TRUE`: Use finite difference to compute Hessian-vector product.
> * **Recommendation**: Set it to TRUE when analytical Hessian is not available. Note: For simple R and USCF calculations, it can always be set to FALSE , which indicates that only the NLC part will be computed with finite difference (if its analytic orbital hessian is unavailable).

### `INTERNAL_STABILITY_ITER`

> **Maximum number of new SCF calculations permitted after the first stability analysis is performed.**
>
> * **Type**: `INTEGER`
> * **Default**: `0 (automatically set to 1 if`
> * **Options**:
>     * $n$
>     * $n$: new SCF calculations permitted.
> * **Recommendation**: Give a larger number if 1 is not enough (still unstable).

### `INTERNAL_STABILITY_DAVIDSON_ITER`

> **Maximum number of Davidson iterations allowed in one stability analysis.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $n$: Perform up to
>     * $n$: Davidson iterations.
> * **Recommendation**: Use the default.

### `INTERNAL_STABILITY_CONV`

> **Convergence criterion for the Davidson solver (for the lowest eigenvalues).**
>
> * **Type**: `INTEGER`
> * **Default**: `4 (3 when`
> * **Options**:
>     * $n$: Terminate Davidson iterations when the norm of the residual vector is below 10 ${}^{-n}$ .
> * **Recommendation**: Use the default.

### `INTERNAL_STABILITY_ROOTS`

> **Number of lowest Hessian eigenvalues to solve for.**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * $n$: Solve for
>     * $n$: lowest eigenvalues.
> * **Recommendation**: Use the default.

???+ example "Example 4.18: Unrestricted SCF calculation of triplet B ${}_{2}$ using B97M-V/6-31g with the GDM
algorithm. A displacement is performed when the first solution is
characterized as a saddle point, and the second SCF gives a stable solution."
    ```qchem
    $molecule
       0 3
       b
       b 1 R
    
       R = 1.587553
    $end
    
    $rem
       METHOD               b97m-v
       BASIS                6-31g
       UNRESTRICTED         true
       THRESH               14
       SCF_FINAL_PRINT      1
       SCF_ALGORITHM        gdm
       SCF_CONVERGENCE      8
       INTERNAL_STABILITY   true  ! turn on internal stability analysis
       FD_MAT_VEC_PROD      false ! use finite-diff for the vv10 part only
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```
