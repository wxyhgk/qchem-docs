---
title: "7.9.10 EOM-CC Calculations of Metastable States"
---

## 7.9.10 EOM-CC Calculations of Metastable States

(July 4, 2026)

While conventional coupled-cluster and equation-of-motion methods allow one to
tackle electronic structure ranging from well-behaved closed-shell molecules to
various open-shell and electronically excited species,[[729]](../bib_references/bib.md#bib760)

meta-stable electronic states, called resonances, present a difficult case
for theory. By using complex scaling, complex basis functions (CBFs),
and complex absorbing potential (CAP)
techniques, **Q-Chem** extends these powerful methods to describe auto-ionizing
states, such as transient anions, highly excited electronic states, and
core-ionized species[[156]](../bib_references/bib.md#bib149)

(CBF extensions of CC and EOM-CC calculations
are described in Sections [4.9.5](../ch04_scf/sec_cbfscf.md) and [8.7](../ch08_basis/sect_zbas.md)). In addition,
users can employ stabilization techniques using charged sphere and scaled
atomic charges options.[[741]](../bib_references/bib.md#bib774)
 These methods are only available within
CCMAN2. The complex CC/EOM code is engaged by COMPLEX_CCMAN;
the specific parameters should be specified in the *$complex_ccman* section.

COMPLEX_CCMAN

### `COMPLEX_CCMAN`

> **Requests complex-scaled or CAP-augmented CC/EOM calculations.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Engage complex CC/EOM code.
> * **Recommendation**: Not available in CCMAN. Need to specify CAP strength or complex-scaling parameter in $complex_ccman section.

The *$complex_ccman* section is used to specify the details of the
complex-scaled/CAP calculations, as illustrated below. If user specifies
CS_THETA, complex scaling calculation is performed.

> ```qchem
> $complex_ccman
>    CS_THETA  10   Complex-scaling parameter theta=0.01, r->r exp(-i*theta)
>    CS_ALPHA  10   Real part of the scaling parameter alpha=0.01,
> !                 r->alpha r exp(-itheta)
> $end
> ```

Alternatively, for CAP calculations, the CAP parameters need to be specified.

> ```qchem
> $complex_ccman
>    CAP_ETA  1000  CAP strength in 10-5 a.u. (0.01)
>    CAP_X    2760  CAP onset along X in 10^-3 bohr (2.76 bohr)
>    CAP_Y    2760  CAP onset along Y in 10^-3 bohr (2.76 bohr)
>    CAP_Z    4880  CAP onset along Z in 10^-3 bohr (4.88 bohr)
>    CAP_TYPE 1     Use cuboid cap (CAP_TYPE=0/2 will use spherical/Voronoi CAP)
> $end
> ```

One can also add real absorbing potential by using CAP_RE_ETA;
it follows the same format as CAP_ETA. For example,
this setup would add purely real absorbing potential with
$\eta$=0.01:

> ```qchem
> $complex_ccman
>    CAP_ETA     0000  CAP strength in 10-5 a.u. (0.00)
>    CAP_RE_ETA  1000  real CAP strength in 10-5 a.u. (0.01)
>    CAP_X    2760  CAP onset along X in 10^-3 bohr (2.76 bohr)
>    CAP_Y    2760  CAP onset along Y in 10^-3 bohr (2.76 bohr)
>    CAP_Z    4880  CAP onset along Z in 10^-3 bohr (4.88 bohr)
>    CAP_TYPE 1     Use cuboid cap (CAP_TYPE=0/2 will use spherical/Voronoi CAP)
> $end
> ```

The CAP_TYPE field specifies the type of the CAP. The current
options are: spherical CAP (CAP_TYPE = 0), cuboid CAP
(CAP_TYPE = 1), and smooth Voronoi[[1283]](../bib_references/bib.md#bib1341)
 CAP
(CAP_TYPE = 2). In the calculations with a Voronoi CAP, the onset is
specified by the CAP_X variable.

CS_THETA is specified in radian$\times$ 10${}^{-3}$.
CS_ALPHA, CAP_X/Y/Z are specified in a.u. $\times$
10${}^{-3}$, *i.e.*, CS_THETA = 10 means $\theta=0.01$; CAP_ETA
is specified in units of $10^{-5}$ $E_{h}$. The CAP is calculated by numerical
integration and the default grid is ($N_{r}=99,N_{\Omega}=590$).
For testing the accuracy of
numerical integration, the numerical overlap matrix is calculated and compared
to the analytical one. If the performance of the default grid is poor, the grid
type can be changed using the keyword XC_GRID (see
Section [5.5](../ch05_dft/sect_quadrature.md) for further details). When CAP calculations are
performed, CC_EOM_PROP = 1 by default; this is necessary for
calculating first-order perturbative correction.

EOM-CC with CBFs (see Section [4.9.5](../ch04_scf/sec_cbfscf.md)) is deployed
by setting COMPLEX_CCMAN = TRUE and
COMPLEX_EXPONENTS = TRUE. As with mean-field calculations
the complex basis must be specified as described in Section [8.7](../ch08_basis/sect_zbas.md).

Advanced users may find the following options useful. Several ways of
conducing complex calculations are possible, *i.e.*, complex scaling/CAPs can be
either engaged at all levels (HF, CCSD, EOM), or not. When applied at post
Hartree-Fock level, CAP can either be added to all blocks of the Fock matrix or
restricted to the virtual-virtual block only. The latter approach, known as
projected CAP,[[1197]](../bib_references/bib.md#bib1251)
 improves the stability of the calculation
results with respect to CAP onset by reducing a CAP-induced perturbation on the
target states through the occupied orbital space.

This type of CAP projection is currently implemented only for EE/EA calculations and is
invoked by setting PROJ_CAP keyword in the *$complex_ccman* section as
follows. PROJ_CAP = 1 deploys CAP/EOM-CCSD with projected CAP added
at the CCSD and EOM steps and PROJ_CAP = 2 deploys CAP/EOM-CCSD/MP2/MP2T
with projected CAP added at the EOM step. The latter implies that
$T$-amplitudes (Sec. [7.9.3](sec_EOMEE.md)) are obtained from a real-valued
calculation (for zero CAP strength) and can be reused to generate complex
eigenvalue trajectories by specifying ETA_STEP and NSTEPS
parameters in *$complex_ccman*.

PROJ_CAP = 3 deploys another form of CAP projection [[1284]](../bib_references/bib.md#bib1340)
 in which the CAP Hamiltonian
is projected onto the subspace spanned by a set of pre-computed EOM eigenvectors. By default,
the excited-state eigenvectors are obtained from a single real-valued calculation, and the CAP matrix
represented in the state basis is printed in the output for each irreducible representation.
This functionality is available for all EOM-CC models for which transition properties
between EOM target states are available. To generate eigenvalue trajectories, CAP_ETA
should be set to a non-zero CAP strength, and subsequent points are specified using
the ETA_STEP and NSTEPS parameters in *$complex_ccman*. Trajectories
are written to a separate output file for each irreducible representation. Additionally, first-order
perturbative corrections can be obtained by setting PROJ_PROP = 1. Note that
when PROJ_PROP = 1, the initial set of real eigenvectors are obtained using the
complex valued code at zero CAP strength. As such, first-order perturbative corrections
are only available for complex EOM-CC models. The complete set of one-particle state and transition OPDMs between each pair of states (which is all that is required for CAP projection) will be exported to checkpoint file for further analysis when GUI = 2 and PROJ_CAP = 3.

By default, if COMPLEX_CCMAN is specified, the EOM calculations are
conducted using complex code. Other parameters are set up as follows:

> ```qchem
> $complex_ccman
>   CS_HF   = true
>   CS_CCSD = true
> $end
> ```

Alternatively, the user can disable complex HF. These options are experimental
and should only be used by advanced users. For CBF-EOM-CC, only CS_HF =
TRUE and CS_CCSD = TRUE is implemented.

Non-iterative triples corrections are available for all complex scaled and
CAP-augmented CC/EOM-CC models and requested in analogy to regular
CC/EOM-CC (see Section [7.9.27](sec_SD3.md) for details).

To take account of the impact of the environment on electronic resonances CAP-EOM-CCSD and CBF-EOM-CCSD can be combined with projection-based embedding,[[1043]](../bib_references/bib.md#bib1088)

as described in Sections [7.9.3.1](sec_EOMEE.md#subsec:eomcc-pbe) and [11.6](../ch11_env/sect_den_emb.md).

Molecular properties and transition moments can be requested for complex scaled or
CAP-augmented CC/EOM-CC calculations in analogy to regular CC/EOM-CC (see Section [7.9.21](sec_EOMGRAD.md) for details). Natural orbitals and
natural transition orbitals can be computed and the exciton wave-functions can
be analyzed, similarly to real-valued EOM-CCSD (same keywords are used to
invoke the analysis). Analytic gradients are available for complex CC/EOM-CC only for cuboid CAPs (CAP_TYPE = 1) introduced at the HF level
(CS_HF = TRUE), as described in Ref. [[108]](../bib_references/bib.md#bib95)
. The
frozen-core approximation is disabled for CAP-CC/EOM-CC gradient
calculations. Geometry optimization can be requested in the same way as in
regular CC/EOM-CC (see Section [7.9.21](sec_EOMGRAD.md) for details).

## 7.9.10.1 Complex-valued RI-EOM-CCSD

To reduce the memory requirements, the RI-approximation can be invoked to decompose
the electron-repulsion integrals. The code has the same structure as for real-valued
RI-EOM-CCSD[[366]](../bib_references/bib.md#bib762)
 but uses a complex-valued RI
decomposition.[[1397]](../bib_references/bib.md#bib592)
 The RI-approximation is available for CCSD
and EOM-IP/EA/EE/SF-CCSD in combination with complex-scaling, complex basis functions
and complex absorbing potentials.[[185]](../bib_references/bib.md#bib180)
 It can be invoked by setting AUX_BASIS to
your favorite auxiliary basis set (*e.g.* RIMP2-aug-cc-pVTZ). For calculations
with complex basis functions, COMPLEX_AUX_BASIS needs to specified as well,
which is usually the same as AUX_BASIS. When using user-defined auxiliary
basis sets, AUX_BASIS is specified in *$aux_basis* while
COMPLEX_AUX_BASIS is specified in *$aux_zbasis*. Complex-valued RI integrals
are currently only available for energies and unrelaxed one-electron properties. It
is also possible to use the RI-approximation for the determination of partial Auger
decay widths by decomposing the CCSD energy or by the ACP method (see sections
[7.9.11](sec_Auger.md) and [7.9.12](sec_AugerComplexVariable.md)).

## 7.9.10.2 Complex-valued RI-EOM-CC2

The RI-EOM-CC2 method is also available for the description of metastable states through electron attachment (EA) in combination with complex absorbing potentials (CAPs) and complex basis functions (CBFs). Two implementations are available in the CCMAN2 and LIBGMBPT modules, which differ in their algorithmic efficiency and supported features.

The CCMAN2 implementation follows a code structure analogous to that of RI-EOM-CCSD, and can be invoked by specifying method = CCMAN2 in the input. However, this implementation does not employ the most efficient algorithm, as the doubles amplitudes are not evaluated *on-the-fly*. Consequently, the memory requirements remain at $\mathcal{O}(N^{4})$, same as EOM-CCSD.

The LIBGMBPT implementation is based on a more efficient algorithm, reducing the memory requirements to $\mathcal{O}(N^{3})$, making it the preferred choice for larger systems. Spin-scaled variants of EA-CC2, including spin-component-scaling (SCS) and scaled opposite-spin (SOS), are also available exclusively in this module and can be invoked in the same manner as in MP2 (see section [6.6.5](../ch06_correlation/topic_sbmp2.md)).

For this implementation, the mixed Davidson/DIIS solver is not employed as in the real-valued EOM-CC2 (see section [7.9.4](sec_eomcc2.md)). Instead, a modified Davidson algorithm is introduced for the solution of the CC2 pseudoeigenvalue equations for electron attachment.

Several input features are worth noting. The user can target attachment to a specific state by specifying the 

EOM_USER_GUESS keyword along with the *$eom_user_guess* section, in the same manner as in EOM-CC (see section [7.9.16](subsec_EOM-CC-diag.md)). The orbital indexing in LIBGMBPT starts from the first occupied orbital, in contrast to the first unoccupied orbital as in CCMAN2, and the frozen core orbitals must be subtracted from the total orbital count. In addition, sequential calculation of multiple roots with a user-defined guess can be requested by setting *$eom_user_guess* = 2.

Finally, point group symmetry is not yet supported in this implementation. Further details on the implementation and its performance on temporary anions can be found in Ref. [[1382]](../bib_references/bib.md#bib1443)
.

The LIBGMBPT implementation can be invoked by setting CCMAN2 = –1, the default currently is CCMAN2.
