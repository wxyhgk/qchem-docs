---
title: "7.11.10 State-Specific PCM with RAS-SF"
---

## 7.11.10 State-Specific PCM with RAS-SF

(July 4, 2026)

The polarizable continuum model (PCM) is an efficient way to incorporate dielectric boundary conditions into a ground-state
quantum chemistry calculation as described in Section [11.2.3](../ch11_env/topic_pcm-em.md), although some additional choices exist regarding how
to model electronic excited states within this formalism.[[569]](../bib_references/bib.md#bib580)
 For vertical transition energies computed using
RAS-SF wave functions, both equilibrium and nonequilibrium versions of a state-specific PCM solvation correction are
available.[[32]](../bib_references/bib.md#bib17)
 Ground-state polarization is
described using the solvent’s static dielectric constant, and in the nonequilibrium solvation approach that polarization is modified upon vertical
excitation using the solvent’s optical dielectric constant.

The equilibrium formulation solves the state-specific Schrödinger equation

<a id="Ch7.E172"></a>
$$
(\hat{H}_{\text{vac}}+\hat{R}_{k})|\Psi_{k}\rangle=E_{k}|\Psi_{k}\rangle \tag{7.172}
$$

where $\hat{R}_{k}$ is the reaction field operator for state $k$. Since $\hat{R}_{k}$ depends on $|\Psi_{k}\rangle$, this equation must be solved iteratively.
The fully relaxed (equilibrium) excitation free energy is

<a id="Ch7.E173"></a>
$$
\Delta G=G_{k}^{\text{eq}}-G_{0}=\Delta E_{k}^{\text{eq}}-W_{k}+W_{0}\;. \tag{7.173}
$$

(It is a *free* energy because the continuum description of the solvent implicitly includes averaging over solvent degrees of freedom.)
We use $G$ to represent a free energy and $W$ to represent polarization work, with subscripts to indicate the electronic state in question.

The nonequilibrium version of the solvation model uses a perturbative framework to solve the Schrödinger equation.
This is described in more detail in Section [11.2.3.3](../ch11_env/topic_pcm-em.md#subsubsec:noneq-PCM). Briefly, this approach is based on a state-specific
Hamiltonian that is partitioned according to

<a id="Ch7.E174"></a>
$$
\hat{H}_{k}^{\text{noneq}}=\underbrace{\hat{H}_{\text{vac}}+\hat{R}_{0}^{\text{s+f}}}_{\hat{H}_{0}}+\lambda(\hat{R}_{k}^{\text{f}}-\hat{R}_{0}^{\text{f}})\;. \tag{7.174}
$$

The zeroth-order Hamiltonian ($\hat{H}_{0}$) includes the ground-state, equilibrium reaction-field operator
$\hat{R}_{0}\equiv R_{0}^{\text{s+f}}=\hat{R}_{0}^{\text{s}}+\hat{R}_{0}^{\text{f}}$. The solvent polarization is divided into “slow” (nuclear) and “fast” (electronic) components, but for equilibrium solvation both components are included. The perturbation (indicated by perturbation
parameter $\lambda$ corrects the fast polarization upon excitation, $|\Psi_{0}\rangle\rightarrow|\Psi_{k}\rangle$. This nonequilibrium
correction is described via first-order perturbation theory. The result is a perturbative, state-specific (ptSS) correction to the
excitation energy:

<a id="Ch7.E175"></a>
$$
\Delta G_{k}^{\text{ptSS(1)}}=G_{k}-G_{0}=\Delta E_{k}^{\text{ptSS(1)}}-W^{\text{f}}_{k(0)}+W^{\text{f}}_{0}+W_{0,k(0)} \tag{7.175}
$$

For further details see Ref. [[32]](../bib_references/bib.md#bib17)
.
