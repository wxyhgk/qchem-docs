---
title: "9.1.1 Introduction"
---

## 9.1.1 Introduction

(July 4, 2026)

Molecular potential energy surfaces rely on the Born-Oppenheimer separation of
nuclear and electronic motion. Of particular interest are the critical points
on these surfaces, *i.e.* where the gradient of the energy vanishes.
Characterization of a critical point requires consideration of the eigenvalues
of the Hessian (second derivative matrix) calculated at that point. An
equilibrium geometry corresponds to a critical point where the eigenvalues of
the Hessian are all positive, whereas a transition-state structure is defined
as a first-order saddle point, and therefore has a Hessian with precisely one
negative eigenvalue. The latter is a local maximum along the reaction path
between the minima corresponding to the reactants and products, and a minimum in
all directions perpendicular to this reaction path.

The quality of a geometry optimization algorithm is of major importance; even
the fastest integral code in the world will be useless if combined with an
inefficient optimization algorithm that requires excessive numbers of steps to
converge. **Q-Chem** is currently transitioning to a new geometry optimization
driver, **Libopt3**, which improves on the older **Optimize** driver.
Details on the difference in capabilities between the two drivers are provided
in Table [9.1](#table:libopt_vs_optimize).

| Feature | LIBOPT3 | OPTIMIZE |
| --- | --- | --- |
| Optimization Type: |  |  |
| Unconstrained | ✓ | ✓ |
| Constrained | ✗ | ✓ |
| Structure Search: |  |  |
| Equilibrium | ✓ | ✓ |
| Transition | ✓ | ✓ |
| Coordinates: |  |  |
| Cartesian | ✓ | ✓ |
| Z -matrix | ✓ | ✓ |
| Redundant Internal | ✓ | – |
| Delocalized Internal | ✓ | ✓ |
| Optimization Algorithms: |  |  |
| Gradient Based | ✓ | – |
| Quasi-Newton | ✓ | ✓ |
| Newton | ✓ | – |
| Step Generation Algorithms: |  |  |
| Line Search (LS) | ✓ | – |
| Eigenvector Following (EF) | ✓ | ✓ |
| QM/MM | ✗ | ✓ |
| GDIIS algorithms | ✗ | ✓ |
| Hessian-Free Characterization | ✗ | ✓ |
| Intrinsic Reaction Coordinates (IRC) | ✗ | ✓ |
| Minimum-Energy Crossing Points (MECPs) | ✓ | ✓ |
| Harmonic Confiner | ✓ | ✓ |

Table 9.1: 
Differences of available features within the two optimization drivers,
as controlled by GEOM_OPT_DRIVER in the *$rem* section.
For unconstrained optimization, the default is
GEOM_OPT_DRIVER = LIBOPT3, whereas **Q-Chem**’s
original driver is selected using GEOM_OPT_DRIVER = OPTIMIZE.

The key to optimizing a molecular geometry successfully is to proceed from the
starting geometry to the final geometry in as few steps as possible. Four
factors influence the path and number of steps:

- starting geometry
- coordinate system
- optimization algorithm
- quality of the Hessian (and gradient)

**Q-Chem** controls the last three of these, but the starting geometry is solely
determined by the user, and the closer it is to the converged geometry, the
fewer optimization steps will be required. Decisions regarding the
optimization algorithm and the coordinate system are generally made by the
**Libopt3** and **Optimize** drivers (*i.e.*, internally, within **Q-Chem**) to
maximize the rate of convergence. Although users may override these choices,
caution should be exercised when doing so as changes may significantly
impact the computational cost.

**Q-Chem** provides the capability to optimize a molecule using Cartesian,
*Z*-matrix, redundant internal, or delocalized internal coordinates. The last
two of these are generated automatically from the Cartesian coordinates, and
delocalized internal coordinates are usually the best choice. These
coordinates were developed by Baker *et al.*,[[63]](../bib_references/bib.md#bib50)
 and can be
considered as an extension of the natural internal coordinates developed by
Pulay *et al.*[[1133]](../bib_references/bib.md#bib1181)
 and the redundant optimization
method of Pulay and Fogarasi.[[1134]](../bib_references/bib.md#bib1184)

The heart of the geometry optimization in **Q-Chem** (for both minima and
transition states) is Baker’s eigenvector-following (EF)
algorithm.[[64]](../bib_references/bib.md#bib46)
 This was developed following the work of Cerjan and
Miller,[[221]](../bib_references/bib.md#bib217)
 and of Simons and
co-workers.[[1256]](../bib_references/bib.md#bib1309)
 The Hessian mode-following option
incorporated into this algorithm is capable of locating a transition state by
walking uphill from the associated minimum. By following the lowest Hessian
mode, the EF algorithm can locate a transition state starting from any
reasonable input geometry and Hessian.

An additional option available for minimization is Pulay’s GDIIS
algorithm,[[285]](../bib_references/bib.md#bib289)
 which is based on the well known DIIS technique for
accelerating SCF convergence.[[1137]](../bib_references/bib.md#bib1183)
 GDIIS must be specifically
requested, as the EF algorithm is the default.

**Q-Chem** incorporates a very accurate and efficient Lagrange multiplier
algorithm for constrained optimization. This was originally developed for use
with Cartesian coordinates[[65]](../bib_references/bib.md#bib48)
 and can handle
constraints that are not necessarily satisfied by the starting geometry. The
Lagrange multiplier approach has been modified for use with delocalized
internal coordinates,[[66]](../bib_references/bib.md#bib51)
 which is much more efficient and is now
the default within **Q-Chem**. The Lagrange multiplier code can locate
constrained transition states as well as minima.

Another consideration when trying to minimize the total optimization time concerns
the quality of the gradient and Hessian. A higher-quality Hessian (*i.e.*,
analytical versus approximate) will in many cases lead to faster convergence,
in the sense of requiring fewer optimization steps. This is why by default for
transition-state optimization with **Libopt3** the exact Hessian will be
calculated. However, the construction of an analytical Hessian requires
significant computational effort and may outweigh the advantage of fewer
optimization cycles. Currently available analytical gradients and Hessians are
summarized in Table [9.2](#table:grad_and_hess).

| Level of Theory | Analytical | Maximum Angular | Analytical | Maximum Angular |
| --- | --- | --- | --- | --- |
| (Algorithm) | Gradients | Momentum Type | Hessian | Momentum Type |
| HF/DFT | ✓ | $k$ | ✓ | $k$ |
| ROHF | ✓ | $h$ | ✗ |  |
| canonical ROHF | ✗ |  | ✗ |  |
| RI-MP2 | ✓ | $h$ | ✗ |  |
| CCSD | ✓ | $h$ | ✗ |  |
| CIS/TDDFT (except RO) | ✓ | $h$ | ✓ | $g$ |
| EOM-CCSD | ✓ | $h$ | ✗ |  |
| ADC( $n$ ) | ✗ |  | ✗ |  |

Table 9.2: 
Gradients and Hessians currently available for geometry optimizations
with maximum angular momentum types for analytical derivative calculations.
Higher angular momentum are supported when GEN_SCFMAN = TRUE.

Features of **Q-Chem**’s geometry and transition-state optimization capabilities include:

- Cartesian, *Z*-matrix or internal coordinate systems
- Eigenvector Following (EF) or GDIIS algorithms
- Constrained optimizations
- Equilibrium structure searches
- Transition structure searches
- Hessian-free characterization of stationary points
- Initial Hessian and Hessian update options
- Reaction pathways using intrinsic reaction coordinates (IRC)
- Optimization of minimum-energy crossing points (MECPs) along conical seams
