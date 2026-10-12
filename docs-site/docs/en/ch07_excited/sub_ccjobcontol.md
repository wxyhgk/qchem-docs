---
title: "7.9.18 EOM-CC Job Control"
---

## 7.9.18 EOM-CC Job Control

(July 4, 2026)

It is important to ensure there are sufficient resources available for the
necessary integral calculations and transformations. For CCMAN/CCMAN2
algorithms, these resources are controlled using the *$rem* variables
CC_MEMORY, MEM_STATIC and MEM_TOTAL (see
Section [6.17](../ch06_correlation/CCparallel.md)).

The exact flavor of correlation treatment within EOM methods is
defined by METHOD (see Section [7.1](sect_ExStatesSummary.md)). For
EOM-CCSD, once should set METHOD to EOM-CCSD,
for CC2,METHOD = EOM-CC2,
for EOM-MP2,
METHOD = EOM-CCSD, *etc.*. In addition, a specification of
the number of *target states* is required through XX_STATES (XX
designates the type of the target states, *e.g.*, EE, SF, IP, EA, DIP, DSF,
*etc.*). Users must be aware of the point group symmetry of the system being
studied and also the symmetry of the initial and target states of interest, as
well as symmetry of transition. It is possible to turn off the use of symmetry
by CC_SYMMETRY. If set to FALSE the molecule will be treated
as having $C_{1}$ symmetry and all states will be of $A$ symmetry.

**Note: 

Only Abelian groups are supported; USE_ABELIAN_SUBGROUP
must be set to TRUE for all CCMAN and CCMAN2 jobs (it is set by default).
**

**Note: 

1.

In finite-difference calculations, the symmetry is turned off
automatically, and the user must ensure that XX_STATES is
adjusted accordingly.

2.

In CCMAN2, different types of
target states can be requested in a single calculation.
In CCMAN, mixing different EOM models in a single calculation is only
allowed in Dyson orbitals calculations.

**

Below we describe alternative way to specify correlation treatment in EOM-CC/CI
calculations. These keywords will be eventually phased out. By default, the
level of correlation of the EOM part of the wave function (*i.e.*, maximum
excitation level in the EOM operators $R$) is set to match
CORRELATION, however, one can mix different correlation levels for the
reference and EOM states by using EOM_CORR. To request a CI
calculation, set CORRELATION = CI and select type of CI expansion by
EOM_CORR. The table below shows default and allowed
CORRELATION and EOM_CORR combinations.

| CORRELATION | Default | Allowed | Target states | CCMAN / |
| --- | --- | --- | --- | --- |
|  | EOM_CORR | EOM_CORR |  | CCMAN2 |
| CI | none | CIS, CIS(D) | EE, SF | y/n |
|  |  | CISD | EE, SF, IP | y/n |
|  |  | SDT, DT | EE, SF, DSF | y/n |
| CIS(D) | CIS(D) | N/A | EE, SF | y/n |
| CCSD, OD | CISD |  | EE, SF, IP, EA, DIP | y/y |
|  |  | SD(fT) | EE, IP, EA | n/y |
|  |  | SD(dT), SD(fT) | EE, SF, fake IP/EA | y/n |
|  |  | SD(dT), SD(fT), SD(sT) | IP | y/n |
|  |  | SDT, DT | EE, SF, IP, EA, DIP, DSF | y/n |

Table 7.1: Default and allowed CORRELATION and EOM_CORR
combinations as well as valid target state types. The last column shows if a
method is available in CCMAN or CCMAN2.

