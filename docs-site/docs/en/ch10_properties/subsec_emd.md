---
title: "10.2.13 Earth Mover’s Distance Analysis"
---

## 10.2.13 Earth Mover’s Distance Analysis

(July 4, 2026)

The Earth Mover’s Distance (EMD) provides a physically intuitive metric for comparing two charge distributions by quantifying
the minimum transport cost required to transform one distribution into the other. [[1432]](../bib_references/bib.md#bib1494)
 In the context of excited-state analysis,
EMD offers a real-space measure of charge rearrangement and therefore complements more traditional descriptors of charge transfer
and density redistribution. The exact evaluation of EMD requires solution of an optimal transport problem, which can become computationally
expensive for large grids. To make this analysis practical for routine applications, **Q-Chem** provides an entropically regularized formulation
based on the Sinkhorn–Knopp algorithm, together with a reduced-grid representation of the charge distribution, in order to obtain an
efficient approximation to the exact EMD while retaining its essential physical interpretation.

## 10.2.13.1 Theory

Let $\mathbf{r}$ and $\mathbf{c}$ denote two discrete nonnegative distributions defined on a real-space grid, with equal total weight.
In the EMD framework, these are interpreted as the source and target distributions, respectively. For a distance matrix $\mathbf{M}$,
whose elements $M_{ij}$ represent the distance between grid points $i$ and $j$, the Earth Mover’s Distance is defined as

<a id="Ch10.E37"></a>
$$
d_{\mathbf{M}}(\mathbf{r},\mathbf{c})=\min_{\mathbf{P}\in U(\mathbf{r},\mathbf{c})}\langle\mathbf{P},\mathbf{M}\rangle=\min_{\mathbf{P}\in U(\mathbf{r},\mathbf{c})}\sum_{ij}P_{ij}M_{ij}, \tag{10.37}
$$

where $\mathbf{P}$ is the transport plan and

<a id="Ch10.E38"></a>
$$
U(\mathbf{r},\mathbf{c})=\left\{\mathbf{P}\in\mathbb{R}_{+}^{d\times d}\;\middle|\;\mathbf{P}\mathbf{1}=\mathbf{r},\;\mathbf{P}^{T}\mathbf{1}=\mathbf{c}\right\}. \tag{10.38}
$$

The admissible transport plans are therefore constrained to reproduce the prescribed source and target marginals. In other words,
each row sum of $\mathbf{P}$ must equal the source distribution, and each column sum must equal the target distribution.

In the present application, the source and target distributions are constructed from the positive and negative parts of the real-space
density difference associated with an excitation. Let

<a id="Ch10.E39"></a>
$$
\Delta\rho(\mathbf{r})=\rho^{\mathrm{ES}}(\mathbf{r})-\rho^{\mathrm{GS}}(\mathbf{r}), \tag{10.39}
$$

where $\rho^{\mathrm{GS}}(\mathbf{r})$ and $\rho^{\mathrm{ES}}(\mathbf{r})$ are the ground-state and excited-state densities, respectively.
The positive and negative components of the density difference define the two charge distributions to be compared,

<a id="Ch10.E40"></a>
$$
\rho^{+}(\mathbf{r})=\max\!\bigl{(}\Delta\rho(\mathbf{r}),0\bigr{)},\qquad\rho^{-}(\mathbf{r})=\max\!\bigl{(}-\Delta\rho(\mathbf{r}),0\bigr{)}. \tag{10.40}
$$

After discretization on a grid with points $\{\mathbf{r}_{i}\}$ and quadrature weights $\{w_{i}\}$, the effective charge
associated with each grid point is

<a id="Ch10.E41"></a>
$$
q_{i}=w_{i}\rho(\mathbf{r}_{i}), \tag{10.41}
$$

and the two nonnegative discrete distributions entering the EMD problem are obtained from the positive and negative components of the density
difference. The total transferred charge is then

<a id="Ch10.E42"></a>
$$
q^{\mathrm{CT}}=\sum_{i}q_{i}^{+}=\sum_{j}q_{j}^{-}, \tag{10.42}
$$

and the corresponding transport cost,

<a id="Ch10.E43"></a>
$$
\mu^{\mathrm{EMD}}=\min_{\mathbf{P}\in U(\mathbf{r},\mathbf{c})}\sum_{ij}P_{ij}M_{ij}, \tag{10.43}
$$

has units of charge times distance. A corresponding length-like quantity may be defined as

<a id="Ch10.E44"></a>
$$
d^{\mathrm{EMD}}=\frac{\mu^{\mathrm{EMD}}}{q^{\mathrm{CT}}}. \tag{10.44}
$$

The exact EMD may be obtained by solving this constrained optimization problem using a transportation simplex algorithm. While this approach
yields the exact optimal transport cost, its computational cost grows rapidly with grid size and can become prohibitive for large systems or dense real-space grids.

## 10.2.13.2 Grid Selection for Efficient EMD Calculations

A direct EMD calculation on the full quadrature grid used in a DFT or TDDFT calculation is generally impractical because the number of grid points may be very large.
Since the optimal transport problem scales unfavorably with the size of the discrete distributions, the present implementation employs a reduced grid for the EMD evaluation.

In this procedure, the electronic density is first evaluated on the underlying quadrature grid used in the electronic-structure calculation. A smaller atom-centered grid
is then introduced for the EMD analysis. Each grid point from the original quadrature grid is assigned to a point on the smaller EMD grid according to spatial proximity, and
the effective charges from the original grid are accumulated onto the selected EMD grid. In this way, the fine-grid density is projected onto a smaller discrete representation
that preserves the overall distribution while substantially reducing the number of points entering the transport problem.

Let $\{\mathbf{r}_{k}^{\mathrm{big}},w_{k}^{\mathrm{big}},\rho_{k}^{\mathrm{big}}\}$ denote the grid points, weights, and densities on the original quadrature grid, and
let $\{\mathbf{r}_{i}^{\mathrm{small}}\}$ denote the reduced grid used for the EMD evaluation. The effective charge assigned to point $i$ on the reduced grid is constructed by
accumulating the charges from all original grid points associated with that reduced point,

<a id="Ch10.E45"></a>
$$
q_{i}^{\mathrm{small}}=\sum_{k\in\Omega_{i}}w_{k}^{\mathrm{big}}\rho_{k}^{\mathrm{big}}, \tag{10.45}
$$

where $\Omega_{i}$ denotes the set of original grid points assigned to reduced grid point $i$. The resulting reduced-grid charges are then used to define the source
and target distributions entering the EMD calculation.

This reduced-grid procedure greatly lowers the cost of both exact and regularized EMD calculations while retaining a physically meaningful representation of the density
difference. The reduced grid is chosen from standard atom-centered quadrature grids in **Q-Chem**. The quality of the EMD result therefore depends on the quality of the
reduced-grid representation of the density difference, and convergence with respect to the EMD grid should be checked whenever high quantitative accuracy is required.

## 10.2.13.3 Entropically Regularized Optimal Transport

To further reduce the cost of the EMD evaluation, one may replace the exact optimal transport problem by an entropically regularized one,

<a id="Ch10.E46"></a>
$$
\mathbf{P}^{\lambda}=\arg\min_{\mathbf{P}\in U(\mathbf{r},\mathbf{c})}\left[\langle\mathbf{P},\mathbf{M}\rangle-\frac{1}{\lambda}h(\mathbf{P})\right], \tag{10.46}
$$

where $h(\mathbf{P})$ is the entropy of the transport plan and $\lambda$ is the regularization parameter. The corresponding regularized transport cost is

<a id="Ch10.E47"></a>
$$
d_{\mathbf{M}}^{\lambda}(\mathbf{r},\mathbf{c})=\langle\mathbf{P}^{\lambda},\mathbf{M}\rangle. \tag{10.47}
$$

The entropy term favors smoother transport plans and removes the need to solve the original linear programming problem directly. The parameter $\lambda$ controls
the balance between smoothness and fidelity to the exact EMD. Larger values of $\lambda$ reduce the influence of the entropy term and drive the solution closer to
the exact EMD, whereas smaller values of $\lambda$ produce a smoother transport plan and generally improve numerical stability.

The regularized problem admits a factorized form for the optimal transport plan,

<a id="Ch10.E48"></a>
$$
\mathbf{P}^{\lambda}=\mathrm{diag}(\mathbf{u})\,\mathbf{K}\,\mathrm{diag}(\mathbf{v}), \tag{10.48}
$$

where

<a id="eq:emd_kernel"></a>
$$
K_{ij}=e^{-\lambda M_{ij}}. \tag{10.49}
$$

The vectors $\mathbf{u}$ and $\mathbf{v}$ are positive scaling factors chosen such that the transport plan satisfies the marginal constraints,

<a id="Ch10.E50"></a>
$$
\mathbf{P}^{\lambda}\mathbf{1}=\mathbf{r},\qquad(\mathbf{P}^{\lambda})^{T}\mathbf{1}=\mathbf{c}. \tag{10.50}
$$

Substituting the factorized form into these constraints yields the coupled fixed-point equations

<a id="Ch10.E51"></a>
$$
u_{i}=\frac{r_{i}}{(\mathbf{K}\mathbf{v})_{i}},\qquad v_{j}=\frac{c_{j}}{(\mathbf{K}^{T}\mathbf{u})_{j}}. \tag{10.51}
$$

These equations form the basis of the Sinkhorn–Knopp algorithm, 

 which alternates updates of $\mathbf{u}$ and $\mathbf{v}$ until the marginal
constraints are satisfied to within a specified threshold.

The computational steps of the method are therefore as follows. First, the density difference is evaluated on the underlying quadrature grid.
Second, the associated charges are projected onto a smaller EMD grid. Third, the distance matrix $\mathbf{M}$ is constructed on that reduced grid,
and the kernel matrix $\mathbf{K}$ is formed according to Eq. ([10.49](#eq:emd_kernel)). Finally, the Sinkhorn iterations are performed to obtain the
regularized transport plan and the corresponding transport cost. The dominant cost of the regularized method is associated with repeated matrix-vector
products involving $\mathbf{K}$ and $\mathbf{K}^{T}$, which is substantially less expensive than solving the exact transportation simplex problem for large grids.

In practice, the principal numerical parameter is the regularization strength $\lambda$. This parameter must be chosen large enough that the regularized
transport cost remains close to the exact EMD, but not so large that the kernel matrix becomes severely ill-conditioned. If $\lambda M_{ij}$ is too large,
the exponential kernel may underflow, leading to unstable scaling vectors and poor convergence behavior. The present implementation therefore exposes
user-adjustable regularization and convergence parameters, where The user-specified regularization parameter is scaled by the maximum element of the distance matrix.
In other words, the effective regularization strength used in the calculation is $\lambda_{\mathrm{eff}}=\frac{\lambda_{\mathrm{in}}}{M_{ij}^{\max}}$, where
$M_{ij}^{\max}=\max_{ij}M_{ij}$. In general, increasing $\lambda_{\mathrm{eff}}$ improves agreement with the exact EMD, whereas decreasing
$\lambda_{\mathrm{eff}}$ improves numerical stability and convergence behavior.

In summary, this feature evaluates the Earth Mover’s Distance between two discrete charge distributions on a real-space grid either using exact transport algorithm or using an entropically regularized optimal
transport formulation solved by the Sinkhorn–Knopp algorithm, with a reduced atom-centered grid for the EMD calculation rather than the full quadrature grid employed in the underlying
electronic-structure calculation. The quality of the result therefore depends both on the EMD grid and on the regularization parameters. The principal user-controlled options are the
activation of EMD analysis itself EMD_ANALYSIS, the grid used for constructing the reduced real-space charge distributions EMD_FIT_GRID, the use of the Sinkhorn
solver SINKHORN, the regularization strength for Sinkhorn solver SINKHORN_REG, the convergence threshold for Sinkhorn solver SINKHORN_THRESHOLD, and the maximum
cycles MAX_SINKHORN_CYCLES. Larger regularization parameters generally improve agreement with the exact EMD but may lead to numerical instability if the kernel matrix becomes too
sharply peaked. Smaller regularization parameters improve numerical robustness, but introduce a larger approximation error relative to the exact EMD.

EMD_ANALYSIS

### `EMD_ANALYSIS`

> **Controls whether Earth Mover’s Distance (EMD) analysis is performed.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not perform EMD analysis.
>     * TRUE
>     * Perform EMD analysis.
> * **Recommendation**: This keyword activates the evaluation of the Earth Mover’s Distance between the positive and negative parts of the real-space density difference. The corresponding charge distributions are constructed on the grid specified by EMD_FIT_GRID .

EMD_FIT_GRID

### `EMD_FIT_GRID`

> **Specifies the atom-centered grid used to construct the reduced real-space charge distributions for Earth Mover’s Distance (EMD) analysis.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $N$
>     * Grid specification
>     * $N$
>     * is in the same format as
>     * XC_GRID
>     * .
> * **Recommendation**: This keyword defines the grid used for the reduced-grid representation of the density difference entering the EMD calculation. The input format is the same as for XC_GRID , but it should be equal or smaller than XC_GRID . A recommended choice is 19000026, and for larger molecules an even smaller grid may be used with only a small loss of accuracy. A denser grid generally improves the quality of the EMD result, but also increases the computational cost of the transport problem.

SINKHORN

### `SINKHORN`

> **Controls whether the entropically regularized Sinkhorn–Knopp algorithm is used for the EMD calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Use the exact transportation simplex algorithm.
>     * TRUE
>     * Use the entropically regularized Sinkhorn–Knopp algorithm.
> * **Recommendation**: The Sinkhorn–Knopp algorithm provides an efficient approximation to the exact Earth Mover’s Distance and is generally preferable for large grids. The corresponding regularization strength is controlled by SINKHORN_REG .

MAX_SINKHORN_CYCLES

### `MAX_SINKHORN_CYCLES`

> **Controls the maximum number of Sinkhorn–Knopp iterations used in the EMD calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $N$
>     * Perform at most
>     * $N$
>     * Sinkhorn iterations.
> * **Recommendation**: Increase this value if the Sinkhorn iterations do not converge within the default number of cycles. This keyword is only relevant when SINKHORN is set to 1.

SINKHORN_THRESHOLD

### `SINKHORN_THRESHOLD`

> **Controls the convergence threshold for the Sinkhorn–Knopp iterations.**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * $N$
>     * Converge the Sinkhorn iterations to a threshold of
>     * $10^{-N}$
>     * .
> * **Recommendation**: Smaller values of $N$ correspond to a looser convergence criterion, while larger values correspond to tighter convergence. This keyword is only relevant when SINKHORN is set to 1.

SINKHORN_REG

### `SINKHORN_REG`

> **Controls the regularization strength used in the entropically regularized Sinkhorn EMD calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $N$
>     * Use a regularization parameter of
>     * $N$
>     * for the Sinkhorn kernel.
> * **Recommendation**: This keyword controls the strength of the entropic regularization in the Sinkhorn formulation of the EMD problem. Larger values generally yield results closer to the exact EMD, but may also lead to numerical instability or slower convergence. Smaller values are more numerically robust, but increase the deviation from the exact optimal transport solution. In the present implementation, the user-specified regularization parameter is internally scaled by the maximum element of the distance matrix before the Sinkhorn kernel is constructed. This keyword is only relevant when SINKHORN is set to 1.

???+ example "Example 10.10: Basic TDDFT calculation with PBE functional for water molecule with EMD analysis for the first three excited singlet and triplet states
with the accurate transportation simplex method algorithm."
    ```qchem
    $molecule
    0 1
    O   0.000000   0.000000   0.000000
    H   0.758602   0.000000   0.504284
    H  -0.758602   0.000000   0.504284
    $end
    
    $rem
    METHOD PBE
    BASIS aug-cc-pVDZ
    CIS_N_ROOTS 3
    CIS_SINGLETS TRUE
    CIS_TRIPLETS TRUE
    STATE_ANALYSIS TRUE
    XC_GRID 50000194
    EMD_ANALYSIS TRUE
    EMD_FIT_GRID 19000026
    SINKHORN FALSE
    SCF_CONVERGENCE 8
    THRESH 13
    N_FROZEN_CORE 0
    $end
    
    ```

???+ example "Example 10.11: Basic TDDFT calculation with PBE functional for water molecule with EMD analysis for the first three excited singlet and triplet states
with the approximate Sinkhorn–Knopp algorithm."
    ```qchem
    $molecule
    0 1
    O   0.000000   0.000000   0.000000
    H   0.758602   0.000000   0.504284
    H  -0.758602   0.000000   0.504284
    $end
    
    $rem
    METHOD PBE
    BASIS aug-cc-pVDZ
    CIS_N_ROOTS 3
    CIS_SINGLETS TRUE
    CIS_TRIPLETS TRUE
    STATE_ANALYSIS TRUE
    XC_GRID 50000194
    EMD_ANALYSIS TRUE
    EMD_FIT_GRID 19000026
    SINKHORN TRUE
    SINKHORN_THRESHOLD 3
    MAX_SINKHORN_CYCLES 30
    SINKHORN_REG 200
    SCF_CONVERGENCE 8
    THRESH 13
    N_FROZEN_CORE 0
    $end
    
    ```
