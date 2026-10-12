---
title: "7.7.2 Maximum Overlap Method"
---

## 7.7.2 Maximum Overlap Method

(July 4, 2026)

The Maximum Overlap Method (MOM) is a useful alternative to CIS and TDDFT for
obtaining low-cost excited states.[[443]](../bib_references/bib.md#bib455)
 It works by modifying
the orbital selection step in the SCF procedure. By choosing orbitals that
most resemble those from the previous cycle, rather than those with the lowest
eigenvalues, non-*aufbau*, excited-state SCF determinants can be determined,
in what has sometimes been called
*excited-state Kohn-Sham theory*.[[520]](../bib_references/bib.md#bib534)

This represents a form of “$\Delta$SCF” approach to computing excitation energies,

which has advantages over TDDFT is certain cases. For example, TDDFT exhibits systemic
problems with the description of charge-transfer and Rydberg excitations,

both of which can be modeled using the $\Delta$SCF approach. The use of MOM also allows the user
to easily target very high energy states, such as those
involving excitation of core electrons,[[118]](../bib_references/bib.md#bib113)
 which can be difficult
to capture using other excited state methods.

In order to calculate an excited state using MOM, the user must correctly
identify the orbitals involved in the transition. For example, in a
$\pi\rightarrow\pi^{\ast}$ transition, the $\pi$ and $\pi^{\ast}$ orbitals must be
identified and this usually requires a preliminary calculation. The user then
manipulates the orbital occupancies using the *$occupied* section, removing an
electron from the $\pi$ and placing it in the $\pi^{\ast}$. The MOM is then
invoked to preserve this orbital occupancy. The success of the MOM relies on
the quality of the initial guess for the calculation. If the virtual orbitals
are of poor quality then the calculation may ‘fall down’ to a lower energy
state of the same symmetry. Often the virtual orbitals of the corresponding
cation are more appropriate for using as initial guess orbitals for the excited state.

Because the MOM states are single determinants, all of **Q-Chem**’s existing
single determinant properties and derivatives are available. This allows, for
example, analytic harmonic frequencies to be computed on excited states. The
orbitals from a Hartree-Fock MOM calculation can also be used in an MP2
calculation. For all excited state calculations, it is important to add
diffuse functions to the basis set. This is particularly true if Rydberg
transitions are being sought. For DFT based methods, it is also advisable to
increase the size of the quadrature grid so that the more diffuse densities are
accurately integrated.

Due to its single-determinant description,
the MOM algorithm for unrestricted $\Delta$SCF calculations of open-shell singlets
is often badly spin contaminated.
Spin contamination can be alleviated by resorting to a
restricted open-shell Kohn-Sham (ROKS) formalism
(see Section [7.7.4](ex_ESROKS.md)),
in which the objective function $E_{\text{S}}=2E_{\text{M}}-E_{\text{T}}$
is optimized, where $E_{\text{S}}$ is the spin-pure singlet energy,
$E_{\text{M}}$ is the energy of the “mixed” (or spin-contaminated)
open-shell singlet state, and $E_{\text{T}}$ is the triplet energy.
MOM can be used in conjunction with ROKS to evaluate a spin-pure
energy for arbitrary open-shell singlet electron configurations
(formerly only $S_{1}$ was accessible within the ROKS formulation).

The MOM-based $\Delta$SCF method can be combined with a PCM based solvation
description for both equilibrium and nonequilibrium effects
(for more details see Section [7.7.9](sect_ROKS_neq-PCM.md)).

The following *$rem* is used to invoke the MOM:

### `MOM_START`

> **Determines when MOM is switched on to preserve orbital occupancies.**
>
> * **Type**: `INTEGER`
> * **Default**: `0 (FALSE)`
> * **Options**:
>     * `0 (FALSE)`: MOM is not used
>     * $n$: MOM begins on cycle
>     * $n$: .
> * **Recommendation**: For calculations on excited states, an initial calculation without MOM is usually required to get satisfactory starting orbitals. These orbitals should be read in setting SCF_GUESS = TRUE and = 1.

### `MOM_METHOD`

> **Determines the target orbitals with which to maximize the overlap on each SCF cycle.**
>
> * **Type**: `INTEGER`
> * **Default**: `MOM`
> * **Options**:
>     * `MOM`: Maximize overlap with the orbitals from the previous SCF cycle.
>     * `IMOM`: Maximize overlap with the initial guess orbitals.
> * **Recommendation**: If appropriate guess orbitals can be obtained, then IMOM can provide more reliable convergence to the desired solution. 75 Barca G. M. J., Gilbert A. T. B., Gill P. M. W. J. Chem. Theory Comput. (2018) , 14 , pp. 1501 . Link

???+ example "Example 7.46: Calculation of the lowest singlet state of CO."
    ```qchem
    $comment
       CO spin-purified calculation
       Step 1: prepare MOs
    $end
    
    $molecule
       0 1
       C
       O  C  1.05
    $end
    
    $rem
       METHOD            B3LYP
       BASIS             6-31G*
    $end
    
    @@@
    
    $comment
      Step 2: spin purification (OPSING=TRUE)
    $end
    
    $molecule
       read
    $end
    
    $rem
       METHOD            B3LYP
       BASIS             6-31G*
       SCF_GUESS         read
       MOM_START         1
       UNRESTRICTED      true
       OPSING            true
    $end
    
    $occupied
       1 2 3 4 5 6 7
       1 2 3 4 5 6 8
    $end
    ```

???+ example "Example 7.47: Input for obtaining the ${}^{2}$ A ${}^{\prime}$ excited state of formamide
corresponding to the $\pi\rightarrow\pi^{\ast}$ transition. The ${}^{1}$ A ${}^{\prime}$ ground state is obtained if MOM is not used in the second calculation. Note
the use of diffuse functions and a larger quadrature grid to accurately model
the larger excited state."
    ```qchem
    $molecule
       1  2
       C
       H  1  1.091480
       O  1  1.214713  2  123.10
       N  1  1.359042  2  111.98  3  -180.00
       H  4  0.996369  1  121.06  2    -0.00
       H  4  0.998965  1  119.25  2  -180.00
    $end
    
    $rem
       METHOD         B3LYP
       BASIS          6-311(2+,2+)G(d,p)
       XC_GRID        000100000194
    $end
    
    @@@
    
    $molecule
       0  1
       C
       H  1  1.091480
       O  1  1.214713  2  123.10
       N  1  1.359042  2  111.98  3  -180.00
       H  4  0.996369  1  121.06  2    -0.00
       H  4  0.998965  1  119.25  2  -180.00
    $end
    
    $rem
       METHOD         B3LYP
       BASIS          6-311(2+,2+)G(d,p)
       XC_GRID        000100000194
       MOM_START      1
       SCF_GUESS      read
       UNRESTRICTED   true
    $end
    
    $occupied
       1:12
       1:11 13
    $end
    ```

Additionally, it is possible to perform a CIS/TDDFT calculation on top of
the MOM excitation. This capability can be useful when modeling pump-probe
spectra. In order to run MOM followed by CIS/TDDFT, the *$rem* variable
CIS_N_ROOTS must be specified. Truncated subspaces may also be
used, see Section [7.3.3](subsec_TRNSS.md).

???+ example "Example 7.48: MOM valence excitation followed by core-state TDDFT using a restricted
subspace"
    ```qchem
    $molecule
       0 1
       O    0.0000    0.0000    0.1168
       H    0.0000    0.7629   -0.4672
       H    0.0000   -0.7629   -0.4672
    $end
    
    $rem
       METHOD       B3LYP
       BASIS        aug-cc-pvdz
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD         B3LYP
       BASIS          aug-cc-pvdz
       SCF_GUESS      read
       MOM_START      1
       UNRESTRICTED   true
       CIS_N_ROOTS    5
       TRNSS          true  ! use truncated subspace for TDDFT
       TRTYPE         3     ! specify occupied orbitals
       CUTVIR         15    ! truncate high energy virtual orbitals
       N_SOL          1     ! number core orbitals, specified in $solute section
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    $solute
       1
    $end
    
    $occupied
       1 2 3 4 5
       1 2 3 4 6
    $end
    ```

If the MOM excitation corresponds to a core hole, a reduced subspace must be
used to avoid de-excitations to the core hole. The *$rem* variable
CORE_IONIZE allows only the hole to be specified so that not all
occupied orbitals need to be entered in the *$solute* section.

### `CORE_IONIZE`

> **Indicates how orbitals are specified for reduced excitation spaces.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `1`: all valence orbitals are listed in $solute section
>     * `2`: only hole(s) are specified all other occupations same as ground state
> * **Recommendation**: For MOM + TDDFT this specifies the input form of the $solute section. If set to 1 all occupied orbitals must be specified, 2 only the empty orbitals to ignore must be specified.

???+ example "Example 7.49: O(1s) core excited state using MOM followed by excitations among valence
orbitals. Note that a reduced excitation subspace must be used to avoid
“excitations” into the empty core hole"
    ```qchem
    $molecule
       0 1
       O   0.0000   0.0000   0.1168
       H   0.0000   0.7629  -0.4672
       H   0.0000  -0.7629  -0.4672
    $end
    
    $rem
       METHOD       B3LYP
       BASIS        aug-cc-pvdz
       INTEGRAL_SYMMETRY    false
       POINT_GROUP_SYMMETRY false
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       METHOD            B3LYP
       BASIS             aug-cc-pvdz
       SCF_GUESS         read
       MOM_START         1
       UNRESTRICTED      true
       CIS_N_ROOTS       5
       TRNSS             true  ! use truncated subspace for TDDFT
       TRTYPE            3     ! specify occupied orbitals
       N_SOL             1     ! number core holes, specified in $solute section
       CORE_IONIZE       2     ! hole orbital specified
       INTEGRAL_SYMMETRY false
       POINT_GROUP_SYMMETRY false
    $end
    
    $solute
       6
    $end
    
    $occupied
       1 2 3 4 5
       2 3 4 5 6
    $end
    ```
