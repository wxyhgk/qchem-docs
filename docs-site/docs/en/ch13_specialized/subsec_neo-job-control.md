---
title: "13.5.4 Job Control for the NEO methods"
---

## 13.5.4 Job Control for the NEO methods

(July 4, 2026)

## 13.5.4.1 General Keywords

The NEO method is a natural extension of the SCF method and it inherits many of its functionalities.
Some keywords that are used in the SCF Job Control are used in the NEO methods with a few additional keywords.
The following *$rem* variables must be specified in order to run NEO calculations:

!!! note "Note"
    Some *$rem* variables, which we find mostly self-explanatory but not discussed below, that
    also influence NEO jobs in regards to geometry and symmetry considerations include
    INPUT_BOHR, SYM_IGNORE, and POINT_GROUP_SYMMETRY.


### `NEO`

> **Enable a NEO-SCF calculation.**
>
> * **Type**: `BOOLEAN`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Enable a NEO-SCF calculation.
>     * `FALSE`: Disable a NEO-SCF calculation.
> * **Recommendation**: Set to TRUE if desired.

### `JOBTYPE`

> **Specifies the type of calculation.**
>
> * **Type**: `STRING`
> * **Default**: `SP`
> * **Options**:
>     * `SP`: Single point energy.
>     * `FORCE`: Analytical force calculation.
>     * `OPT`: Geometry minimization.
>     * `TS`: Transition structure search.
>     * `FREQ`: Frequency calculation.
> * **Recommendation**: Application-dependent. Always use POINT_GROUP_SYMMETRY = FALSE with geometry optimization.

### `METHOD`

> **Specifies the exchange-correlation functional.**
>
> * **Type**: `STRING`
> * **Default**: `No default`
> * **Options**:
>     * `NAME`: Use =
>     * `NAME`: , where
>     * `NAME`: is one of the following: HF for Hartree-Fock theory; one of the DFT methods listed in Section 5.3.5 .;
> * **Recommendation**: In general, consult the literature to guide your selection. Our recommendations for DFT are indicated in bold in Section 5.3.5 .

### `BASIS`

> **Specifies the electronic basis sets to be used.**
>
> * **Type**: `STRING`
> * **Default**: `No default basis set`
> * **Options**:
>     * `General, Gen`: User defined ( $basis keyword required).
>     * `Symbol`: Use standard basis sets as per Chapter
>     * `8`: .
>     * `Mixed`: Use a mixture of basis sets (see Chapter
>     * `8`: ).
> * **Recommendation**: Consult literature and reviews to aid your selection.

The format for the user-defined basis section is as follows:

> | $basis |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- |
> |  | $X$ | 0 |  |  |  |
> |  | $L$ | $K$ | $scale$ |  |  |
> |  | $\alpha_{1}$ | $C_{1}^{L_{\text{min}}}$ | $C_{1}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{1}^{L_{\text{max}}}$ |
> |  | $\alpha_{2}$ | $C_{2}^{L_{\text{min}}}$ | $C_{2}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{2}^{L_{\text{max}}}$ |
> |  | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ |
> |  | $\alpha_{K}$ | $C_{K}^{L_{\text{min}}}$ | $C_{K}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{K}^{L_{\text{max}}}$ |
> | **** |  |  |  |  |  |
> | $end |  |  |  |  |  |

where

| $X$ | Atomic symbol of the atom (atomic number not accepted) |
| --- | --- |
| $L$ | Angular momentum symbol (S, P, SP, D, F, G) |
| $K$ | Degree of contraction of the shell (integer) |
| $scale$ | Scaling to be applied to exponents (default is 1.00) |
| $\alpha_{i}$ | Gaussian primitive exponent (positive real number) |
| $C_{i}^{L}$ | Contraction coefficient for each angular momentum (non-zero real numbers). |

Atoms are terminated with `****` and the complete basis set is
terminated with the *$end* keyword terminator. No blank lines can be
incorporated within the general basis set input. Note that more than one
contraction coefficient per line is required for compound shells like SP.
As with all **Q-Chem** input deck information, all input is case-insensitive.