Table [7.2](#table:EOMCI) shows the correct combinations of CORRELATION
and EOM_CORR for standard EOM and CI models.

| Method | CORRELATION | EOM_CORR | Target states selection |
| --- | --- | --- | --- |
| CIS | CI | CIS | EE_STATES |
|  |  |  | EE_SINGLETS , EE_TRIPLETS |
| SF-CIS | CI | CIS | SF_STATES |
| CIS(D) | CI | CIS(D) | EE_STATES |
|  |  |  | EE_SINGLETS , EE_TRIPLETS |
| SF-CIS(D) | CI | CIS(D) | SF_STATES |
| CISD | CI | CISD | EE_STATES |
|  |  |  | EE_SINGLETS , EE_TRIPLETS |
| SF-CISD | CI | CISD | SF_STATES |
| IP-CISD | CI | CISD | IP_STATES |
| CISDT | CI | SDT | EE_STATES |
|  |  |  | EE_SINGLETS , EE_TRIPLETS |
| SF-CISDT | CI | SDT or DT | SF_STATES |
| EOM-EE-CCSD | CCSD |  | EE_STATES |
|  |  |  | EE_SINGLETS , EE_TRIPLETS |
| EOM-SF-CCSD | CCSD |  | SF_STATES |
| EOM-IP-CCSD | CCSD |  | IP_STATES |
| EOM-EA-CCSD | CCSD |  | EA_STATES |
| EOM-DEA-CCSD | CCSD |  | DIP_STATES |
|  |  |  | DEA_SINGLETS , DEA_TRIPLETS |
| EOM-DIP-CCSD | CCSD |  | DIP_STATES |
|  |  |  | DIP_SINGLETS , DIP_TRIPLETS |
| EOM-2SF-CCSD | CCSD | SDT or DT | DSF_STATES |
| EOM-EE-(2,3) | CCSD | SDT | EE_STATES |
|  |  |  | EE_SINGLETS , EE_TRIPLETS |
| EOM-SF-(2,3) | CCSD | SDT | SF_STATES |
| EOM-IP-(2,3) | CCSD | SDT | IP_STATES |
| EOM-SF-CCSD(dT) | CCSD | SD(dT) | SF_STATES |
| EOM-SF-CCSD(fT) | CCSD | SD(fT) | SF_STATES |
| EOM-IP-CCSD(dT) | CCSD | SD(dT) | IP_STATES |
| EOM-IP-CCSD(fT) | CCSD | SD(fT) | IP_STATES |
| EOM-IP-CCSD(sT) | CCSD | SD(sT) | IP_STATES |

Table 7.2: Commonly used EOM and CI models. “SINGLETS” and “TRIPLETS” are only
available for closed-shell references.

The most relevant EOM-CC input options follow.

### `EE_STATES`

> **Sets the number of excited state roots to find. For closed-shell reference, defaults into EE_SINGLETS . For open-shell references, specifies all low-lying states.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ excited states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `EE_SINGLETS`

> **Sets the number of singlet excited state roots to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ excited states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `EE_TRIPLETS`

> **Sets the number of triplet excited state roots to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ excited states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `SF_STATES`

> **Sets the number of spin-flip target states roots to find.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ SF states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DSF_STATES`

> **Sets the number of doubly spin-flipped target states roots to find.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ doubly spin-flipped states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `IP_STATES`

> **Sets the number of ionized target states roots to find. By default, $\beta$ electron will be removed (see EOM_IP_BETA ).**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ ionized states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `IP_ALPHA`

> **Sets the number of ionized target states derived by removing $\alpha$ electron ( $M_{S}=\tfrac{1}{2}$ ).**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ ionized states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `IP_BETA`

> **Sets the number of ionized target states derived by removing $\beta$ electron ( $M_{S}=\tfrac{1}{2}$ , default for EOM-IP).**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ ionized states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `EA_STATES`

> **Sets the number of attached target states roots to find. By default, $\beta$ electron will be attached (see EA_BETA ).**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ EA states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `EA_ALPHA`

> **Sets the number of attached target states derived by attaching $\alpha$ electron ( $M_{S}=\tfrac{1}{2}$ , default in EOM-EA).**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ EA states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `EA_BETA`

> **Sets the number of attached target states derived by attaching $\beta$ electron ( $M_{S}=\tfrac{1}{2}$ , EA-SF).**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ EA states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DIP_STATES`

> **Sets the number of DIP roots to find. For closed-shell reference, defaults into DIP_SINGLETS . For open-shell references, specifies all low-lying states.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DIP states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DIP_SINGLETS`

> **Sets the number of singlet DIP roots to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DIP singlet states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DIP_TRIPLETS`

> **Sets the number of triplet DIP roots to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DIP triplet states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DIP_AA_STATES`

> **Sets the number of $M_{S}=-1$ DIP roots (remove two $\alpha$ electrons) to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DIP states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DIP_BB_STATES`

> **Sets the number of $M_{S}=+1$ DIP roots (remove two $\beta$ electrons) to find.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DIP states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DIP_AB_STATES`

> **Sets the number of $M_{S}=0$ DIP roots (remove one $\alpha$ and one $\beta$ electron) to find.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DIP states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DEA_STATES`

> **Sets the number of DEA roots to find. For closed-shell reference, defaults into DEA_SINGLETS . For open-shell references, specifies all low-lying states.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DIP states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DEA_SINGLETS`

> **Sets the number of singlet DEA roots to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DEA singlet states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DEA_TRIPLETS`

> **Sets the number of triplet DEA roots to find. Valid only for closed-shell references.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DEA triplet states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DEA_AA_STATES`

> **Sets the number of $M_{S}=1$ DEA roots (two $\alpha$ electrons) to find.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DEA $\alpha\alpha$ states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DEA_BB_STATES`

> **Sets the number of $M_{S}=-1$ DEA roots (two $\beta$ electrons) to find.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DEA $\beta\beta$ states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

### `DEA_AB_STATES`

> **Sets the number of $M_{S}=0$ DEA roots (one $\alpha$ and one $\beta$ electron) to find.**
>
> * **Type**: `INTEGER/INTEGER ARRAY`
> * **Default**: `0`
> * **Options**:
>     * $[i,j,k\ldots]$: Find $i$ DEA $\alpha\beta$ states in the first irrep, $j$ states in the second irrep etc.
> * **Recommendation**: None

**Note: 

It is a symmetry of a *transition* rather than that of a *target
state* which is specified in excited state calculations. The symmetry of the
target state is a product of the symmetry of the reference state and the
transition. For closed-shell molecules, the former is fully symmetric and the
symmetry of the target state is the same as that of transition, however, for
open-shell references this is not so.
**

**Note: 

In earlier versions of **Q-Chem**, we used EOM_XX_STATES. These keywords were replaced by XX_STATES for uniformity (e.g., they are also used in ADC methods to specify target ADC states).
For backward compatibility,
the old keywords are aliased to the new ones, so old inputs would still work.
However, these old keywords eventually will be depreciated. It is recommended
to switch to the new ones.
**

**Note: 

For the XX_STATES options, **Q-Chem** will increase the number of
roots if it suspects degeneracy, or change it to a smaller value, if it cannot
generate enough guess vectors to start the calculations.
**

### `EOM_FAKE_IPEA`

> **If TRUE , calculates fake EOM-IP or EOM-EA energies and properties using the diffuse orbital trick. Default for EOM-EA and Dyson orbital calculations in CCMAN.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE (use proper EOM-IP code)`
> * **Options**:
>     * `FALSE, TRUE`
> * **Recommendation**: None. This feature only works for CCMAN.

**Note: 

When EOM_FAKE_IPEA is set to TRUE, it can change the
convergence of Hartree-Fock iterations compared to the same job without
EOM_FAKE_IPEA, because a very diffuse basis function is added to a
center of symmetry *before* the Hartree-Fock iterations start. For the
same reason, BASIS2 keyword is incompatible with
EOM_FAKE_IPEA. In order to read Hartree-Fock guess from a previous
job, you must specify EOM_FAKE_IPEA (even if you do not request for
any correlation or excited states) in that previous job. Currently, the second
moments of electron density and Mulliken charges and spin densities are
incorrect for the EOM-IP/EA-CCSD target states.
**

### `EOM_USER_GUESS`

> **Specifies if user-defined guess will be used in EOM calculations.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `TRUE`: Solve for a state that has maximum overlap with a trans-n specified in $eom_user_guess .
> * **Recommendation**: The orbitals are ordered by energy, as printed in the beginning of the CCMAN2 output. Not available in CCMAN.

### `EOM_SHIFT`

> **Specifies energy shift in EOM calculations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: corresponds to $n\cdot 10^{-3}$ Hartree shift ( i.e. , 11000 = 11 Hartree); solve for eigenstates around this value.
> * **Recommendation**: Not available in CCMAN.

### `EOM_NGUESS_DOUBLES`

> **Specifies number of excited state guess vectors which are double excitations.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Include
>     * $n$: guess vectors that are double excitations
> * **Recommendation**: This should be set to the expected number of doubly excited states, otherwise they may not be found.

### `EOM_NGUESS_SINGLES`

> **Specifies number of excited state guess vectors that are single excitations.**
>
> * **Type**: `INTEGER`
> * **Default**: `Equal to the number of excited states requested`
> * **Options**:
>     * $n$: Include
>     * $n$: guess vectors that are single excitations
> * **Recommendation**: Should be greater or equal than the number of excited states requested, unless .

### `EOM_PRECONV_SINGLES`

> **When not zero, singly excited vectors are converged prior to a full excited states calculation. Sets the maximum number of iterations for pre-converging procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: do not pre-converge
>     * `1`: pre-converge singles
> * **Recommendation**: Sometimes helps with problematic convergence.

**Note: 

In CCMAN, setting EOM_PRECONV_SINGLES = $N$ would result in $N$
Davidson iterations pre-converging singles.
**

### `EOM_PRECONV_DOUBLES`

> **When not zero, doubly excited vectors are converged prior to a full excited states calculation. Sets the maximum number of iterations for pre-converging procedure**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: Do not pre-converge
>     * `N`: Perform N Davidson iterations pre-converging doubles.
> * **Recommendation**: Occasionally necessary to ensure a doubly excited state is found. Also used in DSF, DIP, and DEA calculations instead of EOM_PRECONV_SINGLES

**Note: 

Not available for EOM-EE in CCMAN2.
**

### `EOM_PRECONV_SD`

> **When not zero, EOM vectors are pre-converged prior to a full excited states calculation. Sets the maximum number of iterations for pre-converging procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: do not pre-converge
>     * `N`: perform N Davidson iterations pre-converging singles and doubles.
> * **Recommendation**: Occasionally necessary to ensure that all low-lying states are found. Also, very useful in EOM(2,3) calculations. None

**Note: 

Not available in CCMAN2.
**

### `EOM_DAVIDSON_CONVERGENCE`

> **Convergence criterion for the RMS residuals (square of the norm) of excited-state vectors.**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: Corresponding to $10^{-n}$ convergence criterion
> * **Recommendation**: Use the default. Normally this value be the same as EOM_DAVIDSON_THRESHOLD .

### `EOM_DAVIDSON_THRESHOLD`

> **Specifies threshold for including a new expansion vector in the iterative Davidson diagonalization. Their norm must be above this threshold.**
>
> * **Type**: `INTEGER`
> * **Default**: `00103`
> * **Options**:
>     * $abcde$: Integer code is mapped to $abc\times 10^{-(de+2)}$ , i.e. , 02505->2.5 $\times 10^{-6}$
> * **Recommendation**: Use the default unless converge problems are encountered. Should normally be set to the same values as EOM_DAVIDSON_CONVERGENCE , if convergence problems arise try setting to a value slightly larger than EOM_DAVIDSON_CONVERGENCE .

### `EOM_DAVIDSON_MAXVECTORS`

> **Specifies maximum number of vectors in the subspace for the Davidson diagonalization.**
>
> * **Type**: `INTEGER`
> * **Default**: `60`
> * **Options**:
>     * $n$: Up to
>     * $n$: vectors per root before the subspace is reset
> * **Recommendation**: Larger values increase disk storage but accelerate and stabilize convergence.

### `EOM_DAVIDSON_MAX_ITER`

> **Maximum number of iteration allowed for Davidson diagonalization procedure.**
>
> * **Type**: `INTEGER`
> * **Default**: `30`
> * **Options**:
>     * $n$: User-defined number of iterations
> * **Recommendation**: Default is usually sufficient

### `EOM_DIIS_CONVERGENCE`

> **Convergence criterion for the DIIS algorithm for solving for real-valued EOM states (only for RI-CC2 in LIBGMBPT).**
>
> * **Type**: `INTEGER`
> * **Default**: `5`
> * **Options**:
>     * $n$: Corresponding to $10^{-n}$ convergence criterion.
> * **Recommendation**: A loose convergence criterion may result in finding an incorrect state.

### `EOM_DIIS_MAXVECTORS`

> **Specifies maximum size of the DIIS subspace (only for RI-CC2 in LIBGMBPT).**
>
> * **Type**: `INTEGER`
> * **Default**: `7`
> * **Options**:
>     * $n$: Up to
>     * $n$: vectors in the DIIS subspace.
> * **Recommendation**: Larger values increase disk storage but accelerate and stabilize convergence.

### `EOM_DIIS_MAX_ITER`

> **Maximum number of iteration allowed for DIIS procedure (only for RI-CC2 in LIBGMBPT).**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$: User-defined number of iterations.
> * **Recommendation**: Default is usually sufficient.

### `EOM_IPEA_FILTER`

> **If TRUE , filters the EOM-IP/EA amplitudes obtained using the diffuse orbital implementation (see EOM_FAKE_IPEA ). Helps with convergence.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE (EOM-IP or EOM-EA amplitudes will not be filtered)`
> * **Options**:
>     * `FALSE, TRUE`
> * **Recommendation**: None

**Note: 

Not available in CCMAN2.
**

### `CC_FNO_THRESH`

> **Initialize the FNO truncation and sets the threshold to be used for both cutoffs (OCCT and POVO).**
>
> * **Type**: `INTEGER`
> * **Default**: `None`
> * **Options**:
>     * `range`: 0000-10000 $abcd$ Corresponding to $ab.cd$ %
> * **Recommendation**: None

### `CC_FNO_USEPOP`

> **Selection of the truncation scheme.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `0`: POVO
> * **Recommendation**: None

### `SCALE_NUCLEAR_CHARGE`

> **Scales charge of each nuclei by a certain value. The nuclear repulsion energy is calculated for the unscaled nuclear charges.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: A total positive charge of (1+ $n/100$ )e is added to the molecule.
> * **Recommendation**: NONE

### `ADD_CHARGED_CAGE`

> **Add a point charge cage of a given radius and total charge.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: No cage.
>     * `1`: Dodecahedral cage.
>     * `2`: Spherical cage.
> * **Recommendation**: Spherical cage is expected to yield more accurate results, especially for small radii.

### `CAGE_RADIUS`

> **Defines radius of the charged cage.**
>
> * **Type**: `INTEGER`
> * **Default**: `225`
> * **Options**:
>     * $n$: radius is $n/100$ Å.
> * **Recommendation**: None

### `CAGE_POINTS`

> **Defines number of point charges for the spherical cage.**
>
> * **Type**: `INTEGER`
> * **Default**: `100`
> * **Options**:
>     * $n$: Number of point charges to use.
> * **Recommendation**: None

### `CAGE_CHARGE`

> **Defines the total charge of the cage.**
>
> * **Type**: `INTEGER`
> * **Default**: `400`
> * **Options**:
>     * $n$: Total charge of the cage is $n/100$ a.u.
> * **Recommendation**: None

### `EOM_EE_IV_PROJ`

> **Enables the application of the inner-valence projector when computing excited states using EOM-EE-CCSD**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Number of active occupied orbitals that are used to construct the inner-valence projector. The orbitals are counted from the bottom, with frozen orbitals excluded from the count.
> * **Recommendation**: none

### `EOM_IP_IV_PROJ`

> **Enables the application of the inner-valence projector when computing ionized states using EOM-IP-CCSD**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * $n$: Number of active occupied orbitals that are used to construct the inner-valence projector. The orbitals are counted from the bottom, with frozen orbitals excluded from the count.
> * **Recommendation**: none
