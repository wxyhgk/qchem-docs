---
title: "9.1.3 Eigenvector-Following (EF) Algorithm"
---

## 9.1.3 Eigenvector-Following (EF) Algorithm

(July 4, 2026)

The work of Cerjan and Miller,[[221]](../bib_references/bib.md#bib217)
 and later Simons and
co-workers,[[1256]](../bib_references/bib.md#bib1309)
 showed that there was a better step
than simply directly following one of the Hessian eigenvectors. A simple
modification to the Newton-Raphson step is capable of guiding the search away
from the current region towards a stationary point with the required
characteristics. This is

<a id="eq:a5t"></a>
$$
\mathbf{h}=-\sum_{i}\left(\frac{F_{i}}{b_{i}-\lambda}\right)\mathbf{u}_{i} \tag{9.6}
$$

in which $\lambda$ can be regarded as a shift parameter on the Hessian
eigenvalue $b_{i}$. Scaling the Newton-Raphson step in this manner effectively
directs the step to lie primarily, but not exclusively (unlike Poppinger’s
algorithm[[1117]](../bib_references/bib.md#bib1164)
), along one of the local eigenmodes, depending
on the value chosen for $\lambda$.
References [[221]](../bib_references/bib.md#bib217)
 all use the same basic
approach of Eq. ([9.6](#eq:a5t)) but differ in the means of determining the value of $\lambda$.

The EF algorithm[[64]](../bib_references/bib.md#bib46)
 uses the rational function approach
presented in Refs. [[72]](../bib_references/bib.md#bib57)
, yielding an eigenvalue equation of the form

<a id="eq:a6"></a>
$$
\left({{\begin{array}[]{*{2}c}{\rm{\bf H}}&{\rm{\bf g}}\\
{{\rm{\bf g}}^{t}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{\rm{\bf h}}\\
1\\
\end{array}}}\right)=\lambda\left({{\begin{array}[]{*{1}c}{\rm{\bf h}}\\
1\\
\end{array}}}\right) \tag{9.7}
$$

from which a suitable $\lambda$ can be obtained. Expanding Eq. ([9.7](#eq:a6)) yields

<a id="eq:a7a"></a>
$$
(\mathbf{H}-\lambda)\mathbf{h}+\mathbf{g}=0 \tag{9.8}
$$

and

<a id="eq:a7b"></a>
$$
\mathbf{g}^{t}\mathbf{h}=\lambda \tag{9.9}
$$

In terms of a diagonal Hessian representation, Eq. ([9.8](#eq:a7a)) rearranges to
Eq. ([9.6](#eq:a5t)), and substitution of Eq. ([9.6](#eq:a5t)) into the diagonal form of
Eq. ([9.9](#eq:a7b)) gives

<a id="Ch9.E10"></a>
$$
\lambda=-\sum_{i}\left(\frac{-F_{i}^{2}}{b_{i}-\lambda}\right) \tag{9.10}
$$

which can be used to evaluate $\lambda$ iteratively.

The eigenvalues, $\lambda$, of the RFO equation Eq. ([9.7](#eq:a6)) have the
following important properties:[[72]](../bib_references/bib.md#bib57)

- •

The $(n+1)$ values of $\lambda$ bracket the $n$ eigenvalues of the
Hessian matrix $\lambda_{i}<b_{i}<\lambda_{i+1}$.
- •

At a stationary point, one of the eigenvalues, $\lambda$, of Eq. ([9.7](#eq:a6)) is
zero and the other $n$ eigenvalues are those of the Hessian at the
stationary point.
- •

For a saddle point of order $m$, the zero eigenvalue separates the $m$
negative and the $(n-m)$ positive Hessian eigenvalues.

This last property, the separability of the positive and negative Hessian
eigenvalues, enables two shift parameters to be used, one for modes along which
the energy is to be maximized and the other for which it is minimized. For a
transition state (a first-order saddle point), in terms of the Hessian
eigenmodes, we have the two matrix equations

<a id="eq:a9a"></a>
$$
\left({{\begin{array}[]{*{2}c}{b_{1}}&{F_{1}}\\
{F_{1}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{h_{1}}\\
1\\
\end{array}}}\right)=\lambda_{p}\left({{\begin{array}[]{*{1}c}{h_{1}}\\
1\\
\end{array}}}\right) \tag{9.11}
$$

<a id="eq:a9b"></a>
$$
\left({{\begin{array}[]{*{4}c}{b_{2}}&&&{F_{2}}\\
&\ddots&{\rm{\bf 0}}&\vdots\\
&{\rm{\bf 0}}&{b_{n}}&{F_{n}}\\
{F_{2}}&\cdots&{F_{n}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{h_{2}}\\
\vdots\\
{h_{n}}\\
1\\
\end{array}}}\right)=\lambda_{n}\left({{\begin{array}[]{*{1}c}{h_{2}}\\
\vdots\\
{h_{n}}\\
1\\
\end{array}}}\right) \tag{9.12}
$$

where it is assumed that we are maximizing along the lowest Hessian mode
$\mathbf{u}_{1}$. Note that $\lambda_{p}$ is the highest eigenvalue of Eq. ([9.11](#eq:a9a)), which
is always positive and approaches zero at convergence, and $\lambda_{n}$ is
the lowest eigenvalue of Eq. ([9.12](#eq:a9b)), which it is always negative and again
approaches zero at convergence.

Choosing these values of $\lambda$ gives a step that attempts to maximize along
the lowest Hessian mode, while at the same time minimizing along all the other
modes. It does this regardless of the Hessian eigenvalue structure (unlike the
Newton-Raphson step). The two shift parameters are then used in
Eq. ([9.6](#eq:a5t)) to give the final step

<a id="Ch9.E13"></a>
$$
\mathbf{h}=-\left(\frac{F_{1}}{b_{1}-\lambda_{p}}\right)\mathbf{u}_{1}+\sum\limits_{i=2}^{n}\left(\frac{F_{i}}{b_{i}-\lambda_{n}}\right)\mathbf{u}_{i} \tag{9.13}
$$

If this step is greater than the maximum allowed, it is scaled down. For
minimization only one shift parameter, $\lambda_{n}$, is used which acts
on all modes.

In Eq. ([9.11](#eq:a9a))) and Eq. ([9.12](#eq:a9b)) it was assumed that the step
would maximize along the lowest Hessian mode, $b_{1}$, and minimize along all the
higher modes. However, it is possible to maximize along modes other than the
lowest, and in this way potentially locate transition states for alternative
rearrangements/dissociations from the same initial starting point. For
maximization along the $k$th mode (instead of the lowest mode),
Eq. ([9.11](#eq:a9a)) is replaced by

<a id="Ch9.E14"></a>
$$
\left({{\begin{array}[]{*{2}c}{b_{k}}&{F_{k}}\\
{F_{k}}&0\\
\end{array}}}\right)\left({{\begin{array}[]{*{1}c}{h_{k}}\\
1\\
\end{array}}}\right)=\lambda_{p}\left({{\begin{array}[]{*{1}c}{h_{k}}\\
1\\
\end{array}}}\right) \tag{9.14}
$$

and Eq. ([9.12](#eq:a9b)) now excludes the $k$th mode, but includes the lowest
mode. Since what was originally the $k$th mode is the mode along which the
negative eigenvalue is required, then this mode will eventually become the
lowest mode at some stage of the optimization. To ensure that the original mode
is being followed smoothly from one cycle to the next, the mode that is
actually followed is the one with the greatest overlap with the mode followed
on the previous cycle. This procedure is known as *mode following*. For
more details and some examples, see Ref. [[64]](../bib_references/bib.md#bib46)
.