Additionally, the NEO-SCF methods require definition of the nuclear basis sets.
Refer to Ref. [[1536]](../bib_references/bib.md#bib1600)
 for selection of the protonic basis sets. Note that the pure (spherical harmonic) and Cartesian angular forms for the protonic basis sets are found
in the main article and in the supported information, respectively. Also, see details about the NEO_PURECART variable described in the next section.

The format for the user-defined neo_basis section is as follows:

> | $neo_basis |  |  |  |  |  |
> | --- | --- | --- | --- | --- | --- |
> |  | $X$ | 0 |  |  |  |
> |  | $L$ | $K$ | $scale$ |  |  |
> |  | $\alpha_{1}$ | $C_{1}^{L_{\text{min}}}$ | $C_{1}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{1}^{L_{\text{max}}}$ |
> |  | $\alpha_{2}$ | $C_{2}^{L_{\text{min}}}$ | $C_{2}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{2}^{L_{\text{max}}}$ |
> |  | $\vdots$ | $\vdots$ | $\vdots$ | $\ddots$ | $\vdots$ |
> |  | $\alpha_{K}$ | $C_{K}^{L_{\text{min}}}$ | $C_{K}^{L_{\text{min}}+1}$ | $\ldots$ | $C_{K}^{L_{\text{max}}}$ |
> | **** |  |  |  |  |  |
> | $end |  |  |  |  |  |

!!! note "Note"
    Several of the post-NEO-HF methods utilizing density fitting also require
    the nuclear auxiliary basis set to be defined. The format for such user-defined *$neo_aux_basis*
    section is identical to the *$basis* and *$neo_basis* input sections. See examples in Section [13.5.6](subsec_neo-examples.md) for more details.


## 13.5.4.2 Additional Keywords

More *$rem* variables that can be used to customize the calculation. Some of these are NEO specific variables,
while others are shared with other **Q-Chem** modules:

### `BASIS_LIN_DEP_THRESH`

> **Sets the threshold for determining linear dependence in the basis set**
>
> * **Type**: `INTEGER`
> * **Default**: `6`
> * **Options**:
>     * $n$: Sets the threshold to $10^{-n}$
> * **Recommendation**: Set to 5 or smaller if you have a poorly behaved SCF and you suspect linear dependence in you basis set. Lower values (larger thresholds) may affect the accuracy of the calculation.

### `NEO_BASIS_LIN_DEP_THRESH`

> **This keyword is used to set the liner dependency threshold for nuclear basis sets. It is defined as $10^{-\mathrm{NEO\_BASIS\_LIN\_DEP\_THRESH}}$ .**
>
> * **Type**: `DOUBLE`
> * **Default**: `5.0`
> * **Options**:
>     * `User-defined`
> * **Recommendation**: No recommendation.

### `PURECART`

> **INTEGER**
>
> * **Type**: `Controls the use of pure (spherical harmonic) or Cartesian angular forms`
> * **Default**: `1111`
> * **Options**:
>     * $hgfd$: Use 1 for pure and 2 for Cartesian.
> * **Recommendation**: This is pre-defined for all standard basis sets

### `NEO_PURECART`

> **This keyword is used to specify Cartesian or spherical Gaussians for nuclear basis functions.**
>
> * **Type**: `INTEGER`
> * **Default**: `2222`
> * **Options**:
>     * `User-defined`
> * **Recommendation**: The default value corresponds to the use of Cartesian Gaussians for all angular momentum classes. The value = 1111 would use spherical Gaussians instead, similar to the use of PURECART .

### `NEO_ISOTOPE`

> **Enable calculations of different types of isotopes. Only one type of isotope is allowed at present.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: This NEO calculation uses protons.
>     * `2`: This NEO calculation uses deuterons.
>     * `3`: This NEO calculation uses tritons.
> * **Recommendation**: Refer to the NEO literature for the best performance on the isotope effects calculations.

### `NEO_VPP`

> **This keyword is used to control whether to remove $J-K$ terms from the nuclear Fock matrix and the corresponding kernel terms for NEO excited state methods. The purpose for the removal of these terms in the case of one quantum proton is to save on computational cost. Note that the ground state NEO-HF or NEO-DFT energy is the same with or without removal of these nuclear $J-K$ terms. The nuclear virtual orbitals will however be different, which may affect the results for perturbative methods ( i.e. , multicomponent excited-state methods and post-NEO-HF wave function methods).**
>
> * **Type**: `LOGICAL/INTEGER`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`（或 `1`）: Enable this option (include nuclear $J-K$ terms).
>     * `FALSE`（或 `0`）: Disable this option (remove nuclear $J-K$ terms).
> * **Recommendation**: Set = 0 only in the case of one quantum hydrogen.

### `XC_GRID`

> **Specifies the type of grid to use for DFT calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `Functional-dependent; see Table`
> * **Options**:
>     * `0`: Use SG-0 for H, C, N, and O; SG-1 for all other atoms.
>     * $n$: Use SG-
>     * $n$: for all atoms, $n=1,2$ , or 3 $XY$ A string of two six-digit integers $X$ and $Y$ , where $X$ is the number of radial points and $Y$ is the number of angular points where possible numbers of Lebedev angular points, which must be an allowed value from Table 5.2 in Section 5.5 . $-XY$ Similar format for Gauss-Legendre grids, with the six-digit integer $X$ corresponding to the number of radial points and the six-digit integer $Y$ providing the number of Gauss-Legendre angular points, $Y=2N^{2}$ .
> * **Recommendation**: We strongly recommend using an unpruned, Euler-Maclaurin-Lebedev grid type for NEO-DFT calculations. Larger grids may be required for optimization and frequency calculations.

### `UNRESTRICTED`

> **Controls the use of restricted or unrestricted orbitals.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Constrain the spatial part of the alpha and beta orbitals to be the same.
>     * `TRUE`: Do not Constrain the spatial part of the alpha and beta orbitals.
> * **Recommendation**: The ROHF method is not available. Note that for unrestricted calculations on systems with an even number of electrons it is usually necessary to break $\alpha$ / $\beta$ symmetry in the initial guess, by using SCF_GUESS_MIX or providing $occupied information (see Section 4.4 on initial guesses).

### `S2THRESH`

> **Cutoff for neglect of overlap integrals, defined via a two-electron shell-pair threshold of $10^{-\mathrm{S2THRESH}}$ ( $\leq 14$ ).**
>
> * **Type**: `INTEGER`
> * **Default**: `Same as`
> * **Options**:
>     * $n$: for a threshold of $10^{-n}$ .
> * **Recommendation**: Increase the value of if the program finds negative eigenvalues for the overlap matrix.

### `THRESH`

> **Cutoff for neglect of two electron integrals. $10^{-\mathrm{THRESH}}$ ( $\leq 14$ ).**
>
> * **Type**: `INTEGER`
> * **Default**: `8`
> * **Options**:
>     * $n$: for a threshold of $10^{-n}$ .
> * **Recommendation**: The value should satisfy $\geq$ 3 + SCF_CONVERGENCE , although = 4 + SCF_CONVERGENCE is the default (in most cases) since Q-Chem v. 6.0. See Ref. 479 Gray M., Bowling P. E., Herbert J. M. J. Phys. Chem. A (2024) , 128 , pp. 7739 . Link for recommended values of in the presence of diffuse basis functions, where tighter thresholds are often required and too-loose thresholds may lead to slower convergence or convergence failure.

### `MEM_STATIC`

> **Sets the memory for AO-integral evaluations and their transformations in Q-Chem 4.1 or older versions.**
>
> * **Type**: `INTEGER`
> * **Default**: `192`
> * **Options**:
>     * $n$: User-defined number of megabytes.
> * **Recommendation**: Use the default.

### `MEM_TOTAL`

> **Sets the total memory available to Q-Chem , in megabytes.**
>
> * **Type**: `INTEGER`
> * **Default**: `2000`
> * **Options**:
>     * $n$: User-defined number of megabytes.
> * **Recommendation**: Use the default, or set to the physical memory of your machine. The minimum requirement is $3X^{2}$ .

## 13.5.4.3 NEO-SCF Specific Keywords

The following *$rem* variables can be used to specify the tolerances for NEO-SCF convergence.
Some of these *$rem* variables are inherited from conventional SCF calculations:

### `SCF_CONVERGENCE`

> **NEO-SCF is considered converged when the electronic wave function error is less that $10^{-\mathrm{SCF\_CONVERGENCE}}$ . Adjust the value of THRESH at the same time. (Starting with Q-Chem 3.0, the DIIS error is measured by the maximum error rather than the RMS error as in earlier versions.)**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * `User-defined`
> * **Recommendation**: None.

### `NEO_N_SCF_CONVERGENCE`

> **NEO-SCF is considered converged when the nuclear wave function error is less that $10^{-\mathrm{NEO\_N\_SCF\_CONVERGENCE}}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `7`
> * **Options**:
>     * `User-defined`
> * **Recommendation**: None.

### `NEO_E_CONV`

> **Energy convergence criteria in the NEO-SCF calculations so that the difference in energy between consecutive iterations is less than $10^{-\mathrm{NEO\_E\_CONV}}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `8`
> * **Options**:
>     * `User-defined`
> * **Recommendation**: Tighter criteria for geometry optimization are recommended. Note that for stepwise calculations, this convergence criteria checks the difference in energy between electronic and protonic microiterations blocks.

### `MAX_SCF_CYCLES`

> **Controls the maximum number of SCF iterations permitted.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * $n$: $n>0$ User-selected.
> * **Recommendation**: Increase for slowly converging systems such as those containing transition metals.

### `NEO_E_MAX_SCF_CYCLES`

> **Controls the maximum number of electronic SCF micoiterations permitted. This variable is only used for stepwise NEO-SCF optimizations.**
>
> * **Type**: `INTEGER`
> * **Default**: `150`
> * **Options**:
>     * $n$: $n>0$ User-selected.
> * **Recommendation**: None.

### `NEO_N_MAX_SCF_CYCLES`

> **Controls the maximum number of nuclear SCF micoiterations permitted. This variable is only used for stepwise NEO-SCF optimizations.**
>
> * **Type**: `INTEGER`
> * **Default**: `150`
> * **Options**:
>     * $n$: $n>0$ User-selected.
> * **Recommendation**: None.

The NEO-SCF iteration procedure has traditionally involved solving the
electronic and quantum nuclear Roothaan/Kohn-Sham equations in alternating fashion until convergence to the variational solution is
reached. This approach can become computationally expensive, especially when many SCF iterations are required to achieve self-consistency.
To accelerate this procedure, those equations may instead be solved simultaneously at every step of the NEO-SCF iteration procedure.
This is now the default scheme for solving the NEO-SCF equations. We support the simultaneous implementation of the Direct Inversion in the Iterative Subspace (DIIS) algorithm[[837]](../bib_references/bib.md#bib883)

as well as the Geometric Direct Minimization (GDM)[[1391]](../bib_references/bib.md#bib1453)
 approach. The following *$rem* variables permit some customization of the NEO-SCF iterations:

### `NEO_SIMULTANEOUS_SCF`

> **Enables simultaneous optimization algorithm.**
>
> * **Type**: `LOGICAL`
> * **Default**: `TRUE`
> * **Options**:
>     * `TRUE`
>     * `FALSE`
> * **Recommendation**: Use the default unless issues with convergence are observed, in which cause set to FALSE to utilize the traditional stepwise approach.

### `SCF_ALGORITHM`

> **Algorithm used for converging the SCF.**
>
> * **Type**: `STRING`
> * **Default**: `DIIS`
> * **Options**:
>     * `DIIS`: Pulay DIIS.
>     * `GDM`: Geometric Direct Minimization.
>     * `DIIS_GDM`: Use DIIS and then later switch to geometric direct minimization.
> * **Recommendation**: In the NEO methods, the GDM procedure is recommended. Note that DIIS_GDM is only supported for simultaneous optimizations.

### `NEO_SCF_GUESS_N`

> **Specifies the initial guess procedure for the nuclear orbitals in a NEO-SCF calculation.**
>
> * **Type**: `STRING`
> * **Default**: `TIGHT`
> * **Options**:
>     * `CORE`: Diagonalize the nuclear core Hamiltonian
>     * `TIGHT`: Occupies the least diffuse nuclear MO
>     * `AUTOSAD`: On-the-fly superposition of nuclear atomic densities from an atomic NEO calculation
>     * `READ`: Read previous nuclear MOs from disk
> * **Recommendation**: Use the default. Note that if is set to READ , only the nuclear MOs from a previous NEO-SCF job are read from disk. The starting guess for the electronic MOs in a NEO calculation remains the converged result from the conventional electronic calculation of the current job. To read in both the electronic and nuclear MOs from a previous NEO-SCF job, must be set to READ in conjunction with SKIP_SCFMAN set to TRUE .

### `NEO_STEPWISE_SCF_STEPS`

> **Specifies the number of NEO-SCF stepwise/alternating macro-iterations to perform before switching to simultaneous algorithm.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `User-defined`
> * **Recommendation**: The rate of convergence of the NEO-SCF procedure is dependent on the initial guess for the electronic and protonic orbitals. For especially difficult systems, it may be helpful to do stepwise optimization before switching to simultaneous.

!!! note "Note"
    The following variables are specific to SCF_ALGORITHM = DIIS.


### `DIIS_SUBSPACE_SIZE`

> **Controls the size of the DIIS subspace during the SCF.**
>
> * **Type**: `INTEGER`
> * **Default**: `10`
> * **Options**:
>     * `User-defined`
> * **Recommendation**: None.

### `DIIS_ERR_RMS`

> **Changes the DIIS convergence metric from the maximum to the RMS error.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`
>     * `FALSE`
> * **Recommendation**: Use the default, the maximum error provides a more reliable criterion.

!!! note "Note"
    The following variables are specific to SCF_ALGORITHM = DIIS_GDM.


### `MAX_DIIS_CYCLES`

> **The maximum number of DIIS iterations before switching to (geometric) direct minimization.**
>
> * **Type**: `INTEGER`
> * **Default**: `50`
> * **Options**:
>     * `1`: Only a single Roothaan step before switching to (G)DM
>     * $n$
>     * $n$: DIIS iterations before switching to (G)DM.
> * **Recommendation**: None

### `THRESH_DIIS_SWITCH`

> **The threshold for switching between DIIS extrapolation and direct minimization of the SCF energy is $10^{-\mbox{{\small THRESH\_DIIS\_SWITCH}}}$ .**
>
> * **Type**: `INTEGER`
> * **Default**: `2`
> * **Options**:
>     * `User-defined.`
> * **Recommendation**: None
