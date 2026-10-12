---
title: "10.11.4 Additional Magnetic Field-Related Properties"
---

## 10.11.4 Additional Magnetic Field-Related Properties

(July 4, 2026)

In addition to NMR chemical shieldings and spin-spin couplings, other magnetic
properties available in **Q-Chem** are

- •

hyperfine interaction tensors,
- •

the nuclear quadrupole interaction from electric field gradient tensors, and
- •

the electronic *g*-tensor,

## 10.11.4.1 Hyperfine Interaction

The hyperfine interaction tensor describes the interaction the interaction of
unpaired electron spin with an atom’s nuclear spin levels:

<a id="eq:hyperfine-hamiltonian"></a>

$$
\hat{H}_{\text{HFI}}/h=\mathbf{\hat{S}}\cdot\mathbf{A}\cdot\mathbf{\hat{I}}, \tag{10.119}
$$

which is broken down into Fermi contact (FC), spin-dipole (SD), and orbital Zeeman/spin-orbit coupling (OZ/SOC) terms:

<a id="eq:hyperfine-tensor"></a>

$$
A_{ab}^{\text{tot}}(N)=A_{ab}^{\text{FC}}(N)\delta_{ab}+A_{ab}^{\text{SD}}(N)+A_{ab}^{\text{OZ/SOC}}, \tag{10.120}
$$

where the Fermi contact (FC) contribution is

<a id="eq:hyperfine-fermi-contact"></a>

$$
A^{\text{FC}}(N)=\frac{\alpha}{2}\frac{1}{S}\frac{8\pi}{3}g_{\text{e}}g_{N}\mu_{N}\sum_{\mu\nu}P_{\mu\nu}^{\alpha-\beta}\left\langle\chi_{\mu}|\delta(\mathbf{r}_{N})|\chi_{\nu}\right\rangle \tag{10.121}
$$

and the spin-dipole (SD) contribution is

<a id="eq:hyperfine-spin-dipole"></a>

$$
A_{ab}^{\text{SD}}(N)=\frac{\alpha}{2}\frac{1}{S}g_{e}g_{N}\mu_{N}\sum_{\mu\nu}P_{\mu\nu}^{\alpha-\beta}\left\langle\chi_{\mu}\left|\frac{3r_{N,a}r_{N,b}-\delta_{ab}r_{N}^{2}}{r_{N}^{5}}\right|\chi_{\nu}\right\rangle \tag{10.122}
$$

for a nucleus $N$. The orbital Zeeman/spin-orbit coupling cross-term
(OZ/SOC) is currently not available.

Hyperfine interaction tensors are available for all SCF-based methods with an
unrestricted (not restricted open-shell) reference. Post-HF methods are unavailable.

