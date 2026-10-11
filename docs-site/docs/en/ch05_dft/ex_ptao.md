---
title: "5.12.3 Thermally-Assisted-Occupation DFT (TAO-DFT)"
---

## 5.12.3 Thermally-Assisted-Occupation DFT (TAO-DFT)

(July 4, 2026)

Aiming to study the ground-state properties of large, strongly correlated
systems with minimum computational complexity, Prof. Jeng-Da Chai recently
developed thermally-assisted-occupation density functional theory
(TAO-DFT).[[227]](../bib_references/bib.md#bib222)
 Unlike conventional multi-reference methods, the
computational complexity of TAO-DFT increases very insignificantly with the
size of the active space (*i.e.*, an active space restriction is not needed for
TAO-DFT calculations), and TAO-DFT appears to be very promising for the study
of large poly-radical systems. TAO-DFT is a DFT scheme with fractional orbital
occupations produced by the Fermi-Dirac distribution, controlled by a
fictitious temperature $\theta$, and existing XC functionals (*e.g.*, LDA[[227]](../bib_references/bib.md#bib222)
,
GGAs[[228]](../bib_references/bib.md#bib228)
, global hybrid GGAs[[229]](../bib_references/bib.md#bib229)
 or range-separated hybrid GGAs [[229]](../bib_references/bib.md#bib229)
) can be used in TAO-DFT.
The computational cost of the method is similar to that of Kohn-Sham DFT for single-point energy calculations and
analytical nuclear gradients, and reduces to the cost of Kohn-Sham DFT in the absence
of strong static correlation effects.

There are several *$rem* variables that are used for TAO-DFT.

TAO_DFT

### `TAO_DFT`

> **Controls whether to use TAO-DFT.**
>
> * **Type**: `Boolean`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not use TAO-DFT
>     * TRUE
>     * Use TAO-DFT
> * **Recommendation**: NONE

TAO_DFT_THETA

### `TAO_DFT_THETA`

> **The parameter $m$ (the mantissa) for the value of the fictitious temperature $\theta=m\times 10^{-n}\ E_{h}$ in TAO-DFT.**
>
> * **Type**: `INTEGER`
> * **Default**: `7`
> * **Options**:
>     * $m$
>     * Customize the mantissa for the fictitious temperature.
> * **Recommendation**: NONE

TAO_DFT_THETA_NDP

### `TAO_DFT_THETA_NDP`

> **The parameter $n$ (the exponent) for the value of the fictitious temperature $\theta=m\times 10^{-n}\ E_{h}$ in TAO-DFT.**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * $n$
>     * Customize the exponential power for the fictitious temperature.
> * **Recommendation**: NONE

PTAO

### `PTAO`

> **Controls whether to perform the pTAO/TDA method.**
>
> * **Type**: `Boolean`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not perform the pTAO/TDA method
>     * TRUE
>     * Perform the pTAO/TDA method
> * **Recommendation**: NONE

Note that setting TAO_DFT_THETA = 0 recovers ordinary
Kohn-Sham DFT.[[227]](../bib_references/bib.md#bib222)
 In addition to the XC functional, a functional
$E_{\theta}[\rho]$ is needed in TAO-DFT. Currently available in **Q-Chem** are
an LDA version[[227]](../bib_references/bib.md#bib222)
 (the ETheta_LDA functional) as well as a
version based on the gradient expansion approximation[[228]](../bib_references/bib.md#bib228)
 (GEA)
(the ETheta_GEA functional), and the latter may be substituted for the former in
the sample jobs below. Furthermore, a functional $E_{x,\theta}[\rho]$ is also
needed in TAO-DFT for global hybrid (GH) GGAs. Currently available in Q-CHEM is
an LDA version (the EThetaX_LDA functional) [[229]](../bib_references/bib.md#bib229)
.
Moreover, two functionals $E^{\text{SR}}_{x,\theta}[\rho]$ and $E^{\text{LR}}_{x,\theta}[\rho]$ are needed in TAO-DFT for range-separated hybrid (RSH) GGAs, and their LDA versions (the SR_ETHETAX_LDA and LR_ETHETAX_LDA functionals) are now available in Q-CHEM [[815]](../bib_references/bib.md#bib858)
. Note that both $E^{\text{SR}}_{x,\theta}[\rho]$ and $E^{\text{LR}}_{x,\theta}[\rho]$ depend on the range-separation parameter $\omega$, and $E^{\text{SR}}_{x,\theta}[\rho]$ reduces to $E_{x,\theta}[\rho]$ when $\omega=0$. Therefore, the SR_ETHETAX_LDA functional with $\omega=0$ is another LDA version of $E_{x,\theta}[\rho]$, denoted as ETHETAX19_LDA.

To improve the performance of TAO-DFT functionals, the B97-type functionals with the semi-empirical dispersion correction based on the D4 model are optimized in TAO-DFT using the system-independent fictitious temperatures, resulting in TAO-B97-D4, TAO-B97X-D4 and TAO-$\omega$B97X-D4 [[815]](../bib_references/bib.md#bib858)
. With the constraint $\theta=0$, the B97-type RSH functional is also optimized in KS-DFT, resulting in KS-$\omega$B97X-D4 [[815]](../bib_references/bib.md#bib858)
 (see Example [5.6.3](ex_ks-wb97xd4.md) for the usage).

Spurious excitations may arise in the time-dependent extension of TAO-DFT with the adiabatic xc kernel (TDTAO-DFT) when $\theta>0$ [[1523]](../bib_references/bib.md#bib1587)
, similar to time-dependent density-matrix functional theory (TDDMFT) using the adiabatic approximation [[442]](../bib_references/bib.md#bib453)
. To address this issue, a post-TAO/TDA method (pTAO/TDA) was proposed [[815]](../bib_references/bib.md#bib858)
. In the pTAO/TDA method, the energy of state X relative to the ground state (i.e., the excitation energy of state X) is given by Eq. (85) in Ref. [[815]](../bib_references/bib.md#bib858)
:

<a id="eq:excitationX"></a>
$$
\omega_{\text{pTAO/TDA}}[\text{X}]=(\omega[\text{X}]-\omega[\text{A}_{1}])+(E_{\text{A}_{1}}-E_{\text{GS}}). \tag{5.76}
$$

Here, $\omega[\text{X}]$ is the relative energy of X to the pTAO reference state, which is available in Q-CHEM through PTAO = TRUE (see Example 5.12.3). In addition, $E_{\text{GS}}$ and $E_{\text{A}_{1}}$ are the ground-state energy and the lowest excitation energy among different spin states of the system, respectively, which are obtained with TAO-DFT. Note that, $(\omega[\text{X}]-\omega[\text{A}_{1}])$ is adopted to suppress the effect of choice of reference state (e.g., the pTAO reference state).

???+ example "Example 5.30: TAO-LDA calculation on Be atom"
    ```qchem
    $molecule
       0 1
       Be
    $end
    
    $rem
       BASIS               6-31G*
       EXCHANGE            gen
       TAO_DFT             true
       TAO_DFT_THETA       7    ! default, theta=7 mhartree
       TAO_DFT_THETA_NDP   3    ! default
    $end
    
    $xc_functional
       X   S             1.0
       C   PW92          1.0
       X   ETheta_LDA    1.0
    $end
    ```

???+ example "Example 5.31: TAO-PBE, spin-restricted calculation on stretched N ${}_{2}$"
    ```qchem
    $molecule
       0 1
       N1
       N2 N1 4.5
    $end
    
    $rem
       BASIS               6-31G*
       EXCHANGE            gen
       TAO_DFT             true
       TAO_DFT_THETA       40  ! theta = 40 mhartree
       TAO_DFT_THETA_NDP   3
    $end
    
    $xc_functional
       X PBE         1.0
       C PBE         1.0
       X ETheta_LDA  1.0
    $end
    ```

???+ example "Example 5.32: TAO-PBE, spin-unrestricted calculation on stretched N ${}_{2}$"
    ```qchem
    $molecule
       0 1
       N1
       N2 N1 5.0
    $end
    
    $rem
       JOBTYPE             opt
       UNRESTRICTED        true
       BASIS               6-31G*
       EXCHANGE            gen
       TAO_DFT             true
       TAO_DFT_THETA       40  ! theta = 40 mhartrees
       TAO_DFT_THETA_NDP   3   ! can omit this line
       SCF_GUESS           gwh
       SCF_GUESS_MIX       3   ! mix in 30% LUMO in alpha to break symmetry
    $end
    
    $xc_functional
       X PBE         1.0
       C PBE         1.0
       X ETheta_LDA  1.0
    $end
    ```

???+ example "Example 5.33: TAO-PBE0 calculation on H ${}_{2}$ molecule"
    ```qchem
    $molecule
       0 1
       H1
       H2 H1 1.00
    $end
    
    $rem
       JOBTYPE             opt
       UNRESTRICTED        true
       BASIS               6-31G*
       EXCHANGE            gen
       TAO_DFT             true
       TAO_DFT_THETA       20  ! theta = 20 mhartrees
       TAO_DFT_THETA_NDP   3   ! can omit this line
       SCF_GUESS           gwh
       SCF_GUESS_MIX       3   ! mix in 30% LUMO in alpha to break symmetry
    $end
    
    $xc_functional
       X ETheta_LDA    1.00
       X EThetaX_LDA   0.25
       X HF            0.25
       X PBE           0.75
       C PBE           1.00
    $end
    ```

???+ example "Example 5.34: TAO-B3LYP calculation on H ${}_{2}$ molecule"
    ```qchem
    $molecule
       0 1
       H1
       H2 H1 1.00
    $end
    
    $rem
       JOBTYPE             opt
       UNRESTRICTED        true
       BASIS               6-31G*
       EXCHANGE            gen
       TAO_DFT             true
       TAO_DFT_THETA       174 ! theta = 17.4 mhartrees
       TAO_DFT_THETA_NDP   4
       SCF_GUESS           gwh
       SCF_GUESS_MIX       3   ! mix in 30% LUMO in alpha to break symmetry
    $end
    
    $xc_functional
       X ETheta_LDA    1.00
       X EThetaX_LDA   0.20
       X HF            0.20
       X Slater        0.08
       X Becke88       0.72
       C LYP           0.81
       C VWN1RPA       0.19
    $end
    ```

???+ example "Example 5.35: TAO-B97-D4 calculation on H ${}_{2}$ molecule"
    ```qchem
    $molecule
    0 1
    H 0.00 0.00 0.00
    H 1.00 0.00 0.00
    $end
    
    $rem
    JOBTYPE              = sp
    unrestricted         = FALSE
    scf_guess            = SAD
    scf_guess_mix        = 0
    scf_algorithm        = diis
    max_scf_cycles       = 300
    GEN_SCFMAN           = FALSE
    xc_grid              = 000075000302
    scf_convergence      = 8
    thresh               = 14
    BASIS                = 6-31G(d)
    TAO_DFT              = true
    TAO_DFT_THETA        = 959717
    TAO_DFT_THETA_NDP    = 8
    EXCHANGE             = gen
    symmetry             = false
    sym_ignore           = true
    basis_lin_dep_thresh = 8
    DFT_D                = D4
    DFT_D4_A1            = 50000000
    DFT_D4_A2            = 350000000
    DFT_D4_S6            = 100000000
    DFT_D4_S8            = 172371500
    DFT_D4_S9            = 100000000
    DFT_D4_S10           = 0
    $end
    
    $XC_functional
    X ETheta_LSDA         1.000000
    X TAO_B97             1.000000
    C TAO_B97             1.000000
    $end
    ```

???+ example "Example 5.36: TAO-B97X-D4 calculation on H ${}_{2}$ molecule"
    ```qchem
    $molecule
    0 1
    H 0.00 0.00 0.00
    H 1.00 0.00 0.00
    $end
    
    $rem
    JOBTYPE              = sp
    unrestricted         = FALSE
    scf_guess            = SAD
    scf_guess_mix        = 0
    scf_algorithm        = diis
    max_scf_cycles       = 300
    GEN_SCFMAN           = FALSE
    xc_grid              = 000075000302
    scf_convergence      = 8
    thresh               = 14
    BASIS                = 6-31G(d)
    TAO_DFT              = true
    TAO_DFT_THETA        = 240964
    TAO_DFT_THETA_NDP    = 7
    EXCHANGE             = gen
    symmetry             = false
    sym_ignore           = true
    basis_lin_dep_thresh = 8
    DFT_D                = D4
    DFT_D4_A1            = 50000000
    DFT_D4_A2            = 400000000
    DFT_D4_S6            = 100000000
    DFT_D4_S8            = 170811200
    DFT_D4_S9            = 100000000
    DFT_D4_S10           = 0
    $end
    
    $XC_functional
    X ETheta_LSDA         1.000000
    X ETHETAX_LSDA19      0.325932
    X HF                  0.325932
    X TAO_B97X            1.000000
    C TAO_B97X            1.000000
    $end
    ```

???+ example "Example 5.37: TAO- $\omega$ B97X-D4 calculation on H ${}_{2}$ molecule"
    ```qchem
    $molecule
    0 1
    H 0.00 0.00 0.00
    H 1.00 0.00 0.00
    $end
    
    $rem
    JOBTYPE              = sp
    unrestricted         = FALSE
    scf_guess            = SAD
    scf_guess_mix        = 0
    scf_algorithm        = diis
    max_scf_cycles       = 300
    GEN_SCFMAN           = FALSE
    xc_grid              = 000075000302
    scf_convergence      = 8
    thresh               = 14
    BASIS                = 6-31G(d)
    TAO_DFT              = true
    TAO_DFT_THETA        = 502796
    TAO_DFT_THETA_NDP    = 7
    EXCHANGE             = gen
    LRC_DFT              = TRUE
    COMBINE_K            = TRUE
    OMEGA                = 300
    symmetry             = false
    sym_ignore           = true
    basis_lin_dep_thresh = 8
    DFT_D                = D4
    DFT_D4_A1            = 65000000
    DFT_D4_A2            = 300000000
    DFT_D4_S6            = 100000000
    DFT_D4_S8            = 131716300
    DFT_D4_S9            = 100000000
    DFT_D4_S10           = 0
    $end
    
    $XC_functional
    X ETheta_LSDA         1.000000
    X LR_ETHETAX_LSDA     1.000000
    X SR_ETHETAX_LSDA     0.179379
    X HF                  0.179379
    X TAO_wB97X           1.000000
    C TAO_wB97X           1.000000
    $end
    ```

???+ example "Example 5.38: TAO- $\omega$ B97X-D4 using the pTAO/TDA method for the calculation of relative energies with respect to the pTAO reference state for the Ar $\cdots$ S ${}_{3}$ dimer"
    ```qchem
    $comment
     Ar-S3 in the singlet state with intermolecular distance R = 5 angstrom
    $end
    
    $molecule
    0 1
    S   3.1879342892   0.0000000000  0.0000000201
    S   2.1560328618   0.0000000000  1.6334812933
    S   2.1560328490   0.0000000000 -1.6334813134
    Ar -2.5000000000   0.0000000000  0.0000000000
    $end
    
    $rem
    JOBTYPE              = sp
    unrestricted         = FALSE
    scf_guess            = SAD
    scf_guess_mix        = 0
    scf_algorithm        = diis
    max_scf_cycles       = 300
    GEN_SCFMAN           = FALSE
    xc_grid              = 000099000590
    scf_convergence      = 8
    thresh               = 14
    BASIS                = 6-31G(d)
    TAO_DFT              = true
    TAO_DFT_THETA        = 502796
    TAO_DFT_THETA_NDP    = 7
    PTAO                 = true
    EXCHANGE             = gen
    LRC_DFT              = TRUE
    COMBINE_K            = TRUE
    OMEGA                = 300
    symmetry             = false
    sym_ignore           = true
    basis_lin_dep_thresh = 8
    DFT_D                = D4
    DFT_D4_A1            = 65000000
    DFT_D4_A2            = 300000000
    DFT_D4_S6            = 100000000
    DFT_D4_S8            = 131716300
    DFT_D4_S9            = 100000000
    DFT_D4_S10           = 0
    max_cis_cycles       = 100
    CIS_N_ROOTS          = 20
    CIS_SINGLETS         = TRUE
    CIS_TRIPLETS         = TRUE
    $end
    
    $XC_functional
    X ETheta_LSDA         1.000000
    X LR_ETHETAX_LSDA     1.000000
    X SR_ETHETAX_LSDA     0.179379
    X HF                  0.179379
    X TAO_wB97X           1.000000
    C TAO_wB97X           1.000000
    $end
    ```
