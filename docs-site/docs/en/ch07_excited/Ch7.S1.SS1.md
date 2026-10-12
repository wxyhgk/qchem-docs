---
title: "7.1.1 Overview"
---

## 7.1.1 Overview

(July 4, 2026)

As for ground state calculations, performing an adequate excited-state
calculation involves making an appropriate choice of method and basis set. The
development of effective approaches to modeling electronic excited states has
historically lagged behind advances in treating the ground state. In part this
is because of the much greater diversity in the character of the wave functions
for excited states, making it more difficult to develop broadly applicable
methods without molecule-specific or even state-specific specification of the
form of the wave function. Recently, however, a hierarchy of single-reference
*ab initio* methods has begun to emerge for the treatment of excited
states. Broadly speaking, **Q-Chem** contains methods that are capable of giving
qualitative agreement, and in many cases quantitative agreement with experiment
for lower optically allowed states. The situation is less satisfactory for
states that involve two-electron excitations, although even here reasonable
results can sometimes be obtained. Moreover, some of the excited state methods
can treat open-shell wave functions, *e.g.* diradicals and triradicals, ionized and electron
attachment states and more.

In excited-state calculations, as for ground state calculations, the user must
strike a compromise between cost and accuracy. This chapter
summarizes **Q-Chem**’s capabilities in four general classes of excited state methods:

- •

Single-electron wave function-based methods (Section [7.2](sect_noncorr.md)).
These are excited state treatments of roughly the same level of
sophistication as the Hartree-Fock ground state method, in the sense
that electron correlation is essentially ignored. Single excitation
configuration interaction (CIS) is the workhorse method of this type.
The spin-flip variant of CIS extends it to diradicals and other situations with small HOMO-LUMO gaps.
- •

Time-dependent density functional theory (TDDFT,
Section [7.3](sect_tddft.md)). TDDFT is a widely used extension of DFT to
excited states. For a cost that is only a little larger than that of a
CIS calculation, TDDFT typically affords significantly greater accuracy due to
a treatment of electron correlation. It, too, has a spin-flip variant (as well as its improved
version, mixed reference SF-TDDFT) that can
be used to study di- and tri-radicals as well as bond breaking.
- •

The Maximum Overlap Method (MOM) for excited $\Delta$SCF states
(Section [7.7.2](ex_OpSing.md)). This method overcomes some of the deficiencies of
TDDFT and, in particular, can be used for modeling charge-transfer and Rydberg
transitions as well as core-excited states.
- •

Restricted open-shell Kohn-Sham (ROKS) method is a spin-purified,
orbital optimized approach for excited states (Section [7.7.4](ex_ESROKS.md)).
It is very accurate for modeling charge-transfer states and core-excitations.
- •

The Square Gradient Minimization (SGM) algorithm can be used to converge both $\Delta$SCF
and ROKS excited states. Details about using SGM in practice can be found in
Section [4.5.15](../ch04_scf/sect_SGM-SCF.md).
- •

The State-Targeted Energy Projection (STEP) algorithm (Section [7.7.8](ex_ROSTEP.md))
is available for $\Delta$SCF and ROKS excited states. It is less expensive than SGM
and usually more robust than MOM.
- •

Wave function-based electron correlation treatments
(Sections [7.8](sect_excorr.md), [7.10](sect_exadc.md), [7.11](topic_rasi.md) and [7.9](topic_eomcc.md)).
Roughly speaking, these are excited state analogues of the ground state
wave function-based electron correlation methods discussed in
Chapter [6](../ch06_correlation/chap_correlation.md). They are more accurate than the methods
of Section [7.2](sect_noncorr.md), but also significantly more
computationally expensive. These methods can also describe certain
multi-configurational wave functions, for example, problematic doublet
radicals, diradicals, triradicals, and more.

**Note: 

Core electrons are frozen by default in most correlated excited-state
calculations (see Section [6.2](../ch06_correlation/sec_core.md)).
**

In general, a basis set appropriate for a ground state density functional
theory or a Hartree-Fock calculation will be appropriate for describing
valence excited states. However, many excited states involve significant
contributions from diffuse Rydberg orbitals, and, therefore, it is often
advisable to use basis sets that include additional diffuse functions. The
6-31+G* or aug-cc-pVDZ basis sets are a reasonable compromise for the low-lying valence excited
states of many organic molecules. To describe true Rydberg excited states,
**Q-Chem** allows the user to add two or more sets of diffuse functions (see
Chapter [8](../ch08_basis/chap_basis.md)). For example the 6-311(2+)G* basis includes two sets
of diffuse functions on heavy atoms and is generally adequate for description
of both valence and Rydberg excited states.

**Q-Chem** supports four main types of excited state calculation:

- •

**Vertical absorption spectrum

**This is the calculation of the excited states of the molecule at the
ground state geometry, as appropriate for absorption spectroscopy. The
methods supported for performing a vertical absorption calculation are:
CIS, RPA, XCIS, SF-XCIS, CIS(D), ADC(2)-s, ADC(2)-x,
ADC(3), RAS-SF, EOM-CCSD or EOM-OD, and EOM-CCSDT, each of which will be discussed in turn.
The calculation of core-excited states for the simulation of
x-ray absorption spectra can be performed with TDDFT as well as
EOM-CCSD and ADC within the CVS approximation
Section [7.12](sec_CoreLevels.md)). All ADC- and EOM-based methods can be combined
with the polarizable continuum model (PCM) to model the absorption
spectrum in solution following state-specific nonequilibrium approach.
Most EOM methods can be combined with explicit solvent treatments using
classical (QM/MM) and polarizable (QM/EFP) embedding.
- •

