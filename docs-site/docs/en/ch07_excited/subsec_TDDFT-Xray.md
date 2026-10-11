---
title: "7.12.2 Calculations of X-Ray Spectroscopy with TDDFT"
---

## 7.12.2 Calculations of X-Ray Spectroscopy with TDDFT

(July 4, 2026)

## 7.12.2.1 Absorption Spectroscopy

X-ray absorption spectroscopy can be calculated using TDDFT
by restricting the excitation space to include excitations from a set of core orbitals.
This is achieved by setting TRNSS = TRUE in the *$rem* section, which triggers the use of
TDDFT with a truncated excitation space as described in Section [7.3.3](subsec_TRNSS.md).
The occupied core orbitals that the user desires to be active in such a calculation should be listed individually
in the *$alist* input section, and the number of such orbitals must be specified using N_SOL in the *$rem* section.
This invokes the CVS approximation, which for TDDFT amounts to freezing all of the occupied orbitals except for
the ones that are listed in *$alist*, while using the full virtual space.

Such calculations are not suited to describe the extended x-ray absorption fine structure
(EXAFS) region, which corresponds to the scattering of the ionized electron by the neighboring atoms.

Standard exchange-correlation functionals (including hybrids) tend to severely underestimate
core excitation energies,[[123]](../bib_references/bib.md#bib112)

although chemical shifts (from one compound to the next) may still be valid.[[404]](../bib_references/bib.md#bib413)
**Q-Chem** has short-range corrected (SRC) functionals
available that are designed to predict K-edge core excitation energies accurately.[[123]](../bib_references/bib.md#bib112)

These functionals are a modification of the more familiar long-range corrected
functionals (discussed in Section [5.6](../ch05_dft/sect_LRC-DFT.md)). However, in SRC-DFT the
short-range component of the Coulomb operator is predominantly Hartree-Fock
exchange, while the mid to long-range component is primarily treated with standard DFT exchange.
Job control variables for SRC functionals are provided below and their use in
conjunction with the CVS approximation is illustrated in Example [7.12.2.1](#ex:TDDFT-CVS-0).
See Section [7.3.6.1](subsec_TDDFT-Control.md#subsec:TDDFT-Control:Basic) for basic TDDFT job control.

HF_SR

### `HF_SR`

> **Sets the fraction of Hartree-Fock exchange at $r_{12}=0$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * =
>     * $n/1000$
> * **Recommendation**: None

HF_LR

### `HF_LR`

> **Sets the fraction of Hartree-Fock exchange at $r_{12}=\infty$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * =
>     * $n/1000$
> * **Recommendation**: None

OMEGA

### `OMEGA`

> **Sets the Coulomb attenuation parameter for the short-range component.**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $\omega=n/1000$
>     * , in units of bohr
>     * ${}^{-1}$
> * **Recommendation**: None

OMEGA2

### `OMEGA2`

> **Sets the Coulomb attenuation parameter for the long-range component.**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * $n$
>     * Corresponding to
>     * $\omega_{2}=n/1000$
>     * , in units of bohr
>     * ${}^{-1}$
> * **Recommendation**: None

SRC_DFT

### `SRC_DFT`

> **Selects form of the short-range corrected functional.**
>
> * **Type**: `INTEGER`
> * **Default**: `No default`
> * **Options**:
>     * 1
>     * SRC1 functional.
>     * 2
>     * SRC2 functional.
> * **Recommendation**: None

???+ example "Example 7.206: Calculation of carbon K-edge [C(1s) $\rightarrow$ virtual excitations] using SRC-TDDFT within the CVS approximation."
    ```qchem
    $comment
    Carbon K-edge excitations for acetone.
    The only active occupied orbitals are three C(1s).
    The SRC1-R1 is parameterized for "first row" (C, N, O, ...)
    $end
    
    $molecule
    0 1
      C   -3.0219081    1.0061477    0.0000001
      O   -2.9337180    2.2246186    0.0000001
      C   -1.7817549    0.1662163   -0.0000003
      C   -4.3700966    0.3535647    0.0000004
      H   -0.8735407    0.8061311   -0.0000005
      H   -1.7663727   -0.4765415   -0.9049102
      H   -1.7663723   -0.4765416    0.9049094
      H   -5.1766925    1.1175964    0.0000006
      H   -4.4778785   -0.2802782    0.9049091
      H   -4.4778790   -0.2802781   -0.9049084
    $end
    
    $rem
    exchange           src1-r1  ! r1 = "first row"
    basis              6-31++G*
    cis_n_roots        25
    cis_triplets       false
    trnss              true
    trtype             3
    n_sol              3 ! no. of active orbs
    $end
    
    $alist
    2 3 4
    $end
    
    ```

Relativistic effects become increasingly significant for calculation
of x-ray absorption spectra at the K-edge of heavier elements. The REL_SHIFT keyword
introduces a correction to the calculated excitation energies to account for these
effects, as illustrated in Example [7.12.2.1](#ex:TDDFT-CVS-0) below.
The element-specific correction that is added is equal to the difference between
relativistic (Douglas-Kroll-Hess) and non-relativistic Hartree-Fock eigenvalues for the $1s$ orbital
of the isolated atom.[[118]](../bib_references/bib.md#bib113)

This probably suffices to account for relativistic effects for K-edge excitations, although in the case of L- or
M-edge excitations the situation is complicated by spin-orbit coupling.

REL_SHIFT

### `REL_SHIFT`

> **Corrects the calculated TDDFT excitation energy for scalar relativistic effects.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $Z$
>     * Corresponding to the atomic number of the core-ionized element.
> * **Recommendation**: The relativistic correction is equal to the difference of relativistic (Douglas-Kroll-Hess) and non-relativistic Hartree-Fock/cc-pCVTZ eigenvalues for the $1s$ orbital of the isolated atom.

???+ example "Example 7.207: Calculation of core-excited states at the phosphorus K-edge, including a scalar relativistic shift."
    ```qchem
    $molecule
       0 1
       H     1.196206    0.000000   -0.469131
       P     0.000000    0.000000    0.303157
       H    -0.598103   -1.035945   -0.469131
       H    -0.598103    1.035945   -0.469131
    $end
    
    $rem
       EXCHANGE       SRC2-R2  ! R2 = "second row" (Al, S, P, ...)
       BASIS          6-311(2+,2+)G**
       CIS_N_ROOTS    6
       CIS_TRIPLETS   false
       TRNSS          true
       TRTYPE         3
       N_SOL          1
       REL_SHIFT      15
    $end
    
    $alist
       1
    $end
    ```

Despite the relatively low computational cost of TDDFT, it can become challenging to calculate
x-ray absorption spectra for large systems. The high density of core-excited states makes
simulating spectra more computationally expensive than comparable calculations of the
UV/vis spectra. This is particularly the case when excitations from many core-orbitals are
required, which is often the situation when studying the carbon K-edge of organic molecules.
There are two aspects to the computational cost, firstly the CPU time required and secondly
the memory required. An implementation of TDDFT called “fTDDFTs” combines aggressive integral
screening and a coarse DFT quadrature grid, which is especially
efficient for the calculation of x-ray absorption spectra.[[126]](../bib_references/bib.md#bib115)

This approach may be fine-tuned using the *$rem* variables FAST_XAS, XAS_SCREEN_LEVEL
and XAS_EDGE. The memory required
for these calculations can be reduced further through the TDDFT_NVIRT keyword that
reduces the number of virtual orbitals included in the TDDFT calculation.
Job control variables for fTDDFTs are listed below and are illustrated in Example [7.12.2.1](#ex:TDDFT-CVS-0).

**Note: 

Currently fTDDFTs works only for restricted CIS/TDA calculations and is not parallelized.
(Multiple threads can be used for the initial SCF calculation but the subsequent CIS/TDA calculation
is performed in serial.)
**

FAST_XAS

### `FAST_XAS`

> **Controls whether fast TDDFT for core excitations is used.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * TRUE
>     * Use fast TDDFT.
> * **Recommendation**: None

XAS_SCREEN_LEVEL

### `XAS_SCREEN_LEVEL`

> **Sets the integral screening procedure for fast TDDFT.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $1$
>     * only evaluate integrals that include the inner core basis function on relevant atom(s).
>     * $2$
>     * only evaluate integrals that include basis functions on relevant atom(s).
> * **Recommendation**: 1

XAS_EDGE

### `XAS_EDGE`

> **Specifies the nuclear charge of element being excited.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Corresponding to the nuclear charge of element being excited.
> * **Recommendation**: None

TDDFT_NVIRT

### `TDDFT_NVIRT`

> **Specifies the number of virtual orbitals included in the XAS TDDFT calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Corresponding to the lowest energy
>     * $n$
>     * virtual orbitals.
> * **Recommendation**: None

???+ example "Example 7.208: Fast, low-memory calculation of core-excited states at the oxygen K-edge of CO using fTDDFTs."
    ```qchem
    $molecule
       0 1
       C     0.000000    0.000000   -0.648906
       O     0.000000    0.000000    0.486357
    $end
    
    $rem
       EXCHANGE           SRC1-R1
       BASIS              6-311G*
       CIS_N_ROOTS        6
       CIS_TRIPLETS       false
       TRNSS              true
       TRTYPE             3
       N_SOL              1
       FAST_XAS           true
       XAS_EDGE           6
       XAS_SCREEN_LEVEL   1
    $end
    
    $alist
       1
    $end
    ```

## 7.12.2.2 Emission Spectroscopy

It is also possible to compute x-ray emission spectroscopy using TDDFT. This is achieved
by using a reference determinant with a core-hole.[[1419]](../bib_references/bib.md#bib1480)
 The calculated
excitation energies can be quite sensitive to the choice of basis set, and for the K-edge
of heavier elements it can be necessary to use large or specially adapted basis sets
to provide a good description of the core region.[[400]](../bib_references/bib.md#bib409)

???+ example "Example 7.209: This example shows a calculation of the XES spectrum of water using TDDFT + MOM."
    ```qchem
    $molecule
       0 1
       O   0.0000   0.0000   0.1168
       H   0.0000   0.7629  -0.4672
       H   0.0000  -0.7629  -0.4672
    $end
    
    $rem
       method       cam-b3lyp
       basis        cc-pvdz
    $end
    
    @@@
    
    $molecule
       +1 2
       O   0.0000   0.0000   0.1168
       H   0.0000   0.7629  -0.4672
       H   0.0000  -0.7629  -0.4672
    $end
    
    $rem
       method       cam-b3lyp
       basis        cc-pvdz
       scf_guess    read
       mom_start    1
       cis_n_roots  5
       cis_triplets false
    $end
    
    $occupied
       1:5
       2:5
    $end
    ```

## 7.12.2.3 XCIS-CVS for Open-Shell Ground States

For open-shell systems, XAS spectra and core-excited states can be computed using the “extended CIS” (XCIS) method
of Section [7.2.3.1](Ch7.S2.SS3.md#topic:xcis). With the CVS approximation, core-to-valence transitions can be specifically and efficiently targeted.[[1015]](../bib_references/bib.md#bib1057)

???+ example "Example 7.210: Calculation of core-excited states at the oxygen pre-edge and K-edge of ${}^{3}$ O ${}_{2}$ using the XCIS-CVS method."
    ```qchem
    $molecule
    0 3
    O 0.0000 0.0000 0.0000
    O 0.0000 0.0000 1.2075
    $end
    
    $rem
     basis = aug-cc-pvtz
     method = hf
     rohf_dods = true
     !roscf_diag_scale_a = 50
     max_scf_cycles = 500
     scf_convergence = 8
    $end
    
    @@@
    
    $molecule
     read
    $end
    
    $rem
     method = hf
     basis = aug-cc-pvtz
     unrestricted = false
     scf_guess = read
     max_scf_cycles = 200
     scf_convergence = 8
     cis_n_roots = 5
     cis_max_cycles = 100
     xcis = true
     rpa = false
     trtype = 3
     n_sol = 2
     trnss = true
    $end
    
    $alist
    1 2
    $end
    ```
