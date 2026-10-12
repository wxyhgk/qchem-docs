---
title: "6.23.1 Introduction"
---

## 6.23.1 Introduction

(July 4, 2026)

The methods described in this section involve the direct variational
optimization of the two-electron reduced-density matrix (2-RDM, ${}^{2}\mathbf{D}$),
subject to necessary ensemble $N$-representability
conditions.[[431]](../bib_references/bib.md#bib441)

Such conditions place restrictions on the 2-RDM in order to ensure that it
is derivable from an ensemble of $N$-electron density matrices. In the
limit that the $N$-representability of the 2-RDM is exactly enforced, the
variational 2-RDM (v2RDM) approach is equivalent to full configuration
interaction (CI). Such computations are, in general, computationally
infeasible, so the v2RDM optimization is typically carried out under a
subset of two- or three-particle conditions. When only partially
enforcing $N$-representability, the v2RDM approach yields a lower bound to
the full CI energy.

In **Q-Chem**, all v2RDM optimizations are carried out under the following
conditions:

- the 2-RDM is positive semidefinite
- the one-electron reduced-density matrix (1-RDM) is positive semidefinite
- the trace of the 2-RDM is equal to the number of pairs of electrons, $N(N-1)$
- each spin block of the 2-RDM properly contracts to the appropriate spin block of the
1-RDM
- the expectation value of $\hat{M}_{S}$ is
$\frac{1}{2}(N_{\alpha}-N_{\beta})$ (the maximal spin projection)

Additionally, an optional spin constraint can be placed on the 2-RDM such
that $\langle\hat{S}^{2}\rangle=S(S+1)$ (in units of $\hbar^{2}$), where the $S$ is the spin quantum
number. Note that this constraint on the expectation value of $\hat{S}^{2}$
does not strictly guarantee that the 2-RDM corresponds to an eigenfunction
of $\hat{S}^{2}$. Without additional constraints, a v2RDM optimization
would yield poor-quality 2-RDMs with energies far below those of full CI.
Reasonable results require, at a minimum, that one enforce the positivity
of additional pair-probability density matrices, including the two-hole
reduced-density matrix (${}^{2}\mathbf{Q}$) and the particle-hole reduced-density
matrix (${}^{2}\mathbf{G}$). The positivity of ${}^{2}\mathbf{D}$, ${}^{2}\mathbf{Q}$, and
${}^{2}\mathbf{G}$ constitute the DQG constraints of Garrod and
Percus.[[430]](../bib_references/bib.md#bib442)
 For many systems, the DQG constraints yield a
reasonable description of the electronic structure. However, if high
accuracy is desired, it is sometimes necessary to consider constraints on
higher-order reduced-density matrices (*e.g.* the three-electron
reduced-density matrix [3-RDM]). In **Q-Chem**, v2RDM optimizations can be
performed under the T1 and T2 partial three-particle
conditions,[[369]](../bib_references/bib.md#bib372)
 which do not explicitly depend
upon the 3-RDM; or the full 3-positivity conditions, which include
the three-particle reduced-density matrix (${}^{3}\mathbf{D}$), the three-hole
reduced-density matrix (${}^{3}\mathbf{Q}$), the two-particle-one-hole
reduced-density matrix (${}^{3}\mathbf{E}$), and the one-particle-two-hole
reduced-density matrix (${}^{3}\mathbf{F}$). The full 3-positivity conditions
guarantee partial conditions automatically.[[929]](../bib_references/bib.md#bib967)

The positivity conditions imposed in v2RDM computations are controlled through the
*$rem* variable RDM_POSITIVITY.

The main utility of the v2RDM approach is in the context of
active-space-based descriptions of strong or nondynamical correlation.
The most common active-space-based approach for strong correlation is the
compete active space self-consistent field (CASSCF) method. By performing
a v2RDM computation within an active space and coupling v2RDM to an
orbital optimization procedure, one can achieve a v2RDM-driven CASSCF
procedure[[441]](../bib_references/bib.md#bib452)
 that
provides a lower bound the conventional CI-based CASSCF energy. Because
the v2RDM-CASSCF method scales polynomially with respect to the number of
active orbitals, v2RDM-CASSCF can handle much larger active spaces (*e.g.*,
50 electrons in 50 orbitals) compared to CI-CASSCF (*e.g.*, 18 electrons in 18 orbitals).

Note that v2RDM-CASSCF only describes electron correlations among the
active orbitas. A computationally inexpensive estimate of the remaining
correlation effects can be achieved with the multiconfiguration
pair-density functional theory (MC-PDFT)
approach,[[886]](../bib_references/bib.md#bib920)

which evaluates the energy
as a functional of the on-top pair density (OTPD). In the MC-PDFT
implementation in **Q-Chem**, the OTPD is derived from a variationally optimized
2-RDM as described in Ref. [[966]](../bib_references/bib.md#bib1007)
.

The current v2RDM, v2RDM-CASSCF, and MC-PDFT implementations must make use of the
density fitting (DF) approximation to the two-electron integrals. The use
of DF integrals is particularly advantageous for v2RDM-CASSCF computations
with large active spaces because of the increased efficiency in the
orbital optimization/integral transformation step. The v2RDM computation
will fail without the *$rem* keyword AUX_BASIS.
Analytic gradients are not available when frozen molecular orbitals are
requested. Specification of the active space is demonstrated in the examples
below. When the formatted checkpoint file is requested, natural orbitals are saved in it.
