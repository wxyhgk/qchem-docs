---
title: "10.3.4 Occupied–Virtual Orbitals for Chemical Valence Analysis"
---

## 10.3.4 Occupied–Virtual Orbitals for Chemical Valence Analysis

(July 4, 2026)

## 10.3.4.1 Overview

In mean-field theory such as HF and KS-DFT, the energy of a quantum state is completely determined by the 1-PDM **P**. Therefore, the energy difference between any two quantum states can be completely determined by the density difference $\Delta\textbf{P}$. Insightful interpretations about the orbital interactions can be obtained from the eigen-decomposition of $\Delta\textbf{P}$, which gives the so-called natural orbitals for chemical valence (NOCV)[[954]](../bib_references/bib.md#bib995)
. The NOCVs appear in pairs $\{|\psi_{\pm i}\rangle\}$ with associated eigenvalues $\pm\lambda_{i}$. However, the NOCVs are mixtures of occupied and virtual orbitals, which makes them hard to interpret; in addition, the associated charge of each NOCV pair is erroneously large[[1250]](../bib_references/bib.md#bib1300)
. An improvement over NOCV is the recently proposed occupied-virtual orbitals for chemical valence (OVOCV) [[1248]](../bib_references/bib.md#bib1302)
, whose construction is summarized below.

## 10.3.4.2 OVOCV analysis between any two single-determinant states

In the orthonormal basis of occupied and virtual orbitals of initial state $I$, the matrix representation of $\hat{P}_{I}$ is

<a id="eq:P_I"></a>

$$
{\color[rgb]{0,0,0}P_{I}}=\begin{pmatrix}1&0\\
0&0\end{pmatrix} \tag{10.52}
$$

where $1$ is $o\times o$ and the diagonal 0 matrix is $v\times v$ in dimension. Under the same basis, the representation of the final density operator $P_{F}$ can be constructed from $P_{I}$ as $P_{F}=\exp\{X\}P_{I}\exp\{-X\}$, where

<a id="Ch10.E53"></a>

$$
X=\begin{pmatrix}0&X_{ov}\\
-X_{ov}^{T}&0\end{pmatrix} \tag{10.53}
$$

With the SVD of $X_{ov}$,

<a id="Xov_SVD"></a>

$$
X_{ov}=U\Sigma V^{T} \tag{10.54}
$$

where $\dim(U)=o\times o,\dim(\Sigma)=o\times v,\dim(V)=v\times v$, we can write $\Delta P$ as

<a id="eq:delta_p"></a>

$$
\Delta P=\begin{pmatrix}U&0\\
0&V\end{pmatrix}\begin{pmatrix}-\sin^{2}{\Sigma^{\prime}}&-\cos{\Sigma^{\prime}}\sin{\Sigma^{\prime}}&0\\
-\sin{\Sigma^{\prime}}\cos{\Sigma^{\prime}}&\sin^{2}{\Sigma^{\prime}}&0\\
0&0&0\end{pmatrix}\begin{pmatrix}U^{T}&0\\
0&V^{T}\end{pmatrix} \tag{10.55}
$$

where $\Sigma^{\prime}=\mathrm{diag}(\sigma_{1},\sigma_{2},...,\sigma_{o})$, and the diagonal 0 matrix is of dimension $v-o$ (assuming $o<v$, which is the case for most practical calculations).

Since $\Delta P$ is rendered diagonal in each of its blocks in the $U,V$ representation, it is natural to define this choice as the Occupied-Virtual Orbitals for Chemical Valence (OVOCVs).

<a id="A3.S8.EGx78"></a>

$$
\displaystyle|\phi^{i}_{\text{occ}}\rangle \tag{10.56}
$$

Specifically, $|\phi^{i}_{\text{occ}}\rangle$ and $|\phi^{i}_{\text{vir}}\rangle$ are the occupied and virtual orbitals of the $i$th OVOCV pair. Since the OVOCVs are obtained by unitary transformations of an orthonormal basis, they still form an orthonormal basis (with a much smaller dimension, as the virtual orbitals irrelevant to the density deformation are deleted).

In the OVOCV basis, $\Delta P$ is:

<a id="eq:delta_p_ovocv"></a>

$$
\Delta P=\begin{pmatrix}-\sin^{2}{\Sigma^{\prime}}&-\cos{\Sigma^{\prime}}\sin{\Sigma^{\prime}}\\
-\sin{\Sigma^{\prime}}\cos{\Sigma^{\prime}}&\sin^{2}{\Sigma^{\prime}}\end{pmatrix} \tag{10.58}
$$

The (diagonal) oo block is negative semi-definite, corresponding to $\sin^{2}\sigma_{i}$ electron loss from the $i\text{th}$ of $o$ initially occupied OVOCV levels. By contrast the (diagonal) vv block is equal and opposite, corresponding to promotion of $\sin^{2}\sigma_{i}$ electrons into the $i\text{th}$ of $o$ initially virtual OVOCV levels.

The energy difference between any two single-determinant states can be obtained as

<a id="Ch10.E59"></a>

$$
\Delta E=\text{Tr}\{\hat{F}^{\text{eff}}\Delta\hat{P}\}, \tag{10.59}
$$

where $\hat{F}^{\text{eff}}$ is an effective fock operator obtained from a line-integral over the density matrices between the two states. Using the decomposition of $\Delta\hat{P}$ in OVOCV basis, we have

<a id="Ch10.E60"></a>

$$
\displaystyle\Delta E \tag{10.60}
$$

The OVOCV analysis is coded for the spin polarized calculations, so UNRESTRICTED = TRUE must be set.

### `OVOCV_ANALYSIS`

> **Perform OVOCV analysis**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not do OVOCV analysis
>     * `1`: Do OVOCV analysis
> * **Recommendation**: None

### `OVOCV_QUADRATURE`

> **Number of quadrature points used for the line-integral of $\hat{F}^{\text{eff}}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * `-1`: Printings for debug purpose
>     * `5`
>     * `5 quadratures`
>     * `9`
>     * `9 quadratures`
>     * `13`
>     * `13 quadratures`
>     * `17`
>     * `17 quadratures`
>     * `21`
>     * `21 quadratures`
> * **Recommendation**: Use 5 for ground state analysis, 9 or 13 for excited state analysis. Increase quadrature numbers to get higher accuracy in $\Delta E$

### `SAVE_OVOCV_INIT_DATA`

> **Saves initial state for OVOCV analysis**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not save initial state data
>     * `1`: Save initial state data
> * **Recommendation**: Set to 1 at the initial state calculation

### `LOAD_OVOCV_INIT_DATA`

> **Load initial state for OVOCV analysis, then do OVOCV analysis using current state as the final state**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not load initial state data
>     * `1`: Load initial state data
> * **Recommendation**: Set to 1 at the final state calculation

### `OVOCV_THRESH`

> **Specifies the significance above which the OVOCVs will be saved**
>
> * **Type**: `INTEGER`
> * **Default**: `500`
> * **Options**:
>     * $N$: OVOCVs that contributes more than $0.001\times N$ kJ/mol in energy decrease will be saved
> * **Recommendation**: None

### `SAVE_OVOCV`

> **Save significant OVOCVs or not**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not save significant OVOCVs
>     * `1`: Save significant OVOCVs
> * **Recommendation**: Set to 1 to save OVOCVs. Note REMs for plotting cube files need also be set

???+ example "Example 10.10.16: OVOCV analysis between a polarized state and the fully converged SCF state."
    ```qchem
    $comment
    Calculate a polarized state
    $end
    
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
    unrestricted        true
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
    frgm_method          stoll
    child_mp             true
    child_mp_orders      232
    ovocv_analysis       1
    save_ovocv_init_data 1
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
    unrestricted        true
    thresh              14
    scf_convergence     8
    scf_algorithm       diis
    method              wb97x-v
    basis               def2-svp
    ecp                 def2-ecp
    scf_guess           read
    sym_ignore          true
    symmetry            false
    make_cube_files     true
    plots               1
    ovocv_analysis      1
    load_ovocv_init_data 1
    ovocv_quadrature    5
    ovocv_thresh        10000
    save_ovocv            0
    $end
    
    $plots
    grid_points 50 50 50
    $end
    ```

???+ example "Example 10.10.17: OVOCV analysis between a DFT state with HF density and the DFT state with DFT density."
    ```qchem
    $comment
    SCF for fragmo to get initial density for HF
    $end
    
    $molecule
    1 2
    --
    0 1
    He 0 0 0
    --
    1 2
    He 0 0 3.0
    $end
    
    $rem
    method              hf
    scf_guess           fragmo
    frgm_method         stoll
    scf_convergence     7
    basis               6-31G**
    scf_algorithm       gdm
    sym_ignore          true   #make sure symmetry is off
    symmetry            false
    internal_stability  true
    unrestricted        true
    $end
    
    @@@
    
    $comment
    HF calculation with frag density
    $end
    
    $molecule
    read
    $end
    
    $rem
    method              hf
    scf_guess           read
    scf_convergence     7
    basis               6-31G**
    scf_algorithm       gdm
    sym_ignore          true   #make sure symmetry is off
    symmetry            false
    internal_stability  true
    unrestricted        true
    ovocv_analysis      1
    save_ovocv_init_data 1
    $end
    
    @@@
    
    $comment
    DFT calculation with HF density
    $end
    
    $molecule
    read
    $end
    
    $rem
    internal_stability  true
    unrestricted        true
    thresh              14
    scf_convergence     7
    scf_algorithm       gdm
    method              PBE
    basis               6-31G**
    scf_guess           read
    scf_max_cycles      500
    sym_ignore          true
    symmetry            false
    IQMOL_FCHK          False
    make_cube_files     true
    plots               1
    ovocv_analysis      1
    load_ovocv_init_data 1
    ovocv_quadrature    17
    ovocv_thresh        500
    save_ovocv            0
    $end
    
    $plots
    grid_points 50 50 50
    $end
    ```

## 10.3.4.3 OVOCV analysis for OO-DFT excitation analysis

With the development of SCF algorithms for non-aufbau determinants, it is often possible to accurately represent an excited state, such as a charge-transfer state or a doubly excited state, with a single Slater determinant using Orbital-Optimized Density Functional Theory (OO-DFT). It is therefore natural to analyze the electronic excitation using the OVOCV method[[1247]](../bib_references/bib.md#bib1303)
, which gives a primary excitation due to a single (or double for double excitation) OVOCV pair $|\psi_{\text{D}}\rangle$ (donor) and $|\psi_{\text{A}}\rangle$ (acceptor), together with many polarized pairs to account for the orbital relaxation effect.
To reveal the importance of orbital relaxations, we introduce an intermediate frozen state (FRZ), whose density is constructed from the complete depletion of donor orbital $|\psi_{\text{D}}\rangle$ and the complete occupation of acceptor orbital $|\psi_{\text{A}}\rangle$, starting from the ground state density $\hat{P}_{\text{G}}$:

<a id="Ch10.E61"></a>

$$
\hat{P}_{\text{FRZ}}=\hat{P}_{\text{G}}-|\psi_{\text{D}}\rangle\langle\psi_{\text{D}}|+|\psi_{\text{A}}\rangle\langle\psi_{\text{A}}|. \tag{10.61}
$$

As a result, the connection between $\hat{P}_{\text{G}}$ and $\hat{P}_{\text{FRZ}}$ reveals the primary excitation, and the connection between $\hat{P}_{\text{FRZ}}$ and $\hat{P}_{\text{E}}$ reveals the orbital relaxation effect.

### `OVOCV_EXCITE_ANALYSIS`

> **Perform OVOCV analysis for OO-DFT excitation analysis**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not do OVOCV OO-DFT analysis
>     * `1`: Do OVOCV OO-DFT analysis
> * **Recommendation**: None

### `OVOCV_EXCITE_TYPE`

> **Specify the excitation type to construct the intermediate FRZ state**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: Construct FRZ state using the largest OVOCV pair in $\alpha$ space
>     * `2`: Construct FRZ state using the largest OVOCV pair in $\beta$ space
>     * `3`: Construct FRZ state using the largest OVOCV pair in both $\alpha$ and $\beta$ space (for double excitation)
> * **Recommendation**: Use 1 or 2 for single excitation, 3 for double excitation

???+ example "Example 10.10.18: OVOCV OO-DFT analysis for long distance charge transfer between NH ${}_{3}$ and F ${}_{2}$ ."
    ```qchem
    $molecule
    0 1
    N     0.000000000     0.000000000     -2.149985070
    H     -0.469826010     -0.813762490     -2.534400940
    H     -0.469826010     0.813762490     -2.534400940
    H     0.939652030     0.000000000     -2.534400940
    F     0.000000000     0.000000000     15.850014930
    F     0.000000000     0.000000000     17.275484090
    $end
    
    $comment
    IMOM we use for TRIPLET EXCITATIONS or MIXED-SPIN configurations
    $end
    
    $rem
    thresh              14
    scf_convergence     8
    method              hf
    basis               def2-TZVP
    scf_algorithm       diis_gdm
    sym_ignore          true   #make sure symmetry is off
    symmetry            false
    XC_GRID             50000194
    unrestricted        true
    ovocv_analysis      1
    save_ovocv_init_data 1
    $end
    
    @@@
    
    $rem
    unrestricted        true
    thresh              14
    scf_convergence     6
    method              hf
    basis               def2-TZVP
    mom_method          imom
    mom_start           1
    scf_guess           read
    scf_max_cycles      500
    sym_ignore          true
    symmetry            false
    XC_GRID             50000194
    make_cube_files     true
    plots               1
    ovocv_analysis      1
    load_ovocv_init_data 1
    ovocv_quadrature    9
    ovocv_thresh        15000
    ovocv_excite_analysis 1
    ovocv_excite_type     1
    save_ovocv            0
    $end
    
    $molecule
    read
    $end
    
    $occupied
    1 2 3 4 5 6 7 8 9 10 11 12 13 15
    1 2 3 4 5 6 7 8 9 10 11 12 13 14
    $end
    
    $plots
    grid_points 50 50 50
    $end
    
    ```

???+ example "Example 10.10.19: OVOCV OO-DFT analysis for LMCT in Fe(H ${}_{2}$ O) ${}^{3+}_{6}$ ."
    ```qchem
    $molecule
    +3 6
    --
    +3 6
    Fe     -0.5022247054     1.2927779200     0.0001938411
    --
    0 1
    H       2.1134166395     2.0808631740    -0.0009010689
    H      -0.5027205697    -1.3235141738    -0.7847973080
    H      -3.1183219511     2.0796505928    -0.0004236834
    H       0.2840444564     1.2933014045     2.6166394903
    H      -0.5027751731     3.9101762183     0.7846214605
    O       1.5358193871     1.2947592260    -0.0014374082
    H       2.1156949943     0.5103151332    -0.0009786075
    O      -0.5019595039     3.3312830798    -0.0005116891
    H      -0.5019009551     3.9098531329    -0.7858415694
    O      -0.5013746615     1.2930914301     2.0381118720
    H      -1.2864874118     1.2932385232     2.6170717164
    O      -2.5401948736     1.2938974534     0.0009627059
    H      -3.1195714968     0.5090879007     0.0019042859
    O      -0.5018840213    -0.7448372467     0.0005186723
    H      -0.5008290080    -1.3235744599     0.7857827770
    O      -0.5020354665     1.2915906981    -2.0378380237
    H       0.2835925140     1.2915440728    -2.6160740707
    H      -1.2869601935     1.2917959205    -2.6170203924
    $end
    
    $rem
    jobtype             sp
    method              wb97x-v
    basis               def2-tzvp
    scf_max_cycles      1000
    scf_algorithm       gdm
    sym_ignore          true
    symmetry            false
    thresh              14
    scf_convergence     7
    unrestricted        true
    ovocv_analysis      1
    save_ovocv_init_data 1
    $end
    
    @@@
    
    $molecule
    +3 6
    --
    +2 5
    Fe     -0.5022247054     1.2927779200     0.0001938411
    --
    +1 2
    H       2.1134166395     2.0808631740    -0.0009010689
    H      -0.5027205697    -1.3235141738    -0.7847973080
    H      -3.1183219511     2.0796505928    -0.0004236834
    H       0.2840444564     1.2933014045     2.6166394903
    H      -0.5027751731     3.9101762183     0.7846214605
    O       1.5358193871     1.2947592260    -0.0014374082
    H       2.1156949943     0.5103151332    -0.0009786075
    O      -0.5019595039     3.3312830798    -0.0005116891
    H      -0.5019009551     3.9098531329    -0.7858415694
    O      -0.5013746615     1.2930914301     2.0381118720
    H      -1.2864874118     1.2932385232     2.6170717164
    O      -2.5401948736     1.2938974534     0.0009627059
    H      -3.1195714968     0.5090879007     0.0019042859
    O      -0.5018840213    -0.7448372467     0.0005186723
    H      -0.5008290080    -1.3235744599     0.7857827770
    O      -0.5020354665     1.2915906981    -2.0378380237
    H       0.2835925140     1.2915440728    -2.6160740707
    H      -1.2869601935     1.2917959205    -2.6170203924
    $end
    
    $rem
    jobtype             sp
    scf_guess           fragmo
    FRGM_METHOD         STOLL
    SCF_PRINT_FRGM      TRUE
    method              wb97x-v
    basis               def2-tzvp
    scf_max_cycles      1000
    scf_algorithm       gdm
    sym_ignore          true
    symmetry            false
    thresh              14
    scf_convergence     7
    unrestricted        true
    $end
    
    $rem_frgm
    SCF_CONVERGENCE     5
    SCF_ALGORITHM       DIIS_GDM
    THRESH              14
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
    jobtype             sp
    method              wb97x-v
    basis               def2-tzvp
    scf_guess           read
    mom_method          imom
    mom_start           1
    sym_ignore          true
    symmetry            false
    thresh              14
    scf_convergence     7
    scf_max_cycles      2000
    unrestricted        true
    make_cube_files     true
    plots               1
    ovocv_analysis      1
    load_ovocv_init_data 1
    ovocv_quadrature    9
    ovocv_thresh        20000
    ovocv_excite_analysis 1
    ovocv_excite_type     2
    save_ovocv            0
    $end
    
    $plots
    grid_points 50 50 50
    $end
    
    ```

???+ example "Example 10.10.20: OVOCV OO-DFT analysis for double excitation in trans-butadiene."
    ```qchem
    $molecule
    0 1
    C       1.7631203268    -0.4019108032    -0.3481693109
    C       0.6037765052     0.2512052721    -0.3293638273
    C      -0.6037682643    -0.2511908395     0.3294491374
    C      -1.7631216007     0.4019093543     0.3482256846
    H      -2.6370356062    -0.0041538614     0.8460657302
    H      -1.8733953929     1.3678634226    -0.1376167636
    H       2.6369974511     0.0040901125    -0.8461249062
    H       1.8735775331    -1.3675549056     0.1382472290
    H      -0.5187645613    -1.2176355085     0.8243565706
    H       0.5187966092     1.2176897568    -0.8241975438
    $end
    
    $rem
    method              wB97X-V
    basis               def2-tzvp
    scf_algorithm       diis_gdm
    sym_ignore          true   #make sure symmetry is off
    symmetry            false
    max_scf_cycles      200
    unrestricted        true
    ovocv_analysis      1
    save_ovocv_init_data 1
    $end
    
    @@@
    
    $rem
    unrestricted        true
    method              wB97X-V
    basis               def2-tzvp
    scf_guess           read
    scf_max_cycles      1000
    mom_method          imom
    mom_start           1
    sym_ignore          true
    symmetry            false
    make_cube_files     true
    plots               1
    ovocv_analysis      1
    load_ovocv_init_data 1
    ovocv_quadrature    9
    ovocv_thresh        1000
    ovocv_excite_analysis 1
    ovocv_excite_type     3
    save_ovocv            0
    $end
    
    $molecule
    read
    $end
    
    $occupied
    1:14 16
    1:14 16
    $end
    
    $plots
    grid_points 50 50 50
    $end
    
    ```
