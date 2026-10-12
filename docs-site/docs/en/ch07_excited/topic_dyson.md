---
title: "7.9.29 Dyson Orbitals for Ionized or Attached States within EOM-CCSD"
---

## 7.9.29 Dyson Orbitals for Ionized or Attached States within EOM-CCSD

(July 4, 2026)

Dyson orbitals can be used to compute total photodetachment/photoionization cross-sections, as well as angular distribution of
photoelectrons. A Dyson orbital is the overlap between the N-electron
molecular wave function and the $N-1$/$N+1$ electron wave function of the
corresponding cation/anion:

<a id="A3.S8.EGx60"></a>

$$
\displaystyle\phi^{d}(1) \tag{7.127}
$$

For the Hartree-Fock wave functions and within Koopmans’ approximation, these
are just the canonical HF orbitals. For correlated wave functions, Dyson
orbitals are linear combinations of the reference molecular orbitals:

<a id="A3.S8.EGx61"></a>

$$
\displaystyle\phi^{d} \tag{7.129}
$$

The calculation of Dyson orbitals is straightforward within the EOM-IP/EA-CCSD methods, where cation/anion and initial molecule states are
defined with respect to the same MO basis. Since the left and right CC vectors
are not the same, one can define correspondingly two Dyson orbitals (left and right):

<a id="A3.S8.EGx62"></a>

$$
\displaystyle\begin{aligned} \displaystyle\gamma_{p}^{R}&\displaystyle=\bigl{\langle}\Phi_{0}e^{T_{1}+T_{2}}L^{EE}\bigl{|}p^{\dagger}\bigr{|}R^{IP}e^{T_{1}+T_{2}}\Phi_{0}\bigr{\rangle}\\
\displaystyle\gamma_{p}^{L}&\displaystyle=\bigl{\langle}\Phi_{0}e^{T_{1}+T_{2}}L^{IP}\bigl{|}p\bigr{|}R^{EE}e^{T_{1}+T_{2}}\Phi_{0}\bigr{\rangle}\end{aligned} \tag{7.132}
$$

The norm of these orbitals is proportional to the one-electron character of the transition.

