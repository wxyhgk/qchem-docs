---
title: "7.10.6 Regularised Excited States with BWs-ADC"
---

## 7.10.6 Regularised Excited States with BWs-ADC

(July 4, 2026)

## 7.10.6.1 Introduction and Theory

A disadvantage of the standard, Møller-Plesset based (MP-)ADC scheme is that
excitation energies and properties start to diverge if the HOMO/LUMO gap approaches zero. This is caused
by divergence of the first order $t_{2}$-amplitudes, which enter the secular matrix.
This issue can be avoided by choosing a *regular* partitioning of the
Hamiltonian for the perturbative expansion of the polarisation propagator.
Here, we employ the size-consistent Brillouin-Wigner partitioning by Carter-Fenk and
Head-Gordon.[[195]](../bib_references/bib.md#bib196)
 While it was originally proposed
as a repartitioning to make second order Brillouin-Wigner theory size-consistent and
size-extensive, it is best to instead view BWs-$n$ as a regularised
Rayleigh-Schrödinger perturbation theory, whose unperturbed Hamiltonian and perturbation are given by:

<a id="A3.S8.EGx65"></a>
$$
\displaystyle\hat{H}^{(0)} \tag{7.147}
$$

Here, $\hat{W}$ is a block-diagonal one-electron operator whose properties are extensively explored in Ref. [[335]](../bib_references/bib.md#bib339)

Within the context of BWs-ADC, we recommend using the $A_{0}$ and $B_{0}$ parameters of MPR-BWs2 (see also [6.9](../ch06_correlation/topic_mpr-bws2.md)):

<a id="Ch7.E149"></a>
$$
\hat{W}=\frac{A_{0}}{8}\sum_{ijkab}\left(\langle ik||ab\rangle{t^{ab}_{jk}}^{(1)}\right)\left(\hat{a}^{\dagger}_{i}\hat{a}_{j}+\hat{a}^{\dagger}_{j}\hat{a}_{i}\right)+\frac{B_{0}}{8}\sum_{ijabc}\left(\langle ij||ac\rangle{t^{bc}_{ij}}^{(1)}\right)\left(\hat{a}^{\dagger}_{a}\hat{a}_{b}+\hat{a}^{\dagger}_{b}\hat{a}_{a}\right) \tag{7.149}
$$

A key aspect of BW-s2 theory is that the combined zeroth order Hamiltonian still constitutes a one-particle operator and can thus be diagonalised self-consistently to yield the *dressed* orbitals $\phi_{p}^{\prime}(r,\sigma)$ with corresponding orbital energies $\varepsilon_{p}^{\prime}$:

<a id="Ch7.E150"></a>
$$
(\hat{F}+\hat{W})\phi_{p}^{\prime}(r,\sigma)=\varepsilon_{p}^{\prime}\phi_{p}^{\prime}(r,\sigma) \tag{7.150}
$$

If the BWs-ADC equations (both the secular matrix-vector product as well as densities required for ISR property calculations) are expressed in terms of dressed orbitals, the algebraic structure of the BWs-ADC equations is almost completely equivalent to that of the corresponding MP-ADC expression. This implies that the computational cost of a BWs-ADC calculation is *nearly identical* to its MP-ADC equivalent. Two additional required steps increase the cost slightly: First, the BW-s2 ground state is iterative. Second, the second order ground state doubles amplitudes (${t^{ab}_{ij}}^{(2)}$) require a one-shot correction of $\mathcal{O}(N^{5})$ cost due to the presence of $\hat{W}$ in $\hat{H}^{(1)}$.

In practice, a BWs-ADC(2) calculation only takes $1-5\%$ longer than an equivalent MP-ADC(2) calculation on the same machine. For a BWs-ADC(3) calculation, this difference is typically even less as all tensor contractions with a computational complexity of $\mathcal{O}(N^{6})$ are identical between BWs-ADC(3) and MP-ADC(3).

## 7.10.6.2 Overview over the implemented BWs-ADC methods

So far, BWs-ADC is only implemented for particle number preserving excited states (i. e. those accessed by the keyword EE_STATES). Below we provide an overview over the properties of each implemented BWs-ADC method.

- -

**BWs-ADC(0)** is implemented for the sake of completeness. Since all zeroth order ADC schemes yield spin-adapted Koopman excitations as excitation vectors and (dressed) orbital energy differences as the corresponding excitation energies, this method is not recommended for practical use with any parameter choice.
- -

**BWs-ADC(1)** is exactly equal to MP-ADC(1) for excitation energies. If a BWs-ADC(1) calculation is attempted, Q-Chem will crash and refer to a regular ADC(1) calculation instead.
- -

**BWs-ADC(2)-s** has been found to consistently outperform MP-ADC(2) as well as CC2, CIS(D) and CIS(D${}_{\infty}$). Note that it performs best for $A_{0}=3.8$ and $B_{0}=0$ with minimal dependence on $A_{0}$, which is extremely close to the optimal parameter choice for the ground state ($A_{0}=4$, $B_{0}=0$). Also note that any choice of $B_{0}\neq 0$ drastically reduces the excitation energy quality.
- -

**BWs-ADC(2)-x** is implemented for the sake of completeness but has not been benchmarked. Due to the ad hoc inclusion of first order terms in the *2p2h-2p2h* block of the secular matrix, only the second order contribution to the *ph-ph* block carries any dependence on the regularisation parameters. Its performance is therefore expected to mimic that of MP-ADC(2)-x.
- -

**BWs-ADC(3)** was found to perform best for $A_{0}=-1$ and $B_{0}=0$, though similar parameter choices with the constraint of $A_{0}-B_{0}=-1$ exhibit almost the same errors. Note that this parameter choice is *deregularising*, i. e. it cannot describe systems with a vanishing or small HOMO/LUMO gap. For states with weak static correlation and small double excitation character, BWs-ADC(3) strongly outperforms BWs-ADC(2). At the same time, excited states whose proper description requires triples which exhibit significant static correlation are comparatively poorly described, leading to a similar overall MAE to BWs-ADC(2) across benchmarks.

An overview over the methods and recommended parameters and settings is given in table [7.4](#table:bwsadc_overview).

| Method | Comp. Scaling | Rec. ( $A_{0}$ , $B_{0}$ ) | MAE [eV] | When to use |
| --- | --- | --- | --- | --- |
| BWs-ADC(0) | $\mathcal{O}(N^{5})$ | - | - | Never |
| BWs-ADC(2)-s | $\mathcal{O}(N^{5})$ | (4, 0) | 0.16 | Single-reference or few-reference systems |
| BWs-ADC(2)-x | $\mathcal{O}(N^{6})$ | - | - | If benchmarks show it to be successful |
| BWs-ADC(3) | $\mathcal{O}(N^{6})$ | (-1, 0) | 0.16 | Single-reference systems |

Table 7.4: Recommendations for the usage of BWs-ADC($n$) methods. Rec. ($A_{0}$, $B_{0}$) refers to the parameters which were found to be optimal on a benchmark of 122 single excitations across small molecules.[[859]](../bib_references/bib.md#bib895)
 MAE denotes the lowest mean absolute excitation energy error determined on that benchmark using the recommended parameters. Note that the MAE of MP-ADC(2) is 0.21 eV and 0.24 eV respectively

. For a more detailed analysis of method performance, see Ref. 

## 7.10.6.3 Using BWs-ADC in Q-Chem

BWs-ADC calculations are executed in a two-step process inside a single Q-Chem job. First, a RI-BW-s2 calculation inside the `libgmbpt` module is run. Second, the converged dressed orbitals and orbital energies are handed over to `adcman` for the subsequent ADC calculation. For this reason, BWs-ADC is *only* available with the Resolution of Identity approximation.

To run a BWs-ADC calculation, include the following in your input file:

- •

In the REM section, set METHOD to RIBWS2.
- •

In the REM section, specify both BASIS and either AUX_BASIS or AUX_BASIS_CORR
- •

Choose a partitioning with the METHOD keyword in the *$bws2* section. We recommend:

- **–**

Set METHOD to MPR-BWS2 in the *$bws2* section.
- **–**

Set MPR_A0 to the desired $A_{0}$ value in the *$bws2* section.
- **–**

Set MPR_B0 to the desired $B_{0}$ value in the *$bws2* section.
- •

In the *$bws2* section, use the EXC_METHOD keyword to determine the BWs-ADC variant:

- **–**

For BWs-ADC(0), set EXC_METHOD to ADC(0) or ADC0.
- **–**

For BWs-ADC(2)-s, set EXC_METHOD to any of ADC(2), ADC2, ADC(2)-S or ADC2-S.
- **–**

For BWs-ADC(2)-x, set EXC_METHOD to ADC(2)-X or ADC2-X.
- **–**

For BWs-ADC(3), set EXC_METHOD to ADC(3) or ADC3.
- •

For a restricted reference, specify the number of excited states using the EE_STATES or the EE_SINGLETS and EE_TRIPLETS keywords in the REM section.
- •

For an unrestricted reference, only use the EE_STATES keyword.

All keywords used for Job Control of RI-BW-s2 calculations (see section [6.8.2](../ch06_correlation/sect_bws2_jobcontrol.md)) can be used to specify details about the ground state calculation in a BWs-ADC calculation.
Additionally, all keywords used for ADC Job Control (see section [7.10.13](sect_adc_jobcontrol.md)) can be used to adjust the ADC part of a BWs-ADC calculation.
