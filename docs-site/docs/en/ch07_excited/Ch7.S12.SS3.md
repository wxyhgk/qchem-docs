---
title: "7.12.3 Methods Based on Kohn-Sham Eigenvalues"
---

## 7.12.3 Methods Based on Kohn-Sham Eigenvalues

(July 4, 2026)

## 7.12.3.1 Koopmans’ Approach

A simpler alternative to TDDFT for x-ray emission is to use Kohn-Sham eigenvalue differences,

<a id="Ch7.E176"></a>

$$
\Delta E=\epsilon_{v}-\epsilon_{c}\;, \tag{7.176}
$$

where $\epsilon_{v}$ and $\epsilon_{c}$ are valence and core energy levels, respectively. Oscillator
strengths are obtained from the corresponding transition dipole matrix elements,

<a id="eq:f-trans-dipole"></a>

$$
f_{c\to v}\propto\|\langle\phi_{c}|\hat{\bm{\mu}}|\phi_{v}\rangle\|^{2}\;. \tag{7.177}
$$

This Koopmans’ theorem-type approach is somewhat crude,
as there is no account for orbital relaxation in the core-excited state, but
it has the benefit that only a ground-state calculation is required and therefore this approach is applicable to large
systems,[[522]](../bib_references/bib.md#bib538)

and in conjunction with SRC functionals even this simple procedure can afford
reasonable estimates of the transition energies.[[521]](../bib_references/bib.md#bib535)
 The method is controlled by *$rem* variables
NCORE_XES and NVAL_XES that specify
the number of core ($c$) and valence ($v$) levels to consider, and an example is given in
Example [7.12.3.1](#ex:XES-KSDFT). Extension of this approach
to resonant x-ray emission spectroscopy (involving an excited electronic state) is possible by modeling that
state as a non-*aufbau* solution of the SCF equations, *e.g.*, using algorithms such as
(Section [4.5.14](../ch04_scf/topic_mom.md)), SGM (Section [4.5.15](../ch04_scf/sect_SGM-SCF.md)), or STEP (Section [4.5.16](../ch04_scf/sect_STEP-SCF.md)).

NCORE_XES

### `NCORE_XES`

> **Specifies how many core levels to use in a Koopmans-type XES calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Compute transition dipoles corresponding to the first (lowest energy)
>     * $n$
>     * core orbitals,
>     * $\phi_{c}$
>     * .
> * **Recommendation**: None

NVAL_XES

### `NVAL_XES`

> **Specifies how many valence virtual levels to use in a Koopmans-type XES calculation.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Compute transition dipoles corresponding to the highest
>     * $n$
>     * occupied orbitals,
>     * $\phi_{v}$
>     * .
> * **Recommendation**: Setting $n=1$ will include the HOMO in the occupied space, $n=2$ will include HOMO and $\text{HOMO}-1$ , etc.

???+ example "Example 7.211: The calculation of the XES spectrum of water using the Koopmans approach with a short-range corrected functional."
    ```qchem
    $molecule
       0 1
       C         0.0000000000    0.0000000000    0.5121520001
       O         0.0000000000    0.0000000000   -0.6942567610
       H         0.9377642813    0.0000000000    1.1074358558
       H        -0.9377642813    0.0000000000    1.1074358558
    $end
    
    $rem
       METHOD          src1r1
       BASIS           6-311G**
       NCORE_XES       2
       NVAL_XES        4
    $end
    ```

## 7.12.3.2 Transition-Potential DFT

The *transition potential* (TP-)DFT method[[1308]](../bib_references/bib.md#bib1365)

is an alternative approach that accounts for some orbital
relaxation yet retains a framework based on Kohn-Sham eigenvalues, requiring only a ground-state calculation.
This approach is based on Slater’s transition concept,[[1269]](../bib_references/bib.md#bib1322)

in which an SCF calculation with a fractional electron (originally $n_{i}=1/2$) is removed from occupied orbital $\phi_{i}$,
then the ionization energy for that MO is approximated as

<a id="eq:TPDFT-ip"></a>

$$
\text{IE}_{i}\approx-\epsilon_{i}(n_{i}=1/2)\;. \tag{7.178}
$$

This can be justified based on a
Taylor expansion in terms of the orbital occupations.[[1269]](../bib_references/bib.md#bib1322)

Excitation energies are approximated as eigenvalue differences $\epsilon_{a}-\epsilon_{i}$ obtained from a
fractional-electron SCF calculation in which $n_{i}=1/2$ electron is promoted from $\phi_{i}$ into the LUMO:

<a id="eq:TPDFT-ee"></a>

$$
\Delta E_{i\to a}=\epsilon_{a}(n_{i}=1/2,n_{\text{LUMO}}=1/2)-\epsilon_{i}(n_{i}=1/2,n_{\text{LUMO}}=1/2)\;, \tag{7.179}
$$

with oscillator strengths $f_{i\to a}\propto|\langle\phi_{i}|\hat{\bm{\mu}}|\phi_{a}\rangle|^{2}$, as in Eq. ([7.177](#eq:f-trans-dipole)).

TP-DFT calculations in **Q-Chem** are setup to remove 1/2 electron from the lowest core orbital of a given atom that is
specified using TPDFT_ATOM. (For more flexible and general fractional-electron SCF schemes, see
Section [7.12.3.3](#ex:XAS-2).) Optionally, one may use TPDFT_LUMO to occupy the LUMO, corresponding
to an excitation energy calculation [Eq. ([7.179](#eq:TPDFT-ee))], or omit this variable to compute the core-level electron
binding energy [Eq. ([7.178](#eq:TPDFT-ip))].

TPDFT_ATOM

### `TPDFT_ATOM`

> **Activate TP-DFT by specifying the atom from which to remove an electron.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Remove an electron from the lowest-energy orbital on the atom whose index is
>     * $n$
>     * .
> * **Recommendation**: Be sure to set UNRESTRICTED = TRUE for TP-DFT calculations.

TPDFT_FRAC

### `TPDFT_FRAC`

> **Specify the fractional value of $n_{i}$ to be removed.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $n$
>     * Remove
>     * $n/100$
>     * of an electron from the orbital specified using
>     * TPDFT_ATOM
>     * .
> * **Recommendation**: None

TPDFT_LUMO

### `TPDFT_LUMO`

> **Specify the fractional value of $n_{\text{LUMO}}$ to be added.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Add
>     * $n/100$
>     * of an electron to the LUMO.
> * **Recommendation**: Leave = 0 for core-level binding energy calculations [Eq. ( 7.178 )] or use = 50 to implement Eq. ( 7.179 ).

???+ example "Example 7.212: TP-DFT excitation energy calculation, removing $n_{i}=1/2$ from O(1s) and placing it in the LUMO."
    ```qchem
    $molecule
       0 1
       O
       H 1 0.95
       H 2 0.95 2 104.5
    $end
    
    $rem
       METHOD       b3lyp
       BASIS        aug-cc-pCVQZ
       UNRESTRICTED true
       TPDFT_ATOM   1
       TPDFT_FRAC   50
       TPDFT_LUMO   50 ! set to 0 for IE calculation
    $end
    
    ```

## 7.12.3.3 Slater-Type Fractional-Electron Methods

A more general set of fractional-electron methods for both core-level ionization (*i.e.*, XPS) and core-level excitation
(XAS and also XES) has been explored by Jana and Herbert.[[626]](../bib_references/bib.md#bib650)
 These methods
generalize Slater’s transition concept,[[1269]](../bib_references/bib.md#bib1322)
 and allow an arbitrary
fraction of an electron to be removed from a core MO and (optionally) placed into a virtual MO, as specified by the user.
The use of these generalized Slater-type methods
is controlled by the *$rem* variables that are described below and illustrated in examples that follow.
For XAS, oscillator strengths are computed according to Eq. ([7.177](#eq:f-trans-dipole)),
and the (occupied, virtual) orbital pairs ($\phi_{i},\phi_{a}$) for which the transition dipole moment is computed are
specified using NCORE_XAS and NVAL_XAS, as described in Section [7.12.3.1](#ex:XES-KSDFT).
To converge the fractional-electron state, it may be necessary to use an algorithm such as MOM (Section [4.5.14](../ch04_scf/topic_mom.md)),
SGM (Section [4.5.15](../ch04_scf/sect_SGM-SCF.md)), or STEP ([4.5.16](../ch04_scf/sect_STEP-SCF.md)).
Consult Refs. [[626]](../bib_references/bib.md#bib650)
 and [[627]](../bib_references/bib.md#bib651)
 for best practices regarding which generalized
Slater-type method to use.

FRACTIONAL_ELECTRON

### `FRACTIONAL_ELECTRON`

> **Specify the fraction of an electron to be removed from the occupied space.**
>
> * **Type**: `INTEGER`
> * **Default**: `NONE`
> * **Options**:
>     * $-n$
>     * Remove
>     * $n/1000$
>     * of an electron.
> * **Recommendation**: The original Slater method ( $n_{i}=1/2$ ) corresponds to = $-$ 500 but there can be other choices.

FRAC_VIR_ELEC

### `FRAC_VIR_ELEC`

> **Specify the fraction of an electron to place into the occupied space.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Add
>     * $n/1000$
>     * of an electron.
> * **Recommendation**: A value $>0$ should be used for excitation (XAS or XES), whereas the default is appropriate for ionization (XPS).

FRAC_ELEC_ORB

### `FRAC_ELEC_ORB`

> **Specify the occupied orbital from which the fractional electron should be removed.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Remove from
>     * $\phi_{n}$
>     * .
> * **Recommendation**: None

FRAC_VIR_ELEC_ORB

### `FRAC_VIR_ELEC_ORB`

> **Specify the virtual orbital to which the fractional electron should be added.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$
>     * Add to
>     * $\phi_{n}$
>     * .
> * **Recommendation**: Use this only if FRAC_VIR_ELEC $>0$ .

???+ example "Example 7.213: Original Slater transition method (STM) for oxygen K-shell XPS, removing $n_{i}=1/2$ electron from O(1s) core orbital.
A normal SCF calculation is used to obtain the initial set of orbitals, followed by a fractional-electron calculation that
is converged using the IMOM algorithm."
    ```qchem
    $molecule
    0 1
    C  -0.00000000  0.00000000  0.07378202
    O   0.00000000  0.00000000  1.20921798
    $end
    
    $rem
     UNRESTRICTED  TRUE
     BASIS         def2-QZVP
     METHOD        B3LYP
     POINT_GROUP_SYMMETRY FALSE
     INTEGRAL_SYMMETRY    FALSE
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
     SCF_GUESS     READ
     METHOD        B3LYP
     BASIS         def2-QZVP
     UNRESTRICTED  TRUE
     FRAC_ELEC_ORB        1  ! lowest-energy orbital is O(1s)
     FRAC_VIR_ELEC_ORB    1
     FRACTIONAL_ELECTRON -500
     FRAC_VIR_ELEC        0
     MOM_START            1
     MOM_METHOD           IMOM
     POINT_GROUP_SYMMETRY FALSE
     INTEGRAL_SYMMETRY    FALSE
    $end
    ```

???+ example "Example 7.214: XAS at carbon K-edge, using Slater’s transition method with $n_{i}=1/2$ electrons removed from
C(1s) and $n_{a}=1/2$ electron placed in the LUMO."
    ```qchem
    $molecule
     0 1
    C  -0.00000000  0.00000000  0.07378202
    O   0.00000000  0.00000000  1.20921798
    $end
    
    $rem
     UNRESTRICTED  TRUE
     BASIS         def2-QZVP
     METHOD        B3LYP
     POINT_GROUP_SYMMETRY FALSE
     INTEGRAL_SYMMETRY    FALSE
    $end
    
    @@@
    
    $molecule
    read
    $end
    
    $rem
     SCF_GUESS     READ
     METHOD        B3LYP
     BASIS         def2-QZVP
     UNRESTRICTED  TRUE
     FRAC_ELEC_ORB        2  ! C(1s)
     FRAC_VIR_ELEC_ORB    1
     FRACTIONAL_ELECTRON -500
     FRAC_VIR_ELEC        500
     MOM_START            1
     MOM_METHOD           IMOM
     NCORE_XAS            2
     NVAL_XAS             2
     POINT_GROUP_SYMMETRY FALSE
     INTEGRAL_SYMMETRY    FALSE
    $end
    ```