Dyson orbitals also offer qualitative insight visualizing the difference
between molecular and ionized/attached states. In ionization/photodetachment processes, these orbitals can be also interpreted as the wave
function of the leaving electron. For additional details, see
Refs. [[1002]](../bib_references/bib.md#bib1043)
 and [[1003]](../bib_references/bib.md#bib1044)
. Dyson orbitals can be
used for computing total and differential photoelectron cross-sections using a
stand-alone **ezDyson** code [[478]](../bib_references/bib.md#bib490)
 or built-in **Q-Chem**’s
functionality (see section [7.9.21.10](sec_EOMGRAD.md#sec:freeEl)).

Dyson orbitals can be computed both for valence states and core-level states;[[1403]](../bib_references/bib.md#bib1463)

see Section [7.9.9](sub_cvs_eom.md) for calculations of Dyson orbitals within the FC-CVS-EOM framework.

The ezSpectra suite: An easy-to-use toolkit for spectroscopy modeling -
Presented by Prof. Samer Gozem, Georgia State University

**Q-Chem** can also compute the overlap of a Dyson orbital with a plane wave,
$\langle\phi^{d}|e^{i{\mathbf{k}r}}\rangle$,
using the DYSON_PW_COUPLING keyword. The user can request calculations of
the overlap for several $|{\mathbf{k}}|$-values and either
perform averaging over ${\mathbf{k}}$-directions or perform the
calculation for a fixed direction of ${\mathbf{k}}$.
This capability is illustrated by examples [7.9.29.2](#ex:DYSONPW) and [7.9.29.2](#ex:DYSONPW)
and explained in section [7.9.21.10](sec_EOMGRAD.md#sec:freeEl).

## 7.9.29.1 Dyson Orbitals Job Control

The calculation of Dyson orbitals is implemented for the ground (reference) and
excited states ionization/electron attachment. To obtain the ground state
Dyson orbitals one needs to run an EOM-IP/EA-CCSD calculation, request
transition properties calculation by setting CC_TRANS_PROP =
TRUE and CC_DO_DYSON = TRUE. The Dyson orbitals
decomposition in the MO basis is printed in the output, for all transitions
between the reference and all IP/EA states. At the end of the file, also
the coefficients of the Dyson orbitals in the AO basis are available.

Two implementations of Dyson orbitals are currently available: (i) the original
implementation in CCMAN; and (ii) new implementation in CCMAN2. The CCMAN
implementation is using a diffuse orbital trick (*i.e.*,
EOM_FAKE_IPEA will be automatically set to TRUE in these
calculations). Note: this implementation has a bug affecting the values of
norms of Dyson orbitals (the shapes are correct); thus, using this code is
strongly discouraged. The CCMAN2 implementation has all types of initial
states available: Dyson orbitals from ground CC, excited EOM-EE, and spin-flip
EOM-SF states; it is fully compatible with all helper features for EOM
calculations, like FNO, RI, Cholesky decomposition. The CCMAN2 implementation
can use a user-specified EOM guess (using EOM_USER_GUESS keyword and
*$eom_user_guess* section), which is recommended for highly excited states
(such as core-ionized states). In addition, CCMAN2 can calculate Dyson
orbitals involving meta-stable states (see Section [7.9.10](sub_cc_cs_cap.md)) and
core-level states (see Section [7.9.9](sub_cvs_eom.md)).

For calculating Dyson orbitals between excited or spin-flip states from the
reference configuration and IP/EA states, same CC_TRANS_PROP =
TRUE and CC_DO_DYSON = TRUE keywords have to be added to the
combination of usual EOM-IP/EA-CCSD and EOM-EE-CCSD or EOM-SF-CCSD
calculations. (However, note the separate keyword CC_DO_DYSON_EE =
TRUE for CCMAN.) The IP_STATES keyword is used to specify
the target ionized states. The attached states are specified by
EA_STATES. The EA-SF states are specified by EOM_EA_BETA.
The excited (or spin-flipped) states are specified by EE_STATES and
SF_STATES. The Dyson orbital decomposition in MO and AO bases is
printed for each EE/SF-IP/EA pair of states first for reference,
then for all excited states in the order: CC-IP/EA1, CC-IP/EA2,$\ldots$,
EE/SF1 - IP/EA1, EE/SF1 - IP/EA2,$\ldots$, EE/SF2
- IP/EA1, EE/SF2 - IP/EA2,$\ldots$, and so on. CCMAN
implementation keeps reference transitions separate, in accordance with
separating keywords.

### `CC_DO_DYSON`

> **CCMAN2: starts all types of Dyson orbitals calculations. Desired type is determined by requesting corresponding EOM-XX transitions CCMAN: whether the reference-state Dyson orbitals will be calculated for EOM-IP/EA-CCSD calculations.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE (the option must be specified to run this calculation)`
> * **Options**:
>     * `TRUE/FALSE`
> * **Recommendation**: none

### `CC_DO_DYSON_EE`

> **Whether excited-state or spin-flip state Dyson orbitals will be calculated for EOM-IP/EA-CCSD calculations with CCMAN.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE (the option must be specified to run this calculation)`
> * **Options**:
>     * `TRUE/FALSE`
> * **Recommendation**: none

Dyson orbitals are most easily visualized by setting IQMOL_FCHK =
TRUE (equivalently, GUI = 2) and reading the resulting
checkpoint file into **IQmol**. In addition to the canonical orbitals, the
Dyson orbitals will appear under the Surfaces item in the Model View. For
step-by-step instructions, see the **ezDyson** manual.

Alternatively Dyson orbitals can be plotted using IANLTY = 200 and the
*$plots* utility. Only the sizes of the box need to be specified, followed by a line of zeros:

> ```qchem
> $plots
>    comment
>    10   -2   2
>    10   -2   2
>    10   -2   2
>    0     0   0    0
> $plots
> ```

All Dyson orbitals on the Cartesian grid will be written in the resulting
`plot.mo` file (only CCMAN). For RHF(UHF) reference, the columns order in
`plot.mo` is:
$\phi^{lr}_{1}\alpha\ (\phi^{lr}_{1}\beta)\ \phi^{rl}_{1}\alpha\ (\phi^{rl}_{1}\beta)\ \phi^{lr}_{2}\alpha\ (\phi^{lr}_{2}\beta)\ \ldots$

In addition, setting the MAKE_CUBE_FILES keyword to TRUE will create
cube files for Dyson orbitals which can be viewed with
Visual Molecular Dynamics (VMD)[[W. Humphrey, A. Dalke, and K. Schulten (1996)]](../bib_references/bib.md#bib627)
or other programs;
see Section [10.5.5](../ch10_properties/sec_cubefiles.md) for details. This option is available for
CCMAN and CCMAN2. The Dyson orbitals will be written to files `mo.1.cube`,
`mo.2.cube`, $\ldots$ in the order $\phi^{lr}_{1}\ \phi^{rl}_{1}\ \ \phi^{lr}_{2}\ \phi^{rl}_{2}\ldots$. For meta-stable states, the real and imaginary parts
of the Dyson orbitals are written to separate files in the order
$\text{Re}(\phi^{lr}_{1})\ \text{Re}(\phi^{rl}_{1})\ \ \text{Re}(\phi^{lr}_{2})\ \text{Re}(\phi^{rl}_{2})\ldots\text{Im}(\phi^{lr}_{1})\ \text{Im}(\phi^{rl}_{1})\ \ \text{Im}(\phi^{lr}_{2})\ \text{Im}(\phi^{rl}_{2})\ldots$

**Note: 

Visualization via the **MolDen** format is not available.
**

## 7.9.29.2 Examples

???+ example "Example 7.166: Plotting grd-ex and ex-grd state Dyson orbitals for ionization of the oxygen
molecule. The target states of the cation are ${}^{2}$ A ${}_{g}$ and ${}^{2}$ B ${}_{2u}$ . Works
for CCMAN only."
    ```qchem
    $molecule
       0 3
       O    0.000  0.000  0.000
       O    1.222  0.000  0.000
    $end
    
    $rem
       BASIS          6-31G*
       METHOD         eom-ccsd
       IP_STATES      [1,0,0,0,0,0,1,0] Target EOM-IP states
       CC_TRANS_PROP  true  request transition OPDMs to be calculated
       CC_DO_DYSON    true  calculate Dyson orbitals
       IANLTY         200
    $end
    
    $plots
    plots excited states densities and trans densities
       10   -2   2
       10   -2   2
       10   -2   2
       0     0   0    0
    $plots
    ```

???+ example "Example 7.167: Plotting ex-ex state Dyson orbitals between the 1st ${}^{2}A_{1}$ excited state of
the HO radical and the the 1st A ${}_{1}$ and A ${}_{2}$ excited states of HO ${}^{-}$ . Works
for CCMAN only."
    ```qchem
    $molecule
       -1 1
       H    0.000   0.000  0.000
       O    1.000   0.000  0.000
    $end
    
    $rem
       METHOD             eom-ccsd
       BASIS              6-31G*
       IP_STATES          [1,0,0,0]  states of HO radical
       EE_STATES          [1,1,0,0]  excited states of HO-
       CC_TRANS_PROP      2          calculate transition properties
       CC_DO_DYSON        true       calculate Dyson orbitals for ionization from ex. states
       IANLTY             200
    $end
    
    $plots
    plot excited states densities and trans densities
       10   -2   2
       10   -2   2
       10   -2   2
       0     0   0    0
    $plots
    ```

???+ example "Example 7.168: Dyson orbitals for ionization of CO molecule;
A ${}_{1}$ and B ${}_{1}$ ionized states requested."
    ```qchem
    $molecule
       0 1
       O
       C  O  1.131
    $end
    
    $rem
       CORRELATION           CCSD
       BASIS                 cc-pVDZ
       PURECART              111        5d, will be required for ezDyson
       IP_STATES             [1,0,1,0]  (A1,A2,B1,B2)
       CCMAN2                true
       CC_DO_DYSON           true
       CC_TRANS_PROP         true       necessary for Dyson orbitals job
       PRINT_GENERAL_BASIS   true       will be required for ezDyson
    $end
    ```

???+ example "Example 7.169: Dyson orbitals for ionization of H ${}_{2}$ O;
core (A ${}_{1}$ ) state requested — ionization from O(1s)."
    ```qchem
    $molecule
       0 1
       O
       H1  O  0.955
       H2  O  0.955  H1  104.5
    $end
    
    $rem
       CORRELATION           CCSD
       BASIS                 cc-pVTZ
       PURECART              111        5d, will be required for ezDyson
       IP_STATES             [1,0,0,0]  (A1,A2,B1,B2)
       EOM_USER_GUESS        1          on, further defined in $eom_user_guess
       CCMAN2                true
       CC_DO_DYSON           true
       CC_TRANS_PROP         true       necessary for Dyson orbitals job
       PRINT_GENERAL_BASIS   true       will be required for ezDyson
       N_FROZEN_CORE         false
    $end
    
    $eom_user_guess
       1
    $end
    ```

???+ example "Example 7.170: Dyson orbitals for ionization of NO molecule using EOM-EA and a closed-shell
cation reference;
A ${}_{1}$ and B ${}_{2}$ states requested."
    ```qchem
    $molecule
       +1 1
       N   0.00000  0.00000  0.00000
       O   0.00000  0.00000  1.02286
    $end
    
    $rem
       CORRELATION            CCSD
       BASIS                  aug-cc-pVTZ
       PURECART               111       5d, will be required for ezDyson
       EA_STATES              [1,0,0,1] (A1,A2,B1,B2)
       CCMAN2                 true
       CC_DO_DYSON            true
       CC_TRANS_PROP          true      necessary for Dyson orbitals job
       PRINT_GENERAL_BASIS    true      will be required for ezDyson
    $end
    ```

???+ example "Example 7.7.171: Dyson orbitals for detachment from the meta-stable ${}^{2}\Pi_{g}$ state of N ${}_{2}^{-}$ ."
    ```qchem
    $molecule
       0 1
       N   0.0   0.0    0.55
       N   0.0   0.0   -0.55
       GH  0.0   0.0    0.0
    $end
    
    $rem
       METHOD            EOM-CCSD
       EA_STATES         [0,0,2,0,0,0,0,0]
       CC_MEMORY         5000
       MEM_STATIC        1000
       BASIS             GEN
       COMPLEX_CCMAN     TRUE
       CC_TRANS_PROP     TRUE
       CC_DO_DYSON       TRUE
       MAKE_CUBE_FILES   TRUE
       IANLTY            200
       FORCE_SYMMETRY_ON TRUE
    $end
    
    $complex_ccman
       CS_HF             1
       CAP_TYPE          1
       CAP_X             2760
       CAP_Y             2760
       CAP_Z             4880
       CAP_ETA           400
    $end
    
    $plots
    plot Dyson orbitals
       50 -10.0 10.0
       50 -10.0 10.0
       50 -10.0 10.0
       0 0 0 0
    $end
    
    $basis
    N    0
    S    8    1.000000
       1.14200000E+04    5.23000000E-04
       1.71200000E+03    4.04500000E-03
       3.89300000E+02    2.07750000E-02
       1.10000000E+02    8.07270000E-02
       3.55700000E+01    2.33074000E-01
       1.25400000E+01    4.33501000E-01
       4.64400000E+00    3.47472000E-01
       5.11800000E-01   -8.50800000E-03
    S    8    1.000000
       1.14200000E+04   -1.15000000E-04
       1.71200000E+03   -8.95000000E-04
       3.89300000E+02   -4.62400000E-03
       1.10000000E+02   -1.85280000E-02
       3.55700000E+01   -5.73390000E-02
       1.25400000E+01   -1.32076000E-01
       4.64400000E+00   -1.72510000E-01
       5.11800000E-01    5.99944000E-01
    S    1    1.000000
       1.29300000E+00    1.00000000E+00
    S    1    1.000000
       1.78700000E-01    1.00000000E+00
    P    3    1.000000
       2.66300000E+01    1.46700000E-02
       5.94800000E+00    9.17640000E-02
       1.74200000E+00    2.98683000E-01
    P    1    1.000000
       5.55000000E-01    1.00000000E+00
    P    1    1.000000
       1.72500000E-01    1.00000000E+00
    D    1    1.000000
       1.65400000E+00    1.00000000E+00
    D    1    1.000000
       4.69000000E-01    1.00000000E+00
    F    1    1.000000
       1.09300000E+00    1.00000000E+00
    S    1    1.000000
       5.76000000E-02    1.00000000E+00
    P    1    1.000000
       4.91000000E-02    1.00000000E+00
    D    1    1.000000
       1.51000000E-01    1.00000000E+00
    F    1    1.000000
       3.64000000E-01    1.00000000E+00
    ****
    GH   0
    S    1    1.000000
       2.88000000E-02    1.00000000E+00
    S    1    1.000000
       1.44000000E-02    1.00000000E+00
    S    1    1.000000
       0.72000000E-02    1.00000000E+00
    S    1    1.000000
       0.36000000E-02    1.00000000E+00
    S    1    1.000000
       0.18000000E-02    1.00000000E+00
    S    1    1.000000
       0.09000000E-02    1.00000000E+00
    P    1    1.000000
       2.45000000E-02    1.00000000E+00
    P    1    1.000000
       1.22000000E-02    1.00000000E+00
    P    1    1.000000
       0.61000000E-02    1.00000000E+00
    P    1    1.000000
       0.305000000E-02    1.00000000E+00
    P    1    1.000000
       0.152500000E-02    1.00000000E+00
    P    1    1.000000
       0.076250000E-02    1.00000000E+00
    D    1    1.000000
       0.755000000E-01    1.00000000E+00
    D    1    1.000000
       0.377500000E-01    1.00000000E+00
    D    1    1.000000
       0.188750000E-01    1.00000000E+00
    D    1    1.000000
       0.094375000E-01    1.00000000E+00
    D    1    1.000000
       0.047187500E-01    1.00000000E+00
    D    1    1.000000
       0.023593750E-01    1.00000000E+00
    ****
    $end
    ```

???+ example "Example 7.172: Dyson orbitals for ionization of triplet O ${}_{2}$ and O ${}_{2}^{-}$ at slightly
stretched (relative to the equilibrium O ${}_{2}$ geometry); B ${}_{3g}$ states are
requested."
    ```qchem
    $comment
       EOM-IP-CCSD/6-311+G* and EOM-EA-CCSD/6-311+G* levels of theory,
       UHF reference.  Start from O2:
        1) detach electron - ionization of neutral (alpha IP).
        2) attach electron, use EOM-EA w.f. as initial state
           - ionization of anion (beta EA).
    $end
    
    $molecule
       0 3
       O   0.00000  0.00000  0.00000
       O   0.00000  0.00000  1.30000
    $end
    
    $rem
       CORRELATION           CCSD
       BASIS                 6-311(3+)G*
       PURECART              2222          6d, will be required for ezDyson
       EOM_IP_ALPHA          [0,0,0,1,0,0,0,0]  (Ag,B1g,B2g,B3g,Au,B1u,B2u,B3u)
       EOM_EA_BETA           [0,0,0,1,0,0,0,0]  (Ag,B1g,B2g,B3g,Au,B1u,B2u,B3u)
       CCMAN2                true
       CC_DO_DYSON           true
       CC_TRANS_PROP         true          necessary for Dyson orbitals job
       PRINT_GENERAL_BASIS   true          will be required for ezDyson
    $end
    ```

???+ example "Example 7.173: Dyson orbitals for ionization of formaldehyde from the first excited state
AND from the ground state."
    ```qchem
    $molecule
       0 1
       O     1.535338855      0.000000000     -0.438858006
       C     1.535331598     -0.000007025      0.767790994
       H     1.535342484      0.937663512      1.362651452
       H     1.535342484     -0.937656488      1.362672535
    $end
    
    $rem
       CORRELATION           CCSD
       BASIS                 6-31G*
       PURECART              2222    6d, will be required for ezDyson
       CCMAN2                true    new Dyson code
       EE_STATES             [1]
       EOM_IP_ALPHA          [1]
       EOM_IP_BETA           [1]
       CC_TRANS_PROP         true    necessary for Dyson orbitals job
       CC_DO_DYSON           true
       PRINT_GENERAL_BASIS   true    will be required for ezDyson
    $end
    ```

???+ example "Example 7.174: Dyson orbitals for core ionization of Li atom use Li ${}^{+}$ as a reference, get
neutral atom via EOM-EA get 1st excitation for the cation via EOM-EE totally:
core ionization AND 1st ionization of Li atom."
    ```qchem
    $molecule
       +1 1
       Li   0.00000  0.00000  0.00000
    $end
    
    $rem
       CORRELATION            CCSD
       BASIS                  6-311+G*
       PURECART               2222          6d, will be required for ezDyson
       CCMAN2                 true          new Dyson code
       EE_STATES              [1,0,0,0,0,0,0,0]
       EA_STATES              [1,0,0,0,0,0,0,0]
       EOM_NGUESS_SINGLES     5             to converge to the lowest EA state
       CC_TRANS_PROP          true          necessary for Dyson orbitals job
       CC_DO_DYSON            true
       PRINT_GENERAL_BASIS    true          will be required for ezDyson
    $end
    ```

???+ example "Example 7.175: Dyson orbitals for ionization of CH ${}_{2}$ from high-spin triplet reference and
from the lowest SF state."
    ```qchem
    $molecule
       0 3
       C
       H  1 rCH
       H  1 rCH 2 aHCH
    
       rCH    = 1.1167
       aHCH   = 102.07
    $end
    
    $rem
       CORRELATION           CCSD
       BASIS                 6-31G*
       SCF_GUESS             core
       CCMAN2                true    new Dyson code
       CC_SYMMETRY           false
       SF_STATES             [1]
       EOM_IP_ALPHA          [2]     one should be careful to request
       EOM_EA_BETA           [2]     meaningful spin for EA/IP state(s)
       CC_TRANS_PROP         true    necessary for Dyson orbitals job
       CC_DO_DYSON           true
       IQMOL_FCHK            true    generate formatted checkpoint file for IQMol
    $end
    ```

???+ example "Example 7.176: Dyson orbitals for ionization of SO ${}^{-}$ using EOM-EA
to describe the anion states and EOM-SF to describe
the neutral; both sets of EOM states are generated
using neutral triplet reference."
    ```qchem
    $comment
    SO-, calculating Dyson orbitals using EOM-EA to describe
    the anion states and EOM-SF to describe the neutral;
    both sets of EOM states are generated using triplet reference.
    $end
    
    $molecule
    0 3
    S    0.0000000    0.0000000   -0.5241891
    O    0.0000000    0.0000000    1.0676951
    $end
    
    $rem
    JOBTYPE¯¯¯SP
    METHOD¯          ¯EOM-CCSD
    BASIS                  ¯6-31G*
    PURECART¯¯111 needed for ezDyson
    EA_BETA¯¯        [0,0,0,1]  anion state
    SF_STATES               [2,2,0,0]  neutral states
    CC_DO_DYSON¯¯true
    CC_TRANS_PROP¯¯true
    PRINT_GENERAL_BASIS¯true  needed for ezDyson
    $end
    
    $trans_prop
    state_list
    ea_beta   4 1      !state 1
    sf_states 1 1    !state 2
    sf_states 1 2    !state 3
    sf_states 2 1
    sf_states 2 2
    end_list
    state_pair_list
    1 2   ! transition 1 <-> 2
    1 3
    1 4
    1 5
    end_pairs
    calc dyson
    $end
    
    ```

???+ example "Example 7.177: Calculation of overlap between Dyson orbital of HCl- computed with EOM-EA and plane wave
for a fixed direction of k."
    ```qchem
    $comment
    Computes coupling between a Dyson orbital and a plane wave for HCl-
    for fixed direction of k-vector: k = [1,1,1] (no averaging) and
    for 6 values of |k|.
    $end
    
    $molecule
    0 1
    H 0 0 0
    Cl 0 0 1.60
    $end
    
    $rem
    basis 6-31+G*
    method eom-ccsd
    ea_states = [1,0,0,0]
    CC_DO_DYSON true
    DYSON_PW_COUPLING true
    $end
    
    $free_electron
    k_x  100  ! the value of kx is  1
    k_y  100  ! the value of ky is  1
    k_z  100  ! the value of kz is  1
    k_grid_points 6  !Coupling will be calculated for 6 |k|-values
    $end
    
    ```

???+ example "Example 7.178: Calculation of overlap between Dyson orbital of N2- computed with EOM-EA and plane wave
averaged over k-orientations."
    ```qchem
    $comment
    Computes coupling betwee a Dyson orbital of N2- and a plane wave with
    averaging over k-directions
    $end
    
    
    $molecule
    0 1
    N 0 0 0
    N 0 0 1.42
    $end
    
    $rem
    basis 6-31+G*
    method eom-ccsd
    CC_DO_DYSON true
    EA_STATES = [0,0,1,0,0,0,0,0]
    DYSON_PW_COUPLING true
    $end
    
    
    $free_electron
    k_avg  1        !perform averaging over k-orientations using default grid
    k_grid_points 6  !Coupling will be calculated for |k|-values  from 0.0 eV to 0.1x(k_grid_points -1)
    $end
    
    ```
