---
title: "7.7.4 Restricted Open-Shell Kohn-Sham Method"
---

## 7.7.4 Restricted Open-Shell Kohn-Sham Method

(July 4, 2026)

Singly-excited states of closed-shell molecules cannot be described via a
single non-*aufbau* filled Slater determinant as both the up and down spins are
equally likely to be excited, leading to at least two configurations with equal
weights. Triplet energies can nonetheless be found from a single determinant
by switching from the $M_{S}=0$ subspace of the ground state to $M_{S}=\pm 1$
(*i.e.*, by having both unpaired electrons have spins pointing in the same direction
instead of having one up and one down spin). This tactic however does not work
on singlet excited states, with non-*aufbau* filled configurations where only the
up (or down) spin is excited being intermediate between singlet and triplet
(and thus spin contaminated). This mixed state is not unlike spin-symmetry
broken, unrestricted ground state solutions. An actual singlet energy can be
obtained via approximate spin-purification post SCF, by removing the triplet
contribution to the energy. The triplet energy thus has to be separately
estimated with a second orbital optimization.

The *restricted open-shell Kohn-Sham* (ROKS) method offers an alternative route to singlet
excited states of this nature. The mixed non-*aufbau* configuration (with either
the up or down spin being excited) is exactly halfway between a singlet and
triplet when restricted open-shell orbitals are used, and has an energy
$E_{\text{mix}}$. The triplet energy $E_{\text{T}}$ is also computable from a single
determinant within the the $M_{S}=\pm 1$ subspaces. Consequently, ROKS optimizes
a set of spin-restricted orbitals $\{\phi_{\text{ROKS}}\}$ such that the spin-purified
singlet energy,

<a id="Ch7.E79"></a>

$$
E_{\text{S}}=2E_{\text{mix}}[\{\phi_{\text{ROKS}}\}]-E_{\text{T}}[\{\phi_{\text{ROKS}}\}]\;, \tag{7.79}
$$

