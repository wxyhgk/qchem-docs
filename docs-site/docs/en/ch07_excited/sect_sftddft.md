---
title: "7.3.4 Spin-Flip TDDFT"
---

## 7.3.4 Spin-Flip TDDFT

(July 4, 2026)

The spin-flip approach provides
a way to describe certain types of difficult multi-configurational states
within a single-reference formalism.[[726]](../bib_references/bib.md#bib757)

SF is particularly suitable for states that can be described as two electrons in two orbitals [(2e,2o)]
or (3e,3o). The idea is to describe such target states as spin-flipping excitations
(*e.g.*, $\alpha\rightarrow\beta$) from a high-spin reference determinant (triplet or
quartet). SF treatment can be combined with different correlation treatments (*e.g.*,
EOM-CC, ADC, CI, RAS-CI)[[205]](../bib_references/bib.md#bib207)
 as well as with DFT.[[1239]](../bib_references/bib.md#bib1294)

SF-TDDFT can describe the ground state as well as a few low-lying excited states.
It can be used to describe diradicals, triradicals, single-molecule magnets, systems with small HOMO-LUMO gaps,
and, in some cases, bond-breaking and conical intersections.[[205]](../bib_references/bib.md#bib207)

SF-DFT calculations are deployed by choosing an appropriate multiplicity of the
reference state and setting SPIN_FLIP to 1 (regular SF-TDDFT) or 2
(MRSF-TDDFT).
SF-DFT is only
used within Tamm-Dancoff approximation (RPA must be set to FALSE).

The original SF-DFT, formulated using collinear kernel,
requires the functionals with substantial fraction of Hartree–Fock exchange. Best results are obtained
using functionals with $\approx 50$% Hartree–Fock exchange,[[1239]](../bib_references/bib.md#bib1294)

behavior that was explained on theoretical grounds.[[603]](../bib_references/bib.md#bib626)

Becke’s half-and-half functional BH&HLYP has become something of a standard
approach when using standard SF-TDDFT.

A SF-TDDFT method with a non-collinear exchange-correlation potential, originally developed by Ziegler and
co-workers,[[1424]](../bib_references/bib.md#bib1486)

has also been implemented.[[114]](../bib_references/bib.md#bib101)

This non-collinear version sometimes improves upon
collinear SF-TDDFT for excitation energies but contains a factor of spin density
($\rho_{\alpha}-\rho_{\beta}$) in the denominator that sometimes causes stability problems.

The SF-DFT states may suffer from spin-contamination. This problem can be addressed
by using a spin-adapted version of SF-TDDFT (Section [7.2.3.3](Ch7.S2.SS3.md#safs-sftddft)),[[1549]](../bib_references/bib.md#bib1615)

or by using mixed-reference SF-TDDFT formulation described below.

Calculations of permanent and transition dipole moments
are available for all
SF-TDDFT variants.
SOCs and wave-function analysis (NTOs and exciton descriptors)
are available for
for standard collinear and non-collinear formulations of SF-TDDFT and for
MR-SFTDDFT.
Analytic gradients and NACs are available for non-spin-adapted collinear and non-collinear formulations of SF-TDDFT.

The following examples illustrate SF-DFT capabilities available in **Q-Chem**:
[7.3.4.2](#ex:MRSFDFT), [7.2.3.3](Ch7.S2.SS3.md#safs-sftddft),
[7.3.10.1](Ch7.S3.SS10.md#ex:dftcis-soc), [7.3.4.2](#ex:MRSFDFT),
[9.8.4](../ch09_opt/sfdft_MECP1.md), and [7.3.4.2](#ex:MRSFDFT).
Other related methods include
SF-XCIS (Section [7.2.3.2](Ch7.S2.SS3.md#topic:sf)), spin-adapted SF-CIS (Section [7.2.3.3](Ch7.S2.SS3.md#safs-sftddft)),
EOM-SF-CC (Section [7.9.6](sec_EOMSF.md)), SF-ADC (Section [7.10.8](sect_SF-ADC.md)),
and SF-RASCI (Section [7.11](topic_rasi.md)).

## 7.3.4.1 Mixed-reference SF-TDDFT

In MRSF-TDDFT,[[781]](../bib_references/bib.md#bib824)

the reference state is constructed as an equal mixture of two Kohn–Sham determinants
corresponding to the $M_{S}=+1$ and $M_{S}=-1$ components of the triplet state.
The resulting mixed-reference reduced density matrix (RDM) defined as

<a id="Ch7.E27"></a>

$$
\rho_{0}^{\rm MR}=\frac{1}{2}(\rho_{0}^{M_{S}=+1}+\rho_{0}^{M_{S}=-1}) \tag{7.27}
$$

is non-idempotent but the idempotency is restored through a complex transformation of the singly occupied
spin-orbitals.[[781]](../bib_references/bib.md#bib824)

By coupling the $\alpha\rightarrow\beta$ spin-flip excitations from the $M_{S}=+1$ component with the $\beta\rightarrow\alpha$ excitations from
the $M_{S}=-1$ component, MRSF-SFTDDFT recovers most of the determinants missing in conventional SF-TDDFT
and by doing so restores spin-completeness.

The current implementation

 of MRSF-TDDFT is available for a ROHF reference (UNRESTRICTED = FALSE)
and can describe both singlet and triplet states. It also affords calculations of transition
properties including matrix elements of the dipole and angular momentum operators, SOCs and wave-function analysis.
MRSF-TDDFT employs a collinear exchange-correlation kernel; hence, hybrid functionals
are recommended, particularly those with a larger fraction of Hartree–Fock exchange.

The orbital Hessian matrix is defined as[[793]](../bib_references/bib.md#bib828)

<a id="Ch7.E28"></a>

$$
A_{pq,rs}^{(k)}=A_{pq,rs}^{(k)(0)}+A_{pq,rs}^{{}^{\prime}(k)} \tag{7.28}
$$

where $k\in\{\text{S},\text{T}\}$ refers to a singlet or triplet state and

<a id="Ch7.E29"></a>

$$
A_{pq,rs}^{(k)(0)}=U_{pq}^{k}\{\delta_{pr}F_{qs}^{\beta}-\delta_{qs}F_{pr}^{\alpha}-c_{H}(pr|sq)\}U_{rs}^{(k)}. \tag{7.29}
$$

The term $A_{pq,rs}^{{}^{\prime}(k)}$ takes care of the coupling between the determinants generated from the two triplet components and is given by

<a id="A3.S8.EGx40"></a>

$$
\displaystyle\begin{aligned} \displaystyle A_{pq,rs}^{{}^{\prime}(k)}&\displaystyle=H_{p\underline{q},r\underline{s}}^{(k){\rm intra}}(U_{pq}^{\text{CO1}}-U_{pq}^{\text{CO2}})(U_{rs}^{\text{CO1}}-U_{rs}^{\text{CO2}})\\
&\displaystyle\qquad+H_{\underline{p}q,\underline{r}s}^{(k){\rm intra}}(U_{pq}^{\text{O1V}}-U_{pq}^{\text{O2V}})(U_{rs}^{\text{O1V}}-U_{rs}^{\text{O2V}})\\
&\displaystyle\qquad+H_{pq,rs}^{(k){\rm inter}}(U_{pq}^{\text{CO1}}U_{rs}^{\text{O2V}}+U_{pq}^{\text{CO2}}U_{rs}^{\text{O1V}}+U_{pq}^{O1V}U_{rs}^{\text{CO2}}+U_{pq}^{\text{O2V}}U_{rs}^{\text{CO1}})\;.\end{aligned} \tag{7.30}
$$

Here, $U_{pq}$ are dimensional transformation matrices and

<a id="Ch7.E31"></a>

$$
\displaystyle H_{pq,rs}^{(k)\text{intra}} \tag{7.31a}
$$

with

<a id="Ch7.E32"></a>

$$
\text{sgn}(k)=\begin{cases}+1,&\text{if}~{}k=\text{S}\\
-1,&\text{if}~{}k=\text{T}\\
\end{cases} \tag{7.32}
$$

and

<a id="Ch7.E33"></a>

$$
\underline{p}=\begin{cases}\text{O2},&\text{if}~{}p=\text{O1}\\
\text{O1},&\text{if}~{}p=\text{O2}\\
\end{cases} \tag{7.33}
$$

The dimensional transformation matrices ensure that the MRSF excitation subspace matches the dimensionality of the SF-TDDFT space for both
$k=\text{S}$ and $k=\text{T}$. Owing to this structure in which the singlet and triplet spaces are completely decoupled from each other, MRSF-TDDFT, in contrast to the original
SF-TDDFT, solves separate eigenvalue problems for singlet and triplet manifolds.

By default, the calculation prints $\langle\hat{S}^{2}\rangle$ values for each state, TDDFT amplitudes,
and transition dipole moments wrt the lowest SF state in each spin manifold.

Enabling keyword STS_MOM=TRUE prints additional
information, including the Cartesian components of the permanent
dipole moments (in a.u.) of each computed state, as well as the Cartesian components of the transition dipole moments
(in a.u.), and the corresponding oscillator strengths between all computed SF states. To compute SOC, use
CALC_SOC=2.

Example [7.3.4.2](#ex:MRSFDFT) illustrates MR-SF-TDDFT calculation for butadiene inlcuing state and transition properties and exciton analysis.

## 7.3.4.2 Examples

???+ example "Example 7.8: SF-TDDFT SP calculation of the 6 lowest states of the TMM diradical using
recommended 50-50 functional."
    ```qchem
    $molecule
       0 3
       C
       C  1  CC1
       C  1  CC2   2  A2
       C  1  CC2   2  A2     3  180.0
       H  2  C2H   1  C2CH   3    0.0
       H  2  C2H   1  C2CH   4    0.0
       H  3  C3Hu  1  C3CHu  2    0.0
       H  3  C3Hd  1  C3CHd  4    0.0
       H  4  C3Hu  1  C3CHu  2    0.0
       H  4  C3Hd  1  C3CHd  3    0.0
    
       CC1    = 1.35
       CC2    = 1.47
       C2H    = 1.083
       C3Hu   = 1.08
       C3Hd   = 1.08
       C2CH   = 121.2
       C3CHu  = 120.3
       C3CHd  = 121.3
       A2    = 121.0
    $end
    
    $rem
       EXCHANGE          gen
       BASIS             6-31G*
       SCF_GUESS         core
       SCF_CONVERGENCE   10
       MAX_SCF_CYCLES    100
       SPIN_FLIP         1
       CIS_N_ROOTS       6
       CIS_CONVERGENCE   10
       MAX_CIS_CYCLES    100
    $end
    
    $xc_functional
       X  HF    0.50
       X  S     0.08
       X  B     0.42
       C  VWN   0.19
       C  LYP   0.81
    $end
    ```

???+ example "Example 7.9: SF-TDDFT with non-collinear exchange-correlation functional for low-lying states
of $\rm CH_{2}$ ."
    ```qchem
    $comment
      Non-collinear SF-DFT calculation for CH2 at 3B1 state geometry from
      EOM-CCSD(fT) calculation
    $end
    
    $molecule
       0 3
       C
       H  1 rCH
       H  1 rCH  2 HCH
    
       rCH = 1.0775
       HCH = 133.29
    $end
    
    $rem
       EXCHANGE             PBE0
       BASIS                cc-pVTZ
       SPIN_FLIP            1
       WANG_ZIEGLER_KERNEL  TRUE
       SCF_CONVERGENCE      10
       CIS_N_ROOTS          6
       CIS_CONVERGENCE      10
    $end
    ```

???+ example "Example 7.10: SF-TDDFT calculation with collinear B5050LYP for $p$ -benzyne with wave-function analysis
(natural orbitals and NTOs) performed by libwfa ."
    ```qchem
    $comment
    Para-benzyne diradical
    Equilibrium singlet state geom from:
    J. Chem. Phys. 136, 204103 (2012)
    Enu = 187.2138176166 hartree
    $end
    
    $molecule
       0 3
       H   2.145810  -1.225292   0.000000
       C   1.201382  -0.709285   0.000000
       C   1.201382   0.709285   0.000000
       H   2.145810   1.225292   0.000000
       C   0.000000   1.335664   0.000000
       C  -1.201382   0.709285   0.000000
       H  -2.145810   1.225291   0.000000
       C  -1.201382  -0.709285   0.000000
       H  -2.145810  -1.225291   0.000000
       C   0.000000  -1.335664   0.000000
    $end
    
    $rem
       METHOD          = b5050lyp
       BASIS           = 6-31G*
       CIS_N_ROOTS     = 4
       SPIN_FLIP       = true
       NEW_DFT         = true
       STATE_ANALYSIS  = true
       WFA_REF_STATE   = 1
       MOLDEN_FORMAT   = true
       NTO_PAIRS       = 4
    $end
    ```

???+ example "Example 7.11: Mixed-reference SF-TDDFT/BHHLYP calculation of butadiene including exciton analysis."
    ```qchem
    $comment
    - Singlet states of butadiene using MRSF-TDDFT
    - State-to-state transition dipole moments, and oscillator strengths
    - Density matrix based analysis of the calculated MRSF states
    $end
    
    $molecule
    0 3
    C   -0.410990219   -1.798958603   0.000000000
    C   -0.559475119   -0.470573512   0.000000000
    C    0.410990219    1.798958603   0.000000000
    C    0.559475119    0.470573512   0.000000000
    H   -1.263114858   -2.463113554   0.000000000
    H    0.571968115   -2.252448386   0.000000000
    H    1.263114858    2.463113554   0.000000000
    H   -1.554995711   -0.040726039   0.000000000
    H   -0.571968115    2.252448386   0.000000000
    H    1.554995711    0.040726039   0.000000000
    $end
    
    $rem
    jobtype            SP
    unrestricted       FALSE
    basis              6-31G*
    exchange           bhhlyp
    correlation        none
    scf_guess          core
    SCF_CONVERGENCE    10
    SCF_ALGORITHM      DIIS
    MAX_SCF_CYCLES     100
    PRINT_ORBITALS     false   ! do not print orbitals
    SPIN_FLIP          2       ! keyword to perform MRSF-TDDFT calculation
    CIS_N_ROOTS        4       ! 4 MRSF states requested
    CIS_SINGLETS       TRUE    ! asking for singlet states
    CIS_TRIPLETS       FALSE
    CIS_CONVERGENCE    8
    MAX_CIS_CYCLES     100
    STS_MOM            TRUE    ! calculate state-to-state transition moments
    STATE_ANALYSIS     TRUE    ! density matrix based analysis of MRSF states
    NTO_PAIRS          2       ! write 2 NTO pairs per excited states
    $end
    ```
