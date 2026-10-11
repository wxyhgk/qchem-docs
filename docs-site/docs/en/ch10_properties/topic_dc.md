---
title: "10.15.2 Diabatic-State-Based Methods"
---

## 10.15.2 Diabatic-State-Based Methods

(July 4, 2026)

## 10.15.2.1 Electronic coupling in charge transfer

A charge transfer involves a change in the electron numbers in a pair of
molecular fragments. As an example, we will use the following reaction when
necessary, and a generalization to other cases is straightforward:

<a id="eq:electron-transfer"></a>

$$
\mathrm{D}^{-}\mathrm{A}\longrightarrow\mathrm{D}\mathrm{A}^{-} \tag{10.177}
$$

where an extra electron is localized to the donor (D) initially, and it becomes
localized to the acceptor (A) in the final state. The two-state secular
equation for the initial and final electronic states can be written as

<a id="eq:2by2HS"></a>

$$
{\bf H}-E{\bf S}=\left(\begin{array}[]{cc}H_{\mathrm{ii}}-S_{\mathrm{ii}}E&H_{\mathrm{if}}-S_{\mathrm{if}}E\\
H_{\mathrm{if}}-S_{\mathrm{if}}E&H_{\mathrm{ff}}-S_{\mathrm{ff}}E\end{array}\right)=0 \tag{10.178}
$$