**Electronic spectra beyond UV-Vis

****Q-Chem** affords calculations of other types of electronic spectra, including
electronic circular dichroism, optical rotations, and two-photon transitions. Extensions to core-level spectra are
also available.
- •

**Visualization

**It is possible to visualize the excited states either by
attachment/detachment density analysis (available for CIS, RPA, TDDFT,
ADC, EOM-CC) or by plotting the transition density (see *$plots*
descriptions in Chapters [3](../ch03_inputs/chap_inputs.md) and [10](../ch10_properties/chap_properties.md)).
Transition densities can be calculated for CIS, EOM-CCSD, and ADC methods.
The theoretical basis of the attachment/detachment density analysis
is discussed in Section [7.13.2](sect_AttachDetach.md) of this Chapter (more
details are given in Section [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md)).
In addition Dyson orbitals can be calculated and plotted for ionization
from the ground and electronically excited states or detachment from
electron-attached states for CCSD and EOM-CCSD wave functions. For the
RAS-SF method (Section [7.11](topic_rasi.md)), one can plot the natural orbitals
of a computed electronic state.
- •

**Excited-state optimization**

Optimization of the geometry of stationary points on excited state
potential energy surfaces is valuable for understanding the geometric
relaxation that occurs between the ground and excited state. Analytic
first derivatives are available for UCIS, RCIS, TDDFT, and EOM-CCSD.
Excited state optimizations may also be performed using finite difference
methods, however, these can be very time-consuming to perform.
- •

**Optimization of the crossings between potential energy surfaces**

Seams between potential energy surfaces can be located and optimized by using analytic
gradients within EOM-CCSD, CIS, and TD-DFT formalisms.
- •

**Properties

**Properties such as dipole moments, spatial extent
of electron densities and $\langle\hat{S}^{2}\rangle$ values can be computed for
ADC, EOM-CCSD, EOM-MP2, EOM-OD, RAS-SF and CIS wave functions.
Static polarizabilities are available for CCSD, EOM-EE-CCSD, and EOM-SF-CCSD methods.
- •

**Transition properties and state interactions

**Transition dipole moments and oscillator strengths can be computed with
practically all excited-state methods. Matrix elements and
cross-sections for two-photon absorption are available for EOM-EE-CCSD
and ADC methods. Spin-orbit couplings and matrix elements of angular momentum operators
can be computed for EOM-CCSD, RAS-SF, CIS,
and TDDFT wave functions. Dyson orbitals are available for EOM-CC wave
functions. Transition properties can be computed between the reference
and target states (*e.g.*, HF-CIS) or between different target states (*e.g.*, CIS-CIS or CCSD-EOM-CCSD).
- •

**Excited-state vibrational analysis**

Given an optimized excited state geometry, **Q-Chem** can calculate the
force constants at the stationary point to predict excited state
vibrational frequencies. Stationary points can also be characterized as
minima, transition structures or $n$th-order saddle points.
Analytic excited state vibrational analysis can only be performed using
the UCIS, RCIS, and TDDFT methods, for which efficient analytical second
derivatives are available. EOM-CCSD frequencies are also available using
analytic first derivatives and second derivatives obtained from finite
difference methods. EOM-OD frequencies are only available through finite difference calculations.

**Note: 

EOM-CC and most of the CI codes are part of CCMAN and CCMAN2. CCMAN is
a legacy code which is being phased out. All new developments and
performance-enhancing features are implemented in CCMAN2.
**

### `METHOD`

> **Specifies the level of theory.**
>
> * **Type**: `STRING`
> * **Default**: `None`
> * **Options**:
>     * `CIS`: Section 7.2.2
>     * `CIS(D)`: Section 7.8.2
>     * `RI-CIS(D)`: Section 7.8.3
>     * `SOS-CIS(D)`: Section 7.8.4
>     * `SOS-CIS(D0)`: Section 7.8.5
>     * `CISD`: Section 7.9.3
>     * `CISDT`: Section 7.9.3
>     * `EOM-OD`: Section 7.9.3
>     * `EOM-CC2`: Section 7.9.4
>     * `EOM-CCSD`: Section 7.9.3
>     * `EOM-CCSDT`: Section 7.9.23
>     * `EOM-MP2`: Section 7.9.5.1
>     * `EOM-MP2T`: Section 7.9.5.1
>     * `EOM-CCSD-S(D)`: Section 7.9.5.2
>     * `EOM-MP2-S(D)`: Section 7.9.5.2
>     * `EOM-CCSD(dT)`: Section 7.9.27
>     * `EOM-CCSD(fT)`: Section 7.9.27
>     * `EOM-CC(2,3)`: Section 7.9.24
>     * `ADC(0)`: Section 7.10
>     * `ADC(1)`: Section 7.10
>     * `ADC(2)`: Section 7.10
>     * `ADC(2)-X`: Section 7.10
>     * `ADC(3)`: Section 7.10
>     * `SOS-ADC(2)`: Section 7.10
>     * `SOS-ADC(2)-X`: Section 7.10
>     * `CVS-ADC(1)`: Section 7.10
>     * `CVS-ADC(2)`: Section 7.10
>     * `CVS-ADC(2)-X`: Section 7.10
>     * `CVS-ADC(3)`: Section 7.10
>     * `RAS-CI`: Section 7.11
>     * `RAS-CI-2`: Section 7.11
> * **Recommendation**: Consult the literature for guidance.
