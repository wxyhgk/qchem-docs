---
title: "7.3.10 Spin-Orbit Coupling"
---

## 7.3.10 Spin-Orbit Coupling

(July 4, 2026)

The following sections describe two different ways to include spin-orbit couplings (SOCs) into TDDFT calculations.

## 7.3.10.1 SOCs Between TDDFT States

There are several levels at which SOCs can be incorporated into TDDFT:[[713]](../bib_references/bib.md#bib745)

1. (i)

one-electron part of the Breit-Pauli Hamiltonian,
2. (ii)

one-electron SOC using scaled nuclear charges, and
3. (iii)

full SOC using the mean-field treatment of the two-electron part.[[1103]](../bib_references/bib.md#bib1151)

Options (i) and (ii) are
are available for both TDA and RPA variants (including TDHF and CIS states), for restricted Kohn-Sham references only.
Option (iii) is available for both restricted and unrestricted variants, but only within TDA.
Calculations of SOC for SF-TDDFT (both standard and MR-SFTDDFT) are also possible within TDA using option (iii).
A Python code is available,[[882]](../bib_references/bib.md#bib1655) which harvests SOCs along with TDDFT energies and oscillator
strengths from the **Q-Chem** output and uses them to construct and diagonalize the Breit-Pauli Hamiltonian,
to obtain the coupled states.[[881]](../bib_references/bib.md#bib916)
 It can be used to compute L- and M-edge spectra for TDDFT, CIS, and
DFT/CIS methods.

The implementation of one-electron SOC, options (i) and (ii), is based on the following.
The SOCs are computed by evaluating matrix elements of the one-electron part of the Breit-Pauli Hamiltonian:

<a id="eq:HSO_Breit_Pauli"></a>

$$
\hat{H}_{\text{SO}}=-\frac{\alpha_{0}^{2}}{2}\sum_{i,A}\frac{Z_{A}}{r^{3}_{iA}}\left(\mathbf{r}_{iA}\times\mathbf{p}_{i}\right)\bm{\cdot}\mathbf{s}_{i} \tag{7.38}
$$

where $i$ denotes electrons, $A$ denotes nuclei, $\alpha_{0}=1/137.037$ is
the fine structure constant, and $Z_{A}$ is the bare positive charge on nucleus $A$.
In the second quantization representation, the spin-orbit Hamiltonian in different directions can be expressed as

<a id="Ch7.E39"></a>

$$
\displaystyle\hat{H}_{\text{SO},x} \tag{7.39a}
$$

where $\hat{\tilde{L}}_{\alpha}=\hat{L}_{\alpha}r^{-3}$ for $\alpha\in\{x,y,z\}$ and
$\tilde{L}_{\alpha,pq}$ are the matrix elements of this operator. The single-reference *ab initio*
excited states (within the TDA) are given by

<a id="Ch7.E40"></a>

$$
\displaystyle\big{|}\Phi^{I}_{\text{singlet}}\big{\rangle} \tag{7.40a}
$$

where $s^{Ia}_{i}$ and $t^{Ia}_{i}$ are singlet and triplet excitation coefficients of the $I$th singlet or triplet state respectively, with the normalization

<a id="Ch7.E41"></a>

$$
\sum_{ia}(s^{Ia}_{i})^{2}=\sum_{ia}(t^{Ia}_{i})^{2}=\frac{1}{2}\;. \tag{7.41}
$$

The quantity $|\Phi_{\text{HF}}\rangle$ refers to the Hartree-Fock ground state. Thus the SOC constant from the
singlet state to different triplet manifolds are

<a id="Ch7.E42"></a>

$$
\big{\langle}\Phi^{I}_{\text{singlet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=0}_{\text{triplet}}\big{\rangle}=\frac{\alpha_{0}^{2}\hbar}{2}\left(\sum_{i,a,b}\tilde{L}_{z,ab}\;s^{Ia}_{i}\;t^{Jb}_{i}-\sum_{i,j,a}\tilde{L}_{z,ij}\;s^{Ia}_{i}\;t^{Ja}_{j}\right) \tag{7.42}
$$

or

<a id="A3.S8.EGx45"></a>

$$
\displaystyle\begin{aligned} \displaystyle\big{\langle}\Phi^{I}_{\text{singlet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=\pm 1}_{\text{triplet}}\big{\rangle}&\displaystyle=\mp\frac{\alpha_{0}^{2}\hbar}{2\sqrt{2}}\left(\sum_{i,a,b}\tilde{L}_{x,ab}\;s^{Ia}_{i}\;t^{Jb}_{i}-\sum_{i,j,a}\tilde{L}_{x,ij}\;s^{Ia}_{i}\;t^{Ja}_{j}\right)\\
&\displaystyle\qquad\qquad+\frac{\alpha_{0}^{2}\hbar}{2\sqrt{2}\text{i}}\left(\sum_{i,a,b}\tilde{L}_{y,ab}\;s^{Ia}_{i}\;t^{Jb}_{i}-\sum_{i,j,a}\tilde{L}_{y,ij}\;s^{Ia}_{i}\;t^{Ja}_{j}\right)\;.\end{aligned} \tag{7.43}
$$

The SOC constant between different triplet manifolds can be obtained as

<a id="A3.S8.EGx46"></a>

$$
\displaystyle\begin{aligned} \displaystyle\big{\langle}\Phi^{I,M_{s}=0}_{\text{triplet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=\pm 1}_{\text{triplet}}\big{\rangle}&\displaystyle=\mp\frac{\alpha_{0}^{2}\hbar}{2\sqrt{2}}\left(\sum_{i,a,b}\tilde{L}_{x,ab}\;t^{Ia}_{i}\;t^{Jb}_{i}+\sum_{i,j,a}\tilde{L}_{x,ij}\;t^{Ia}_{i}\;t^{Ja}_{j}\right)\\
&\displaystyle\qquad\qquad\frac{\alpha_{0}^{2}\hbar}{2\sqrt{2}\text{i}}\left(\sum_{i,a,b}\tilde{L}_{y,ab}\;t^{Ia}_{i}\;t^{Jb}_{i}+\sum_{i,j,a}\tilde{L}_{y,ij}\;t^{Ia}_{i}\;t^{Ja}_{j}\right)\end{aligned} \tag{7.44}
$$

or

<a id="Ch7.E45"></a>

$$
\big{\langle}\Phi^{I,M_{s}=\pm 1}_{\text{triplet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=\pm 1}_{\text{triplet}}\big{\rangle}=\pm\frac{\alpha_{0}^{2}\hbar}{2}\left(\sum_{i,a,b}\tilde{L}_{z,ab}\;t^{Ia}_{i}\;t^{Jb}_{i}+\sum_{i,j,a}\tilde{L}_{z,ij}\;t^{Ia}_{i}\;t^{Ja}_{j}\right)\;. \tag{7.45}
$$

Note that

<a id="Ch7.E46"></a>

$$
\big{\langle}\Phi^{I,M_{s}=0}_{\text{triplet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=0}_{\text{triplet}}\big{\rangle}=0=\big{\langle}\Phi^{I,M_{s}=\pm 1}_{\text{triplet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J,M_{s}=\mp 1}_{\text{triplet}}\big{\rangle}\;. \tag{7.46}
$$

The total (root-mean-square) spin-orbit coupling is

<a id="eqn:soc_const"></a>

$$
\displaystyle\big{\langle}\Phi^{I}_{\text{singlet}}\big{|}\hat{H}_{\text{SO}}\big{|}\Phi^{J}_{\text{triplet}}\big{\rangle} \tag{7.47a}
$$

For RPA states, the SOC constant can simply be obtained by replacing $s^{Ia}_{i}\;t^{Jb}_{j}$
with $X^{Ia}_{i,\text{triplet}}X^{Jb}_{j,\text{triplet}}+Y^{Ia}_{i,\text{singlet}}Y^{Jb}_{j,\text{triplet}}$
and $t^{Ia}_{i}\;t^{Jb}_{j}$ with
$X^{Ia}_{i,\text{triplet}}X^{Jb}_{j,\text{triplet}}+Y^{Ia}_{i,\text{triplet}}Y^{Jb}_{j,\text{triplet}}$.

A TDDFT + SOC calculation is activated by *$rem* variable CALC_SOC:

### `CALC_SOC`

> **Controls whether to calculate the SOC constants for EOM-CC, RAS-CI, CIS, TDDFT/TDA and TDDFT/RPA.**
>
> * **Type**: `INTEGER/LOGICAL`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not perform the SOC calculation.
>     * `1`: Perform the SOC calculation using the one-electron part of the Breit-Pauli Hamiltonian
>     * `2`: Perform the full SOC calculation using a mean-field treatment of the two-electron contribution
>     * `4`: Perform the SOC calculation using scaled nuclear charges
> * **Recommendation**: The final two options are described in Section 7.9.21.4 .

Examples [7.3.10.1](#ex:dftcis-soc), [7.3.10.1](#ex:dftcis-soc), and [7.3.10.1](#ex:dftcis-soc)
illustrate calculations of SOCs for (SF)-TDDFT states using the above features.
These calculations can also be carried out for CIS states by modifying METHOD appropriately.

The **libwfa** analysis of the spinless one-particle transition density
matrices (as described in Ref. [[1105]](../bib_references/bib.md#bib1152)
)
is implemented for the TDDFT and SF-TDDFT calculations.
To activate this analysis, use the following: CALC_SOC = 2,
STATE_ANALYSIS = TRUE, MOLDEN_FORMAT = TRUE,
and NTO_PAIRS = $N$. Consult Section [10.2](../ch10_properties/sec_wfa.md) for details of the **libwfa** package.

**Note: 

This analysis differs from the NTO analysis of the regular transition density matrix between the singlet and triplet states.
**

???+ example "Example 7.21: Calculation of one-electron SOCs for using TDDFT/TDA."
    ```qchem
    $comment
       This sample input calculates the spin-orbit coupling constants for water
       between its ground state and its TDDFT/TDA excited triplets as well as the
       coupling between its TDDFT/TDA singlets and triplets.  Results are given in
       cm-1.
    $end
    
    $molecule
       0 1
       H       0.000000    -0.115747     1.133769
       H       0.000000     1.109931    -0.113383
       O       0.000000     0.005817    -0.020386
    $end
    
    $rem
       EXCHANGE             b3lyp
       BASIS                6-31G
       CIS_N_ROOTS          4
       CIS_CONVERGENCE      8
       MAX_SCF_CYCLES       600
       MAX_CIS_CYCLES       50
       SCF_ALGORITHM        diis
       MEM_STATIC           300
       MEM_TOTAL            2000
       CIS_SINGLETS         true
       CIS_TRIPLETS         true
       CALC_SOC             true
       MAX_CIS_CYCLES       300
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    ```

???+ example "Example 7.22: Calculation of full SOCs for water molecule including mean-field treatment
of the two-electron part of the Breit-Pauli Hamilton and UHF/TDDFT/TDA."
    ```qchem
    $comment
    Calculation of full SOCs for water molecule inlcuding mean-field treatment
    of the two-electron part of the Breit-Pauli Hamiltonian and Wigner-Eckart theorem.
    UHF/TDDFT/B3LYP/6-31G within the TDA.
    $end
    
    $molecule
    0 1
    H       0.000000    -0.115747     1.133769
    H       0.000000     1.109931    -0.113383
    O       0.000000     0.005817    -0.020386
    $end
    
    $rem
    jobtype                 sp
    unrestricted            true
    method                  b3lyp
    basis                   6-31G
    cis_n_roots             4
    cis_convergence         8
    cis_singlets            true
    cis_triplets            true
    calc_soc                2
    $end
    ```

???+ example "Example 7.23: Calculation of SOCs for methylene using non-collinear SF-TDDFT/PBE0."
    ```qchem
    $comment
    Calculation of SOCs for methylene using non-collinear SF-TDDFT/PBE0,
    with tight convergence.
    $end
    
    $molecule
    0 3
    H1
    C  H1 1.0775
    H2 C  1.0775 H1 133.29
    $end
    
    $rem
    method = pbe0
    basis = cc-pvtz
    scf_convergence = 12
    cis_convergence = 12
    thresh = 14
    cis_n_roots = 2
    calc_soc = 2                    Compute full SOC with mean-field treatment of 2el part
    wang_ziegler_kernel =  true     Important for 1,1 diradicals
    spin_flip = true
    $end
    ```

???+ example "Example 7.24: DFT/CIS calculation of the sulfur L ${}_{2,3}$ -edge in H ${}_{2}$ S. Input is set
to compute SOCs and state-to-state transition moments that can be read by the pySETSOC code, 882 to construct and diagonalize the Breit-Pauli Hamiltonian.
See Section 7.2.2.4 for additional details about the DFT/CIS method."
    ```qchem
    $molecule
    0 1
    S
    H  1 1.343015
    H  1 1.343015 2 92.538291
    $end
    
    
    $rem
     method         cam-b3lyp
     unrestricted   false
     cis_n_roots    200
     calc_soc       2     ! spin-orbit mean-field
     sts_mom        true  ! state-to-state moments, for osc. strengths
     dftcis         1
     dftcis_params  2
     basis          def2-tzvpd
     trnss          true
     trtype         3     ! use alist
     n_sol          3
    $end
    
    $alist
    2 3 4 5
    $end
    ```

## 7.3.10.2 TDDFT+SOC for Spin-Adiabats

For a system with SOC, it can be helpful to calculate the electronic eigenfunctions
(called “spin-adiabats”) of the entire (Coulomb + SOC) Hamiltonian. Computation of such spin-adiabatic states has been implemented
within the CIS or TDDFT/TDA framework, with the SOC treated by the one-electron
Breit–Pauli Hamiltonian at the post-SCF level.

Within a CIS or TDDFT/TDA-SOC, the wave function is represented as

<a id="A3.S8.EGx48"></a>

$$
\displaystyle\left|{\Psi}\right\rangle=\sum_{\epsilon}{\sum_{ia}{t_{ia}^{(\epsilon)}\left|{\Phi_{i}^{a(\epsilon)}}\right\rangle}} \tag{7.48}
$$

where $\epsilon$ is a label of spin, and

<a id="A3.S8.EGx49"></a>

$$
\displaystyle\left|{\Phi_{i}^{a(\epsilon)}}\right\rangle\equiv\begin{cases}\frac{1}{\sqrt{2}}\left(|{\Psi_{i_{\alpha}}^{a_{\alpha}}}\rangle+|{\Psi_{i_{\beta}}^{a_{\beta}}}\rangle\right)&\text{if }\epsilon=\text{singlet}\\
\frac{1}{\sqrt{2}}\left(|{\Psi_{i_{\alpha}}^{a_{\alpha}}}\rangle-|{\Psi_{i_{\beta}}^{a_{\beta}}}\rangle\right)&\text{if }\epsilon=\text{triplet,}m_{s}=0\\
|{\Psi_{i_{\beta}}^{a_{\alpha}}}\rangle&\text{if }\epsilon=\text{triplet,}m_{s}=+1\\
|{\Psi_{i_{\alpha}}^{a_{\beta}}}\rangle&\text{if }\epsilon=\text{triplet,}m_{s}=-1\end{cases} \tag{7.49}
$$

The spin-adiabatic wave functions in Eq. ([7.48](#eq:spinadiabatdef)) are obtained as the eigenstates of following Hamiltonian
having $(4N_{O}N_{V})^{2}$ total matrix elements:

<a id="A3.S8.EGx50"></a>

$$
\displaystyle H=A+V_{\text{SO}}+V_{m} \tag{7.50}
$$

In Eq. ([7.50](#eq:tda_soc)), $A$ is the usual CIS-like TDDFT/TDA linear response matrix (including the one-electron and two-electron terms):

<a id="A3.S8.EGx51"></a>

$$
\displaystyle\langle{\Phi_{\bm{i}}^{\bm{a}}}|{A}|{\Phi_{\bm{j}}^{\bm{b}}}\rangle \tag{7.51}
$$

where the indices $\bm{a},\bm{b},\bm{i},\bm{j}$ are the spin-orbitals, $F$ is the Fock matrix, $E_{gs}$ is the SCF energy, and $\Omega$ is the DFT exchange-correlation functional. More details can be found in Section [7.3.1](sect_tddftintro.md) and Ref. [[107]](../bib_references/bib.md#bib94)
.

The $V_{\text{SO}}$ in Eq. ([7.50](#eq:tda_soc)) is the one-electron SOC Hamiltonian appearing in Eq. ([7.38](#eq:HSO_Breit_Pauli)), and the $V_{m}=g\mu_{B}\mathbf{B}\cdot\mathbf{S}$ is the spin-Zeeman term. Here $g=2$ is assumed. (The coupling between orbital motion and magnetic field is not yet included.) In matrix form, $V_{\text{SO}}+V_{m}$ reads

<a id="A3.S8.EGx52"></a>

$$
\displaystyle\langle{\Psi_{\bm{i}}^{\bm{a}}}|{V_{\text{SO}}+V_{m}}|{\Psi_{\bm{j}}^{\bm{b}}}\rangle=V_{\bm{a}\bm{b}}\delta_{\bm{i}\bm{j}}-V_{\bm{j}\bm{i}}\delta_{\bm{a}\bm{b}} \tag{7.52}
$$

The matrix elements of $V$ are given by

<a id="A3.S8.EGx53"></a>

$$
\displaystyle V_{p_{\alpha}q_{\alpha}} \tag{7.53}
$$

where $\alpha_{0}$ is the fine-structure constant and $\tilde{\mathbf{L}}=\mathbf{L}/r^{3}$.

**Note: 

Currently, this CIS or TDDFT/TDA-SOC implementation supports only restricted SCF calculations (which would produce excited state singlets and triplets in the absence of SOC). Also, the ground state is not coupled to the excited states through SOC (or otherwise).
**

The code is triggered by setting *$rem* variable CIS_SOC = $N$, where $N$ is the number of roots desired:

### `CIS_SOC`

> **Controls the roots of performing TDDFT/TDA-SOC calculation.**
>
> * **Type**: `INTEGER/LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Do not perform the calculation. $N$ Solve the $N$ lowest spin-adiabatic states of TDDFT/TDA-SOC.
> * **Recommendation**: Less than or equal to $4\times$ CIS_N_ROOTS. TDDFT/TDA-SOC first performs a standard TDDFT/TDA calculation so as to generate an initial guess before rerunning the diagonalization to generate the spin adiabats. Therefore, it is a good idea to perform a stand-alone normal TDDFT/TDA calculation and generate the excited spin-diabats and check the desired range of energies, before generating the excited spin-adiabats.

To include a post-SCF magnetic field, the *$bfield_postscf* section must be initialized:

> ```qchem
> $bfield_postscf
>     B_x B_y B_z
>     $end
> ```

Here, the $B_{x},B_{y},B_{z}$ are the spatial components of the external magnetic field in Tesla. Their format must be float (i.e., “0” should be “0.0”).

Derivative coupling calculations are possible between spin-adiabats, but note that the value of the real and imaginary components may vary between different calculations – because the wave functions are complex-valued and may acquire a different global phase (gauge) for each calculation. The norm of derivative coupling should not change.

Examples [7.3.10.2](#ex:cissoc), [7.3.10.2](#ex:cissoc) and [7.3.10.2](#ex:cissoc) illustrate the energy, gradient and derivative coupling calculations using TDDFT/TDA-SOC. In Example [7.3.10.2](#ex:cissoc), a post-SCF external magnetic field is also included.

???+ example "Example 7.25: TDDFT/TDA-SOC calculation of formaldehyde using the $\omega$ B97X functional for the lowest 7 spin-adiabats."
    ```qchem
    $rem
    jobtype                 sp
    exchange                wb97x
    basis                   6-31g
    cis_convergence         8
    cis_n_roots             2
    symmetry                false
    sym_ignore              true
    cis_soc                 7
    $end
    
    $molecule
    0   1
    C 0 0 0
    H 0 0 1.101224
    H 1.00171657 0 -0.45744749
    O -1.00461935 0 -0.645642
    $end
    
    ```

???+ example "Example 7.26: Nuclear gradient of the 4th state in the TDDFT/TDA-SOC calculation of formaldehyde with the $\omega$ B97X functional."
    ```qchem
    $rem
    jobtype                 force
    exchange                wb97x
    basis                   6-31g
    cis_convergence         8
    cis_n_roots             2
    symmetry                false
    sym_ignore              true
    cis_soc                 4
    cis_state_deriv         4
    new_dft                 1 ! This is necessary
    $end
    
    $molecule
    0   1
    C 0 0 0
    H 0 0 1.101224
    H 1.00171657 0 -0.45744749
    O -1.00461935 0 -0.645642
    $end
    
    ```

???+ example "Example 7.27: Derivative coupling between the 4th and 7th TDDFT/TDA-SOC states for a calculation of benzaldehyde with the $\omega$ B97X functional, in the presence of 10 Tesla external magnetic field along the z-direction."
    ```qchem
    $rem
    jobtype                 sp
    exchange                wb97x
    basis                   6-31g
    scf_convergence         10
    cis_convergence         10
    cis_n_roots             2
    symmetry                false
    sym_ignore              true
    cis_soc                 7
    calc_nac                true
    cis_der_numstate        2
    $end
    
    $derivative_coupling
    ...
    4 7
    $end
    
    $bfield_postscf
    0.0 0.0 10.0
    $end
    
    $molecule
    0   1
    C -0.0827555811 -0.0021927111 0.0742168160
    C 0.0163712008 -0.0019362341 1.3503524350
    H 0.9426483579 -0.0021873514 1.9554892885
    C -1.2462538108 -0.0012178895 2.1035447415
    H -1.1928615664 -0.0009432042 3.1942205420
    C -2.4029093145 -0.0008942470 1.4089112839
    H -3.3571329386 -0.0003915665 1.9718859042
    C -2.4418611557 -0.0012099958 0.0672877891
    H -3.3674530317 -0.0009676703 -0.5174127708
    C -1.1678601986 -0.0019316068 -0.6798528411
    H -1.2448466539 -0.0022668669 -1.7738119236
    C 1.1607172056 -0.0028394281 -0.8113481262
    H 1.2563061018 -0.0031882755 -1.8250763954
    O 2.4950317353 -0.0032860998 -0.1735593327
    $end
    
    ```