This is very close to an eigenvalue problem except for the non-orthogonality
between the initial and final states. A standard eigenvalue form for
Eq. ([10.178](#eq:2by2HS)) can be obtained by using the Löwdin transformation:

<a id="Ch10.E179"></a>

$$
\mathbf{H}_{\textrm{eff}}=\mathbf{S}^{-1/2}\mathbf{H}\mathbf{S}^{-1/2}, \tag{10.179}
$$

where the off-diagonal element of the effective Hamiltonian matrix represents
the *electronic coupling* for the reaction, and it is defined by

<a id="eq:coupling-normal"></a>

$$
V=H^{\textrm{eff}}_{\mathrm{if}}=\frac{H_{\mathrm{if}}-S_{\mathrm{if}}(H_{\mathrm{ii}}+H_{\mathrm{ff}})/2}{1-S^{2}_{\mathrm{if}}} \tag{10.180}
$$

In a general case where the initial and final states are not normalized, the
electronic coupling is written as

<a id="eq:coupling"></a>

$$
V=\sqrt{S_{\mathrm{ii}}S_{\mathrm{ff}}}\times\frac{H_{\mathrm{if}}-S_{\mathrm{if}}(H_{\mathrm{ii}}/S_{\mathrm{ii}}+H_{\mathrm{ff}}/S_{\mathrm{ff}})/2}{S_{\mathrm{ii}}S_{\mathrm{ff}}-S^{2}_{\mathrm{if}}} \tag{10.181}
$$

Thus, in principle, $V$ can be obtained when the matrix elements for the
Hamiltonian $H$ and the overlap matrix $S$ are calculated.

The direct coupling (DC) scheme calculates the electronic coupling values via
Eq. ([10.181](#eq:coupling)), and it is widely used to calculate charge transfer
coupling.[[1014]](../bib_references/bib.md#bib1056)
 In the DC scheme,
the coupling matrix element is calculated directly using charge-localized
determinants (the “diabatic states” in electron transfer literature). In
electron transfer systems, it has been shown that such charge-localized states
can be approximated by symmetry-broken unrestricted Hartree-Fock (UHF)
solutions.[[1014]](../bib_references/bib.md#bib1056)
 The adiabatic eigenstates are
assumed to be the symmetric and anti-symmetric linear combinations of the two
symmetry-broken UHF solutions in a DC calculation. Therefore, DC couplings can
be viewed as a result of two-configuration solutions that may recover the non-dynamical correlation.

The core of the DC method is based on the corresponding orbital
transformation[[689]](../bib_references/bib.md#bib715)
 and a calculation for Slater’s determinants in
$H_{\mathrm{if}}$ and $S_{\mathrm{if}}$.[[376]](../bib_references/bib.md#bib381)
 Unfortunately, the
calculation of $H_{\mathrm{if}}$ is not available for DFT method because a functional
of the two densities $\rho_{\mathrm{i}}$ and $\rho\mathrm{f}$ is unknown and there are no
existing approximate forms for $H_{\mathrm{if}}$.[[1502]](../bib_references/bib.md#bib1560)

To calculate charge transfer coupling with DFT, we can use the CDFT-CI method
(Section [5.11.5](../ch05_dft/sect_CDFT-CI.md)), the frontier molecular orbital (FMO)
approach (Section [10.15.2.5](#subsubsect:FMO-DC)),[[1384]](../bib_references/bib.md#bib1456)

or a hybrid scheme, namely, DC with CDFT wave functions (Section [10.15.2.4](#subsubsect:DC)).

## 10.15.2.2 Corresponding orbital transformation

Let $|\Psi_{a}\rangle$ and $|\Psi_{b}\rangle$ be two single Slater-determinant
wave functions for the initial and final states, and $\mathbf{a}$ and $\mathbf{b}$ be the
spin-orbital sets, respectively:

<a id="A3.S8.EGx91"></a>

$$
\displaystyle\mathbf{a} \tag{10.182}
$$

Since the two sets of spin-orbitals are not orthogonal, the overlap matrix
$\mathbf{S}$ can be defined as:

<a id="Ch10.E184"></a>

$$
\mathbf{S}=\int\mathbf{b}^{\dagger}\mathbf{a}\ d\tau. \tag{10.184}
$$

We note that $\mathbf{S}$ is not Hermitian in general since the molecular orbitals of
the initial and final states are separately determined. To calculate the matrix
elements $H_{ab}$ and $S_{ab}$, two sets of new orthogonal spin-orbitals can be
used by the corresponding orbital transformation.[[689]](../bib_references/bib.md#bib715)
 In this
approach, each set of spin-orbitals $\mathbf{a}$ and $\mathbf{b}$ are linearly transformed,

<a id="A3.S8.EGx92"></a>

$$
\displaystyle\hat{\mathbf{a}} \tag{10.185}
$$

where $\mathbf{V}$ and $\mathbf{U}$ are the left-singular and right-singular matrices,
respectively, in the singular value decomposition (SVD) of $\mathbf{S}$:

<a id="Ch10.E187"></a>

$$
\mathbf{S}=\mathbf{U}\hat{\mathbf{s}}\mathbf{V}^{\dagger} \tag{10.187}
$$

The overlap matrix in the new basis is now diagonal

<a id="Ch10.E188"></a>

$$
\int\hat{\mathbf{b}}^{\dagger}\hat{\mathbf{a}}=\mathbf{U}^{\dagger}\left(\int\mathbf{b}^{\dagger}\mathbf{a}\right)\mathbf{V}=\hat{\mathbf{s}} \tag{10.188}
$$

## 10.15.2.3 Generalized density matrix

The Hamiltonian for electrons in molecules are a sum of one-electron and
two-electron operators. In the following, we derive the expressions for the one- and two-electron operators

<a id="Ch10.E189"></a>

$$
\displaystyle\Omega^{(1)} \tag{10.189a}
$$

where

<a id="Ch10.E190"></a>

$$
\displaystyle\omega(i) \tag{10.190a}
$$

Matrix elements of the Hamiltonian can then be expressed as $H_{ab}=\Omega^{(1)}_{ab}+\Omega^{(2)}_{ab}$, where

<a id="Ch10.E191"></a>

$$
\Omega^{(1)}_{ab}=\langle\Psi_{b}|\Omega^{(1)}|\Psi_{a}\rangle=\det(\mathbf{U})\det(\mathbf{V}^{\dagger})\sum^{N}_{i=1}\langle\hat{b}_{i}|\omega(1)|\hat{a}_{i}\rangle\prod^{N}_{j\neq i}\hat{s}_{jj} \tag{10.191}
$$

and

<a id="eq:2par"></a>

$$
\Omega^{(2)}_{ab}=\langle\Psi_{b}|\Omega^{(2)}|\Psi_{a}\rangle=\frac{1}{2}\det(\mathbf{U})\det(\mathbf{V}^{\dagger})\sum^{N}_{ij}\langle\hat{b}_{i}\hat{b}_{j}|\omega(1,2)(1-P_{12})|\hat{a}_{i}\hat{a}_{j}\rangle\prod^{N}_{k\neq{i,j}}\hat{s}_{kk}\;. \tag{10.192}
$$

Overlap integrals are

<a id="eq:1par"></a>

$$
S_{ab}=\langle\Psi_{b}|\Psi_{a}\rangle=\det(\mathbf{U})\det(\mathbf{V}^{\dagger})\prod_{i=1}^{N}\hat{s}_{ii}\;. \tag{10.193}
$$

In an atomic orbital basis set, $\{\chi\}$, we can expand the molecular spin orbitals $\mathbf{a}$ and $\mathbf{b}$,

<a id="A3.S8.EGx95"></a>

$$
\displaystyle\mathbf{a}=\chi\mathbf{A},\qquad\hat{\mathbf{a}}=\chi\mathbf{A}\mathbf{V}=\chi\hat{\mathbf{A}} \tag{10.194}
$$

The one-electron terms, Eq. ([10.193](#eq:1par)), can be expressed as

<a id="A3.S8.EGx96"></a>

$$
\displaystyle\Omega^{(1)}_{ab} \tag{10.196}
$$

where $\displaystyle T_{ii}=S_{ab}/\hat{s}_{ii}$ and define a
generalized density matrix, $\mathbf{G}$:

<a id="eq:g-density"></a>

$$
\mathbf{G}=\hat{\mathbf{A}}\mathbf{T}\hat{\mathbf{B}}^{\dagger}\;. \tag{10.197}
$$

Similarly, the two-electron terms, Eq. ([10.192](#eq:2par)), are

<a id="A3.S8.EGx97"></a>

$$
\displaystyle\begin{aligned} \displaystyle\Omega^{(2)}_{ab}&\displaystyle=\frac{1}{2}\sum_{ij}\sum_{\lambda\sigma}\sum_{\mu\nu}\hat{A}_{\lambda i}\hat{A}_{\sigma j}\left(\frac{1}{\hat{s}_{ii}}\right)T_{jj}\hat{B}^{\dagger}_{i\mu}\hat{B}^{\dagger}_{j\nu}\langle\chi_{\mu}\chi_{\nu}|\omega(1,2)|\chi_{\lambda}\chi_{\sigma}\rangle\\
&\displaystyle=\sum_{\lambda\sigma\mu\nu}G^{\text{L}}_{\lambda\mu}G^{\text{R}}_{\sigma\nu}\langle\mu\nu||\lambda\sigma\rangle\end{aligned} \tag{10.198}
$$

where $\mathbf{G}^{\text{R}}$ and $\mathbf{G}^{\text{L}}$ are generalized density matrices as defined
in Eq. ([10.197](#eq:g-density)) except $T_{ii}$ in $\mathbf{G}^{\text{L}}$ is replaced by $1/(2s_{ii})$.

The $\alpha$- and $\beta$-spin orbitals are treated explicitly. In terms of the
spatial orbitals, the one- and two-electron contributions can be reduced to

<a id="eq:1par-g-ab"></a>

$$
\Omega^{(1)}_{ab}=\sum_{\lambda\sigma}G^{\alpha}_{\lambda\sigma}\omega_{\sigma\lambda}+\sum_{\lambda\sigma}G^{\beta}_{\lambda\sigma}\omega_{\sigma\lambda} \tag{10.199}
$$

<a id="A3.S8.EGx98"></a>

$$
\displaystyle\begin{aligned} \displaystyle\Omega^{(2)}_{ab}&\displaystyle=\sum_{\lambda\sigma\mu\nu}G^{\text{L}\alpha}_{\lambda\mu}G^{\text{R}\alpha}_{\sigma\nu}(\langle\mu\nu|\lambda\sigma\rangle-\langle\mu\nu|\sigma\lambda\rangle)+\sum_{\lambda\sigma\mu\nu}G^{\text{L}\beta}_{\lambda\mu}G^{\text{R}\alpha}_{\sigma\nu}\langle\mu\nu|\lambda\sigma\rangle\\
&\displaystyle\qquad+\sum_{\lambda\sigma\mu\nu}G^{\text{L}\alpha}_{\lambda\mu}G^{\text{R}\beta}_{\sigma\nu}\langle\mu\nu|\lambda\sigma\rangle+\sum_{\lambda\sigma\mu\nu}G^{\text{L}\beta}_{\lambda\mu}G^{\text{R}\beta}_{\sigma\nu}(\langle\mu\nu|\lambda\sigma\rangle-\langle\mu\nu|\sigma\lambda\rangle)\end{aligned} \tag{10.200}
$$

The resulting one- and two-electron contributions, Eqs. ([10.199](#eq:1par-g-ab))
and ([10.200](#eq:2par-g-ab)) can be easily computed in terms of generalized density matrices
using standard one- and two-electron integral routines in **Q-Chem**.

## 10.15.2.4 Direct coupling method for electronic coupling

It is important to obtain proper charge-localized initial and final states for
the DC scheme, and this step determines the quality of the coupling values.
**Q-Chem** provides three approaches to construct charge-localized states:

- •

**The “1+1” approach

**Since the system consists of donor and acceptor molecules or fragments, with a
charge being localized either donor or acceptor, it is intuitive to combine
wave functions of individual donor and acceptor fragments to form a
charge-localized wave function. We call this approach “1+1” since the zeroth
order wave functions are composed of the HF wave functions of the two fragments.

For example, for the case shown in Example ([10.177](#eq:electron-transfer)), we can
use **Q-Chem** to calculate two HF wave functions: those of anionic donor and of
neutral acceptor and they jointly form the initial state. For the final state,
wave functions of neutral donor and anionic acceptor are used. Then the
coupling value is calculated via Eq. ([10.181](#eq:coupling)).

???+ example "Example 10.74: Calculate the electron-transfer coupling for ethylene dimer
with “1+1” charge-localized states"
    ```qchem
    $molecule
      -1  2
    --
      -1  2,  0  1
       C    0.662489    0.000000    0.000000
       H    1.227637    0.917083    0.000000
       H    1.227637   -0.917083    0.000000
       C   -0.662489    0.000000    0.000000
       H   -1.227637   -0.917083    0.000000
       H   -1.227637    0.917083    0.000000
    --
       0  1, -1  2
       C    0.720595    0.000000    4.5
       H    1.288664    0.921368    4.5
       H    1.288664   -0.921368    4.5
       C   -0.720595    0.000000    4.5
       H   -1.288664   -0.921368    4.5
       H   -1.288664    0.921368    4.5
    $end
    
    $rem
       METHOD               HF
       BASIS                6-31G(d)
       SCF_PRINT_FRGM       FALSE
       SCF_GUESS            FRAGMO
       STS_DC               TRUE
       POINT_GROUP_SYMMETRY FALSE
    $end
    ```

In the *$molecule* subsection, the first line is for the charge and
multiplicity of the whole system. The following blocks are two inputs for the
two molecular fragments (donor and acceptor). In each block the first line
consists of the charge and spin multiplicity in the initial state of the
corresponding fragment, a comma, then the charge and multiplicity in the final
state. Next lines are nuclear species and their positions of the fragment.
For example, in the above example, the first block indicates that the electron
donor is a doublet ethylene anion initially, and it becomes a singlet neutral
species in the final state. The second block is for another ethylene going from
a singlet neutral molecule to a doublet anion.

Note that the last three *$rem* variables in this example,
POINT_GROUP_SYMMETRY, SCF_GUESS and STS_DC must be set to
be the values as in the example in order to perform DC calculation with “1+1”
charge-localized states. An additional *$rem* variable,
SCF_PRINT_FRGM is included. When it is TRUE a detailed
output for the fragment HF self-consistent field calculation is given.
- •

**The “relaxed” approach

**In “1+1” approach, the intermolecular interaction is neglected in the initial
and final states, and so the final electronic coupling can be underestimated.
As a second approach, **Q-Chem** can use “1+1” wave function as an initial
guess to look for the charge-localized wave function by further HF
self-consistent field calculation. This approach would ‘relax’ the wave
function constructed by “1+1” method and include the intermolecular
interaction effects in the initial and final wave functions. However, this
method may sometimes fail, leading to either convergence problems or a
resulting HF wave function that cannot represent the desired charge-localized
states. This is more likely to be a problem when calculations are performed
with diffusive basis functions, or when the donor and acceptor molecules are
very close to each other.

To perform relaxed DC calculation, set STS_DC = RELAX.
- •

**Hybrid scheme: Constrained DFT charge-localized states

**Constrained (C)DFT (Section [5.11](../ch05_dft/topic_cdft.md)) can be used to obtain
charge-localized states. It is recommended to set both charge and spin
constraints in order to generate proper charge localization. To perform DC
calculation with CDFT states, set SAVE_SUBSYSTEM = 10 and
SAVE_SUBSYSTEM = 20 to save CDFT molecular orbitals in the first two
jobs of a batch jobs, and then in the third job of the batch job, set
SCF_GUESS = READ and STS_DC = TRUE to
compute electronic coupling values.

???+ example "Example 10.10.75: Calculate the electron-transfer coupling for ethylene dimer using CDFT charge-localized states"
    ```qchem
    $molecule
     -1  2
     C  0.662489  0.000000  0.000000
     H  1.227637  0.917083  0.000000
     H  1.227637 -0.917083  0.000000
     C -0.662489  0.000000  0.000000
     H -1.227637 -0.917083  0.000000
     H -1.227637  0.917083  0.000000
     C  0.720595  0.000000  4.500000
     H  1.288664  0.921368  4.500000
     H  1.288664 -0.921368  4.500000
     C -0.720595  0.000000  4.500000
     H -1.288664 -0.921368  4.500000
     H -1.288664  0.921368  4.500000
    $end
    
    $rem
       METHOD          =  wb97xd
       BASIS           =  cc-pvdz
       CDFT            =  true
       SAVE_SUBSYSTEM  =  10
       POINT_GROUP_SYMMETRY = False
    $end
    
    $cdft
     1.0
     1.0  1 6
     1.0
     1.0  1 6  s
    $end
    
    @@@
    
    $molecule
     read
    $end
    
    $rem
       METHOD          =  wb97xd
       BASIS           =  cc-pvdz
       CDFT            =  true
    point_group_symmetry = False
       SAVE_SUBSYSTEM  =  20
    $end
    
    $cdft
     1.0
     1.0  7 12
     1.0
     1.0  7 12  s
    $end
    
    @@@
    
    $molecule
     read
    $end
    
    $rem
       METHOD      =  hf
       BASIS       =  cc-pvdz
    point_group_symmetry = False
       SCF_GUESS   =  read
       STS_DC      =  true
    $end
    ```

## 10.15.2.5 The frontier molecular orbital approach

The frontier molecular orbital (FMO) approach is often used with DFT to
calculate ET coupling.[[1384]](../bib_references/bib.md#bib1456)
 FMO coupling value is
essentially an off-diagonal Kohn-Sham matrix element that accounts for overlap,

<a id="eq:coupling-FMO"></a>

$$
V^{\mathrm{FMO}}=\frac{f_{\mathrm{DA}}-S\left(f_{\mathrm{DD}}+f_{\mathrm{AA}}\right)/2}{1-S^{2}} \tag{10.201}
$$

where $f_{\mathrm{DA}}=\langle\phi^{\mathrm{D}}_{\mathrm{FMO}}|\hat{f}|\phi^{\mathrm{A}}_{\mathrm{FMO}}\rangle$, with
$\hat{f}$ being the Kohn-Sham operator of the donor-acceptor system. The quantities
$\phi^{\text{D}}_{\text{FMO}}$ and $\phi^{\text{A}}_{\text{FMO}}$
are the Kohn-Sham frontier MOs for the donor and acceptor fragments, respectively,
which represents one-particle scheme of a charge transfer process.

In this approach, computations are often performed separately in the two
fragments, and the off-diagonal Kohn-Sham operator (and the overlap matrix) in
the FMOs is subsequently calculated. To compute FMO couplings, **Q-Chem** has
a setup that is similar to the “1+1” approach.

It may be of interest to compute couplings for frontier orbitals beyond the HOMO of the donor
and the LUMO of the acceptor. They *$rem* options
STS_TRANS_DONOR and STS_TRANS_ACCEPTOR can be used to select a
range of occupied and virtual orbitals for FMO coupling calculations.

STS_TRANS_DONOR

### `STS_TRANS_DONOR`

> **Control the range of frontier MOs for the donor in the FMO approach to ET couplings.**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * $o$
>     * -
>     * $v$
>     * Compute couplings between
>     * $o$
>     * and
>     * $v$
>     * occupied and virtual MOs, respectively.
> * **Recommendation**: None

STS_TRANS_ACCEPTOR

### `STS_TRANS_ACCEPTOR`

> **Control the range of frontier MOs for the acceptor in the FMO approach to ET couplings.**
>
> * **Type**: `STRING`
> * **Default**: `NONE`
> * **Options**:
>     * $o$
>     * -
>     * $v$
>     * Compute couplings between
>     * $o$
>     * and
>     * $v$
>     * occupied and virtual MOs, respectively.
> * **Recommendation**: None

???+ example "Example 10.76: Calculate the electron-transfer coupling for a stacked ethylene dimer with the FMO approach"
    ```qchem
    $molecule
     0  1
    --
     0  1
     C   0.662489   0.000000   0.000000
     H   1.227637   0.917083   0.000000
     H   1.227637  -0.917083   0.000000
     C  -0.662489   0.000000   0.000000
     H  -1.227637  -0.917083   0.000000
     H  -1.227637   0.917083   0.000000
    --
     0  1
     C   0.720595   0.000000   4.500000
     H   1.288664   0.921368   4.500000
     H   1.288664  -0.921368   4.500000
     C  -0.720595   0.000000   4.500000
     H  -1.288664  -0.921368   4.500000
     H  -1.288664   0.921368   4.500000
    $end
    
    $rem
       METHOD              =  lrcwpbe
       OMEGA               =  370
       BASIS               =  dz*
       SCF_PRINT_FRGM      =  true
       SCF_GUESS           =  fragmo
       STS_DC              =  fock
       STS_TRANS_DONOR     =  2-3  ! use HOMO, HOMO-1 and LUMO, LUMO+1, LUMO+2 of donor
       STS_TRANS_ACCEPTOR  =  1-2  ! use HOMO and LUMO, LUMO+1 of acceptor
       POINT_GROUP_SYMMETRY= False
    $end
    
    $rem_frgm
     print_orbitals = 5
    $end
    
    ```
