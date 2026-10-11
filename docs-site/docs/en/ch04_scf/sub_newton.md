---
title: "4.5.11 Newton Methods"
---

## 4.5.11 Newton Methods

(July 4, 2026)

**Q-Chem** also offers various Newton methods for converging SCF problems. In these
methods, the step to take in the orbital rotation space is calculated as $\boldsymbol{\Delta}=-\mathbf{H}^{-1}\mathbf{g}$, where $\mathbf{g}$ and $\mathbf{H}$ are the gradient
and *exact* Hessian of the SCF energy with respect to the orbital rotation variables,
respectively. In the quadratic regime in the vicinity of an energy minimum, the Hessian
matrix is positive definite and by taking Newton steps the minimum can be reached
very efficiently, usually within very few steps. However, when far from the minimum the
Hessian matrix is often indefinite and a Newton step may not even lead to descending.
Since to obtain SCF orbital Hessian (Hessian-vector products in the actual
implementation) is computationally demanding, it is typically recommended to perform
SCF calculations using another algorithm (*e.g.* GDM) and then start using Newton
methods after the error is below a certain threshold. See Section [4.5.12](sub_custom_algorithm.md)
for job control details for general hybrid-algorithm calculations and the examples therein.
In addition, a line search algorithm is employed in the **Q-Chem** implementation of
Newton methods to prevent them from overstepping.

In the actual implementation of these methods in **Q-Chem**, the Newton steps are calculated
by iteratively solving the linear equation $\mathbf{H}\boldsymbol{\Delta}=-\mathbf{g}$.
This avoids the explicit evaluation and inversion of the SCF orbital Hessian and thus is
computationally more efficient. The conjugate-gradient (CG) and minimal residual (MINRES)
solvers are currently supported, which correspond to the NEWTON_CG and
NEWTON_MINRES algorithms in **Q-Chem**, respectively. The CG method requires
the Hessian matrix to be positive definite, which may not be satisfied when far from
convergence. In those cases, the CG iterations will be terminated when negative curvature
is detected (based on $(\mathbf{p}^{(i)})^{T}\mathbf{H}\mathbf{p}^{(i)}<0$, where
$\mathbf{p}^{(i)}$ is the update to the solution vector $\boldsymbol{\Delta}^{(i)}$ at the $i$-th
iteration. Then the unconverged $\boldsymbol{\Delta}^{(i)}$ will be adopted as the update
direction (see Ref. 

 for details). The MINRES algorithm, on the
other hand, doesn’t require the Hessian matrix to be positive definite, so this method will be
able to solve for $\boldsymbol{\Delta}$ in most cases except when singularity exists. However,
as mentioned above, the obtained update (orbital rotation) may not lead to descending in
energy when the Hessian is not positive definite.

A “saddle-free” Newton-CG algorithm (SF_NEWTON_CG) is also implemented in
**Q-Chem**. This methods aims to restore the curvature of the Hessian matrix when negative
eigenvalues are present by using the following modified Hessian:

<a id="eq:sf_newton"></a>

$$
\widetilde{\mathbf{H}}=\mathbf{H}-\mathbf{v}_{-}\lambda_{-}\mathbf{v}_{-}^{T} \tag{4.44}
$$

where $\lambda_{-}$ is a diagonal matrix formed by negative eigenvalues and $\mathbf{v}_{-}$
represents the corresponding eigenvectors. At each iteration, the algorithm will start with solving
for a few lowest eigenvalues and eigenvectors using the Davidson algorithm, and then CG will be
used to solve $\widetilde{\mathbf{H}}\boldsymbol{\Delta}=-\mathbf{g}$, where the modified Hessian
is guaranteed to be positive definite.

???+ example "Example 4.15: SCF calculation for a water molecule using the NEWTON_CG algorithm"
    ```qchem
    $molecule
    0 1
       O  -1.551007  -0.114520   0.000000
       H  -1.934259   0.762503   0.000000
       H  -0.599677   0.040712   0.000000
    $end
    
    $rem
       jobtype  sp
       method   b3lyp
       basis    6-31g(d)
       scf_algorithm   newton_cg
       scf_convergence 9
    $end
    ```
