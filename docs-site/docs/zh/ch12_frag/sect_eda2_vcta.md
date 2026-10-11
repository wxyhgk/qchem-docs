---
title: "12.6.8 ALMO-EDA with Non-Perturbative Polarization and Charge Transfer Analysis"
---

## 12.6.8 ALMO-EDA with Non-Perturbative Polarization and Charge Transfer Analysis

(July 4, 2026)

**Q-Chem** also supports the non-perturbative [[1396]](../bib_references/bib.md#bib1457)
 (variational) energy and
charge decomposition analysis in the second-generation ALMO-EDA framework through the eda2 driver. The advantage
of this method over the perturbative CT analysis method is that the energy and charge
decompositions are both exact and there are no higher-order terms left. Currently, this method is
implemented for both restricted and unrestricted SCF calculations, and is eligible to analyze both
polarization [[1249]](../bib_references/bib.md#bib1301)
 (POL) and charge transfer (CT) processes of intermolecular interactions.
The non-perturbative POL and CT analysis can be invoked by setting EDA_POL_A = TRUE and
EDA_VCT_A = TRUE, respectively. The POL analysis [[1249]](../bib_references/bib.md#bib1301)
 uses the recently developed
fragment density matrix connecting method and can break the energy lowering and charge shift in the POL process into
exactly fragment-wise additive sums. The CT analysis will print out the pairwise energy and charge changes between fragments
as matrices, with fragment labels starting from 1, following the orders in the Q-Chem fragment input. The
interpretation is that the energy lowering and charge transfer happens due to electron donation from the fragments labeled
in the rows to the fragments labeled in the columns.

The default orbital analysis method is the complementary occupied-virtual pairs (COVP) method. To select the significant COVPs,
set EDA_COVP_THRESH = $N$ to print out the COVPs that contributes more than $0.001\times N$ kJ/mol to the energy
decrease, and the default value is set to 500. To visualize the COVPs, set EDA_SAVE_COVP = TRUE,
MAKE_CUBE_FILES = TRUE and PLOTS = TRUE to save the orbitals as cube files, which can
be visualized using IQmol, VMD, or other visualization software. The natural orbitals for chemical valence (NOCV) analysis can also be
performed by setting EDA_NOCV = TRUE. To select the significant NOCVs, set EDA_NOCV_THRESH = $N$
to print out NOCVs that contributes more than $0.001\times N$ kJ/mol to energy decrease, and the default value is also set to 500.
The NOCV analysis includes the POL process, CT process, and the traditional NOCV results which combine the POL and CT processes.
As pointed out in this paper [[1250]](../bib_references/bib.md#bib1300)
, the ETS-NOCV method approximates the effective Fock matrix integration with only one quadrature,
which is set by EDA_NOCV_QUADRATURE =1, and **Q-Chem** also supports 5-quadratures for systems with significant density changes.
As an improvement upon the NOCVs, the recently proposed occupied-virtual orbitals for chemical valence (OVOCV) [[1248]](../bib_references/bib.md#bib1302)
 can also be used
to analyse the CT step. The OVOCVs block-diagonalize the density difference operator into 2 $\times$ 2 blocks, which are spanned by one level
that is filled in the initial state (the occupied OVOCV) and one that is empty (the virtual OVOCV), making them much easier to interpret than
the NOCVs. For a more detailed introduction to OVOCV analysis, we refer the users to [10.3.4](../ch10_properties/sect_ovocv-analysis.md). To enable OVOCV analysis,
set OVOCV_ANALYSIS = 1 and OVOCV_THRESH = $N$ to print out the OVOCVs that contributes
more than $0.001\times N$ kJ/mol to the energy decrease.

Unrestricted analysis will be used if at least one of the fragments has an open-shell structure. It can also be forced by setting
UNRESTRICTED=TRUE.

EDA_POL_A

### `EDA_POL_A`

> **Perform EDA for polarization process**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not perform EDA for polarization process
>     * TRUE
>     * Perform EDA for polarization process
> * **Recommendation**: Set to TRUE to perform EDA for polarization process

EDA_VCT_A

### `EDA_VCT_A`

> **Perform non-perturbative CT analysis**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not perform non-perturbative CT analysis
>     * TRUE
>     * Perform non-perturbative CT analysis.
> * **Recommendation**: Set to TRUE to perform non-perturbative CT analysis

EDA_COVP_THRESH

### `EDA_COVP_THRESH`

> **Specifies the significance above which the COVPs will be saved**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * $N$
>     * COVPs that contributes more than
>     * $0.001\times N$
>     * kJ/mol in energy decrease will be saved
> * **Recommendation**: None

EDA_SAVE_COVP

### `EDA_SAVE_COVP`

> **Save significant COVPs or not**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not save significant COVPs
>     * TRUE
>     * Save significant COVPs
> * **Recommendation**: Set to TRUE to save COVPs. Note that REMs for plotting cube files need also be set

EDA_NOCV

### `EDA_NOCV`

> **Perform NOCV analysis**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not do NOCV analysis
>     * TRUE
>     * Do NOCV analysis
> * **Recommendation**: None

EDA_NOCV_THRESH

### `EDA_NOCV_THRESH`

> **Specifies the significance above which the NOCVs will be saved**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * $N$
>     * NOCVs that contributes more than
>     * $0.001\times N$
>     * kJ/mol in energy decrease will be saved
> * **Recommendation**: None

EDA_SAVE_NOCV

### `EDA_SAVE_NOCV`

> **Save significant NOCVs or not**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not save significant NOCVs
>     * 1
>     * Save significant NOCVs
> * **Recommendation**: Set to 1 to save NOCVs. Note REMs for plotting cube files need also be set

EDA_NOCV_QUADRATURE

### `EDA_NOCV_QUADRATURE`

> **Number of quadratures used to integrate effective fock matrix**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * 1
>     * Use 1 quadrature
>     * 5
>     * Use 5 quadratures
> * **Recommendation**: Most of the time, one quadrature is enough. However, in cases where the NOCV energy decreases are very different from the corresponding COVP results, it is recommended to increase the quadrature numbers.

OVOCV_ANALYSIS

### `OVOCV_ANALYSIS`

> **Perform OVOCV analysis**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * FALSE
>     * Do not do OVOCV analysis
>     * TRUE
>     * Do OVOCV analysis
> * **Recommendation**: None

OVOCV_THRESH

### `OVOCV_THRESH`

> **Specifies the significance above which the OVOCVs will be saved**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * $N$
>     * OVOCVs that contributes more than
>     * $0.001\times N$
>     * kJ/mol in energy decrease will be saved
> * **Recommendation**: None

SAVE_OVOCV

### `SAVE_OVOCV`

> **Save significant OVOCVs or not**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * 0
>     * Do not save significant OVOCVs
>     * 1
>     * Save significant OVOCVs
> * **Recommendation**: Set to 1 to save OVOCVs. Note REMs for plotting cube files need also be set

???+ example "Example 12.20: Restricted EDA calculation for the H ${}_{2}$ O-Na ${}^{+}$ system with non-perturbative POL and CT analysis."
    ```qchem
    $molecule
    1 1
    --
    0 1
    H         -0.73946        0.94887        0.78379
    O         -1.16910        0.63297       -0.02844
    H         -2.12156        0.70793        0.14730
    --
    1 1
    Na        -0.17266       -0.04338       -1.86190
    $end
    
    $comment
    EDA2 (R) calculation with variational POL and CT analyses
    based on the eda2 driver
    $end
    
    $rem
    jobtype              eda
    eda2                 1
    method               B3LYP
    scf_print_frgm       1
    basis                6-31G*
    scf_algorithm        diis
    thresh               12
    incfock              false
    mem_total            16000
    scf_convergence      7
    scf_final_print      2
    eda_pol_a            1
    eda_vct_a            1
    eda_covp_thresh      500
    eda_save_covp        0
    make_cube_files      true
    plots                true
    point_group_symmetry false
    integral_symmetry    false
    $end
    
    $plots
     grid_points 50 50 50
    $end
    
    ```

???+ example "Example 12.21: Unrestricted EDA calculation for the CH ${}_{3}$ -Na ${}^{+}$ system with non-perturbative POL and CT analysis."
    ```qchem
    $molecule
    1 2
    --
    0 2
    C¯-1.447596 -0.000023  0.000019
    H¯-1.562749  0.330361 -1.023835
    H¯-1.561982  0.721445  0.798205
    H¯-1.561187 -1.052067  0.225866
    --
    1 1
    Na¯ 1.215591  0.000036 -0.000032
    $end
    
    $comment
    EDA2 (U) calculation with variational POL and CT analyses
    based on the eda2 driver
    $end
    
    $rem
    jobtype              eda
    eda2                 1
    method               B3LYP
    scf_print_frgm       true
    basis                aug-cc-PVTZ
    scf_algorithm        diis
    thresh               12
    incfock              false
    mem_total            16000
    scf_convergence      7
    eda_pol_a            1
    eda_vct_a            1
    eda_covp_thresh      500
    eda_save_covp        0
    make_cube_files      true
    plots                true
    point_group_symmetry false
    integral_symmetry    false
    $end
    
    $plots
     grid_points 50 50 50
    $end
    
    ```

???+ example "Example 12.22: Unrestricted EDA calculation for the Rn ${}^{+}$ -CH ${}_{4}$ system with non-perturbative POL and CT analysis and NOCV analysis"
    ```qchem
    $molecule
    1 2
    --
    0 1
    C         0.0551597051    0.0364080371   -0.0375528310
    H        -0.0563410694   -1.0144740143   -0.3153331540
    H        -0.0537558345    0.7868509829   -0.8318467516
    H        -0.8718690962    0.2438110339    0.5677588397
    H         1.0408273042    0.1810559688    0.4109829953
    --
    1 2
    Rn       -0.2646060092    0.6373989916    3.0026329017
    $end
    
    $rem
    jobtype             eda
    eda2                1
    method              b3lyp
    scf_print_frgm      1
    basis               def2-tzvp
    ecp                 def2-ecp
    scf_algorithm       diis
    thresh              12
    incfock             0
    mem_total           16000
    scf_final_print     2
    iprint              20000000
    scf_convergence     7
    eda_pol_a           1
    eda_vct_a           1
    eda_save_covp       0
    eda_nocv            1
    eda_save_nocv       0
    eda_covp_thresh     500
    eda_nocv_thresh     500
    eda_nocv_quadrature 1
    make_cube_files     true
    plots               true
    point_group_symmetry false
    integral_symmetry    false
    $end
    
    $plots
     grid_points 100 100 100
    $end
    
    ```

???+ example "Example 12.23: Restricted EDA calculation for the ethene- $[\text{PtCl}_{3}]^{-}$ system with non-perturbative POL and CT analysis.
OVOCV analysis is enabled for CT analysis."
    ```qchem
    $molecule
    -1 1
    --
    0 1
    C      -2.1241906261     0.4405879048    -0.6028769327
    H      -2.2759080470     0.1247332923    -1.6303256895
    H      -2.2970177347     1.4883974948    -0.3784045735
    C      -2.1383367135    -0.5060266611     0.4271962891
    H      -2.3004855320    -1.5544440597     0.1975704475
    H      -2.3216355550    -0.1916949240     1.4498166705
    --
    -1 1
    Pt     -0.1374350284    -0.0292366293    -0.0576671311
    Cl     -0.1541352882    -1.7330117528    -1.6304294395
    Cl      2.1808813192    -0.0260821423    -0.0234510188
    Cl     -0.2063937942     1.6741234771     1.5139773781
    $end
    
    $rem
    jobtype              eda
    eda2                 1
    eda_bsse             0
    method               wb97x-v
    scf_print_frgm       1
    sym_ignore           1
    symmetry             false
    basis                def2-svp
    ecp                  def2-ecp
    scf_algorithm        diis
    thresh               14
    incfock              0
    mem_total            16000
    scf_final_print      2
    scf_convergence      8
    eda_pol_a            1
    eda_vct_a            1
    eda_covp_thresh      10000
    eda_save_covp        0
    eda_nocv             1
    eda_save_nocv        0
    eda_nocv_thresh      10000
    eda_nocv_quadrature  5
    ovocv_analysis       1
    ovocv_thresh         10000
    save_ovocv           0
    make_cube_files      true
    plots                true
    $end
    
    $plots
    grid_points 50 50 50
    $end
    
    ```
