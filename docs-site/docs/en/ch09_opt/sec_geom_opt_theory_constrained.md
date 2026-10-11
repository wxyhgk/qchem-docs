---
title: "9.1.5 Constrained Optimization"
---

## 9.1.5 Constrained Optimization

(July 4, 2026)

Constrained optimization refers to the optimization of molecular structures in
which certain parameters (*e.g.*, bond lengths, bond angles or dihedral angles)
are fixed. In quantum chemistry calculations, this has traditionally been
accomplished using *Z*-matrix coordinates, with the desired parameter set in
the *Z*-matrix and simply omitted from the optimization space. In 1992, Baker
presented an algorithm for constrained optimization directly in Cartesian
coordinates.[[65]](../bib_references/bib.md#bib48)
 Baker’s algorithm used both penalty functions
and the classical method of Lagrange multipliers,

 and was
developed in order to impose constraints on a molecule obtained from a
graphical model builder as a set of Cartesian coordinates. Some improvements
widening the range of constraints that could be handled were made in 1993.[[61]](../bib_references/bib.md#bib49)
**Q-Chem** includes the latest version of this algorithm,
which has been modified to handle constraints directly in delocalized internal
coordinates.[[66]](../bib_references/bib.md#bib51)

The essential problem in constrained optimization is to minimize a function of
$n$ variables $F(\mathbf{x})$ subject to a series of $m$ constraints of
the form $C_{i}(\mathbf{x})=0$ for $i=\ell,\ldots,m$. Assuming $m<n$, then perhaps the best
way to proceed (if this were possible in practice) would be to use the $m$
constraint equations to eliminate $m$ variables, and then solve the
resulting unconstrained problem in terms of the $n-m$ independent variables.
This is exactly what occurs in a *Z*-matrix optimization. Such an approach
cannot be used in Cartesian coordinates as standard distance and angle
constraints are non-linear functions of the appropriate coordinates. For
example, a distance constraint between atoms $i$ and $j$ is, in Cartesians,
given by $(R_{ij}-R_{0})=0$, with

<a id="Ch9.E17"></a>
$$
R_{ij}=\bigl{[}(x_{i}-x_{j})^{2}+(y_{i}-y_{j})^{2}+(z_{i}-z_{j})^{2}\bigr{]}^{1/2} \tag{9.17}
$$

and $R_{0}$ is the constrained distance. This obviously cannot be satisfied by
elimination. What can be eliminated in Cartesians are the individual $x$, $y$
and $z$ coordinates themselves and in this way individual atoms can be totally
or partially frozen.

Internal constraints can be handled in Cartesian coordinates by introducing the
Lagrangian function

<a id="eq:a15"></a>
$$
L(\mathbf{x},\lambda)=F(\mathbf{x})-\sum\limits_{i=1}^{m}{\lambda_{i}C_{i}(\mathbf{x})} \tag{9.18}
$$

which replaces the function $F(\mathbf{x})$ in the unconstrained case. Here, the
$\lambda_{i}$ are the so-called Lagrange multipliers, one for each constraint
$C_{i}(\mathbf{x})$. Differentiating Eq. ([9.18](#eq:a15)) with respect to $\mathbf{x}$ and $\lambda$ affords

<a id="A3.S8.EGx70"></a>
$$
\displaystyle\frac{dL(\mathbf{x},\lambda)}{dx_{j}} \tag{9.19}
$$

At a stationary point of the Lagrangian we have $\hat{\bm{\nabla}}\mathbf{L}=\bm{0}$, *i.e.*, all
$dL/dx_{j}=0$ and all $dL/d\lambda_{i}=0$. This latter condition means that all
$C_{i}(\mathbf{x})=0$ and thus all constraints are satisfied. Hence, finding a set
of values ($\mathbf{x}$, $\lambda$) for which $\hat{\bm{\nabla}}\mathbf{L}=\bm{0}$ will give a
possible solution to the constrained optimization problem in exactly the same
way as finding an $\mathbf{x}$ for which $\mathbf{g}=\hat{\bm{\nabla}}\mathbf{F}=\bm{0}$ gives a solution
to the corresponding unconstrained problem.

The Lagrangian second derivative matrix, which is the analogue of the Hessian matrix
in an unconstrained optimization, is given by

<a id="eq:a17"></a>
$$
\hat{\nabla}^{2}\mathbf{L}=\left(\begin{array}[]{cc}\displaystyle\frac{d^{2}L(\mathbf{x},\lambda)}{dx_{j}dx_{k}}&\displaystyle\frac{d^{2}L(\mathbf{x},\lambda)}{dx_{j}d\lambda_{i}}\\
\displaystyle\frac{d^{2}L(\mathbf{x},\lambda)}{dx_{j}d\lambda_{i}}&\displaystyle\frac{d^{2}L(\mathbf{x},\lambda)}{d\lambda_{j}d\lambda_{i}}\end{array}\right) \tag{9.21}
$$

where

<a id="A3.S8.EGx71"></a>
$$
\displaystyle\frac{d^{2}L(\mathbf{x},\lambda)}{dx_{j}dx_{k}} \tag{9.22}
$$

Thus, in addition to the standard gradient vector and Hessian matrix for the
unconstrained function $F(\mathbf{x})$, we need both the first and second
derivatives (with respect to coordinate displacement) of the constraint
functions. Once these quantities are available, the corresponding Lagrangian
gradient, (Eq. ([9.19](#eq:a16a))), and Lagrangian second derivative matrix,
(Eq. ([9.21](#eq:a17))), can be formed, and the optimization step calculated in a similar
manner to that for a standard unconstrained optimization.[[65]](../bib_references/bib.md#bib48)

In the Lagrange multiplier method, the unknown multipliers, $\lambda_{i}$, are an
integral part of the parameter set. This means that the optimization space
consists of all $n$ variables $\mathbf{x}$ plus all $m$ Lagrange multipliers
$\lambda$, one for each constraint. The total dimension of the constrained
optimization problem, $n+m$, has thus increased by $m$ compared to the
corresponding unconstrained case. The Lagrangian Hessian matrix,
$\hat{\nabla}^{2}\mathbf{L}$, has $m$ extra modes compared to the standard (unconstrained)
Hessian matrix, $\hat{\nabla}^{2}\mathbf{F}$. What normally happens is that these additional
modes are dominated by the constraints (*i.e.*, their largest components
correspond to the constraint Lagrange multipliers) and they have negative
curvature (a negative Hessian eigenvalue). This is perhaps not surprising when
one realizes that any motion in the parameter space that breaks the constraints
is likely to lower the energy.

Compared to a standard unconstrained minimization, where a stationary point is
sought at which the Hessian matrix has all positive eigenvalues, in the
constrained problem we are looking for a stationary point of the Lagrangian
function at which the Lagrangian Hessian matrix has as many negative
eigenvalues as there are constraints (*i.e.*, we are looking for an $m$th-order
saddle point). For further details and practical applications of
constrained optimization using Lagrange multipliers in Cartesian coordinates;
see Ref. [[65]](../bib_references/bib.md#bib48)
.

Eigenvector following can be implemented in a constrained optimization in a
similar way to the unconstrained case. Considering a constrained minimization
with $m$ constraints, then Eq. ([9.11](sect_ef.md#eq:a9a)) is replaced by

<a id="eq:a18a"></a>
$$
\left({{\begin{array}[]{*{4}c}{b_{1}}&&&{F_{1}}\\
&\ddots&{\rm{\bf 0}}&\vdots\\
&{\rm{\bf 0}}&{b_{m}}&{F_{m}}\\
{F_{1}}&\cdots&{F_{m}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{h_{1}}\\
\vdots\\
{h_{m}}\\
1\\
\end{array}}}\right)=\lambda_{p}\left({{\begin{array}[]{*{1}c}{h_{1}}\\
\vdots\\
{h_{m}}\\
1\\
\end{array}}}\right) \tag{9.25}
$$

and Eq. ([9.12](sect_ef.md#eq:a9b)) by

<a id="eq:a18b"></a>
$$
\left({{\begin{array}[]{*{4}c}{b_{m+1}}&&&{F_{m+1}}\\
&\ddots&{\rm{\bf 0}}&\vdots\\
&{\rm{\bf 0}}&{b_{m+n}}&{F_{m+n}}\\
{F_{m+1}}&\cdots&{F_{m+n}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{h_{m+1}}\\
\vdots\\
{h_{m+n}}\\
1\\
\end{array}}}\right)=\lambda_{n}\left({{\begin{array}[]{*{1}c}{h_{m+1}}\\
\vdots\\
{h_{m+n}}\\
1\\
\end{array}}}\right) \tag{9.26}
$$

where $b_{i}$ are now the eigenvalues of $\hat{\nabla}^{2}\mathbf{L}$, with corresponding
eigenvectors $\mathbf{u}_{i}$, and $F_{i}=\mathbf{u}_{i}^{t}\hat{\nabla}\mathbf{L}$. Here Eq. ([9.25](#eq:a18a))
includes the $m$ constraint modes along which a negative Lagrangian Hessian
eigenvalue is required, and Eq. ([9.26](#eq:a18b)) includes all the other modes.

Equations ([9.25](#eq:a18a)) and ([9.26](#eq:a18b)) implement eigenvector following
for a constrained minimization. Constrained transition state searches can be
carried out by selecting one extra mode to be maximized in addition to the $m$
constraint modes, *i.e.*, by searching for a saddle point of the Lagrangian
function of order $m+\ell$.

It should be realized that, in the Lagrange multiplier method, the desired
constraints are only satisfied at convergence, and not necessarily at
intermediate geometries. The Lagrange multipliers are part of the optimization
space; they vary just as any other geometrical parameter and, consequently the
degree to which the constraints are satisfied changes from cycle to cycle,
approaching 100% satisfied near convergence. One advantage this brings is
that, unlike in a standard *Z*-matrix approach, constraints do not have to be
satisfied in the starting geometry.

Imposed constraints can normally be satisfied to very high accuracy, $10^{-6}$
or better. However, problems can arise for both bond and dihedral angle
constraints near $0^{\circ}$ and $180^{\circ}$ and, instead of attempting to
impose a single constraint, it is better to split angle constraints near these
limiting values into two by using a dummy atom,[[61]](../bib_references/bib.md#bib49)
 exactly
analogous to splitting a $180^{\circ}$ bond angle into two $90^{\circ}$ angles
in a *Z*-matrix.

**Note: 

Exact $0^{\circ}$ and $180^{\circ}$ single angle constraints cannot be
imposed, as the corresponding constraint normals, $\hat{\bm{\nabla}}\mathbf{C}_{i}$, are zero,
and result in rows and columns of zeros in the Lagrangian Hessian matrix.
**
