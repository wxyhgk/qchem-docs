---
title: "7.3.11 CIS-1D and TDDFT-1D"
---

## 7.3.11 CIS-1D and TDDFT-1D

(July 4, 2026)

Simulating nonadiabatic dynamics is challenging particularly at crossings
between the ground state (S${}_{0}$) and the first excited state (S${}_{1}$).
For S${}_{1}$/S${}_{0}$ conical intersections, conventional electronic structure methods
(such as HF/CIS and DFT/TDDFT—but not their spin-flip variants) produce
incorrect dimensionality for the crossing
seam.[[1548]](../bib_references/bib.md#bib1614)

The TDDFT-1D method address this limitation by combining DFT and CI
to achieve smooth crossings of S${}_{0}$ and S${}_{1}$ states[[1351]](../bib_references/bib.md#bib1410)

while keeping the cost comparable to that of a standard TDDFT calculation.

The idea behind the CIS-1D and the TDDFT-1D method is to diagonalize a configuration interaction
Hamiltonian whose basis includes the reference state, all singly excited configurations, and one unique doubly excited configuration.
This unique double (the “1D” in CIS-1D/TDDFT-1D) in the CI Hamiltonian gives rise to the CIS-1D method if one starts from a Hartree–Fock reference,
or TDDFT-1D if one starts from a Kohn–Sham reference.

The doubly excited configuration is formed by exciting a pair of electrons from the HOMO ($h$) to the LUMO ($l$). To find the unique double, the canonical molecular orbitals are rotated such that the energy of the doubly excited configuration ($E_{d}$) is minimized.[[56]](../bib_references/bib.md#bib38)

From these optimized orbitals a CI Hamiltonian is constructed,

<a id="eq:configHamiltoninan_tddft1d"></a>

$$
\mathbf{H}=\begin{pmatrix}\epsilon_{0}&0&\left\langle\psi_{0}|H|\psi_{h\bar{h}}^{l\bar{l}}\right\rangle\\
0&\left\langle\psi_{i}^{a}|H|\psi_{j}^{b}\right\rangle&\left\langle\psi_{i}^{a}|H|\psi_{h\bar{h}}^{l\bar{l}}\right\rangle\\
\left\langle\psi_{0}|H|\psi_{h\bar{h}}^{l\bar{l}}\right\rangle&\left\langle\psi_{h\bar{h}}^{l\bar{l}}|H|\psi_{i}^{a}\right\rangle&\left\langle\psi_{h\bar{h}}^{l\bar{l}}|H|\psi_{h\bar{h}}^{l\bar{l}}\right\rangle\end{pmatrix}\;, \tag{7.57}
$$

in the basis of the reference state along with all singly substituted determinants ($\text{\textbar}{\psi_{i}^{a}}\rangle$) and one unique doubly substituted
determinant ($\text{\textbar}{\psi_{h\bar{h}}^{l\bar{l}}}\rangle$). Diagonalizing $\mathbf{H}$ yields the CIS-1D or TDDFT-1D states.
At geometries that are far from crossing points, excitation energies computed with TDDFT-1D
are generally at the same level of accuracy as TDDFT with the Tamm–Dancoff approximation (TDA).
TDDFT-1D’s key advantage appears near ground- and excited-state crossing points, where it produces smooth potential energy surfaces.

To facilitate nonadiabatic dynamics simulations, analytical gradients and derivative couplings are available for the TDDFT-1D method.[[1352]](../bib_references/bib.md#bib1411)

This facilitates the optimization of minimum-energy crossing points (MECPs) between electronic states.

## 7.3.11.1 Job Control for TDDFT-1D

The rem variables for TDDFT-1D calculations are similar to those for CIS calculations and
the following *$rem* variables are used to control TDDFT-1D.

### `CIS1D_N_ROOTS`

> **Sets the number of CIS-1D and TDDFT-1D states to calculate. The lowest eigenstate of $\mathbf{H}$ is the ground state, followed by excited states.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: $n>0$ , Calculate the lowest
>     * $n$: CIS-1D or TDDFT-1D states.
> * **Recommendation**: None

### `CIS1D_ED_CONVERGENCE`

> **Convergence criterion for the minimization of $E_{d}$ , used to optimize the orbitals. The stopping criterion is set to $10^{-\text{CIS1D\_ED\_CONVERGENCE}}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `7`
> * **Options**:
>     * $n$: Convergence achieved when the error is lower than $10^{-n}$ .
> * **Recommendation**: Convergence on the roots of $\mathbf{H}$ is controlled by CIS_CONVERGENCE , which is set to 9 by default for a CIS-1D or TDDFT-1D calculation. If CIS_CONVERGENCE is increased then should also be increased.

### `CIS1D_MAX_CYCLES`

> **Maximum number of Davidson iterations to diagonalize $\mathbf{H}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `60`
> * **Options**:
>     * $n$: Use up to
>     * $n$: iterations.
> * **Recommendation**: The memory allocated for the Davidson iterations (used to diagonalize $\mathbf{H}$ ) is $(n_{\text{occ}}n_{\text{virt}}+\text{2})$ ( )( CIS1D_N_ROOTS )/2 double-precision numbers, where $n_{\text{occ}}$ and $n_{\text{virt}}$ are the number of occupied and virtual orbitals, respectively. Larger values of may require increasing MEM_TOTAL .

### `CIS1D_SCALE_GD`

> **Scaling factor for the coupling matrix element $\langle\psi_{0}|\hat{H}|\psi_{h\bar{h}}^{l\bar{l}}\rangle$ between the reference state and the doubly substituted Slater determinant.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$: $0\leq n\leq 100$ , The coupling element is scaled by $n/100$ .
> * **Recommendation**: There is no rigorous way to determine the coupling elements in $\mathbf{H}$ , since the Kohn-Sham determinant is not a true wave function, so the couplings are computed using a “pseudo-wave function” approach. 1028 Ou Q., Alguire E. C., Subotnik J. E. J. Phys. Chem. B (2015) , 119 , pp. 7150 . Link , 1548 Zhang X., Herbert J. M. J. Chem. Phys. (2015) , 142 , pp. 064109 . Link It sometimes becomes necessary to scale the coupling elements to obtain accurate potential energy surfaces, and the scaling factor has to be determined with some benchmarking. 56 Athavale V., Teh H.-H., Subotnik J. E. J. Chem. Phys. (2021) , 155 , pp. 154105 . Link

### `CIS1D_SCALE_SD`

> **Scaling factor for the coupling matrix element $\langle\psi_{i}^{a}|H|\psi_{h\bar{h}}^{l\bar{l}}\rangle$ between the single excitations and the lone double excitation.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$: $0\leq n\leq 100$ , The coupling element is scaled by $n/100$ .
> * **Recommendation**: Same as CIS1D_SCALE_GD .

### `CIS1D_STATE_DERIV`

> **Selects the CIS-1D/TDDFT-1D state for which gradients are calculated. This is useful for jobs such as geometry optimizations.**
>
> * **Type**: `INTEGER`
> * **Default**: `$-1$`
> * **Options**:
>     * $n$: $n\geq 0$ , Selects the
>     * $n$: th CIS-1D/TDDFT-1D state.
> * **Recommendation**: None

### `CIS1D_DER_NUMSTATE`

> **Determines the number of states for which derivative couplings are to be calculated. The states are specified in the $derivative_coupling section**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not calculate derivative couplings.
>     * $n$: Calculate $n(n-1)/2$ pairs of derivative couplings.
> * **Recommendation**: None

## 7.3.11.2 Examples of TDDFT-1D

???+ example "Example 7.28: TDDFT-1D calculation of water using the B3LYP functional for the lowest 5 states."
    ```qchem
    $molecule
    0 1
    H 0.96 0 0
    O 0.000000000000000 0.000000000000000 0.000000000000000
    H -0.240364803892264 0.929421734762983 0
    $end
    
    $rem
    METHOD    b3lyp
    BASIS     cc-pvdz
    SYM_IGNORE  true
    cis1d_n_roots 5
    $end
    ```

???+ example "Example 7.29: TDDFT-1D calculation of the gradient of the 1st excited state of water in the presence of external charges"
    ```qchem
    $molecule
    0 1
    H 0.96 0 0
    O 0.000000000000000 0.000000000000000 0.000000000000000
    H -0.240364803892264 0.929421734762983 0
    $end
    
    $rem
    METHOD    b3lyp
    BASIS     cc-pvdz
    SYM_IGNORE  true
    cis1d_n_roots 4
    cis1d_state_deriv 1
    jobtype force
    $end
    
    $external_charges
    0.0 0.0 -1.0 -1.0
    0.0 0.0 1.2 1.0
    0.0 0.0 -2.0 -1.0
    0.0 0.0 2.2 1.0
    $end
    ```

???+ example "Example 7.30: Optimizing the MECP between the ground and the 1st excited state of ethylene using the $\omega$ B97X functional."
    ```qchem
    $rem
    geom_opt_driver optimize
    scf_convergence 10
    thresh_diis_switch 9
    cis_convergence 8
    jobtype opt
    mecp_opt      true
    mecp_methods  branching_plane
    MECP_PROJ_HESS true
    mecp_state1  [0,0]
    mecp_state2  [0,1]
    unrestricted false
    calc_nac 1
    scf_algorithm diis_gdm
    cis1d_n_roots 5
    exchange wb97x
    basis 6-31G*
    symmetry_ignore true
    $end
    
    $molecule
    0 1
    C         0.0188526101    0.0181382820   -0.3533168752
    C         1.3813178426    0.0038321438   -0.0594695222
    H         2.0062266305   -0.8967843506    0.0891927721
    H        -0.3788613100   -0.7769905091   -1.0012547284
    H        -0.0243170648   -0.6123230262    0.6288689086
    H         1.9213240937    0.9262667800    0.1943673040
    $end
    ```