is stationary. This therefore needs only one orbital optimization, in contrast to
the two sets needed for the $\Delta$SCF approach mentioned in the preceding
paragraph. The structure of the ROKS Fock matrix however is more complex,
by virtue of the two-determinant nature of the equations.[[579]](../bib_references/bib.md#bib600)

It is also important to note that this excited-state method is
distinct from ROKS theory for open-shell ground states, which is a single-determinant method
corresponding to the high-spin state with multiple unpaired spins.

The implementation of ROKS excited states in **Q-Chem** largely follows the
theoretical framework established by Filatov and Shaik;[[388]](../bib_references/bib.md#bib396)

see Ref. [[714]](../bib_references/bib.md#bib746)
 for the case of the
lowest excited singlet ($S_{1}$ state) with a DIIS-based approach. An example is provided below.
ROKS for higher excited states is possible using either the squared-gradient approach
(Section [7.7.5](ex_BEDSCF.md)),
the maximum overlap method (Section [7.7.2](ex_OpSing.md)),
or else state-targeted energy projection (Section [7.7.8](ex_ROSTEP.md)).

ROKS has been found to be significantly more accurate than TDDFT for describing
charge-transfer states,[[513]](../bib_references/bib.md#bib523)
 and preliminary evidence
shows the same to hold for Rydberg states. ROKS is also extremely accurate for
core excitation energies, with the SCAN functional yielding errors below 0.5 eV
for both K- and L-edge excitations of small molecules.[[510]](../bib_references/bib.md#bib525)

Examples of using ROKS/SGM to compute core-excited states are provided in
Section [7.7.5](ex_BEDSCF.md). Analytic nuclear gradients (in the excited state) are
also available, enabling geometry optimization and molecular dynamics
calculations as well, along with finite-difference frequency calculations.
Users of the ROKS code are requested to cite Ref. [[714]](../bib_references/bib.md#bib746)
, and in addition
Ref. [[511]](../bib_references/bib.md#bib526)
 if the SGM implementation is
employed, as well as Ref. [[513]](../bib_references/bib.md#bib523)
 for charge-transfer states and
Ref. [[510]](../bib_references/bib.md#bib525)
 for application to core excitations.

The chief limitation of ROKS is that it can only describe states with one
broken electron pair. It is consequently applicable only to certain excited
states of closed-shell systems: all singlet single excitations well-described
by a single natural transition orbital (NTO) pair, or higher singlets where
only one electron pair is broken in total (like the ${}^{1}$B${}_{3g}$ doubly
excited state of tetrazine). Fortunately, most charge-transfer and
core-excitations do not require more than one broken electron pair, and so this
limitation is not a major problem in practice.

Furthermore, ROKS often suffers from an unphysical mixing between the open-shell
orbitals when they belong to the same spatial symmetry, which often manifests in
$\pi\to\pi^{\ast}$ and $1s\to 3s$ excitations.[[408]](../bib_references/bib.md#bib417)

This is associated with the inherent ambiguity
in defining an effective Fock operator for a two-determinant wave
function.[[579]](../bib_references/bib.md#bib600)
 Convergence is often difficult for the states where
this mixing manifests, and the overlap with the ground state may be significant.
Two protocols can be used to alleviate this issue. The first is a level-shift technique
that splits the energy between the two singly-occupied orbitals thereby
supressing their mixing.[[714]](../bib_references/bib.md#bib746)
 It is only available with DIIS and
for the ROKS implementation on the old SCF engine (GEN_SCFMAN = FALSE).
The second is a total supression of the mixing between the singly-occupied orbitals.
While this may disregard the correct variational condition,[[579]](../bib_references/bib.md#bib600)
 it
produces excited states with much smaller overlaps with the ground state and provides
smoother convergence. See Example 7.7.4 for a demonstration.

To perform an ROKS excited state calculation, simply set the keyword
ROKS = TRUE and ensure that UNRESTRICTED = FALSE.
It is recommended to perform a preliminary ground-state calculation on the system
first, and then use the ground-state orbitals to construct the initial guess
using SCF_GUESS = READ. Transition dipole moments between two
arbitrary configurations (normally the ground state and an excited state computed
with either $\Delta$SCF or ROKS) can be computed by setting TRANS_MOM_SAVE =
TRUE on the calculation of the initial state and TRANS_MOM_READ =
TRUE on the calculation of the final state. The non-orthogonality of
the orbital bases is accounted for.

### `ROKS`

> **Controls whether ROKS calculation will be performed.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: ROKS is not performed.
>     * `TRUE`: ROKS will be performed.
> * **Recommendation**: Set to TRUE if ROKS calculation is desired. Make sure that UNRESTRICTED is not set to TRUE .

### `ROKS_LEVEL_SHIFT`

> **Introduce a level shift of $N$ /100 hartree to aid DIIS convergence.**
>
> * **Type**: `INTEGER`
> * **Default**: `0`
> * **Options**:
>     * `0`: No shift $N$ level shift of $N$ /100 hartree.
> * **Recommendation**: Use in cases of problematic DIIS convergence. Only available for the ROKS implementation on the old SCF engine ( GEN_SCFMAN = FALSE ).

### `ROKS_SS_MIXING`

> **Allow coupling between the two singly-occupied molecular orbitals.**
>
> * **Type**: `INTEGER`
> * **Default**: `1`
> * **Options**:
>     * `0`: Supress coupling.
>     * `1`: Allow coupling.
> * **Recommendation**: Supress coupling when the resuling states are difficult to converge and / or overlap significantly with the ground state. Only for GDM and SGM-based solvers.

### `TRANS_MOM_SAVE`

> **Save orbitals for a subsequent transition dipole calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Dont save orbitals.
>     * `TRUE`: Save orbitals.
> * **Recommendation**: Saves the orbitals of the calculation for which this variable is set. It usually would be the ground state calculation but it could be any restricted SCF, unrestricted SCF, or ROKS calculation, which allows computing general inter-state transition dipoles.

### `TRANS_MOM_READ`

> **Read previously-saved reference orbitals and compute transition dipole with orbitals from current calculation.**
>
> * **Type**: `LOGICAL`
> * **Default**: `FALSE`
> * **Options**:
>     * `FALSE`: Don’t read orbitals.
>     * `TRUE`: Read orbitals.
> * **Recommendation**: It assumes that a set of orbitals was previously saved with TRANS_MOM_SAVE . If so, reads said orbitals and computes the transition dipole moment with the orbitals of the current calculation.

???+ example "Example 7.50: RO-PBE0/6-311+G* excited state gradient of formaldehyde, using the ground
state orbitals as an initial guess. This used the DIIS based implementation of Ref 714 Kowalczyk T. et al. J. Chem. Phys. (2013) , 138 , pp. 164101 . Link ."
    ```qchem
    $comment
       ROKS excited state gradient of formaldehyde
       Use orbitals from ground state for initial guess
    $end
    
    $rem
       EXCHANGE          pbe0
       BASIS             6-311+G*
       SCF_CONVERGENCE   9
    point_group_symmetry False
    $end
    
    $molecule
       0 1
       H      -0.940372    0.000000    1.268098
       H       0.940372    0.000000    1.268098
       C       0.000000    0.000000    0.682557
       O       0.000000    0.000000   -0.518752
    $end
    
    @@@
    
    $molecule
       read
    $end
    
    $rem
       ROKS              true
       UNRESTRICTED      false
       EXCHANGE          pbe0
       BASIS             6-311+G*
       JOBTYPE           force
       SCF_CONVERGENCE   9
    point_group_symmetry False
       SCF_GUESS         read
    $end
    ```

???+ example "Example 7.51: ROKS calculation on the lowest $\pi\to\pi^{\ast}$ excited state of acetone
using $\omega$ B97X-D/STO-3G. To observe the mixing of the open shells, as well as the
effect of mixing suppression, try running this example with ROKS_SS_MIXING set to
TRUE/FALSE."
    ```qchem
    $comment
      Plain old SCF on the ground state.
    $end
    
    $molecule
      0   1
      C   0.00000000      0.00000000      0.18807702
      C   0.00000000      2.42007545     -1.31764698
      C   0.00000000     -2.42007545     -1.31764698
      O   0.00000000      0.00000000      2.48269094
      H   0.00000000      4.03690733     -0.05185132
      H   0.00000000     -4.03690733     -0.05185132
      H   1.66061256      2.48420530     -2.53995285
      H  -1.66061256      2.48420530     -2.53995285
      H   1.66061256     -2.48420530     -2.53995285
      H  -1.66061256     -2.48420530     -2.53995285
    $end
    
    $rem
      METHOD               WB97X-D
      UNRESTRICTED         FALSE
      BASIS                STO-3G
      INPUT_BOHR           TRUE
      INTEGRAL_SYMMETRY    FALSE
      POINT_GROUP_SYMMETRY TRUE
      GEN_SCFMAN           TRUE
      SCF_ALGORITHM        DIIS_GDM
      SCF_CONVERGENCE      8
      MAX_SCF_CYCLES       200
      MEM_TOTAL            1000
      MEM_STATIC           100
      THRESH               14
    $end
    
    @@@
    
    $comment
      Plain old SCF on the ground state with UNRESTRICTED = TRUE
      to enable TRANS_MOM_SAVE.
    $end
    
    $molecule
      read
    $end
    
    $rem
      METHOD               WB97X-D
      UNRESTRICTED         TRUE
      BASIS                STO-3G
      INPUT_BOHR           TRUE
      INTEGRAL_SYMMETRY    FALSE
      POINT_GROUP_SYMMETRY TRUE
      SYM_IGNORE           TRUE
      GEN_SCFMAN           TRUE
      SCF_GUESS            READ
      SCF_ALGORITHM        DIIS
      SCF_CONVERGENCE      10
      MAX_SCF_CYCLES       200
      TRANS_MOM_SAVE       1
      MEM_TOTAL            1000
      MEM_STATIC           100
      THRESH               14
    $end
    
    @@@
    
    $comment
      ROKS calculation targeting the \pi -> \pi^{*} state. Attempt
      to run this calculation with ROKS_SS_MIXING = TRUE to see
      what happens.
    $end
    
    $molecule
      read
    $end
    
    $rem
      METHOD               WB97X-D
      UNRESTRICTED         FALSE
      ROKS                 TRUE
      ROKS_SS_MIXING       FALSE
      BASIS                STO-3G
      INPUT_BOHR           TRUE
      INTEGRAL_SYMMETRY    FALSE
      POINT_GROUP_SYMMETRY TRUE
      GEN_SCFMAN           TRUE
      SCF_GUESS            READ
      SCF_ALGORITHM        GDM
      SCF_CONVERGENCE      7
      MAX_SCF_CYCLES       1000
      TRANS_MOM_READ       2
      THRESH               14
      MEM_STATIC           100
      MEM_TOTAL            1000
    $end
    
    $reorder_mo
      1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 15 17
      1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 15 17
    $end
    
    ```
