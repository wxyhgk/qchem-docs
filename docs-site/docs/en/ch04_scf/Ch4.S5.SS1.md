---
title: "4.5.1 Introduction"
---

## 4.5.1 Introduction

(July 4, 2026)

As for any numerical optimization procedure, the rate of convergence of the SCF
procedure is dependent on the initial guess and on the algorithm used to step
towards the stationary point. **Q-Chem** features a number of SCF optimization
algorithms which can be selected via the *$rem* variable SCF_ALGORITHM, including:

Methods that are based on extrapolation or interpolation:

- The highly successful DIIS procedures. These are the default (except
for restricted open-shell SCF calculations) and are available for all
orbital types (see Section [4.5.3](sect_diis.md)).
The damping

 and level-shifting
technique[[578]](../bib_references/bib.md#bib599)

can also be invoked together with DIIS (R, U only).
- ADIIS: the combination of augmented Roothaan-Hall (ARH) energy function
and DIIS developed by Hu and Yang,[[601]](../bib_references/bib.md#bib624)
 which is available for
R and U only.

Methods that make use of orbital gradient:

- Direct Minimization (DM), which has been re-implemented as simple
steepest descent with line search, and is available for all orbital
types. DM can be invoked after a few DIIS iterations.
- Limited-memory Broyden-Fletcher-Goldfarb-Shanno algorithm (L_BFGS),
which is a quasi-Newton method using the gradients and steps taken in
the previous iterations to construct the approximate Hessian.
- Geometric Direct Minimization (GDM) which is an improved and highly
robust version of DM and is the recommended fall-back when DIIS fails.
Like DM, It can also be invoked after a few iterations with
DIIS to improve the initial guess. GDM is the default algorithm for
restricted open-shell SCF calculations and is available for all
orbital types (see Section [4.5.7](sect_gdm.md)). GDM comes in three variants:

- GDM: the default implementation.
- GDM_LS: Uses a line search at every iteration.
- GDM_QLS: Employs a quadratic energy model to perform the
line search at every iteration.
- Square Gradient Minimization (SGM) family: SGM is a GDM-inspired method for
excited state orbital optimization. Currently, three variants of this approach
are supported: SGM (for RO and and OS_RO), SGM_LS (for R, U, RO and OS_RO)
and SGM_QLS (for R and U), which are based upon the corresponding GDM approaches.
For further details, see Section [4.5.15](sect_SGM-SCF.md).

Methods that require orbital Hessian:

- NEWTON_CG/NEWTON_MINRES (solve $\mathbf{Hd}=-\mathbf{g}$ for the
update direction with CG/MINRES solvers).
- SF_NEWTON_CG (the “saddle-free" version of NEWTON_CG).

The analytical orbital Hessian is available for R/U/RO/G/CR unless special
density functionals (*e.g.*, those nonlocal functionals except for VV10 [[1416]](../bib_references/bib.md#bib1477)
)
are used, while the use of finite-difference Hessian is available for all orbital
types by setting FD_MAT_VEC_PROD = TRUE.

In addition to these algorithms, there is also the maximum overlap method (MOM)
which ensures that DIIS always occupies a continuous set of orbitals and does
not oscillate between different occupancies. MOM can also be used to obtain
higher-energy solutions of the SCF equations (see Section [7.7.2](../ch07_excited/ex_OpSing.md)). The
relaxed constraint algorithm (RCA), which guarantees that the energy goes down
at every step, is also available via the old SCF code (set
GEN_SCFMAN = FALSE). Nevertheless, the performance of the
ADIIS [[601]](../bib_references/bib.md#bib624)
 algorithm should be similar to it.

Since the code in GEN_SCFMAN is highly modular, the availability of different
SCF algorithms to different SCF (orbital) types is largely extended in general.
For example, the old ROSCF implementation requires the use of the GWH guess and
the GDM algorithm exclusively. Such a limitation has been eliminated in
GEN_SCFMAN based RO calculations.