Calculation of excited state (CIS/TDA-TDDFT) singlet–triplet hyperfine couplings are also available,
but formatted differently than the ground state
unrestricted counterpart. Excited state couplings are printed as contributions from FC and SD for each pair of
excited states and for each spin operator $S_{x},S_{y},S_{z}$. For this method,
the nuclear spin states are averaged to get final coupling contributions.[[44]](../bib_references/bib.md#bib961)

## 10.11.4.2 Nuclear Quadrupole Interaction

Another sensitive probe of the individual nuclear environments in a molecule
is the nuclear quadrupole interaction (NQI), which is a measure of how a nuclear
quadrupole moment interacts with the local electric field gradient:

<a id="eq:nqi-hamiltonian"></a>

$$
\hat{H}_{\text{NQI}}/h=\mathbf{\hat{I}}\cdot\mathbf{Q}\cdot\mathbf{\hat{I}}, \tag{10.123}
$$

<a id="eq:nqi-tensor"></a>

$$
\displaystyle Q_{ab}(N) \tag{10.124}
$$

for a nucleus $N$. Diagonalizing the tensor gives three principal values,
ordered $|Q_{1}|\leq|Q_{2}|\leq|Q_{3}|$, which are components of the
asymmetry parameter eta:

<a id="eq:nqi-eta"></a>

$$
\eta=\frac{Q_{1}-Q_{2}}{Q_{3}} \tag{10.125}
$$

## 10.11.4.3 Electronic *g*-tensor

The electronic *g*-tensor is a measure of the electron describes the coupling of unpaired electron spins with an external magnetic field,
represented by the phenomenological Hamiltonian

<a id="Ch10.E126"></a>

$$
\hat{H}^{\text{g-tensor}}=\mu_{\text{B}}\mathbf{S}\cdot\mathbf{g}\cdot\mathbf{B}, \tag{10.126}
$$

where $\mu_{\text{B}}$ is the Bohr magneton, $\mathbf{S}$ is the intrinsic molecular spin vector,
and $\mathbf{B}$ is the incident magnetic field vector.

The $g$-tensor is comprised of the spin–Zeeman term and the $g$-tensor shift that includes the relativistic mass correction
$\mathbf{g}^{\text{rmc}}$, diamagnetic spin-orbit coupling $\mathbf{g}^{\text{dso}}$ and paramagnetic spin–orbit coupling
$\mathbf{g}^{\text{pso}}$ terms:

<a id="Ch10.E127"></a>

$$
\mathbf{g}=g_{\text{e}}\mathbf{I}+\mathbf{g}^{\text{rmc}}+\mathbf{g}^{\text{dso}}+\mathbf{g}^{\text{pso}}\;. \tag{10.127}
$$

For the spin–Zeeman term the contribution is isotropic and equals the free electron $g$-factor, $g_{\text{e}}$.
The relativistic interaction terms are added as perturbations following the Breit-Pauli *ansatz*, resulting in the expressions given below.
The relativistic mass correction shift term $g^{\text{rmc}}$ is

<a id="Ch10.E128"></a>

$$
g^{\text{rmc}}_{pq}=-\frac{\alpha^{2}g_{\text{e}}}{2S}\delta_{pq}\sum_{\mu\nu}P^{\alpha-\beta}_{\mu\nu}T_{\mu\nu} \tag{10.128}
$$

with $\alpha$ as the fine-structure constant, $P^{\alpha-\beta}_{\mu\nu}$ as the spin density matrix, and $T_{\mu\nu}$ as kinetic energy integrals.
The diamagnetic spin-orbit term $g^{\text{dso}}$ is currently not implemented in **Q-Chem** and therefore excluded but typically
also only of minor importance for lighter elements or first to second row transition metal systems.

The paramagnetic spin-orbit coupling term $g^{\text{pso}}$ is a second-order term in the perturbation series but constitutes the main contribution to the $g$-tensor shift

<a id="Ch10.E129"></a>

$$
g^{\text{pso}}=\frac{1}{\alpha S}\sum_{N}\frac{\left\langle\Psi_{0}\left|h^{\text{SO}}\right|\Psi_{N}\right\rangle\left\langle\Psi_{N}\left|h^{\text{OZ}}\right|\Psi_{0}\right\rangle}{E_{N}-E_{0}} \tag{10.129}
$$

where $h^{\text{SO}}$ is the spin-orbit coupling interaction where a spin-orbit mean-field approach
is used by default,[[364]](../bib_references/bib.md#bib370)
 and $h^{\text{OZ}}$ the orbital Zeeman interaction,

<a id="Ch10.E130"></a>

$$
h^{\text{OZ}}=\mu_{\text{B}}\mathbf{L}\cdot\mathbf{B}\;, \tag{10.130}
$$

with $\mathbf{L}$ as angular momentum.

In this implementation the paramagnetic spin-orbit coupling term is evaluated using a response theory approach,
as first demonstrated by Gauss *et al.*,[[432]](../bib_references/bib.md#bib444)

but with a computational approach following that used in the **Q-Chem** polarization code.[[978]](../bib_references/bib.md#bib1019)

At the moment the $g$-tensor is only implemented at the CCSD level.

## 10.11.4.4 Job Control and Examples

Only one keyword is necessary in the *$rem* section to activate the magnetic property module.

### `MAGNET`

> **Activate the magnetic property module.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`（或 `0`）: Don’t activate the magnetic property module.
>     * `TRUE`（或 `1`）: Activate the magnetic property module.
> * **Recommendation**: None.

All other options are controlled through the *$magnet* input section, which has
the same key-value format as the *$rem* section (see section [3.4](../ch03_inputs/sect_rem.md)).
Current options are:

### `Hyperfine`

> **Activate the calculation of hyperfine interaction tensors. INPUT SECTION: $magnet**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`（或 `0`）: Don’t calculate hyperfine interaction tensors.
>     * `TRUE`（或 `1`）: Calculate hyperfine interaction tensors.
> * **Recommendation**: None. Due to the nature of the property, which requires the spin density, this is not meaningful for restricted (RHF) references. Only UHF (not ROHF) is available.

### `Electric`

> **Activate the calculation of electric field gradient tensors. INPUT SECTION: $magnet**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`（或 `0`）: Don’t calculate EFG tensors and nuclear quadrupole parameters.
>     * `TRUE`（或 `1`）: Calculate EFG tensors and nuclear quadrupole parameters.
> * **Recommendation**: None.

For both hyperfine and EFG tensors, the results for all nuclei are automatically calculated.

### `Hyperfine_Full`

> **Activate calculation of excited state hyperfine couplings. INPUT SECTION: $magnet**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `False (or 0)`: Don’t calculate excited state hyperfine couplings.
>     * `True (or 1)`: Calculate excited state hyperfine couplings.
> * **Recommendation**: None.

### `Hyperfine_Full_NRoots`

> **Specify number of roots for excited state hyperfine calculation. INPUT SECTION: $magnet**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `n`: Calculate hyperfine couplings between lowest n CIS/TDA-TDDFT states.
> * **Recommendation**: None.

### `Hyperfine_Full_Root_Offset`

> **Specify offset for roots for excited state hyperfine calculation. INPUT SECTION: $magnet**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `m`: Calculate hyperfine couplings between lowest n CIS/TDA-TDDFT states, starting at m ${}^{\text{th}}$ root.
> * **Recommendation**: None.

### `Hyperfine_Full_Singlet_Other_Singlet`

> **Specify whether to calculate couplings between singlet excited states. INPUT SECTION: $magnet**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `False (or 0)`: Don’t calculate excited state hyperfine couplings between singlets.
>     * `True (or 1)`: Calculate excited state hyperfine couplings between singlets.
> * **Recommendation**: None.

### `Hyperfine_Full_Triplet_Other_Triplet`

> **Specify whether to calculate couplings between triplet excited states. INPUT SECTION: $magnet**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `False (or 0)`: Don’t calculate excited state hyperfine couplings between triplets.
>     * `True (or 1)`: Calculate excited state hyperfine couplings between triplets.
> * **Recommendation**: None.

Calculation of g-tensor is activated by specifying the G_TENSOR keyword in the *$rem* section.
Example [10.11.4.4](#ex:CCSD-gtensor) illustrates g-tensor calculation for water cation.

### `G_TENSOR`

> **Activates g-tensor calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`（或 `0`）: Don’t calculate g-tensor
>     * `TRUE`（或 `1`）: Calculate g-tensor.
> * **Recommendation**: None.

???+ example "Example 10.62: Calculating hyperfine and EFG tensors for the glycine cation."
    ```qchem
    $molecule
       1 2
       N     0.0000000000     0.0000000000     0.0000000000
       C     1.4467530000     0.0000000000     0.0000000000
       C     1.9682482963     0.0000000000     1.4334965024
       O     1.2385450522     0.0000000000     2.4218667010
       H     1.7988742211    -0.8959881458    -0.5223754133
       H     1.7997303368     0.8930070757    -0.5235632630
       H    -0.4722340827    -0.0025218132     0.8996536532
       H    -0.5080000000     0.0766867527    -0.8765335943
       O     3.3107284257    -0.0000000000     1.5849828121
       H     3.9426948542    -0.0000000000     0.7289954096
    $end
    
    $rem
       METHOD                hf
       BASIS                 def2-sv(p)
       SCF_CONVERGENCE       11
       THRESH                14
       MAGNET                true
       INTEGRAL_SYMMETRY     false
       POINT_GROUP_SYMMETRY  false
    $end
    
    $magnet
       HYPERFINE  true
       ELECTRIC   true
    $end
    ```

???+ example "Example 10.63: Calculating g-tensor for the water cation."
    ```qchem
    $molecule
       1 2
       O    0.00000000   0.00000000   0.13475163
       H    0.00000000  -1.70748899  -1.06930309
       H    0.00000000   1.70748899  -1.06930309
    $end
    
    $rem
       INPUT_BOHR      = true
       METHOD          = ccsd
       BASIS           = 3-21g
       CC_REF_PROP     = true
       G_TENSOR        = true
       N_FROZEN_CORE   = 0
       NO_REORIENT     = true
       SCF_CONVERGENCE = 12
       CC_CONVERGENCE  = 12
       POINT_GROUP_SYMMETRY = false
    $end
    
    $gauge_origin
    0.000000 0.000000  0.0172393
    $end
    ```

Excited state HFC values are printed as

> `Nucleus: IDX`
> 
> 
> …
> 
> 
> `STATE1 / STATE2`
> 
> 
> `FC: S_x_contribution S_y_contribution S_z_contribution`
> 
> 
> `SD: S_x_contribution S_y_contribution S_z_contribution`
> 
> 
> …

???+ example "Example 10.64: Calculating excited state hyperfine coupling for Pyrene-Dimethylaniline radical pair."
    ```qchem
    $molecule
       READ    pydma_xyz.txt
    $end
    
    $rem
       EXCHANGE             wb97x-d3
       BASIS                def2-svpd
       CIS_SINGLETS         true
       CIS_TRIPLETS         true
       CIS_MULLIKEN         true
       CIS_N_ROOTS          15        ! 15 TDA-TDDFT roots for each spin state
       RPA                  false
       MAGNET               true      ! Turn on magnetman
       CC_PRINT_PREC        12        ! Print precision affects precision of printed hfc
       POINT_GROUP_SYMMETRY false
       CIS_MAX_CYCLES       500
       SCF_MAX_CYCLES       500
       SCF_CONVERGENCE      10
       CIS_CONVERGENCE      8
       XC_GRID              3
    $end
    
    $magnet
       HYPERFINE_FULL                       true  ! Activate excited state hfc calculation
       HYPERFINE_FULL_NROOTS                30    ! Calculate all roots
       HYPERFINE_FULL_SINGLET_OTHER_SINGLET false ! Neglect singlet-singlet couplings
       HYPERFINE_FULL_TRIPLET_OTHER_TRIPLET false ! Neglect triplet-triplet couplings
    $end
    ```
