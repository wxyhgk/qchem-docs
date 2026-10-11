---
title: "9.1.7 GDIIS Algorithm"
---

## 9.1.7 GDIIS Algorithm

(July 4, 2026)

Direct inversion in the iterative subspace (DIIS) was originally developed by
Pulay for accelerating SCF convergence.[[1137]](../bib_references/bib.md#bib1183)
 Subsequently, Csaszar
and Pulay used a similar scheme for geometry optimization, which they termed
GDIIS.[[285]](../bib_references/bib.md#bib289)
 The method is somewhat different from the usual
quasi-Newton type approach and is included in **Optimize** as an alternative to
the EF algorithm. Tests indicate that its performance is similar to EF, at
least for small systems, however, there is rarely an advantage in using GDIIS
in preference to EF.

In GDIIS geometries generated in previous optimization cycles, $\mathbf{x}_{i}$, are
linearly combined to find the “best” geometry for the current cycle

<a id="eq:a23"></a>
$$
\mathbf{x}_{n}=\sum\limits_{i=1}^{m}c_{i}\mathbf{x}_{i} \tag{9.33}
$$

where the problem is to find the best values for the coefficients $c_{i}$.

If we express each geometry by its deviation from the sought-after
final geometry, $\mathbf{x}_{f}$, *i.e.*, $\mathbf{x}_{f}=\mathbf{x}_{i}+\mathbf{e}_{i}$, where
$\mathbf{e}_{i}$ is an error vector, then it is obvious that if the conditions

<a id="eq:a24"></a>
$$
\mathbf{r}=\sum c_{i}\mathbf{e}_{i} \tag{9.34}
$$

and

<a id="eq:a25"></a>
$$
\sum{c_{i}}=1 \tag{9.35}
$$

are satisfied, then the relation

<a id="Ch9.E36"></a>
$$
\sum c_{i}\mathbf{x}_{i}=\mathbf{x}_{f} \tag{9.36}
$$

also holds.

The true error vectors $\mathbf{e}_{i}$ are, of course, unknown. However, in the case
of a nearly quadratic energy function they can be approximated by

<a id="Ch9.E37"></a>
$$
\mathbf{e}_{i}=-\mathbf{H}^{-1}\mathbf{g}_{i} \tag{9.37}
$$

where $\mathbf{g}_{i}$ is the gradient vector corresponding to the geometry $\mathbf{x}_{i}$
and $\mathbf{H}$ is an approximation to the Hessian matrix. Minimization of the
norm of the residuum vector $\mathbf{r}$, Eq. ([9.34](#eq:a24)), together with the constraint
equation, Eq. ([9.35](#eq:a25)), leads to a system of $m+l$ linear equations

<a id="eq:a28"></a>
$$
\left({{\begin{array}[]{c c c c}{B_{11}}&\cdots&{B_{1m}}&1\\
\vdots&\ddots&\vdots&\vdots\\
{B_{m1}}&\cdots&{B_{mm}}&1\\
1&\cdots&1&0\\
\end{array}}}\right)\left({{\begin{array}[]{c}{c_{1}}\\
\vdots\\
{c_{m}}\\
{-\lambda}\\
\end{array}}}\right)=\left({{\begin{array}[]{c}0\\
\vdots\\
0\\
1\\
\end{array}}}\right) \tag{9.38}
$$

where $B_{ij}=\langle\mathbf{e}_{i}|\mathbf{e}_{j}\rangle$ is the scalar product of the error
vectors $\mathbf{e}_{i}$ and $\mathbf{e}_{j}$, and $\lambda$ is a Lagrange multiplier.

The coefficients $c_{i}$ determined from Eq. ([9.38](#eq:a28)) are used to calculate an
intermediate interpolated geometry

<a id="Ch9.E39"></a>
$$
\mathbf{x}_{m+1}^{\prime}=\sum c_{i}\mathbf{x}_{i} \tag{9.39}
$$

and its corresponding interpolated gradient

<a id="Ch9.E40"></a>
$$
\mathbf{g}_{m+1}^{\prime}=\sum c_{i}\mathbf{g}_{i} \tag{9.40}
$$

A new, independent geometry is generated from the interpolated geometry and
gradient according to

<a id="Ch9.E41"></a>
$$
\mathbf{x}_{m+1}=\mathbf{x}_{m+1}^{\prime}-\mathbf{H}^{-1}\mathbf{g}_{m+1}^{\prime}\;. \tag{9.41}
$$

**Note: 

Convergence is theoretically guaranteed regardless of the quality of the
Hessian matrix, as long as it is positive definite. The original GDIIS
algorithm used a static Hessian (*i.e.* the initial guess Hessian) which was
often a simple identity matrix. Updating the Hessian at each cycle generally
results in more rapid convergence, and this is the default in **Optimize**.
**

Other improvements to the original method include limiting the number of
previous geometries used in Eq. ([9.33](#eq:a23)) by neglecting
earlier geometries, and eliminating any geometries more than a certain distance
from the current geometry (default = 0.3 a.u.).
