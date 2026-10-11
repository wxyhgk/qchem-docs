---
title: "9.8.5 State-Tracking Algorithm"
---

## 9.8.5 State-Tracking Algorithm

(July 4, 2026)

For optimizing excited-state geometries and other applications, it can be
important to find and follow electronically excited states of a particular
character as the geometry changes. Various state-tracking procedures have
been proposed for such cases.[[527]](../bib_references/bib.md#bib541)

One such algorithm, based on the
overlap of the attachment/detachment densities at successive steps,
is available in **Q-Chem** (see Section [7.13.2](../ch07_excited/sect_AttachDetach.md)).[[256]](../bib_references/bib.md#bib256)

Using the densities
avoids any issues that may be introduced by sign changes in the orbitals or
configuration-interaction coefficients.

Two parameters are used to influence the choice of the electronic surface. One
($\gamma_{E}$) controls the energy window for states included in the search,
and the other ($\gamma_{S}$) controls how well the states must overlap in
order to be considered of the same character. These can be set by the user or
generated automatically based on the magnitude of the nuclear displacement.
The energy window is defined relative to the estimated energy for the current
step (*i.e.*, $E_{\rm est}\pm\gamma_{E}$), which in turn is based on the
energy, gradient and nuclear displacement of previous steps. This estimated
energy is specific to the type of calculation (*e.g.*, geometry optimization).

The similarity metric for the overlap is defined as

<a id="eq:similarity_metric"></a>
$$
\mathcal{S}=1-\tfrac{1}{2}\bigl{(}||\Delta\mathbf{A}||+||\Delta\mathbf{D}||\bigr{)} \tag{9.59}
$$

where $\Delta\mathbf{A}=\mathbf{A}_{t+1}-\mathbf{A}_{t}$ is the difference in
attachment density matrices (Eq. ([7.185](../ch07_excited/sect_AttachDetach.md#eq:attach_density_matrix))) and $\Delta\mathbf{D}=\mathbf{D}_{t+1}-\mathbf{D}_{t}$ is the difference in detachment
density matrices (Eq. ([7.183](../ch07_excited/sect_AttachDetach.md#eq:detach_density_matrix))), at successive steps.
Equation ([9.59](#eq:similarity_metric)) uses the matrix spectral norm,

<a id="Ch9.E60"></a>
$$
||\mathbf{M}||=\left(\lambda_{\rm max}\mathbf{M}^{\dagger}\mathbf{M}\right)^{1/2} \tag{9.60}
$$

where $\lambda_{\rm max}$ is the largest eigenvalue of $\mathbf{M}$.

The selected state always satisfies one of the following

1. 1.

It is the only state in the window defined by $\gamma_{E}$.
2. 2.

It is the state with the largest overlap, provided at least one state has
$\mathcal{S}\geq\gamma_{S}$.
3. 3.

It is the nearest state energetically if all states in the window have
$\mathcal{S}<\gamma_{S}$, or if there are no states in the energy window.

State-following can currently be used with CIS or TDDFT excited states and is
initiated with the *$rem* variable STATE_FOLLOW. It can be used with
geometry optimization, *ab initio* molecular dynamics,[[256]](../bib_references/bib.md#bib256)

or with the freezing/growing-string method. The desired state is
specified using CIS_STATE_DERIV for optimization or dynamics, or
using SET_STATE_REACTANT and SET_STATE_PRODUCT for the
freezing- or growing-string methods. The results for geometry optimizations
can be affected by the step size (GEOM_OPT_DMAX), and using a step
size smaller than the default value can provide better results. Also, it is
often challenging to converge the strings in freezing/growing-string calculations.

STATE_FOLLOW

### `STATE_FOLLOW`

> **Turns on state following.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not use state-following.
>     * TRUE
>     * Use state-following.
> * **Recommendation**: None.

FOLLOW_ENERGY

### `FOLLOW_ENERGY`

> **Adjusts the energy window for near states**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Use dynamic thresholds, based on energy difference between steps.
>     * $n$
>     * Search over selected state
>     * $E_{\rm est}\pm n\times 10^{-6}~{}E_{h}$
>     * .
> * **Recommendation**: Use a wider energy window to follow a state diabatically, smaller window to remain on the adiabatic state most of the time.

FOLLOW_OVERLAP

### `FOLLOW_OVERLAP`

> **Adjusts the threshold for states of similar character.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Use dynamic thresholds, based on energy difference between steps.
>     * $n$
>     * Percentage overlap for previous step and current step.
> * **Recommendation**: Use a higher value to require states have higher degree of similarity to be considered the same (more often selected based on energy).
