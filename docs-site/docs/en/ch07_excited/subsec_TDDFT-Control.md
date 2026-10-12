---
title: "7.3.6 Job Control for TDDFT"
---

## 7.3.6 Job Control for TDDFT

(July 4, 2026)

## 7.3.6.1 Basic Settings

Input for time-dependent density functional theory calculations follows very
closely the input already described for the uncorrelated excited state methods
described in the previous section (in particular, see
Section [7.2.4](sec_CIS-jobcontrol.md)). There are several points to be aware of:

- The exchange and correlation functionals are specified exactly as for a
ground state DFT calculation, through EXCHANGE and
CORRELATION. To active TDDFT, set CIS_N_ROOTS to a value $\geq 1$,
specifying the number of excited states to compute.
- If RPA is set to TRUE, a “full” TDDFT calculation
will be performed, however the default value is RPA = FALSE,
which invokes the TDA,[[580]](../bib_references/bib.md#bib602)
 in which the de-excitation
amplitudes $\mathbf{y}$ in Eq. ([7.15](sect_tddftintro.md#eq:TDDFT)) are neglected, which is usually a
good approximation for excitation energies, although oscillator strengths
within the TDA no longer formally satisfy the Thomas-Reiche-Kuhn sum
rule.

 For RPA = TRUE, a TDA calculation
is performed first and used as the initial guess for the full TDDFT
calculation. The TDA calculation can be skipped altogether using
RPA = 2. RPA is not implemented for restricted open-shell
calculations, only TDA.
- If SPIN_FLIP is set to 1 (or TRUE) or 2
when performing a TDDFT
calculation, a SF-TDDFT calculation will be performed. At present,
SF-TDDFT is only implemented within the TDA so RPA must be set
to FALSE. Remember to set the spin multiplicity to 3 for
systems with an even-number of electrons (*e.g.*, diradicals), and
4 for odd-number electron systems (*e.g.*, triradicals). MR-SFTDDFT (invoked by
SPIN_FLIP=2)
is only implemented for triplet references.
- If MGGA_GINV is set to 1 when performing a TDDFT
calculation, gauge invariance correction will be added to meta-GGA
functionals.[[84]](../bib_references/bib.md#bib69)

Some basic job control variables (to be added to the *$rem* section) are described below.
There are additional options for x-ray spectroscopy; see Section [7.12.2](subsec_TDDFT-Xray.md).

### `CIS_SINGLETS`

> **Controls whether to compute singlet excited states.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `FALSE`: Do not compute singlet excitations.
>     * `TRUE`: Compute singlet excitations.
> * **Recommendation**: This option makes sense only for a singlet ground state, since the use of an open-shell ground state does not afford spin-pure excited states.

### `CIS_TRIPLETS`

> **Controls whether to compute triplet excited states.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `FALSE`: Do not compute triplet excitations.
>     * `TRUE`: Compute triplet excitations.
> * **Recommendation**: This option makes sense only for a singlet ground state, since the use of an open-shell ground state does not afford spin-pure excited states.

### `SPIN_FLIP`

> **Selects whether to perform a standard excited state calculation, or a spin-flip calculation. Spin multiplicity should be set to 3 for systems with an even number of electrons, and 4 for systems with an odd number of electrons.**
>
> * **Type**: `INEGER`
> * **Default**: `0`
> * **Options**:
>     * `1`: Do original SF-TDDFT.
>     * `2`: Do MRSF-TDDFT.
> * **Recommendation**: None

### `MGGA_GINV`

> **Controls whether to add gauge invariance correction to meta-GGA functionals.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: No correction.
>     * `1`: Add gauge invariance correction to meta-GGA functionals.
> * **Recommendation**: Not recommended when TDA is used because the TDA violates gauge invariance.

### `WANG_ZIEGLER_KERNEL`

> **Controls whether to use the Wang-Ziegler non-collinear exchange-correlation kernel in a SF-TDDFT calculation. Set NEW_DFT = TRUE if using a Q-Chem version older than 5.0.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not use non-collinear kernel.
>     * `TRUE`: Use non-collinear kernel.
> * **Recommendation**: None

### `CIS_GUESS_TYPE`

> **Controls how to generate the initial guess excitation vectors in CIS/TDA/RPA calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Generate $N$ (no. of roots requested) occupied $\to$ virtual single orbital transitions according to their orbital energy difference order (from low to high). This is the common scenario.
>     * `1`: Generate $N-1$ occupied $\to$ virtual single orbital transitions according to their orbital energy difference order (from low to high), and generate another guess excitation vector consist of all the remaining single orbital transitions in the occupied $\to$ virtual transition space with equal weights.
>     * `2`: Generate $N$ occupied/virtual single orbital transitions according to their orbital energy difference order (from low to high), and generate one more guess excitation vector consist of all the remaining single orbital transitions in the occupied $\to$ virtual transition space with equal weights.
> * **Recommendation**: The default setting should work for most of the cases. However, when the number of roots is small, in some CIS/TDA/RPA calculations, low energy excited states could be missing. The options = 1 or 2 may remedy this root missing issue by sampling more vectors in the transition space. Setting = 1 or 2 may take more cycles to converge in the Davidson iteration, but the results are expected to be more reliable. Currently, = 1 or 2 are not supported in SF-XCIS calculations. Setting TRNSS = TRUE also disables the setting of .

## 7.3.6.2 Options for Charge-Separation Metrics

The charge-separation metrics $\Lambda$, $\Delta r$, $\Delta\sigma$, and $\Gamma$ can be computed (for each TDDFT excited state),
and in both the canonical and NTO representations, by setting CIS_CT_METRICS = TRUE. Some additional options
are described below. For **libwfa** job control (*e.g.*, to compute the recommended metrics $d_{\text{e-h}}$, $d_{\text{exc}}$, and $d_{\text{CD1}}$),
see Section [10.2.12](../ch10_properties/ex_StateAnal_MolDen.md).

### `CIS_CT_METRICS`

> **Controls whether to compute the charge-separation metrics $\Lambda$ , $\Delta r$ , $\Delta\sigma$ , and $\Gamma$ (Section 7.3.2 ).**
>
> * **Type**: `INTEGER`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not compute these metrics.
>     * `TRUE`: Compute all four metrics (for each excited state), in both the canonical and NTO representations.
> * **Recommendation**: Request if desired. (There is some overhead associated with computing $\Lambda$ , but it should be small.)

### `SPATIAL_OVERLAP_METRIC`

> **Controls whether $O_{ia}$ or $\tilde{O}_{ia}$ is used to evaluate $\Lambda$ in Eq. ( 7.16 ).**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: Compute $\Lambda$ using $O_{ia}$ .
>     * `2`: Compute $\Lambda$ using $\tilde{O}_{ia}$ .
> * **Recommendation**: Option 1 represents the original metric suggested by Tozer and co-workers in Ref. 1057 Peach M. J. G. et al. J. Chem. Phys. (2008) , 128 , pp. 044118 . Link .

### `SPATIAL_OVERLAP_GRID`

> **Controls the grid that is used to evaluate $O_{ia}$ or $\tilde{O}_{ia}$ in Eq. ( 7.17 ).**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: Use a EML grid with $N_{r}=300$ and $N_{\Omega}=302$ .
>     * `2`: Use a EML grid with $N_{r}=400$ and $N_{\Omega}=434$ .
> * **Recommendation**: None.

### `SPATIAL_OVERLAP_PRINT`

> **Controls whether to print the spatial overlaps $O_{ia}$ or $\tilde{O}_{ia}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not print the $O_{ia}$ .
>     * `1`: Print the frontier overlaps only (5 occupied and 5 virtual orbitals.
>     * `2`: Print all of the $O_{ia}$ .
> * **Recommendation**: These may be useful for a posteriori analysis of the spatial proximity of various MOs; however, option 2 will engender significant printing for large molecules. Whether it is $O_{ia}$ [Eq. ( 7.17 )] or $\tilde{O}_{ia}$ [Eq. ( 7.18 )] that is printed depends upon the setting of SPATIAL_OVERLAP_ANAL .

## 7.3.6.3 Options for a Truncated Subspace

The following options can be used to implement the reduced excitation space that was described in Section [7.3.3](subsec_TRNSS.md).

### `CISTR_PRINT`

> **Controls level of output.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Increase output level.
> * **Recommendation**: None

### `CUTOCC`

> **Specifies occupied orbital cutoff.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * `0-200`: Use a cutoff of /100
> * **Recommendation**: None

### `CUTVIR`

> **Specifies virtual orbital cutoff.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0-100`: CUTOFF = CUTVIR/100
> * **Recommendation**: None

### `N_SOL`

> **Specifies number of atoms or orbitals in the $solute or $alist section.**
>
> * **Type**: `INTEGER`
> * **Default**: `No default.`
> * **Options**:
>     * `User defined.`
> * **Recommendation**: Reads from either the $solute or $alist input section.

### `TRNSS`

> **Controls whether reduced single excitation space is used.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Use reduced excitation space.
> * **Recommendation**: None

### `TRTYPE`

> **Controls how reduced subspace is specified.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: Select orbitals localized on a set of atoms.
>     * `2`: Specify a set of orbitals.
>     * `3`: Specify a set of occupied orbitals, include excitations to all virtual orbitals.
> * **Recommendation**: None

## 7.3.6.4 Job Control for EA-TDDFT

Like NOCIS/STEX/1C-NOCIS, the options for the EA-TDDFT/EA-CIS
method are controlled via the *$nocis* section after NOCIS is set to TRUE in *$rem*.

### `NOCIS`

> **Requests a NOCIS/STEX/1C-NOCIS/EA-TDDFT calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not run these methods.
>     * `TRUE`: Run one of these methods, options controlled in $nocis .
> * **Recommendation**: None

The options below are set within the *$nocis* section.

### `NUM_REF`

> **Sets the number of reference orbitals in a NOCIS/STEX/1C-NOCIS/EA-TDDFT calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$: Positive integer
> * **Recommendation**: Set according to the number of consecutive orbitals of interest for the calculation. For example, for the oxygen K-edge in CO ${}_{\text{2}}$ , the number of references would be 2 (two oxygen 1s orbitals), whereas for the carbon K-edge it would be 1 (one carbon 1s).

### `ORB_OFFSET`

> **Determines the starting orbital for a NOCIS/STEX/1C-NOCIS/EA-TDDFT calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$: Positive integer
> * **Recommendation**: Set according to the first orbital of interest in the system in question. For example, this would be set to 0 for the oxygen K-edge in CO ${}_{\text{2}}$ because the two O(1s) orbitals lie below the C(1s), so for the carbon K-edge this would be set to 2.

### `LOCALIZE_ORBITALS`

> **Choose which core orbitals to localize with the Boys objective function. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `$-1$`
> * **Options**:
>     * $n$: Integer, normally positive.
> * **Recommendation**: Set to $-1$ to skip Boys localization entirely, or set to a value greater than NUM_REF to include more orbitals in the preliminary localization, otherwise use the default.

### `SUBSYSTEM_ATOMS`

> **Choose which atoms to consider for an EA-TDDFT calculation. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * List of integers delimited by spaces:: $i\ j\ k$ …
> * **Recommendation**: Use only if excitations out of a particular subset of atoms is of interest and the definition of ORB_OFFSET and NUM_REF is nontrivial. This is an expert option, and should only be used in specific situations such as isolating the oxygen K-edge of all water molecules at the air/water interface.

### `DSCF_ALGORITHM`

> **Sets the $\Delta$ SCF algorithm to be used in the optimization of the core-ionized reference determinants. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `MOM`
> * **Options**:
>     * `MOM, IMOM, STEP, or STEP_MOM`
> * **Recommendation**: Use MOM unless convergence issues arise. IMOM occasionally provides improved convergence, but the combination of STEP and MOM used by the STEP_MOM option is particularly robust. In rare cases, STEP may be necessary, but this is not recommended as the number of SCF cycles required is quite large. If STEP_MOM is requested, the option STEP_MOM_START must also be set.

### `STEP_MOM_START`

> **Sets the SCF cycle on which the STEP algorithm stops and the MOM algorithm starts. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: Positive integer.
> * **Recommendation**: For best results, set such that STEP reaches a convergence threshold of at least $10^{-4}$ a.u. before switching to MOM, but if MOM continues to collapse or oscillate, then wait until tighter convergence is achieved to switch algorithms.

### `REF_SCF_ALGORITHM`

> **Sets the SCF algorithm for the core-ion reference calculations. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `DIIS`
> * **Options**:
>     * DIIS, GDM, GDM_LS, SGM, or SGM_LS
> * **Recommendation**: Use DIIS for MOM, IMOM, STEP, or STEP_MOM calculations, but if these algorithms are not providing satisfactory convergence to the desired core-ion state, this can be set to SGM or SGM_LS.

### `REF_SCF_CONVERGENCE`

> **Sets SCF convergence threshold for the core-ion reference calculations. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `Same as`
> * **Options**:
>     * $n$: Positive integer
> * **Recommendation**: None

### `REF_SCF_GUESS`

> **Initial guess for core-ion reference calculations. INPUT SECTION: $nocis**
>
> * **Type**: `STRING`
> * **Default**: `Koopman`
> * **Options**:
>     * Read (the Koopmans guess is automatically used if no option is specified)
> * **Recommendation**: The default core-ion guess is generated by removing an electron from the core orbital using the ground-state MO coefficients (Koopmans guess). Alternatively, when convergence issues arise it may be useful to run an EA-TDDFT job with a different functional ( i.e. , LDA or GGA), then read the converged core-ion orbitals into a subsequent EA-TDDFT job with the functional of interest ( i.e. , a range-separated hybrid).

### `EA_TDA`

> **Invokes EA-TDDFT within the Tamm-Dancoff approximation. INPUT SECTION: $nocis**
>
> * **Type**: `NONE`
> * **Default**: `NONE`
> * **Options**:
>     * The presence of this keyword will activate: .
> * **Recommendation**: This is the most cost-effective form of the EA-TDDFT equations and has almost no effect on results for K-edge XAS.

### `EA_RPA`

> **Solves the full EA-TDDFT equations. INPUT SECTION: $nocis**
>
> * **Type**: `NONE`
> * **Default**: `NONE`
> * **Options**:
>     * The presence of this keyword will activate: .
> * **Recommendation**: No recommendation.

### `SINGLETS`

> **Compute only singlets. INPUT SECTION: $nocis**
>
> * **Type**: `NONE`
> * **Default**: `NONE`
> * **Options**:
>     * The presence of this keyword without the: Triplets keyword will compute singlets without computing triplets.
> * **Recommendation**: No recommendation.

### `TRIPLETS`

> **Compute only triplets. INPUT SECTION: $nocis**
>
> * **Type**: `NONE`
> * **Default**: `NONE`
> * **Options**:
>     * The presence of this keyword without the: Singlets keyword will compute triplets without computing singlets.
> * **Recommendation**: No recommendation.

### `N_ROOTS`

> **Sets the number of roots to print. INPUT SECTION: $nocis**
>
> * **Type**: `INTEGER`
> * **Default**: `All`
> * **Options**:
>     * $n$: where $n<m_{\rm{roots}}$
> * **Recommendation**: No recommendation. Beware that unlike CIS/TDDFT jobs this keyword only prints fewer roots, but the entirety of the Hamiltonian is still diagonalized via direct diagonalization.

### `PRINT_NTOS`

> **Prints natural transition orbitals to cube files for each root that is printed via the N_ROOTS keyword. INPUT SECTION: $nocis**
>
> * **Type**: `NONE`
> * **Default**: `NONE`
> * **Options**:
>     * The presence of this keyword automatically generates: all NTOs (default), or N_ROOTS NTOs.
> * **Recommendation**: No recommendation, but one should be sure to also include a $plots section with appropriate details such that the cube files can be generated.

???+ example "Example 7.12: EA-TDDFT with Tamm-Dancoff approximation for the K-edge of NH ${}_{3}$ .
This job truncates the number of printed (singlet) roots to 10.
The core-ion SCF will use the SGM algorithm."
    ```qchem
    $rem
    method          rCAM-B3LYP
    rel_x2c         true
    basis           aug-cc-pCVDZ
    nocis           true
    scf_convergence 8
    thresh          14
    integral_symmetry    false
    point_group_symmetry false
    $end
    
    $nocis
    n_roots         10
    orb_offset      0
    num_ref         1
    singlets
    ea_tda
    ref_scf_algorithm sgm
    $end
    
    $molecule
    0 1
    N   0.0000   0.0000   0.1163
    H   0.0000   0.9399  -0.2713
    H   0.8140  -0.4700  -0.2713
    H  -0.8140  -0.4700  -0.2713
    $end
    ```

???+ example "Example 7.13: Full EA-TDDFT for the K-edge of NH ${}_{3}$ . The core-ion SCF will use the default MOM algorithm."
    ```qchem
    $rem
    method          rCAM-B3LYP
    rel_x2c         true
    scf_convergence 8
    basis           aug-cc-pCVDZ
    nocis           true
    thresh          14
    integral_symmetry    false
    point_group_symmetry false
    $end
    
    $nocis
    n_roots         10
    orb_offset      0
    num_ref         1
    singlets
    ea_rpa
    $end
    
    $molecule
    0 1
    N   0.0000   0.0000   0.1163
    H   0.0000   0.9399  -0.2713
    H   0.8140  -0.4700  -0.2713
    H  -0.8140  -0.4700  -0.2713
    $end
    ```
