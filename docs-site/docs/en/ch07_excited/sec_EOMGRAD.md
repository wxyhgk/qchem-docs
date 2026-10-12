---
title: "7.9.21 Analytic Gradients and Properties for CCSD and EOM-XX-CCSD"
---

## 7.9.21 Analytic Gradients and Properties for CCSD and EOM-XX-CCSD

(July 4, 2026)

The coupled-cluster suite in **Q-Chem** can calculate properties of
target EOM states including permanent dipoles, angular momentum projections, static
polarizabilities, $\langle\hat{S}^{2}\rangle$ and $\langle\hat{R}^{2}\rangle$ values, $g$-tensors (CCSD only), nuclear
gradients (and geometry optimizations). The target state of interest
is selected by CC_STATE_TO_OPT in the *$rem* section, which specifies the
symmetry and the number of the EOM state. In addition to state
properties, calculations of various interstate properties are
available, including transition dipoles, angular momentum matrix elements, two-photon absorption transition
moments (and cross-sections), spin–orbit couplings, electronic circular dichroism (ECD) rotatory strengths, Dyson orbitals, and photo-ionization cross sections.

Analytic gradients are available for the CCSD and all EOM-CCSD methods for
both closed- and open-shell references (UHF and RHF only), including frozen
core/virtual functionality[[804]](../bib_references/bib.md#bib838)
 and RI/Cholesky representation of
the two-electron integrals (see also Section [6.16](../ch06_correlation/sec_CCGRAD.md)).
These calculations should be feasible whenever the corresponding single-point energy calculation is feasible.

!!! note "Note"
    Gradients for ROHF and non-HF (*e.g.*, B3LYP) orbitals are not yet available.


For the CCSD and EOM-CCSD wave functions, **Q-Chem** can calculate
permanent and transition dipole moments, oscillator strengths,
ECD rotatory strengths [both in length gauge (origin dependent) and in velocity
gauge (origin independent)], $\langle\hat{R}^{2}\rangle$
(as well as XX, YY and ZZ components separately, which is
useful for assigning different Rydberg states, *e.g.*, $3p_{x}$ vs. $3s$, *etc.*), and the
$\langle\hat{S}^{2}\rangle$ values. Calculation of $g$-tensors is available for CCSD wave functions
(see Section [10.11.4](../ch10_properties/sec_magnetman.md) and example [10.11.4.4](../ch10_properties/sec_magnetman.md#ex:CCSD-gtensor)).

!!! note "Note"
    $g$-tensors can also be computed with state-interaction approach using EOM-CC and RAS-CI
    wave-functions, as described in Ref. [[660]](../bib_references/bib.md#bib684)
    .


Interface of the CCSD and EOM-CCSD codes with the NBO 5.0
package is also available. Furthermore, excited state analyses can be requested for
EOM-CCSD excited states. For EOM-MP2, only state properties (dipole moments, angular momentum
projections, $\langle\hat{R}^{2}\rangle$, $\langle\hat{S}^{2}\rangle$ are available).
Similar functionality is available for some EOM-OD and CI models (CCMAN only).

Analysis of the real- and complex-valued EOM-CC wave functions can also be
performed; see Sections [7.9.30](ex_eomip-wfa.md) and [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md). NTO analysis
for EOM-IP/DIP /EA/DEA/SF states is, obviously, only available for the transitions
between the EOM states, so CC_STATE_TO_OPT keyword needs to be
used, as in calculations of transition properties.

Users must be aware of the point group symmetry of the system being studied and
also the symmetry of the excited (target) state of interest. It is possible to
turn off the use of symmetry using the CC_SYMMETRY. If set to
FALSE the molecule will be treated as having $C_{1}$ symmetry and all
states will be of $A$ symmetry.

**Q-Chem** allows flexible control of interstate properties calculations, by
using the CC_TRANS_PROP keyword or rem section *$trans_prop*: the user can
request the transitions between all computed EOM target states and the
reference state (CC_TRANS_PROP = 1) or the calculations of all
transition properties between all computed EOM target states
(CC_TRANS_PROP = 2). By default, the reference state is the CCSD
reference. To compute transition properties relative to a particular EOM state,
use CC_STATE_TO_OPT.

By default, only one-electron properties are computed. To activate calculations
of two-electron properties, such as NACs, SOCs, 2PA, additional keywords should
be activated, as described below.

The *$trans_prop* input section allows the user to specify precisely which
properties and for which pairs of states to computed. When the *$trans_prop*
section is present in the input, it overrides the setting of the
CC_TRANS_PROP *$rem* variable. However, for *$trans_prop* to work,
CC_TRANS_PROP *does* need to be set.

> ```qchem
> $trans_prop
>    state_list         ! Start a list of states
>    ee_singlets 1 1    ! state 1: EE singlet with irrep = 1 and istate = 1
>    ee_triplets 1 2    ! state 2: EE triplet with irrep = 1 and istate = 2
>    ref                ! state 3: Reference state (can be CC or MP2, but the latter NYI
>                       ! in transition prop driver)
>    end_list           ! End list
>    state_pair_list    ! Start to specify pairs of states,
>    3 1                ! transition from state 3 to state 1 (known bug here: CC state
>                       ! needs to be 1st one)
>    3 2                ! transition from state 3 to state 2 (known bug here: CC state
>                       ! needs to be 1st one)
>    end_pairs          ! End list of pairs
>    calc nac           ! Compute NAC for all transition pairs listed before this keyword
>    state_list         ! Start another list of states (user is able to request multiple
>                       ! state lists for multiple tasks)
>    ref                ! reference state
>    ee_singlets 0 0    ! zero means all requested irreps/istate in $rem
>    end_list
>    calc dipole soc    ! Compute transition dipole and SOC
>    calc opdm_norm     ! Compute norm of transition OPDM
> $end
> ```

Notes about the *$trans_prop* input section:

1. `calc` computes properties for the *first* pair list (or state
list) *before* it.
2. The pair list is *optional*: if there is no pair list, all possible
combinations within the state list will be considered.
3. Options after `calc` include: `nac`, `soc`, `dyson`,
`2pa`, `dipole`, `default`, `pcm`, `opdm_norm`,
`wfa`, `ang`, `linmom`, `dipole linmom`, `ecd`. Currently, only some of them are implemented.

!!! note "Note"
    The *$trans_prop* section is a new feature and is still under development —
    use at your own risk. Eventually, this section will replace other controls and
    will become a default.


## 7.9.21.1 Calculations of Angular Momentum Matrix Elements Using EOM-CC Wave Functions

Angular momentum matrix elements can be useful for analyzing wave functions, assigning state characters, or
identifying term
symmetry labels in linear molecules. As other one-electron properties, these matrix elements
are evaluated using one-particle state and transition density matrices.
Angular momentum is a gauge-dependent property, meaning that its value depends on the origin of the gauge.
The gauge position can be controlled with *$gauge_origin* input section.
The default position of the gauge corresponds to the $(0,0,0)$ of the coordinate system.

> ```qchem
> $gauge_origin            Position of the gauge origin for
>    1.00  0.200  0.500       angular momentum calculations in angstroms.
> $end
> ```

## 7.9.21.2 EOM-CC Oscillator Strengths in Velocity and Mixed Gauges

The oscillator strength of one-photon absorption is usually calculated in the length gauge (“lg”)

<a id="Ch7.E110"></a>

$$
f^{\rm{lg}}=\frac{2\omega_{fn}}{3}\sum_{\alpha=x,y,z}\langle n|\hat{\mu}_{\alpha}|f\rangle\langle f|\hat{\mu}_{\alpha}|n\rangle, \tag{7.110}
$$

where $\hat{\mu}$ is the electric dipole moment operator,
but it can also be expressed in velocity gauge (“vg”) and mixed gauge (“mx”) as follows

<a id="Ch7.E111"></a>

$$
f^{\rm{vg}}=\frac{2}{3\omega_{fn}}\sum_{\alpha=x,y,z}\langle n|\hat{p}_{\alpha}|f\rangle\langle f|\hat{p}_{\alpha}|n\rangle, \tag{7.111}
$$

<a id="Ch7.E112"></a>

$$
f^{\rm{mx}}=\frac{2i}{3}\sum_{\alpha=x,y,z}\langle n|\hat{\mu}_{\alpha}|f\rangle\langle f|\hat{p}_{\alpha}|n\rangle, \tag{7.112}
$$

where $\hat{p}$ is the linear momentum operator.

All three gauges are implemented as part of the EOM-CCSD transition properties in **Q-Chem**.
Whereas $f^{\rm lg}$ is computed as the default transition property, the other two must be activated. This is done in the *$trans_prop* input section by specifying `calc linmom` for velocity gauge only, or `calc dipole linmom` for all three gauges.
This is illustrated in Example [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1).

Note that:

- –

If the calculation of ECD is activated in the input, $f^{\rm lg}$, $f^{\rm vg}$, and $f^{\rm mx}$ will also be computed;
- –

If the energy separation between the two states is very small (threshold = $10^{-6}$), as in case of (near)-degenerate states,
a warning is issued and the calculation of the velocity gauge strength is skipped.

## 7.9.21.3 Calculations of EOM-CC Rotatory Strengths (ECD and XCD) in Length and Velocity Gauges

**Q-Chem** affords ECD and XCD calculations using EOM-CC wave functions using formalism and implementation described in
Ref. [[46]](../bib_references/bib.md#bib29)
.
The rotatory strength of ECD within CC theory is defined as:

<a id="A3.S8.EGx56"></a>

$$
\displaystyle R^{\text{lg}}_{nf} \tag{7.113}
$$

in the length (“lg”) and velocity (“vg”) formulations, respectively. $\hat{\mu}$ is the electric dipole moment operator and $\hat{p}$ is the linear momentum operator. The length-gauge expression in Eq. ([7.113](#eq:length)) is gauge-origin dependent, whereas Eq. ([7.114](#eq:velocity)) is gauge-origin independent.

ECD is available for ground-state and excited-state EOM-EE-CCSD transitions in the valence and core-excited regimes. The latter
is based on the fc-CVS-EOM-EE-CCSD framework. ECD is also available for the transitions between EOM-EA-CCSD states. The ECD calculations are not available for EOM-IP/EOM-DIP calculations yet.

The computation of rotatory strengths is activated in the input by either
activating CC_EOM_ECD or via *$trans_prop* section, as illustrated in Example [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1).
In the latter case, the user can either request the calculation of
the transition dipole moment, linear momentum, and angular momentum operators together (“`calc dipole linmom ang`”)
or request ECD only (“`calc ecd`”).

Note that:

- –

Rotatory strengths will be computed in both length and velocity gauge;
- –

Oscillator strengths in length, velocity, and mixed gauges will be computed as well;
- –

If the energy separation between the two states is very small (threshold = $10^{-6}$), as in the case of (near)-degenerate s
states, a warning is issued and the calculation of the velocity gauge strength is skipped.

## 7.9.21.4 Calculations of Spin-Orbit Couplings Using EOM-CC Wave Functions

Calculations of spin-orbit couplings (SOCs) for EOM-CC wave functions is
available in CCMAN2.[[364]](../bib_references/bib.md#bib370)

We employ a perturbative approach
in which SOCs are computed as matrix elements of the respective part of the
Breit–Pauli Hamiltonian using zero-order non-relativistic wave functions.
There are two versions of the code that can be engaged by using CALC_SOC.
The old code computes SOC as a matrix element between a
pair of states that need to be explicitly computed; thus, it is able to produce
only one matrix element per transition. Although this approach can be used to
extract the whole matrix through rotations of the molecule,[[1107]](../bib_references/bib.md#bib1150)

the relative phases of these matrix elements are
lost. The new version of the code solves this issue and also improves
performance.[[1103]](../bib_references/bib.md#bib1151)
 The new code uses
Wigner–Eckart’s theorem to compute the entire spin-orbit matrix. We
partition excitation operators by their spin properties. Since the spin–orbit
operator is a triplet operator, we can consider the following triplet
excitation operators

<a id="A3.S8.EGx57"></a>

$$
\displaystyle T^{1,1}_{p,q}=-a^{\dagger}_{p\alpha}a_{q\beta} \tag{7.115}
$$

If we apply Wigner–Eckart’s theorem, the following matrix elements are
decomposed into the Clebsch–Gordan coefficients and reduced matrix elements:

<a id="eq:WignerEckart_u"></a>

$$
\langle\Psi_{I}SM|T^{1,k}_{p,q}|\Psi_{J}S^{\prime}M^{\prime}\rangle=\langle S^{\prime}M^{\prime}|1k|SM\rangle\langle\Psi_{I}S||T^{1,\cdot}_{p,q}||\Psi_{J}S^{\prime}\rangle, \tag{7.118}
$$

where $S$ and $S^{\prime}$ denote spins, and $M$ and $M^{\prime}$ denote spin
projections of $\Psi_{I}$ and $\Psi_{J}$, respectively. The reduced matrix
elements form a new, spinless triplet transition density matrix, which we will
denote as $u^{1,\cdot}$. The spin-orbit reduced matrix elements are obtained
as a trace with $u^{1,\cdot}$:

<a id="A3.S8.EGx58"></a>

$$
\displaystyle\langle\Psi_{I}S||H_{L_{-}}||\Psi_{J}S^{\prime}\rangle=-\frac{1}{2}\sum_{p,q}h^{SO}_{L_{-};p,q}u^{1,\cdot}_{p,q} \tag{7.119}
$$

Applying Wigner–Eckart’s theorem again, all possible matrix elements are
generated from reduced matrix elements. This algorithm is available for the
EOM-EE/SF/IP/EA/DIP /DEA wave functions for MP2 and CCSD references, as well as between the CCSD reference and EOM-EE/SF.
Examples [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1), [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1), [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) illustrate
calculations of SOCs for various EOM-CC models.

```qchem
A(Ket)->B(Bra) transition SO matrices
 Analyzing Sz ans S^2 of the pair of states...
 Ket state:  Computed S^2 = 2.019877 will be treated as 2.000000 Sz = 0.000000
 Bra state:  Computed S^2 = 0.019216 will be treated as 0.000000 Sz = 0.000000
 Clebsch-Gordan coefficient: <1.000,0.000;1.000,0.000|0.000,0.000> = 0.577
 One-electron SO (cm-1)
 Reduced matrix elements:
 <S|| Hso(L-) ||S’> = (-2.660965,-22.180075)
 <S|| Hso(L0) ||S’> = (0.000000,-20.019517)
 <S|| Hso(L+) ||S’> = (-2.660965,22.180075)
 SOCC = 21.593626
 Actual matrix elements:
       |Sz=-1.00>           |Sz=0.00>           |Sz=1.00>
 <Sz=0.00|(1.536309,12.805673)(0.000000,-11.558274)(1.536309,-12.805673)
 Mean-field SO (cm-1)
 Reduced matrix elements:
 <S|| Hso(L-) ||S’> = (-2.069801,-9.910572)
 <S|| Hso(L0) ||S’> = (0.000000,-10.692261)
 <S|| Hso(L+) ||S’> = (-2.005570,9.957712)
 Singlet part of <S|| Hso(L0) ||S’> = (-0.000000,0.037101) (excluded from all matrix elements)
 L-/L+ Averaged reduced matrix elements:
 <S|| Hso(L-) ||S’> = (-2.037685,-9.934142)
 <S|| Hso(L+) ||S’> = (-2.037685,9.934142)
 SOCC = 10.328006
 Actual matrix elements:
       |Sz=-1.00>           |Sz=0.00>           |Sz=1.00>
 <Sz=0.00|(1.176458,5.735480)(0.000000,-6.173180)(1.176458,-5.735480)
```

The algorithm is activated by setting CALC_SOC to 1 or 2. The
execution relies on a non-zero Clebsch-Gordan coefficient (otherwise, it is not
possible to extract the necessary information from the transition density
matrix). If the Clebsch-Gordan coefficient is zero, a warning will be printed,
and the transition will be skipped. Usually it is possible to select the
states, leading to non-zero Clebsch-Gordan coefficients, by selecting SF or EE,
alpha or beta electrons in case of EA or IP. Determination of state
multiplicities is based on $\hat{S}^{2}$. In case of a strong spin contamination, a
warning is printed, and the closest multiplicity is assumed.

In the case of open-shell references, the resulting reduced matrix elements may
violate symmetries implied by the spin-orbit operator. Setting
CALC_SOC to 1 will produce these reduced matrix elements, but the
actual spin-orbit matrix will be produced from the *averaged* reduced
matrix elements, in which the desired symmetry is restored. Setting
CALC_SOC to 2 will form spin-orbit matrix without averaging of
reduced matrix elements. Although in practice the difference between these two
options is small, the averaging may simplify the analysis of splittings.
Examples [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) and [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1)
illustrate calculation of SOC using SOMF
in the acetylene-O complex.

!!! note "Note"
    In the case of ECP, attempts to compute SOCs using the above algorithms
    (with CALC_SOC=1 or 2)
    will, most likely, result in unphysically low SOC values.
    Instead, we recommend using effective charges (CALC_SOC=4).


To activate the NTO analysis of the spinless one-particle transition density matrices,[[1105]](../bib_references/bib.md#bib1152)

and to compute spin-orbit integrals over NTOs,
set STATE_ANALYSIS = TRUE , MOLDEN_FORMAT = TRUE,
in addition to CALC_SOC = 1, 2, or 4.

**Q-Chem** also affords computing SOCs using one-electron SO operator with
effective nuclear charges.[[380]](../bib_references/bib.md#bib384)

The rational for this approach is that the effect of the
mean-field two-electron part of the SOC operator
can be approximated by screened nuclear charges.
In the case of all-electron calculations (no ECP), this approach is less rigorous than SOMF,
but it does not use two-electron integrals at all and is, therefore, less expensive.
Moreover, using effective charges allows one to obtain reasonable values of SOCs with ECPs.
This calculation is activated by using CALC_SOC = 4. **Q-Chem** output will contain
one-electron SOCs computed with the original and screened (effective) nuclear charges.
In the case of open-shell references, SOCs are computed using $L_{+}/L_{-}$ averaging (as
for the CALC_SOC = 1 case). By default, the calculations use effective
charges from Fedorov *et al.*,[[380]](../bib_references/bib.md#bib384)
 tabulated for elements Li through At,
except for lanthanides. For all-electron calculations,
the effective charges from the 6-31G basis are used, and for ECPs, SBKJC charges are used.
Alternatively, the user can provide user-defined effective charges via input section
*$soc_eff_charges*, as follows:

> ```qchem
> $soc_eff_charges
>    8.0  6.0   !use eff. charge=6 for oxygen (Z=8)
>    17.0 11.0 !use eff. charge=11 for chlorine (Z=17)
> $end
> ```

Examples [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) and [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) illustrate this capability.

The legacy code has the full two-electron treatment and the mean-field
approximation. To enable the SOC calculation, transition properties between
EOM states must be enabled via CC_TRANS_PROP, and SOC requested
setting CALC_SOC to 3. By default, one-electron and mean-field
two-electron couplings will be computed. Full two-electron coupling calculation
is activated by setting CC_EOM_PROP_TE.

As with other EOM transition properties, the initial EOM state is set by
CC_STATE_TO_OPT, and couplings are computed between that state and
all other EOM states. In the absence of CC_STATE_TO_OPT, SOCs are
computed between the reference state and all EOM-EE or EOM-SF states.

!!! note "Note"
    In a spin-restricted case, such as EOM-EE calculations using closed-shell
    reference state, SOCs between the singlet and triplet EOM manifolds cannot be
    computed (only SOCs between the reference state and EOM triplets can be
    calculated). To compute SOCs between EOM-EE singlets and EOM-EE triplets, run
    the same job with UNRESTRICTED = TRUE, such that triplets and
    singlets appear in the same manifold.


!!! note "Note"
    The most flexible control for computing transition properties is afforded by the
    *$trans_prop* input section, as described in Section 7.9.21.


## 7.9.21.5 Calculations of Non-Adiabatic Couplings Using EOM-CC Wave Functions

Calculations of nonadiabatic (derivative) couplings (NACs) for EOM-CC wave functions is
available in CCMAN2. We employ Szalay’s approach in which couplings are computed
by a modified analytic gradient code, via “summed states”:[[1336]](../bib_references/bib.md#bib1394)

<a id="eq:Szalay:ExactH"></a>

$$
h^{x}_{IJ}\equiv\langle\Psi_{I}|H^{x}|\Psi_{J}\rangle=\frac{1}{2}\left(G_{(I+J)}-G_{I}-G_{J}\right), \tag{7.122}
$$

where, $G_{I}$, $G_{J}$, and $G_{IJ}$ are analytic gradients for states $I$, $J$,
and a fictitious summed state $|\Psi_{I+J}\rangle\equiv|\Psi_{I}\rangle+|\Psi_{J}\rangle$. Currently, NACs for EE/IP/EA are available.[[375]](../bib_references/bib.md#bib380)

!!! note "Note"
    Note that the individual components of the NAC vector depend on the
    molecular orientation.


## 7.9.21.6 Transition Moments and Cross Sections for Two-Photon Absorption
within EOM-EE-CCSD

Calculation of transition moments and cross-sections for two-photon absorption
for EOM-EE-CCSD wave functions is available in **Q-Chem** (CCMAN2 only). Both
CCSD-EOM and EOM-EOM transitions can be computed. The formalism is described in
Ref. [[977]](../bib_references/bib.md#bib1018)
. This feature is available both for canonical and
RI/CD implementations. The undamped canonical 2PA cross sections between EOM-DEA-CCSD states
are also available. Relevant keywords are CC_EOM_2PA (turns on
the calculation, controls NTO calculation), CC_STATE_TO_OPT (used
for EOM-EOM transitions); additional customization can be performed using the
*$2pa* section. The quantity printed out is the microscopic cross-section
$\delta^{TPA}$ (also known as rotationally averaged 2PA strength), as defined
in Eq. (30) of Ref. [[977]](../bib_references/bib.md#bib1018)
.

The *$2pa* section is used to specify the range of frequency-pairs satisfying
the resonance condition. If *$2pa* section is absent in the input, the
transition moments are computed for 2 degenerate photons with total energy
matching the excitation energy of each target EOM state (for CCSD-EOM) or each
EOM-EOM energy difference (for EOM-EOM transitions): $2h\nu=E_{ex}$
For resonant or near-resonant calculations (*i.e.*, when one of the photons is in
resonance with an excited state), damped response theory should be used;
such calculations are deployed by adding DAMPED_EPSILON in the *$2pa* section
(the value of $\epsilon$ is specified in hartrees, 0.001 is usually sufficient).

> ```qchem
> $2pa                      Non-degenerate resonant 2PA
>    N_2PA_POINTS 6         Number of frequency pairs
>    OMEGA_1 500000 10000   Scans 500 cm$^{-1}$ to 550 cm$^{-1}$
>                           in steps of 10 cm$^{-1}$
> $end
> ```

N_2PA_POINTS is the number of frequency pairs across the spectrum.
The first value associated with OMEGA_1 is the frequency $\times 1000$ in cm${}^{-1}$ at the start of the spectrum and the second value is the
step size $\times 1000$ in cm${}^{-1}$. The frequency of the second photon at
each step is determined within the code as the excitation energy minus
OMEGA_1.

To gain insight into computed cross sections for 2PA, one can perform NTO
analysis of the response one-particle density matrices [[979]](../bib_references/bib.md#bib1020)
. To
activate NTO analysis of the 2PA response one-particle transition density
matrices, set STATE_ANALYSIS = TRUE, MOLDEN_FORMAT
= TRUE (to export the orbitals as **MolDen** files),
NTO_PAIRS (specifies the number of orbitals to print). The NTO
analysis will be performed for the full 2PA response one-particle transition
density matrices as well as the normalized $\omega$DMs (see
Ref. [[979]](../bib_references/bib.md#bib1020)
 for more details).

By default, both undamped and damped 2PA response wave functions are computed using a new
iterative Davidson-like subspace procedure called the **Dalton** solver.[[248]](../bib_references/bib.md#bib251)

It is controlled by the DALTON_XCONV, DALTON_PRECOND_START,
DALTON_MAXITER, and DALTON_MAXSPACE
keywords. Damped 2PA response wave functions can also be computed using the older
DIIS procedure by setting DAMPED_DALTON_SOLVER = FALSE.
The DIIS solver is controlled by the
CC_MAX_ITER, CC_DIIS_START,
CC_DIIS_SIZE, CC_EOM_2PA_ECONV, and CC_EOM_2PA_XCONV.

!!! note "Note"
    The **Dalton** solver uses square of the norm of the residual in estimating convergence (as in the Davidson solver),
    whereas the DIIS solver uses the norm of the difference of the response vector between iterations.


2PA calculations can be carried out using single precision, by activating
CC_EOM_2PA_SINGLE_PREC keyword, in addition to the keywords activating
single-precision execution of CC and EOM-CC equations (see Section [7.9.15](sec_SP_EOM_CC.md).
Capabilities for computing other non-linear properties include RIXS (see Section [7.9.9.1](sub_cvs_eom.md#sec:cvs_eom_rixs))
and static and dynamic polarizabilities (Section [7.9.21.8](#sec:EOMpol)).

## 7.9.21.7 Calculation of Optical Rotation for CCSD Wave Function

**Q-Chem** affords calculations of the optical rotation (OR) tensor and the related specific optical rotation[[1058]](../bib_references/bib.md#bib1103)

(at a chosen frequency corresponding to
the polarimeter’s operating lamp) for a CCSD wave function (in CCMAN2)[[46]](../bib_references/bib.md#bib29)
. The theory is based on the
expectation-value approach, *i.e.*, the sum-over-states expressions recast into closed-form expressions using response
states[[46]](../bib_references/bib.md#bib29)
. The calculation involves computing regular or damped
response wave functions. Length gauge, velocity gauge, and modified velocity gauge are used[[1059]](../bib_references/bib.md#bib1104)
.

The calculation of the regular (i.e., undamped) optical rotation is deployed by setting CC_OPTROT to 5 and involves computing
(undamped) density matrices using zero-order and response wave functions.
If the frequency of probing linearly-polarized (lp) light is nearly resonant with an excitation energy, the undamped response
calculations
diverge. By augmenting the frequency with a phenomenological imaginary damping factor
(*e.g.*, 0.001 hartree), the corresponding
damped response wave functions are computed.

In the length (velocity) gauge, the real (imaginary) part of the damped optical rotation tensor corresponds to the differential absorption of
the two circularly polarized components of the lp light, *i.e.*, to the electronic circular dichroism (ECD).
The imaginary (real) part corresponds to the dispersion (ORD).
Currently, these features are available for the canonical implementation only (no RI/CD).

!!! note "Note"
    CC_FULLRESPONSE must be set to 0 and
    CC_REF_PROP must be set to TRUE for these
    calculations.


The response equations for OR are solved using the same solver as the response equations for polarizabilities
(see Section [7.9.21.8](#sec:EOMpol) for relevant keywords).

A typical *$opt_rot* section input for a regular (undamped) optical rotation calculation at the sodium D-line
(589.6 nm = 16960.651 cm${}^{-1}$) is:

> ```qchem
> $opt_rot
> omega_1  16960651 0 1    !One calculation at D-line
> damped_epsilon 0.0       ! Disables damped OR [mandatory].
> length_gauge <0 or 1>    ! Computes length-gauge OR if set to 1
> velocity_gauge <0 or 1>  ! Computes (modified) velocity gauge OR if set to 1
> $end
> ```

For a damped calculation, the frequency range, damping factor, and gauge choice are selected using the *$opt_rot* section as follows:

> ```qchem
> $opt_rot
> omega_1  500000 10000 6  !Scans 500 cm$^{-1}$ to 550 cm$^{-1}$
>                          !      in steps of 10 cm$^{-1}$
> damped_epsilon 0.01      ! (Optional) Use for damped CCSD OR only.
>                          ! Sets a damping factor of 0.01 Hartrees.
> length_gauge <0 or 1>    ! Computes length-gauge OR if set to 1
> velocity_gauge <0 or 1>  !Computes (modified) velocity gauge OR if set to 1
> $end
> ```

!!! note "Note"
    Like other transition properties, ECD/XCD spectra can also be computed
    from the rotatory strengths between EOM-CC/CVS-EOM-CC states.
    See Section 7.9.21.


## 7.9.21.8 Calculations of Static and Dynamic Polarizabilities for CCSD and EOM-CCSD
Wave Functions

Calculation of the static and dynamic dipole polarizabilities for CCSD and EOM-EE/SF-CCSD
wave functions is available in CCMAN2. Polarizabilities are calculated as
second derivatives of the CCSD or EOM-CCSD energy[[978]](../bib_references/bib.md#bib1019)
 as well as
using the expectation-value approach, *i.e.*, the sum-over-states expression for
the exact wave function[[976]](../bib_references/bib.md#bib1021)
. In the analytic derivative approach
(or the response-theory formalism), only the response of the cluster amplitudes
is taken into the account; orbital relaxation is not included.
CC_FULLRESPONSE must be set to 2 to turn off the orbital
relaxation but allow amplitude response in EOM calculations, if the
polarizabilities are to be computed with this approach (both CC_POL
and EOM_POL must equal 1 or 2). CC_POL
and EOM_POL = 3 or 4 coupled with
CC_FULLRESPONSE = 0 will enable expectation-value
polarizabilities. Note that CC_REF_PROP and CC_EOM_PROP/
must be set to TRUE for these calculations.

Dynamic polarizabilities are enabled using the *$dyn_pol* section, which
specifies the frequency range. Without this section, only the static
polarizabilities will be computed.
CCSD and EOM-EE/SF-CCSD dynamic polarizabilities for imaginary frequencies
are also available through the use of the *$dyn_pol* section.
CCSD static and dynamic polarizabilities within the damped response theory are also available,
which can be turned on by specifying the *damped_epsilon* variable in the
*$dyn_pol* section.

> ```qchem
> $dyn_pol
>    500000 10000 6  ! Scans 500 cm$^{-1}$ to 550 cm$^{-1}$
>                    !       in steps of 10 cm$^{-1}$
> damped_epsilon 10  ! (Optional) Use for damped CCSD polarizabilities only.
>                    ! Sets a damping factor of 10/1000 Hartrees.
> $end
> ```

Currently, these features are available for the canonical implementation only.

!!! note "Note"
    EOM-CCSD polarizabilities are available for the EE and SF wave functions only.


By default, both undamped and damped polarizability response wave functions are computed using a new
iterative Davidson-like subspace procedure called the **Dalton** solver.[[248]](../bib_references/bib.md#bib251)

It is controlled by the DALTON_XCONV, DALTON_PRECOND_START,
DALTON_MAXITER, and DALTON_MAXSPACE
keywords. Damped polarizability response wave functions can also be computed using the older DIIS solver
by setting DAMPED_DALTON_SOLVER = FALSE. The DIIS solver is controlled by CC_MAX_ITER, CC_DIIS_START, CC_DIIS_SIZE, and CC _CONVERGENCE.

!!! note "Note"
    The **Dalton** solver uses square of the norm of the residual in estimating convergence (as in the Davidson solver), whereas the DIIS solver uses the norm of the difference of the response vector between iterations. The default threshold for convergence in response calculations (2PA, polarizability, RIXS) is 5.


## 7.9.21.9 Calculations of Static and Dynamic First Hyperpolarizabilities for CCSD Wave Functions

Calculation of the static and dynamic dipole first hyperpolarizabilities for CCSD
wave functions is available in CCMAN2 (currently, canonical implementation only).
First hyperpolarizabilities are computed within the damped-response expectation-value
approach[[981]](../bib_references/bib.md#bib1024)
.
Setting CC_1HPOL to 1 deploys the algorithm that
computes this property with the least number of response wave-function calculations.
Setting CC_1HPOL to 3, computes this property by constructing
the second-order response density matrices, which involves computing a
large number of second-order response wave functions. These second-order response
density matrices are then used to compute second-order response natural orbitals
using **libwfa** for quantitative wave-function and orbital analyses.
Calculations of first hyperpolarizabilities require the *$1hpol* section, which
specifies the frequency ranges of the two photons ($\omega_{1}$ and $\omega_{2}$;
$\omega_{3}=\omega_{1}+\omega_{2}$),
as well as the corresponding damping factors.

!!! note "Note"
    CC_FULLRESPONSE must be set to 0
    and CC_REF_PROP must be set to TRUE for these calculations.


> ```qchem
> $1hpol
> omega_1 0000000 1500000 3 0.01 !Scans omega_1 from 0 cm$^{-1}$ to (3-1)*1500 cm$^{-1}
>                                ! in steps of 1500 cm$^{-1}
>                                ! damping factor epsilon_1 is 0.01 Hartrees
> omega_2 0000000 2500000 4 0.01 !Scans omega_2 from 0 cm$^{-1}$ to (4-1)*2500 cm$^{-1}
>                                ! in steps of 2500 cm$^{-1}
>                                ! damping factor epsilon_2 is 0.01 Hartrees
> omega_3 0.01                   ! damping factor epsilon_3 is 0.01 Hartrees
> $end
> ```

Example [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) computes
static and dynamic first hyperpolarizability for CCSD/STO-3G wave function for LiH using the framework of damped response theory and
the expectation-value approach.
The property for the following set of 3 photons is calculated (frequencies in cm${}^{-1}$):
(0, 0; 0), (2500, 0; -2500), (5000, 0; -5000), (0, 3500; -3500), (0, 7000; -7000), (2500, 3500; -6000), (2500, 7000; -9500),
(5000, 3500; -8500), (5000, 7000; -12000).

## 7.9.21.10 Photoionization and Photodetachment Cross Sections and PADs

**Q-Chem** can compute quantities describing photo-ionization/photodetachment
following the theoretical framework based on Dyson orbitals[[478]](../bib_references/bib.md#bib490)
.
One can use computed Dyson orbitals and then calculate cross sections using the stand-alone
**ezDyson** code[[478]](../bib_references/bib.md#bib490)
 or request such calculations to be done by **Q-Chem**;
the latter version is more efficient.
These calculations require Dyson orbitals, which connect the initial and target states, and
a wave-function of the free electron. Currently, only plane-wave treatment is available. This
feature is only available in ccman2.

Total and angular-resolved photoionization cross sections can be computed by using the following
set-up. First, the user should request calculation of appropriate initial and target states
and the corresponding Dyson orbitals (using CC_DO_DYSON keyword) or the corresponding setting in *$trans_prop* section). Second, CC_FREE_ELECTRON should be set to TRUE.
Third, the parameters
for the cross sections—such as polarization of the light, energy range of photoelectrons, and details of
orientational averaging—should be specified in the *$free_electron* section.

> ```qchem
> $free_electron
> N_ENERGY_POINTS 20  !number of points in the kinetic energy grid
> KE_MIN 10   !minimum kinetic energy of the free-electron in 1E-2  eV (here, 0.1 eV)
> KE_MAX 1010  !maximum kinetic energy of the free-electron in 1E-2  eV  (here, 10.1 eV)
> SPIN_DEG 2  !spin degeneracy factor
> ORB_DEG 1  !orbital degeneracy factor
> POL_X 0  !X-component of the polarization vector in 1E-2 (here, 0)
> POL_Y 0  !Y-component of the polarization vector in 1E-2 (here, 0)
> POL_Z 100  !Z-component of the polarization vector in 1E-2 (here, 1)
> CIRC_POL 0  !if circular polarization is requested
> DO_AVERAGE 0  !if orientational averaging to be performed
> N_THETA 50  !number of theta-points in the angular grid
> N_PHI 10  !number of phi-points in the angular grid
> $end
> ```

Using a similar setup, one can also compute overlap between a Dyson orbital and
a plane wave. This calculation is activated by the DYSON_PW_COUPLING keyword
(CC_DO_DYSON should also be set to TRUE).
The parameters for the calculation, such as number of $|{\mathbf{k}}|$-values
and whether averaging over different ${\mathbf{k}}$-orientations should be performed,
are specified in *$free_electron* section. Examples [7.9.29.2](topic_dyson.md#ex:DYSONPW) and [7.9.29.2](topic_dyson.md#ex:DYSONPW)
and excerpts below illustrate this capability. The default is no averaging and five grind points for
$|{\mathbf{k}}|$.

> ```qchem
> $free_electron
> k_avg  1  !perform averaging over k-orientations using default grid of 50( theta)x10(phi)
> k_grid_points 6  !Coupling computed for |k|-values  from 0.0 eV to 0.1x(k_grid_points -1)
> $end
> ```

!!! note "Note"
    The grid of $|{\mathbf{k}}|$ values is computed as
    $\sqrt{2E}$ where $E$ runs from 0.0 eV to 0.1*($k\_grid\_points$-1) eV.


> ```qchem
> $free_electron
> k_x  100  ! kx=1 (k_x/100)
> k_y  100  ! ky=1
> k_z  100  ! kz=1
> k_grid_points 6  ! coupling computed for  |k|-values  from 0.0 eV to 0.1x(k_grid_points -1)
> $end
> ```

!!! note "Note"
    The magnitude of $|{\mathbf{k}}|$ does not matter, only direction does.


Photoelectron angular distribution (PAD) — $\Omega(\theta,\phi)$,
where $\theta$ and $\phi$ are angular coordinates of the photoelectron’s vector
$\mathbf{k}$ in the lab frame — will be written in separate files
for each ionized state (i.e., pad_1A1, pad_1B2, etc). For a linear polarization, asymmetry parameter $\beta$ will be calculated along with
the cross section.
Input parameters for the calculation are specified through the *$free_electron* section.
The default values are: SPIN_DEG=2, ORB_DEG=1, and DO_AVERAGE=0 (no averaging).
The calculations require a number of $\theta$ and $\phi$ points to be specified by the user
(defaults are 50 and 10 respectively) to determine the directions of the wave-vector $\mathbf{k}$
for computing PAD.
The user should specify either the three components of the polarization (for linear polarization)
or the circular polarization; the two options are mutually exclusive. For circular-polarized light,
$z$ is the direction of light propagation.
If DO_AVERAGE is set to 1, averaging over all molecular orientations is performed
and polarization of light is assumed to be along the $z$-axis (the polarization setting
will be ignored).
These features are illustrated in examples [7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1)-[7.9.22.1](Ch7.S9.SS22.md#ex:CCFE1) below.

### `CC_FREE_ELECTRON`

> **Specifies whether properties involving free electrons will be computed.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE/FALSE`
> * **Recommendation**: None

### `DYSON_PW_COUPLING`

> **Calculate overlap between Dyson orbital and plane wave.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE (do not compute coupling)`
> * **Options**:
>     * `TRUE/FLSE`
> * **Recommendation**: Activate when needed. CC_DO_DYSON must be turned on.
