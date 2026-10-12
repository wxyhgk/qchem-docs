---
title: "10.2.12 General Excited-State Analysis"
---

## 10.2.12 General Excited-State Analysis

(July 4, 2026)

**Q-Chem** features a module for extended excited-state analysis via the wave function analysis library **libwfa**.[[1096]](../bib_references/bib.md#bib1146)
**libwfa** is interfaced to the ADC, CC/EOM-CC, CIS, and TDDFT/SF-TDDFT
methods. These analyses are based on the state, transition
and difference density matrices of the excited states. The theoretical
background for such analysis is given in Chapter [7.13](../ch07_excited/sec_ES_visual.md).
A more extended discussion of different analysis methods and classification schemes for excited states
can be found elsewhere,

 as can a review of visualization tools and charge-transfer metrics for
TDDFT calculations.[[572]](../bib_references/bib.md#bib586)

| Descriptor | Explanation |
| --- | --- |
| Leading singular values | Largest NTO occupation numbers |
| Sum of singular values (Omega) | $\Omega=\\|\bm{\gamma}^{\text{IF}}\\|^{2}$ , sum of NTO occupation numbers |
| E(h) | Energy of hole NTO, $E_{I}(\text{h})=\sum_{pq}\alpha_{pI}F_{pq}\alpha_{qI}$ |
| E(p) | Energy of particle NTO, $E_{I}(\text{p})=\sum_{pq}\beta_{pI}F_{pq}\beta_{qI}$ |
| PR_NTO | NTO participation ratio $\mbox{PR}_{\text{NTO}}$ |
| Entanglement entropy (S_HE) | $S_{H\|E}=-\sum_{i}\lambda_{i}\log_{2}\lambda_{i}$ |
| Nr of entangled states (Z_HE) | $Z_{HE}=2^{S_{H\|E}}$ |
| Renormalized S_HE/Z_HE | Replace $\lambda_{i}\rightarrow\lambda_{i}/\Omega$ in the above two formulas |
| <Phe> | Expectation value of the particle-hole permutation |
|  | operator, measuring de-excitations [[686]](../bib_references/bib.md#bib711) |
| <r_h> [Ang] | Mean position of hole $\langle\vec{x}_{\text{h}}\rangle_{\text{exc}}$ |
| <r_e> [Ang] | Mean position of electron $\langle\vec{x}_{\text{e}}\rangle_{\text{exc}}$ |
| \|<r_e - r_h>\| [Ang] | Electron–hole distance, $\vec{d}_{\text{e-h}}=\\|\langle\vec{x}_{\text{e}}-\vec{x}_{\text{h}}\rangle\\|$ |
| Hole size [Ang] | RMS hole size: $\sigma_{\text{h}}=(\langle\vec{x}_{\text{h}}^{\,2}\rangle_{\text{exc}}-\langle\vec{x}_{\text{h}}\rangle_{\text{exc}}^{2})^{1/2}$ |
| Electron size [Ang] | RMS elec. size: $\sigma_{\text{e}}=(\langle\vec{x}_{\text{e}}^{\,2}\rangle_{\text{exc}}-\langle\vec{x}_{\text{e}}\rangle_{\text{exc}}^{2})^{1/2}$ |
| RMS electron-hole separation [Ang] | $d_{\text{exc}}=\big{(}\big{\langle}\\|\vec{x}_{\text{e}}-\vec{x}_{\text{h}}\\|^{2}\big{\rangle}_{\text{exc}}\big{)}^{1/2}$ |
| Charge-displacement metric 1 | $d_{\text{CD1}}=d_{\text{e-h}}+\|\sigma_{\text{h}}-\sigma_{\text{e}}\|$ |
| Charge-displacement metric 2 | $d_{\text{CD2}}=d_{\text{e-h}}-\tfrac{1}{2}\big{(}\sigma_{\text{h}}+\sigma_{\text{e}}\big{)}$ |
| Charge-displacement metric 3 | $d_{\text{CD3}}=d_{\text{e-h}}+d_{\text{exc}}$ |
| Covariance(r_h, r_e) [Ang^2] | $\mbox{COV}\left(\vec{x}_{\text{h}},\vec{x}_{\text{e}}\right)=\langle\vec{x}_{\text{h}}\bm{\cdot}\vec{x}_{\text{e}}\rangle_{\text{exc}}-\langle\vec{x}_{\text{h}}\rangle_{\text{exc}}\bm{\cdot}\langle\vec{x}_{\text{e}}\rangle_{\text{exc}}$ |
| Correlation coefficient | $R_{\text{eh}}=\mbox{COV}\left(\vec{x}_{\text{h}},\vec{x}_{\text{e}}\right)/\sigma_{\text{h}}\bm{\cdot}\sigma_{\text{e}}$ |
| Center-of-mass size | $\tfrac{1}{2}\big{(}\big{\langle}\\|\vec{x}_{\text{e}}+\vec{x}_{\text{h}}\\|^{2}\big{\rangle}_{\text{exc}}-\langle\vec{x}_{\text{e}}+\vec{x}_{\text{h}}\rangle_{\text{exc}}^{2}\big{)}^{1/2}$ |

Table 10.1: 
Descriptors output by **Q-Chem** for transition density matrix analysis. Note
that squares of the singular values, which correspond to the weights of the respective NTO
pairs, are printed. $\Omega$ equals the square of the norm of the one-electron transition density matrix (1TDM).
The charge-displacement metrics $d_{\text{CD}n}$ are defined in Ref. [[563]](../bib_references/bib.md#bib587)
.

One-electron transition-density matrix (1TDM) based analyses include the construction and
export of natural transition orbitals (NTOs),[[913]](../bib_references/bib.md#bib947)

electron and hole densities,[[1099]](../bib_references/bib.md#bib1142)

evaluation of charge transfer numbers,[[1097]](../bib_references/bib.md#bib1141)

analysis of exciton multipole moments,[[74]](../bib_references/bib.md#bib43)

and quantification of electron–hole entanglement.[[1100]](../bib_references/bib.md#bib1145)

The NTOs are obtained by singular value decomposition (SVD) of the 1TDM:[[572]](../bib_references/bib.md#bib586)

<a id="A3.S8.EGx77"></a>

$$
\displaystyle\gamma^{\text{IF}}_{pq} \tag{10.34}
$$

where $\bm{\sigma}$ is diagonal matrix containing singular values and unitary
matrices $\bm{\alpha}$ and $\bm{\beta}$ contain the respective particle and hole
NTOs. Note that:

<a id="Ch10.E36"></a>

$$
\|\bm{\gamma}\|^{2}=\sum_{pq}\gamma_{pq}^{2}=\sum_{K}\sigma_{K}^{2}\equiv\Omega \tag{10.36}
$$

Furthermore, the formation and export of state-averaged NTOs, and the
decomposition of the excited states into transitions of state-averaged NTOs are
implemented.[[1099]](../bib_references/bib.md#bib1142)
 The difference and/or state densities
can be exported themselves, as well as employed to construct and export natural
orbitals, natural difference orbitals, and attachment and detachment
densities.[[572]](../bib_references/bib.md#bib586)
 Furthermore, two measures of unpaired
electrons are computed.[[546]](../bib_references/bib.md#bib560)
 In addition, a Mulliken or
Löwdin population analysis and an exciton analysis can be performed based on
the difference/state densities.[[572]](../bib_references/bib.md#bib586)
 The main descriptors of the various
analyses that are printed for each excited state are given in
Tables [10.1](#table:TDM-analysis) and [10.2](#table:density-analysis).
Detailed descriptions with illustrative examples can be found
elsewhere.[[1099]](../bib_references/bib.md#bib1142)

Note that these descriptions are invariant to orbital rotations,
unlike some standard metrics for charge-transfer analysis that are discussed in
Section [7.3.2](../ch07_excited/sec_CT-metrics.md).[[563]](../bib_references/bib.md#bib587)

| Descriptor | Explanation |
| --- | --- |
| n_u | Number of unpaired electrons $n_{\text{u}}=\sum_{i}\mbox{min}(n_{i},2-n_{i})$ |
| n_u,nl | Number of unpaired electrons $n_{\text{u,nl}}=\sum_{i}n_{i}^{2}(2-n_{i})^{2}$ |
| PR_NO | NO participation ratio $\mbox{PR}_{\text{NO}}$ |
| p_D and p_A | Promotion number $p_{\text{D}}$ and $p_{\text{A}}$ |
| PR_D and PR_A | D/A participation ratio $\mbox{PR}_{\text{D}}$ and $\mbox{PR}_{\text{A}}$ |
| <r_h> [Ang] | Mean position of detachment density $\vec{d}_{\text{D}}$ |
| <r_e> [Ang] | Mean position of attachment density $\vec{d}_{\text{A}}$ |
| \|<r_e - r_h>\| [Ang] | Linear D/A distance $\vec{d}_{\text{D}\to\text{A}}=\vec{d}_{\text{A}}-\vec{d}_{\text{D}}$ |
| Hole size [Ang] | RMS size of detachment density $\sigma_{\text{D}}$ |
| Electron size [Ang] | RMS size of attachment density $\sigma_{\text{A}}$ |

Table 10.2: 
Descriptors output by **Q-Chem** for difference/state density matrix analysis.

**libwfa** also computes descriptors for differentiating between diradical and ionic excited states, as defined within valence-bond theory.
These descriptors, denoted `LOC`, `LOCa`, `QT`, and `QTa`, are zero for perfect diradical states and increase with the ionic character of the state.[[341]](../bib_references/bib.md#bib355)

To activate any excited-state analysis STATE_ANALYSIS has to be set
to TRUE. For individual analyses there is currently only a limited
amount of fine grained control. The construction and export of any type of
orbitals is controlled by MOLDEN_FORMAT to export the orbitals as
**MolDen** files, and NTO_PAIRS which specifies the number of
important orbitals to print (note that the same keyword controls the number of
natural orbitals, the number of natural difference orbitals, and the number of
NTOs to be printed). Setting MAKE_CUBE_FILES to TRUE
triggers the construction and export of densities in “cube file”
format

, which requires the specification of the *$plots*
section in either old or new format (see Sections [10.5.4](sect_plot.mo.md) and
[10.5.5](sec_cubefiles.md) for details).
Setting IQMOL_FCHK = TRUE (equivalently, GUI = 2)
will export data to the “`.fchk`” formatted checkpoint file, and
switches off the generation of cube files. The population analyses are
controlled by POP_MULLIKEN and LOWDIN_POPULATION. Setting
the latter to TRUE will enforce Löwdin population analysis to be
employed for regular populations as well as CT numbers,
while by default the Mulliken population analysis is used.

Any **MolDen** or cube files generated by the excited state analyses can be
found in the directory `plots` in the job’s scratch directory. Their names
always start with a unique identifier of the excited state (the exact form of
this human readable identifier varies with the excited state method). The
names of **MolDen** files are then followed by either `_no.mo`,
`_ndo.mo`, or `_nto.mo` depending on the type of orbitals they
contain. In case of cube files the state identifier is followed by
`_dens`, `_diff`, `_trans`, `_attach`, `_detach`,
`_elec`, or `_hole` for state, difference, transition, attachment,
detachment, electron, or hole densities, respectively. All cube files have the
suffix `.cube`. In unrestricted calculations an additional part is added
to the file name before `.cube` which indicates $\alpha$ (`_a`) or
$\beta$ (`_b`) spin. The only exception is the state density for which
`_tot` or `_sd` are added indicating the total or spin-density parts
of the state density.
Analysis of relaxed CIS or TDDFT densities can be triggered by
CIS_RELAXED_DENSITY = TRUE.
The corresponding output files are marked by `_rlx`.
Computation of ESPs for state, transition, and electron/hole densities (see Ref. [[686]](../bib_references/bib.md#bib711)
) can be
triggered by setting ESP_GRID = $-3$.
These are indicated by `_esp` as part of the file name.

The `ctnum_*.om` file created in the main directory serves as input
for a charge transfer number analysis, as explained, *e.g.*, in
Refs. [[1097]](../bib_references/bib.md#bib1141)
. Use the
external `TheoDORE` program (`theodore-qc.sourceforge.net`) to
create electron/hole correlation plots and to compute fragment based descriptors.

!!! note "Note"
    - When doing excited-state calculations from an open-shell reference, **libwfa** will perform the analysis for both $\alpha\alpha$ and $\beta\beta$ transition
    densities. Make sure you look at the correct one. The way to figure it out is
    to remember that in open-shell references $N_{\alpha}>N_{\beta}$, *e.g.*, in
    doublet references, the unpaired electron is $\alpha$ and the hole is $\beta$.
    Thus, for transitions of the unpaired electron into the unoccupied orbitals
    you need $\alpha\alpha$ block, whereas for the transitions from doubly occupied orbitals
    into the singly unoccupied orbital (the hole) you need the $\beta\beta$ block.

    - To activate all types of analyses in CCMAN2 jobs, you have to activate CC_REF_PROP,
    CC_EOM_PROP, and CC_TRANS_PROP.
    This is shown in Example [7.9.30](../ch07_excited/ex_eomip-wfa.md).

    - In Hermitian formalisms, $\gamma^{\text{IF}}$ is a Hermitian conjugate
    of $\gamma^{\text{FI}}$, but in non-Hermitian approaches, such as
    coupled-cluster theory, the two are slightly different. While for quantitative
    interstate properties both $\gamma^{\text{IF}}$ and $\gamma^{\text{FI}}$ are
    computed, the qualitative trends in exciton properties derived from
    $(\gamma^{\text{IF}})^{\dagger}$ and $\gamma^{\text{FI}}$ are very similar. Only
    one 1TDM is analyzed for EOM-CC.

    - In spin-restricted calculations, the **libwfa** module computes NTOs for
    the $\alpha\alpha$ block of transition density. Thus, when computing NTOs for
    the transitions between open-shell EOM-IP/EA states make sure to specify
    correct spin states. For example, use EOM_EA_ALPHA to visualize
    transitions involving the extra electron.


### `STATE_ANALYSIS`

> **Triggers the general state analysis via libwfa .**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not run excited state analysis.
>     * `TRUE`: Activate excited state analysis.
> * **Recommendation**: This analysis produces only minimal computational overhead (as long as no cube files are produced) and can be activated whenever some additional information about the excited state is required.

### `WFA_LEVEL`

> **Master variable for controlling the amount of output produced by libwfa .**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * `1`: Only perform some population analyses.
>     * `2`: Also perform exciton analysis and compute natural (transition/difference) orbitals.
>     * `3`: Also perform charge transfer number analysis.
>     * `4`: Maximal output including cube files for NTOs (this is needed to reproduce Ref.
>     * `686`: Kimber P., Plasser F. Phys. Chem. Chem. Phys. (2020) ,
>     * `22`: , pp. 6058 . Link )
> * **Recommendation**: Reduce if you want less print-out.

### `NTO_PAIRS`

> **Controls how many hole/particle NTO pairs and frontier natural orbital pairs and natural difference orbital pairs are printed in the standard output.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $N$: Write $N$ NTO/NO/NDO pairs per excited state.
> * **Recommendation**: This controls the print-out to the standard output. Use WFA_ORB_THRESH if you want to modify the number of orbitals exported.

### `WFA_ORB_THRESH`

> **Controls the number of hole/particle NTO pairs and frontier natural orbital pairs and natural difference orbital pairs exported to the Molden files.**
>
> * **Type**: `INTEGER`
> * **Default**: `3`
> * **Options**:
>     * $N$: Export all NTO/NO/NDO pairs with a weight above $10^{-N}$ .
### `WFA_REF_STATE`

> **Controls the reference state for the transition and difference density matrices used by libwfa . This keyword works for CIS/TDDFT/SF-TDDFT computations. Use CC_STATE_TO_OPT for EOM-CC.**
>
> * **Type**: `INTEGER`
> * **Default**: `-1`
> * **Options**:
>     * `-1`: Use default: ground-state for standard CIS/TDDFT computations, first response state for SF-TDDFT.
>     * `0`: Reference state
>     * `N`: $N$ th excited state/response state.
> * **Recommendation**: NONE

???+ example "Example 10.7: Basic excited-state analysis example for formaldehyde at the ADC(2)/def2-SV(P) level:
computation of various descriptors and output of NOs, NTOs, and NDOs in MolDen format. libwfa used in this basic mode does usually not add notable computational cost."
    ```qchem
    $molecule
       0 1
       C     0.000000   0.000000    0.523383
       O    -0.000000   0.000000   -0.671856
       H     0.931138   0.000000    1.11728
       H    -0.931138   0.000000    1.11728
    $end
    
    $rem
       METHOD           adc(2)
       BASIS            def2-sv(p)
       N_FROZEN_CORE    fc
       EE_SINGLETS      [0,1,1,0]
       STATE_ANALYSIS   true
       MOLDEN_FORMAT    true
    $end
    ```

???+ example "Example 10.8: Analysis of two TDDFT excited states of formaldehyde using libwfa including output of cube files.
This uses the new $plots format (see Section 10.5.4.1 ) with grid points specified.
The cubes files of HOMO and LUMO will also be generated."
    ```qchem
    $molecule
    0 1
      C    0.0000000   -0.0000000   -0.6133791
      O   -0.0000000    0.0000000    0.6060734
      H    0.0000000    0.9391300   -1.1555819
      H    0.0000000   -0.9391300   -1.1555819
    $end
    
    $rem
       METHOD           PBE0
       BASIS            6-31+G(d)
       CIS_N_ROOTS      2
       CIS_TRIPLETS     false
       MAKE_CUBE_FILES  true
       PLOTS            true
       STATE_ANALYSIS   true
    $end
    
    $plots
       grid_points                    50 50 50
       alpha_molecular_orbital        8-9
    $end
    ```

!!! note "Note"
    For the output of orbitals and densities it is possible to use either the MOLDEN_FORMAT = TRUE
    (see Example 10.2.12),
    MAKE_CUBE_FILES = TRUE
    (see Example 10.2.12),
    or GUI = 2 options.
    These options are mutually exclusive when STATE_ANALYSIS is activated.


???+ example "Example 10.9: Uracil computed at the PBE0/def2-SV(P) level. Activation of extended libwfa functionality including export of NTOs and densities in cube format and computation of the ESPs of these densities.
This extended libwfa mode can add significant computational cost, especially if a fine grid is chosen."
    ```qchem
    $molecule
       0 1
       C    1.194380    1.102510    0.000000
       C   -0.008366    1.692430    0.000000
       N   -1.169600    0.978035    0.000000
       C   -1.212060   -0.402293    0.000000
       N    0.034691   -0.979140    0.000000
       C    1.281590   -0.348737    0.000000
       O   -2.243420   -1.023750    0.000000
       O    2.299180   -0.995854    0.000000
       H   -0.123160    2.767140    0.000000
       H   -2.061440    1.444100    0.000000
       H    0.044818   -1.989990    0.000000
       H    2.104720    1.679840    0.000000
    $end
    
    $rem
       METHOD            pbe0
       BASIS             def2-sv(p)
       CIS_N_ROOTS       4
       CIS_SINGLETS      true
       CIS_TRIPLETS      true
       RPA               false
       STATE_ANALYSIS    true
       NTO_PAIRS         3
       MAKE_CUBE_FILES   true
       ESP_GRID          -3
       WFA_LEVEL         4
       WFA_ORB_THRESH    3
    $end
    
    $plots
    Write cube files for all 4 states
    35  -3.5  3.5
    35  -3.5  3.5
    15  -1.5  1.5
    0  4  0  0
    1 2 3 4
    $end
    ```

Other examples of **libwfa** uses:

- Example [7.3.4.2](../ch07_excited/sect_sftddft.md#ex:MRSFDFT) illustrates wave-function analysis of the SF-DFT
states in para-benzyne;
- Example [7.9.9.2](../ch07_excited/sub_cvs_eom.md#ex:cvsee1) illustrates wave-function analysis of XAS transitions
within CVS-EOM-EE;
- Example [7.9.30](../ch07_excited/ex_eomip-wfa.md) illustrates wave-function analysis for transitions between EOM-IP states;
- Example [7.9.19](../ch07_excited/ex_CAPlibwfa.md) illustrates wave-function analysis of complex-valued densities
within CAP-EOM-CCSD.
