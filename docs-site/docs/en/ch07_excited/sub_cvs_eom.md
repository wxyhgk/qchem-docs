---
title: "7.9.9 EOM-CC Calculations of Core-Level States"
---

## 7.9.9 EOM-CC Calculations of Core-Level States

(July 4, 2026)

The core-valence separation (CVS) scheme[[218]](../bib_references/bib.md#bib215)
 allows one
to extend standard methods for excited and ionized states to the core-level
states. In this approach, the excitations involving core electrons are
decoupled from the rest of the configurational space. This allows one to reduce
computational costs and decouple the highly excited core states from the
continuum. Currently, CVS is implemented within EOM-EE/SF/IP-CCSD for energies
and transition properties (oscillator strengths, NTOs, Dyson orbitals, exciton
descriptors, SOCs, ECD cross sections). CVS-EOM-EE-CCSD can be used to model NEXAFS, while CVS-EOM-IP-CCSD
can be used to model XPS and XES. These methods can also be used to compute transient
absorption spectra, *e.g.*, valence pump/x-ray probe experiments.[[1403]](../bib_references/bib.md#bib1463)

The calculation of non-linear spectra, such as RIXS, is also possible. L-edge spectra
(XAS and XPS) can be described by using state-interaction
approach

in which spin-orbit coupling is evaluated using non-relativistic CVS-EOM-EE
states.[[1404]](../bib_references/bib.md#bib1464)
 Auger spectra can be computed using CVS-EOM-EE
via Feshbach–Fano approach[[1262]](../bib_references/bib.md#bib1316)
, either combined with
the explicit treatment of the continuum or using one-center approximation;[[1264]](../bib_references/bib.md#bib1318)

see Section [7.9.11](sec_Auger.md).

In **Q-Chem**, a slightly different version of CVS-EOM-EE-CCSD than the original
theory by Coriani and Koch[[269]](../bib_references/bib.md#bib270)
 is implemented: the reference
coupled-cluster amplitudes do not include core electrons.[[1402]](../bib_references/bib.md#bib1462)

To distinguish this method from the original,[[269]](../bib_references/bib.md#bib270)
 we refer in what follows to
the **Q-Chem** implementation as frozen-core-ground-state/core-valence-separated
EOM (FC-CVS-EOM) approach.[[1402]](../bib_references/bib.md#bib1462)

In the FC-CVS-EOM approach the ground-state parameters (amplitudes and
Lagrangian multipliers) are computed within the frozen-core approximation,
whereas the core-excitation energies and transition strengths
are obtained imposing that
at least one index in the EOM excitation (and ionization) operators refer to a
core occupied orbital.
Likewise, CVS is enforced in the calculation of the response
states in RIXS.[[982]](../bib_references/bib.md#bib1022)

To ensure the best convergence of EOM equations, the calculation is
*edge-specific* with respect to the highest lying edges (or deepest lying
core orbitals): the frozen-core and CVS spaces are selected for each edge such
that the core orbitals addressed in the excited state calculations are
explicitly frozen in the ground-state calculation and specifically included in
the EOM calculation. Examples [7.9.9.2](#ex:cvsee1) and [7.9.9.2](#ex:cvsee1) below
illustrate this point.

Although the convergence of FC-CVS-EOM is much more robust that that of regular
EOM-CCSD, sometimes calculations would collapse to low-lying artificial states.
If this happens, rerun the calculation using CVS_EOM_SHIFT to
specify an approximate onset of the edge.

To invoke the CVS scheme, use METHOD = CCSD and
CVS_EE_STATES instead of EE_STATES to specify the desired
target states (likewise, CVS_EE_SINGLETS and
CVS_EE_TRIPLETS can be used in exactly the same way as in regular
EOM calculations). For ionized states, use CVS_IP_STATES or
CVS_IP_ALPHA/CVS_IP_BETA. Spin-flip version can be deployed by
using CVS_SF_STATES (this may be needed for computing SOCs and L-edge spectra).
Preconverging single amplitudes can be invoked by CVS_EOM_PRECONV_SINGLES.
Transition properties and
Dyson orbitals can be computed either within the CVS manifold or between the CVS and
valence manifolds (see Section [7.9.29](topic_dyson.md) for definition of Dyson
orbitals). CVS-EOM-CCSD is only available with CCMAN2.

!!! note "Note"
    (1) Core electrons must be frozen in CVS-EOM calculations. The exact
    definition of the core depends on the edge, so using default values may be not appropriate.
    (2) The default setting (N_FROZEN_CORE = FC)
    does not work correctly in QM/MM calculations. One should
    specify the number of frozen core orbitals explicitly.


It is possible to set up customized CVS calculations for ionization/excitation
originating from a particular core orbital. To do so, one should first use
*$reorder_mo* feature to reorder orbitals such that the desired core
orbital appears the first in the list and then run a CVS-EOM calculation
with N_FROZEN_CORE = 1.

!!! note "Note"
    *$reorder_mo* works only with old SCF code (GEN_SCFMAN=FALSE).


It is also possible to split the frozen-core space into CVS-active and CVS-inactive subspaces
using the keyword N_FC_CVS_INACTIVE, which defines the size of the CVS-active
subspace as N_FROZEN_CORE minus N_FC_CVS_INACTIVE.
These CVS-active orbitals are arranged such that they precede the valence orbital subspace
but follow the CVS-inactive orbitals in the molecular orbital ordering
(use *$reorder_mo* section to customize if required).

### `CVS_EOM_SHIFT`

> **Specifies energy shift in CVS-EOM calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: corresponds to $n\times 10^{-3}$ hartree shift ( i.e. , 11000 = 11 hartree); solve for eigenstates around this value.
> * **Recommendation**: Improves the stability of the calculations.

### `N_FC_CVS_INACTIVE`

> **Number of frozen-core CVS inactive orbitals**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `n, where 0`: $\leq$
>     * `n`: $\leq$ total FC orbitals
> * **Recommendation**: Useful in cluster calculations.

### `CVS_EOM_PRECONV_SINGLES`

> **When not zero, singly excited vectors are converged prior to a full excited states calculation (CVS states only). Sets the maximum number of iterations for pre-converging procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: do not pre-converge
>     * `1`: pre-converge singles
> * **Recommendation**: Sometimes helps with problematic convergence.

### `CVS_EE_SINGLETS`

> **Sets the number of singlet core-excited state roots to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ excited states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `CVS_EE_TRIPLETS`

> **Sets the number of triplet core-excited state roots to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ excited states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `CVS_SF_STATES`

> **Sets the number of core-level spin-flip target states roots to find.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ SF states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `CVS_IP_STATES`

> **Sets the number of core-ionized states to find. By default, $\beta$ electron will be removed.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * `[i,j,k…]`: Find $i$ ionized states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `CVS_IP_ALPHA`

> **Sets the number of ionized target states derived by removing $\alpha$ electron ( $M_{S}=-\tfrac{1}{2}$ ).**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ ionized states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `CVS_IP_BETA`

> **Sets the number of ionized target states derived by removing $\beta$ electron ( $M_{S}=\tfrac{1}{2}$ , default for CVS-IP).**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ ionized states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

## 7.9.9.1 EOM-CC Calculations of RIXS

RIXS is a coherent two-photon process involving core-level states.[[982]](../bib_references/bib.md#bib1022)

The calculations of RIXS cross-sections require solving response equations, in the same
fashion as in calculations of 2PA cross-sections (see Section [7.9.21.6](sec_EOMGRAD.md#sec:2PA)).
Currently, only calculations of RIXS cross-sections between the CCSD reference and the
EOM-CCSD target states are possible.
Because of the resonant
nature of RIXS, damped response theory is used to handle singularities in the resolvent.
In addition,
CVS is enforced on the response vectors to eliminate their coupling with the ionization continuum.
To set up RIXS calculation, one needs to set METHOD = EOM-CCSD and
to specify the number of excited states to be included by using EE_STATES (note that only 2PA
bright states need to be included) and to activate CVS by using CVS_EE_STATES asking for zero states.
RIXS calculations is deployed by activating CC_EOM_RIXS.
The option for performing wave-function analysis (*e.g.*, NTO analysis) of
the complex RIXS one-particle transition density matrices is also available.
Conceptual details can be found in Ref. [[980]](../bib_references/bib.md#bib1023)
.
Finally, one can request to compute REXS (cross-section for the “elastic” peak) by
CC_REF_PROP = 1 (by default, REXS is not calculated)
This feature is only available within fc-CVS-EOM-EE-CCSD.

### `CC_EOM_RIXS`

> **Whether or not the RIXS scattering moments and cross-sections will be calculated.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: Perform RIXS within fc-CVS-EOM-EE-CCSD using the response wave functions of the CCSD reference state only
>     * `2`: Perform RIXS within fc-CVS-EOM-EE-CCSD response theory along with the wave-function analysis of RIXS transition density matrices
>     * `11`: Perform RIXS within the standard EOM-EE-CCSD using the response wave functions of the CCSD reference state only
>     * `12`: Use $\sigma$ -intermediates for RIXS response calculations within the standard EOM-EE-CCSD
> * **Recommendation**: Use 1 to deploy fc-CVS-EOM-EE-CCSD with robust convergence

!!! note "Note"
    Since the RIXS response solutions within EOM-EE-CCSD often do not converge, fc-CVS-EOM-EE-CCSD RIXS calculations with CC_EOM_RIXS = 1 are recommended for smooth convergence. All other options are experimental.


To specify pumping frequencies and damping
factor $\epsilon$, use *$rixs* section:

> ```qchem
> $rixs
> damped_epsilon 0.005       Damping factor in hartree.
> omega_1 2306503 500 10 0   Pumping frequencies: starting w (cm-1), increment (cm-1),
>                            number of frequency points, algo (always 0 for now)
> omega_2 2200000 600 20 0   Emitted frequencies:  starting w (cm-1), increment (cm-1),
>                            number of frequency points, algo (always 0 for now)
> $end
> ```

Damping factor (DAMPED_EPSILON) is specified in atomic units (0.005 is a good choice).
OMEGA_1 specifies the starting pumping frequency (in cm${}^{-1}$), the increment in frequency
scan (in cm${}^{-1}$), number of frequency points, and the algorithm for response equation (use zero until further notice).
OMEGA_2 should be specified only for generating 2D RIXS scans.
Example [7.9.9.2](#ex:cvsee1) illustrates the setup of RIXS calculations.

By default, the damped RIXS response wave functions are computed using a new
iterative, Davidson-like subspace procedure called the **Dalton** solver.[[248]](../bib_references/bib.md#bib251)

It is controlled by the DALTON_XCONV, DALTON_PRECOND_START,
DALTON_MAXITER, and DALTON_MAXSPACE keywords.
Damped RIXS response wave functions can also be computed using the older
DIIS procedure, by setting DAMPED_DALTON_SOLVER = FALSE.
The DIIS solver is controlled by the
CC_MAX_ITER, CC_DIIS_START,
CC_DIIS_SIZE, CC_EOM_2PA_ECONV, and
CC_EOM_2PA_XCONV.

!!! note "Note"
    - For better convergence of the response equations with DIIS solver,
    increase CC_DIIS_SIZE (25 is recommended) and consider using a larger damping factor.

    - The **Dalton** 
    solver uses square of the norm of the residual in estimating convergence (as in the Davidson solver),
    whereas the DIIS solver uses the norm of the difference of the response vector between iterations.


## 7.9.9.2 Examples

The following examples illustrate how to perform these calculations.

- Example [7.9.9.2](#ex:cvsee1): the $1s$ orbital on the oxygen atom is frozen in
the CCSD calculation (N_FROZEN_CORE = FC). In the EOM
calculation, the CVS approximation is invoked (CVS_EE_SINGLETS), so
that the core-excitation energies are obtained as the lowest excitations. The
calculation of the oscillator strengths and rotatory strengths is activated
by selecting CC_TRANS_PROP = 1 and the **libwfa** analysis is invoked by
STATE_ANALYSIS = TRUE (see Section [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md)).
Note that rotatory strengths will be zero for non-chiral systems.
- Example [7.9.9.2](#ex:cvsee1): CVS-EOM-EE-CCSD calculations in a two-edge
molecule (carbon monoxide). In the present implementation, the calculation should be done
separately for each edge. The first job computes carbon-edge states. Since
the carbon $1s$ orbital is the highest in energy (among the core $1s$ orbitals
of the molecule), the input for the C-edge is similar to
example [7.9.9.2](#ex:cvsee1). Both the oxygen’s and the carbon’s $1s$ orbitals are
frozen in the reference CCSD calculation. In the EOM part, the carbon
core-excited states are automatically selected. In this case, using default
frozen core settings (N_FROZEN_CORE = FC) is equivalent to
specifying N_FROZEN_CORE = 2. In the second input, the oxygen edge
is computed. As the core-orbitals of oxygen lie deeper, the frozen core and CVS
selection specifically targets the oxygen edge by using a smaller core. The
1$s$ orbital of the oxygen atom is selected by N_FROZEN_CORE = 1. If
the molecule has other edges, the deepest lying core orbitals, up to and
including those of the edge of interest, should be selected by an appropriate
value of N_FROZEN_CORE.
- Example [7.9.9.2](#ex:cvsee1): calculation of the XAS spectrum of ammonia using
additional set of Rydberg functions placed on the nitrogen; the exponents of
the Rydberg functions were generated using Kaufmann’s recipe[[672]](../bib_references/bib.md#bib696)
.
Note that when ghost atoms are used, the symmetry is turned off. It can be forced on by using
FORCE_SYMMETRY_ON keyword.
Alternatively, this calculation can be set up by adding additional diffuse functions
to all (or selected) atoms using even-tempered exponents. Users must ensure that the ghost atoms do not lower the symmetry.
- Example [7.9.9.2](#ex:cvsee1): calculation of the XES spectrum of benzene.
- Examples [7.9.9.2](#ex:cvsee1) and [7.9.9.2](#ex:cvsee1): calculations of Dyson
orbitals between core-excited and core-ionized states and between core-excited and valence-ionized states.
- Example [7.9.9.2](#ex:cvsee1): setup of RIXS calculations.

Calculations of L-edge spectra using state-interaction
approach[[1404]](../bib_references/bib.md#bib1464)
 entails a two-step procedure. First, **Q-Chem** computes necessary CVS-EOM states and SOCs. In the second step, the spin-orbit
perturbed spectrum is computed by a post-processing script. Scripts, detailed
instructions, and examples can be found elsewhere.

???+ example "Example 7.70: FC-CVS-EOM-EE-CCSD calculation of the first six dipole-allowed core excitation
energies and their intensities at the oxygen edge of water. Wave-function
analysis is also performed."
    ```qchem
    $molecule
       0 1
       O    0.0000   0.0000   0.1173
       H    0.0000   0.7572  -0.4692
       H    0.0000  -0.7572  -0.4692
    $end
    
    $rem
       METHOD              = eom-ccsd
       BASIS               = aug-cc-pVDZ
       CVS_EE_SINGLETS     = [3,0,2,1]
       N_FROZEN_CORE       = fc
       CC_TRANS_PROP       = true
       EOM_PRECONV_SINGLES = true
       STATE_ANALYSIS      = true !invoke libwa to compute NTOs and exciton descriptors
       MOLDEN_FORMAT       = true
       NTO_PAIRS           = 3
       POP_MULLIKEN        = true
    $end
    ```

???+ example "Example 7.71: FC-CVS-EOM-EE-CCSD calculations of the first two dipole-allowed core
excitation energies per irreducible representation and their intensities at
(1) carbon and (2) oxygen edges of carbon monoxide."
    ```qchem
    $molecule
       0 1
       O    0.0000   0.0000    0.913973
       C    0.0000   0.0000   -1.218243
    $end
    
    $rem
       METHOD               =  eom-ccsd
       BASIS                =  aug-cc-pVDZ
       INPUT_BOHR           =  true
       CVS_EE_SINGLETS      =  [2,0,2,2]
       N_FROZEN_CORE        =  fc            !For C K-edge
       EOM_PRECONV_SINGLES  =  true
       CC_TRANS_PROP        =  true
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD               =  eom-ccsd
       BASIS                =  aug-cc-pVDZ
       CVS_EE_SINGLETS      =  [2,0,2,2]
       N_FROZEN_CORE        =  1             !For O K-edge
       EOM_PRECONV_SINGLES  =  true
       CC_TRANS_PROP        =  true
    $end
    ```

???+ example "Example 7.7.72: Calculation of XAS spectrum of ammonia using additional Rydberg functions placed on the ghost atom."
    ```qchem
    $comment
    NEXAFS AMMONIA / 6-311++G**+Rydberg functions
    Optimized geometry: NH3_opt_coord.out
    $end
    
    $molecule
    0 1
    N      -0.0002568808    -0.2210075702    -0.0000000021
    H       0.8838383819     0.5154343604     1.5287018716
    H      -1.7658867303     0.5161842661     0.0000000000
    H       0.8838383819     0.5154343604    -1.5287018716
    Gh      0.0000000000     0.0000000000     0.0000000000
    $end
    
    $rem
        input_bohr = true
        jobtype = sp
        method = eom-ccsd
        cvs_ee_singlets    [5,5]
        basis = general    !User-defined basis to add extra Rydberg functions
        n_frozen_core = fc
        cc_trans_prop = true
        eom_preconv_singles = true
        eom_davidson_convergence = 4
        eom_shift = 14760
        FORCE_SYMMETRY_ON = true   Forces symmetry to be turned on
        MEM_TOTAL 30000   30GB of total memory
    $end
    
    $basis
    N    0
    6-311++G*
    ****
    H    0
    6-311++G*
    ****
    Gh   0
    S   1   1.00
            0.0112533427        1.0000000000
    S   1   1.00
            0.0058583805        1.0000000000
    S   1   1.00
            0.0033459739        1.0000000000
    S   1   1.00
            0.0020484225        1.0000000000
    S   1   1.00
            0.0013236424        1.0000000000
    P   1   1.00
            0.0192542060        1.0000000000
    P   1   1.00
            0.0099882106        1.0000000000
    P   1   1.00
            0.0056893607        1.0000000000
    P   1   1.00
            0.0034756797        1.0000000000
    P   1   1.00
            0.0022420590        1.0000000000
    D   1   1.00
            0.0274456919        1.0000000000
    D   1   1.00
            0.0142043987        1.0000000000
    D   1   1.00
            0.0080765930        1.0000000000
    D   1   1.00
            0.0049271863        1.0000000000
    D   1   1.00
            0.0031748110        1.0000000000
    ****
    $end
    
    ```

???+ example "Example 7.73: Calculation of XES spectrum of benzene"
    ```qchem
    $comment
    RI-MP2/cc-pVTZ optimized geometry. XES calculation.
    $end
    
    $molecule
    0 1
        H         2.4750347531    0.0000000000    0.0000000000
        C         1.3935929418    0.0000000000    0.0000000000
        C         0.6967964709    1.2068868901    0.0000000000
        H         1.2375173766    2.1434429715    0.0000000000
        C        -0.6967964709    1.2068868901    0.0000000000
        H        -1.2375173766    2.1434429715    0.0000000000
        C        -1.3935929418    0.0000000000    0.0000000000
        H        -2.4750347531    0.0000000000    0.0000000000
        C        -0.6967964709   -1.2068868901    0.0000000000
        H        -1.2375173766   -2.1434429715    0.0000000000
        C         0.6967964709   -1.2068868901    0.0000000000
        H         1.2375173766   -2.1434429715    0.0000000000
    $end
    
    $rem
       BASIS         =  6-31G*
       METHOD        =  eom-ccsd
       IP_STATES     = [3,2,1,1,0,1,2,2] !All valence Koompans-like ionized states
                                         !except for 3 lowest ones
       CVS_IP_STATES = [2,1,0,0,0,0,1,2] !All core-ionized states
       CC_TRANS_PROP = 2 !Compute transitions between all pairs of EOM states
       CC_MEMORY     = 8000  !8 GB
    $end
    ```

???+ example "Example 7.74: Calculation of Dyson orbitals between FC-CVS-EOM-EE-CCSD and
FC-CVS-EOM-IP-CCSD manifolds."
    ```qchem
    $comment
       CVS-IP/CVS-EE Dyson orbitals, formaldehyde
    $end
    
    $molecule
       0 1
       C
       H   1  1.096135
       H   1  1.096135  2  116.191164
       O   1  1.207459  2  121.904418  3  -180.000000  0
    $end
    
    $rem
       METHOD           =  eom-ccsd
       BASIS            =  cc-pVDZ   ! Please do not use BASIS2
       SCF_CONVERGENCE  =  8
       CVS_IP_STATES    =  [1,0,0,0]
       CVS_EE_STATES    =  [1,0,1,0]
       CC_DO_DYSON      =  true
       CC_TRANS_PROP    =  2 !Compute all EOM-to-EOM transitions
    $end
    ```

???+ example "Example 7.75: Calculation of Dyson orbitals between FC-CVS-EOM-EE-CCSD and EOM-IP-CCSD
manifolds."
    ```qchem
    $comment
       IP/CVS-EE Dyson orbitals, formaldehyde
    $end
    
    $molecule
       0 1
       C
       H  1  1.096135
       H  1  1.096135  2  116.191164
       O  1  1.207459  2  121.904418  3  -180.000000  0
    $end
    
    $rem
       METHOD           =  eom-ccsd
       BASIS            =  cc-pVDZ
       SCF_CONVERGENCE  =  8
       IP_STATES        =  [1,0,0,0]   ! Valence a1 hole
       CVS_EE_STATES    =  [1,0,0,0]
       CC_DO_DYSON      =  true
       CC_TRANS_PROP    =  2 !Compute all EOM-to-EOM transitions
    $end
    ```

???+ example "Example 7.76: Calculation of Dyson orbitals between FC-CVS-EOM-EE-CCSD and
FC-CVS-EOM-IP-CCSD manifolds."
    ```qchem
    $comment
    CVS-IP/CVS-EE Dyson orbitals, formaldehyde
    $end
    
    $molecule
       0 1
       C
       H  1  1.096135
       H  1  1.096135  2  116.191164
       O  1  1.207459  2  121.904418  3  -180.000000  0
    $end
    
    $rem
       BASIS           =  cc-pVDZ
       SCF_CONVERGENCE = 8
       METHOD          = eom-ccsd
       IP_STATES       = [1,0,0,0]   ! Valence a1 hole
       CVS_EE_STATES   = [1,0,0,0]
       CC_DO_DYSON     = true
       CC_TRANS_PROP   = true        ! required to activate a Dyson orbitals job
    $end
    ```

???+ example "Example 7.77: Calculation of RIXS/REXS for benzene (10 excited states per 2PA active irrep)"
    ```qchem
    $comment
    RI-MP2/cc-pVTZ optimized geometry.
    Pump XAS transition peak A at 285.97 eV, only one frequency point.
    $end
    
    $molecule
       0 1
       H      2.4750347531    0.0000000000    0.0000000000
       C      1.3935929418    0.0000000000    0.0000000000
       C      0.6967964709    1.2068868901    0.0000000000
       H      1.2375173766    2.1434429715    0.0000000000
       C     -0.6967964709    1.2068868901    0.0000000000
       H     -1.2375173766    2.1434429715    0.0000000000
       C     -1.3935929418    0.0000000000    0.0000000000
       H     -2.4750347531    0.0000000000    0.0000000000
       C     -0.6967964709   -1.2068868901    0.0000000000
       H     -1.2375173766   -2.1434429715    0.0000000000
       C      0.6967964709   -1.2068868901    0.0000000000
       H      1.2375173766   -2.1434429715    0.0000000000
    $end
    
    $rem
       BASIS         = 6-31(+,+)G**
       METHOD        = eom-ccsd
       CVS_EE_STATES = [0,0,0,0,0,0,0,0]       just to invoke CVS
       EE_STATES     = [10,10,10,10,0,0,0,0]   10 states in each 2PA active irrep
       CC_REF_PROP   = 1     ! Calculate REXS in addition to RIXS
       CC_EOM_RIXS   = 1     ! Activate RIXS calculation using fc-CVS-EOM-EE-CCSD
       CC_DIIS_SIZE  = 25    ! Use for better convergence of response equations
       CC_MEMORY     = 8000  !8 GB
       mem_total = 8500
    $end
    
    $rixs
       omega_1         2306503 500 1 0
       damped_epsilon  0.005
    $end
    ```

???+ example "Example 7.78: FC-CVS-EOM-EE-CCSD and FC-CVS-EOM-IP-CCSD calculation for a water dimer with core excitations and ionization arising from the energetically lowest core orbital with the other core orbital kept CVS inactive. The first input reorders MOs. The second input defines CVS active and inactive orbitals before computing core-level states and properties."
    ```qchem
    $molecule
    0 1
              O      -4.9920582819    -0.1246131900     2.2067549109
              H      -5.5873205924    -0.9397949066     2.3252790559
              H      -4.9827539950     0.0559440223     1.1016406903
              O      -6.5474306925    -1.1803213469    -1.0374284134
              H      -5.7367207770    -0.6839235793    -0.7295169422
              H      -6.2716956294    -2.1185636950    -1.1190969125
    $end
    
    $rem
       GEN_SCFMAN = false
       use_libqints = true
       CC_MEMORY = 4000
       MEM_STATIC = 600
       BASIS  =  6-31g
       METHOD  =  hf
       n_frozen_core = 0
       thresh =  14          Does not converge with defaults
       scf_algorithm gdm     Does not converge with defaults
    $end
    
    $reorder_mo
    2 1 3
    2 1 3
    $end
    
    @@@
    
    $molecule
    0 1
              O      -4.9920582819    -0.1246131900     2.2067549109
              H      -5.5873205924    -0.9397949066     2.3252790559
              H      -4.9827539950     0.0559440223     1.1016406903
              O      -6.5474306925    -1.1803213469    -1.0374284134
              H      -5.7367207770    -0.6839235793    -0.7295169422
              H      -6.2716956294    -2.1185636950    -1.1190969125
    $end
    
    $rem
       CC_MEMORY = 4000
       MEM_STATIC = 600
       BASIS  =  6-31g
       thresh =  14          Does not converge with defaults
       n_frozen_core = 2
       scf_guess = read
       max_scf_cycles = 0
       method = eom-ccsd
       cvs_ee_states = [2]
       cvs_ip_states = [1]
       n_fc_cvs_inactive = 1
       cc_trans_prop = 1
       cc_ref_prop = 1
       cc_eom_prop = 1
    $end
    
    
    ```
